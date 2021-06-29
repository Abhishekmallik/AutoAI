from django.urls import path
from django.views.decorators.csrf import csrf_exempt    
from processing.api import views


urlpatterns = [
    path('datasethead',views.DatasetHead.as_view()),
    path('datasetdescribe',views.DatasetDescribe.as_view()),
    path('datasetmissing',views.DatasetMissing.as_view()),
    path('datasettypes',views.DatasetDatatypes.as_view()),
    path('image',views.Image.as_view()),
    path('getList',csrf_exempt(views.getList)),
    path('processedlist',views.ProcessedList.as_view()),
    path('result',csrf_exempt(views.result)),
    path('file',csrf_exempt(views.upload_file)),
  
    #path('file',views.FileInfo.as_view()),
    path('setfileid',views.fileid),
    path('temp',views.temp),

#########################

    path('dataset',views.DataSet.as_view()),
    path('upload_file',views.UploadFile.as_view()),
    path('get_file_list',views.UploadedFileList.as_view()),
    path('processedmetadata',views.ProcessedMetaInfo.as_view()),
    path('csvmetadata',views.GetCsvMetaInfo.as_view()),
    path('results',views.ResultInfo.as_view()),
    path('delete',views.DeleteFile.as_view()),
    path('plot',views.PlotView.as_view()),
]