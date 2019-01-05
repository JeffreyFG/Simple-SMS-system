from tkinter import *

import boto3
import xlrd

root = Tk()
sheet= None

def getData():
    ftypes = [('Excel Files', "*.xlsx")]
    ttl = "Enter the Excel File"
    dir1 = 'C:\\'
    file_name=entry_1.get()
    file_location = "C:/Users/Jeffr/Desktop/" + file_name + ".xlsx"
    #fileName = filedialog.askopenfilename(filetypes=ftypes, initialdir=dir1, title=ttl)
    message = entry_2.get()
    work_book = xlrd.open_workbook(file_location)
    sheet = work_book.sheet_by_index(0)
    print("Jeff")

def sendData():
    client = boto3.client('sns', 'us-west-2')
    message=entry_2.get()
    number_of_students = sheet.nrows()
    for i in range(0, number_of_students):
        id = sheet.cell_value(i, 0)
        last = sheet.cell_value(i, 1)
        first = sheet.cell_value(i, 2)
        phone_number = int(sheet.cell_value(i, 3))
        phone_number = str(phone_number)

        client.publish(PhoneNumber=phone_number,Message=str("Dear " + first + " " + last + " " + str(id) + " " + message))



button1 = Button(root,text="open the file",command=getData)
button2 = Button(root,text="Send the text",command=sendData)
button1.grid(row=3,column=1)
button2.grid(row=2 ,column=1)
theLabel = Label(root,text="This si easy")
label_1 = Label(root,text="Name of the file no need for file extension")
label_2 = Label(root,text="Enter the message for the studnet")
entry_1= Entry(root)
entry_2= Entry(root)
label_1.grid(row=0)
label_2.grid(row=1)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

root.mainloop()















