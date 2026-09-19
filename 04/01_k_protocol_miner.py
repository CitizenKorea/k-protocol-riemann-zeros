#!/usr/bin/env python3
# ==============================================================================
# K-Protocol: Autonomous Theory-Driven Screening Engine (Ranked by Isolation Metric)
# ==============================================================================

import argparse
from dataclasses import asdict, dataclass
from itertools import product
import json
import logging
import os
import sys
from typing import Any, Dict, List, Set

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("KProtocolMiner")


@dataclass(frozen=True)
class CandidateCompound:
  id: int
  formula: str
  target_orbital: str
  isolation_score: float  # Phi_2D = (c/a) * (r_Y / r_X)
  c_over_a: float
  anion_ratio: float
  lattice_a: float
  lattice_c: float
  space_group: str = "I4/mmm (No. 139)"


class CrystalChemistryDB:
  RADII: Dict[str, float] = {
      "Sr2+": 1.44,
      "Ba2+": 1.61,
      "Ca2+": 1.34,
      "La3+": 1.36,
      "Y3+": 1.18,
      "K1+": 1.64,
      "Rb1+": 1.72,
      "Cs1+": 1.88,
      "Cu2+": 0.730,  # 3d9
      "Ni1+": 0.690,  # 3d9
      "Ti3+": 0.670,  # 3d1
      "V4+": 0.580,  # 3d1
      "O2-": 1.40,
      "Cl1-": 1.81,
      "Br1-": 1.96,
      "I1-": 2.20,
  }

  ORBITAL_CONFIGS: Dict[str, str] = {
      "Cu2+": "3d9 (Cuprate-analog Hole)",
      "Ni1+": "3d9 (Nickelate Hole-pocket)",
      "Ti3+": "3d1 (Titanate Electron-pocket)",
      "V4+": "3d1 (Vanadate Electron-pocket)",
  }


class KProtocolBatchMiner:

  def __init__(
      self,
      master_db_path: str = "k_protocol_master_db.json",
      qe_output_dir: str = "./qe_calculations",
      min_anion_ratio: float = 1.25,
      min_c_over_a: float = 3.60,
  ):
    self.master_db_path = master_db_path
    self.qe_output_dir = qe_output_dir
    self.min_anion_ratio = min_anion_ratio
    self.min_c_over_a = min_c_over_a
    self.existing_db: List[Dict[str, Any]] = []
    self.existing_formulas: Set[str] = set()
    self._load_master_database()

  def _load_master_database(self) -> None:
    if os.path.exists(self.master_db_path):
      try:
        with open(self.master_db_path, "r", encoding="utf-8") as f:
          self.existing_db = json.load(f)
        self.existing_formulas = {item["formula"] for item in self.existing_db}
        logger.info(
            f"Loaded {len(self.existing_db)} records from"
            f" '{self.master_db_path}'."
        )
      except Exception:
        self.existing_db = []
        self.existing_formulas = set()

  def run_mining(
      self, batch_size: int = 100, generate_qe_cards: bool = True
  ) -> List[CandidateCompound]:
    A_pool_2p = ["Sr", "Ba", "Ca"]
    A_pool_3p = ["La", "Y"]
    A_pool_1p = ["K", "Rb", "Cs"]
    M_pool = [("Cu", 2), ("Ni", 1), ("Ti", 3), ("V", 4)]
    X_pool = [("O", -2)]
    Y_pool = [("Cl", -1), ("Br", -1), ("I", -1)]

    discovered_pool: List[Dict[str, Any]] = []

    # Combinatorial generation across strict neutral stoichiometry
    for (m_sym, m_val), (x_sym, x_val), (y_sym, y_val) in product(
        M_pool, X_pool, Y_pool
    ):
      req_A = 6 - m_val

      if req_A % 2 == 0:
        val = req_A // 2
        a_list = A_pool_2p if val == 2 else A_pool_1p
        for a_sym in a_list:
          formula = f"{a_sym}2{m_sym}{x_sym}2{y_sym}2"
          r_a = CrystalChemistryDB.RADII[f"{a_sym}{val}+"]
          cand = self._eval(
              formula, a_sym, a_sym, val, val, m_sym, m_val, x_sym, y_sym, r_a
          )
          if cand["valid"]:
            discovered_pool.append(cand)
      else:
        pairs = (
            product(A_pool_3p, A_pool_2p)
            if req_A == 5
            else product(A_pool_1p, A_pool_2p)
        )
        v1, v2 = (3, 2) if req_A == 5 else (1, 2)
        for a1, a2 in pairs:
          formula = f"{a1}{a2}{m_sym}{x_sym}2{y_sym}2"
          r_a = (
              CrystalChemistryDB.RADII[f"{a1}{v1}+"]
              + CrystalChemistryDB.RADII[f"{a2}{v2}+"]
          ) / 2.0
          cand = self._eval(
              formula, a1, a2, v1, v2, m_sym, m_val, x_sym, y_sym, r_a
          )
          if cand["valid"]:
            discovered_pool.append(cand)

    # Physical Sorting: Rank purely by Isolation Index (Phi_2D) descending
    discovered_pool.sort(key=lambda x: x["isolation_score"], reverse=True)

    # Filter out compounds already existing in DB
    new_candidates: List[CandidateCompound] = []
    for raw in discovered_pool:
      if raw["formula"] not in self.existing_formulas:
        item_id = len(self.existing_db) + len(new_candidates) + 1
        cand_obj = CandidateCompound(
            id=item_id,
            formula=raw["formula"],
            target_orbital=raw["target_orbital"],
            isolation_score=raw["isolation_score"],
            c_over_a=raw["c_over_a"],
            anion_ratio=raw["anion_ratio"],
            lattice_a=raw["lattice_a"],
            lattice_c=raw["lattice_c"],
        )
        new_candidates.append(cand_obj)
        self.existing_formulas.add(raw["formula"])

        if generate_qe_cards:
          self._write_qe_card(raw)

        if len(new_candidates) >= batch_size:
          break

    if new_candidates:
      self.existing_db.extend([asdict(c) for c in new_candidates])
      with open(self.master_db_path, "w", encoding="utf-8") as f:
        json.dump(self.existing_db, f, indent=2, ensure_ascii=False)

    return new_candidates

  def _eval(
      self,
      formula: str,
      a1: str,
      a2: str,
      v1: int,
      v2: int,
      m: str,
      m_val: int,
      x: str,
      y: str,
      r_a: float,
  ) -> Dict[str, Any]:
    m_key = f"{m}{m_val}+"
    r_m = CrystalChemistryDB.RADII[m_key]
    r_x = CrystalChemistryDB.RADII[f"{x}2-"]
    r_y = CrystalChemistryDB.RADII[f"{y}1-"]

    anion_ratio = r_y / r_x
    a_est = round(2.0 * (r_m + r_x) * 0.95, 3)
    c_est = round(2.0 * (r_a + r_y) * 2.30, 3)
    c_over_a = round(c_est / a_est, 2)
    isolation_score = round(c_over_a * anion_ratio, 3)

    return {
        "formula": formula,
        "target_orbital": CrystalChemistryDB.ORBITAL_CONFIGS[m_key],
        "anion_ratio": round(anion_ratio, 3),
        "c_over_a": c_over_a,
        "isolation_score": isolation_score,
        "lattice_a": a_est,
        "lattice_c": c_est,
        "valid": (
            anion_ratio >= self.min_anion_ratio
            and c_over_a >= self.min_c_over_a
        ),
        "elements": {"A1": a1, "A2": a2, "M": m, "X": x, "Y": y},
    }

  def _write_qe_card(self, cand: Dict[str, Any]) -> None:
    target_dir = os.path.join(self.qe_output_dir, cand["formula"])
    os.makedirs(target_dir, exist_ok=True)
    a_bohr = cand["lattice_a"] * 1.88972612
    el = cand["elements"]
    is_ordered_A = el["A1"] != el["A2"]

    species = f"""    {el['A1']}  1.0  {el['A1']}.UPF
    {el['M']}   1.0  {el['M']}.UPF
    {el['X']}   1.0  {el['X']}.UPF
    {el['Y']}   1.0  {el['Y']}.UPF"""
    if is_ordered_A:
      species += f"\n    {el['A2']}  1.0  {el['A2']}.UPF"

    scf_template = f"""&CONTROL
    calculation = 'scf',
    prefix = '{cand["formula"]}',
    outdir = './tmp/',
    pseudo_dir = './pseudo/',
/
&SYSTEM
    ibrav = 6,
    celldm(1) = {a_bohr:.4f},
    celldm(3) = {cand["c_over_a"]:.4f},
    nat = 7,
    ntyp = {5 if is_ordered_A else 4},
    ecutwfc = 45.0,
    ecutrho = 360.0,
    occupations = 'smearing',
    smearing = 'cold',
    degauss = 0.02,
/
&ELECTRONS
    conv_thr = 1.0d-6,
/
ATOMIC_SPECIES
{species}
ATOMIC_POSITIONS (crystal)
    {el['M']}   0.000000  0.000000  0.000000
    {el['X']}   0.500000  0.000000  0.000000
    {el['X']}   0.000000  0.500000  0.000000
    {el['Y']}   0.000000  0.000000  0.355000
    {el['Y']}   0.000000  0.000000  0.645000
    {el['A1']}  0.500000  0.500000  0.182000
    {el['A2']}  0.500000  0.500000  0.818000
K_POINTS (automatic)
    4 4 2 0 0 0
"""
    with open(os.path.join(target_dir, "scf.in"), "w", encoding="utf-8") as f:
      f.write(scf_template)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--batch-size", type=int, default=100)
  parser.add_argument("--db", type=str, default="k_protocol_master_db.json")
  args = parser.parse_args()

  miner = KProtocolBatchMiner(master_db_path=args.db)
  results = miner.run_mining(batch_size=args.batch_size)

  print("\n" + "=" * 90)
  print(
      f"  K-PROTOCOL STRICT SCREENING (RANKED BY ISOLATION INDEX): {len(results)}"
      " FOUND"
  )
  print("=" * 90)
  print(
      f"{'Rank':<5} | {'Formula':<20} | {'Orbital Target':<28} | {'Phi_2D':<7}"
      f" | {'c/a':<5} | {'rY/rX':<5}"
  )
  print("-" * 90)
  for c in results:
    print(
        f"{c.id:<5} | {c.formula:<20} | {c.target_orbital:<28} |"
        f" {c.isolation_score:<7.3f} | {c.c_over_a:<5.2f} | {c.anion_ratio:<5.2f}"
    )
  print("=" * 90 + "\n")