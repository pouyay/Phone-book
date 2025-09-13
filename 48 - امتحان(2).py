import tkinter as tk
import csv
import os
import winsound

root = tk.Tk()
root.geometry("512x512")
root.title("دفترچه تلفن")

from tkinter import messagebox
from tkinter import Toplevel
from tkinter import PhotoImage


file_name = "contacts.csv"

#---------------------------------------------

txtName = tk.StringVar()
txtPhone = tk.StringVar()

#---------------------------------------------

bg_image = PhotoImage(file = "bg3.png.png")
bg_label = tk.Label(root , image = bg_image)
bg_label.place(x=0 , y=0 , relwidth = 1 , relheight=1)


#---------------------------------------------

def نمایش_تعداد():
    """نمایش تعداد مخاطبین با messagebox"""
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
            count = len(lines) - 1 if lines else 0  
    else:
        count = 0
    messagebox.showinfo("تعداد مخاطبین", f"تعداد مخاطبین: {count}")
    
#---------------------------------------------

def btnذخيره(event = None):
    winsound.Beep(1000, 150)
    name = txtName.get().strip()
    phone = txtPhone.get().strip()

    if not name or not phone:
        messagebox.showwarning("خطا", "لطفا همه بخش‌ها را پر کنید")
        return

    if not phone.isdigit():
        messagebox.showwarning("خطا", "شماره تلفن باید فقط شامل عدد باشد.")
        return

    if len(phone) != 8:
        messagebox.showwarning("خطا", "شماره تلفن باید دقیقاً ۸ رقم باشد.")
        return
    
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  
            for row in reader:
                if name == row[0] or phone == row[1]:
                    messagebox.showwarning("خطا", "نام یا شماره قبلاً ذخیره شده است!")
                    return

    file_exists = os.path.isfile(file_name)
    with open(file_name, mode="a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["نام کاربری", "شماره تلفن"])  
        writer.writerow([name, phone])
    messagebox.showinfo("پیام", "اطلاعات با موفقیت ذخیره شد")

    txtName.set("")
    txtPhone.set("")

#--------------------------------------------

def btnخروج():
    winsound.Beep(1000, 150)
    root.destroy()

#--------------------------------------------

def نمايشbtn():
    winsound.Beep(1000, 150)
    content = ""
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                content += " | ".join(row) + "\n\n"  
    else:
        content = "هنوز هیچ مخاطبی ذخیره نشده است."

    window = Toplevel(root)
    window.title("لیست مخاطبین")
    window.geometry("400x400")
    window.configure(bg="skyblue")

    frame = tk.Frame(window, bg="skyblue")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text_box = tk.Text(
        frame, 
        wrap="word", 
        font=("Tahoma", 14, "bold"),  
        yscrollcommand=scrollbar.set,
        bg="skyblue",
        highlightbackground="skyblue",
        highlightcolor="skyblue",
        relief="flat",
        spacing1=5, 
        spacing3=5   
    )
    
    text_box.tag_configure("center", justify='center')  
    text_box.insert("1.0", content)
    text_box.tag_add("center", "1.0", "end")
    text_box.config(state="disabled")
    text_box.pack(expand=True, fill="both")

    scrollbar.config(command=text_box.yview)
    

#----------------------------------------------


tk.Label(root,text ="نام کاربري :").grid(column = 0 , row = 0 , pady = 5 )
tk.Entry(root , textvariable=txtName ).grid(column = 1 , row = 0)

tk.Label(root,text ="شماره تلفن :").grid(column = 0 , row = 1 , pady = 10)
tk.Entry(root , textvariable=txtPhone ).grid(column = 1 , row = 1)


vcmd = (root.register(lambda P: P.isdigit() and len(P) <= 8 or P == ""), "%P")
tk.Label(root, text="شماره تلفن :").grid(column=0, row=1, pady=10)
tk.Entry(root, textvariable=txtPhone, validate="key", validatecommand=vcmd).grid(column=1, row=1)

Button1 = tk.Button(root, text = "ذخيره" , bg="green" , command = btnذخيره)
Button1.place(x = 100 , y = 101)

Button2 = tk.Button(root , text = "خروج" , bg="red" , command = btnخروج)
Button2.place(x = 200 , y = 101)

Button3 = tk.Button(root , text = "نمايش مخاطبين" , bg="yellow" , command = نمايشbtn)
Button3.place(x = 300 , y = 101)

Button4 = tk.Button(root, text="تعداد مخاطبین", font=("Tahoma", 12, "bold"), bg="blue", command=نمایش_تعداد)
Button4.place(x=180, y=150)

#-----------------------------------------------

root.bind('<Return>', btnذخيره)

root.mainloop()



# ufr-8 براي اينه که در نوشتن فارسي مشکلي نداشته باشه
# n{'-'*30} يعن ياون خط رو سي بار تکرار ميکنه
#event = None براي اينه که هم به کيبور کار کنه و هم با دکمه
