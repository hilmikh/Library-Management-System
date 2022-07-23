#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import mysql.connector  

def find_book():
    book_title = str(input('input book title:'))
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="pass"
          )
        mycursor = mydb.cursor()
        
        query_find_book = f"""
          SELECT * FROM lms.book
          WHERE book_title='{book_title}';
          """
        df_find_book = pd.read_sql(query_find_book,mydb)
        print(df_find_book)
    except Exception as error_find_book:
        print(str(error_find_book))

