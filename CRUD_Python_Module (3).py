# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        #USER = 'aacuser' 
        #PASS = 'aacpassword' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method

    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result = self.database.animals.insert_one(data)  # data should be dictionary       
            return result.acknowledged  #true for successful creation 
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 
            

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None: 
            request = self.database.animals.find(query)
        else: 
            raise Exception("No data found") 
            
        return list(request)
    
    #Update an existing document 
    def update(self, query, updateValue):
        if query and updateValue:
            update = self.database.animals.update_many(query, {"$set": updateValue})
            self.records_updated = update.modified_count
            self.records_matched = update.matched_count
            
            return True if update.modified_count > 0 else False
        else:
            raise Exception("Invalid Input")
            
    
    
    #Delete an existing document
    def delete(self, query):
        if query is not None: 
            deletion = self.database.animals.delete_many(query)
            self.records_deleted = deletion.deleted_count
            
            return True if deletion.deleted_count > 0 else false
        
        else: 
            raise Exception("Invalid Input")