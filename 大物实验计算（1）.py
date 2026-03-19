import numpy as np
import math


# =========================================================================
# 辅助函数：格式化 N(U) 字符串
# =========================================================================
def format_NU(N_val, U_val, sig_figs=2):
    """
    按照大学物理实验要求格式化结果：
    1. U 保留两位有效数字
    2. N 四舍五入到与 U 相同的精度（末位对齐）
    """
    if U_val == 0:
        return f"{N_val}(0)"

    # 计算 U 的量级，确定需要保留的小数位数
    # mag 为 U 第一个有效数字所在的位置（例如 0.012 为 -2）
    mag = math.floor(math.log10(abs(U_val)))
    # 为了保留 2 位有效数字，需要保留的小数位数为：
    decimals = (sig_figs - 1) - mag

    # 修正：如果 decimals < 0，说明 U 是大于 10 的整数
    if decimals < 0:
        U_sig2 = round(U_val, decimals)
        N_round = round(N_val, decimals)
        return f"{int(N_round)}({int(U_sig2)})"
    else:
        U_sig2 = round(U_val, decimals)
        N_round = round(N_val, decimals)
        # 生成格式化模板，如 "%.2f(%.2f)"
        fmt = f"%.{decimals}f(%.{decimals}f)"
        return fmt % (N_round, U_sig2)


# -------------------------------------------------------------------------
# 模块一：题 1 与 题 2 的计算
# -------------------------------------------------------------------------
def solve_prob1_and_2(L, W, delta_L=0.1, delta_W=0.1, k=2):
    n_count = len(L)

    # --- 计算输入量 L 和 W 的平均值 ---
    L_bar = np.mean(L)
    W_bar = np.mean(W)

    # --- 计算输出量 S 的平均值 ---
    S_bar = L_bar * W_bar

    # --- 计算输入量 L 和 W 的 A 类不确定度 ---
    # Python 的 np.std 默认 ddof=0，R 的 sd() 是 ddof=1 (样本标准差)
    uA_L = np.std(L, ddof=1) / math.sqrt(n_count)
    uA_W = np.std(W, ddof=1) / math.sqrt(n_count)

    # 【核心】：面积 S 的 A 类不确定度采用基于偏微分的传递公式
    # uA_S = sqrt( (dS/dL * uA_L)^2 + (dS/dW * uA_W)^2 )，其中 dS/dL=W, dS/dW=L
    uA_S = math.sqrt((W_bar * uA_L) ** 2 + (L_bar * uA_W) ** 2)

    # --- 计算 B 类不确定度 ---
    uB_L = delta_L / math.sqrt(3)
    uB_W = delta_W / math.sqrt(3)
    # 面积 S 的 B 类不确定度传递
    uB_S = math.sqrt((W_bar * uB_L) ** 2 + (L_bar * uB_W) ** 2)

    # --- 计算合成不确定度 ---
    uc_L = math.sqrt(uA_L ** 2 + uB_L ** 2)
    uc_W = math.sqrt(uA_W ** 2 + uB_W ** 2)
    uc_S = math.sqrt(uA_S ** 2 + uB_S ** 2)

    # --- 计算扩展不确定度 ---
    U_L = k * uc_L
    U_W = k * uc_W
    U_S = k * uc_S

    # 打印结果
    print("========== 题 1 & 题 2 计算结果 ==========")
    print("【题 1 结果 (A类采用偏微分传递)】")
    print(f"L 平均值 = {L_bar:.3f} cm, u_A(L) = {uA_L:.5f} cm")
    print(f"W 平均值 = {W_bar:.3f} cm, u_A(W) = {uA_W:.5f} cm")
    print(f"S 平均值 = {S_bar:.3f} cm^2, u_A(S) = {uA_S:.5f} cm^2")

    print("\n【题 2 结果 (B类采用偏微分传递)】")
    print(f"u_B(L) = {uB_L:.5f} cm, u_c(L) = {uc_L:.5f} cm, U(L) = {U_L:.5f} cm")
    print(f"u_B(W) = {uB_W:.5f} cm, u_c(W) = {uc_W:.5f} cm, U(W) = {U_W:.5f} cm")
    print(f"u_B(S) = {uB_S:.5f} cm^2, u_c(S) = {uc_S:.5f} cm^2, U(S) = {U_S:.5f} cm^2")

    print("\n【最终结果表示 N=N(U) ，U保留2位有效数字】")
    print(f"L = {format_NU(L_bar, U_L)} cm")
    print(f"W = {format_NU(W_bar, U_W)} cm")
    print(f"S = {format_NU(S_bar, U_S)} cm^2")
    print("==========================================\n")


# -------------------------------------------------------------------------
# 模块二：题 3 与 题 4 的计算
# -------------------------------------------------------------------------
def solve_prob3_and_4(l_mm, delta_l_mm, delta_t_s, t_react_s, g_approx, limit_percent):
    l_m = l_mm / 1000
    limit = limit_percent / 100
    T_approx = 2 * math.pi * math.sqrt(l_m / g_approx)

    uB_l_mm = delta_l_mm / math.sqrt(3)
    rel_uB_l = uB_l_mm / l_mm

    # --- 题 3 计算 ---
    uB_t1 = delta_t_s / math.sqrt(3)
    # 根据均分原理: rel_uB_l = 2 * (uB_t / t)  => t = 2 * uB_t / rel_uB_l
    t1_min = (2 * uB_t1) / rel_uB_l
    n1_min = t1_min / T_approx

    # 计入反应时间 (反应时间直接作为误差，不除以 sqrt(3))
    uB_t2 = math.sqrt((delta_t_s / math.sqrt(3)) ** 2 + t_react_s ** 2)
    t2_min = (2 * uB_t2) / rel_uB_l
    n2_min = t2_min / T_approx

    # --- 题 4 计算 ---
    # rel_uc^2 = (uB_l/l)^2 + (2 * uB_t / t)^2 <= limit^2
    # 2 * uB_t / t = sqrt(limit^2 - (uB_l/l)^2)
    denominator = math.sqrt(limit ** 2 - rel_uB_l ** 2)

    t4_1_min = (2 * uB_t1) / denominator
    n4_1_min = t4_1_min / T_approx

    t4_2_min = (2 * uB_t2) / denominator
    n4_2_min = t4_2_min / T_approx

    print("========== 题 3 & 题 4 计算结果 ==========")
    print(f"预估单摆周期 T ≈ {T_approx:.4f} s")
    print(f"摆长相对不确定度 u_B(l)/l = {rel_uB_l:.6e}")

    print("\n【题 3 结果 (均分原理)】")
    print(f"(1) 不计反应时间 (uB_t = {uB_t1:.5f} s):")
    print(f"    最少总时间 t = {t1_min:.2f} s, 摆动次数 n = {n1_min:.2f} 次 -> 至少需 {math.ceil(n1_min)} 次")
    print(f"(2) 计入反应时间 (uB_t = {uB_t2:.5f} s, 反应误差直接计入不除以根号3):")
    print(f"    最少总时间 t = {t2_min:.2f} s, 摆动次数 n = {n2_min:.2f} 次 -> 至少需 {math.ceil(n2_min)} 次")

    print("\n【题 4 结果 (B类相对不确定度 <= 1%)】")
    print(f"分母校验项 sqrt(limit^2 - (uB_l/l)^2) = {denominator:.6e}")
    print(f"-> 采用题 3(1) 条件 (不计反应时间):")
    print(f"   最少总时间 t = {t4_1_min:.2f} s, 摆动次数 n = {n4_1_min:.2f} 次 -> 至少需 {math.ceil(n4_1_min)} 次")
    print(f"-> 采用题 3(2) 条件 (计入反应时间):")
    print(f"   最少总时间 t = {t4_2_min:.2f} s, 摆动次数 n = {n4_2_min:.2f} 次 -> 至少需 {math.ceil(n4_2_min)} 次")
    print("==========================================\n")


# =========================================================================
# 执行区
# =========================================================================
if __name__ == "__main__":
    # --- 题 1、2 数据 ---
    L_data = np.array([180.23, 180.20, 180.16, 180.18, 180.19])
    W_data = np.array([75.15, 75.19, 75.10, 75.12, 75.13])
    instrument_delta_L = 0.1
    instrument_delta_W = 0.1

    solve_prob1_and_2(L=L_data, W=W_data, delta_L=instrument_delta_L, delta_W=instrument_delta_W)

    # --- 题 3、4 数据 ---
    pendulum_l_mm = 701
    delta_l_mm = 1
    delta_t_s = 0.1
    reaction_t_s = 0.4
    gravity_approx = 9.8
    limit_pct = 1.0

    solve_prob3_and_4(l_mm=pendulum_l_mm, delta_l_mm=delta_l_mm,
                      delta_t_s=delta_t_s, t_react_s=reaction_t_s,
                      g_approx=gravity_approx, limit_percent=limit_pct)