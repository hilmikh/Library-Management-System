#!/usr/bin/env python
# coding: utf-8

# In[3]:
import pandas as pd
import mysql.connector  

def show_user():
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_show_table_user = "SELECT * FROM lms.user;"
        df_table_user = pd.read_sql(query_show_table_user,mydb)
        print(df_table_user)
    except Exception as error_show_user:
        print(str(error_show_user))

