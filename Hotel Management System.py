import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 1. CUSTOMER FUNCTIONS
def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    with open('customers.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, address, email])
    print("Customer added successfully!")

def view_customers():
    try:
        with open('customers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No customers found.")

def search_customer():
    name = input("Enter name to search: ")
    try:
        with open('customers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    print(row)
                    return
            print("Customer not found.")
    except FileNotFoundError:
        print("No customers found.")

# 2. ROOM FUNCTIONS
def add_room():
    room_type = input("Enter room type (Deluxe/Royal): ")
    price = input("Enter price: ")
    with open('rooms.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([room_type, price])
    print("Room added successfully!")

def view_rooms():
    try:
        with open('rooms.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No rooms found.")

# 3. BOOKING FUNCTIONS
def add_booking():
    name = input("Enter customer name: ")
    room_type = input("Enter room type (Deluxe/Royal): ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")
    price = float(input("Enter price: "))
    with open('bookings.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, room_type, check_in, check_out, price])
    print("Booking added successfully!")

def view_bookings():
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No bookings found.")

def filter_bookings():
    date = input("Enter date to filter (YYYY-MM-DD): ")
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == date:
                    print(row)
    except FileNotFoundError:
        print("No bookings found.")

# 4. SERVICE FUNCTIONS
def add_service():
    name = input("Enter customer name: ")
    service = input("Enter service (Spa/Gym/Pool): ")
    charge = float(input("Enter charge: "))
    with open('services.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, service, charge])
    print("Service added successfully!")

def view_services():
    try:
        with open('services.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No services found.")

# 5. BUFFET FUNCTIONS
def add_buffet():
    name = input("Enter customer name: ")
    items = input("Enter buffet items (comma separated): ")
    price = float(input("Enter price: "))
    with open('buffet.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, items, price])
    print("Buffet added successfully!")

def view_buffet():
    try:
        with open('buffet.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No buffet items found.")

# 6. ACTIVITIES FUNCTIONS
def add_activity():
    name = input("Enter customer name: ")
    activity = input("Enter activity (Adventure/Spa/Culture): ")
    charge = float(input("Enter charge: "))
    with open('activities.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, activity, charge])
    print("Activity added successfully!")

def view_activities():
    try:
        with open('activities.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No activities found.")

# 7. FEEDBACK FUNCTIONS
def add_feedback():
    name = input("Enter customer name: ")
    rating = input("Enter rating (1-5): ")
    comment = input("Enter comment: ")
    with open('feedback.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, rating, comment])
    print("Feedback added successfully!")

def view_feedback():
    try:
        with open('feedback.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No feedback found.")

# 8. BILLING FUNCTIONS
def generate_bill():
    name = input("Enter customer name: ")
    total = 0
    # Booking
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    total += float(row[4])
    except:
        pass
    # Services
    try:
        with open('services.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    total += float(row[2])
    except:
        pass
    # Buffet
    try:
        with open('buffet.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    total += float(row[2])
    except:
        pass
    # Activities
    try:
        with open('activities.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    total += float(row[2])
    except:
        pass

    print(f"Total bill for {name}: {total}")
    with open('bills.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, total])
    print("Bill generated successfully!")

# 9. PAYMENT FUNCTIONS
def add_payment():
    name = input("Enter customer name: ")
    amount = float(input("Enter amount paid: "))
    mode = input("Enter payment mode (Cash/Card): ")
    status = "Done"
    with open('payments.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, mode, status])
    print("Payment added successfully!")

def view_payments():
    try:
        with open('payments.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No payments found.")

# 10. REPORT FUNCTIONS
def daily_report():
    date = datetime.now().strftime("%Y-%m-%d")
    total = 0
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == date:
                    total += float(row[4])
    except:
        pass
    print(f"Daily revenue: {total}")
    plot_daily_revenue()

def monthly_report():
    month = datetime.now().strftime("%Y-%m")
    total = 0
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2].startswith(month):
                    total += float(row[4])
    except:
        pass
    print(f"Monthly revenue: {total}")
    plot_monthly_revenue()

def occupancy_report():
    total_rooms = 0
    occupied = 0
    try:
        with open('rooms.csv', 'r') as file:
            total_rooms = sum(1 for row in file)
        with open('bookings.csv', 'r') as file:
            occupied = sum(1 for row in file)
    except:
        pass
    print(f"Occupancy rate: {occupied}/{total_rooms}")

# 11. GRAPH FUNCTIONS
def plot_revenue():
    dates = []
    revenue = []
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                dates.append(row[2])
                revenue.append(float(row[4]))
    except:
        pass
    plt.plot(dates, revenue)
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.show()
    print("Revenue graph plotted successfully!")

def plot_daily_revenue():
    date = datetime.now().strftime("%Y-%m-%d")
    revenue = []
    hours = []
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == date:
                    hours.append(row[2][11:])
                    revenue.append(float(row[4]))
    except:
        pass
    plt.plot(hours, revenue)
    plt.xlabel("Hour")
    plt.ylabel("Revenue")
    plt.show()
    print("Daily revenue graph plotted successfully!")

def plot_monthly_revenue():
    month = datetime.now().strftime("%Y-%m")
    revenue = []
    days = []
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2].startswith(month):
                    days.append(row[2][8:])
                    revenue.append(float(row[4]))
    except:
        pass
    plt.plot(days, revenue)
    plt.xlabel("Day")
    plt.ylabel("Revenue")
    plt.show()
    print("Monthly revenue graph plotted successfully!")

# 12. MENUS
def customer_menu():
    while True:
        print("""
1. Add Customer
2. View Customers
3. Search Customer
4. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            search_customer()
        elif choice == '4':
            break

def room_menu():
    while True:
        print("""
1. Add Room
2. View Rooms
3. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            add_room()
        elif choice == '2':
            view_rooms()
        elif choice == '3':
            break

def booking_menu():
    while True:
        print("""
1. Add Booking
2. View Bookings
3. Filter Bookings
4. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            add_booking()
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            filter_bookings()
        elif choice == '4':
            break

def service_menu():
    while True:
        print("""
1. Add Service
2. Add Buffet
3. Add Activity
4. Add Feedback
5. Generate Bill
6. Add Payment
7. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            add_service()
        elif choice == '2':
            add_buffet()
        elif choice == '3':
            add_activity()
        elif choice == '4':
            add_feedback()
        elif choice == '5':
            generate_bill()
        elif choice == '6':
            add_payment()
        elif choice == '7':
            break

def report_menu():
    while True:
        print("""
1. Daily Report
2. Monthly Report
3. Occupancy Report
4. Plot Revenue Graph
5. Plot Daily Revenue Graph
6. Plot Monthly Revenue Graph
7. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            daily_report()
        elif choice == '2':
            monthly_report()
        elif choice == '3':
            occupancy_report()
        elif choice == '4':
            plot_revenue()
        elif choice == '5':
            plot_daily_revenue()
        elif choice == '6':
            plot_monthly_revenue()
        elif choice == '7':
            break

def view_data_menu():
    while True:
        print("""
1. View Services
2. View Buffet
3. View Activities
4. View Feedback
5. View Payments
6. Back
""")
        choice = input("Enter choice: ")
        if choice == '1':
            view_services()
        elif choice == '2':
            view_buffet()
        elif choice == '3':
            view_activities()
        elif choice == '4':
            view_feedback()
        elif choice == '5':
            view_payments()
        elif choice == '6':
            break

def main_menu():
    while True:
        print("""
1. Customer Management
2. Room Management
3. Booking Management
4. Services
5. Reports
6. View Data
7. Exit
""")
        choice = input("Enter choice: ")
        if choice == '1':
            customer_menu()
        elif choice == '2':
            room_menu()
        elif choice == '3':
            booking_menu()
        elif choice == '4':
            service_menu()
        elif choice == '5':
            report_menu()
        elif choice == '6':
            view_data_menu()
        elif choice == '7':
            break

if __name__ == "__main__":
    main_menu()