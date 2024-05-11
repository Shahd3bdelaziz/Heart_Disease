import pandas as pd
import pickle
import numpy as np
from flask import Flask , request,jsonify
import tensorflow as tf
app=Flask(__name__)

decision_tree = pickle.load(open("models/DT.pkl","rb"))
pca = pickle.load(open("models/pca.pkl","rb"))
neural_network = tf.keras.models.load_model("models/NN.h5")
scaler = pickle.load(open("models/scaler.pkl","rb"))
encoder= pickle.load(open("models/encoder.pkl","rb"))
best_features=np.array([1 ,0 ,1 ,1 ,0 ,1 ,1])

@app.route("/predict",methods=["POST"])
def prediction():
    json_=request.json
    query_df=pd.DataFrame(json_)
    x=scaler.transform(query_df)
    x=pca.transform(x)
    x=x[:,best_features]

    
    answers=[]
    for i in x:
        ans={}
        res=decision_tree.predict(x)
        res=encoder.inverse_transform(res)[0]
        ans["Decision treee"]=res
        res2=neural_network.predict(x)
        res2=np.round(res2).astype(int)
        res2=encoder.inverse_transform(res2)[0]
        ans["Neural Network"]=res2
        answers.append(ans)
    
    return jsonify(answers)

if __name__=="__main__":
    app.run()