"""Write a Python script to append list of city names in a file ‘cities.txt’"""
# append city names
def append(filename,text):
    with open(filename,'a') as f:
        f.write("%s\n"%text)
    print('Done')
append('cities.txt',"neemrana") # any time in call append function
append('cities.txt',"bahroad")