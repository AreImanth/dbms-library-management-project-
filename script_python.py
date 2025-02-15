import mysql.connector

def connect_to_db():     
    conn = mysql.connector.connect(
        host='hostname @ex- localhost',
        user='db_user_name',
        password='db_password',
        db='db_name'
    )
    return conn
print(connect_to_db)      

def fetch_data(query):        #defining a cursor for fetching the data.
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def insert_data(query, data):      #definig a function for insertion of data into the database.
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def delete_data(query, data):      #defining a function for deletion of data from the database.
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def display_results(results):     #defining a function to display the retrieved data from the database. 
    for row in results:
        print(row)
    print()

def main_menu():
    while True:
        print("Choose an operation:")
        print("1. Insert Data")
        print("2. Delete Data")
        print("3. Retrieve Data")
        print("4. Exit")
        print()
        choice = input("Enter your choice (1/2/3/4): ")
        print()

        if choice == '1':
            insert_menu()
        elif choice == '2':
            delete_menu()
        elif choice == '3':
            retrieve_menu()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

def insert_menu():
    print("Insert Data into:")
    print("1. Author")
    print("2. Admins")
    print("3. Books")
    print("4. catogery")
    print("5. users")
    print("6. issued_book")
    print()
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    print()

    if choice == '1':
        id = input("Enter author's ids: ")
        name = input("Enter author's Name: ")
        query = "INSERT INTO author (author_id, author_name) VALUES (%s, %s)"
        data = (id, name)
    elif choice == '2':
        ids = input("Enter admin's ids: ")
        Name = input("Enter admin's name: ")
        Email = input("enter the email: ")
        password = input("enter the password: ")
        mobile_no = input("enter the mobile number: ")
        query = "INSERT INTO admins (ids,Name,Email,password,mobile_no) VALUES (%s, %s,%s,%s,%s)"
        data = (ids,Name,Email,password,mobile_no)
    elif choice == '3':
        books_id = input("Enter book's id: ")
        books_name = input("Enter book's name: ")
        authors_id = input("enter the id of author: ")
        catogery_id = input("enter the catogery id: ")
        book_nos = input("enter the number of books: ")
        books_price = input("enter the price of the book: ")
        query = "INSERT INTO books (books_id,books_name,authors_id,catogery_id,book_nos,books_price) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (books_id,books_name,authors_id,catogery_id,book_nos,books_price)
    elif choice == '4':
        catogery_id = input("enter the catogery id: ")
        catogery_name = input("enter the catogery name: ")
        query = "INSERT INTO catogery (catogery_id,catogery_name) VALUES (%s,%s)"
        data = (catogery_id,catogery_name)
    elif choice == '5':
        user_id = input("enter the user's id: ")
        name = input("enter the user's name: ")
        email = input("enter the user's email please: ")
        passkey = input("enter the password of the user: ")
        phone = input("enter the phone number of user: ")
        address = input("enter the full address of user: ")
        query ="INSERT INTO users (user_id,name,email,passkey,phone,address) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (user_id,name,email,passkey,phone,address)
    elif choice == '6':
        serial_no = input("please enter the serial number of the book: ")
        book_nos = input("please enter the book number: ")
        books_name = input("please enter the name of the book: ")
        book_author = input("please enter the name of the author: ")
        user_id = input("please enter the id of the user: ")
        status = input("please enter the status(available/not available): ")
        issue_date = input("please enter the date of issue: ")
        query = "INSERT INTO issued_book(serial_no,book_nos,books_name,book_author,user_id,status,issue_date)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (serial_no,book_nos,books_name,book_author,user_id,status,issue_date)
    else:
        print("Invalid choice.")
        print()
        return
    print()

    insert_data(query, data)
    print("Data inserted successfully.")
    print()

def delete_menu():
    print("Delete Data from:")
    print("1. Author")
    print("2. Admins")
    print("3. Books")
    print("4. catogery")
    print("5. users")
    print("6. issued_book")
    print()
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    print()

    if choice == '1':
        id = input("Enter author's ID to delete: ")
        query = "DELETE FROM author WHERE author_id = %s"
    elif choice == '2':
        id = input("Enter admin's ID to delete: ")
        query = "DELETE FROM admins WHERE ids = %s"
    elif choice == '3':
        id = input("Enter book's ID to delete: ")
        query = "DELETE FROM books WHERE books_id = %s"
    elif choice == '4':
        id = input("enter the catogery;s id please: ")
        query = "DELET FROM catogery WHERE catogery_id = %s"
    elif choice == '5':
        id = input("enter the user's id please: ")
        query = "DELETE FROM users WHERE user_id = %s"
    elif choice == '6':
        id = input("enter the serial number of the book's issue: ")
        query = "DELETE FROM issued_book where serial_no = %s"
    else:
        print("Invalid choice.")
        print()
        return
    data = (id,)
    delete_data(query, data)
    print("Data deleted successfully.")
    print()

def retrieve_menu():
    print("Retrieve Data from:")
    print("1. Author")
    print("2. Admins")
    print("3. Books")
    print("4. catogery")
    print("5. users")
    print("6. issued_book")
    print()
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    print()

    if choice == '1'
        query = "SELECT * FROM author"
    elif choice == '2':
        query = "SELECT * FROM admins"
    elif choice == '3':
        query = "SELECT * FROM books"
    elif choice == '4':
        query = "select *from catogery"
    elif choice == '5':
        query = "select *from users"
    elif choice == '6':
        query = "select *from issued_book"
    else:
        print("Invalid choice.")
        print()
        return

    results = fetch_data(query)
    display_results(results)

if __name__ == "__main__":
    main_menu()
