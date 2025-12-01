# Zadanie Dodatkowe           
def trajkant(a,b,c):          
    cyfry = [a,b,c]     
    cyfry.sort()   
    duza = cyfry[2]
    reszta = cyfry[:2]
    if sum(reszta) > duza:
        return True
    else:
        return False
