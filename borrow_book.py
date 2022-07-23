#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector  

def borrow_book():
    id_user = int(input('input user id:'))
    user_name = str(input('input name:'))
    book_id = int(input('input book id:'))
    book_title = str(input('input book title:'))
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_add_borrow = f"""
        INSERT INTO lms.borrow(id_user, user_name, book_id, book_title, borrow_date, return_date)
        VALUES({id_user}, '{user_name}', {book_id}, '{book_title}', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 3 DAY));
        """
        mycursor.execute(query_add_borrow) #input borrowing data
    
        query_reduce_stock = f"""
        UPDATE lms.book
        SET stock = GREATEST(0, stock - 1)
        WHERE book_id = {book_id};
        """
        mycursor.execute(query_reduce_stock) #reduce stock by 1 when borrowed
    except Exception as err_borrow_book:
        print(str(err_borrow_book))

