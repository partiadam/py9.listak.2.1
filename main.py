'''
2.1 Feladat
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! 
Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. 
A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. 
A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!

    O O O
    O O O
    O O O 
'''

tarolo = []

def listToString(i):
    str1 = " "
    return (str1.join(i)) 

for i in range(3):
    tarolo.append(['O' for szam in range(3)])

def ooo():
    for i in tarolo:
        print(listToString(i))

ooo()