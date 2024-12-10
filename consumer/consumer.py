import stomp
import json

class Consumer_Data_Geo(stomp.ConnectionListener):

    def on_message(self, data):
        print('\n\nNovo dado recebido:\n\n', data.body)
        self.process_data(data.body)

    def process_data(self, data):
        data = json.loads(data)
        formatted_data = {
        "Indice": data['Indice'],
        "Name": data['Name'],
        "Type": data['Type'],
        "Latitude": data['Latitude'],
        "Longitude": data['Longitude'],
        "Location": data['Location'],
        "WikipediaLink": data['WikipediaLink'],
        "PictureLink": data['PictureLink'],
        "BuildInYear": data['BuildInYear'],
            }

        data_list.append(formatted_data)
        print(data_list)

data_list = []
connect_ActiveMQ = stomp.Connection([('localhost', 61613)])  
connect_ActiveMQ.set_listener('', Consumer_Data_Geo())
connect_ActiveMQ.connect(wait=True)
dado = connect_ActiveMQ.subscribe(destination='/queue/data_geolocated', id=1, ack='auto')
print(data_list)

while True:
    pass