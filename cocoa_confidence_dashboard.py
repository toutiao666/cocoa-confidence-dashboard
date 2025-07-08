import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 时间轴设置
dates = pd.date_range(start='2025-03-01', end='2026-03-01', freq='MS')
t = np.arange(len(dates))

# 中位预测产量（假设逐步上修）
mid_pred = 160 + 2 * np.sin(t / 3)

# 置信区间宽度（假设随时间收敛）
ci_width = 20 * np.exp(-0.2 * t)

# 上下置信区间
upper = mid_pred + ci_width
lower = mid_pred - ci_width

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(dates, mid_pred, color='blue', label='中位预测产量')
plt.fill_between(dates, lower, upper, color='blue', alpha=0.3, label='95%置信区间')
plt.title('可可 03合约：2025-2026年 置信区间收敛模拟图')
plt.xlabel('时间')
plt.ylabel('预测产量（万吨）')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
