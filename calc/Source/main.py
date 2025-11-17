print("Kalkulačka pravého úhlu by Roman Suk in Python [Verze 7.2 Final version]")
print("Copyright <c> 2020 Roman Cooperation. Všechna práva vyhrazena.")
print("V případě chyb napište na roman.suk05@gmail.com\n")
def recursive_main():
    try:
        a = float(input("Zadejte stranu <a> trojúhelníku v centimetrech (např.: 12.5): "))
    except ValueError:
        print("Zadaná hodnota nebylo číslo! Napište trojci číslic znovu.")
        recursive_main()
    try:
        b = float(input("Zadejte stranu <b> trojúhelníku v centimetrech (např.: 12.5): "))
    except ValueError:
        print("Zadaná hodnota nebylo číslo! Napište trojci číslic znovu.")
        recursive_main()
    try:
        c = float(input("Zadejte stranu <c> trojúhelníku v centimetrech (např.: 12.5): "))
    except ValueError:
        print("Zadaná hodnota nebylo číslo! Napište trojci číslic znovu.")
        recursive_main()
    strana_je_mensi = c <= a or c <= b
    if strana_je_mensi:
        print()
        print("Strana <c> musí být největší! ")
    print()
    print("a2 + b2 = c2")
    print(a**2, "+", b**2, "=", c**2)
    print(a**2 + b**2, "=", c**2)
    cislo_je_spravne = a**2 + b**2 == c**2
    if cislo_je_spravne:
        print("Trojúhelník je pravoúhlý, protože se", a**2 + b**2, end=" ")
        print("cm rovná s(e)", c**2, "cm.\n")
    else:
        print("Trojúhelník není pravoúhlý, protože se", a**2 + b**2, end=" ")
        print("cm nerovná s(e)", c**2, "cm.\n")
    recursive_answer()
def recursive_answer():
    odpoved = input("Chcete pokracovat? Pro pokračování = <Ano> pro konec = <Ne>: ")
    if odpoved == "Ano":
        recursive_main()
    elif odpoved == "Ne":
        print("Děkuji za použití")
        exit()
    else:
        print("Program nepochopil vaší odpověd, použíte <Ano> nebo <Ne>. ")
        print()
        recursive_answer()
recursive_main()