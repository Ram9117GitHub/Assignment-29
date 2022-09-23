"""Write a Python script to store a list of city names in a file ‘cities.txt’"""
list_of_city_names = ['Delhi','Patna','Bihar sarif']
# open file in write mode
with open('cities.txt','w') as f:
    for item in list_of_city_names:
        # write a new line
        f.write("%s\n"%item)
    print('Done')
