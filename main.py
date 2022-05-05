from tkinter import *
from tkinter import ttk
import win32com.client

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root=Tk()
root.title('Removable Devices')
# Set the size of the window
root.geometry("700x350")
lst = []
wmi = win32com.client.GetObject ("winmgmts:")
props = ['Access', 'Availability', 'BlockSize', 'Caption','CreationClassName','Description', 'DeviceID', 'DriveType', 'ErrorCleared', 'ErrorDescription', 'ErrorMethodology', 'FileSystem', 'FreeSpace','MaximumComponentLength', 'MediaType','Name','NumberOfBlocks', 'PNPDeviceID', 'Path_','Size','Status','SystemCreationClassName', 'SystemName', 'VolumeDirty', 'VolumeName', 'VolumeSerialNumber']
for i, usb in enumerate(wmi.InstancesOf("Win32_LogicalDisk")):
    if usb.drivetype==2:
        lst.append(usb)

options=["["+i.name[0]+"]:"+i.VolumeName for i in lst]
# Function to print the index of selected option in Combobox
def callback(*arg):
    for i in frame.winfo_children():
        i.destroy()
    current = lst[cb.current()]
    for i,e in enumerate(props):
        # print("{}: {}".format(e, eval("current.{}".format(e))))
        Label(frame, text=e).grid(row=i, column=1)
        Label(frame, text="{}".format(eval("current.{}".format(e)))).grid(row=i,column=2)
# Create a combobox widget
var= StringVar()
cb= ttk.Combobox(root, textvariable= var)
cb['values']= options
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)

myframe=Frame(root,relief=GROOVE)
myframe.pack(fill='x')

canvas=Canvas(myframe, bg="white", height=1000, width=1000)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(fill='x',side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

root.mainloop()
