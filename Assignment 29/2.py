"""Write a Python script to create a new file ‘myfile.txt’ and store user entered text."""
f=open('myfile.txt','w')
f.close()
def writing(filename,text):
    with open(filename,'w') as f:
        f.write(text)
writing('myfile.txt','my is name ram kumar')