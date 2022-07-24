#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import mysql.connector  

def show_book():
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="pass"
          )
        mycursor = mydb.cursor()
        
        query_show_table_book = "SELECT * FROM lms.book"
        df_table_book = pd.read_sql(query_show_table_book,mydb)
        print(df_table_book)
    except Exception as error_show_book:
        print(str(error_show_book))

