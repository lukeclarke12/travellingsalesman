import matplotlib.pyplot as plt
import numpy as np

# "SpainMadrid": [+40.4167, -3.7033588],

coordinates = {
"AlbaniaTirana": [+41.3317, +19.8172104],
"AndorralaVella": [+42.5075, +1.52181409],
"AustriaVienna": [+48.2092, +16.3728170],
"BelarusMinsk": [+53.9678, +27.5766198],
"BelgiumBrussels": [+50.8371, +4.367676],
"Bosnia&HerzegovinaSarajevo": [+43.8608, +18.4214577],
"BulgariaSofia": [+42.7105, +23.3238591],
"CroatiaZagreb": [+5.8150, +15.9785130],
"CzechRepublicPrague": [+50.0878, +14.4205244],
"DenmarkCopenhagen": [+55.6763, +12.56810],
"EstoniaTallin": [59.4389, +24.754537],
"FinlandHelsinki": [+60.1699, +24.938425],
"FranceParis": [+48.8567, +2.351034],
"GermanyBerlin": [+52.5235, +13.411534],
"GreeceAthens": [+37.9792, +23.7166153],
"HungaryBudapest": [+47.4984, +19.0408102],
"IcelandReykjavik": [+64.1353, -21.895215],
"IrelandDublin": [+53.3441, -6.26758],
"ItalyRome": [+41.8955, +12.482314],
"KosovoPristina": [+42.6740,  +21.1788652],
"LatviaRiga": [+56.9465, +24.10498],
"LithuaniaVilnius": [+54.6896, +25.2799124],
"LuxembourgLuxembourg": [+49.6100, +6.1296273],
"MaltaValletta": [+35.9042, +14.51890],
"MoldovaChisinau": [+47.0167, +28.849780],
"MontenegroPodgorica": [+42.4602, +19.259561],
"NetherlandsAmsterdam": [+52.3738, +4.89101],
"NorthMacedoniaSkopje": [+42.0024, +21.4361243],
"NorwayOslo": [+59.9138, +10.738712],
"PolandWarsaw": [+52.2297, +21.012293],
"PortugalLisbon": [+38.7072, -9.135515],
"RomaniaBucharest": [+44.4479, +26.097970],
"RussiaMoscow": [+55.7558, +37.6176124],
"SanMarinoSanMarino": [+43.9424, +12.4578328],
"SerbiaBelgrade": [+44.8048, +20.4781116],
"SlovakiaBratislava": [+48.2116, +17.1547131],
"SloveniaLjubljana": [+46.0514, +14.5060281],
"SwedenStockholm": [+59.3328, +18.064515],
"SwitzerlandBern": [+46.9480, +7.4481513],
"UkraineKiev": [+50.4422, +30.5367168],
"UnitedKingdomLondon": [+51.5002, -0.126214]
}


import haversine as hs

l = []

currentcity = [+40.4167, -3.7033588]


def next_city(current, availablecities):
    c += 0
    l = []

    for i in availablecities:
        d = hs.haversine(current, availablecities[i])
        l.append(d)




<<<<<<< HEAD
=======
    min_value = l[0]
    min_index = 0
>>>>>>> 4c2e150996caedb4407f127bd34305019563a58a

    for i, value in enumerate(l):
        if value < min_value:
            min_value = value
            min_index = i
            c += co

    closestcity = list(availablecities.keys())[min_index]

    current = closestcity

<<<<<<< HEAD
closetcity = list(coordinates.keys())[min_index]
=======
    print(current)
>>>>>>> 4c2e150996caedb4407f127bd34305019563a58a

    availablecities.pop(closestcity)

<<<<<<< HEAD
currentcity = coordinates[closestcity]

print(currentcity)

coordinates.pop(closestcity)

print(coordinates)
=======
    return (coordinates[current], availablecities)

current = [+40.4167, -3.7033588]
city_dict = coordinates.copy()
>>>>>>> 4c2e150996caedb4407f127bd34305019563a58a
