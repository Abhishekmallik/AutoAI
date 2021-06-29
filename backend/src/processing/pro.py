'''
import time 
from processing.api.models import Results
from processing.api.models import FileInfo,CsvData
from channels.db import database_sync_to_async
import pandas as pd
import json
import django_rq
from processing.tasks import addSome
from django_rq import job
import channels
from celery.decorators import task
import channels
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@database_sync_to_async
def time_(id):
    fileinfo = FileInfo.objects.filter(id=id)
    Results.objects.create(fileinfo=fileinfo[0],accuracy=95.77)

    return "Sucess"


  
async def process():
    print('Hi')
    new_event = {
        "type":"websocket.temp",
        "text":"Group send"
    }
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
        "aakash", 
          new_event
        )
    
    return "Success"


    queryset = CsvData.objects.filter(fileinfo_id=id)
    if len(queryset)!=0:
        return "Success"
    
    print('Check')
    fileinfo = FileInfo.objects.filter(id=id)[0]
    df = pd.read_csv('./static/upload/'+id)
    head = json.loads((df.head().to_json(orient="records")))
    describe = json.loads((df.describe().to_json(orient='split')))
    datatypes = list(df.dtypes.to_frame('dtypes').reset_index()['dtypes'].astype(str))
    df = pd.DataFrame({'total_missing': df.isnull().sum(), 'perc_missing': (df.isnull().sum()/df.shape[0])*100})
    missing = json.loads((df.to_json(orient='split')))
    csvdata = CsvData.objects.create(fileinfo=fileinfo,head=head,describe=describe,missing=missing,datatypes=datatypes)
    print("Working")
    return "Success"
    
    '''