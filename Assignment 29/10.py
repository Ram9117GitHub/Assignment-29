"""Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data"""
import pickle as pk
f= open('bookfile.txt','rb')
s = pk.load(f)
for key in s:
    print(key,"....",s[key])
f.close()
"""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""
"""book_name .... Python
Price .... 400"""