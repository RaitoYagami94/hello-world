#Chương trình dịch từ Tiếng Việt sang Tiếng Anh sử dụng thuật toán của Google translate
#Nhập thư viện Tkinter và googel translate
#try:

from tkinter import * 
from PIL import Image, ImageTk
from googletrans import Translator

#print("the imported file is", tkinter.__file__)
# Tạo TK window
root = Tk()
root.title('Google Translator')
root.geometry("500x630")
root.iconbitmap("E:\\0000Python_Learning\\GoogleTranslate\\Logo.ico")

# Tạo nền xanh transformer
load= Image.open("E:\\0000Python_Learning\\GoogleTranslate\\background.png")
render= ImageTk.PhotoImage(load)
Img=Label(root, image=render)
Img.place(x=0,y=0)

#Tạo tên chương trình dạng ảnh
name=Label(root,text = "Vietnamese to ...", fg="#ffffff",bd=0, bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

# Cửa sổ nhập thông tin cần dịch
box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

Button_frame = Frame(root).pack(side=BOTTOM)

# Định nghĩa hàm cho box và box1 để xóa text và lấy text để dịch
def clearTV():
    box.delete(1.0,END)
def clearDich():
    box1.delete(1.0,END)

# Khởi tạo hàm dịch các ngôn ngữ
def translateE():
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest="en")
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)
def translateD():
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest="de")
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)

def translateF():
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest="fr")
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)
    
def translateR():
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest="ru")
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)

def translateKhac():
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest=w)
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)
#Khởi tạo nút xóa chữ và câu lệnh xóa #Đặt vị trí nút xóa chữ
clear_button=Button(Button_frame, text = "Xóa TV", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=clearTV)
clear_button.place(x=5, y= 155)

#Khởi tạo nút xóa chữ và câu lệnh xóa #Đặt vị trí nút xóa chữ
clear_button1=Button(Button_frame, text = "Xóa dịch", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=clearDich)
clear_button1.place(x=5, y= 455)

#Khởi tạo nút dịch và câu lệnh dịch (t= Translator()) #Đặt vị trí nút dịch Tiếng Anh
trans_buttonE=Button(Button_frame, text = "Anh", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=translateE)
trans_buttonE.place(x=190, y= 295)
#Tiếng Pháp
trans_buttonF=Button(Button_frame, text = "Pháp", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=translateF)
trans_buttonF.place(x=190, y= 330)
#Tiếng Đức
trans_buttonD=Button(Button_frame, text = "Đức", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=translateD)
trans_buttonD.place(x=250, y= 295)
#Tiếng Nga
trans_buttonR=Button(Button_frame, text = "Nga", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=translateR)
trans_buttonR.place(x=250, y= 330)

# Them nut chon ngo ngu
T_lang = StringVar(root)
T_lang.set("Khác...") # default value
w = OptionMenu(root, T_lang, "lo", "my", "ro", command=translateKhac)
print(w)
w.place(x=300, y=325)

#Đưa kết quả dịch vào box1
box1=Text(root,width=28,height=8,font=("ROBOTO", 16))
box1.pack(pady=60)

# Copyright
COP=Label(root,text = "Copyright of Nguyễn Hồng Quảng, VNSC", fg="#ffffff",bd=0, bg="#03152D")
COP.config(font=("Arial",10))
COP.pack(pady=70)
COP.place(x=10, y=605)
#print (COP)

root.mainloop()#kết thúc vòng lặp cửa sổ
"""
except Exception as e:
    print (e)
input()
"""