# import thư viện
import pandas as pd
import matplotlib.pyplot as plt

#Tính tỷ lệ nợ MOB330 - xuất file csv (theo Tên sản phẩm)
path = r'C:\Users\ADMIN\Desktop\Tài liệu học Python\bài tập lớn\dulieuno.csv' #Đường dẫn mở file
df = pd.read_csv(path) #lệnh mở file
Mob330_mau = df.groupby('TEN_SAN_PHAM').sum()['MOB3_30_PASS'] #nhóm theo tên sản phẩm
Mob330_tu = df.groupby('TEN_SAN_PHAM').sum()['MOB3_30']
Mob330_sanpham = pd.concat([Mob330_tu, Mob330_mau], axis=1) #Gộp 2 bảng
Mob330_sanpham['TY_LE_NO'] = Mob330_sanpham['MOB3_30']/Mob330_sanpham['MOB3_30_PASS']*100 #thêm cột Tỷ lệ nợ = Mob330 tử/mẫu
di = Mob330_sanpham.to_csv(r'C:\Users\ADMIN\Desktop\Tài liệu học Python\bài tập lớn\no.csv', encoding='UTF-8') #xuất file csv
print(di)

#Vẽ đồ thị
dx = pd.read_csv(r'C:\Users\ADMIN\Desktop\Tài liệu học Python\bài tập lớn\no.csv') # đường dẫn mở file kết quả
Tyleno = dx['TY_LE_NO']
sanpham = dx['TEN_SAN_PHAM']
plt.subplots(figsize=(10,10))
plt.bar(x = sanpham, height = Tyleno, color = '#FF9821', align='center')
plt.xticks(sanpham, rotation = 20, size = 5, color = '#FF3D5A')
plt.xlabel('SẢN PHẨM', size = 15)
plt.ylabel('%30+MOB3', size = 15)
plt.title('%30+MOB3 THEO SẢN PHẨM', size = 30)
plt.show()






