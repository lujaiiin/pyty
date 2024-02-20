import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
import pymysql
from tkinter import ttk



def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='', db='members_db'
    )
    return conn


class App(customtkinter.CTk):
    # ...
    def button1_command():
        
        subprocess.run(["python3", "Bc.py"], check=True)
        

class App(customtkinter.CTk):
    def __init__(root, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #placeholder for entry
        root.ph1 = tk.StringVar()
        root.ph2 = tk.StringVar()
        root.ph3 = tk.StringVar()
        root.ph4 = tk.StringVar()
        root.ph5 = tk.StringVar()
        root.ph6 = tk.StringVar()
        root.ph7 = tk.StringVar()


        root.mt_trea = ttk.Treeview(root)
        #set placehander value
        def setph(word, num):
            if num == 1:
                root.ph1.set(word)
            if num == 2:
                root.ph2.set(word)
            if num == 3:
                root.ph3.set(word)
            if num == 4:
                root.ph4.set(word)
            if num == 5:
                root.ph5.set(word)
            if num == 6:
                root.ph6.set(word)
            if num == 7:
                root.ph7.set(word)

                            
        def read():
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM member_d")
            results = cursor.fetchall()
            conn.commit()
            conn.close()
            return results

        def refreshTable():
            for data in root.mt_trea.get_children():
                root.mt_trea.delete(data)

            for array in read():
                root.mt_trea.insert(parent='', index='end', iid=array[0], text="", values=array, tag="orow")

            root.mt_trea.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
            root.mt_trea.grid(row=0, column=1, columnspan=7, rowspan=16, padx=10, pady=20)

        def add_event():
            memid=str(root.input_box_1.get())
            fname=str(root.input_box_2.get())
            lname=str(root.input_box_3.get())
            address=str(root.input_box_4.get())
            phone=str(root.input_box_5.get())
            phone1=str(root.input_box_6.get())
            phone2=str(root.input_box_7.get())
            degry=str(root.input_box_8.get())
            salary=str(root.input_box_9.get())

                    
            if (memid=="" or memid==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (phone=="" or phone==" ") or (phone1=="" or phone1==" ") or (phone2=="" or phone2==" ")or (degry=="" or degry==" ")or (salary=="" or salary==" "):
                messagebox.showinfo("Error", "please fill up the blank entry")
                return
            else:
                try:
                    conn= connection()
                    cursor=conn.cursor()
                            
                    cursor.execute("INSERT INTO member_d VALUE ('"+memid+"', '"+fname+"', '"+lname+"', '"+address+"', '"+phone+"', '"+phone1+"', '"+phone2+"', '"+degry+"', '"+salary+"') ")
                    conn.commit()
                    conn.close()
                except: 
                    messagebox.showinfo("Error", "member ID already exist")
                    return 
            refreshTable()
        
        
        def delete_event():
            desicion=messagebox.askquestion("WARRNING!!!", "Delete the selected data??")
            if desicion != "yes":
                return
            else:
                print("indelet")
                selected_item=root.mt_trea.selection()[0]
                deleteData=str(root.mt_trea.item(selected_item)['values'][0])
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM member_d WHERE MEMID='"+str(deleteData)+"'")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Error", "SORRY an error occured")
                    return
            refreshTable()
        
                
        def select_event():
            try:
                selected_item = root.mt_trea.selection()[0]
                values = root.mt_trea.item(selected_item)['values']
                
                root.input_box_1.delete(0, tk.END)  # Clear the current text
                root.input_box_1.insert(0, values[0])  # Member ID

                root.input_box_2.delete(0, tk.END)  # Clear the current text
                root.input_box_2.insert(0, values[1])  # Firstname

                root.input_box_3.delete(0, tk.END)  # Clear the current text
                root.input_box_3.insert(0, values[2])  # Lastname

                root.input_box_4.delete(0, tk.END)  # Clear the current text
                root.input_box_4.insert(0, values[3])  # Address

                root.input_box_5.delete(0, tk.END)  # Clear the current text
                root.input_box_5.insert(0, values[4])  # Phone

                root.input_box_6.delete(0, tk.END)  # Clear the current text
                root.input_box_6.insert(0, values[5])  # Phone1

                root.input_box_7.delete(0, tk.END)  # Clear the current text
                root.input_box_7.insert(0, values[6])  # Phone2
                
                root.input_box_8.delete(0, tk.END)  # Clear the current text
                root.input_box_8.insert(0, values[7])  # Phone2
                
                root.input_box_9.delete(0, tk.END)  # Clear the current text
                root.input_box_9.insert(0, values[8])  # Phone2

            
            except IndexError:
                messagebox.showinfo("Error", "Please select a data row")

        def search_event():
            memid=str(root.input_box_1.get())
            fname=str(root.input_box_2.get())
            lname=str(root.input_box_3.get())
            address=str(root.input_box_4.get())
            phone=str(root.input_box_5.get())
            phone1=str(root.input_box_6.get())
            phone2=str(root.input_box_7.get())
            degry=str(root.input_box_8.get())
            salary=str(root.input_box_9.get())
            
            
            conn= connection()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM member_d WHERE MEMID='"+
                        memid+"' or FNAME='"+
                        fname+"' or LNAME='"+
                        lname+"' or ADDRESS='"+
                        address+"' or PHONE='"+
                        phone+"' or PHONE1='"+
                        phone1+"' or PHONE2='"+
                        phone2+"' or DEGRY='"+
                        degry+"' or SALARY='"+
                        salary+"'")
            try:
                result=cursor.fetchall()
                for num in range(0,7):
                    setph(result[0][num], (num+1))
                    
                conn.commit()
                conn.close()
                
            except:
                messagebox.showinfo("Error", "No data found")       
       
        
        def update_event():
            selectedMemberid=""
            try:
                selected_item=root.mt_trea.selection()[0]
                selectedMemberid=str(root.mt_trea.item(selected_item)['values'][0])
            except:
                messagebox.showinfo("Error", "Please select a data row")
                
            memid=str(root.input_box_1.get())
            fname=str(root.input_box_2.get())
            lname=str(root.input_box_3.get())
            address=str(root.input_box_4.get())
            phone=str(root.input_box_5.get()) 
            phone1=str(root.input_box_6.get())
            phone2=str(root.input_box_7.get())
            degry=str(root.input_box_8.get())
            salary=str(root.input_box_9.get())
            
            if (memid=="" or memid==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (phone=="" or phone==" ") or (phone1=="" or phone1==" ") or (phone2=="" or phone2==" ") or (salary=="" or salary==" ") or (degry=="" or degry==" "):
                messagebox.showinfo("Error", "please fill up the blank entry")
                return
            else:
                try:
                    conn= connection()
                    cursor=conn.cursor()
                    cursor.execute("UPDATE member_d SET MEMID='"+
                    memid+"', FNAME='"+
                    fname+"', LNAME='"+
                    lname+"', ADDRESS='"+
                    address+"', PHONE='"+
                    phone+"' , PHONE1='"+
                    phone1+"', PHONE2='"+
                    phone2+"',DEGRY='"+
                    degry+"', SALARY='"+
                    salary+"' WHERE MEMID='"+
                    selectedMemberid+"' ")
                    conn.commit()
                    conn.close()
                except: 
                    messagebox.showinfo("Error", "member id already excest")
                    return   
            refreshTable()
            
        
        def reset_event():
            desicion=messagebox.askquestion("WARRNING!!!", "Delete all data??")
            if desicion != "yes":
                return
            else:
                try:
                    conn= connection()
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM member_d")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Error", "SORRY an error occured")
                    return
                
            refreshTable()
        
            
        def button2_command():
            root.withdraw()
            subprocess.run(["python3", "Employee.py"], check=True)
        
        def button3_command():
            root.withdraw()
            subprocess.run(["python3", "master.py"], check=True)
                
        def button4_command():
            root.withdraw()
            subprocess.run(["python3", "ph.py"], check=True)

        def button5_command():
            root.withdraw()
            subprocess.run(["python3", "Contract.py"], check=True)

        # configure window
        root.title("اعضاء هيئة التدريس(بكالوريس)")
        root.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        root.grid_columnconfigure(1, weight=1)  # Sidebar column
        root.grid_columnconfigure(1, weight=3)  # Main content column
        root.grid_rowconfigure(0, weight=1)  # Row for the form

        # create sidebar frame with widgets
        root.sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
        root.sidebar_frame.grid(row=0, column=0, sticky="ns")


        root.sidebar_frame.grid_rowconfigure(6, weight=1)
        root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Dash", font=customtkinter.CTkFont(size=20, weight="bold"))
        root.sidebar_button_1 = customtkinter.CTkButton(root.sidebar_frame, text="العاملين", command=button2_command)
        root.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        root.sidebar_button_2 = customtkinter.CTkButton(root.sidebar_frame, text="بكالوريس", command=root.sidebar_button_event)
        root.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        root.sidebar_button_3 = customtkinter.CTkButton(root.sidebar_frame, text="ماجستير", command=button3_command)
        root.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        root.sidebar_button_4 = customtkinter.CTkButton(root.sidebar_frame, text="دكتوراه", command=button4_command)
        root.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        root.sidebar_button_5 = customtkinter.CTkButton(root.sidebar_frame, text="متعاونين", command=button5_command)
        root.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)



        root.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=root.change_appearance_mode_event)
        
        root.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10,  10))
        root.scaling_label = customtkinter.CTkLabel(root.sidebar_frame, text="UI Scaling:", anchor="w")
        root.scaling_label.grid(row=7, column=0, padx=20, pady=(10,  0))
        root.scaling_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["100%" , "120%"],
                                                               command=root.change_scaling_event)
        root.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10,  20))





        root.main_content_frame = ctk.CTkFrame(root)
        root.main_content_frame.grid(row=0, column=1, sticky="nsew")                           
        root.mt_trea = ttk.Treeview(root.main_content_frame)
        root.mt_trea.grid(row=0, column=1, rowspan=16, padx=10, pady=20, sticky="nsew")
        refreshTable()
        root.mt_trea['columns']=("Member ID", "Firstname", "Lastname", "Address", "Phone", "Phone1", "Phone2", "Phone3", "Phone4")
        root.mt_trea.column("#0", width=0)
        root.mt_trea.column("Member ID", anchor="w", width=150)
        root.mt_trea.column("Firstname", anchor="w", width=150)
        root.mt_trea.column("Lastname",  anchor="w",width=150)
        root.mt_trea.column("Address", anchor="w",width=150)
        root.mt_trea.column("Phone", anchor="w",width=150)
        root.mt_trea.column("Phone1", anchor="w",width=150)
        root.mt_trea.column("Phone2", anchor="w",width=150)
        root.mt_trea.column("Phone3", anchor="w",width=150)
        root.mt_trea.column("Phone4", anchor="w",width=150)

        root.mt_trea.heading("Member ID", text="الرقم الوطني", anchor="w")
        root.mt_trea.heading("Firstname", text="الاسم الكامل", anchor="w")
        root.mt_trea.heading("Lastname", text="تاريخ الميلاد", anchor="w")
        root.mt_trea.heading("Address", text="المؤهل ", anchor="w")
        root.mt_trea.heading("Phone", text="تاريخ البداء", anchor="w")
        root.mt_trea.heading("Phone1", text="المدة ", anchor="w")
        root.mt_trea.heading("Phone2", text="الوظيفة", anchor="w")
        root.mt_trea.heading("Phone3", text="الدرجة", anchor="w")
        root.mt_trea.heading("Phone4", text="المرتب", anchor="w")
        refreshTable()
        

        
        # Create input text boxes
        root.input_label_1 = ctk.CTkLabel(root.main_content_frame, text="الوطني الرقم")
        root.input_label_1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_1 = ctk.CTkEntry(root.main_content_frame, placeholder_text="الوطني الرقم ")
        root.input_box_1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


        root.input_label_2 = ctk.CTkLabel(root.main_content_frame, text="الاسم الكامل")
        root.input_label_2.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_2 = ctk.CTkEntry(root.main_content_frame, placeholder_text="الكامل الاسم  ")
        root.input_box_2.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


        root.input_label_3 = ctk.CTkLabel(root.main_content_frame, text="تاريخ الميلاد")
        root.input_label_3.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_3 = ctk.CTkEntry(root.main_content_frame, placeholder_text="الميلاد تاريخ ")
        root.input_box_3.grid(row=3, column=0, padx=5, pady=5, sticky="ew")



        root.input_label_4 = ctk.CTkLabel(root.main_content_frame, text="الدرجة العلمية")
        root.input_label_4.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_4 = ctk.CTkEntry(root.main_content_frame, placeholder_text=" المؤهل ")
        root.input_box_4.grid(row=4, column=0, padx=5, pady=5, sticky="ew")



        root.input_label_5 = ctk.CTkLabel(root.main_content_frame, text="البداء تاريخ")
        root.input_label_5.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_5 = ctk.CTkEntry(root.main_content_frame, placeholder_text="البداء تاريخ")
        root.input_box_5.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        
        root.input_label_6 = ctk.CTkLabel(root.main_content_frame, text="   المدة")
        root.input_label_6.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_6 = ctk.CTkEntry(root.main_content_frame, placeholder_text="   المدة")
        root.input_box_6.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
        
        root.input_label_7 = ctk.CTkLabel(root.main_content_frame, text=" الوظيفة  ")
        root.input_label_7.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_7 = ctk.CTkEntry(root.main_content_frame, placeholder_text=" الوظيفة  ")
        root.input_box_7.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
        
        root.input_label_8 = ctk.CTkLabel(root.main_content_frame, text=" الدرجة  ")
        root.input_label_8.grid(row=8, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_8 = ctk.CTkEntry(root.main_content_frame, placeholder_text="  الدرجة ")
        root.input_box_8.grid(row=8, column=0, padx=5, pady=5, sticky="ew")
        
        root.input_label_9 = ctk.CTkLabel(root.main_content_frame, text="المرتب")
        root.input_label_9.grid(row=9, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_9 = ctk.CTkEntry(root.main_content_frame, placeholder_text="  المرتب ")
        root.input_box_9.grid(row=9, column=0, padx=5, pady=5, sticky="ew")

        # ... Repeat for the rest of the input boxes ...

        # Create buttons
        root.add_button = ctk.CTkButton(root.main_content_frame, text="اضافة", command=add_event)
        root.add_button.grid(row=11, column=0, padx=5, pady=5, sticky="ew")
        refreshTable()

        root.update_button = ctk.CTkButton(root.main_content_frame, text="تعديل", command=update_event)
        root.update_button.grid(row=12, column=0, padx=5, pady=5, sticky="ew")

        root.delete_button = ctk.CTkButton(root.main_content_frame, text="حذف", command=delete_event)
        root.delete_button.grid(row=13, column=0, padx=5, pady=5, sticky="ew")
        
        root.select_button = ctk.CTkButton(root.main_content_frame, text="تحديد", command=select_event)
        root.select_button.grid(row=14, column=0, padx=5, pady=5, sticky="ew")
        
        root.search_button = ctk.CTkButton(root.main_content_frame, text="بحث ", command=search_event)
        root.search_button.grid(row=15, column=0, padx=5, pady=5, sticky="ew")
        
        root.reset_button = ctk.CTkButton(root.main_content_frame, text="الضبط اعادة", command=reset_event)
        root.reset_button.grid(row=16, column=0, padx=5, pady=5, sticky="ew")




    def open_input_dialog_event(root):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(root, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(root, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) /  100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(root):
        print("sidebar_button click")    
         

if __name__ == "__main__":
    customtkinter.set_appearance_mode("light") 
    customtkinter.set_default_color_theme("dark-blue")  
    app = App()
    app.mainloop()
