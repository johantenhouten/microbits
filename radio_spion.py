#
# radio spion code die hoort bij opdracht 5
# laat zien hie je alle tekst beirchten op kanaal 1 afdrukt
#
# de test functie zend een leesbaar bericht op kanaal 1 (deze is nodig om in de editor
# te testen. In werkelijkheid sturen spionage apparatuur nooit berichten!
# 
#
# werkt met https://makecode.microbit.org/#editor
#




# voor de zekerheid wordt radio groep op 1 gezet
radio.set_group(1)

#
# Functie die aangeroepen wordt als een tekst bericht 
# ontvangen wordt.
#
# Deze functie toont het ontvangen bericht op de display.
#
def toon_bericht(afgeluisterd_bericht):
    basic.show_string(afgeluisterd_bericht)


#
# Functie die aangeroepen wordt als knop A ingedrukt wordt
#
# Deze functie verzend de tekst "TEST BERICHT".
#
def stuur_testbericht():
    radio.send_string("TEST BERICHT")


# definieer de functie die gekoppeld is aan knop A
radio.on_received_string(toon_bericht)

# definieer de functie die aangeropen wordt als
# een bericht wordt ontvangen
input.on_button_pressed(Button.A, stuur_testbericht)
