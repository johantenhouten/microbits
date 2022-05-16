# werkt voor nu alleen met https://makecode.microbit.org/#editor
# daar kan je extra biblitheek invoeren

#
#
def afstand():
     return grove.measure_in_centimeters_v2(DigitalPin.P1)


def on_forever():
    basic.show_number(afstand())
    music.play_tone(Note.C, music.beat())
    basic.pause(1000)


basic.forever(on_forever)
