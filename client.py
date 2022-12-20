import socket
import employees

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# get local machine name
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    # get employee id
    print("What is the employee id?")
    query_id = input()
    send(query_id)


    # first id
    if query_id == "E00123":
        # income
        while True:
            print("Salary (S) or Annual Leave (L) Query")
            query_income_1 = input()
            send(query_income_1)
            # salary
            if query_income_1.lower() == "s":
                while True:
                    print("Current salary (C) or total salary (T) for year?")
                    query_income_2 = input()
                    send(query_income_2)
                    # current salary
                    if query_income_2.lower() == "c":
                        print(f"Employee {employees.get_name('E00123')}")
                        print(f"Current basic salary: {employees.get_salary('E00123')}")
                        break
                    # total salary
                    elif query_income_2.lower() == "t":
                        while True:
                            print("What year?")
                            query_income_3 = input()
                            send(query_income_3)
                            if query_income_3 == '2018':
                                print(f"Employee {employees.get_name('E00123')}:")
                                print(f"Total Salary for 2018: Basic pay, {employees.get_salary('E00123')};"
                                      f" Overtime, {int((employees.get_salary('E00123') * 0.05))}")
                                break
                            else:
                                print("Please enter a valid year... eg: 2018")
                        break
                    else:
                        print("Please enter a valid command")
                        continue
                break
            # annual leave
            elif query_income_1.lower() == "l":
                while True:
                    print("Current Entitlement (C) or Leave taken for year (Y)")
                    query_income_4 = input()
                    send(query_income_4)
                    # leave taken
                    if query_income_4.lower() == "y":
                        while True:
                            print("What year?")
                            query_income_5 = input()
                            send(query_income_5)
                            if query_income_5 == '2016':
                                print(f"Employee {employees.get_name('E00123')}")
                                print(f"Leave taken in 2016: {employees.get_leave_taken('E00123', 2016)} day/s")
                                break
                            else:
                                print("Please enter a valid year... eg: 2016")
                        break
                    # current entitlement
                    elif query_income_4.lower() == "c":
                        print(f"Employee {employees.get_name('E00123')}:")
                        print(f"Current annual leave entitlement: {employees.get_annual_leave('E00123')} day/s")
                        break
                    else:
                        print("Please enter a valid command")
                        continue
                break
            else:
                print("Please enter a valid command")
                continue

    # second id
    elif query_id == "E01033":
        # income
        while True:
            print("Salary (S) or Annual Leave (L) Query")
            query_income_1 = input()
            send(query_income_1)
            # salary
            if query_income_1.lower() == "s":
                while True:
                    print("Current salary (C) or total salary (T) for year?")
                    query_income_2 = input()
                    send(query_income_2)
                    # current salary
                    if query_income_2.lower() == "c":
                        print(f"Employee {employees.get_name('E01033')}")
                        print(f"Current basic salary: {employees.get_salary('E01033')}")
                        break
                    # total salary
                    elif query_income_2.lower() == "t":
                        while True:
                            print("What year?")
                            query_income_3 = input()
                            send(query_income_3)
                            if query_income_3 == '2018':
                                print(f"Employee {employees.get_name('E01033')}:")
                                print(f"Total Salary for 2018: Basic pay, {employees.get_salary('E01033')}; Overtime,"
                                      f" {int((employees.get_salary('E01033') * 0.05))}")
                                break
                            else:
                                print("Please enter a valid year... eg: 2018")
                        break
                    else:
                        print("Please enter a valid command")
                        continue
                break
            # annual leave
            elif query_income_1.lower() == "l":
                while True:
                    print("Current Entitlement (C) or Leave taken for year (Y)")
                    query_income_4 = input()
                    send(query_income_4)
                    # leave taken
                    if query_income_4.lower() == "y":
                        while True:
                            print("What year?")
                            query_income_5 = input()
                            send(query_income_5)
                            if query_income_5 == '2016':
                                print(f"Employee {employees.get_name('E01033')}")
                                print(f"Leave taken in 2016: {employees.get_leave_taken('E01033', 2016)} day/s")
                                break
                            else:
                                print("Please enter a valid year... eg: 2016")
                        break

                    # current entitlement
                    elif query_income_4.lower() == "c":
                        print(f"Employee {employees.get_name('E01033')}:")
                        print(f"Current annual leave entitlement: {employees.get_annual_leave('E01033')} day/s")
                        break
                    else:
                        print("Please enter a valid command")
                        continue
                break
            else:
                print("Please enter a valid command")
                continue
    else:
        print("Sorry... I don't recognise that employee id")
        continue

    # continue or exit
    print("Would you like to continue (C) or exit (X)?")
    query_x = input()
    if query_x.lower() == "x":
        break
    elif query_x.lower() == "c":
        continue

send(DISCONNECT_MESSAGE)
