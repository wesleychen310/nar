import pandas as pd
import matplotlib.pyplot as plt

# 讀取資料
data = pd.read_csv('nar0_data.csv')  # 替換為你的 CSV 文件路徑
nar0 = data['nar0']

# 畫直方圖（線性尺度，每 1 億一組）
max_value = nar0.max()  # 最大值約 11.7 億
bins = range(0, int(max_value) + 100000000, 100000000)  # 從 0 到 11.7 億，每 1 億一組（約 118 組）
plt.hist(nar0, bins=bins, edgecolor='black')
plt.xlabel('nar0 (Linear Scale)')
plt.ylabel('Frequency')
plt.title('Distribution of nar0 (Linear Scale, 100M per Bin)')
plt.show()

# 畫直方圖（對數尺度，更適合柏拉圖分佈）
plt.hist(nar0, bins=100, log=True, edgecolor='black')  # log=True 將 Y 軸設為對數尺度，100 個 bin
plt.xscale('log')  # X 軸設為對數尺度
plt.xlabel('nar0 (Log Scale)')
plt.ylabel('Frequency (Log Scale)')
plt.title('Distribution of nar0 (Log-Log Scale)')
plt.show()
