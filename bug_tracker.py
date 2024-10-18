import sqlite3

# Connect to SQLite database (creates bug_tracker.db if not exists)
conn = sqlite3.connect('bug_tracker.db')
cursor = conn.cursor()

# Create the bugs table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

# Function to add a new bug
def add_bug():
    title = input("Enter bug title: ")
    description = input("Enter bug description: ")
    status = "Open"
    cursor.execute("INSERT INTO bugs (title, description, status) VALUES (?, ?, ?)",
                   (title, description, status))
    conn.commit()
    print("Bug added successfully!")

# Function to view all bugs
def view_bugs():
    cursor.execute("SELECT * FROM bugs")
    bugs = cursor.fetchall()
    print("\nBug List:")
    for bug in bugs:
        print(f"ID: {bug[0]}, Title: {bug[1]}, Description: {bug[2]}, Status: {bug[3]}")
    print()

# Function to update a bug's status
def update_bug():
    bug_id = input("Enter bug ID to update: ")
    new_status = input("Enter new status (Open/Closed): ")
    cursor.execute("UPDATE bugs SET status = ? WHERE id = ?", (new_status, bug_id))
    conn.commit()
    print("Bug status updated successfully!")

# Function to delete a bug
def delete_bug():
    bug_id = input("Enter bug ID to delete: ")
    cursor.execute("DELETE FROM bugs WHERE id = ?", (bug_id,))
    conn.commit()
    print("Bug deleted successfully!")

# Main menu loop
while True:
    print("\nSimple Bug Tracker")
    print("1. Add a Bug")
    print("2. View All Bugs")
    print("3. Update Bug Status")
    print("4. Delete a Bug")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_bug()
    elif choice == '2':
        view_bugs()
    elif choice == '3':
        update_bug()
    elif choice == '4':
        delete_bug()
    elif choice == '5':
        print("Exiting the bug tracker. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

# Close the database connection
conn.close()
