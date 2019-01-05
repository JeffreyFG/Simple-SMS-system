from tkinter import *

import boto3
import xlrd



class Jeff:
    def getData(self):
        ftypes = [('Excel Files', "*.xlsx")]
        ttl = "Enter the Excel File"
        dir1 = 'C:\\'
        file_name = self.entry_1.get()
        file_location = "C:/Users/Jeffr/Desktop/" + file_name + ".xlsx"
        # fileName = filedialog.askopenfilename(filetypes=ftypes, initialdir=dir1, title=ttl)
        message = self.entry_2.get()
        work_book = xlrd.open_workbook(file_location)
        self.sheet = work_book.sheet_by_index(0)
    def getSet(self):
        client = boto3.client('sns', 'us-west-2')
        message = self.entry_2.get()
        number_of_students = self.sheet.nrows()
        for i in range(0, number_of_students):
            id = self.sheet.cell_value(i, 0)
            last = self.sheet.cell_value(i, 1)
            first = self.sheet.cell_value(i, 2)
            phone_number = int(self.sheet.cell_value(i, 3))
            phone_number = str(phone_number)

            client.publish(PhoneNumber=phone_number,Message=str("Dear " + first + " " + last + " " + str(id) + " " + message))
    def __init__(self ):
        sheet = None
        work_Book = None
        root = Tk()
        button1 = Button(root, text="open the file", command=self.getData)
        button2 = Button(root, text="Send the text", command=self.sendData)
        button1.grid(row=3, column=1)
        button2.grid(row=2, column=1)
        theLabel = Label(root, text="This si easy")
        label_1 = Label(root, text="Name of the file no need for file extension")
        label_2 = Label(root, text="Enter the message for the studnet")
        entry_1 = Entry(root)
        entry_2 = Entry(root)
        label_1.grid(row=0)
        label_2.grid(row=1)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)

        root.mainloop()

j=Jeff()