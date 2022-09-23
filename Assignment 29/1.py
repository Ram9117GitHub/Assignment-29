"""Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d.  Name of the file
"""
f=open('test.txt','w') #Which file opening mode is used
f.write("Be a good listener")
f.close() # b. Whether a file is closed or not
# a. Whether a file is read only
def reading(filename):
    try:
        f=open(filename,'r')
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("File doesn't exists")
reading('test.txt')
# Name of the file
import os 
os.rename('test.txt','file2.txt')


