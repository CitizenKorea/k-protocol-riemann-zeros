import os
import numpy as np

# ==============================================================================
# [K-PROTOCOL Paper 04-2] Structural & DFT Input Generator
# Space Group: I4/mmm (No. 139) | Outputs: CIF, SCF.in, BANDS.in
# ==============================================================================

TARGETS = {
    "Ba2AgO2I2": {
        "M": "Ag", "X": "O", "Y": "I", "A": "Ba",
        "r_M": 0.94, "r_X": 1.40, "r_Y": 2.20, "r_A": 1.35,
        "mass_M": 107.87, "mass_X": 15.999, "mass_Y": 126.90, "mass_A": 137.33,
        "pseudo_M": "Ag.pbe-d-kjpaw_psl.1.0.0.UPF", "pseudo_X": "O.pbe-n-kjpaw_psl.1.0.0.UPF",
        "pseudo_Y": "I.pbe-n-kjpaw_psl.1.0.0.UPF", "pseudo_A": "Ba.pbe-spn-kjpaw_psl.1.0.0.UPF"
    },
    "Ba2AgO2Br2": {  # Chemical Redox Defense Compound
        "M": "Ag", "X": "O", "Y": "Br", "A": "Ba",
        "r_M": 0.94, "r_X": 1.40, "r_Y": 1.96, "r_A": 1.35,
        "mass_M": 107.87, "mass_X": 15.999, "mass_Y": 79.904, "mass_A": 137.33,
        "pseudo_M": "Ag.pbe-d-kjpaw_psl.1.0.0.UPF", "pseudo_X": "O.pbe-n-kjpaw_psl.1.0.0.UPF",
        "pseudo_Y": "Br.pbe-n-kjpaw_psl.1.0.0.UPF", "pseudo_A": "Ba.pbe-spn-kjpaw_psl.1.0.0.UPF"
    },
    "Ba2AuO2I2": {
        "M": "Au", "X": "O", "Y": "I", "A": "Ba",
        "r_M": 1.02, "r_X": 1.40, "r_Y": 2.20, "r_A": 1.35,
        "mass_M": 196.97, "mass_X": 15.999, "mass_Y": 126.90, "mass_A": 137.33,
        "pseudo_M": "Au.pbe-dn-kjpaw_psl.1.0.0.UPF", "pseudo_X": "O.pbe-n-kjpaw_psl.1.0.0.UPF",
        "pseudo_Y": "I.pbe-n-kjpaw_psl.1.0.0.UPF", "pseudo_A": "Ba.pbe-spn-kjpaw_psl.1.0.0.UPF"
    },
    "Cs2TaO2I2": {
        "M": "Ta", "X": "O", "Y": "I", "A": "Cs",
        "r_M": 0.68, "r_X": 1.40, "r_Y": 2.20, "r_A": 1.67,
        "mass_M": 180.95, "mass_X": 15.999, "mass_Y": 126.90, "mass_A": 132.91,
        "pseudo_M": "Ta.pbe-spfn-kjpaw_psl.1.0.0.UPF", "pseudo_X": "O.pbe-n-kjpaw_psl.1.0.0.UPF",
        "pseudo_Y": "I.pbe-n-kjpaw_psl.1.0.0.UPF", "pseudo_A": "Cs.pbe-spn-kjpaw_psl.1.0.0.UPF"
    }
}

OUTPUT_DIR = "dft_structure_inputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

K_PATH_TEXT = """K_POINTS (crystal_b)
5
 0.0000000000   0.0000000000   0.0000000000   40  ! Gamma
 0.5000000000   0.0000000000   0.0000000000   40  ! X
 0.5000000000   0.5000000000   0.0000000000   40  ! M
 0.0000000000   0.0000000000   0.0000000000   40  ! Gamma
 0.0000000000   0.0000000000   0.5000000000    1  ! Z
"""

def get_params(info):
    a = 2.0 * (info["r_M"] + info["r_X"])
    d_my = info["r_M"] + info["r_Y"]
    c = 2.0 * (d_my + (info["r_A"] + info["r_X"]) + (info["r_A"] + info["r_Y"]))
    return a, c, d_my / c, (d_my + (info["r_A"] + info["r_Y"])) / c

for name, info in TARGETS.items():
    a, c, z_y, z_a = get_params(info)
    
    # 1. CIF 생성
    cif_str = f"""data_{name}
_symmetry_space_group_name_H-M    'I 4/m m m'
_symmetry_Int_Tables_number       139
_cell_length_a  {a:.4f}  _cell_length_b  {a:.4f}  _cell_length_c  {c:.4f}
_cell_angle_alpha 90.0000  _cell_angle_beta 90.0000  _cell_angle_gamma 90.0000
loop_
_atom_site_label _atom_site_type_symbol _atom_site_Wyckoff_symbol _atom_site_fract_x _atom_site_fract_y _atom_site_fract_z
  {info['M']}1  {info['M']}  2a  0.00000  0.00000  0.00000
  {info['X']}1  {info['X']}  4c  0.00000  0.50000  0.00000
  {info['Y']}1  {info['Y']}  4e  0.00000  0.00000  {z_y:.5f}
  {info['A']}1  {info['A']}  4e  0.00000  0.00000  {z_a:.5f}
"""
    with open(os.path.join(OUTPUT_DIR, f"{name}.cif"), "w") as f:
        f.write(cif_str)

    # 2. QE SCF 생성
    base_qe = f"""&CONTROL
    calculation = '{{calc}}'
    prefix = '{name}'
    outdir = './out_{name}/'
    pseudo_dir = './pseudo/'
/
&SYSTEM
    ibrav = 7, celldm(1) = {a * 1.88972612:.6f}, celldm(3) = {c / a:.6f}
    nat = 7, ntyp = 4, ecutwfc = 60.0, ecutrho = 480.0
    occupations = 'smearing', smearing = 'gaussian', degauss = 0.01
/
&ELECTRONS
    conv_thr = 1.0d-8, mixing_beta = 0.4
/
ATOMIC_SPECIES
  {info['M']}  {info['mass_M']}  {info['pseudo_M']}
  {info['X']}  {info['mass_X']}  {info['pseudo_X']}
  {info['Y']}  {info['mass_Y']}  {info['pseudo_Y']}
  {info['A']}  {info['mass_A']}  {info['pseudo_A']}
ATOMIC_POSITIONS (crystal)
  {info['M']}  0.000000  0.000000  0.000000
  {info['X']}  0.000000  0.500000  0.000000
  {info['X']}  0.500000  0.000000  0.000000
  {info['Y']}  0.000000  0.000000  {z_y:.6f}
  {info['Y']}  0.000000  0.000000 -{z_y:.6f}
  {info['A']}  0.000000  0.000000  {z_a:.6f}
  {info['A']}  0.000000  0.000000 -{z_a:.6f}
"""
    with open(os.path.join(OUTPUT_DIR, f"{name}_scf.in"), "w") as f:
        f.write(base_qe.format(calc="scf") + "\nK_POINTS (automatic)\n  8 8 2 0 0 0\n")
        
    # 3. QE BANDS 동시 생성 (통합 완료)
    with open(os.path.join(OUTPUT_DIR, f"{name}_bands.in"), "w") as f:
        f.write(base_qe.format(calc="bands") + "\n" + K_PATH_TEXT)

print("All CIF, SCF, and BANDS input files generated cleanly in:", OUTPUT_DIR)