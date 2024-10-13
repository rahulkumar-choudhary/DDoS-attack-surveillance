#!/Users/rahul/Documents/code/DDoS-attack-surveillance/ddos/bin/python3

import pickle
import pandas as pd

# load the model file
loaded_model = pickle.load(open('../model/done/ddos_model.pkl', 'rb'))

csvLocation='../test-data/networkRequest.csv'

def classmodel_prd(): 
    
    # realtime attack prediction data load (saved using tshark)
    saved_data = pd.read_csv(csvLocation)

    # remove null row from csv data
    all_col=saved_data.columns
    saved_data_new = saved_data[saved_data[all_col].notnull()]
    saved_data_no_null=saved_data_new.dropna()

    # remove the "." from IP
    def ip_to_int(ip):
        parts = ip.split('.')
        return int(''.join([part.zfill(3) for part in parts]))

    # Apply the custom function to the "ip_address" column
    saved_data_no_null['ip.src'] = saved_data_no_null['ip.src'].apply(ip_to_int)
    saved_data_no_null['ip.dst'] = saved_data_no_null['ip.dst'].apply(ip_to_int)

    # load data into the model and predict the outcome
    prediction = loaded_model.predict(saved_data_no_null)

    ddosAttack=0
    noDdosAttack=0

    for i in prediction:
        if i==1:
            ddosAttack+=1
        elif i==0:
            noDdosAttack+=1

    output=f" Predicted DDoS attack: {ddosAttack} Predicted normal call: {noDdosAttack}"

    return output