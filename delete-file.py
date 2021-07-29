import os
if os.path.exists("C:/Users\kumar.rajeev/Desktop/BillingReport29.7.21Copy.xlsx"):
    a=input('Are you sure to delete this file ! press y for yes or press n for no: ')
    if a=='y':
        os.remove("C:/Users\kumar.rajeev/Desktop/BillingReport29.7.21Copy.xlsx")
        print('File deleted')
    else:
        print('File not deleted')
else:
    print("File does not exist")


path="C:/Users/kumar.rajeev/Desktop"
name='test'

#To create a directory
os.mkdir("C:/Users/kumar.rajeev/Desktop/name1")





