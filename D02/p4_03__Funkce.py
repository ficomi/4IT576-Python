#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_03__Funkce.py
"""
Příkazy zadávané ve výpisech kapitoly:
P03. Funkce
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q



#Stránka 1.2.1	Příklady definice funkce
###########################################################################q
def jednořádková(): print('Volána jednořádková funkce')

def víceřádková():
    print('První příkaz')
    print('Druhý příkaz')
    print('Třetí příkaz')

jednořádková()
víceřádková()



#Stránka 1.2.2	Funkce a její atributy
###########################################################################q
def fce():  fce.call+=1;  print(f'Funkce volána {fce.call} krát')

fce.call = 0  # Atribut funkce, v němž bude pořadí volání
fce()
xxx = fce;   xxx()



#Stránka 1.2.4	Příklad: definice funkce pozdrav()
###########################################################################q
def pozdrav():
    """Zjistí požadované oslovení a popřeje dobrý den."""
    oslovení = input('Jak vás mám oslovovat? ')
    print('Dobrý den,', oslovení)

pozdrav()    # Volání definované funkce
šéfe
help(pozdrav)
pozdrav.__doc__



#Stránka 1.5	Definice prázdné funkce
###########################################################################q
def prázdná_s_dokumentací(): """Dokumentační komentář."""

def prázdná_s_výpustkou(): ...

def prázdná_s_příkazem_pass(): pass

prázdná_s_dokumentací()
prázdná_s_výpustkou()
prázdná_s_příkazem_pass()



#Stránka 1.5.1	Prázdné funkce jinak
###########################################################################q
def prázdná_s_dokumentací():
    """Popis k čemu bude tato funkce sloužit."""

def prázdná_s_výpustkou():
    ...

def prázdná_s_příkazem_pass():
    pass



#Stránka 2.2	Parametr, argument, anotace
###########################################################################q
def anot_demo(počet:int, string:str) -> str:
    return počet * string



#Stránka 2.2.1	Zjištění anotací
###########################################################################q
anot_demo.__annotations__



#Stránka 2.2.2	Příklad
###########################################################################q
def hypotenuse(a:float, b:float) -> float:
    """Vrátí přeponu pravoúhlého trojúhelníku
    se zadanými odvěsnami.
    """
    a2 = a * a
    b2 = b * b
    from math import sqrt  # Funkce pro výpočet odmocniny
    c = sqrt(a2 + b2)
    return c

print(f'{hypotenuse(3, 4) = },  {hypotenuse(12, 16) = }')
hypotenuse.__annotations__



#Stránka 2.3.1	Příklad 1 – povolená zadání
###########################################################################q
def pos_key_demo(p1, p2, p3, p4='Nezadán', p5='Nezadán'):
    """Pomocná funkce pro demonstraci možností
    zadávání argumentů."""
    print(f'{p1=}, {p2=}, {p3=}, {p4=}, {p5=}')

pos_key_demo('a1', 'a2', 'a3', 'a4')
pos_key_demo(10, 20, p5=55, p3=33)



#Stránka 2.3.2	Příklad 2 – chybné zadání
###########################################################################q
pos_key_demo(10, 30, p5=55, p2=22)



#Stránka 2.4.1	Ukázky použití funkce print()
###########################################################################q
print(1, 2, 3, sep='-', end=' - KONEC\n')
(print('Počátek', 'start', end='__'),
 print('levý-střed','střed','pravý-střed',sep='...',end='__'),
 print('konec', 'úplný konec', sep='?'))



#Stránka 2.5	Povinně poziční, resp. pojmenované argumenty
###########################################################################q
def fce(pos1, pos2=2, /, gen1=11, gen2=22, *, kwd1=111, kwd2=222):
    """První dva argumenty jsou povinně poziční,
    druhé dva nemají specifikován povinný způsob zadávání
    a poslední dva jsou povinně pojmenované.
    Povinně zadaný musí být pouze argument pos1."""
    print(f'{pos1=}, {pos2=}, {gen1=}, {gen2=}, {kwd1=}, {kwd2=}')



#Stránka 2.5.1	Příklady užití výše definované funkce
###########################################################################q
fce(1, 2, 10, 20, kwd1=110, kwd2=220)
fce(1, 2, 10, gen2=21, kwd1=111, kwd2=221)
fce(1, 2, gen1=12, gen2=22, kwd1=112, kwd2=222)



#Stránka 2.5.2	Volání funkce jako argument
###########################################################################q
def dotaz() -> str:
    return input('Jak vás mám oslovovat? ')

def pozdrav(oslovení: str) -> None:
    print(f'Dobrý den {oslovení}')

pozdrav(dotaz())
kámo



#Stránka 0.X:	Popisek
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/xxx.py
"""
#---------------------------------------------------------------------------
                                                                       #SYNC
###########################################################################q
dbg.stop_mod(1, __name__)
