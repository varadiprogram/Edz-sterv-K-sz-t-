import time

#kérdések
magassag = int(input("Hány cm vagy?: "))
suly = int(input("Hány kg vagy?: "))
szalkasitas_vagy_tomegeles = input("Szálkásítani akarsz vagy Tömegelni?: ")

#szűnet
print("")
time.sleep(0.2)
print(".")
time.sleep(0.2)
print("..")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("")

#változat : Szálkásítás
if 130 <= magassag <= 280 and 30 <= suly <= 200 and szalkasitas_vagy_tomegeles == "Szálkásítani":
    print("Nap 1: Mell és Tricepsz\n"
    "\n"
    "Bench Press (padon fekvő nyomás) - 4 sorozat, 8-10 ismétlés\n"
    "Döntött padon történő súlyzó pressz (incline dumbbell press) - 3 sorozat, 10 ismétlés\n"
    "Döntött padon történő súlyzó mellbicepsz - 3 sorozat, 10 ismétlés\n"
    "Tricepsz nyújtás kábelről - 3 sorozat, 10 ismétlés\n"
    "Nap 2: Hát és Bicepsz\n"
    "\n"
    "Húzódzkodás - 4 sorozat, amennyi az erődből telik\n"
    "Súlyzóval történő húzódzkodás - 3 sorozat, 8-10 ismétlés\n"
    "Evezés gépen - 3 sorozat, 10 ismétlés\n"
    "Kéz súlyzóval történő összehúzása (bicepsz gyakorlat) - 3 sorozat, 10 ismétlés\n"
    "Nap 3: Láb és Váll\n"
    "\n"
    "Guggolás - 4 sorozat, 8-10 ismétlés\n"
    "Lábprés gép - 3 sorozat, 10 ismétlés\n"
    "Láb emelés (leg extension) gépen - 3 sorozat, 10 ismétlés\n"
    "Fej fölött történő súlyzó nyomás (military press) - 3 sorozat, 8-10 ismétlés\n"
    "Oldalemelés súlyzóval - 3 sorozat, 12 ismétlés\n"
    "Nap 4: Pihenő\n"
    "\n"
    "Nap 5: Ismét Mell és Tricepsz\n"
    "\n"
    "Nap 6: Ismét Hát és Bicepsz\n"
    "\n"
    "Nap 7: Ismét Láb és Váll\n"
    "\n")

#változat : Tömegelés
elif 130 <= magassag <= 280 and 30 <= suly <= 200 and szalkasitas_vagy_tomegeles == "Tömegelni":
    print("Hétfő: Mell és Tricepsz\n"
    "\n"
    "Bench Press (padon fekvő nyomás) - 4 sorozat, 8-10 ismétlés\n"
    "Döntött padon történő súlyzó pressz (incline dumbbell press) - 3 sorozat, 10 ismétlés\n"
    "Tricepsz kickback (súlyzóval) - 3 sorozat, 10 ismétlés\n"
    "Kedd: Hát és Bicepsz\n"
    "\n"
    "Húzódzkodás - 4 sorozat, amennyi az erődből telik\n"
    "Súlyzóval történő húzódzkodás - 3 sorozat, 8-10 ismétlés\n"
    "Kéz súlyzóval történő összehúzása (bicepsz gyakorlat) - 3 sorozat, 10 ismétlés\n"
    "Szerda: Pihenő\n"
    "\n"
    "Csütörtök: Láb és Váll\n"
    "\n"
    "Guggolás - 4 sorozat, 8-10 ismétlés\n"
    "Lábprés gép - 3 sorozat, 10 ismétlés\n"
    "Fej fölött történő súlyzó nyomás (military press) - 3 sorozat, 8-10 ismétlés\n"
    "Péntek: Mell és Tricepsz\n"
    "\n"
    "Bench Press (padon fekvő nyomás) - 3 sorozat, 6-8 ismétlés (nehezebb súlyokkal)\n"
    "Tricepsz nyújtás kábelről - 3 sorozat, 10 ismétlés\n"
    "Szombat: Hát és Bicepsz\n"
    "\n"
    "Húzódzkodás - 3 sorozat, amennyi az erődből telik\n"
    "Evezés súlyzóval vagy evezőgépen - 3 sorozat, 10 ismétlés\n"
    "Vasárnap: Pihenő\n")
    
#hiba estén    
else:
    print("Valamit elgépelt vagy nem érvényes adatot adott meg.")
    
#szűnet
print("")
time.sleep(1.2)
print("")
#kilépés a programmból
print("By: Váradi Zsolt 10.A")
input("Nyomj egy Entert a kilépéshez")

    

    
    
    
