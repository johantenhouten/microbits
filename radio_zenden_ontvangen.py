# 
# Voorbeeld programma voor zenden ontvangen van radio signalen met Micro:bit
# 
# Gebruik https://makecode.microbit.org/#editor en gebruikt 
# deze code werkt zowel op de zender als de ontvanger.
#
# LET OP: een "while True" lus voorkomt
# dat de radio.on_received_number(functie_radio_ontvangt_getal) werkt
# 


#
# Zender en Ontvanger meten dezelfde kanaal gebruiken.
# Kanaal is een getal tussen 1 en 255. 
# Zet radio kanaal op 13. 
#
radio.set_group(13)


#
# functie die wordt aangeroepen voor on_button_pressed
#
def button_A_pressed():
    basic.show_string("A")
    # zend bericht : getal 0
    radio.send_number(0)

#
# functie die wordt aangeroepen voor on_button_pressed
#
def button_B_pressed():
    basic.show_string("B")
    # zend bericht : getal 0
    radio.send_number(1)

#
# functie die wordt aangeroepen als de radio een getal as bericht ontvangt
#
def functie_radio_ontvangt_getal(getal):
    if getal == 0:
        basic.show_icon(IconNames.HEART)
    elif getal == 1:
        basic.show_icon(IconNames.SKULL)
    else:
        basic.clear_screen()

#
# definieer de functies die horen bij gebeurtenissen
#
radio.on_received_number(functie_radio_ontvangt_getal)
input.on_button_pressed(Button.A, button_A_pressed)
input.on_button_pressed(Button.B, button_B_pressed)

