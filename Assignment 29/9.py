"""Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)"""
import pickle as pk
# book data 
book_data = {'book_name':'Python','Price':400}
f=open('bookfile.txt','ab')
pk.dump(book_data,f)
f.close()