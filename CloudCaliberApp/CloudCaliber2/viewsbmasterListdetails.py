
from django.shortcuts import render
import json
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


import textutils.settings

#import textutils.settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import threading as th
from CloudCaliber import views
from CloudCaliber import viewsapi 
from CloudCaliber import views8d
from CloudCaliber import viewscalibrations
from CloudCaliber import viewsduecalendar
from CloudCaliber import viewsdamaged
from CloudCaliber import viewsduelist
from CloudCaliber import viewsgaugeusagewise
from CloudCaliber import viewsissuereturn
from CloudCaliber import viewsmasterlist
from CloudCaliber import viewsmasterlistdetails
from CloudCaliber import viewsmsastudy
from CloudCaliber import viewsuserlist
from CloudCaliber import viewsvalidations
from CloudCaliber import viewscategorycreation

from CloudCaliber.models import Admin1Companyinfo, Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Admincategoryidcontinuousnolist, Adminassetcontinuousformatlist, Adminassetserialformatlist,  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist

# from CloudCaliber.serializers import   AdminuserlistSerializer, AdminassetcategorytypelistSerializer, Adminassetcategorytypelist1Serializer
 
from .forms import MasterListModelForm

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)




@csrf_exempt
def MasterDetailsListDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryDetailsListDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")

@csrf_exempt
def MasterHistoryListDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")

@csrf_exempt
def MasterListDetailsDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")



@csrf_exempt
def MasterListCalibrationDetailsDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


