import pandas as pb
import socket as sk
import functions


data_Wonders = pb.read_csv('wonders_of_world.csv', encoding='ISO-8859-1')
data_Tips = pb.read_csv('tips_wonders_of_world.csv', encoding='ISO-8859-1')

#server = sk.

game_Status = True
score = 0
livesPlayer = 3

while game_Status:
    

    data_User = functions.registerUser("Gabriel")
    data_GeolocalitionData = functions.getGeolocationData(-8.0476, -34.877)

    data_filter = functions.filter_Values_Column(data_Tips)

    tip = functions.giveTips(data_filter)
    print(f"\n Dica: {tip} \n")


    geo_hash = functions.inputUserGeoHash()
    answer_key_geohash = functions.convertToGeoHash(data_GeolocalitionData, 7)
    result_check = functions.checkResponseUser(answer_key_geohash, geo_hash)

    if(result_check):
        score = score + functions.score_control(result_check)
        print(f"\n------------ Pontuação atual: {score} -------------\n")
        print(f"\n------------ Número de vidas: {livesPlayer} -------------\n")
    else:
        livesPlayer = livesPlayer - functions.lives_control(result_check)
        print(f"\n------------ Número de vidas: {livesPlayer} -------------\n")

                              
    menu_op = input("\nDeseja continuar? [S] para sim ou [N] para não\n")
    if(menu_op == "N" or livesPlayer == 0):
        print('\n------------------------\nJogo encerrado!\n------------------------\n')
        game_Status = False



    








