import csv
import sys
import Tkinter as tk
from Tkinter import *
import tkMessageBox
import sys
import os




root = tk.Tk()
v = tk.IntVar()

root.title('User Search Screen')
root.geometry("700x700")
tk.Label(root, text="First Name]").grid(row=0, column = 0)
e1 = tk.Entry(root)
e1.grid(row=0, column = 1)

tk.Label(root, text="Last Name").grid(row=1, column = 0)
e2 = tk.Entry(root)
e2.grid(row=1, column = 1)
e3=tk.Entry(root)
total_entry_count =0
roleName_lst = []

#Get the rolename for the dropdown menu from the role file


def callback():
    #e1.delete(0,'end')
    #e2.delete(0,'end')

  global e3
  global total_entry_count
  e3.delete(0,tk.END)

  try:
    for x in range(0,total_entry_count):
        e3.delete(0,tk.END)
        e3.grid_remove()
        e3.config()
        print('inside destroy')

    FirstName = e1.get()
    LastName =  e2.get()

    FullName = FirstName + LastName
    employee_lst = []
    #The hierarchy below the 'FullName' employee is fetched using the below function
    employee_lst = getSubOrdinates(FullName)

    #Incase there are no subordinates, a warning is issued to the UI user
    if len(employee_lst) ==0:
      warning_msg =  '''No subordinates found for the employee

                     '''
      tkMessageBox.showwarning(warning_msg, "Warning")

    # The entry list is populated using the list returned from getSubOrdinates
    elif len(employee_lst) > 0:
      cols=['Id','Name','Role']
      for y in range(0,len(employee_lst)+1):
        for x in range(len(cols)):
         if y==0:
            e3=tk.Entry(root,font=('Arial 10 bold'),bg='light green',justify='center',textvariable=str(x)+str(y))
            e3.grid(column=x, row=y+15)
            e3.insert(0,cols[x])
            total_entry_count +=1
         else:
            e3=tk.Entry(root,textvariable=str(x)+str(y))
            e3.grid(column=x, row=y+15)
            total_entry_count +=1
            if(x==0):
                e3.insert(0,employee_lst[y-1]['Id'])
            elif(x==1):
                e3.insert(0,employee_lst[y-1]['Name'])
            else:
                e3.insert(0,employee_lst[y-1]['Role'])
                                                   
    else:
      error_msg = '''Please contact Technical Support Team
                  '''
      tkMessageBox.showerror(error_msg, "Error")


  except:
   raise

   #The buttons submit and quit are created

MyButton_Search = Button(root, text="Search",  width=10, command= lambda: callback())
MyButton_Search.grid(row=16, column=15)
myButton_Quit = Button(root, text='Quit',  command=root.quit).grid(row=0, column=20, sticky=W, pady=4)


root.mainloop()
                                                   