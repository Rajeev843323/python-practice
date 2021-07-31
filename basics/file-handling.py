"""File handling is the most important part of any development or web application. python
have several functions for creating, reading, updating and deleting the file. 
1) open() function: this takes two parameters file name and modes. there are four
different modes for opening a file (a) "r": Read - opens a file for reading, error if 
file does not exist. (b) "a": Append - open a file for appending. if file does not exist
it creates a new file. (c) "w": Write - open a file for writing. if file does not exist
it creates a new file. (d) "x" : Create - create a specified (new) file. if file already
exist it returns an error. bydefault this considering the file location of root directory
where python file has saved """

#To open excel file and notpad file from desktop
import os
fl=r"C:/Users/kumar.rajeev/Desktop/Python_destination.txt"
fl2="C:/Users/kumar.rajeev/Desktop/BillingReport28.7.21.xlsx"
os.startfile(fl)
os.startfile(fl2)


#For web application we can write code as below to open txt file
import webbrowser
webbrowser.open("C:/Users/kumar.rajeev/Desktop/Python_destination.txt")

#Read and print excel file using pandas
import pandas as pd
df = pd.read_excel('C:/Users/kumar.rajeev/Desktop/BillingReport28.7.21.xlsx')
print(df)

#opening the image file.
from PIL import Image
img=Image.open('45229.jpg')
img.show()


#Work on txt file using file handling
#ex of default file name and its location
fl=open('Python_destination.txt')
for i in fl:
    print(i)
fl.close()

#Or
fl=open('Python_destination.txt')
print(fl.read())
fl.close()

#if file is on different location specify the path
fl=open("C:\\Users\kumar.rajeev\Desktop\Python_destination.txt",'r')
print(fl.read())
fl.close()

#Or
fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'r')
print(fl.read())
fl.close()

#Read only first 10 character from file
fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'r')
print(fl.read(10))

#return 1 line from file use readline() function 1 time for 2 line use function 2 time
fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'r')
print(fl.readline())
print(fl.readline())
print(fl.readline())
fl.close()

fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'r')
print(fl.name)
for i in fl:
    print(i)
fl.close()    

"""Write something to an existing file we are opening the file using open() method and
using parameter 'w' (write- will overwrite any exising content) and 'a' (append - will
append at end of the file)"""

fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'a')
fl.write('\nThis is the append message\nmy name is Rajeev\naddress is Patna')
fl.close()

fl=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'w')
fl.write('This is the overwrite message')
fl.close()

#create new empty text file
fl=open("createtest.txt",'x')

#copy from another file to new created file
fl1=open("createtest.txt",'a')
f2=open("C:/Users\kumar.rajeev/Desktop/Python_destination.txt",'r')
for i in f2:
    fl1.write(i)
f2.close()
fl1.close()

#delete file: to delete file we must import os module
import os
os.remove("C:/Users\kumar.rajeev/Desktop/BillingReport29.7.21Copy.xlsx")


    

    