import pyautogui as pg
import time
import keyboard

# INSTRUKCJA
# odpal program --> najedz myszka na lewa rekawice --> kilkij ENTER --> potem najedz na prawa --> kliknij ENTER --> GOTOWE


# TUTAJ KOLORY RINGÓW (W RAZIE CZEGO TO TRZEBA POBRAC KOLORY RINGU (JESLI SIE JAKIES POJAWIA NOWE) I DOPISAC DO PONIŻSZEJ LISTY - metoda pg.pixel(x,y)

ring_colors = [
               (78, 76, 78),
               (185, 183, 185),
               (40, 39, 41),
               (196, 195, 197),
               (39, 38, 39),
               (37, 32, 115),
               (107, 0, 1),
               (36, 38, 117),
               (38, 38, 38),
               (195, 195, 195),
               (184, 184, 184),
               (77, 77, 77),
               (117, 0, 0)
               ]


print("KALIBRACJA:\n 1. ustaw kursor myszy na LEWA REKAWICE\n 2. Wcisnij Enter\n====================================")
while True:

    if keyboard.is_pressed('enter'):
        left = pg.position()

        print("OK! TERAZ PRAWA")
        time.sleep(1)
        pass

        while True:
            if keyboard.is_pressed('enter'):
                right = pg.position()

                print("SKALIBROWANO!", left, right)
                break
        break

while keyboard.is_pressed('q') == False:
    left_color = pg.pixel(left[0], left[1])
    right_color = pg.pixel(right[0], right[1])

    if left_color not in ring_colors:
        print("LEWY!")
        pg.click(left[0], left[1])
    else:
        if right_color not in ring_colors:
            print("PRAWA!")
            pg.click(right[0], right[1])