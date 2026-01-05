# tehdään skirpti joka tallentaa darts tuloksia, 3 heittoa / vuoro
# jatketaan siten että lasketaan keskiarvo 'vapaalta kierrokselta'
# nyt pisteet tallentuu vain ohjelmaan muttei tiedostoon, opetellaan tallentamaan kaikki json-filuun

import json

data = {
    'sessio_id' : 'sessio1',
    'kierrokset' : 0,
    'kierros' : [],
    'kierroksien_ka' : 0,
    'heitetyt_tikat': 0
}

json_str = json.dumps(data, indent=4)
with open('sample.json', 'w') as f:
    f.write(json_str)

print(json_str)

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
    if sum == 0:
        return None
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

data['kierrokset'] = kierroksia
data['heitetyt_tikat'] = 3 * kierroksia

with open('sample.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Tallennettu sample.json")
print(json.dumps(data, indent=4))

#TODO 
# - Aloita kierros 
# - Lopeta kierros 
# - Pelimuoto: 
# - Vapaa heittely 
# - 301/501 
# - Kellotaulu

