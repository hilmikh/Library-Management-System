#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector  

def return_book():
    id_user = int(input('input user id:'))
    book_id = int(input('input book id:'))
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_del_borrow = f"""
          DELETE FROM lms.borrow
          WHERE id_user={id_user} AND book_id={book_id};
          """
        mycursor.execute(query_del_borrow) #delete borrowing data
    
        query_increase_stock = f"""
          UPDATE lms.book
          SET stock = GREATEST(0, stock + 1)
          WHERE book_id = {book_id};
          """
        mycursor.execute(query_increase_stock) #increase stock by 1 when borrowed
    except Exception as err_return_book:
        print(str(err_return_book))

