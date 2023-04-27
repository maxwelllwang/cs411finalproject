from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient('localhost', 27017)

 
   # Create the database for our example (we will use the same database throughout the tutorial
   collection = client['academicworld']["faculty"]
   find = {"test_set":"abc"}
   for doc in collection.find():
      print(doc)
   return client['academicworld']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   print(dbname)