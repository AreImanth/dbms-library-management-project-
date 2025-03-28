# Library Management Project:


Creation of a library management database using mysql and performing operations on the database using python.


## Database Schema:

1. Admins: attributes: - ids(primary key), name, email, password, mobile_no.

2. Author: attributes: - author_id(primary key), author_name.

3. Books: Attributes: books_id(Primary Key), books_name, Author_id, catogery, books_nos, books_price.

4. Catogery: attributes: -  catogery_id(primary key), and catogery_name.

5. users: Attributes: User_id (Primary Key), Name, Email, Address, passkey, Phone Number, address.

6. Issued_books: Attributes:serial_no(primarykey),book_nos,books_name,book_author,user_id,status,issue_date.


## Relationships:

1. Author - Books (1:N or One-to-Many): One author can write multiple books. This is represented by the line connecting Author and Books, with "1" on the Author side and "N" on the Books side.

2. Books - Category (1:N or One-to-Many): One category can have multiple books.

3. Users - Issued Book (1:N or One-to-Many): One user can issue multiple books (over time, represented by multiple entries in the Issued Book table).

4. Issued Book - Books (1:1 or One-to-One): Each entry in the Issued Book table represents one specific book being issued. Note: While a book could be issued multiple times, each issuance is a separate record, hence the 1:1 relationship between the issuance record and a specific book instance. This avoids data redundancy (like storing the book name multiple times). The books_name and book_author in Issued Book might seem redundant, but they are useful for historical records even if the book's information changes in the Books table.

5. Admins: The Admins table has no direct relationship with other tables in this simplified ER diagram. It's an independent entity for managing administrative users of the system. In a more complex system, we might have relationships like "Admin adds Book" or "Admin manages User," but those are not represented in the current code.


## DATABASE CONNECTION:

The following steps are used to connect a python application to database.

1.	Import mysql.connector  module (python module used to import mysql).

2.	Create a connection object with the database.

### Syntax for connection object is:

* Connection_object() = mysql.connector.connect(host=<host_name>,user=<user_name>,password=<db_password>,database=<database_name>).

3.	Create the cursor object.

4.	Execute the queries.


## Connection:

Def connect_to_db(): establishes a connection to the mysql database using the ‘mysql.connector’ library. It uses the following connection parameters:

* ‘host’ : ‘host name’   #example= ‘localhost’

* ‘user’ : ’user name’    #example= ‘root’

* ‘password’ : ‘password’   #example = database password(or server password).

* ‘database(db)’ : ‘database name’   #example= ‘library_management’.


## Data Manipulation Functions:

* `fetch_data(query)`: Executes a given SQL query and fetches all the resulting rows. It handles database connection and cursor management. 

*  `insert_data(query, data)`: Executes an SQL INSERT query with provided data. It commits the changes to the database. 

*  `delete_data(query, data)`: Executes an SQL DELETE query with provided data. It commits the changes to the database.


## Display Function:

* `display_results(results)`: Takes a list of rows (results from a query) and prints them in a user-friendly format.


## Menu Functions:
 
 * `main_menu()`: The main program loop. It presents a menu with options to insert, delete, retrieve data, or exit.

*  `insert_menu()`: Presents a sub-menu for choosing which table to insert data into (Author, Admins, Books, Category, Users, Issued Books). It prompts the user for the necessary data and constructs the appropriate SQL INSERT query. 

* `delete_menu()`: Presents a sub-menu for choosing which table to delete data from. It prompts the user for the ID of the record to delete and constructs the SQL DELETE query. 

* `retrieve_menu()`: Presents a sub-menu for choosing which table to retrieve data from. It constructs the SQL SELECT query and displays the results.


## How to Run:

1. Install MySQL Connector: `pip install mysql-connector-python` 
2. Set up MySQL Database: Create a database named `library_manage` and create the necessary tables with appropriate columns and data types. 
3. Update Database Credentials: Modify the `connect_to_db()` function with your MySQL username, password, and database name if different. 
4. Run the Python script: `python your_script_name.py`


### Note:
1. Forks are much appreciated.
2. The entities for the database can be added or removed as for the requirements and changes can be done to the python script accordingly.
#### i will also try to upload the GUI for the project as early as possible.
