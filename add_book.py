#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector  

def add_book():
    book_id = int(input('input book id: '))
    book_title = str(input('input book title: '))
    genre = str(input('input book genre: '))
    stock = int(input('input book stock: '))  #data input

    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_add_book = f"""
          INSERT INTO lms.book(book_id, book_title, genre, stock)
          VALUES({book_id}, '{book_title}', '{genre}', {stock});
          """
        mycursor.execute(query_add_book)  #register new book based on input
        mydb.commit()
        print("...................................")
        print("book registration successful")
        print("...................................")
    except Exception as err_book_add:
        print(str(err_book_add))

