# microbits

Voorbeeld python code voor Microbits opdrachten.

# TIPS
- als je een variabele buiten een functie definieert (denk aan aantal kattenbak bezoeken, aantal stappen, laatste gekozen bericht...), gebruik dan binnen die functie het keyword ***global***. Als je dat niet doet, creert Python een andere variabele met exact dezelfde naam 

```python
stappen = 0

def functie():
    global stappen
    stappen = stappen + 1
    
```



- als je met toetsen werkt, maak of een functie die aangeroepen wordt wanneer je op die toest drukt ***input.on_button_pressed(Button.A, functienaam)***
- definieer je functies met logische namen
- gebruik een underscore in namen die uit twee woorden bestaan. Dus bereken_aantal in plaats van berekenaantal

# Voorbeelden 
hier onder een aantal uitwerkingen van de projcten.
- <img src="https://github.com/johantenhouten/microbits/blob/main/media/robotarm.jpg" width=50% height=50%>
- <img src="https://github.com/johantenhouten/microbits/blob/main/media/kattenluik.jpg" width=50% height=50%>
- <img src="https://github.com/johantenhouten/microbits/blob/main/media/stappentellen-1.jpg" width=50% height=50%>
- <img src="https://github.com/johantenhouten/microbits/blob/main/media/stappentellen-2.jpg" width=50% height=50%>

?raw=true
