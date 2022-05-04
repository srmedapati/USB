from tkinter import *
import win32com.client
 
class Table:
    def __init__(self,root):
        # code for creating table
        for i in range(total_rows):
            val=0
            for j in range(total_columns+1):
                val+=1
                if j==total_columns:
                    self.e=Button(root, text ="Properties", command = getProp(lst[j-1]))
                    self.e.grid(row=i, column=j)
                else:
                    self.e = Entry(root,width=15*val,fg='black',font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
def getProp(desc):
    sub_win=Tk()
    print(desc)

lst=[]
root = Tk()
wmi = win32com.client.GetObject ("winmgmts:")
for i, usb in enumerate(wmi.InstancesOf("Win32_USBHub")):
    lst.append((i+1,usb.name,usb.DeviceID))
total_rows = len(lst)
total_columns = len(lst[0])
t = Table(root)
root.mainloop()
