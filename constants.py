from enum import Enum

class Nakshatra(Enum):
    Ashwini = 1
    Bharani = 2 
    Krittika = 3
    Rohini = 4
    Mrigashirsa = 5
    Ardra = 6
    Punarvasu = 7
    Pushya = 8
    Ashlesha = 9
    Magha = 10
    Purva_Phalguni = 11
    Uttara_Phalguni = 12
    Hasta = 13
    Chitra = 14
    Swati = 15
    Vishika = 16
    Anuradha = 17
    Jyestha = 18
    Mula = 19
    Purva_Ashadha = 20
    Uttara_Ashadha = 21
    Shravana = 22
    Dhanishta = 23
    Shatabhisha = 24
    Purva_Bhadrapada = 25
    Uttara_Bhadrapada = 26
    Revati = 27
    Abhijit = 28

class Rashi(Enum):
    Aries = 1
    Tauras = 2
    Gemini = 3
    Cancer = 4
    Leo = 5
    Virgo = 6
    Libra = 7
    Scorpios = 8
    Sagittarius = 9
    Capricorn = 10
    Aquarius = 11
    Pisces = 12

class Planet(Enum):
    Sun = 1
    Moon = 2 
    Mars = 3
    Merc = 4
    Jup = 5
    Ven = 6
    Sat = 7
    Rahu = 8
    Ketu = 9

class RelationShip(Enum):
    Friend = 1
    Neutral = 2 
    Enemy = 3
    
FireSign = [Rashi.Aries,Rashi.Leo,Rashi.Sagittarius]
EarthSign = [Rashi.Tauras,Rashi.Virgo,Rashi.Capricorn]
AirSign = [Rashi.Gemini,Rashi.Libra, Rashi.Aquarius]
WaterSign = [Rashi.Cancer,Rashi.Scorpios,Rashi.Pisces]

def getNakshatra(moonFullDegree):
    return Nakshatra(1 + int(moonFullDegree*60/800))

def getSignAndDegree(fullDegree):
    if fullDegree >360:
        fullDegree = FullDegree%360
    sign = 1+ (fullDegree/30)
    sign_int = int(sign)
    sign_Rashi = Rashi(sign_int)
    Sign_remainder = sign-sign_int
    assert (sign_Rashi.value >=1 and sign_Rashi.value <=12) , "Rashi is out of range"
    return sign_Rashi, Sign_remainder*30


def getLord(fullDegree):
    signRashi, signDegree = getSignAndDegree(fullDegree)
    if signRashi in [Rashi.Aries, Rashi.Scorpios]:
        return Planet.Mars
    elif signRashi in [Rashi.Tauras, Rashi.Libra]:
        return Planet.Ven
    elif signRashi in [Rashi.Gemini, Rashi.Virgo]:
        return Planet.Merc
    elif signRashi == Rashi.Cancer:
        return Planet.Moon
    elif signRashi == Rashi.Leo:
        return Planet.Sun
    elif signRashi in [Rashi.Sagittarius, Rashi.Pisces]:
        return Planet.Jup
    elif signRashi in [Rashi.Capricorn, Rashi.Aquarius]:
        return Planet.Sat
    else: 
        return None

def getFriendsPlanets(planet):
    if planet == Planet.Sun:
        return [Planet.Moon, Planet.Mars, Planet.Jup]
    elif planet == Planet.Moon:
        return [Planet.Merc, Planet.Sun]
    elif planet == Planet.Mars:
        return [Planet.Moon, Planet.Sun, Planet.Jup]
    elif planet == Planet.Merc:
        return [Planet.Ven, Planet.Sun]
    elif planet == Planet.Jup:
        return [Planet.Moon, Planet.Sun, Planet.Mars]
    elif planet == Planet.Ven:
        return [Planet.Merc, Planet.Sat]
    elif planet == Planet.Sat:
        return [Planet.Merc, Planet.Ven]
    else: 
        return []

def getNeutralsPlanets(planet):
    if planet == Planet.Sun:
        return [Planet.Merc]
    elif planet == Planet.Moon:
        return [Planet.Mars,Planet.Jup,Planet.Ven,Planet.Sat]
    elif planet == Planet.Mars:
        return [Planet.Ven, Planet.Sat]
    elif planet == Planet.Merc:
        return [Planet.Mars, Planet.Jup, Planet.Sat]
    elif planet == Planet.Jup:
        return [Planet.Sat]
    elif planet == Planet.Ven:
        return [Planet.Mars, Planet.Jup]
    elif planet == Planet.Sat:
        return [Planet.Jup]
    else: 
        return []

def getEnemiesPlanets(planet):
    if planet == Planet.Sun:
        return [Planet.Ven, Planet.Sat]
    elif planet == Planet.Moon:
        return []
    elif planet == Planet.Mars:
        return [Planet.Merc]
    elif planet == Planet.Merc:
        return [Planet.Moon]
    elif planet == Planet.Jup:
        return [Planet.Merc,Planet.Ven]
    elif planet == Planet.Ven:
        return [Planet.Sun, Planet.Moon]
    elif planet == Planet.Sat:
        return [Planet.Sun, Planet.Moon, Planet.Mars]
    else: 
        return []

def getRelationShip(lord1, lord2):
    if lord1 in getFriendsPlanets(lord2):
        return RelationShip.Friend
    elif lord1 in getNeutralsPlanets(lord2):
        return RelationShip.Neutral
    else:
        return RelationShip.Enemy

def getRelationShips(lord1, lord2):
    relationship1 = getRelationShip(lord1, lord2)
    relationship2 = getRelationShip(lord2, lord1)
    return relationship1, relationship2
