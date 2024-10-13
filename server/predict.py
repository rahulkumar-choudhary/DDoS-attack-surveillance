#!/Users/rahul/Documents/code/DDoS-attack-surveillance/ddos/bin/python3

###############################################################################
## normal prediction without threshold classification model:

import prd_classmodel

# change te csv and model location in the file
output = prd_classmodel.classmodel_prd()

# print (output)

#############################################################################
## push the output of prediction realtime to firebase

import database as firebase_upload

firebase_upload.upload(output)
