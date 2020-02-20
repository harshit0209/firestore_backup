import firebase_admin
from firebase_admin import credentials
from firebase_admin import credentials, firestore
certif=input("Enter Credentials Ceritificate path : ")
cred = credentials.Certificate(certif)
#    "atmp-a7338-firebase-adminsdk-4hze2-a71782e25a.json")
firebase_admin.initialize_app(cred)
store = firestore.client()
docu=input("Document Name: ")
f= open(docu+".txt","w+")
doc_ref = store.collection(docu)
try:
    docs = doc_ref.stream()        
    print("Getting Document")
    for doc in docs:
        
        x=u'{},'.format(doc.to_dict())
        z=doc.to_dict()                    
        
        f.write(str(z)+"\n")       
    print("Document Data Save to "+docu+".txt")    
    f.close()          
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
