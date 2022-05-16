# zet radio kaneel op 1. Beide zender en ontvanger meten dezelfde kanaal gebruiken.
radio.set_group(1)


# wanneer op A wordt gedrukt
def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)


# wanneer op A wordt gedrukt
def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    if receivedNumber == 0:
        basic.show_icon(IconNames.HEART)
    elif receivedNumber == 1:
        basic.show_icon(IconNames.SKULL)
    else:
        basic.clear_screen()

radio.on_received_number(on_received_number)

