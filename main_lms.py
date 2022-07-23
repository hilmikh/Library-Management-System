import mysql.connector              
import pandas as pd
import functionpkg

try:  # establish connection to mysql
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hilmi179"
        )
    mycursor = mydb.cursor()
    print("MySQL Database connection successful")
except Exception as error_connection:
    print(str(error_connection))

try:  # create necessary database and tables
    query_choose_db = "USE lms;"
    mycursor.execute(query_choose_db)  
    
    query_create_db = "CREATE DATABASE IF NOT EXISTS LMS;"
    mycursor.execute(query_create_db)  # create lms database

    query_create_table_user = """
      CREATE TABLE IF NOT EXISTS user(
      id_user INT AUTO_INCREMENT PRIMARY KEY,
      user_name VARCHAR(45),
      user_address VARCHAR(100),
      birthdate DATE
    );
    """
    mycursor.execute(query_create_table_user)  # create table: user

    query_create_table_book = """
      CREATE TABLE IF NOT EXISTS book(
      book_id INT PRIMARY KEY,
      book_title VARCHAR(100),
      genre VARCHAR(45),
      stock INT
    );
    """
    mycursor.execute(query_create_table_book)  # create table: book

    query_create_table_borrow = """
      CREATE TABLE IF NOT EXISTS borrow(
      id_user INT,
      user_name VARCHAR(45),
      book_id INT,
      book_title VARCHAR(100),
      borrow_date DATE,
      return_date DATE
    );
    """
    mycursor.execute(query_create_table_borrow)  # create table: borrow

    query_add_fk = """
      ALTER TABLE borrow
      ADD FOREIGN KEY (id_user) REFERENCES user(id_user),
      ADD FOREIGN KEY (book_id) REFERENCES book(book_id);
    """
    mycursor.execute(query_add_fk)  # add foreign key: id_user and book_id
    print("MySQL Database and Tables Initialization successful")
except Exception as error_initialize:
    print(str(error_initialize, " exiting program..."))
    exit()
    
print(".....Library Management System.....\n"
      "  1. Register New User\n"
      "  2. Register New Book\n"
      "  3. Borrow Book\n"
      "  4. Return Book\n"
      "  5. Show Registered User\n"
      "  6. Show Book Catalogue\n"
      "  7. Show Book Borrowing Transaction\n"
      "  8. Find Book\n"
      "  9. Exit\n"
      )
while True:
    pick_function = int(input("pick a function (1-9)"))
    if pick_function<1 or pick_function>9:
        print("only pick number between 1-9!")
        continue
    elif pick_function==1:
        functionpkg.register_user()
        continue
    elif pick_function==2:
        functionpkg.add_book()
        continue
    elif pick_function==3:
        functionpkg.borrow_book()
        continue
    elif pick_function==4:
        functionpkg.return_book()
        continue
    elif pick_function==5:
        functionpkg.show_user()
        continue
    elif pick_function==6:
        functionpkg.show_book()
        continue
    elif pick_function==7:
        functionpkg.show_borrow()
        continue
    elif pick_function==8:
        functionpkg.find_book()
        continue
    elif pick_function==9:
        break
exit()

