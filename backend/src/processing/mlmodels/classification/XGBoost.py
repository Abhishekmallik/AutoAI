import pandas as pd # data processing
import numpy as np # working with arrays
from sklearn.model_selection import train_test_split # splitting the data
from xgboost import XGBClassifier   # model algorithm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from processing.api.models import Result,FileInfo
from celery.decorators import task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
@task
def process(model,target,file_name):

    df = pd.read_csv('./static/upload/processed_'+file_name)    
    X = df.drop([target], axis = 1).values
    y = pd.DataFrame({target: df[target]}).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    start = time.time()
    xgb = XGBClassifier()
    xgb.fit(X_train, y_train)
    time_taken = time.time()-start 
    y_pred = xgb.predict(X_test)

    accuracy = accuracy_score(y_test,y_pred)
    precision = precision_score(y_test, y_pred)
    recall =  recall_score(y_test, y_pred)
    f1score = f1_score(y_test, y_pred)

   

    metrics = {
        "accuracy":accuracy,
        "precision_score":precision,
        "recall_score":recall,
        "f1_score" : f1score,
        "time_taken":time_taken
    }
    fileinfo = FileInfo.objects.filter(id=file_name)[0]
    Result.objects.create(fileinfo=fileinfo,parameters={},metrics=metrics,model=model)

    new_event = {
        "type":"websocket.result",
        "text":"Group send"
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        file_name, 
          new_event
        )



    
    return "Success"




    
    return "Success"
