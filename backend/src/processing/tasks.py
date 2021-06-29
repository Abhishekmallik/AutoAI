from processing.api.models import CsvData,FileInfo,Plot
from celery.decorators import task
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
import pandas as pd
import json
import time
from asgiref.sync import async_to_sync
import matplotlib.pyplot as plt
import seaborn as sns
import io
from django.core.files import File

@task
def process(file_name):
      
    fileinfo = FileInfo.objects.filter(id=file_name)[0]
    df = pd.read_csv('./static/upload/'+file_name)
    head = json.loads((df.head().to_json(orient="records")))
    describe = json.loads((df.describe().to_json(orient='split')))
    datatypes = list(df.dtypes.to_frame('dtypes').reset_index()['dtypes'].astype(str))
    df = pd.DataFrame({'total_missing': df.isnull().sum(), 'perc_missing': (df.isnull().sum()/df.shape[0])*100,'unique_count':list(df.apply(lambda col: len(col.unique())))})
    missing = json.loads((df.to_json(orient='split')))
    csvdata = CsvData.objects.create(fileinfo=fileinfo,head=head,describe=describe,missing=missing,datatypes=datatypes)
     
    new_event = {
        "type":"websocket.temp",
        "text":"Group send"
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        file_name, 
          new_event
        )
    
    return "Success"


@task
def plot(data):
      
    
    title = data['title']
    dataset = data['dataset']
    type_of_plot = data['type_of_plot']
    X = data['x_axis']
    x_axis_label = data['x_axis_label']
    Y = data['y_axis']
    y_axis_label = data['y_axis_label']
    id = data['id']

    path = './static/upload/'+id
    if dataset=='processed':
        path = './static/upload/processed_'+id

    df = pd.read_csv(path)
    
  

    h =''

    if type_of_plot =='scatter_plot':
        type_of_plot = 'Scatter Plot'
        sns.catplot(data = df, x = X, y = Y)
        
    if type_of_plot =='violin_plot':
        type_of_plot = 'Violin Plot'

        sns.catplot(data = df, x = X, y = Y, kind = 'violin', split=True)
        
    if type_of_plot =='bar_plot':
        type_of_plot = 'Bar Plot'

        sns.catplot(data = df, x = X, y = Y, kind = 'bar')

    if type_of_plot =='box_plot':
        type_of_plot = 'Box Plot'

        sns.boxplot(data = df, x = X, y = Y, hue = h)

    if type_of_plot =='sworm_plot':
        type_of_plot = 'Sworm Plot'

        sns.swarmplot(data = df, x = X, y = Y, hue = h) 

    buf = io.BytesIO()
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(title)
    plt.tight_layout()
    plt.autoscale(enable=True, axis='both', tight=None)
    
    plt.savefig(buf,format="png",dpi=300,bbox_inches='tight')
    image = File(buf, name='random.png') 
    

    fileinfo  = FileInfo.objects.filter(id=id)[0]
    Plot.objects.create(fileinfo=fileinfo,images=image,type_of=type_of_plot,title=title)

    new_event = {
        "type":"websocket.plot",
        "text":"Group send"
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        id, 
          new_event
        )
    
    return "Success"
