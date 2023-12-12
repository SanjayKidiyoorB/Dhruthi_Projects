
from django.shortcuts import render
import os
import re
from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
import cloudcaliber_project.settings
import threading as th

from CloudCaliber.models import Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist

# from CloudCaliber.serializers import   AdminuserlistSerializer, AdminassetcategorytypelistSerializer, Adminassetcategorytypelist1Serializer


# @csrf_exempt
# def AdminuserlistApi(request,id=0):
#     if request.method=='GET':
#         Adminuserlists = Adminuserlist.objects.all()
#         AdminuserlistSerializerOBJ=AdminuserlistSerializer(Adminuserlists,many=True)
#         return JsonResponse(AdminuserlistSerializerOBJ.data,safe=False)
#     elif request.method=='POST':
#         AdminuserlistData = JSONParser().parse(request)
#         AdminuserlistSerializerOBJ=AdminuserlistSerializer(data=AdminuserlistData)
#         if AdminuserlistSerializerOBJ.is_valid():
#             AdminuserlistSerializerOBJ.save
#             return JsonResponse("User is Added Successfully!",safe=False)        
#         return JsonResponse("User to be Added Failed!",safe=False)        
#     elif request.method=='PUT':
#         AdminuserlistData = JSONParser().parse(request)
#         AdminuserlistOBJ=Adminuserlist.objects.get(lUserId=AdminuserlistData['lUserId'])
#         AdminuserlistSerializerOBJ=AdminuserlistSerializer(AdminuserlistOBJ,data=AdminuserlistData)
#         if AdminuserlistSerializerOBJ.is_valid():
#             AdminuserlistSerializerOBJ.save
#             return JsonResponse("User is Updated Successfully!",safe=False)        
#         return JsonResponse("User to be Updated Failed!",safe=False)        
#     elif request.method=='DELETE': 
#         AdminuserlistOBJ=Adminuserlist.objects.get(lUserId=id)
#         AdminuserlistOBJ.delete()
#         return JsonResponse("User to be Added Failed!",safe=False)


# @csrf_exempt
# def AdminassetcategorytypelistApi(request,id=0):
#     if request.GET.get('Classification_ID', None) is not None:
#         Classification_ID = request.GET.get('Classification_ID')
        
#         AdminassetcategorytypelistOBJ=Adminassetcategorytypelist.objects.get(lUserId=id)
#     if request.method=='GET':
#         Adminassetcategorytypelists = Adminassetcategorytypelist.objects.all()
#         AdminassetcategorytypelistSerializerOBJ=AdminassetcategorytypelistSerializer(Adminassetcategorytypelists,many=True)
#         return JsonResponse(AdminassetcategorytypelistSerializerOBJ.data,safe=False)
#     elif request.method=='POST':
#         AdminassetcategorytypelistData = JSONParser().parse(request)
#         AdminassetcategorytypelistSerializerOBJ=AdminassetcategorytypelistSerializer(data=AdminassetcategorytypelistData)
#         if AdminassetcategorytypelistSerializerOBJ.is_valid():
#             AdminassetcategorytypelistSerializerOBJ.save
#             return JsonResponse("User is Added Successfully!",safe=False)        
#         return JsonResponse("User to be Added Failed!",safe=False)        
#     elif request.method=='PUT':
#         AdminassetcategorytypelistData = JSONParser().parse(request)
#         AdminassetcategorytypelistOBJ=Adminassetcategorytypelist.objects.get(lUserId=AdminassetcategorytypelistData['lUserId'])
#         AdminassetcategorytypelistSerializerOBJ=AdminassetcategorytypelistSerializer(AdminassetcategorytypelistOBJ,data=AdminassetcategorytypelistData)
#         if AdminassetcategorytypelistSerializerOBJ.is_valid():
#             AdminassetcategorytypelistSerializerOBJ.save
#             return JsonResponse("User is Updated Successfully!",safe=False)        
#         return JsonResponse("User to be Updated Failed!",safe=False)        
#     elif request.method=='DELETE': 
#         AdminassetcategorytypelistOBJ=Adminassetcategorytypelist.objects.get(lUserId=id)
#         AdminassetcategorytypelistOBJ.delete()
#         return JsonResponse("User to be Added Failed!",safe=False)



# @csrf_exempt
# def Adminassetcategorytypelist1Api(request,id=0):
#     if request.method=='GET':
#         Adminassetcategorytypelist1s = Adminassetcategorytypelist1.objects.all()
#         Adminassetcategorytypelist1SerializerOBJ=Adminassetcategorytypelist1Serializer(Adminassetcategorytypelist1s,many=True)
#         return JsonResponse(Adminassetcategorytypelist1SerializerOBJ.data,safe=False)
#     elif request.method=='POST':
#         Adminassetcategorytypelist1Data = JSONParser().parse(request)
#         Adminassetcategorytypelist1SerializerOBJ=Adminassetcategorytypelist1Serializer(data=Adminassetcategorytypelist1Data)
#         if Adminassetcategorytypelist1SerializerOBJ.is_valid():
#             Adminassetcategorytypelist1SerializerOBJ.save
#             return JsonResponse("User is Added Successfully!",safe=False)        
#         return JsonResponse("User to be Added Failed!",safe=False)        
#     elif request.method=='PUT':
#         Adminassetcategorytypelist1Data = JSONParser().parse(request)
#         Adminassetcategorytypelist1OBJ=Adminassetcategorytypelist1.objects.get(lUserId=Adminassetcategorytypelist1Data['lUserId'])
#         Adminassetcategorytypelist1SerializerOBJ=Adminassetcategorytypelist1Serializer(Adminassetcategorytypelist1OBJ,data=Adminassetcategorytypelist1Data)
#         if Adminassetcategorytypelist1SerializerOBJ.is_valid():
#             Adminassetcategorytypelist1SerializerOBJ.save
#             return JsonResponse("User is Updated Successfully!",safe=False)        
#         return JsonResponse("User to be Updated Failed!",safe=False)        
#     elif request.method=='DELETE': 
#         Adminassetcategorytypelist1OBJ=Adminassetcategorytypelist1.objects.get(lUserId=id)
#         Adminassetcategorytypelist1OBJ.delete()
#         return JsonResponse("User to be Added Failed!",safe=False)