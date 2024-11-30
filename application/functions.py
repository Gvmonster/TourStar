import random
import geohash2

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

def convertToGeoHash(data_GeolocalitionData, precision):
    geohash = geohash2.encode(data_GeolocalitionData[0], data_GeolocalitionData[1], precision)
    print(f"Geohash: {geohash}")

    return geohash



#def lifeControl(geo_hash):

def checkResponseUser(answer_key_geohash, geohash_user_response):
    if(answer_key_geohash == geohash_user_response):
        print('------------------------\nParabéns, você acertou!\n------------------------\nProxima rodada')
        return True
    else:
        print("Não foi dessa vez")
        return False

    
    


