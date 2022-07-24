# Library-Management-System
Library Management System written in Python and MySQL

## Purpose
The purpose of this project is to fulfill the 4th assignment for the python subject in pacmann data analyst bootcamp program

## Task
1. Create the main/launcher app with several function including:
   - connect to sql database and create necessary database and tables
   - receive input (what function to use) from user
   - connect to function via functionpkg.py (__init__.py)
2. Create functionpkg.py (__init__.py) to connect the main/launcher app with functions
3. Create user registration function (register_user.py), which receive input new user data and insert the data to "user" table in mysql using "INSERT INTO.." sql command
4. Create book registration function (add_book.py), which receive input new book data and insert the data to "book" table in mysql using "INSERT INTO.." sql command
5. Create borrow function (borrow_book.py), which function is:
   - receive input borrowing book data and insert the data to "borrow" table in mysql using "INSERT INTO.." sql command
   - reduce the stock value in "book" table in mysql using "UPDATE.." sql command
6. Create user book returning function (return_book.py), which function is:
   - receive input returning book data and delete the data in "borrow" table in mysql using "DELETE FROM.." sql command
   - increase the stock value in "book" table in mysql using "UPDATE.." sql command
7. Create show registered user function (show_user.py), which will print "user" table in mysql using a combination of "SELECT *.." sql command and Pandas library
8. Create show registered book function (show_book.py), which will print "book" table in mysql using a combination of "SELECT *.." sql command and Pandas library
9. Create show borrow data function (show_borrow.py), which will print "borrow" table in mysql using a combination of "SELECT *.." sql command and Pandas library
10. Create book finding function (find_book.py), which receive input of the book title and will print the searched book title in "book" table in mysql using a combination of "SELECT .. WHERE.." sql command and Pandas library

## Features
The Library Management System will have the following listed features:
1. User Management
 - register new user
 - show registered user
2. Book Catalogue Management
 - register new book
3. Book Renting Management
 - borrow book
 - return book

## How to run
1. change the mysql configuration (host, user, password) in every py file
2. start main.py

##Test Case Screenshot
1. User Management:
   - register new user
   - show registered user
![alt text](https://github.com/hilmikh/Library-Management-System/blob/main/screenshot/user_regis.PNG)
2. Book Catalogue Management
   - register new book
   - show registered book
 ![alt text](https://github.com/hilmikh/Library-Management-System/blob/main/screenshot/book_regis.PNG)
3. Book Renting Management
 - borrow book
 ![alt text](https://github.com/hilmikh/Library-Management-System/blob/main/screenshot/book_borrow.PNG)
 - return book
 ![alt text](https://github.com/hilmikh/Library-Management-System/blob/main/screenshot/book_return.PNG)
4. Find Book
 ![alt text](https://github.com/hilmikh/Library-Management-System/blob/main/screenshot/find_book.PNG)
