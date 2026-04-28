import json
from connect import get_connection


def add_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")

    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    res = cur.fetchone()

    if res:
        gid = res[0]
    else:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        gid = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (name, email, birthday, gid))

    conn.commit()
    cur.close()
    conn.close()


def add_phone():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()


def move_group():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Contact name: ")
    group = input("New group: ")

    cur.execute("CALL move_to_group(%s, %s)", (name, group))

    conn.commit()
    cur.close()
    conn.close()


def search():
    conn = get_connection()
    cur = conn.cursor()

    q = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def filter_group():
    conn = get_connection()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name,
               p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = {}
    for name, email, birthday, group, phone, ptype in cur.fetchall():
        if name not in data:
            data[name] = {
                "name": name,
                "email": email,
                "birthday": str(birthday),
                "group": group,
                "phones": []
            }
        if phone:
            data[name]["phones"].append({
                "number": phone,
                "type": ptype
            })

    with open("contacts.json", "w") as f:
        json.dump(list(data.values()), f, indent=4)

    print("Exported to contacts.json")

    cur.close()
    conn.close()


def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for c in data:
        name = c.get("name")
        email = c.get("email")
        birthday = c.get("birthday")
        group = c.get("group")

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. skip/overwrite? ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (group,))
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        gid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
        """, (name, email, birthday, gid))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1.Add contact")
        print("2.Add phone")
        print("3.Move group")
        print("4.Search")
        print("5.Filter by group")
        print("6.Export JSON")
        print("7.Import JSON")
        print("0.Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            add_phone()
        elif choice == "3":
            move_group()
        elif choice == "4":
            search()
        elif choice == "5":
            filter_group()
        elif choice == "6":
            export_json()
        elif choice == "7":
            import_json()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()