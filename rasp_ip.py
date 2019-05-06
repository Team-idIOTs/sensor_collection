import os
import pyrebase

from creds import *

firebase = pyrebase.initialize_app(config)
db = firebase.database()

output = os.popen("hostname -I").read()

print(output)

data = {"output":output}

db.child("rasp" + str(pi_number)).child("ip").set(data)
