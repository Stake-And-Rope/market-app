import postgres_conn


def crud_operations():

    user_choice = input(f"On which table would you like to perform operations?: ")
    print(f"Operations: create; read; update; delete")
    activity = input(f"Which operation from the above would you like to perform?: ")

    def create():
        if user_choice == "customers":
            customer_id = input(f"\nEnter customer's ID: ")
            first_name = input(f"Enter customer's first name: ")
            last_name = input(f"Enter customer's last name: ")
            email_address = input(f"Enter customer's email address: ")
            phone = input(f"Enter customer's phone number: ")
            postgres_conn.admin_client()
            postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO customers values ('{customer_id}', '{first_name}', "
                                                  f"'{last_name}', '{email_address}', '{phone}')")
            postgres_conn.POSTGRES_CONNECTION.commit()
        elif user_choice == "employees":
            employee_id = input(f"\nEnter employee's ID: ")
            first_name = input(f"Enter employee's first_name: ")
            last_name = input(f"Enter employee's last name: ")
            email_address = input(f"Enter employee's email address: ")
            phone = input(f"Enter employee's phone number: ")
            postgres_conn.admin_client()
            postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO employees values ('{employee_id}', '{first_name}', "
                                                  f"'{last_name}', '{email_address}', '{phone}')")
            postgres_conn.POSTGRES_CONNECTION.commit()

    def read():
        pass

    if activity == "create":
        create()


crud_operations()