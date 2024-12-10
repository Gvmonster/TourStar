import random
import geohash2

def getGeolocationData(lat, long):
    listGeolocation = [lat, long]

    return listGeolocation


def registerUser(name):
    name = name

    return [name]

def filter_Values_Column(data):
    list_tips = data['CRISTO REDENTOR'].tolist()

    return list_tips


def giveTips(data):
    list_indice = random.randint(0, 19)
    print(list_indice)
    
    return data[list_indice]

def inputUserGeoHash():
    geo_hash = input("Digite o código geohash: ")

    return geo_hash

def convertToGeoHash(data_GeolocalitionData, precision):
    geohash = geohash2.encode(data_GeolocalitionData[0], data_GeolocalitionData[1], precision)

    return geohash



def score_control(resultCheck):
    if(resultCheck):
        return 5
    else:
        return 0
    
def lives_control(result_check):
    if(result_check == False):
        return 1

def checkResponseUser(answer_key_geohash, geohash_user_response):
    if(answer_key_geohash == geohash_user_response):
        print('------------------------\nParabéns, você achou o tesouro!\n------------------------\nPróxima rodada')
        return True
    else:
        print("O tesouro não está aqui!")
        return False

    
    


