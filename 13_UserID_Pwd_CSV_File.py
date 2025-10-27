#Program 13 - CREATING USER-ID & PASSWORD USING CSV FILE

import csv
CSV_FILE = 'users.csv'
def create_csv():
    n = int(input("Enter number of users to add: "))
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['User_ID', 'Password'])
        for i in range(n):
            user_id = input(f"Enter User-ID for user {i+1}: ")
            password = input(f"Enter Password for {user_id}: ")
            writer.writerow([user_id, password])
    print("\nCSV file created successfully!\n")

def display_csv():
    print("\nUser-ID and Passwords stored in CSV file:")
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_password():
    uid = input("\nEnter User-ID to search: ")
    found = False
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == uid:
                print(f"Password for '{uid}' is: {row[1]}")
                found = True
                break
    if not found:
        print(f"User-ID '{uid}' not found in file.")

while True:
    print("1. Create CSV File")
    print("2. Display All Records")
    print("3. Search Password by User-ID")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        create_csv()
    elif choice == '2':
        display_csv()
    elif choice == '3':
        search_password()
    elif choice == '4':
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Please try again.")
