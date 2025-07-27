def menuitem_file():
    print("Fájl menüpont")
    # Itt lehetne fájlkezelési műveleteket végezni, pl. fájl megnyitása, mentése stb.

def menuitem_edit():
    print("Szerkesztés menüpont")
    # Itt lehetne szerkesztési műveleteket végezni, pl. szöveg módosítása, másolása stb.    

def exit_from_while():
    print("Kilépés")
    exit()


menuk={
    "file": menuitem_file,
    "edit": menuitem_edit,
    "exit": exit_from_while
}    
menupontok: list[str] = ["file", "edit"]
while True:
    print("kérlek válassz")
    for  menupont in menupontok:
        print(menupont)
    parancs = input("parancs [kilépés: exit]: ")
    fuggveny = menuk.get(parancs)
    if fuggveny:
        fuggveny()
    else:
        print("Ismeretlen parancs!")
    print()    