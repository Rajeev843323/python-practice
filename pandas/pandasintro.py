'''Pandas is a python library used to analyze data. pandas is used for working with data
sets. pandas is using for analyzing, cleaning, exploring and manupulating data. pandas 
allows us to analyze big data and give conclusion based on statistical theories. this 
can clean messy (sisorded, dirty) data sets and make them readable and  relevent. 
relevent data is very useful in data science. '''
'''What can pandas do : pandas can check 1) Is there a corelation between 2 or more
columns. 2) What is average value. 3) Max value 4) Min value. Pandas are also able to 
delete rows that are not relevent, or containing wrong value, like empty or null values.
This is called cleaning the data. Pandas is located at the github repository. github 
enables us to make many people on the same codebase. for example'''

'''import pandas as pd
mydataset={"Cars":["BMW", "Volvo", "Ford"], "Passing":[3,7,2]}
df=pd.DataFrame(mydataset)
print(df)

#To check pandas version
print(pd.__version__)


#Pandas Series: pandas series is like a column in a table. it holds 1-D array of any type
#create a simple pandas series from a list
import pandas as pd
a=[2,4,6,8]
myvar=pd.Series(a)
df=pd.DataFrame(a)
print(myvar)
print(df)
print(myvar[0])

#Create our own label or index
a=[10,20,30,40]
myvar=pd.Series(a, index=['x','y','z', 'p'])        
print(myvar)

#Create a simpale data series from dictionary
calaries={"day1": 343, "day2": 456, "day3": 764}
a=pd.Series(calaries)
print(a)


"""Data Frame: Data frame in pandas are usually a multidimensional table. Series is like
a column and data frame is a whole table. Pandas DataFrame is a 2 Dimensional Data
structure like 2-D array, or a table with rows and columns. Bydefault Df is loading only
5 rows from starting and 5 rows from end and middle is shown with ... so if we want to 
load complete dataframe as an output we are using to_string() method with df"""
#Create Data frame from two series
import pandas as pd
data = {
    "calaries": [420, 380,390],
    "duration": [50,40,45]
}
df=pd.DataFrame(data)
print(df)

#Locate row: loc attribute is using with dataframe
#return 1st row as result it means index 0
import pandas as pd
data = {
    "calaries": [420, 380,390],
    "duration": [50,40,45]
}
df=pd.DataFrame(data)
print(df.to_string())
#print(df.loc[0])

#Return row 0 and 1 we have to use list of indexes
#print(df.loc[[0, 1]])
#print(df.loc[[0, 1, 2]])'''


#Load files data into a dataframe
import pandas as pd
#df=pd.read_csv("E:/PERSONAL/Training and Study Material\workplace/python-practice/Sample.csv")
#print(df)

data=pd.read_excel("E:/PERSONAL/Training and Study Material/workplace\python-practice/Billing Report 27.8.21.xlsx")
print(data)