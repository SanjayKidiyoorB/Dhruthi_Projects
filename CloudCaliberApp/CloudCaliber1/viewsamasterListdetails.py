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
from CloudCaliber.models import  Admincategoryidcontinuousnolist, Masterinstrumentpreventivemabigintenancelist, Masterinstrumentslistpart2, Adminassetcontinuousformatlist, Adminassetserialformatlist,  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
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
def MasterDetailsList(request,lID):

    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterDetailsListAdmin(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterDetailsListAllPlant(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryDetailsList(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryDetailsListAdmin(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryDetailsListAllPlant(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryList(request,lID):
    Thistorytransactions_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Validation").order_by('-dtcalibrationdate')             
    


    ThistorytransactionsIssue_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Issue History").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsCalibration_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Calibration").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsValidation_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Validation").order_by('-dtcalibrationdate')             
    
    Thistorytransactions8D_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "8D").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsService_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Service").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsPrepone_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Prepone").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsPostpone_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Postpone").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsRequest_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Request").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsUsage_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Usage").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsTransfer_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Transfer").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsDetailsEdited_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "Details Edited").order_by('-dtcalibrationdate')             
    
    ThistorytransactionsDC_List = Thistorytransactions.objects.filter(linstrumentid=lID, shistorytype = "DC").order_by('-dtcalibrationdate')             
    
    return render(request, "CloudCaliber/adminOperatorListDetails.html",
                    {
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List, 
                        'ThistorytransactionsIssue_List': ThistorytransactionsIssue_List,  
                    }
                    )


@csrf_exempt
def MasterHistoryListAdmin(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")





@csrf_exempt
def MasterHistoryListAllPlant(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")





@csrf_exempt
def MasterListDetails(request,lID):

    lIDa =0
    
    lIDa =lID

    if request.method == "POST":
        data = request.POST 

    else:
            
        MasterinstrumentslistOBJ =  Masterinstrumentslist.objects.values().get(lid=lIDa)
        Masterinstrumentslistpart2OBJ =  Masterinstrumentslistpart2.objects.values().get(linstrumentid=lIDa)
        Masterinstrumentsparepartslist2OBJ =  Masterinstrumentsparepartslist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentpurchasechecklist2OBJ =  Masterinstrumentpurchasechecklist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentpreventivemabigintenancelist2OBJ =  Masterinstrumentpreventivemabigintenancelist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentpartprojectslist2OBJ =  Masterinstrumentpartprojectslist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentenvironmentconditionlist2OBJ =  Masterinstrumentenvironmentconditionlist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentcalibrationsettingslist2OBJ =  Masterinstrumentcalibrationsettingslist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentcalibrationmasterslist2OBJ =  Masterinstrumentcalibrationmasterslist.objects.values().filter(linstrumentid=lIDa)
        Masterinstrumentattachmentslist2OBJ =  Masterinstrumentattachmentslist.objects.values().filter(linstrumentid=lIDa) 
        return render(request, "CloudCaliber/MasterListDetails.html",
                        {
                            'title':'User list', 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'MasterinstrumentslistOBJ': MasterinstrumentslistOBJ, 
                            'Masterinstrumentslistpart2OBJ': Masterinstrumentslistpart2OBJ, 
                            'Masterinstrumentsparepartslist2OBJ': Masterinstrumentsparepartslist2OBJ, 
                            'Masterinstrumentpurchasechecklist2OBJ': Masterinstrumentpurchasechecklist2OBJ, 
                            'Masterinstrumentpreventivemabigintenancelist2OBJ': Masterinstrumentpreventivemabigintenancelist2OBJ, 
                            'Masterinstrumentpartprojectslist2OBJ': Masterinstrumentpartprojectslist2OBJ, 
                            'Masterinstrumentenvironmentconditionlist2OBJ': Masterinstrumentenvironmentconditionlist2OBJ, 
                            'Masterinstrumentcalibrationsettingslist2OBJ': Masterinstrumentcalibrationsettingslist2OBJ, 
                            'Masterinstrumentcalibrationmasterslist2OBJ': Masterinstrumentcalibrationmasterslist2OBJ, 
                            'Masterinstrumentattachmentslist2OBJ': Masterinstrumentattachmentslist2OBJ,  
                            })





@csrf_exempt
def MasterListCalibrationDetails(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")







