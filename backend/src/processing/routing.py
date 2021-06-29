from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.security.websocket import AllowedHostsOriginValidator
from processing.consumers import DataSetConsumer,ResultConsumer,PlotConsumer


application = ProtocolTypeRouter({
  'websocket': AllowedHostsOriginValidator(
    URLRouter(
      [
        
        url(r"^dataset",DataSetConsumer),
        url(r"^result/", ResultConsumer),
        url(r"^plot/", PlotConsumer),

      
        
      ]
    )
  )
})