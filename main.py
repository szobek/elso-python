from functions import show_users
from menu import show_menu
from menu_class import Menu

# show_users()
# show_menu()
menu=Menu()
menu.add_item("File")
menu.add_item("Edit")
menu.add_item("Exit")
menu.display()