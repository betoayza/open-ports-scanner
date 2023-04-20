import socket
import sys

is_running = True
while is_running:
    try:
        option = int(input("""\nWhat you wanna do?:
        1. Search target
        2. Exit

        Choose: """))
        if option == 1:
            target = socket.gethostbyname(
                input("\nInsert domain or IP address: "))

            print(f"Connecting to: {target}...\n")
            for x, port in enumerate(range(1, 150)):
                # create socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)  # connection time limit
                result = s.connect_ex((target, port))
                if result == 0:  # if success
                    print(f"PORT {x}: OPEN")
                s.close()  # close socket connection

            print("\nFinished!")
        elif option == 2:
            is_running = False
        else:
            print("\n   That's not a valid option...")
    except ValueError:
        print("\n   That's not a number...")
    except:        
        print("\n   That domain/IP doesn't exist...")

# exit
print("\nThank for trying!")
sys.exit()