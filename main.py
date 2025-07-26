# print("elsó sor")
# data="other"
# val = input(f"második sor {data}")
# print("harmadik sor", val)
menupontok: list[str] = ["1. pont", "2. pont", "3. pont", "4. pont", "5. pont", "6. pont", "7. pont", "8. pont", "9. pont", "10. pont"]
while True:
    print("kérlek válassz")
    for  menupont in menupontok:
        print(menupont)
   
    match input("kérlek válassz egy menüpontot: "):
        case '1':
            print("1. pont")
        case '2':
            print("2. pont")
        case '3':
            print("3. pont")
        case '4':
            print("4. pont")
        case '5':
            print("5. pont")
        case '6':
            print("6. pont")
        case '7':
            print("7. pont")
        case '8':
            print("8. pont")
        case '9':
            print("9. pont")
        case '10':
            print("10. pont")
        case "k":
            print("Kilépés")
            break
        case _:
            print("Nincs ilyen menüpont")