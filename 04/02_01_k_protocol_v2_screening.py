import os
import numpy as np
import pandas as pd
from itertools import combinations_with_replacement

# ==============================================================================
# [K-PROTOCOL Paper 04-2] Room-Temperature Superconducting Parents Miner
# Inverse-Design Engine for 4d/5d Plaquettes with Giant Superexchange (J)
# Output: k_protocol_v2_screened_492.csv
# ==============================================================================

# 1. Shannon Ionic Radii Database (in Angstroms, Coordination-Specific)
IONIC_RADII = {
    # Planar Anions (X) - 4/6 coordination
    "O2-": 1.40,
    "F-": 1.33,
    
    # Apical Anions (Y) - 6 coordination
    "Cl-": 1.81,
    "Br-": 1.96,
    "I-": 2.20,
    
    # Metal Cations (M) - Square-Planar / Octahedral low-spin
    # 3d metals
    "Cu2+": {"r": 0.73, "orbit": "3d", "d_count": 9, "U": 8.0, "t_ratio": 1.0},
    "Ni1+": {"r": 0.78, "orbit": "3d", "d_count": 9, "U": 7.5, "t_ratio": 0.95},
    "V4+":  {"r": 0.58, "orbit": "3d", "d_count": 1, "U": 6.0, "t_ratio": 0.90},
    "Ti3+": {"r": 0.67, "orbit": "3d", "d_count": 1, "U": 5.5, "t_ratio": 0.85},
    
    # 4d metals (High J potential)
    "Ag2+": {"r": 0.94, "orbit": "4d", "d_count": 9, "U": 5.2, "t_ratio": 1.48},
    "Pd1+": {"r": 0.98, "orbit": "4d", "d_count": 9, "U": 5.0, "t_ratio": 1.40},
    "Nb4+": {"r": 0.68, "orbit": "4d", "d_count": 1, "U": 4.5, "t_ratio": 1.35},
    
    # 5d metals (Giant J potential)
    "Au2+": {"r": 1.02, "orbit": "5d", "d_count": 9, "U": 3.8, "t_ratio": 1.85},
    "Ta4+": {"r": 0.68, "orbit": "5d", "d_count": 1, "U": 3.5, "t_ratio": 1.65},

    # Spacer Cations (A)
    "Li+": 0.76, "Na+": 1.02, "K+": 1.38, "Rb+": 1.52, "Cs+": 1.67,
    "Mg2+": 0.72, "Ca2+": 1.00, "Sr2+": 1.18, "Ba2+": 1.35,
    "La3+": 1.03, "Y3+": 0.90, "Bi3+": 1.03
}

VALENCES = {
    # A-site
    "Li": 1, "Na": 1, "K": 1, "Rb": 1, "Cs": 1,
    "Mg": 2, "Ca": 2, "Sr": 2, "Ba": 2,
    "La": 3, "Y": 3, "Bi": 3,
    # M-site
    "Cu": 2, "Ni": 1, "V": 4, "Ti": 3,
    "Ag": 2, "Pd": 1, "Nb": 4,
    "Au": 2, "Ta": 4
}

T0_CUPRATE = 0.45    # eV (Canonical baseline for Sr2CuO2Cl2)
J0_BASE_MEV = 130.0  # meV for Sr2CuO2Cl2
CSV_OUTPUT_PATH = "k_protocol_v2_screened_492.csv"

def get_a_radius(elem):
    """A자리 양이온 이온 반경 조회"""
    v = VALENCES[elem]
    key = f"{elem}+" if v == 1 else f"{elem}{v}+"
    return IONIC_RADII[key]

def estimate_superexchange(m_ion, x_ion):
    """초교환 결합 에너지 J = 4*t^2 / U 추정"""
    props = IONIC_RADII[m_ion]
    t = T0_CUPRATE * props["t_ratio"]
    if x_ion == "F-":
        t *= 0.88
    j_ev = (4.0 * (t ** 2)) / props["U"]
    return j_ev * 1000.0  # meV 반환

def run_k_protocol_v2_screening():
    candidates = []
    
    a_elements = ["Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba", "La", "Y", "Bi"]
    m_ions = ["Cu2+", "Ni1+", "V4+", "Ti3+", "Ag2+", "Pd1+", "Nb4+", "Au2+", "Ta4+"]
    x_ions = ["O2-"]
    y_ions = ["Cl-", "Br-", "I-"]
    
    for x_name in x_ions:
        r_x = IONIC_RADII[x_name]
        
        for y_name in y_ions:
            r_y = IONIC_RADII[y_name]
            
            # 1. 꼭짓점 차폐 조건: r_Y / r_X >= 1.25
            steric_ratio = r_y / r_x
            if steric_ratio < 1.25:
                continue
                
            for m_ion in m_ions:
                m_elem = m_ion[:2] if m_ion[1].isalpha() else m_ion[:1]
                q_m = VALENCES[m_elem]
                r_m = IONIC_RADII[m_ion]["r"]
                
                # 2. 전기적 중성 조건: Q(A_tot) + Q(M) = +6
                target_q_a = 6 - q_m
                if target_q_a <= 0:
                    continue
                    
                j_est = estimate_superexchange(m_ion, x_name)
                
                # A자리 양이온 조합 탐색 (A1, A2)
                for a1, a2 in combinations_with_replacement(a_elements, 2):
                    if (VALENCES[a1] + VALENCES[a2]) == target_q_a:
                        # 화학식 표기: 산화수 높은 양이온 우선 배치
                        if VALENCES[a1] < VALENCES[a2]:
                            a_first, a_second = a2, a1
                        else:
                            a_first, a_second = a1, a2
                            
                        r_a1 = get_a_radius(a_first)
                        r_a2 = get_a_radius(a_second)
                        mean_r_a = (r_a1 + r_a2) / 2.0
                        
                        # 격자 상수 및 기하 파라미터 계산
                        a_lat = 2.0 * (r_m + r_x) / np.sqrt(2.0)
                        c_lat = 2.0 * ((r_m + r_x) + 2.0 * (mean_r_a + r_y))
                        c_over_a = c_lat / a_lat
                        
                        # 골즈슈미트 허용 계수 (Goldschmidt Tolerance Factor: tf)
                        # 페로브스카이트 슬래브 안정성 지표 (이상값: 0.85 ~ 1.05)
                        t_factor = (mean_r_a + r_x) / (np.sqrt(2.0) * (r_m + r_x))
                        
                        # 3. 2차원 고립 조건: c/a >= 3.60
                        if c_over_a >= 3.60:
                            phi_2d = c_over_a * steric_ratio
                            theta_rt = phi_2d * (j_est / J0_BASE_MEV)
                            
                            if a_first == a_second:
                                formula = f"{a_first}2{m_elem}{x_name[0]}2{y_name[:-1]}2"
                            else:
                                formula = f"{a_first}{a_second}{m_elem}{x_name[0]}2{y_name[:-1]}2"
                                
                            candidates.append({
                                "Formula": formula,
                                "Metal": m_ion,
                                "Orbit": IONIC_RADII[m_ion]["orbit"],
                                "c/a": round(c_over_a, 2),
                                "r_Y/r_X": round(steric_ratio, 3),
                                "t_factor": round(t_factor, 3),
                                "Phi_2D": round(phi_2d, 3),
                                "J_est (meV)": round(j_est, 1),
                                "Theta_RT": round(theta_rt, 2)
                            })
                            
    df = pd.DataFrame(candidates)
    df = df.drop_duplicates(subset=["Formula"]).sort_values(by="Theta_RT", ascending=False).reset_index(drop=True)
    return df

if __name__ == "__main__":
    print("=" * 75)
    print(" [K-PROTOCOL Paper 04-2] Room-Temperature Superconducting Parents Screening ")
    print("=" * 75)
    
    df_results = run_k_protocol_v2_screening()
    
    # 492개 전체 데이터셋 CSV 저장
    df_results.to_csv(CSV_OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(f"\n>> Complete dataset of {len(df_results)} candidates exported to: '{CSV_OUTPUT_PATH}'")
    
    print("\n[Top 10 Ultra-High J Candidates (Room-Temperature Targets)]")
    print(df_results.head(10).to_string(index=True))
    
    print("\n[Canonical Benchmarks & Key Controls]")
    benchmarks = df_results[df_results["Formula"].isin([
        "Ba2AgO2I2", "Ba2AgO2Br2", "Ba2AuO2I2", "Cs2TaO2I2", 
        "Sr2CuO2Cl2", "LaSrNiO2Cl2", "Cs2VO2I2"
    ])]
    print(benchmarks.to_string(index=False))
    print("=" * 75)