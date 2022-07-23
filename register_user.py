#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector  

def register_user():
    user_name = str(input('input name:'))
    user_address = str(input('input address:'))
    birthdate = str(input('input birthdate (YYYY-MM-DD):'))  #data input
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="pass"
          )
        mycursor = mydb.cursor()
        
        query_register_user = f"""
          INSERT INTO lms.user(user_name, user_address, birthdate)
          VALUES('{user_name}', '{user_address}', '{birthdate}');
          """
        mycursor.execute(query_register_user)  #register new user based on input
    except Exception as err_user_regis:
        print(str(err_user_regis))

