from django.contrib import admin


from processing.api.models import CsvData,FileInfo,ProcessedMetaData,Result,Plot



admin.site.register(CsvData)
admin.site.register(FileInfo)
admin.site.register(ProcessedMetaData)
admin.site.register(Result)
admin.site.register(Plot)
# Register your models here.
