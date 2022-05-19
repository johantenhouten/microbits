# Basis programma stappen teller
stappen = 0

# toon het aantal stappen voor halve seconde
def toon_getal():
    global stappen
    basic.show_number(stappen)
    basic.pause(500)
    basic.clear_screen()


# zet aantal stappen op 0
def reset_getal():
    global stappen
    stappen = 0

#verhoog aantal stappen met 1
def een_stap():
    global stappen
    stappen = stappen + 1



# wijs functies toe aan knoppen en beweging
input.on_button_pressed(Button.A, toon_getal)
input.on_button_pressed(Button.B, reset_getal)
input.on_gesture(Gesture.SHAKE, een_stap)
