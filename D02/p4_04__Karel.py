#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_04__Karel.py
"""
Příkazy zadávané ve výpisech kapitoly:
P04. Balíčky, knihovny, Karel
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q



#Stránka 3.3.1	Příklady vytvoření světa s robotem
###########################################################################q
from robotcz import *
new_world(1,5)    # Prázdný svět o jednom řádku a pěti sloupcích
new_world('0123456789', # Svět o dvou řádcích a deseti sloupcích
          ' .:…∷…:. #') # s políčky obsahujícími značky nebo zeď
k = Karel()     # Umístí robota do levého dolního rohu
#_               # Tisk podpisu naposledy vytvořeného světa



#Stránka 3.5.1	Demonstrace akcí
###########################################################################q
step(k)            # Posune robota o krok vpřed
turn_left(k)       # Otočí robota vlevo
put(k); step(k)    # Položí značku a popojde
pick(k); turn_left(k); step(k)  # Zvedne, otočí se a popojde
step(k)  # Pokusí se posunout o krok vpřed do okrajové zdi



#Stránka 3.6.1	Demonstrace testů
###########################################################################q
is_wall(k)                  # Stojí čelem k okrajové zdi
turn_left(k);   is_wall(k)  # Nyní má před sebou volno
is_east(k)                  # Hledí na jih
turn_left(k);   is_east(k)  # Po otočce hledí na východ
r = Karel(-1,-2)    # Nový robot vpravo před zdí
robot_before(r)     # Před ním je zeď, ne robot => vrátí None
is_wall(r)          # Testuje neokrajovou zeď



#Stránka 3.7.1	Demonstrace zakrytí a odkrytí
###########################################################################q
turn_left(k);  turn_left(k);  turn_left(k)  # Pomalá vpravo
def turn_right(k:Karel) -> Karel:
    """Otočí zadaného robota rychle vpravo."""
    hide(k)   # Další akce budou prováděny rychle a tajně
    turn_left(k);  turn_left(k);  turn_left(k)
    unhide(k) # Vracíme se k pomalému, veřejnému provádění
    return k

k; turn_right(k)       # Rychlá otočka vpravo



#Stránka 3.7.2	Vnoření příkazů k zakrytí a odkrytí
###########################################################################q
def turn_about(k:Karel) -> Karel:
    """Otočí zadaného robota čelem vzad."""
    hide(k)    # Zapínáme zrychlené provádění
    turn_left(k);  turn_left(k)
    unhide(k)  # Vracíme se k veřejnému provádění
    return k

def step_back(k:Karel) -> Karel:
    """Udělá se zadaným robotem krok zpět."""
    hide(k)    # Zapínáme zrychlené provádění
    turn_about(k);  step(k);  turn_about(k)
    unhide(k)  # Vracíme se k veřejnému provádění
    return k

turn_about(k); step_back(r)  # První se otočí, druhý couvne



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
