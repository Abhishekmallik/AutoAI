from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,generics    
from rest_framework.decorators import action
import pandas as pd
import json
import io
import base64

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from django.core.files.images import ImageFile 
from django.http import JsonResponse
import time
import seaborn as sns
from rest_framework.decorators import api_view
from processing.api.serializers import FileInfoSerializer
from django.views.generic import ListView
import PIL.Image
from asgiref.sync import sync_to_async
from processing.api.models import FileInfo,CsvData,ProcessedMetaData,Result,Plot
from django.core.files.base import ContentFile
from processing.tasks import process,plot 
from itertools import groupby   
from asgiref.sync import async_to_sync
from django.core.files.uploadedfile import InMemoryUploadedFile
from operator import itemgetter 
import processing.mlmodels.classification.DecisionTree as DecisionTree
import processing.mlmodels.classification.GaussianNaiveBayes as GaussianNaiveBayes
import processing.mlmodels.classification.KNN as KNN
import processing.mlmodels.classification.LogisticRegression as LogisticRegression
import processing.mlmodels.classification.RandomForest as RandomForest
import processing.mlmodels.classification.XGBoost as XGBoost
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
import statistics as st
import processing.mlmodels.regression.ElasticNet as ElasticNet
import processing.mlmodels.regression.LassoRegression as LassoRegression
import processing.mlmodels.regression.LinearRegression as LinearRegression
import processing.mlmodels.regression.RidgeRegression as RidgeRegression
import processing.mlmodels.regression.SGDRegressor as SGDRegressor
from django.core.files import File


import os

def temp(request):

    t = Thread(target=wait,) 
    t.setDaemon(True)
    t.start()
    
    head = CsvData.objects.all()
    for obj in head:
        print(obj.head[0])

    return HttpResponse('Hi there')

def wait():

    time.sleep(5)
    print("ho")
    return HttpResponse('Yo')

'''
class FileInfo(generics.CreateAPIView,generics.ListAPIView):

    permission_classes = []
   

    def list(self, request):

        #queryset = self.queryset.filter(username=request.GET['user'])
        #serializer = FileInfoSerializer(queryset,many=True)
        #return Response(serializer.data)
        return Response({"success":"true"})

    def post(self, request):

        file = request.FILES['file']
        uploaded_file_name = file.name
        username = request.GET['user']
        
        
        f = FileInfo.objects.create(

                                username = username,
                                uploaded_file_name = uploaded_file_name,
                                processed_file_name = ''

                                )
        with open('./static/upload/'+str(f.id), 'wb+') as destination:  
                for chunk in file.chunks():  
                    destination.write(chunk)  

        return Response({"success":"true"})
'''


class DatasetHead(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
       
        df = pd.read_csv('./static/upload/uploaded_file.csv',nrows=5)
        return Response(json.loads((df.to_json(orient="records"))))


class DatasetDescribe(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        df = pd.read_csv('./static/upload/uploaded_file.csv')
        df = df.describe()

        return Response(json.loads((df.to_json(orient='split'))))


class DatasetMissing(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        df = pd.read_csv('./static/upload/uploaded_file.csv')
        df = pd.DataFrame({'total_missing': df.isnull().sum(), 'perc_missing': (df.isnull().sum()/df.shape[0])*100})
        return Response(json.loads((df.to_json(orient='split'))))
    
class DatasetDatatypes(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format=None):
        
        df = pd.read_csv('./static/upload/uploaded_file.csv')
        new_df = pd.DataFrame()
        new_df['total_missing'] = df.isnull().sum()
        print(new_df)
        df = df.dtypes.to_frame('dtypes').reset_index()
        df['dtypes'] = df['dtypes'].astype('|S')
        df['total_missing']= list(new_df['total_missing'])
        print(df)
        return Response(json.loads((df.to_json(orient='records'))))   




class ProcessedList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        df = pd.read_csv('./static/upload/processed_file.csv')
        return Response(df.columns.values)


class Image(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        image_data =open('../media/static/upload/image.png','rb').read()    
            
        response = HttpResponse(content_type = 'image/png')
        return response  


def getList(request):

    if request.method== "POST":
        dic = json.loads(request.body)
        print(dic)
        processColumns(dic)
    return HttpResponse('Hi There')



def run_model(target,model,file_name):

    
        #




    if model =="decision_tree":
        DecisionTree.process.delay("Decision Tree",target,file_name)

    if model =="gaussian_naive_bayes":
        GaussianNaiveBayes.process.delay("Gaussian Naive Bayes",target,file_name)
        
    if model =="knn":
        KNN.process.delay("KNN",target,file_name)

    if model =="logistic_regression":
        LogisticRegression.process.delay("Logistic Regression",target,file_name)

    if model =="random_forest":
        RandomForest.process.delay("Random Forest",target,file_name)

    if model =="xgboost":
        XGBoost.process.delay("Xgboost",target,file_name)

    if model =="elsatic_net":
        ElasticNet.process.delay("ElasticNet",target,file_name)

    if model =="lasso_regression":
        LassoRegression.process.delay("Lasso Regression",target,file_name)

    if model =="linear_regression":
        LinearRegression.process.delay("Linear Regression",target,file_name)

    if model =="ridge_regression":
        RidgeRegression.process.delay("Ridge Regression",target,file_name)

    if model =="sgd_regressor":
        SGDRegressor.process.delay("SGD Regressor",target,file_name)



def result(request):

    if request.method== "POST":
        
        dic = json.loads(request.body)
        print(dic)
        target = dic['target']
        model = dic['model']
        file_name = dic['file_name']
     

        run_model(target,model,file_name)

        
       
    return HttpResponse('Hi There')

def processColumns(dic):

    columns = dic['selected']
    actions = dic['action']
    encoder = dic['encoder']
    normalizer = dic['normalizer']
    file_name = dic['id']
    df = pd.read_csv('./static/upload/'+file_name)
    df = df[columns]
    
    #Missing Values
    for i in range(0, len(columns)):
        c = columns[i]
    
        if c in actions:
            a = actions[c]

            if a == 'mean':
                df[c].fillna(df[c].mean(), inplace=True)
            if a == 'median':
                df[c].fillna(df[c].median(), inplace=True)
            if a == 'mode':
                df[c].fillna(df[c].median(), inplace=True)
            if a == 'delete_column':
                df.drop([c], axis=1, inplace=True)
            if a == 'delete_missing':
                df[c].dropna(how='any', axis=0, inplace=True)
            if a == 'rep_min_freq':
                l = list(dict(df[c].value_counts()))
                df[c].fillna(l[len(l) - 1])
            if a == 'rep_max_freq':
                l = list(dict(df[c].value_counts()))
                df[c].fillna(l[0])

    #Encoding
    
    for col in encoder:
        print('Column',col)
        if encoder[col] == "one_hot":
            enc = OneHotEncoder()
            enc_df = pd.DataFrame(enc.fit_transform(df[[col]]).toarray())
            columns = enc_df.columns
            l = []
            for i in columns:
                l.append(str(col)+str(i))
            enc_df.columns = l
            df = df.join(enc_df)
            df.drop([col], axis = 1, inplace = True)
        
        elif encoder[col] == "label":
            enc = LabelEncoder()
            df[col]= enc.fit_transform(df[col]) 
        
        elif encoder[col] == "ordinal":
            enc = OrdinalEncoder()
            df[[col]]= enc.fit_transform(df[[col]]) 
            


    #Normalization    
    for col in normalizer:
        l = list(df[col])
        m = 0
        if normalizer[col] == "max":
            m = max(l)
        elif normalizer[col] == "min":
            m = min(l)
        elif normalizer[col] == "median":
            m = st.median(l)
        elif normalizer[col] == "mean":
            m = st.mean(l)
        elif normalizer[col] == "mode":
            m = st.mode(l)
        if m == 0:
            continue
        column = []
        for i in l:
            column.append(i/m)
        df[col] = column




    df.to_csv('./static/upload/processed_'+file_name,index=False)

'''
dic = {
    'selected':["Pclass","Survived" ],
    'action': {}
}

processColumns(dic)

LogisticRegression.process("model","Survived","file_name")

'''
def upload_file(request):


    if request.method =="GET":

        FileList = FileInfo.objects.filter(username=request.GET['user'])
        se = FileInfoSerializer()
        se.serialize(FileList)
        
        print(se.getValue())

    return HttpResponse({"Hi":"There"})

    if request.method =="POST":
        pass
        





def fileid(request):

    request.session.save()
    file_id = request.GET['id']
    request.session['file_id']=file_id
    print(request.session['file_id'])
    request.session.save()

    return HttpResponse('Hi')



class DataSet(APIView):

    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):

        id = request.GET["id"]

        query_result = CsvData.objects.filter(fileinfo_id=id)
        response = dict()

        if len(query_result) != 0 :
            data = query_result[0]
            response['head'] = data.head
            response['describe'] = data.describe
            response['missing'] = data.missing

        return Response(response)

    

class UploadFile(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request,format=None):
        
        file = request.FILES['file']
        uploaded_file_name = file.name
        username = request.GET['user']
        print(type(file))

        f = FileInfo.objects.create(
                                username = username,
                                uploaded_file_name = uploaded_file_name,
                                processed_file_name = '',
                                file_size=file.size)
        
        with open('./static/upload/'+str(f.id), 'wb+') as destination:  
                for chunk in file.chunks():  
                    destination.write(chunk)  

    

        process.delay(str(f.id))
        return HttpResponse({"success":"true"})


class UploadedFileList(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):

        username = request.GET["username"]
        queryset = FileInfo.objects.filter(username=username)

        file_list = []

        for file in queryset:
            file_list.append({
                "id":file.id ,
                "uploaded_file_name":file.uploaded_file_name,
                "uploaded_on":file.uploaded_on,
                "size":file.file_size
                })

        return Response(file_list)


class ProcessedMetaInfo(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        id = request.GET['id']
        queryset = ProcessedMetaData.objects.filter(fileinfo_id=id)
        response = dict()
        if len(queryset)!=0:
            data = queryset[0]
            response["columns"] = data.columns
            response["actions"] = data.actions
            response["encoder"] = data.encoder
            response["normalizer"] = data.normalizer
            
        return Response(response)

    def post(self,request,format=None):

        body = json.loads(request.body)
        #print(body)
        id = body['id']
        columns = body['selected']
        actions = body["action"]
        encoder = body['encoder']
        normalizer = body['normalizer']

        queryset = ProcessedMetaData.objects.filter(
                                        fileinfo_id = id)

     
        if len(queryset)==0:
            ProcessedMetaData.objects.create(fileinfo_id = id,columns = columns,actions = actions,encoder=encoder,normalizer=normalizer)
        else :
            ProcessedMetaData.objects.filter(fileinfo_id=id).update(fileinfo_id = id,columns = columns,actions = actions,encoder=encoder,normalizer=normalizer)
        processColumns(body)
        return Response({"message":"success"})


class GetCsvMetaInfo(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        id = request.GET['id']
        queryset = CsvData.objects.filter(fileinfo_id=id)   
        print('Q',queryset)
        response = list()
        if len(queryset)!=0:
            data = queryset[0]
            missing = data.missing
            datatypes = data.datatypes

            for data,index,dtypes in zip(missing['data'],missing['index'],datatypes) :
                response.append({
                    "index":index,
                    "dtypes":dtypes,
                    "total_missing":data[0],
                    "unique_count" :data[2]
                })
                
        return Response(response)


class ResultInfo(APIView):

    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):

        id = request.GET['id']
        filter = request.GET['filter']

        query_result = []

        if filter == "all":
            query_result =  Result.objects.filter(fileinfo__username=id)
        else :
            query_result = Result.objects.filter(fileinfo_id=id)


        print(query_result)
        response = list()

        for result in query_result:

            response.append({
                "created_at":result.created_at,
                "model":result.model,
                "metrics":result.metrics,
                "parameters":result.parameters

            })
        return Response(response)


class DeleteFile(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    def delete(self,request):
        
        id = json.loads(request.body)['id']
        path_to_upload_file = './static/upload/'+id
        if os.path.exists(path_to_upload_file):
            os.remove(path_to_upload_file)
        path_to_processed_file = './static/upload/processed_'+id
        if os.path.exists(path_to_processed_file):
            os.remove(path_to_processed_file)
        return Response('Hi')




class PlotView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        id = request.GET['id']

        query_result = Plot.objects.filter(fileinfo_id=id)
        img_list = []
        for res in query_result:
            img_list.append({
                'image_url':res.images.name,
                'title':res.title,
                'created_at':res.created_at,
                'type_of':res.type_of

            })
  

        response = {}
        for key, value in groupby(img_list, 
                          key = itemgetter('type_of')): 
            res = []
            for k in value: 
                res.append(k)
            
            response[key]= res

        return Response(response)





    def post(self,request,format=None):

        data = json.loads(request.body)
        print(data)
        plot.delay(data)
        return  Response('Success')

