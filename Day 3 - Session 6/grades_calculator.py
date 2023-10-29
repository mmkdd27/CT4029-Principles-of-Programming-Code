import sqlite3

def table_maker():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    create_table = """
    CREATE TABLE IF NOT EXISTS grades (
        module_code TEXT,
        grade TEXT,
        CATS TEXT,
        module_name TEXT
    );
    """
    cursor.execute(create_table)
    conn.commit()
    conn.close()
table_maker()

def module_selector():
    module = str(input("""please choose a module:
     [a]-CT4010 Computers and Security
     [b]-CT4022 Principles of Cyber Forensics
     [c]-CT4029 Principles of Programming
     [d]-CT4033 Systems Design 
     [e]-CT4034 Web Development
      enter module letter here : """))

    return module.lower()


def module_translator(module):
    if module == "a":
        module_name = "Computers and Security"
        module_code = "CT4010"
        print("you chose", module_name)
        return module_code, module_name
    elif module == "b":
        module_name = "Principles of Cyber Forensics"
        module_code = "CT4022"
        print("you chose", module_name)
        return module_code, module_name
    elif module == "c":
        module_name = "Principles of Programming"
        module_code = "CT4029"
        print("you chose", module_name)
        return module_code, module_name
    elif module == "d":
        module_name = "Systems Design"
        module_code = "CT4033"
        print("you chose", module_name)
        return module_code, module_name
    elif module == "e":
        module_name = "Web Development"
        module_code = "CT4034"
        print("you chose", module_name)
        return module_code, module_name
    else:
        print("please select a module form the list ")
        module_selector()


def CATS_selector():
    CATS = int(input("how many CAT points does the module have? : "))
    if CATS == 15 or CATS == 30:
        return CATS
    else:
        print("a module can have 15 or 30 CATS points ,please reenter")
        CATS_selector()


def grades_input(CATS):
    if CATS == 15:
        grade = int(input("please enter your grade : %"))
        return grade
    elif CATS == 30:
        grade1 = int(input("please enter your grade for the first assignment : %"))
        grade2 = int(input("please enter your grade for the second assignment : %"))
        grade = (grade2 + grade1) * 0.5
        return grade


def insert_data(CATS, module_code, module_name, grade):
    conn2 = sqlite3.connect('grades.db')
    cursor2 = conn2.cursor()

    cursor2.execute("INSERT INTO grades (module_code, grade, CATS, module_name) VALUES (?, ?, ?, ?)",
                    (module_code, grade, CATS, module_name,))

    conn2.commit()
    conn2.close()


def data_entry():
    module = module_selector()
    module_code, module_name = module_translator(module)
    CATS = CATS_selector()
    grade = grades_input(CATS)
    insert_data(CATS, module_code, module_name, grade)


def gui1():
    option = str(input("""please choose an option
    [a]-enter my grades
    [b]-see my grades
    [d]-delete my grades
     [a]/[b]/[d] : """))
    option.lower()
    if option == "a" or option == "b" or option == "d":
        if option == "a":
            number_of_modules = int(input("hoe many modules do you wish to enter ? : "))
            for i in range(0, number_of_modules):
                data_entry()
        if option == "b":
            con3 = sqlite3.connect('grades.db')
            c = con3.cursor()
            c.execute("SELECT * FROM grades")
            rows = c.fetchall()
            for row in rows:
                print(row)
            con3.close()
        if option == "d":
            check = option = str(input("""please conform by writing delete  : """))
            if check == "delete":
                data_deletion()
            else:
                print(" the attempt was unsuccessful ")


    else:
        print("please enter a valid option")
        gui1()
    cont = str(input("do you wish to continue ? [y]/[n]"))
    cont.lower()
    if cont == "n" or cont == "y":
        if cont == "n":
            quit()
        elif cont == "y":
            gui1()

    else:
        print("please enter a valid option")


def data_entry():
    module = module_selector()
    module_code, module_name = module_translator(module)
    CATS = CATS_selector()
    grade = grades_input(CATS)
    insert_data(CATS, module_code, module_name, grade)
def data_deletion():
    deleter = sqlite3.connect('grades.db')
    cursor = deleter.cursor()
    drop_table = """DROP TABLE grades"""
    cursor.execute((drop_table))
    input("data was deleted")
    table_maker()

gui1()
