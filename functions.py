users: list[str] = ["Alice", "Bob", "Charlie"]
def show_users():
    print("Felhasználók listája:")
    for user in users:
        print(f"- {user}")