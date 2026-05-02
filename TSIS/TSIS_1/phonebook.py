import json
from connect import get_connection

def execute_query(query, params=None, fetch=True):
    conn = get_connection()
    if not conn: return None
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        if fetch:
            return cur.fetchall()
        conn.commit()
    except Exception as e:
        print(f"error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def import_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for item in data:
            name = item.get('name')
            email = item.get('email')
            bday = item.get('birthday')
            
            execute_query("CALL upsert_contact(%s, %s, %s)", (name, email, bday), fetch=False)
            print(f"Contact: {name}")
            
        print("Imported")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Import error: {e}")

def view_with_pagination():
    limit = 2 
    offset = 0
    
    while True:
        rows = execute_query("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    
        if not rows:
            print("Empty.")
        for r in rows:
            print(f"Name: {r[0]} | Mail: {r[1]}")
            
        print("\n[n] Ahead | [p] Back | [q] Exit to menu")
        choice = input("Action: ").lower()
        
        if choice == 'n':
            offset += limit
        elif choice == 'p':
            offset = max(0, offset - limit)
        elif choice == 'q':
            break

def search_contacts():
    pattern = input("Enter name or action: ")
    results = execute_query("SELECT * FROM search_contacts_by_pattern(%s)", (pattern,))
    
    if results:
        for r in results:
            print(f"Name: {r[0]} | Mail: {r[1]} | Phone: {r[2]}")
    else:
        print("Not found.")

def main():
    while True:
        print("\n MENU PHONEBOOK (TSIS 1) ")
        print("1. Contact search")
        print("2. Pagination")
        print("3. Import from JSON")
        print("0. EXIT")
        
        choice = input("Choose: ")
        
        if choice == '1':
            search_contacts()
        elif choice == '2':
            view_with_pagination()
        elif choice == '3':
            import_from_json("contacts.json")
        elif choice == '0':
            print("See ya!")
            break
        else:
            print("Wrong input.")

if __name__ == "__main__":
    main()