# tehdään skirpti joka tallentaa darts tuloksia, 3 heittoa / vuoro
# jatketaan siten että lasketaan keskiarvo 'vapaalta kierrokselta'
kierroksia = 0
lista_per_kierros = []
lista_kierroksen_tulos = []

def kierros_count(para1):
    summa = 0
    for num in para1:
        summa = summa + num
    #return summa / (len(para1)) #funktio palauttaa keskiarvon, joka tallennetaan toiseen listaan! HUOM. ka/ per tikka
    return summa
def kierros_lista_läpikäynti(para2):
    #jotain lissää
    sum = 0
    for turn in lista_kierroksen_tulos:
        sum = sum + turn
    return sum / len(lista_kierroksen_tulos)

while input('Jatka heittoja painamalla k') == 'k':
    #syötä täällä heittosi
    heitto1 = int(input('Tikka 1: '))
    heitto2 = int(input('Tikka 2: '))
    heitto3 = int(input('Tikka 3: '))
    lista_per_kierros.append(heitto1)
    lista_per_kierros.append(heitto2)
    lista_per_kierros.append(heitto3)
    lista_kierroksen_tulos.append(kierros_count(lista_per_kierros))
    print('Vuoro heitetty!!!')
    lista_per_kierros.clear()
    kierroksia += 1

print(f'Lopetit heittovuoron. Heitit yhteensä {kierroksia} kierrosta!')
print(lista_kierroksen_tulos)
print('Heittovuoron keskiarvo: ', kierros_lista_läpikäynti(lista_kierroksen_tulos))

#TODO 
# - Aloita kierros 
# - Lopeta kierros 
# - Pelimuoto: 
# - Vapaa heittely 
# - 301/501 
# - Kellotaulu

