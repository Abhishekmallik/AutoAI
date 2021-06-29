import pandas as pd # data processing
import numpy as np # working with arrays
from sklearn.model_selection import train_test_split # splitting the data
from sklearn.linear_model import Ridge # model algorithm
from sklearn.metrics import mean_squared_error, r2_score
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
    ridge = Ridge()
    ridge.fit(X_train, y_train)
    time_taken = time.time()-start
    y_pred = ridge.predict(X_test)
    
    slope = ridge.coef_.tolist()  
    intercept = ridge.intercept_.tolist()
    rmse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    

    metrics = {
        "slope":slope,
        "intercept":intercept,
        "r2_score":r2,
        "mean_squared_error" : rmse,
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
