#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector  

def register_user():
    user_name = str(input('input name: '))
    birthdate = str(input('input birthdate (YYYY-MM-DD): '))  
    occupation = str(input('input occupation: ')) 
    user_address = str(input('input address: '))  #  user data input
    
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="hilmi179"
          )
        mycursor = mydb.cursor()
        
        query_register_user = f"""
          INSERT INTO lms.user(user_name, birthdate, occupation, user_address)
          VALUES('{user_name}', '{birthdate}', '{occupation}', '{user_address}');
          """
        mycursor.execute(query_register_user)  #register new user based on input
        mydb.commit()
        print("user registration successful")
    except Exception as err_user_regis:
        print(str(err_user_regis))

