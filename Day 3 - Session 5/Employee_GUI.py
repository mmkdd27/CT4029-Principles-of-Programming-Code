import tkinter
import sqlite3

def create_table():
    conn = sqlite3.connect('self_register.db')
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def register_user():
    def save():
        user_id = id_entry.get()
        user_name = name_entry.get()
        user_email = email_entry.get()
        plaintext_password = password_entry.get()

        conn = sqlite3.connect('self_register.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO employees (id, name, email, password) VALUES (?, ?, ?, ?)",
                       (user_id, user_name, user_email, plaintext_password))
        conn.commit()
        conn.close()
        print("User registered successfully!")

    registeration = tkinter.Tk()
    registeration.title("Employee Registration")

    id_label = tkinter.Label(registeration, text="Enter employee id here:")
    id_label.pack()
    id_entry = tkinter.Entry(registeration)
    id_entry.pack()

    name_label = tkinter.Label(registeration, text="Enter your name here:")
    name_label.pack()
    name_entry = tkinter.Entry(registeration)
    name_entry.pack()

    email_label = tkinter.Label(registeration, text="Enter your email here:")
    email_label.pack()
    email_entry = tkinter.Entry(registeration)
    email_entry.pack()

    password_label = tkinter.Label(registeration, text="Enter your password here:")
    password_label.pack()
    password_entry = tkinter.Entry(registeration, show='*')
    password_entry.pack()

    register_button = tkinter.Button(registeration, text="Register", command=save)
    register_button.pack(pady=5)

    registeration.mainloop()

def check_access():
    def verify_access():
        user_input = input_entry.get()
        user_password = password_entry.get()
        conn = sqlite3.connect('self_register.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=? OR name=? OR email=?", (user_input, user_input, user_input))
        user_record = cursor.fetchone()

        if user_record:
            stored_password = user_record[3]
            if user_password == stored_password:
                print("Access Granted")
            else:
                print("Access Denied")
        else:
            print("Access Denied")

        conn.close()

    access_window = tkinter.Tk()
    access_window.title("Access Verification")

    input_label = tkinter.Label(access_window, text="Enter employee id, Name, or Email:")
    input_label.pack()
    input_entry = tkinter.Entry(access_window)
    input_entry.pack()

    password_label = tkinter.Label(access_window, text="Enter Password:")
    password_label.pack()
    password_entry = tkinter.Entry(access_window, show='*')
    password_entry.pack()

    verify_button = tkinter.Button(access_window, text="Verify Access", command=verify_access)
    verify_button.pack(pady=5)

    access_window.mainloop()

create_table()
register_user()
check_access()
