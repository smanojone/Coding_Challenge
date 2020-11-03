import csv
import sys
import Tkinter as tk
from Tkinter import *
import tkMessageBox
import sys
import os

#The below parameters should generally be stored in a config file along with other configurations

root = tk.Tk()
v = tk.IntVar()

root.title('Add User screen')
root.geometry("500x500")
tk.Label(root, text="First Name [Mandatory]").grid(row=0, column = 0)
e1 = tk.Entry(root)
e1.grid(row=0, column = 1)

tk.Label(root, text="Last Name [Mandatory]").grid(row=1, column = 0)
e2 = tk.Entry(root)
e2.grid(row=1, column = 1)

tk.Label(root, text="Select RoleName").grid(row=2, column = 0)
#Get the role details from the role file


label1 = Label(root)
roleData_lst = GetRoles()

roleName_lst = []

#Get the rolename for the dropdown menu from the role file

for x in range(0,len(roleData_lst)):
  roleName_lst.append(roleData_lst[x]["Name"])

OptMenu = StringVar(root)
OptMenu.set(roleName_lst[0]) # default value

w = OptionMenu(root, OptMenu,*roleName_lst).grid(row=2, column=1)

#This function is called at the click of the buttion
def callback():
    #e1.delete(0,'end')
    #e2.delete(0,'end')

    global label1

    label1.destroy()

    First_Name = e1.get()
    Last_Name =  e2.get()
    Role_Name= OptMenu.get()


    #The data is picked from the UI and passed to the below function to write the employee file
    return_status = writeUserToFile(First_Name,Last_Name,Role_Name,roleData_lst)
    if return_status ==0:
      success_msg = '''User added successfully
                    '''
      tkMessageBox.showinfo(success_msg, "Information")
    elif return_status == 1:
      warning_msg =  '''FirstName or LastName Not Provided
                     '''
      tkMessageBox.showwarning(warning_msg, "Warning")
    else:
      error_msg = '''Please contact Technical Support Team
                  '''
      tkMessageBox.showerror(error_msg, "Error")




MyButton1 = Button(root, text="Submit",  width=10, command= lambda: callback())
MyButton1.grid(row=16, column=3)
myButton2 = Button(root, text='Quit',  command=root.quit).grid(row=0, column=11, sticky=W, pady=4)



root.mainloop()
