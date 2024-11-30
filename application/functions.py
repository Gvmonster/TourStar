import random

def getGeolocationData(lat, long): #recebe latitude e longitude do ActivityMQ
    listGeolocation = [lat, long]

    return listGeolocation


def registerUser(name):
    name = name
    score = 0 

    return [name, score]

def filter_Values_Column(data):
    list_tips = data['CRISTO REDENTOR'].tolist()

    return list_tips


def giveTips(data):
    list_indice = random.randint(0, 19)
    print(list_indice)
    
    return data[list_indice]

def inputUserGeoHash():
    geo_hash = input("Digite algo: ")

    return geo_hash



