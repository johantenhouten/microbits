#
# werkt voor  https://makecode.microbit.org/#editor
#
# voor het berekenen van afstand moet eerst de grove uitbreiding worden geladen
# daarna zijn grove functies beschikbaar.
#

# 
# functie die de ultrasoon sensor op de grove kit uitleest
# in dit voorbeeld is de ultrasoon sensor in PIN 1 geplaatst.
# let op dat PIN1 niet voor iets anders wordt gebruikt
# 
# de grove kit wordt niet in de online omgeving gesimuleerd.
def afstand():
    # de functie grove.measure_in_centimeters_v2 geeft een antwoord 
    # als een decimaal breuk (3.45 betekent 3 centimeter en 4.5 millimeter)
    # geeft als afstand het aantal decimeters
    cm = grove.measure_in_centimeters_v2(DigitalPin.P1) 

    # deel het aantal centimeters door 10 en neem alleen het hele gtal
    return int(cm/10)


while True:
    # als de afstand onder de 50cm komt laat een schedel zien, anders veeg scherm leeg
    if afstand() < 5:
        basic.show_icon(IconNames.SKULL)
    else:
        basic.clear_screen()
