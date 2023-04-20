import datetime

from pymongo import MongoClient
import json

hay = True


class DataBase:
    
    def __init__(self ):
        hay = True

    def regresadic():
        client = MongoClient("mongodb+srv://grandino:iloveanalsex2022@cluster0.ocvhun7.mongodb.net/?retryWrites=true&w=majority")

        # Database Name
        db = client["Dinosaurio"]

        # Collection Name
        col = db["users"]

        query = {
        "User": {
        "$regex": 'ni'
        }
        }

        x = col.find(query)

        json_resultados = []

        for data in x:
            myFecha = data["BirthDate"].strftime("%x")
            json_resultados.append({"User":data["User"],"Password":data["Password"],"BirthDate":myFecha})


        client.close()

        #myJson = {"MyData":"Locos","Data:":json_resultados}

        return json.dumps(json_resultados)
    
    def regresaUser(str_User):

        client = MongoClient("mongodb+srv://grandino:iloveanalsex2022@cluster0.ocvhun7.mongodb.net/?retryWrites=true&w=majority")

        # Database Name
        db = client["Dinosaurio"]

        # Collection Name
        col = db["users"]

        query = {
        "User": {
        "$regex": str_User
        }
        }

        x = col.find(query)

        json_resultados = []

        for data in x:
            myFecha = data["BirthDate"].strftime("%x")
            json_resultados.append({"User":data["User"],"Password":data["Password"],"BirthDate":myFecha})


        client.close()

        return json.dumps(json_resultados)