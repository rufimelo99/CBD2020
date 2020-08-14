#https://www.w3schools.com/python/python_mongodb_find.asp
import pymongo
from datetime import datetime #ISODate "probelem"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cbd"]
mycol = mydb["rest"]


def createIndexes():
    #to create indexes (just need this once)
    mycol.create_index("localidade")
    mycol.create_index("gastronomia")
    mycol.create_index("nome")

def addRest(restaurant):
    inserted_restaurant = mycol.insert_one(restaurant)
    print("Done!")

def searchRest(nome):
    if nome :
        for result in mycol.find({"nome": nome}):
            print(result)

def updateName(oldname, name):
    #https://www.w3schools.com/python/python_mongodb_update.asp
    if oldname and name:
        myquery = { "nome": oldname }
        newvalues = { "$set": { "nome": name } }
        mycol.update_one(myquery, newvalues)
        print("Done!")

def countLocalidades():
    query = mycol.aggregate(
        [{"$group": {"_id": "$localidade", "n": {"$sum": 1}}}])
    print("Numero de localidades distintas: ")
    return len(list(query))

def countRestByLocalidade():
    query = mycol.aggregate(
        [{"$group": {"_id": "$localidade", "n": {"$sum": 1}}}])
    print("Numero de restaurantes por localidade: "+str(list(query)))
    
def countRestByLocalidadeByGastronomia():
    query = mycol.aggregate(
        [{"$group": {"_id": {"localidade":"$localidade","gastronomia": "$gastronomia"}, "number": {"$sum": 1}}}])
    for i in list(query):
        print(i)

def getRestWithNameCloserTo(search):
    query = mycol.find({"nome": {"$regex": search}})
    for i in list(query):
        print(i)


def main():
    searchRest("Glorious Food")
    addRest({
        "address" : {
            "building" : "284",
            "coord" : [
                -73.9829239,
                40.6580753
            ],
            "rua" : "Prospect Park West",
            "zipcode" : "11215"
        },
        "localidade" : "Brooklyn",
        "gastronomia" : "American",
        "grades" : [
            {
                "date" : datetime(2020, 1, 1, 0, 0),
                "grade" : "A",
                "score" : 11
            }
        ],
        "nome" : "The Movable Feast 2",
        "restaurant_id" : "101011010101"
    }
    )
    updateName("The Movable Feast 2", "The Movable Feast 3")
    countLocalidades()
    countRestByLocalidade()
    countRestByLocalidadeByGastronomia()
    getRestWithNameCloserTo("The Mo" )

if __name__ == "__main__":
    main()