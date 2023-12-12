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

from CloudCaliber.models import Admin1Companyinfo, Thistorytransactionmsa, Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentslistpart2, Masterinstrumentsparepartslist, Masterinstrumentslist 
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
def MasterHistoryList(request,lID):


      
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

        
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
 
    lCategoryID = request.session['lCategoryID']                       
    lLoginUserId = request.session['lLoginUserId']  
    semployeename = request.session['semployeename'] 
    semployeeno = request.session['semployeeno']  
    lunitid = request.session['lunitid']  
    sunitno = request.session['sunitno']  
    lcompanyid = request.session['lcompanyid']  
    scompantname = request.session['scompantname']  
    semailaddress = request.session['semailaddress']  
    smobile = request.session['smobile']  

    if request.session:
        request.session.clear()
 
    request.session['bSAPCodeDone']  = 0
    request.session['bSAPCodeNotDone']  = 0
    request.session['ID_Categories']  = 0
    request.session['ClassificationData']  = 0
    request.session['Flow1Data']  = 0
    request.session['Flow2Data']  = 0
    request.session['Flow3Data']  = 0
    request.session['Flow4Data']  = 0
    request.session['Flow5Data']  = 0
    request.session['GaugeClass']  = 0
    request.session['Location']  = 0 
    request.session['txtSearch']  = "" 

    CurDateFrom = datetime.today().strftime('%d-%m-%Y')
    request.session['CurDateFrom']  = CurDateFrom
    request.session['CurDateTo']  = CurDateFrom
    
    request.session['lCategoryID'] = lCategoryID                        
    request.session['lLoginUserId'] = lLoginUserId
    request.session['semployeename'] = semployeename
    request.session['semployeeno'] = semployeeno
    request.session['lunitid'] = lunitid
    request.session['sunitno']  = sunitno
    request.session['lcompanyid']  = lcompanyid
    request.session['scompantname']  = scompantname
    request.session['semailaddress'] = semailaddress
    request.session['smobile']  = smobile
    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
        sPlantName = AdminunitlistActive.splantname

    request.session['sPlantCode']   =sPlantCode


    lIDa =0
    lIDa = lID 

    lIDB =0
    lIDB =362
    lCount =0

    Thistorytransactions_List = Thistorytransactions.objects.filter(linstrumentid=lIDa, shistorytype = "Validation").order_by('-dtcalibrationdate')             
    

    Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('sinstrumentid', 'sdescription').get(lid=lIDa)


    #Masterinstrumentslistpart2_list =  Masterinstrumentslistpart2.objects.filter(linstrumentid=lIDa)

    #ThistorytransactionsCalibration_ListTemp =  Thistorytransactions.objects.filter(linstrumentid=lIDB)

    sSearch = "Inprocess"
    ThistorytransactionsInprocess_List = Thistorytransactions.objects.values_list('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate') 
       
    sSearch = "Request"
    ThistorytransactionsRequest_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Calibration"
    ThistorytransactionsCalibration_List = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate') 
    
    sSearch = "Issue History"
    sSearch1 = ""
    sSearch1 = "ISSUED"
    sSearch2 = ""
    sSearch2 = "RETURNED"
    ThistorytransactionsIssue_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch) | Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch1) | Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch2).order_by('-dtcalibrationdate')               
     
    sSearch = "Validation"
    ThistorytransactionsValidation_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Damaged"
    sSearch1 = ""
    sSearch1 = "UNDER SERVICE"
    ThistorytransactionsDamaged_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch) | Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch1).order_by('-dtcalibrationdate')               
     
    sSearch = "Service"
    ThistorytransactionsService_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Prepone"
    ThistorytransactionsPrepone_ListD = Thistorytransactions.objects.values().filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Postpone"
    ThistorytransactionsPostpone_ListD = Thistorytransactions.objects.values().filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Usage"
    ThistorytransactionsUsage_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Transfer"
    ThistorytransactionsTransfer_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "Masterlist Details edited"
    ThistorytransactionsEditied_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "DC"
    ThistorytransactionsDC_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "8D"
    Thistorytransactions8D_ListD = Thistorytransactions.objects.values('lid', 'lhistorymainid', 'shistorytype', 'scalibrationvendor', 'senteredby', 'scurrentstatus', 'dtcalibrationdate', 'sto', 'sfrom', 'dthistorydate', 'sreturneddate', 'scalibrationvendor').filter(linstrumentid=lIDa, shistorytype=sSearch).order_by('-dtcalibrationdate')               
     
    sSearch = "8D"
    Thistorytransactionmsa_ListD = Thistorytransactionmsa.objects.values('lhistorytranid', 'historymainid', 'historytype', 'calibrationvendor', 'enteredby', 'currentstatus', 'calibrationdate').filter(instrumentid=lIDa).order_by('-calibrationdate')               
     
 
    return render(request, "CloudCaliber/MasterHistoryList.html",
                    {
                        'title':'User list', 
                        'message':'Your User list page.',
                        'sPlantName': sPlantName,
                        'semployeename': semployeename, 
                        'year':datetime.now().year,  
                        'ThistorytransactionsCalibration_List': ThistorytransactionsCalibration_List, 
                        'ThistorytransactionsIssue_ListVal': ThistorytransactionsIssue_ListD, 
                        'ThistorytransactionsInprocess_List': ThistorytransactionsInprocess_List, 
                        'Masterinstrumentslist_list': Masterinstrumentslist_list,    
                        'ThistorytransactionsRequest_ListD': ThistorytransactionsRequest_ListD,
                        'Thistorytransactionmsa_ListD': Thistorytransactionmsa_ListD,
                        'ThistorytransactionsValidation_ListD': ThistorytransactionsValidation_ListD,
                        'ThistorytransactionsDamaged_ListD': ThistorytransactionsDamaged_ListD,
                        'ThistorytransactionsService_ListD': ThistorytransactionsService_ListD,
                        'ThistorytransactionsUsage_ListD': ThistorytransactionsUsage_ListD,
                        'Thistorytransactions8D_ListD': Thistorytransactions8D_ListD,
                        'ThistorytransactionsEditied_ListD': ThistorytransactionsEditied_ListD,
                        'ThistorytransactionsTransfer_ListD': ThistorytransactionsTransfer_ListD,
                        'ThistorytransactionsPrepone_ListD': ThistorytransactionsPrepone_ListD,
                        'ThistorytransactionsPostpone_ListD': ThistorytransactionsPostpone_ListD,
                        'ThistorytransactionsDC_ListD': ThistorytransactionsDC_ListD,
                        
                    }
                    )


@csrf_exempt
def MasterHistoryListAdmin(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")





@csrf_exempt
def MasterHistoryListAllPlant(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")


@csrf_exempt
def MasterHistoryListDisabled(request,lID):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")




