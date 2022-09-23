"""Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.
"""
f=open('myfile.txt','w')
f.close()
def append(filename,text):
    with open(filename,'w') as f:
        f.write(text)
        print(text)
append('myfile.txt','my is name ram kumar')
append('myfile.txt','my is name raj kumar')