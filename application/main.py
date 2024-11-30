import pandas as pb
import socket as sk
import functions

data_Wonders = pb.read_csv('wonders_of_world.csv', encoding='ISO-8859-1')
data_Tips = pb.read_csv('tips_wonders_of_world.csv', encoding='ISO-8859-1')

#server = sk.

game_Status = True



while game_Status:

    data_User = functions.registerUser("Gabriel")
    data_GeolocalitionData = functions.getGeolocationData("-21.04805556", "-43.21055556")

    data_filter = functions.filter_Values_Column(data_Tips)

    tip = functions.giveTips(data_filter)
    print(f"Dica: {tip}")


    geo_hash = functions.inputUserGeoHash()


    menu_op = input("Deseja continuar? [S] para sim ou [N] para não")
    if(menu_op == "N"):
        game_Status = False
    








