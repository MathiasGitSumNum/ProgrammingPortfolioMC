from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'somethingSmart1'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 31942
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s' % (USER,PASS,HOST,PORT,DB))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, createData):
        if createData is not None:
            self.collection.insert_one(createData)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data is empty")

# Create method to implement the R in CRUD.
    def read(self, readData = None):
        if readData is not None:
            result = self.collection.find(readData, {"_id": False})
        else:
            result = self.collection.find({}, {"_id":False})
        return result

# Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        if searchData is not None and updateData is not None:
                result = self.collection.update_many(searchData, {'$set':updateData})
        else:
            return "One or more arguments was null"
        return result.raw_result

# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
                result = self.collection.delete_many(deleteData)
        else:
            return "argument was null"