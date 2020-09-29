import pickle

'''
Pickling with a file
'''
def picklingWithAFile():
    def storeData(): 
        # initializing data to be stored in db 
        Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
        'age' : 21, 'pay' : 40000} 
        Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 
        'age' : 50, 'pay' : 50000} 
    
        # database 
        db = {} 
        db['Omkar'] = Omkar 
        db['Jagdish'] = Jagdish 
        
        # Its important to use binary mode 
        dbfile = open('examplePickle', 'ab') 
        
        # source, destination 
        pickle.dump(db, dbfile)                      
        dbfile.close() 
  
    def loadData(): 
        # for reading also binary mode is important 
        dbfile = open('examplePickle', 'rb')      
        db = pickle.load(dbfile) 
        for keys in db: 
            print(keys, '=>', db[keys]) 
        dbfile.close()

    storeData()
    loadData() 

picklingWithAFile()

'''
Pickling without a file
'''
def picklingWithoutAFile():
    # initializing data to be stored in db 
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',  
    'age' : 21, 'pay' : 40000} 
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 
    'age' : 50, 'pay' : 50000} 
    
    # database 
    db = {} 
    db['Omkar'] = Omkar 
    db['Jagdish'] = Jagdish 

    # For storing 
    b = pickle.dumps(db)       # type(b) gives <class 'bytes'> 
    
    # For loading 
    myEntry = pickle.loads(b) 
    print(myEntry) 

picklingWithoutAFile()