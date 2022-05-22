# Add your Python code here. E.g.
from microbit import *
import radio


# zet de radio aan en zet het kanaal op 1
radio.on()
radio.config(channel = 1)




geheim = 7
boodschap = "De ooievaar zit op het nest."

#
# functie voor het versleutelen van een bericht.
# 
def versleutel(bericht):
    versleuteld_bericht = ""
    # neem elke letter uit het bericht
    for letter in bericht:
        # met ord() zet je een letter om in een ASCII code, 
        # ord("A") geeft 65
        # met het getal kunnen we iets doen
        # met chr() zet je een coe weer om in een letter
        # ord(65) geeft "A"
        letter_code = ord(letter)
        letter_code = letter_code + geheim
        letter = chr(letter_code)
        versleuteld_bericht = versleuteld_bericht + letter

    return versleuteld_bericht 


while True:
    display.scroll(versleutel(boodschap))
    display.show(Image.HEART)
    sleep(2000)
