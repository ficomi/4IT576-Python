#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_00b_module_template_1.py
"""
Zdroje: Prezentace

Problémy: Žádné
"""

from robotcz import *
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

def author_name() -> str:
    """Jméno Autora/Autorky modulu."""
    return 'Fico Miloslav'


def author_id() -> str:
    """Identifikační string autora/autorky modulu."""
    return 'FICM01'



# Další požadované funkce

def step_back(k:Karel) -> Karel:
    hide(k)    
    turn_left(k)
    turn_left(k)  
    step(k)
    turn_left(k)
    turn_left(k)  
    unhide(k)  
    return k

def put_left(k:Karel) -> Karel:
    hide(k)    
    turn_left(k) 
    step(k)
    put(k)
    turn_left(k)
    turn_left(k) 
    step(k)
    turn_left(k)
     
    unhide(k)  
    return k

def put_around(k:Karel) -> Karel:
    hide(k)    
    step(k)
    put(k)
    
    turn_left(k)
    step(k)
    put(k)
    
    turn_left(k)
    step(k)
    put(k)
    
    step(k)
    put(k)
    
    turn_left(k)
    step(k)
    put(k)
    
    step(k)
    put(k)
    
    turn_left(k)
    step(k)
    put(k)
    
    step(k)
    put(k)
    
    turn_left(k)
    step(k)
    
    turn_left(k)
    step(k)
    
    turn_left(k)
    turn_left(k)
     
    unhide(k)  
    return k


###########################################################################q
dbg.stop_mod(1, __name__)
