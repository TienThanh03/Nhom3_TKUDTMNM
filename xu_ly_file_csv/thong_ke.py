import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
tongsv= in_data[:,1]
print('Tong so sinh vien di thi :', tongsv)
diemA = in_data[:,3]
diemBc = in_data[:,4]
print('Tong sv:',tongsv)
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
tongsvAp= in_data[:,2]
print('SV dat diem A+ :',tongsvAp,'Tong: ',np.sum(tongsvAp))
tongsvA= in_data[:,3]
print('SV dat diem A :',tongsvA,'Tong: ',np.sum(tongsvA))
tongsvBp= in_data[:,4]
print('SV dat diem B+ :',tongsvBp,'Tong: ',np.sum(tongsvBp))
tongsvB= in_data[:,5]
print('SV dat diem B :',tongsvB,'Tong: ',np.sum(tongsvB))
tongsvCp= in_data[:,6]
print('SV dat diem C+ :',tongsvCp,'Tong: ',np.sum(tongsvCp))
tongsvC= in_data[:,7]
print('SV dat diem C :',tongsvC,'Tong: ',np.sum(tongsvC))
tongsvDp= in_data[:,8]
print('SV dat diem D+ :',tongsvDp,'Tong: ',np.sum(tongsvDp))
print('SV dat diem Dp :',tongsvDp,'Tong: ',np.sum(tongsvDp))
tongsvD= in_data[:,9]
print('SV dat diem D :',tongsvD,'Tong: ',np.sum(tongsvD))
tongsvF= in_data[:,10]
print('SV dat diem F :',tongsvF,'Tong: ',np.sum(tongsvF))
print('Tong so SV dat diem >=D: ', np.sum(tongsv)- np.sum(tongsvF))
lop1=in_data[0,2:9] 
print('Lop 1 co ',np.sum(lop1),'SV dat >=D')
lop2=in_data[1,2:9] 
print('Lop 2 co ',np.sum(lop2),'SV dat >=D')
lop3=in_data[2,2:9] 
print('Lop 3 co ',np.sum(lop3),'SV dat >=D')
lop4=in_data[3,2:9] 
print('Lop 4 co ',np.sum(lop4),'SV dat >=D')
lop5=in_data[4,2:9] 
print('Lop 5 co ',np.sum(lop5),'SV dat >=D')
lop6=in_data[5,2:9] 
print('Lop 6 co ',np.sum(lop6),'SV dat >=D')
lop7=in_data[6,2:9] 
print('Lop 7 co ',np.sum(lop7),'SV dat >=D')
lop8=in_data[7,2:9] 
print('Lop 8 co ',np.sum(lop8),'SV dat >=D')
lop9=in_data[8,2:9] 
print('Lop 9 co ',np.sum(lop9),'SV dat >=D')
# Tính trung bình cộng
average_scores = np.mean(in_data[:, 2:11], axis=0)
# In ra trung bình cộng
print('Trung bình cộng số sinh viên đạt từng loại điểm:')
print('A+:', int(average_scores[0]))
print('A:', int(average_scores[1]))
print('B+:', int(average_scores[2]))
print('B:', int(average_scores[3]))
print('C+:', int(average_scores[4]))
print('C:', int(average_scores[5]))
print('D+:', int(average_scores[6]))
print('D:', int(average_scores[7]))
print('F:', int(average_scores[8]))
def tinh_su_chenh_lech(a,b):
    return np.abs(int(np.sum(a)) - int(np.sum(b)))
#tim su chenh lech giua sv dat diem A,B,C,D
print("su chech lech giua A va B la: {0}".format(tinh_su_chenh_lech(tongsvA,tongsvB)))
print("su chech lech giua A va C la: {0}".format(tinh_su_chenh_lech(tongsvA,tongsvC)))
print("su chech lech giua A va D la: {0}".format(tinh_su_chenh_lech(tongsvA,tongsvD)))
print("su chech lech giua A va F la: {0}".format(tinh_su_chenh_lech(tongsvA,tongsvF)))
print("su chech lech giua B va C la: {0}".format(tinh_su_chenh_lech(tongsvB,tongsvC)))
print("su chech lech giua B va D la: {0}".format(tinh_su_chenh_lech(tongsvB,tongsvD)))
print("su chech lech giua B va C la: {0}".format(tinh_su_chenh_lech(tongsvB,tongsvF)))
print("su chech lech giua C va D la: {0}".format(tinh_su_chenh_lech(tongsvC,tongsvD)))
print("su chech lech giua C va F la: {0}".format(tinh_su_chenh_lech(tongsvC,tongsvF)))
print("su chech lech giua D va F la: {0}".format(tinh_su_chenh_lech(tongsvD,tongsvF)))
print('A+:', average_scores[0])
print('A:', average_scores[1])
print('B+:', average_scores[2])
print('B:', average_scores[3])
print('C+:', average_scores[4])
print('C:', average_scores[5])
print('D+:', average_scores[6])
print('D:', average_scores[7])
print('F:', average_scores[8])
# Tính tổng số sinh viên đạt mỗi bài kiểm tra
total_scores = np.sum(in_data[:, -5:], axis=0)
# In ra tổng số sinh viên đạt từng bài kiểm tra
print('Tổng số sinh viên đạt từng bài kiểm tra:')
print('L1:', total_scores[-5])
print('L2:', total_scores[-4])
print('TX1:', total_scores[-3])
print('TX2:', total_scores[-2])
print('Cuối kỳ:', total_scores[-1])
#compare l1, l2, tx1, tx2, final
def compare(sum1,sum2,ten_diem_1,ten_diem_2):
    if sum1 > sum2 :
        print("so sinh vien dat {0} nhieu hon(>) so sinh vien dat {1} la : {2} sinh vien".format(ten_diem_1,ten_diem_2,sum1-sum2))
    elif sum1 < sum2 :
        print("so sinh vien dat {0} it hon(>) so sinh vien dat {1} la : {2} sinh vien".format(ten_diem_1, ten_diem_2, sum2 - sum1))
    else:
        print("so sinh vien dat {0} bang(==) so sinh vien dat {1} : {2} sinh vien".format(ten_diem_1,ten_diem_2,sum2))
print("so sanh so sinh vien dat")
compare(total_scores[-3],total_scores[-2],"TX1","TX2")
compare(total_scores[-3],total_scores[-1],"TX1","Cuoi ky")
compare(total_scores[-2],total_scores[-1],"TX2","Cuoi ky")
compare(total_scores[-5],total_scores[-4],"L1","L2")

# Dữ liệu cho các đồ thị tròn
nhan = ['A+', 'A', 'B+', 'B', 'C+', 'C','D+','D','F']

# Dữ liệu mẫu cho 9 đồ thị cột
data = [
    [in_data[0,2],in_data[0,3],in_data[0,4],in_data[0,5],in_data[0,6],in_data[0,7],in_data[0,8],in_data[0,9],in_data[0,10]],
    [in_data[1,2],in_data[1,3],in_data[1,4],in_data[1,5],in_data[1,6],in_data[1,7],in_data[1,8],in_data[1,9],in_data[1,10]],
    [in_data[2,2],in_data[2,3],in_data[2,4],in_data[2,5],in_data[2,6],in_data[2,7],in_data[2,8],in_data[2,9],in_data[2,10]],
    [in_data[3,2],in_data[3,3],in_data[3,4],in_data[3,5],in_data[3,6],in_data[3,7],in_data[3,8],in_data[3,9],in_data[3,10]],
    [in_data[4,2],in_data[4,3],in_data[4,4],in_data[4,5],in_data[4,6],in_data[4,7],in_data[4,8],in_data[4,9],in_data[4,10]],
    [in_data[5,2],in_data[5,3],in_data[5,4],in_data[5,5],in_data[5,6],in_data[5,7],in_data[5,8],in_data[5,9],in_data[5,10]],
    [in_data[6,2],in_data[6,3],in_data[6,4],in_data[6,5],in_data[6,6],in_data[6,7],in_data[6,8],in_data[6,9],in_data[6,10]],
    [in_data[7,2],in_data[7,3],in_data[7,4],in_data[7,5],in_data[7,6],in_data[7,7],in_data[7,8],in_data[7,9],in_data[7,10]],
    [in_data[8,2],in_data[8,3],in_data[8,4],in_data[8,5],in_data[8,6],in_data[8,7],in_data[8,8],in_data[8,9],in_data[8,10]],
]
# Dữ liệu cho đồ thị cột
labels = ['Lop 1', 'Lop 2', 'Lop 3', 'Lop 4', 'Lop 5', 'Lop 6', 'Lop 7', 'Lop 8', 'Lop 9']
x = np.arange(len(labels))
fig, ax = plt.subplots()
width = 0.1  # Chiều rộng của cột
for i in range(9):
    ax.bar(x + i * width, data[i], width, label=labels[i])
ax.set_xlabel('Loại Điểm')
ax.set_ylabel('Số Lượng Sinh Viên')
ax.set_title('Số Lượng Sinh Viên Đạt Từng Loại Điểm Theo Lớp')
ax.set_xticks(x + 4.5 * width)
ax.set_xticklabels(nhan)
ax.legend()
plt.show()


# Tạo mảng chứa tổng số sinh viên đạt từng loại điểm qua từng kỳ thi
total_scores_per_exam = np.sum(in_data[:, 2:11], axis=1)

# Vẽ đồ thị đường cho biến động của số lượng sinh viên đạt từng loại điểm qua từng kỳ thi
plt.plot(total_scores_per_exam, marker='o', linestyle='-', color='b')
plt.xlabel('Kỳ Thi')
plt.ylabel('Tổng Số Sinh Viên Đạt')
plt.title('Biến Động Số Lượng Sinh Viên Đạt Điểm Qua Các Kỳ Thi')
plt.xticks(np.arange(len(total_scores_per_exam)), np.arange(1, len(total_scores_per_exam) + 1))
