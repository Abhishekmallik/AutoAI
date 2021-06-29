import asyncio
import json
from channels.consumer import AsyncConsumer
import processing.pro as f
import random
import celery
import time
from processing.api.models import CsvData
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from processing import tasks as tasks
from urllib.parse import parse_qs
class ResultConsumer(AsyncConsumer):
  
  async def websocket_connect(self, event):

    
    query_string  = parse_qs(self.scope['query_string'].decode('utf8'))
    id = query_string['id'][0]

    await self.channel_layer.group_add(
      id,
      self.channel_name
    ) 

    await self.send({
        "type":"websocket.accept",
    })
 
  
    

  async def websocket_receive(self, event):
  
    await self.send({
        "type":"websocket.send",
        "text":"Success"
    })

  async def websocket_result(self,event):

    await self.send({
      "type":"websocket.send",
      "text":"Result success"
    })    
  

  async def websocket_disconnect(self, event):
    print('disconnected', event)
  




class DataSetConsumer(AsyncConsumer):
  async def websocket_connect(self, event):

    query_string  = parse_qs(self.scope['query_string'].decode('utf8'))
    id = query_string['id'][0]

    await self.channel_layer.group_add(
      id,
      self.channel_name
    ) 


    await self.send({
        "type":"websocket.accept",
    })
 
  
    

  async def websocket_receive(self, event):
  
    await self.send({
        "type":"socket.send",
        "text":"Success"
    })



  async def websocket_temp(self,event):
    print('I am called')
    await self.send(({
      "type":"websocket.send",
      "text":"Success"
    }))
      
  def websocket_disconnect(self, event):
    print('disconnected', event)
    
  

class PlotConsumer(AsyncConsumer):
  async def websocket_connect(self, event):

    query_string  = parse_qs(self.scope['query_string'].decode('utf8'))
    id = query_string['id'][0]

    await self.channel_layer.group_add(
      id,
      self.channel_name
    ) 


    await self.send({
        "type":"websocket.accept",
    })
 
  
    

  async def websocket_receive(self, event):
  
    await self.send({
        "type":"socket.send",
        "text":"Success"
    })



  async def websocket_plot(self,event):
    print('I am called')
    await self.send(({
      "type":"websocket.send",
      "text":"Success"
    }))
      
  def websocket_disconnect(self, event):
    print('disconnected', event)
    
  
