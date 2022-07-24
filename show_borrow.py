#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import mysql.connector

def show_borrow():
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_show_table_borrow = "SELECT * FROM lms.borrow;"
        df_table_borrow = pd.read_sql(query_show_table_borrow,mydb)
        print(df_table_borrow)
    except Exception as error_show_borrow:
        print(str(error_show_borrow))

