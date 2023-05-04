import postgres_conn


def crud_operations():
    activity = ""
    user_choice = input(f"On which table would you like to perform operations?: ")
    if user_choice != "customers" and user_choice != "employees":
        print("There is no such table. Please run the program again and enter a valid one.")
    else:
        print(f"Operations: create; read; update; delete")
        activity = input(f"Which operation from the above would you like to perform?: ")

    def create():
        person = user_choice[:-1]
        customer_id = input(f"\nEnter {person}'s ID: ")
        first_name = input(f"Enter {person}'s first name: ")
        last_name = input(f"Enter {person}'s last name: ")
        email_address = input(f"Enter {person}'s email address: ")
        phone = input(f"Enter {person}'s phone number: ")
        postgres_conn.admin_client()
        postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO customers values ('{customer_id}', '{first_name}', "
                                                  f"'{last_name}', '{email_address}', '{phone}')")
        postgres_conn.POSTGRES_CONNECTION.commit()

    def read():
        postgres_conn.admin_client()
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT * FROM {user_choice};")
        all_records = postgres_conn.POSTGRES_CURSOR.fetchall()
        number_record = 1
        for record in all_records:
            print(f"{number_record}. C{user_choice[1:-1]}'s ID: {record[0]} | First name: {record[1]} | Last name: {record[2]} | "
                  f"Email address: {record[3]} | Phone number: {record[4]}")
            number_record += 1

    def update():
        try:
            column = input(f"Which column would you like to change: ")
            condition = input(f"What is the condition on which you want to make the change?: ")
            new_value = input(f"What is the new value?: ")

            postgres_conn.admin_client()
            postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE {user_choice} SET {column} = '{new_value}' WHERE {condition};")
            postgres_conn.POSTGRES_CONNECTION.commit()
            print("Updates done!")
        except (Exception) as error:
            print(f"Query is not valid.")

    def delete():
        try:
            postgres_conn.admin_client()
            condition = input(f"What is the condition on which you want to delete the record?: ")
            postgres_conn.POSTGRES_CURSOR.execute(f"DELETE FROM {user_choice} WHERE {condition};")
            postgres_conn.POSTGRES_CONNECTION.commit()
            print(f"Updates done! The record has been deleted.")
        except (Exception) as error:
            print(f"Query is not valid.")

    if activity == "create":
        create()
    elif activity == "read":
        read()
    elif activity == "update":
        update()
    elif activity == "delete":
        delete()
    else:
        print(f"There is no such operation. Please run the program again and enter a valid one.")


crud_operations()