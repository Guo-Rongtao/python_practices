import math
import numpy as np


# 辅助函数：格式化 N(U) 字符串

def format_NU(N_val, U_val, sig_figs=2):

    # 按照大学物理实验要求格式化结果：
    # 1. U 保留两位有效数字
    # 2. N 四舍五入到与 U 相同的精度（末位对齐）

    if U_val == 0:
        return f"{N_val}(0)"
    # 计算 U 的量级，确定需要保留的小数位数，mag 为 U 第一个有效数字所在的位置（例如 0.012 为 -2）：
    mag = math.floor(math.log10(abs(U_val)))
    # 为了保留 2 位有效数字，需要保留的小数位数为：
    decimals = (sig_figs - 1) - mag
    # 修正：如果 decimals < 0，说明 U 是大于 10 的整数：
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


def solve(x, y, delta_x=0.1, delta_y=0.1, k=2):
    n_count = len(x)

# --- 计算输入量 x和 y和他们的乘积 S的平均值 ---

    x_average = np.mean(x)
    y_average = np.mean(y)
    S_average = x_average * y_average

# --- 计算输入量 x 和 y 的 A 类不确定度 ---
# Python 的 np.std 默认 ddof=0，R 的 sd() 是 ddof=1 (样本标准差)
    uA_x= np.std(x, ddof=1) / math.sqrt(n_count)
    uA_y = np.std(y, ddof=1) / math.sqrt(n_count)
   #【核心】：乘积 S 的 A 类不确定度采用基于偏微分的传递公式：uA_S = sqrt( (dS/dx * uA_x)^2 + (dS/dy * uA_y)^2 )，其中 dS/dx=y, dS/dy=x
    uA_S = math.sqrt((y_average * uA_x) ** 2 + (x_average * uA_y) ** 2)

# --- 计算 B 类不确定度 ---
    uB_x = delta_x / math.sqrt(3)
    ub_y = delta_y / math.sqrt(3)
    uB_S = math.sqrt((y_average * uB_x) ** 2 + (x_average * ub_y) ** 2)

# --- 计算合成不确定度 ---
    uC_x = math.sqrt(uA_x ** 2 + uB_x ** 2)
    uC_y = math.sqrt(uA_y ** 2 + ub_y ** 2)
    uC_S = math.sqrt(uA_S ** 2 + uB_S ** 2)

# --- 计算扩展不确定度 ---
    U_x = k * uC_x
    U_y = k * uC_y
    U_S = k * uC_S

# 打印结果
    print(
        f"x的平均值 = {x_average:.3f} cm,\n\
         x的A类不确定度u_A(x) = {uA_x:.5f} cm,\n  \
         x的B类不确定度u_B(x) = {uB_x:.5f} cm,\n  \
         x的合成不确定度u_c(L) = {uC_x:.5f} cm,\n  \
         x的扩展不确定度U(x) = {U_x:.5f} cm\n\n"
    )

    print(
        f"y的平均值 = {y_average:.3f} cm,\n\
          y的A类不确定度u_A(y) = {uA_y:.5f} cm,\n\
          y的B类不确定度u_B(y) = {ub_y:.5f} cm,\n\
          y的合成不确定度u_c(y) = {uC_y:.5f} cm,\n\
          y的扩展不确定度U(y) = {U_y:.5f} cm\n\n"
    )

    print(
        f"x和y的乘积S的平均值 = {S_average:.3f} cm^2, \n\
          A类不确定度u_A(S) = {uA_S:.5f} cm^2,\n\
          B类不确定度u_B(S) = {uB_S:.5f} cm^2,\n\
          合成不确定度u_c(S) = {uC_S:.5f} cm^2,\n\
          扩展不确定度U(S) = {U_S:.5f} cm^2"
    )


    print("\n【最终结果表示 N=N(U) ，U保留2位有效数字】")
    print(f"x = {format_NU(x_average, U_x)} cm")
    print(f"y = {format_NU(y_average, U_y)} cm")
    print(f"S = {format_NU(S_average, U_S)} cm^2")
    print("==========================================\n")


# ==================================执行区=======================================
if __name__ == "__main__":
    # --- 输入数据 ---
    x_data = np.array([0.770,0.772,0.771,0.771,0.773])
    y_data = np.array([0.214,0.215,0.216,0.217,0.218])
    instrument_delta_x = 0.1
    instrument_delta_y = 0.1

    solve(x=x_data, y=y_data, delta_x=instrument_delta_x, delta_y=instrument_delta_y)