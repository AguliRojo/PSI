#cw1
cw1 = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
      "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków " \
      "później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował " \
      "się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, " \
      "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na " \
      "komputerach osobistych, jak Aldus PageMaker "
#cw 2
imie = "Bartosz"
nazwisko = "Miniszewski"
# "przekazane jako indeks do 3 znaku nazwiska oraz 2 znaku imienia."
# W przykładzie jest 4 i 3 znak
litera_1 = imie[1]
litera_2 = nazwisko[2]
liczba_liter1 = 0
liczba_liter2 = 0

for i in cw1:
    if i == litera_1:
        liczba_liter1 += 1
    if i == litera_2:
        liczba_liter2 += 1

cw2 = f"W tekście jest {liczba_liter1} {litera_1} oraz {liczba_liter2} liter {litera_2}"
print(cw2)
