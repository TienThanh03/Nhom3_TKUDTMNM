import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df.iloc[:, :])

print('Dữ liệu:')
print(in_data)
print('Tổng số sinh viên đi thi:')
tongsv = in_data[:, 1]
print(np.sum(tongsv))

diemA = in_data[:, 3]
diemBc = in_data[:, 4]
diemB = in_data[:, 5]
diemCd= in_data[:, 6]
lop = in_data[:, 0]

maxa = diemA.max()
i, = np.where(diemA == maxa)
lop_maxa = in_data[i, 0]

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(diemA, labels=lop, autopct='%1.1f%%')
ax.set_title('Tỉ lệ sinh viên đạt loại A')


fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(diemBc, labels=lop, autopct='%1.1f%%')
ax.set_title('Tỉ lệ sinh viên đạt loại B+')

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(diemB, labels=lop, autopct='%1.1f%%')
ax.set_title('Tỉ lệ sinh viên đạt loại B')

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(diemCd, labels=lop, autopct='%1.1f%%')
ax.set_title('Tỉ lệ sinh viên đạt loại C+')


diemA_mean = np.mean(diemA)
print('Trung bình cộng số SV đạt điểm A:', diemA_mean)
diemBc_mean = np.mean(diemBc)
print('Trung bình cộng điểm số SV đạt điểm B+:', diemBc_mean)
diemB_mean = np.mean(diemB)
print('Trung bình cộng số SV đạt điểm B:', diemA_mean)
diemCd_mean = np.mean(diemCd)
print('Trung bình cộng số SV đạt điểm C+:', diemA_mean)

print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))

max_mean = max(diemA_mean, diemBc_mean, diemB_mean, diemCd_mean)

if max_mean == diemA_mean:
    print('Kiểu điểm có trung bình lớn nhất là A')
elif max_mean == diemBc_mean:
    print('Kiểu điểm có trung bình lớn nhất là B+')
elif max_mean == diemB_mean:
    print('Kiểu điểm có trung bình lớn nhất là B')
elif max_mean == diemCd_mean:
    print('Kiểu điểm có trung bình lớn nhất là C+')
else:
    print('Có nhiều kiểu điểm có trung bình lớn nhất')

fig, ax = plt.subplots(figsize=(8, 6))
width = 0.1
x = np.arange(len(lop))

rects1 = ax.bar(x, diemA, width, label='Điểm A')
rects2 = ax.bar(x + width, diemBc, width, label='Điểm B+')
rects3 = ax.bar(x + 2 * width, diemB, width, label='Điểm B')
rects4 = ax.bar(x + 3 * width, diemCd, width, label='Điểm C+')

ax.set_xlabel('Lớp')
ax.set_ylabel('Số sinh viên')
ax.set_title('So sánh số sinh viên đạt điểm A, B+, B và C của từng lớp')
ax.set_xticks(x + 2 * width)
ax.set_xticklabels(lop)
ax.legend()

plt.show()
