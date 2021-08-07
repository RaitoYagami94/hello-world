#Chương trình dịch từ Tiếng Việt sang Tiếng Anh sử dụng thuật toán của Google translate
#Nhập thư viện Tkinter và googel translate

from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# print("the imported file is", tkinter.__file__)
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

# xóa text trong box và box1
def clearTV():
    box.delete(1.0,END)
def clearDich():
    box1.delete(1.0,END)

# Khởi tạo hàm dịch các ngôn ngữ

def translateD(test0):
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest= test0)
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)
def translateKhac(test1):
    INPUT=box.get(1.0,END)
    print (INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi", dest=test1)
    b=a.text+"\n"
    print (b)
    box1.insert(END,b)
    
#Khởi tạo nút xóa chữ và câu lệnh xóa #Đặt vị trí nút xóa chữ
clear_button=Button(Button_frame, text = "Xóa TV", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=clearTV)
clear_button.place(x=5, y= 155)

#Khởi tạo nút xóa chữ và câu lệnh xóa #Đặt vị trí nút xóa chữ
clear_button1=Button(Button_frame, text = "Xóa dịch", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#ffffff", command=clearDich)
clear_button1.place(x=5, y= 455)

# Them nut chon ngo ngu
T_D = StringVar(root)
T_D.set("Defautl...") # default value
w = OptionMenu(root, T_D, "en", "fr", "de", "ru", command=translateD)
test0=T_D
#print(T_D)
w.place(x=140, y=310)

# Them nut chon ngo ngu
T_lang = StringVar(root)
T_lang.set("Khác...") # default value
w = OptionMenu(root, T_lang,"af", "sq", "am", "hmn", "ml",
                            "pt", "pa", "ro", "hu", "mt",
                            "sn", "sd", "si", "is", "mi",
                            "sw", "sv", "tg", "ig", "mr",
                            "ar", "sk", "hy", "id", "mn",
                            "ru", "ta", "sm", "ga", "my",
                            "sl", "az", "so", "it", "ne",
                            "te", "gd", "th", "ja", "no",
                            "sr", "be", "ur", "jw", "or",
                            "es", "st", "bn", "kn", "ps",
                            "tr", "su", "ug", "kk", "fa",
                            "bs", "uk", "uz", "km", "pl",
                            "bg", "ca", "ceb", "ko", "he",
                            "cy", "ny", "xh", "ku", "hi",
                            "zh-cn", "yi", "yo", "ky", "mg",
                            "zu", "co", "hr", "lo", "ms",
                            "cs", "da", "nl", "la", "ha",
                            "eo", "tl", "fi", "lv", "haw",
                            "fy", "gl", "ka", "lt", "iw",
                            "el", "gu", "ht", "lb", "mk",
                            command=translateKhac)
test1=T_lang
#print(T_lang)
w.place(x=250, y=310)

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
