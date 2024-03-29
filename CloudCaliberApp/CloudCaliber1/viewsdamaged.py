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

import textutils.settings

import threading as th 
from CloudCaliber import views
from CloudCaliber import viewsapi
from CloudCaliber import viewsidcreate
from CloudCaliber import views8d
from CloudCaliber import viewscalibrations
from CloudCaliber import viewsduecalendar 
from CloudCaliber import viewsduelist
from CloudCaliber import viewsgaugeusagewise
from CloudCaliber import viewsissuereturn
from CloudCaliber import viewsmasterlist
from CloudCaliber import viewsmasterlistdetails
from CloudCaliber import viewsmsastudy
from CloudCaliber import viewsuserlist
from CloudCaliber import viewsvalidations
from CloudCaliber import viewscategorycreation

from CloudCaliber.models import Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist
from CloudCaliber.models import Tservicehistory, Thistorymain, Thistorymainpart1, Thistorymainpart2, Masterinstrumentslist , Masterinstrumentslistpart2,   Masterinstrumentpreventivemabigintenancelist 



 
@csrf_exempt 
def GaugeRepairDetails(request, lID):
    
    sCodeFinal1 = ""



    lPlantIdSelect = 0
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

    request.session['badmin'] =0
    request.session['badmin1'] = 0
    request.session['bstores'] = 0
    request.session['bcalibration'] = 0
    request.session['bservice'] = 0
    request.session['bmsa'] = 0
    request.session['bmasterlistonlyallplant'] = 1  
    request.session['breadonly'] =0
    sPlantCode = ""
    sCategoryCode = ""
    lcontinuousnob  = ""
    bFlow = 0
    sFlowName  = ""
    lcontinuousnoa  =0
    bFlow1 = 0
    sFlowName1  = ""
    lcontinuousnoa1  = 0
    bFlow2 = 0
    sFlowName2  = ""
    lcontinuousnoa2  =0
    bFlow3 = 0
    sFlowName3  = ""
    lcontinuousnoa3  =0
    bFlow4 = 0
    sFlowName4  = ""
    lcontinuousnoa4  =0
    bFlow5 = 0
    sFlowName5  = ""
    lcontinuousnoa5  =0
    bFlow6 = 0
    sFlowName6  = ""
    lcontinuousnoa6  =0
    bFlow7 = 0
    sFlowName7  = ""
    lcontinuousnoa7  =0
    bFlow8 = 0
    sFlowName8  = ""
    lcontinuousnoa8  =0
    bFlow9 = 0
    sFlowName9  = ""
    lcontinuousnoa9  =0
    bFlow10 = 0
    sFlowName10  = ""
    lcontinuousnoa10  =0
    
    bSAPCodeDone = 0
    bSAPCodeNotDone = 0

    cmbClassificationID = 0
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    
    getFlow1Code = ""
    request.session['getFlow1Code']  =getFlow1Code
    getFlow2Code = ""
    request.session['getFlow2Code']  =getFlow2Code
    getFlow3Code = ""
    request.session['getFlow3Code']  =getFlow3Code
    getFlow4Code = ""
    request.session['getFlow4Code']  =getFlow4Code
    getFlow5Code = ""
    request.session['getFlow5Code']  =getFlow5Code
    getFlowContCode = ""
    request.session['getFlowContCode']  =getFlowContCode


    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
 
    request.session['sPlantCode']   =sPlantCode

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode



    sReturnDate3 = ""
    sReturnDate2 = ""
    sReturnDate1 = ""
    sReturnDate = "" 
    dtReturnDate = datetime.now()
    sReturnDate1 = str(datetime.now()) 
    sReturnDate = sReturnDate1[0:10]

    if request.method == "POST":


        data = request.POST

    else:


        AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
        if AdminunitlistActive:
            sPlantCode = AdminunitlistActive.splantno
            sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
            sPlantNameNameA = AdminunitlistActive.splantname

        request.session['sPlantCode']   =sPlantCode
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else: 
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

        Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)

        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')


        return render(request, "CloudCaliber/GaugeRepairDetails.html", 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
            
            'CurDateNow':datetime.now(),
            'lPlantId':lPlantId,  
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName , 
            'Location': 0 , 
            'semployeename':  semployeename,
            'txtSearch': "" , 
            'sCodeFinal1': "" ,  
            'sCodeFinal2': "" ,  
            'cmbClassificationID': 0 , 
            'cmbCategoryID': 0 ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': "",  
            'cmbFlow2label': "",  
            'cmbFlow3label': "",  
            'cmbFlow4label': "",
            'cmbFlow5label': "",  
            'bNewID': 0 ,  
            'Adminassettypelist_list':Adminassettypelist_list,
            'bSAPCodeDone': bSAPCodeDone, 
            'bSAPCodeNotDone': bSAPCodeNotDone, 
            'sReturnDate': sReturnDate,
        }) 


@csrf_exempt 
def GaugeRepairHistoryDetails(request, lID):
    
    sCodeFinal1 = ""



    lPlantIdSelect = 0
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

    request.session['badmin'] =0
    request.session['badmin1'] = 0
    request.session['bstores'] = 0
    request.session['bcalibration'] = 0
    request.session['bservice'] = 0
    request.session['bmsa'] = 0
    request.session['bmasterlistonlyallplant'] = 1  
    request.session['breadonly'] =0
    sPlantCode = ""
    sCategoryCode = ""
    lcontinuousnob  = ""
    bFlow = 0
    sFlowName  = ""
    lcontinuousnoa  =0
    bFlow1 = 0
    sFlowName1  = ""
    lcontinuousnoa1  = 0
    bFlow2 = 0
    sFlowName2  = ""
    lcontinuousnoa2  =0
    bFlow3 = 0
    sFlowName3  = ""
    lcontinuousnoa3  =0
    bFlow4 = 0
    sFlowName4  = ""
    lcontinuousnoa4  =0
    bFlow5 = 0
    sFlowName5  = ""
    lcontinuousnoa5  =0
    bFlow6 = 0
    sFlowName6  = ""
    lcontinuousnoa6  =0
    bFlow7 = 0
    sFlowName7  = ""
    lcontinuousnoa7  =0
    bFlow8 = 0
    sFlowName8  = ""
    lcontinuousnoa8  =0
    bFlow9 = 0
    sFlowName9  = ""
    lcontinuousnoa9  =0
    bFlow10 = 0
    sFlowName10  = ""
    lcontinuousnoa10  =0
    
    bSAPCodeDone = 0
    bSAPCodeNotDone = 0

    cmbClassificationID = 0
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    
    getFlow1Code = ""
    request.session['getFlow1Code']  =getFlow1Code
    getFlow2Code = ""
    request.session['getFlow2Code']  =getFlow2Code
    getFlow3Code = ""
    request.session['getFlow3Code']  =getFlow3Code
    getFlow4Code = ""
    request.session['getFlow4Code']  =getFlow4Code
    getFlow5Code = ""
    request.session['getFlow5Code']  =getFlow5Code
    getFlowContCode = ""
    request.session['getFlowContCode']  =getFlowContCode


    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
 
    request.session['sPlantCode']   =sPlantCode

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode



    sReturnDate3 = ""
    sReturnDate2 = ""
    sReturnDate1 = ""
    sReturnDate = "" 
    dtReturnDate = datetime.now()
    sReturnDate1 = str(datetime.now()) 
    sReturnDate = sReturnDate1[0:10]

    if request.method == "POST":


        data = request.POST

    else:


        AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
        if AdminunitlistActive:
            sPlantCode = AdminunitlistActive.splantno
            sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
            sPlantNameNameA = AdminunitlistActive.splantname

        request.session['sPlantCode']   =sPlantCode
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else: 
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

        Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)

        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')


        return render(request, "CloudCaliber/GaugeRepairDetails.html", 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
            
            'CurDateNow':datetime.now(),
            'lPlantId':lPlantId,  
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName , 
            'Location': 0 , 
            'semployeename':  semployeename,
            'txtSearch': "" , 
            'sCodeFinal1': "" ,  
            'sCodeFinal2': "" ,  
            'cmbClassificationID': 0 , 
            'cmbCategoryID': 0 ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': "",  
            'cmbFlow2label': "",  
            'cmbFlow3label': "",  
            'cmbFlow4label': "",
            'cmbFlow5label': "",  
            'bNewID': 0 ,  
            'Adminassettypelist_list':Adminassettypelist_list,
            'bSAPCodeDone': bSAPCodeDone, 
            'bSAPCodeNotDone': bSAPCodeNotDone, 
            'sReturnDate': sReturnDate,
        }) 




@csrf_exempt
def GaugeServiceRepair(request, lID):
    
    sCodeFinal1 = ""
    sCodeFinal2 = ""
 
    historyserviceid = 0
    

    lPlantIdSelect = 0
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

    #semployeename = semployeeno + " | " + semployeename
    request.session['badmin'] =0
    request.session['badmin1'] = 0
    request.session['bstores'] = 0
    request.session['bcalibration'] = 0
    request.session['bservice'] = 0
    request.session['bmsa'] = 0
    request.session['bmasterlistonlyallplant'] = 1  
    request.session['breadonly'] =0
    sPlantCode = ""
    sCategoryCode = ""
    lcontinuousnob  = ""
    bFlow = 0
    sFlowName  = ""
    lcontinuousnoa  =0
    bFlow1 = 0
    sFlowName1  = ""
    lcontinuousnoa1  = 0
    bFlow2 = 0
    sFlowName2  = ""
    lcontinuousnoa2  =0
    bFlow3 = 0
    sFlowName3  = ""
    lcontinuousnoa3  =0
    bFlow4 = 0
    sFlowName4  = ""
    lcontinuousnoa4  =0
    bFlow5 = 0
    sFlowName5  = ""
    lcontinuousnoa5  =0
    bFlow6 = 0
    sFlowName6  = ""
    lcontinuousnoa6  =0
    bFlow7 = 0
    sFlowName7  = ""
    lcontinuousnoa7  =0
    bFlow8 = 0
    sFlowName8  = ""
    lcontinuousnoa8  =0
    bFlow9 = 0
    sFlowName9  = ""
    lcontinuousnoa9  =0
    bFlow10 = 0
    sFlowName10  = ""
    lcontinuousnoa10  =0
    
    bSAPCodeDone = 0
    bSAPCodeNotDone = 0

    cmbClassificationID = 0
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    

    sIssueDate3 = ""
    sIssueDate2 = ""
    sIssueDate1 = ""
    sIssueDate = "" 
    dtIssueDate = datetime.now()
    sIssueDate1 = str(datetime.now()) 
    sIssueDate = sIssueDate1[0:10]


    getFlow1Code = ""
    request.session['getFlow1Code']  =getFlow1Code
    getFlow2Code = ""
    request.session['getFlow2Code']  =getFlow2Code
    getFlow3Code = ""
    request.session['getFlow3Code']  =getFlow3Code
    getFlow4Code = ""
    request.session['getFlow4Code']  =getFlow4Code
    getFlow5Code = ""
    request.session['getFlow5Code']  =getFlow5Code
    getFlowContCode = ""
    request.session['getFlowContCode']  =getFlowContCode


    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
 
    request.session['sPlantCode']   =sPlantCode

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    if request.method == "POST":


        data = request.POST
        bSAPCodeDone = 0

        txtMissingScrapDate1 = ""
        txtMissingScrapDate2 = ""
        txtMissingScrapDate3 = ""
        txtMissingScrapDate = ""
        if 'txtMissingScrapDate' in request.POST:
            txtMissingScrapDate = data.get("txtMissingScrapDate")

            txtMissingScrapDate1 = txtMissingScrapDate
            txtMissingScrapDate2  = txtMissingScrapDate1.split("/")
            txtMissingScrapDate = ""
            
            if(len(txtMissingScrapDate2) > 1):
                txtMissingScrapDate = txtMissingScrapDate2[2] + "-" + txtMissingScrapDate2[1] + "-" + txtMissingScrapDate2[0]
            else:
                txtMissingScrapDate2  = txtMissingScrapDate1.split("-") 
                if(len(txtMissingScrapDate2) > 1):
                    txtMissingScrapDate = txtMissingScrapDate2[2] + "-" + txtMissingScrapDate2[1] + "-" + txtMissingScrapDate2[0] 

 




        if(txtMissingScrapDate == ''): 
            txtMissingScrapDate =str(datetime.now()) 
            txtMissingScrapDate = txtMissingScrapDate[0:10] 
 

        txtReason = ""
        if 'txtReason' in request.POST:
            txtReason = data.get("txtReason")

        txtApproved = ""
        if 'txtApproved' in request.POST:
            txtApproved = data.get("txtApproved")
            



        txtMissingScrapdBy = ""
        if 'txtMissingScrapdBy' in request.POST:
            txtMissingScrapdBy = data.get("txtMissingScrapdBy")


        if 'cmbClose' in request.POST: 
            return   redirect('Dashboard')  

            
        if 'cmbMissingScrap' in request.POST: 
        

            if (txtReason == 0):
                messages.success(request, 'Reason for Scrapping the Missing Gauge is not entered. Please enter Reason and Save')

                AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
                if AdminunitlistActive:
                    sPlantCode = AdminunitlistActive.splantno
                    sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
                    sPlantNameNameA = AdminunitlistActive.splantname

                request.session['sPlantCode']   =sPlantCode
                
                Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:
                    Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
                    
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else: 
                    Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
                    
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

                Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

                Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
                
                Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                lunitidA=request.session['lunitid']  
                AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

                Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)
        
                
                

                Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



                return render(request, "CloudCaliber/GaugeServiceRepair.html", 
                {
                    'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
                    
                    'CurDateNow':datetime.now(),
                    'lPlantId':lPlantId,  
                    '30DateNow':datetime.now() + timedelta(days=30),  
                    'AreaofUselist_list':AreaofUselist_list,
                    'Adminunitlist_list':Adminunitlist_list,
                    'title':'User list', 
                    'message':'Your User list page.',
                    'sPlantName': sPlantName , 
                    'Location': 0 , 
                    'semployeename':  semployeename,
                    'txtSearch': "" , 
                    'sCodeFinal1': "" ,  
                    'sCodeFinal2': "" ,  
                    'cmbClassificationID': 0 , 
                    'cmbCategoryID': 0 ,  
                    'cmbFlow1ID': 0 ,  
                    'cmbFlow2ID': 0 ,  
                    'cmbFlow3ID': 0 ,  
                    'cmbFlow4ID': 0 ,
                    'cmbFlow5ID': 0 ,     
                    'cmbFlow1label': "",  
                    'cmbFlow2label': "",  
                    'cmbFlow3label': "",  
                    'cmbFlow4label': "",
                    'cmbFlow5label': "",  
                    'bNewID': 0 ,  
                    'Adminassettypelist_list':Adminassettypelist_list,
                    'bSAPCodeDone': bSAPCodeDone, 
                    'bSAPCodeNotDone': bSAPCodeNotDone,  
                    'sIssueDate': sIssueDate, 
                }) 
            
            if (txtApproved == ""):
                messages.success(request, 'Scrapping the Missing Gauge Approval is not Entered. Please enter Approval Employee Name / ID  and Save')

                AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
                if AdminunitlistActive:
                    sPlantCode = AdminunitlistActive.splantno
                    sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
                    sPlantNameNameA = AdminunitlistActive.splantname

                request.session['sPlantCode']   =sPlantCode
                
                Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:
                    Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
                    
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else: 
                    Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
                    
                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

                if(sFlowName1 == "Part No1"):
                    Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
                else:  
                    Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

                Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

                Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
                
                Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                lunitidA=request.session['lunitid']  
                AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

                Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)
        
                
                

                Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



                return render(request, "CloudCaliber/GaugeServiceRepair.html", 
                {
                    'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
                    
                    'CurDateNow':datetime.now(),
                    'lPlantId':lPlantId,  
                    '30DateNow':datetime.now() + timedelta(days=30),  
                    'AreaofUselist_list':AreaofUselist_list,
                    'Adminunitlist_list':Adminunitlist_list,
                    'title':'User list', 
                    'message':'Your User list page.',
                    'sPlantName': sPlantName , 
                    'Location': 0 , 
                    'semployeename':  semployeename,
                    'txtSearch': "" , 
                    'sCodeFinal1': "" ,  
                    'sCodeFinal2': "" ,  
                    'cmbClassificationID': 0 , 
                    'cmbCategoryID': 0 ,  
                    'cmbFlow1ID': 0 ,  
                    'cmbFlow2ID': 0 ,  
                    'cmbFlow3ID': 0 ,  
                    'cmbFlow4ID': 0 ,
                    'cmbFlow5ID': 0 ,     
                    'cmbFlow1label': "",  
                    'cmbFlow2label': "",  
                    'cmbFlow3label': "",  
                    'cmbFlow4label': "",
                    'cmbFlow5label': "",  
                    'bNewID': 0 ,  
                    'Adminassettypelist_list':Adminassettypelist_list,
                    'bSAPCodeDone': bSAPCodeDone, 
                    'bSAPCodeNotDone': bSAPCodeNotDone,  
                    'sIssueDate': sIssueDate, 
                }) 
            
             
            shistorytype=""
            shistorytype="Service"
            scalibrationvendor=""
            scalibrationvendorid=""
            senteredby=""
            semployeename = request.session['semployeename'] 
            semployeeno = request.session['semployeeno']  
            senteredby= semployeename + " (" + semployeeno + ")"
            scalibrationresult="" 

              
            scurrentstatus=""
            scurrentstatus="Service"
            dtcalibrationdate=datetime.now()
            dtcalibrationdate=datetime.strptime(txtMissingScrapDate, '%d-%m-%Y').date()
            fcalibcost=0
            llplantid=0
            ssplantname=""
            slplantcode=""
            lcompanyid=0  
            llplantid=lPlantId
            ssplantname=sPlantName
            slplantcode=sPlantCode
            lcompanyid=lcompanyid  
    
            linstrumentid =0
            linstrumentid = lID
            sinstrumentid = ""
            sinstrumentDesc = ""
 
                
            Masterinstrumentslist_listAQ =  Masterinstrumentslist.objects.get(  lid=linstrumentid)
            if Masterinstrumentslist_listAQ:                
                sinstrumentid = Masterinstrumentslist_listAQ.sinstrumentid
                sinstrumentDesc = Masterinstrumentslist_listAQ.sdescription

            dtreturneddate=datetime.now()
            sinstrumentcode=""
            sinstrumentcode=sinstrumentid
            sdesc=""
            sdesc=sinstrumentDesc
            sto=""
            sfrom=""
            dthistorydate=datetime.now()
            shistorydate=""
            sreturneddate=""
            scomment=""
            llineid=0 

 
            MasterinstrumentslistSaveOBJA =  Masterinstrumentslist.objects.get(lid=linstrumentid) 
             
            
            scomment="Gauge Damaged - Repaired on " + str(txtMissingScrapDate) + " | by : " + senteredby + " | Approvedby : " + txtApproved + " | Reason : " + txtReason
            MasterinstrumentslistSaveOBJA.scurrentstatus ="Under Calibration" 
  
            
            MasterinstrumentslistSaveOBJA.save()

            ThistorytransactionsSave = Thistorytransactions(linstrumentid  = linstrumentid )
            ThistorytransactionsSave.save() 

                    
            lTransID =0
            lTransID = ThistorytransactionsSave.lid
            ThistorytransactionsSaveUpdate =  Thistorytransactions.objects.get(lid =lTransID) 

            ThistorytransactionsSaveUpdate.lhistorymainid=0
            ThistorytransactionsSaveUpdate.linstrumentid=linstrumentid
            ThistorytransactionsSaveUpdate.shistorytype=shistorytype
            ThistorytransactionsSaveUpdate.scalibrationvendor=scalibrationvendor
            ThistorytransactionsSaveUpdate.scalibrationvendorid=scalibrationvendorid
            ThistorytransactionsSaveUpdate.senteredby=senteredby
            ThistorytransactionsSaveUpdate.scalibrationresult=scalibrationresult
            ThistorytransactionsSaveUpdate.scurrentstatus=scomment
            ThistorytransactionsSaveUpdate.dtcalibrationdate=dtcalibrationdate
            ThistorytransactionsSaveUpdate.fcalibcost=fcalibcost
            ThistorytransactionsSaveUpdate.llplantid=llplantid
            ThistorytransactionsSaveUpdate.ssplantname=ssplantname
            ThistorytransactionsSaveUpdate.slplantcode=slplantcode
            ThistorytransactionsSaveUpdate.lcompanyid=lcompanyid
            ThistorytransactionsSaveUpdate.dtreturneddate=dtreturneddate
            ThistorytransactionsSaveUpdate.sinstrumentcode=sinstrumentcode
            ThistorytransactionsSaveUpdate.sdesc=sdesc
            ThistorytransactionsSaveUpdate.sto=sto
            ThistorytransactionsSaveUpdate.sfrom=sfrom
            ThistorytransactionsSaveUpdate.dthistorydate=dthistorydate
            ThistorytransactionsSaveUpdate.shistorydate=shistorydate
            ThistorytransactionsSaveUpdate.sreturneddate=sreturneddate
            ThistorytransactionsSaveUpdate.llineid=llineid 
            ThistorytransactionsSaveUpdate.scomment=scomment



            ThistorytransactionsSaveUpdate.save()







            scurrentstatusMaster = "IDLE"
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
            
            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno
                sPlantName = AdminunitlistActive.splantname

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



            lhistorymainid =0
            linstrumentid = lID
            lscheduleid = 0
            sinstrumentcode = ""
            sinstrumentdesc = ""
            scurrentstatus = ""
            scalibrationresult = ""
            dtcalibrationdate = datetime.now()
            scalibrationdate = ""


            scalibrationdate1 = ""
            scalibrationdate2 = ""
            scalibrationdate3 = ""
            scalibrationdate1 = str(dtcalibrationdate)
            scalibrationdate2  = scalibrationdate1.split("-")
            
            scalibrationdate3  = scalibrationdate2[2].split(" ")
            
            scalibrationdate = scalibrationdate3[0] + "-" + scalibrationdate2[1] + "-" + scalibrationdate2[0] 


            fcalibcost = 0
            stimetaken = ""
            sdevicecondition = ""
            stemperature  =  ""
            shumidity  =  ""
            lenteredbyid  =  0
            senteredby  =  ""
            lapprovedbyid  =  0
            sapprovedby  =  ""
            sapprovaldate  =  ""
            scertificateno  =  ""
            scomments  =  ""
            scalibrationvendor  =  ""
            lcalibrationvendorid  =  0
            spurchaseorderno = ""
            scalibrationcertificatefile = ""
            scalibrationcertificatepath = ""
            straceability = ""
            dtdispatchdate = datetime.now()
            sdispatchdate = ""
            dtduedate = datetime.now()
            sduedate = ""
            lcalibratedbyid = 0
            scalibratedby = ""
            bapproved = 0
            scalibrationcertificateno = ""
            bcertificate = 0
            ftotalerror = 0
            facconstant = 0
            flc = 0
            fproducttolerance = 0
            facceptancecriteria = 0
            dtindentdate = datetime.now()
            sndentdate = ""
            dgtreturneddate = datetime.now()
            sreturneddate = ""
            dtissuedate = datetime.now()
            sissuedate = ""
            bpressuregauge = 0
            btimer = 0
            bpowersupply = 0
            bgeneral = 0
            bvernier = 0
            bboregaugewithdial = 0
            bboregauge = 0
            bdialindicator = 0
            bheightgauge = 0
            bmicrometer = 0
            ferrormax = 0
            ferrormin = 0
            ftotalerror1 = 0
            dtrecddate = datetime.now()
            srecddate = ""
            dtissueddate = datetime.now()
            sissueddate = ""
            scategory = ""
            spurchaseordernosinstdesc = ""
            stemp1 = ""
            stemp2 = ""
            stemp3 = ""
            stemp4 = ""
            stemp5 = ""
            stemp6 = ""
            stemp7 = ""
            stemp8 = ""
            stemp9 = ""
            stemp10 = ""
            straceabilityfile1 = ""
            straceabilitypath1 = ""
            straceabilityfile2 = ""
            straceabilitypath2 = ""
            straceabilityfile3 = ""
            straceabilitypath3 = ""
            bdcdone = 0
            lplantid = 0
            splantname = ""
            lplantcode = ""
            lcompanyid = 0
            lplantcode =sPlantCode
            lplantid =lunitid
            lcompanyid =lcompanyid
            splantname = sPlantName

            spodate = ""
            binternal = 0
            bexternal = 0
            snablexpirydate = ""
            sexternalnablcertificate = ""
            bissued = 0
            bapprove = 0
            breturned = 0
            llastlocationid = 0
            lrepairid = 0
            lrecalibrationid = 0
            slaststatus = "" 
            slastlocation = "" 
            slastissuedto = "" 
            slastmachineto = "" 
            slastpartnoto = "" 


            lhistorytraceid1 = 0
            lhistorytraceid2 = 0
            lhistorytraceid3 = 0
            lhistorytraceid4 = 0
            lhistorytraceid5 = 0

            
            shistorytraceid1 = "" 
            shistorytraceid2 = "" 
            shistorytraceid3 = "" 
            shistorytraceid4 = "" 
            shistorytraceid5 = "" 

            lcalibratedbyid = lLoginUserId
            scalibratedby = semployeename + " (" + semployeeno + ")"


            lSerNo =0
            ThistorymainFind =  Thistorymain.objects.values().filter(linstrumentid =linstrumentid)
            if ThistorymainFind:
                for ThistorymainFindA in ThistorymainFind:
                    lSerNo = lSerNo +1

            lscheduleid = lSerNo

            Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
            lConditionId =0    
            if(Admincalibconditionslist_list1):
                lConditionId =0
                for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                    if(lConditionId ==0 ):
                        lConditionId = Admincalibconditionslist_listOBJ.lid


            AdmincalibconditionslistFind =  Admincalibconditionslist.objects.get(lid=lConditionId)  
            if AdmincalibconditionslistFind:
                stemperature = AdmincalibconditionslistFind.stemperature
                shumidity = AdmincalibconditionslistFind.shumidity

            
            MasterinstrumentslistFind =  Masterinstrumentslist.objects.get(lid =linstrumentid)

            Masterinstrumentslistpart2AOBJAB =  Masterinstrumentslistpart2.objects.filter(linstrumentid=linstrumentid).values()
                    

            if MasterinstrumentslistFind:

                

                lhistorycard =0
                bsentforcalibration = 1
                sinstrumentcode = MasterinstrumentslistFind.sinstrumentid
                sinstrumentdesc = MasterinstrumentslistFind.sdescription

                dtduedate = MasterinstrumentslistFind.dtnextcalib
                sduedate = MasterinstrumentslistFind.snextcalibdate
                sdevicecondition = MasterinstrumentslistFind.scurrentstatus
                stemp10= MasterinstrumentslistFind.scurrentstatus
                slaststatus= MasterinstrumentslistFind.scurrentstatus
                llastlocationid= MasterinstrumentslistFind.ldefaultlocationid
                slastlocation= MasterinstrumentslistFind.slocationname
                slastissuedto= MasterinstrumentslistFind.sissuedto
                slastmachineto= MasterinstrumentslistFind.sissuedmachineto
                slastpartnoto= MasterinstrumentslistFind.sissuedpartno



                ThistorymainSave = Thistorymain(  linstrumentid = linstrumentid, stemp10 =scurrentstatusMaster )

                ThistorymainSave.save() 


                lhistorymainid =0
                lhistorymainid = ThistorymainSave.lhistorymainid  


                dtnextcalib = datetime.now() 
                snextcalibdate = ""

                snextcalibdate2 = ""
                snextcalibdate1 = str(dtnextcalib)
                snextcalibdate2  = snextcalibdate1.split("-")
                
                snextcalibdate3  = snextcalibdate2[2].split(" ")
                
                snextcalibdate = snextcalibdate3[0] + "-" + snextcalibdate2[1] + "-" + snextcalibdate2[0] 

                dtnextcalib = datetime.strptime(snextcalibdate, '%d-%m-%Y').date()

                MasterinstrumentslistFind.bsentforcalibration = bsentforcalibration
                MasterinstrumentslistFind.lhistorycard = lhistorymainid

                MasterinstrumentslistFind.scalibrationstartdate = snextcalibdate
                MasterinstrumentslistFind.lhistorycard = lhistorymainid
                MasterinstrumentslistFind.lhistoryid = lhistorymainid
                MasterinstrumentslistFind.scurrentstatus='UNDER CALIBRATION'
                MasterinstrumentslistFind.save() 



                slscheduleid =""
                slscheduleid = str(lscheduleid)
                if(len(slscheduleid )== 1):
                    scalibrationcertificateno  = sinstrumentcode + "-000" + slscheduleid
                elif (len(slscheduleid )== 2):
                    scalibrationcertificateno  = sinstrumentcode + "-00" + slscheduleid
                elif (len(slscheduleid )== 3):
                    scalibrationcertificateno  = sinstrumentcode + "-0" + slscheduleid
                else:
                    scalibrationcertificateno  = sinstrumentcode + "-" + slscheduleid



                ThistorymainSaveUpdate =  Thistorymain.objects.get(lhistorymainid =lhistorymainid)
                
                ThistorymainSaveUpdate.lscheduleid = lscheduleid
                ThistorymainSaveUpdate.sinstrumentcode = sinstrumentcode
                ThistorymainSaveUpdate.sinstrumentdesc = sinstrumentdesc
                ThistorymainSaveUpdate.scurrentstatus = scurrentstatus
                ThistorymainSaveUpdate.scalibrationresult = scalibrationresult
                ThistorymainSaveUpdate.dtcalibrationdate = dtcalibrationdate
                ThistorymainSaveUpdate.scalibrationdate = scalibrationdate
                ThistorymainSaveUpdate.fcalibcost = fcalibcost
                ThistorymainSaveUpdate.stimetaken = stimetaken
                ThistorymainSaveUpdate.sdevicecondition = sdevicecondition
                ThistorymainSaveUpdate.stemperature = stemperature
                ThistorymainSaveUpdate.shumidity = shumidity
                ThistorymainSaveUpdate.lenteredbyid = lenteredbyid
                ThistorymainSaveUpdate.senteredby = senteredby
                ThistorymainSaveUpdate.lapprovedbyid = lapprovedbyid
                ThistorymainSaveUpdate.sapprovedby = sapprovedby
                ThistorymainSaveUpdate.sapprovaldate = sapprovaldate
                ThistorymainSaveUpdate.scertificateno = scertificateno
                ThistorymainSaveUpdate.scomments = scomments
                ThistorymainSaveUpdate.scalibrationvendor = scalibrationvendor
                ThistorymainSaveUpdate.lcalibrationvendorid = lcalibrationvendorid
                ThistorymainSaveUpdate.spurchaseorderno = spurchaseorderno
                ThistorymainSaveUpdate.scalibrationcertificatefile = scalibrationcertificatefile
                ThistorymainSaveUpdate.scalibrationcertificatepath = scalibrationcertificatepath
                ThistorymainSaveUpdate.straceability = straceability
                ThistorymainSaveUpdate.dtdispatchdate = dtdispatchdate
                ThistorymainSaveUpdate.sdispatchdate = sdispatchdate
                ThistorymainSaveUpdate.dtduedate = dtduedate
                ThistorymainSaveUpdate.sduedate = sduedate
                ThistorymainSaveUpdate.lcalibratedbyid = lcalibratedbyid
                ThistorymainSaveUpdate.scalibratedby = scalibratedby
                ThistorymainSaveUpdate.bapproved = bapproved
                ThistorymainSaveUpdate.scalibrationcertificateno = scalibrationcertificateno
                ThistorymainSaveUpdate.bcertificate = bcertificate
                ThistorymainSaveUpdate.ftotalerror = ftotalerror
                ThistorymainSaveUpdate.facconstant = facconstant
                ThistorymainSaveUpdate.flc = flc
                ThistorymainSaveUpdate.fproducttolerance = fproducttolerance
                ThistorymainSaveUpdate.facceptancecriteria = facceptancecriteria
                ThistorymainSaveUpdate.dtindentdate = dtindentdate
                ThistorymainSaveUpdate.sndentdate = sndentdate
                ThistorymainSaveUpdate.dgtreturneddate = dgtreturneddate
                ThistorymainSaveUpdate.sreturneddate = sreturneddate
                ThistorymainSaveUpdate.dtissuedate = dtissuedate
                ThistorymainSaveUpdate.sissuedate = sissuedate
                ThistorymainSaveUpdate.bpressuregauge = bpressuregauge
                ThistorymainSaveUpdate.btimer = btimer
                ThistorymainSaveUpdate.bpowersupply = bpowersupply
                ThistorymainSaveUpdate.bgeneral = bgeneral
                ThistorymainSaveUpdate.bvernier = bvernier
                ThistorymainSaveUpdate.bboregaugewithdial = bboregaugewithdial
                ThistorymainSaveUpdate.bboregauge = bboregauge
                ThistorymainSaveUpdate.bdialindicator = bdialindicator
                ThistorymainSaveUpdate.bheightgauge = bheightgauge
                ThistorymainSaveUpdate.bmicrometer = bmicrometer
                ThistorymainSaveUpdate.ferrormax = ferrormax
                ThistorymainSaveUpdate.ferrormin = ferrormin
                ThistorymainSaveUpdate.ftotalerror1 = ftotalerror1
                ThistorymainSaveUpdate.dtrecddate = dtrecddate
                ThistorymainSaveUpdate.srecddate = srecddate
                ThistorymainSaveUpdate.dtissueddate = dtissueddate
                ThistorymainSaveUpdate.sissueddate = sissueddate
                ThistorymainSaveUpdate.scategory = scategory
                ThistorymainSaveUpdate.spurchaseordernosinstdesc = spurchaseordernosinstdesc
                ThistorymainSaveUpdate.stemp1 = stemp1
                ThistorymainSaveUpdate.stemp2 = stemp2
                ThistorymainSaveUpdate.stemp3 = stemp3
                ThistorymainSaveUpdate.stemp4 = stemp4
                ThistorymainSaveUpdate.stemp5 = stemp5
                ThistorymainSaveUpdate.stemp6 = stemp6
                ThistorymainSaveUpdate.stemp7 = stemp7
                ThistorymainSaveUpdate.stemp8 = stemp8
                ThistorymainSaveUpdate.stemp9 = stemp9
                ThistorymainSaveUpdate.stemp10 = stemp10
                ThistorymainSaveUpdate.straceabilityfile1 = straceabilityfile1
                ThistorymainSaveUpdate.straceabilitypath1 = straceabilitypath1
                ThistorymainSaveUpdate.straceabilityfile2 = straceabilityfile2
                ThistorymainSaveUpdate.straceabilitypath2 = straceabilitypath2
                ThistorymainSaveUpdate.straceabilityfile3 = straceabilityfile3
                ThistorymainSaveUpdate.straceabilitypath3 = straceabilitypath3
                ThistorymainSaveUpdate.bdcdone = bdcdone
                ThistorymainSaveUpdate.lplantid = lplantid
                ThistorymainSaveUpdate.splantname = splantname
                ThistorymainSaveUpdate.lplantcode = lplantcode
                ThistorymainSaveUpdate.lcompanyid = lcompanyid
                sagencyservice = ""

                for Masterinstrumentslistpart2AOBJAB1 in Masterinstrumentslistpart2AOBJAB:

                    sagencyservice = Masterinstrumentslistpart2AOBJAB1['sagencyservice']
                    if (sagencyservice == "A"):                    
                        ThistorymainSaveUpdate.bexternal =1
                        ThistorymainSaveUpdate.binternal =0
                    elif (Masterinstrumentslistpart2AOBJAB1['sagencyservice'] == "C"):                    
                        ThistorymainSaveUpdate.bexternal =1
                        ThistorymainSaveUpdate.binternal =0
                    else:          
                        ThistorymainSaveUpdate.bexternal =0
                        ThistorymainSaveUpdate.binternal =1
                ThistorymainSaveUpdate.snablexpirydate =""
                ThistorymainSaveUpdate.sexternalnablcertificate =""
                ThistorymainSaveUpdate.bissued =0
                ThistorymainSaveUpdate.bapprove =0
                ThistorymainSaveUpdate.breturned =0
                ThistorymainSaveUpdate.llastlocationid =llastlocationid
                ThistorymainSaveUpdate.lrepairid =0
                ThistorymainSaveUpdate.lrecalibrationid =0
                ThistorymainSaveUpdate.slaststatus =slaststatus
                ThistorymainSaveUpdate.slastlocation =slastlocation
                ThistorymainSaveUpdate.slastissuedto =slastissuedto
                ThistorymainSaveUpdate.slastmachineto =slastmachineto
                ThistorymainSaveUpdate.slastpartnoto =slastpartnoto


                ThistorymainSaveUpdate.save() 



            lhistoryid  = 0
            lhistoryid =lhistorymainid
            linstrumentid =linstrumentid
            lmasterinstrumentid1 = 0
            smasterinstrumentid1 = ""
            smasterdescription1 = ""
            slastcalibrationdate1 = ""
            snextcalibrationdate1 = ""
            lmasterinstrumentid2 = 0
            smasterinstrumentid2 = ""
            smasterdescription2 = ""
            slastcalibrationdate2 = ""
            snextcalibrationdate2 = ""
            lmasterinstrumentid3 = 0
            smasterinstrumentid3 = ""
            smasterdescription3 = ""
            slastcalibrationdate3 = ""
            snextcalibrationdate3 = ""
            lmasterinstrumentid4 = 0
            smasterinstrumentid4 = ""
            smasterdescription4 = ""
            slastcalibrationdate4 = ""
            snextcalibrationdate4 = ""
            lmasterinstrumentid5 = 0
            smasterinstrumentid5 = ""
            smasterdescription5 = ""
            slastcalibrationdate5 = ""
            snextcalibrationdate5 = ""
            stypeoffile1 = ""
            sfile1 = ""
            stypeoffile2 = ""
            sfile2 = ""
            stypeoffile3 = ""
            sfile3 = ""
            stypeoffile4 = ""
            sfile4 = ""
            stypeoffile5 = ""
            sfile5 = ""
            suom1 = ""
            sappliedvalue1 = ""
            fappliedvaluea1 = 0
            fappliedvalueb1 = 0
            fappliedvaluec1 = 0
            fappliedvalued1 = 0
            fappliedvaluee1 = 0
            derrorallowed1 = 0
            dmax1 = 0
            dmin1 = 0
            suom2 = ""
            sappliedvalue2 = ""
            fappliedvaluea2 = 0
            fappliedvalueb2 = 0
            fappliedvaluec2 = 0
            fappliedvalued2 = 0
            fappliedvaluee2 = 0
            derrorallowed2 = 0
            dmax2 = 0
            dmin2 = 0
            suom3 = ""
            sappliedvalue3 = ""
            fappliedvaluea3 = 0
            fappliedvalueb3 = 0
            fappliedvaluec3 = 0
            fappliedvalued3 = 0
            fappliedvaluee3 = 0
            derrorallowed3 = 0
            dmax3 = 0
            dmin3 = 0
            suom4 = ""
            sappliedvalue4 = ""
            fappliedvaluea4 = 0
            fappliedvalueb4 = 0
            fappliedvaluec4 = 0
            fappliedvalued4 = 0
            fappliedvaluee4 = 0
            derrorallowed4 = 0
            dmax4 = 0
            dmin4 = 0
            suom5 = ""
            sappliedvalue5 = ""
            fappliedvaluea5 = 0
            fappliedvalueb5 = 0
            fappliedvaluec5 = 0
            fappliedvalued5 = 0
            fappliedvaluee5 = 0
            derrorallowed5 = 0
            dmax5 = 0
            dmin5 = 0
            suom6 = ""
            sappliedvalue6 = ""
            fappliedvaluea6 = 0
            fappliedvalueb6 = 0
            fappliedvaluec6 = 0
            fappliedvalued6 = 0
            fappliedvaluee6 = 0
            derrorallowed6 = 0
            dmax6 = 0
            dmin6 = 0
            suom7 = ""
            sappliedvalue7 = ""
            fappliedvaluea7 = 0
            fappliedvalueb7 = 0
            fappliedvaluec7 = 0
            fappliedvalued7 = 0
            fappliedvaluee7 = 0
            derrorallowed7 = 0
            dmax7 = 0
            dmin7 = 0
            suom8 = ""
            sappliedvalue8 = ""
            fappliedvaluea8 = 0
            fappliedvalueb8 = 0
            fappliedvaluec8 = 0
            fappliedvalued8 = 0
            fappliedvaluee8 = 0
            derrorallowed8 = 0
            dmax8 = 0
            dmin8 = 0
            suom9 = ""
            sappliedvalue9 = ""
            fappliedvaluea9 = 0
            fappliedvalueb9 = 0
            fappliedvaluec9 = 0
            fappliedvalued9 = 0
            fappliedvaluee9 = 0
            derrorallowed9 = 0
            dmax9 = 0
            dmin9 = 0
            suom10 = ""
            sappliedvalue10 = ""
            fappliedvaluea10 = 0
            fappliedvalueb10 = 0
            fappliedvaluec10 = 0
            fappliedvalued10 = 0
            fappliedvaluee10 = 0
            derrorallowed10 = 0
            dmax10 = 0
            dmin10 = 0
            suom11 = ""
            sappliedvalue11 = ""
            fappliedvaluea11 = 0
            fappliedvalueb11 = 0
            fappliedvaluec11 = 0
            fappliedvalued11 = 0
            fappliedvaluee11 = 0
            derrorallowed11 = 0
            dmax11 = 0
            dmin11 = 0
            suom12 = ""
            sappliedvalue12 = ""
            fappliedvaluea12 = 0
            fappliedvalueb12 = 0
            fappliedvaluec12 = 0
            fappliedvalued12 = 0
            fappliedvaluee12 = 0
            derrorallowed12 = 0
            dmax12 = 0
            dmin12 = 0
            suom13 = ""
            sappliedvalue13 = ""
            fappliedvaluea13 = 0
            fappliedvalueb13 = 0
            fappliedvaluec13 = 0
            fappliedvalued13 = 0
            fappliedvaluee13 = 0
            derrorallowed13 = 0
            dmax13 = 0
            dmin13 = 0
            suom14 = ""
            sappliedvalue14 = ""
            fappliedvaluea14 = 0
            fappliedvalueb14 = 0
            fappliedvaluec14 = 0
            fappliedvalued14 = 0
            fappliedvaluee14 = 0
            derrorallowed14 = 0
            dmax14 = 0
            dmin14 = 0
            suom15 = ""
            sappliedvalue15 = ""
            fappliedvaluea15 = 0
            fappliedvalueb15 = 0
            fappliedvaluec15 = 0
            fappliedvalued15 = 0
            fappliedvaluee15 = 0
            derrorallowed15 = 0
            dmax15 = 0
            dmin15 = 0
            suom16 = ""
            sappliedvalue16 = ""
            fappliedvaluea16 = 0
            fappliedvalueb16 = 0
            fappliedvaluec16 = 0
            fappliedvalued16 = 0
            fappliedvaluee16 = 0
            derrorallowed16 = 0
            dmax16 = 0
            dmin16 = 0
            suom17 = ""
            sappliedvalue17 = ""
            fappliedvaluea17 = 0
            fappliedvalueb17 = 0
            fappliedvaluec17 = 0
            fappliedvalued17 = 0
            fappliedvaluee17 = 0
            derrorallowed17 = 0
            dmax17 = 0
            dmin17 = 0
            suom18 = ""
            sappliedvalue18 = ""
            fappliedvaluea18 = 0
            fappliedvalueb18 = 0
            fappliedvaluec18 = 0
            fappliedvalued18 = 0
            fappliedvaluee18 = 0
            derrorallowed18 = 0
            dmax18 = 0
            dmin18 = 0
            suom19 = ""
            sappliedvalue19 = ""
            fappliedvaluea19 = 0
            fappliedvalueb19 = 0
            fappliedvaluec19 = 0
            fappliedvalued19 = 0
            fappliedvaluee19 = 0
            derrorallowed19 = 0
            dmax19 = 0
            dmin19 = 0
            suom20 = ""
            sappliedvalue20 = ""
            fappliedvaluea20 = 0
            fappliedvalueb20 = 0
            fappliedvaluec20 = 0
            fappliedvalued20 = 0
            fappliedvaluee20 = 0
            derrorallowed20 = 0
            dmax20 = 0
            dmin20 = 0
            suom21 = ""
            sappliedvalue21 = ""
            fappliedvaluea21 = 0
            fappliedvalueb21 = 0
            fappliedvaluec21 = 0
            fappliedvalued21 = 0
            fappliedvaluee21 = 0
            derrorallowed21 = 0
            dmax21 = 0
            dmin21 = 0
            suom22 = ""
            sappliedvalue22 = ""
            fappliedvaluea22 = 0
            fappliedvalueb22 = 0
            fappliedvaluec22 = 0
            fappliedvalued22 = 0
            fappliedvaluee22 = 0
            derrorallowed22 = 0
            dmax22 = 0
            dmin22 = 0
            suom23 = ""
            sappliedvalue23 = ""
            fappliedvaluea23 = 0
            fappliedvalueb23 = 0
            fappliedvaluec23 = 0
            fappliedvalued23 = 0
            fappliedvaluee23 = 0
            derrorallowed23 = 0
            dmax23 = 0
            dmin23 = 0
            suom24 = ""
            sappliedvalue24 = ""
            fappliedvaluea24 = 0
            fappliedvalueb24 = 0
            fappliedvaluec24 = 0
            fappliedvalued24 = 0
            fappliedvaluee24 = 0
            derrorallowed24 = 0
            dmax24 = 0
            dmin24 = 0
            suom25 = ""
            sappliedvalue25 = ""
            fappliedvaluea25 = 0
            fappliedvalueb25 = 0
            fappliedvaluec25 = 0
            fappliedvalued25 = 0
            fappliedvaluee25 = 0
            derrorallowed25 = 0
            dmax25 = 0
            dmin25 = 0
            suom26 = ""
            sappliedvalue26 = ""
            fappliedvaluea26 = 0
            fappliedvalueb26 = 0
            fappliedvaluec26 = 0
            fappliedvalued26 = 0
            fappliedvaluee26 = 0
            derrorallowed26 = 0
            dmax26 = 0
            dmin26 = 0
            suom27 = ""
            sappliedvalue27 = ""
            fappliedvaluea27 = 0
            fappliedvalueb27 = 0
            fappliedvaluec27 = 0
            fappliedvalued27 = 0
            fappliedvaluee27 = 0
            derrorallowed27 = 0
            dmax27 = 0
            dmin27 = 0
            suom28 = ""
            sappliedvalue28 = ""
            fappliedvaluea28 = 0
            fappliedvalueb28 = 0
            fappliedvaluec28 = 0
            fappliedvalued28 = 0
            fappliedvaluee28 = 0
            derrorallowed28 = 0
            dmax28 = 0
            dmin28 = 0
            suom29 = ""
            sappliedvalue29 = ""
            fappliedvaluea29 = 0
            fappliedvalueb29 = 0
            fappliedvaluec29 = 0
            fappliedvalued29 = 0
            fappliedvaluee29 = 0
            derrorallowed29 = 0
            dmax29 = 0
            dmin29 = 0
            suom30 = ""
            sappliedvalue30 = ""
            fappliedvaluea30 = 0
            fappliedvalueb30 = 0
            fappliedvaluec30 = 0
            fappliedvalued30 = 0
            fappliedvaluee30 = 0
            derrorallowed30 = 0



            dmax30 = 0
            dmin30 = 0


            lPart3ID =0
            Masterinstrumentslistpart3Filter =  Masterinstrumentslistpart3.objects.values().filter(linstrumentid =linstrumentid) 
            
            if Masterinstrumentslistpart3Filter:
                for Masterinstrumentslistpart3FilterA in Masterinstrumentslistpart3Filter:
                    lPart3ID =Masterinstrumentslistpart3FilterA['lid']

                    Masterinstrumentslistpart3Find =  Masterinstrumentslistpart3.objects.get(lid=lPart3ID)
                    if Masterinstrumentslistpart3Find:
                        
                        lmasterinstrumentid1 = Masterinstrumentslistpart3Find.lmasterinstrumentid1

                        if (lmasterinstrumentid1 != 0):
                            MasterinstrumentslistFind1 =  Masterinstrumentslist.objects.get(lid =lmasterinstrumentid1)
                            if MasterinstrumentslistFind1:  
                                lhistorytraceid1 = MasterinstrumentslistFind1.lhistoryid
                                shistorytraceid1 = MasterinstrumentslistFind1.scertificateno

                        smasterinstrumentid1 =  Masterinstrumentslistpart3Find.smasterinstrumentid1
                        smasterdescription1 =  Masterinstrumentslistpart3Find.smasterdescription1 
                        lmasterinstrumentid2 =  Masterinstrumentslistpart3Find.lmasterinstrumentid2
                        if (lmasterinstrumentid2 != 0):
                            MasterinstrumentslistFind2 =  Masterinstrumentslist.objects.get(lid =lmasterinstrumentid2)
                            if MasterinstrumentslistFind2:  
                                lhistorytraceid2 = MasterinstrumentslistFind2.lhistoryid
                                shistorytraceid2 = MasterinstrumentslistFind2.scertificateno

                        smasterinstrumentid2 =  Masterinstrumentslistpart3Find.smasterinstrumentid2
                        smasterdescription2 =  Masterinstrumentslistpart3Find.smasterdescription2
                        lmasterinstrumentid3 =  Masterinstrumentslistpart3Find.lmasterinstrumentid3
                        if (lmasterinstrumentid3 != 0):
                            MasterinstrumentslistFind3 =  Masterinstrumentslist.objects.get(lid =lmasterinstrumentid3)
                            if MasterinstrumentslistFind3:  
                                lhistorytraceid3 = MasterinstrumentslistFind3.lhistoryid
                                shistorytraceid3 = MasterinstrumentslistFind3.scertificateno

                        smasterinstrumentid3 =  Masterinstrumentslistpart3Find.smasterinstrumentid3
                        smasterdescription3 =  Masterinstrumentslistpart3Find.smasterdescription3
                        lmasterinstrumentid4 =  Masterinstrumentslistpart3Find.lmasterinstrumentid4
                        if (lmasterinstrumentid4 != 0):
                            MasterinstrumentslistFind4 =  Masterinstrumentslist.objects.get(lid =lmasterinstrumentid4)
                            if MasterinstrumentslistFind4:  
                                lhistorytraceid4 = MasterinstrumentslistFind4.lhistoryid
                                shistorytraceid4 = MasterinstrumentslistFind4.scertificateno

                        smasterinstrumentid4 =  Masterinstrumentslistpart3Find.smasterinstrumentid4
                        smasterdescription4 =  Masterinstrumentslistpart3Find.smasterdescription4
                        lmasterinstrumentid5 =  Masterinstrumentslistpart3Find.lmasterinstrumentid5
                        if (lmasterinstrumentid5 != 0):
                            MasterinstrumentslistFind5 =  Masterinstrumentslist.objects.get(lid =lmasterinstrumentid5)
                            if MasterinstrumentslistFind5:  
                                lhistorytraceid5 = MasterinstrumentslistFind5.lhistoryid
                                shistorytraceid5 = MasterinstrumentslistFind5.scertificateno

                        smasterinstrumentid5 =  Masterinstrumentslistpart3Find.smasterinstrumentid5
                        smasterdescription5 =  Masterinstrumentslistpart3Find.smasterdescription5 
 


                        suom1 =     Masterinstrumentslistpart3Find.suom1
                        sappliedvalue1 =     Masterinstrumentslistpart3Find.sappliedvalue1
                        fappliedvaluea1 =     Masterinstrumentslistpart3Find.fappliedvaluea1
                        fappliedvalueb1 =     Masterinstrumentslistpart3Find.fappliedvalueb1
                        fappliedvaluec1 =     Masterinstrumentslistpart3Find.fappliedvaluec1
                        fappliedvalued1 =     Masterinstrumentslistpart3Find.fappliedvalued1
                        fappliedvaluee1 =     Masterinstrumentslistpart3Find.fappliedvaluee1
                        derrorallowed1 =     Masterinstrumentslistpart3Find.derrorallowed1
                        dmax1 =     Masterinstrumentslistpart3Find.dmax1
                        dmin1 =     Masterinstrumentslistpart3Find.dmin1
                        suom2 =     Masterinstrumentslistpart3Find.suom2
                        sappliedvalue2 =     Masterinstrumentslistpart3Find.sappliedvalue2
                        fappliedvaluea2 =     Masterinstrumentslistpart3Find.fappliedvaluea2
                        fappliedvalueb2 =     Masterinstrumentslistpart3Find.fappliedvalueb2
                        fappliedvaluec2 =     Masterinstrumentslistpart3Find.fappliedvaluec2
                        fappliedvalued2 =     Masterinstrumentslistpart3Find.fappliedvalued2
                        fappliedvaluee2 =     Masterinstrumentslistpart3Find.fappliedvaluee2
                        derrorallowed2 =     Masterinstrumentslistpart3Find.derrorallowed2
                        dmax2 =     Masterinstrumentslistpart3Find.dmax2
                        dmin2 =     Masterinstrumentslistpart3Find.dmin2
                        suom3 =     Masterinstrumentslistpart3Find.suom3
                        sappliedvalue3 =     Masterinstrumentslistpart3Find.sappliedvalue3
                        fappliedvaluea3 =     Masterinstrumentslistpart3Find.fappliedvaluea3
                        fappliedvalueb3 =     Masterinstrumentslistpart3Find.fappliedvalueb3
                        fappliedvaluec3 =     Masterinstrumentslistpart3Find.fappliedvaluec3
                        fappliedvalued3 =     Masterinstrumentslistpart3Find.fappliedvalued3
                        fappliedvaluee3 =     Masterinstrumentslistpart3Find.fappliedvaluee3
                        derrorallowed3 =     Masterinstrumentslistpart3Find.derrorallowed3
                        dmax3 =     Masterinstrumentslistpart3Find.dmax3
                        dmin3 =     Masterinstrumentslistpart3Find.dmin3
                        suom4 =     Masterinstrumentslistpart3Find.suom4
                        sappliedvalue4 =     Masterinstrumentslistpart3Find.sappliedvalue4
                        fappliedvaluea4 =     Masterinstrumentslistpart3Find.fappliedvaluea4
                        fappliedvalueb4 =     Masterinstrumentslistpart3Find.fappliedvalueb4
                        fappliedvaluec4 =     Masterinstrumentslistpart3Find.fappliedvaluec4
                        fappliedvalued4 =     Masterinstrumentslistpart3Find.fappliedvalued4
                        fappliedvaluee4 =     Masterinstrumentslistpart3Find.fappliedvaluee4
                        derrorallowed4 =     Masterinstrumentslistpart3Find.derrorallowed4
                        dmax4 =     Masterinstrumentslistpart3Find.dmax4
                        dmin4 =     Masterinstrumentslistpart3Find.dmin4
                        suom5 =     Masterinstrumentslistpart3Find.suom5
                        sappliedvalue5 =     Masterinstrumentslistpart3Find.sappliedvalue5
                        fappliedvaluea5 =     Masterinstrumentslistpart3Find.fappliedvaluea5
                        fappliedvalueb5 =     Masterinstrumentslistpart3Find.fappliedvalueb5
                        fappliedvaluec5 =     Masterinstrumentslistpart3Find.fappliedvaluec5
                        fappliedvalued5 =     Masterinstrumentslistpart3Find.fappliedvalued5
                        fappliedvaluee5 =     Masterinstrumentslistpart3Find.fappliedvaluee5
                        derrorallowed5 =     Masterinstrumentslistpart3Find.derrorallowed5
                        dmax5 =     Masterinstrumentslistpart3Find.dmax5
                        dmin5 =     Masterinstrumentslistpart3Find.dmin5
                        suom6 =     Masterinstrumentslistpart3Find.suom6
                        sappliedvalue6 =     Masterinstrumentslistpart3Find.sappliedvalue6
                        fappliedvaluea6 =     Masterinstrumentslistpart3Find.fappliedvaluea6
                        fappliedvalueb6 =     Masterinstrumentslistpart3Find.fappliedvalueb6
                        fappliedvaluec6 =     Masterinstrumentslistpart3Find.fappliedvaluec6
                        fappliedvalued6 =     Masterinstrumentslistpart3Find.fappliedvalued6
                        fappliedvaluee6 =     Masterinstrumentslistpart3Find.fappliedvaluee6
                        derrorallowed6 =     Masterinstrumentslistpart3Find.derrorallowed6
                        dmax6 =     Masterinstrumentslistpart3Find.dmax6
                        dmin6 =     Masterinstrumentslistpart3Find.dmin6
                        suom7 =     Masterinstrumentslistpart3Find.suom7
                        sappliedvalue7 =     Masterinstrumentslistpart3Find.sappliedvalue7
                        fappliedvaluea7 =     Masterinstrumentslistpart3Find.fappliedvaluea7
                        fappliedvalueb7 =     Masterinstrumentslistpart3Find.fappliedvalueb7
                        fappliedvaluec7 =     Masterinstrumentslistpart3Find.fappliedvaluec7
                        fappliedvalued7 =     Masterinstrumentslistpart3Find.fappliedvalued7
                        fappliedvaluee7 =     Masterinstrumentslistpart3Find.fappliedvaluee7
                        derrorallowed7 =     Masterinstrumentslistpart3Find.derrorallowed7
                        dmax7 =     Masterinstrumentslistpart3Find.dmax7
                        dmin7 =     Masterinstrumentslistpart3Find.dmin7
                        suom8 =     Masterinstrumentslistpart3Find.suom8
                        sappliedvalue8 =     Masterinstrumentslistpart3Find.sappliedvalue8
                        fappliedvaluea8 =     Masterinstrumentslistpart3Find.fappliedvaluea8
                        fappliedvalueb8 =     Masterinstrumentslistpart3Find.fappliedvalueb8
                        fappliedvaluec8 =     Masterinstrumentslistpart3Find.fappliedvaluec8
                        fappliedvalued8 =     Masterinstrumentslistpart3Find.fappliedvalued8
                        fappliedvaluee8 =     Masterinstrumentslistpart3Find.fappliedvaluee8
                        derrorallowed8 =     Masterinstrumentslistpart3Find.derrorallowed8
                        dmax8 =     Masterinstrumentslistpart3Find.dmax8
                        dmin8 =     Masterinstrumentslistpart3Find.dmin8
                        suom9 =     Masterinstrumentslistpart3Find.suom9
                        sappliedvalue9 =     Masterinstrumentslistpart3Find.sappliedvalue9
                        fappliedvaluea9 =     Masterinstrumentslistpart3Find.fappliedvaluea9
                        fappliedvalueb9 =     Masterinstrumentslistpart3Find.fappliedvalueb9
                        fappliedvaluec9 =     Masterinstrumentslistpart3Find.fappliedvaluec9
                        fappliedvalued9 =     Masterinstrumentslistpart3Find.fappliedvalued9
                        fappliedvaluee9 =     Masterinstrumentslistpart3Find.fappliedvaluee9
                        derrorallowed9 =     Masterinstrumentslistpart3Find.derrorallowed9
                        dmax9 =     Masterinstrumentslistpart3Find.dmax9
                        dmin9 =     Masterinstrumentslistpart3Find.dmin9
                        suom10 =     Masterinstrumentslistpart3Find.suom10
                        sappliedvalue10 =     Masterinstrumentslistpart3Find.sappliedvalue10
                        fappliedvaluea10 =     Masterinstrumentslistpart3Find.fappliedvaluea10
                        fappliedvalueb10 =     Masterinstrumentslistpart3Find.fappliedvalueb10
                        fappliedvaluec10 =     Masterinstrumentslistpart3Find.fappliedvaluec10
                        fappliedvalued10 =     Masterinstrumentslistpart3Find.fappliedvalued10
                        fappliedvaluee10 =     Masterinstrumentslistpart3Find.fappliedvaluee10
                        derrorallowed10 =     Masterinstrumentslistpart3Find.derrorallowed10
                        dmax10 =     Masterinstrumentslistpart3Find.dmax10
                        dmin10 =     Masterinstrumentslistpart3Find.dmin10
                        suom11 =     Masterinstrumentslistpart3Find.suom11
                        sappliedvalue11 =     Masterinstrumentslistpart3Find.sappliedvalue11
                        fappliedvaluea11 =     Masterinstrumentslistpart3Find.fappliedvaluea11
                        fappliedvalueb11 =     Masterinstrumentslistpart3Find.fappliedvalueb11
                        fappliedvaluec11 =     Masterinstrumentslistpart3Find.fappliedvaluec11
                        fappliedvalued11 =     Masterinstrumentslistpart3Find.fappliedvalued11
                        fappliedvaluee11 =     Masterinstrumentslistpart3Find.fappliedvaluee11
                        derrorallowed11 =     Masterinstrumentslistpart3Find.derrorallowed11
                        dmax11 =     Masterinstrumentslistpart3Find.dmax11
                        dmin11 =     Masterinstrumentslistpart3Find.dmin11
                        suom12 =     Masterinstrumentslistpart3Find.suom12
                        sappliedvalue12 =     Masterinstrumentslistpart3Find.sappliedvalue12
                        fappliedvaluea12 =     Masterinstrumentslistpart3Find.fappliedvaluea12
                        fappliedvalueb12 =     Masterinstrumentslistpart3Find.fappliedvalueb12
                        fappliedvaluec12 =     Masterinstrumentslistpart3Find.fappliedvaluec12
                        fappliedvalued12 =     Masterinstrumentslistpart3Find.fappliedvalued12
                        fappliedvaluee12 =     Masterinstrumentslistpart3Find.fappliedvaluee12
                        derrorallowed12 =     Masterinstrumentslistpart3Find.derrorallowed12
                        dmax12 =     Masterinstrumentslistpart3Find.dmax12
                        dmin12 =     Masterinstrumentslistpart3Find.dmin12
                        suom13 =     Masterinstrumentslistpart3Find.suom13
                        sappliedvalue13 =     Masterinstrumentslistpart3Find.sappliedvalue13
                        fappliedvaluea13 =     Masterinstrumentslistpart3Find.fappliedvaluea13
                        fappliedvalueb13 =     Masterinstrumentslistpart3Find.fappliedvalueb13
                        fappliedvaluec13 =     Masterinstrumentslistpart3Find.fappliedvaluec13
                        fappliedvalued13 =     Masterinstrumentslistpart3Find.fappliedvalued13
                        fappliedvaluee13 =     Masterinstrumentslistpart3Find.fappliedvaluee13
                        derrorallowed13 =     Masterinstrumentslistpart3Find.derrorallowed13
                        dmax13 =     Masterinstrumentslistpart3Find.dmax13
                        dmin13 =     Masterinstrumentslistpart3Find.dmin13
                        suom14 =     Masterinstrumentslistpart3Find.suom14
                        sappliedvalue14 =     Masterinstrumentslistpart3Find.sappliedvalue14
                        fappliedvaluea14 =     Masterinstrumentslistpart3Find.fappliedvaluea14
                        fappliedvalueb14 =     Masterinstrumentslistpart3Find.fappliedvalueb14
                        fappliedvaluec14 =     Masterinstrumentslistpart3Find.fappliedvaluec14
                        fappliedvalued14 =     Masterinstrumentslistpart3Find.fappliedvalued14
                        fappliedvaluee14 =     Masterinstrumentslistpart3Find.fappliedvaluee14
                        derrorallowed14 =     Masterinstrumentslistpart3Find.derrorallowed14
                        dmax14 =     Masterinstrumentslistpart3Find.dmax14
                        dmin14 =     Masterinstrumentslistpart3Find.dmin14
                        suom15 =     Masterinstrumentslistpart3Find.suom15
                        sappliedvalue15 =     Masterinstrumentslistpart3Find.sappliedvalue15
                        fappliedvaluea15 =     Masterinstrumentslistpart3Find.fappliedvaluea15
                        fappliedvalueb15 =     Masterinstrumentslistpart3Find.fappliedvalueb15
                        fappliedvaluec15 =     Masterinstrumentslistpart3Find.fappliedvaluec15
                        fappliedvalued15 =     Masterinstrumentslistpart3Find.fappliedvalued15
                        fappliedvaluee15 =     Masterinstrumentslistpart3Find.fappliedvaluee15
                        derrorallowed15 =     Masterinstrumentslistpart3Find.derrorallowed15
                        dmax15 =     Masterinstrumentslistpart3Find.dmax15
                        dmin15 =     Masterinstrumentslistpart3Find.dmin15
                        suom16 =     Masterinstrumentslistpart3Find.suom16
                        sappliedvalue16 =     Masterinstrumentslistpart3Find.sappliedvalue16
                        fappliedvaluea16 =     Masterinstrumentslistpart3Find.fappliedvaluea16
                        fappliedvalueb16 =     Masterinstrumentslistpart3Find.fappliedvalueb16
                        fappliedvaluec16 =     Masterinstrumentslistpart3Find.fappliedvaluec16
                        fappliedvalued16 =     Masterinstrumentslistpart3Find.fappliedvalued16
                        fappliedvaluee16 =     Masterinstrumentslistpart3Find.fappliedvaluee16
                        derrorallowed16 =     Masterinstrumentslistpart3Find.derrorallowed16
                        dmax16 =     Masterinstrumentslistpart3Find.dmax16
                        dmin16 =     Masterinstrumentslistpart3Find.dmin16
                        suom17 =     Masterinstrumentslistpart3Find.suom17
                        sappliedvalue17 =     Masterinstrumentslistpart3Find.sappliedvalue17
                        fappliedvaluea17 =     Masterinstrumentslistpart3Find.fappliedvaluea17
                        fappliedvalueb17 =     Masterinstrumentslistpart3Find.fappliedvalueb17
                        fappliedvaluec17 =     Masterinstrumentslistpart3Find.fappliedvaluec17
                        fappliedvalued17 =     Masterinstrumentslistpart3Find.fappliedvalued17
                        fappliedvaluee17 =     Masterinstrumentslistpart3Find.fappliedvaluee17
                        derrorallowed17 =     Masterinstrumentslistpart3Find.derrorallowed17
                        dmax17 =     Masterinstrumentslistpart3Find.dmax17
                        dmin17 =     Masterinstrumentslistpart3Find.dmin17
                        suom18 =     Masterinstrumentslistpart3Find.suom18
                        sappliedvalue18 =     Masterinstrumentslistpart3Find.sappliedvalue18
                        fappliedvaluea18 =     Masterinstrumentslistpart3Find.fappliedvaluea18
                        fappliedvalueb18 =     Masterinstrumentslistpart3Find.fappliedvalueb18
                        fappliedvaluec18 =     Masterinstrumentslistpart3Find.fappliedvaluec18
                        fappliedvalued18 =     Masterinstrumentslistpart3Find.fappliedvalued18
                        fappliedvaluee18 =     Masterinstrumentslistpart3Find.fappliedvaluee18
                        derrorallowed18 =     Masterinstrumentslistpart3Find.derrorallowed18
                        dmax18 =     Masterinstrumentslistpart3Find.dmax18
                        dmin18 =     Masterinstrumentslistpart3Find.dmin18
                        suom19 =     Masterinstrumentslistpart3Find.suom19
                        sappliedvalue19 =     Masterinstrumentslistpart3Find.sappliedvalue19
                        fappliedvaluea19 =     Masterinstrumentslistpart3Find.fappliedvaluea19
                        fappliedvalueb19 =     Masterinstrumentslistpart3Find.fappliedvalueb19
                        fappliedvaluec19 =     Masterinstrumentslistpart3Find.fappliedvaluec19
                        fappliedvalued19 =     Masterinstrumentslistpart3Find.fappliedvalued19
                        fappliedvaluee19 =     Masterinstrumentslistpart3Find.fappliedvaluee19
                        derrorallowed19 =     Masterinstrumentslistpart3Find.derrorallowed19
                        dmax19 =     Masterinstrumentslistpart3Find.dmax19
                        dmin19 =     Masterinstrumentslistpart3Find.dmin19
                        suom20 =     Masterinstrumentslistpart3Find.suom20
                        sappliedvalue20 =     Masterinstrumentslistpart3Find.sappliedvalue20
                        fappliedvaluea20 =     Masterinstrumentslistpart3Find.fappliedvaluea20
                        fappliedvalueb20 =     Masterinstrumentslistpart3Find.fappliedvalueb20
                        fappliedvaluec20 =     Masterinstrumentslistpart3Find.fappliedvaluec20
                        fappliedvalued20 =     Masterinstrumentslistpart3Find.fappliedvalued20
                        fappliedvaluee20 =     Masterinstrumentslistpart3Find.fappliedvaluee20
                        derrorallowed20 =     Masterinstrumentslistpart3Find.derrorallowed20
                        dmax20 =     Masterinstrumentslistpart3Find.dmax20
                        dmin20 =     Masterinstrumentslistpart3Find.dmin20
                        suom21 =     Masterinstrumentslistpart3Find.suom21
                        sappliedvalue21 =     Masterinstrumentslistpart3Find.sappliedvalue21
                        fappliedvaluea21 =     Masterinstrumentslistpart3Find.fappliedvaluea21
                        fappliedvalueb21 =     Masterinstrumentslistpart3Find.fappliedvalueb21
                        fappliedvaluec21 =     Masterinstrumentslistpart3Find.fappliedvaluec21
                        fappliedvalued21 =     Masterinstrumentslistpart3Find.fappliedvalued21
                        fappliedvaluee21 =     Masterinstrumentslistpart3Find.fappliedvaluee21
                        derrorallowed21 =     Masterinstrumentslistpart3Find.derrorallowed21
                        dmax21 =     Masterinstrumentslistpart3Find.dmax21
                        dmin21 =     Masterinstrumentslistpart3Find.dmin21
                        suom22 =     Masterinstrumentslistpart3Find.suom22
                        sappliedvalue22 =     Masterinstrumentslistpart3Find.sappliedvalue22
                        fappliedvaluea22 =     Masterinstrumentslistpart3Find.fappliedvaluea22
                        fappliedvalueb22 =     Masterinstrumentslistpart3Find.fappliedvalueb22
                        fappliedvaluec22 =     Masterinstrumentslistpart3Find.fappliedvaluec22
                        fappliedvalued22 =     Masterinstrumentslistpart3Find.fappliedvalued22
                        fappliedvaluee22 =     Masterinstrumentslistpart3Find.fappliedvaluee22
                        derrorallowed22 =     Masterinstrumentslistpart3Find.derrorallowed22
                        dmax22 =     Masterinstrumentslistpart3Find.dmax22
                        dmin22 =     Masterinstrumentslistpart3Find.dmin22
                        suom23 =     Masterinstrumentslistpart3Find.suom23
                        sappliedvalue23 =     Masterinstrumentslistpart3Find.sappliedvalue23
                        fappliedvaluea23 =     Masterinstrumentslistpart3Find.fappliedvaluea23
                        fappliedvalueb23 =     Masterinstrumentslistpart3Find.fappliedvalueb23
                        fappliedvaluec23 =     Masterinstrumentslistpart3Find.fappliedvaluec23
                        fappliedvalued23 =     Masterinstrumentslistpart3Find.fappliedvalued23
                        fappliedvaluee23 =     Masterinstrumentslistpart3Find.fappliedvaluee23
                        derrorallowed23 =     Masterinstrumentslistpart3Find.derrorallowed23
                        dmax23 =     Masterinstrumentslistpart3Find.dmax23
                        dmin23 =     Masterinstrumentslistpart3Find.dmin23
                        suom24 =     Masterinstrumentslistpart3Find.suom24
                        sappliedvalue24 =     Masterinstrumentslistpart3Find.sappliedvalue24
                        fappliedvaluea24 =     Masterinstrumentslistpart3Find.fappliedvaluea24
                        fappliedvalueb24 =     Masterinstrumentslistpart3Find.fappliedvalueb24
                        fappliedvaluec24 =     Masterinstrumentslistpart3Find.fappliedvaluec24
                        fappliedvalued24 =     Masterinstrumentslistpart3Find.fappliedvalued24
                        fappliedvaluee24 =     Masterinstrumentslistpart3Find.fappliedvaluee24
                        derrorallowed24 =     Masterinstrumentslistpart3Find.derrorallowed24
                        dmax24 =     Masterinstrumentslistpart3Find.dmax24
                        dmin24 =     Masterinstrumentslistpart3Find.dmin24
                        suom25 =     Masterinstrumentslistpart3Find.suom25
                        sappliedvalue25 =     Masterinstrumentslistpart3Find.sappliedvalue25
                        fappliedvaluea25 =     Masterinstrumentslistpart3Find.fappliedvaluea25
                        fappliedvalueb25 =     Masterinstrumentslistpart3Find.fappliedvalueb25
                        fappliedvaluec25 =     Masterinstrumentslistpart3Find.fappliedvaluec25
                        fappliedvalued25 =     Masterinstrumentslistpart3Find.fappliedvalued25
                        fappliedvaluee25 =     Masterinstrumentslistpart3Find.fappliedvaluee25
                        derrorallowed25 =     Masterinstrumentslistpart3Find.derrorallowed25
                        dmax25 =     Masterinstrumentslistpart3Find.dmax25
                        dmin25 =     Masterinstrumentslistpart3Find.dmin25
                        suom26 =     Masterinstrumentslistpart3Find.suom26
                        sappliedvalue26 =     Masterinstrumentslistpart3Find.sappliedvalue26
                        fappliedvaluea26 =     Masterinstrumentslistpart3Find.fappliedvaluea26
                        fappliedvalueb26 =     Masterinstrumentslistpart3Find.fappliedvalueb26
                        fappliedvaluec26 =     Masterinstrumentslistpart3Find.fappliedvaluec26
                        fappliedvalued26 =     Masterinstrumentslistpart3Find.fappliedvalued26
                        fappliedvaluee26 =     Masterinstrumentslistpart3Find.fappliedvaluee26
                        derrorallowed26 =     Masterinstrumentslistpart3Find.derrorallowed26
                        dmax26 =     Masterinstrumentslistpart3Find.dmax26
                        dmin26 =     Masterinstrumentslistpart3Find.dmin26
                        suom27 =     Masterinstrumentslistpart3Find.suom27
                        sappliedvalue27 =     Masterinstrumentslistpart3Find.sappliedvalue27
                        fappliedvaluea27 =     Masterinstrumentslistpart3Find.fappliedvaluea27
                        fappliedvalueb27 =     Masterinstrumentslistpart3Find.fappliedvalueb27
                        fappliedvaluec27 =     Masterinstrumentslistpart3Find.fappliedvaluec27
                        fappliedvalued27 =     Masterinstrumentslistpart3Find.fappliedvalued27
                        fappliedvaluee27 =     Masterinstrumentslistpart3Find.fappliedvaluee27
                        derrorallowed27 =     Masterinstrumentslistpart3Find.derrorallowed27
                        dmax27 =     Masterinstrumentslistpart3Find.dmax27
                        dmin27 =     Masterinstrumentslistpart3Find.dmin27
                        suom28 =     Masterinstrumentslistpart3Find.suom28
                        sappliedvalue28 =     Masterinstrumentslistpart3Find.sappliedvalue28
                        fappliedvaluea28 =     Masterinstrumentslistpart3Find.fappliedvaluea28
                        fappliedvalueb28 =     Masterinstrumentslistpart3Find.fappliedvalueb28
                        fappliedvaluec28 =     Masterinstrumentslistpart3Find.fappliedvaluec28
                        fappliedvalued28 =     Masterinstrumentslistpart3Find.fappliedvalued28
                        fappliedvaluee28 =     Masterinstrumentslistpart3Find.fappliedvaluee28
                        derrorallowed28 =     Masterinstrumentslistpart3Find.derrorallowed28
                        dmax28 =     Masterinstrumentslistpart3Find.dmax28
                        dmin28 =     Masterinstrumentslistpart3Find.dmin28
                        suom29 =     Masterinstrumentslistpart3Find.suom29
                        sappliedvalue29 =     Masterinstrumentslistpart3Find.sappliedvalue29
                        fappliedvaluea29 =     Masterinstrumentslistpart3Find.fappliedvaluea29
                        fappliedvalueb29 =     Masterinstrumentslistpart3Find.fappliedvalueb29
                        fappliedvaluec29 =     Masterinstrumentslistpart3Find.fappliedvaluec29
                        fappliedvalued29 =     Masterinstrumentslistpart3Find.fappliedvalued29
                        fappliedvaluee29 =     Masterinstrumentslistpart3Find.fappliedvaluee29
                        derrorallowed29 =     Masterinstrumentslistpart3Find.derrorallowed29
                        dmax29 =     Masterinstrumentslistpart3Find.dmax29
                        dmin29 =     Masterinstrumentslistpart3Find.dmin29
                        suom30 =     Masterinstrumentslistpart3Find.suom30
                        sappliedvalue30 =     Masterinstrumentslistpart3Find.sappliedvalue30
                        fappliedvaluea30 =     Masterinstrumentslistpart3Find.fappliedvaluea30
                        fappliedvalueb30 =     Masterinstrumentslistpart3Find.fappliedvalueb30
                        fappliedvaluec30 =     Masterinstrumentslistpart3Find.fappliedvaluec30
                        fappliedvalued30 =     Masterinstrumentslistpart3Find.fappliedvalued30
                        fappliedvaluee30 =     Masterinstrumentslistpart3Find.fappliedvaluee30
                        derrorallowed30 =     Masterinstrumentslistpart3Find.derrorallowed30
                        dmax30 =     Masterinstrumentslistpart3Find.dmax30
                        dmin30 =     Masterinstrumentslistpart3Find.dmin30




            Thistorymainpart1Save = Thistorymainpart1(lhistoryid=lhistorymainid, linstrumentid = linstrumentid )
            Thistorymainpart1Save.save() 

            lid1 =0
            lid1 = Thistorymainpart1Save.lid



            Thistorymainpart1SaveUpdate =  Thistorymainpart1.objects.get(lid =lid1) 
        
            Thistorymainpart1SaveUpdate.lmasterinstrumentid1 = lmasterinstrumentid1
            Thistorymainpart1SaveUpdate.smasterinstrumentid1 = smasterinstrumentid1
            Thistorymainpart1SaveUpdate.smasterdescription1 = smasterdescription1
            Thistorymainpart1SaveUpdate.slastcalibrationdate1 = slastcalibrationdate1
            Thistorymainpart1SaveUpdate.snextcalibrationdate1 = snextcalibrationdate1
            Thistorymainpart1SaveUpdate.lmasterinstrumentid2 = lmasterinstrumentid2
            Thistorymainpart1SaveUpdate.smasterinstrumentid2 = smasterinstrumentid2
            Thistorymainpart1SaveUpdate.smasterdescription2 = smasterdescription2
            Thistorymainpart1SaveUpdate.slastcalibrationdate2 = slastcalibrationdate2
            Thistorymainpart1SaveUpdate.snextcalibrationdate2 = snextcalibrationdate2
            Thistorymainpart1SaveUpdate.lmasterinstrumentid3 = lmasterinstrumentid3
            Thistorymainpart1SaveUpdate.smasterinstrumentid3 = smasterinstrumentid3
            Thistorymainpart1SaveUpdate.smasterdescription3 = smasterdescription3
            Thistorymainpart1SaveUpdate.slastcalibrationdate3 = slastcalibrationdate3
            Thistorymainpart1SaveUpdate.snextcalibrationdate3 = snextcalibrationdate3
            Thistorymainpart1SaveUpdate.lmasterinstrumentid4 = lmasterinstrumentid4
            Thistorymainpart1SaveUpdate.smasterinstrumentid4 = smasterinstrumentid4
            Thistorymainpart1SaveUpdate.smasterdescription4 = smasterdescription4
            Thistorymainpart1SaveUpdate.slastcalibrationdate4 = slastcalibrationdate4
            Thistorymainpart1SaveUpdate.snextcalibrationdate4 = snextcalibrationdate4
            Thistorymainpart1SaveUpdate.lmasterinstrumentid5 = lmasterinstrumentid5
            Thistorymainpart1SaveUpdate.smasterinstrumentid5 = smasterinstrumentid5
            Thistorymainpart1SaveUpdate.smasterdescription5 = smasterdescription5
            Thistorymainpart1SaveUpdate.slastcalibrationdate5 = slastcalibrationdate5
            Thistorymainpart1SaveUpdate.snextcalibrationdate5 = snextcalibrationdate5
            Thistorymainpart1SaveUpdate.stypeoffile1 = stypeoffile1
            Thistorymainpart1SaveUpdate.sfile1 = sfile1
            Thistorymainpart1SaveUpdate.stypeoffile2 = stypeoffile2
            Thistorymainpart1SaveUpdate.sfile2 = sfile2
            Thistorymainpart1SaveUpdate.stypeoffile3 = stypeoffile3
            Thistorymainpart1SaveUpdate.sfile3 = sfile3
            Thistorymainpart1SaveUpdate.stypeoffile4 = stypeoffile4
            Thistorymainpart1SaveUpdate.sfile4 = sfile4
            Thistorymainpart1SaveUpdate.stypeoffile5 = stypeoffile5
            Thistorymainpart1SaveUpdate.sfile5 = sfile5
            Thistorymainpart1SaveUpdate.suom1 = suom1
            Thistorymainpart1SaveUpdate.sappliedvalue1 = sappliedvalue1
            Thistorymainpart1SaveUpdate.fappliedvaluea1 = fappliedvaluea1
            Thistorymainpart1SaveUpdate.fappliedvalueb1 = fappliedvalueb1
            Thistorymainpart1SaveUpdate.fappliedvaluec1 = fappliedvaluec1
            Thistorymainpart1SaveUpdate.fappliedvalued1 = fappliedvalued1
            Thistorymainpart1SaveUpdate.fappliedvaluee1 = fappliedvaluee1
            Thistorymainpart1SaveUpdate.derrorallowed1 = derrorallowed1
            Thistorymainpart1SaveUpdate.dmax1 = dmax1
            Thistorymainpart1SaveUpdate.dmin1 = dmin1
            Thistorymainpart1SaveUpdate.suom2 = suom2
            Thistorymainpart1SaveUpdate.sappliedvalue2 = sappliedvalue2
            Thistorymainpart1SaveUpdate.fappliedvaluea2 = fappliedvaluea2
            Thistorymainpart1SaveUpdate.fappliedvalueb2 = fappliedvalueb2
            Thistorymainpart1SaveUpdate.fappliedvaluec2 = fappliedvaluec2
            Thistorymainpart1SaveUpdate.fappliedvalued2 = fappliedvalued2
            Thistorymainpart1SaveUpdate.fappliedvaluee2 = fappliedvaluee2
            Thistorymainpart1SaveUpdate.derrorallowed2 = derrorallowed2
            Thistorymainpart1SaveUpdate.dmax2 = dmax2
            Thistorymainpart1SaveUpdate.dmin2 = dmin2
            Thistorymainpart1SaveUpdate.suom3 = suom3
            Thistorymainpart1SaveUpdate.sappliedvalue3 = sappliedvalue3
            Thistorymainpart1SaveUpdate.fappliedvaluea3 = fappliedvaluea3
            Thistorymainpart1SaveUpdate.fappliedvalueb3 = fappliedvalueb3
            Thistorymainpart1SaveUpdate.fappliedvaluec3 = fappliedvaluec3
            Thistorymainpart1SaveUpdate.fappliedvalued3 = fappliedvalued3
            Thistorymainpart1SaveUpdate.fappliedvaluee3 = fappliedvaluee3
            Thistorymainpart1SaveUpdate.derrorallowed3 = derrorallowed3
            Thistorymainpart1SaveUpdate.dmax3 = dmax3
            Thistorymainpart1SaveUpdate.dmin3 = dmin3
            Thistorymainpart1SaveUpdate.suom4 = suom4
            Thistorymainpart1SaveUpdate.sappliedvalue4 = sappliedvalue4
            Thistorymainpart1SaveUpdate.fappliedvaluea4 = fappliedvaluea4
            Thistorymainpart1SaveUpdate.fappliedvalueb4 = fappliedvalueb4
            Thistorymainpart1SaveUpdate.fappliedvaluec4 = fappliedvaluec4
            Thistorymainpart1SaveUpdate.fappliedvalued4 = fappliedvalued4
            Thistorymainpart1SaveUpdate.fappliedvaluee4 = fappliedvaluee4
            Thistorymainpart1SaveUpdate.derrorallowed4 = derrorallowed4
            Thistorymainpart1SaveUpdate.dmax4 = dmax4
            Thistorymainpart1SaveUpdate.dmin4 = dmin4
            Thistorymainpart1SaveUpdate.suom5 = suom5
            Thistorymainpart1SaveUpdate.sappliedvalue5 = sappliedvalue5
            Thistorymainpart1SaveUpdate.fappliedvaluea5 = fappliedvaluea5
            Thistorymainpart1SaveUpdate.fappliedvalueb5 = fappliedvalueb5
            Thistorymainpart1SaveUpdate.fappliedvaluec5 = fappliedvaluec5
            Thistorymainpart1SaveUpdate.fappliedvalued5 = fappliedvalued5
            Thistorymainpart1SaveUpdate.fappliedvaluee5 = fappliedvaluee5
            Thistorymainpart1SaveUpdate.derrorallowed5 = derrorallowed5
            Thistorymainpart1SaveUpdate.dmax5 = dmax5
            Thistorymainpart1SaveUpdate.dmin5 = dmin5
            Thistorymainpart1SaveUpdate.suom6 = suom6
            Thistorymainpart1SaveUpdate.sappliedvalue6 = sappliedvalue6
            Thistorymainpart1SaveUpdate.fappliedvaluea6 = fappliedvaluea6
            Thistorymainpart1SaveUpdate.fappliedvalueb6 = fappliedvalueb6
            Thistorymainpart1SaveUpdate.fappliedvaluec6 = fappliedvaluec6
            Thistorymainpart1SaveUpdate.fappliedvalued6 = fappliedvalued6
            Thistorymainpart1SaveUpdate.fappliedvaluee6 = fappliedvaluee6
            Thistorymainpart1SaveUpdate.derrorallowed6 = derrorallowed6
            Thistorymainpart1SaveUpdate.dmax6 = dmax6
            Thistorymainpart1SaveUpdate.dmin6 = dmin6
            Thistorymainpart1SaveUpdate.suom7 = suom7
            Thistorymainpart1SaveUpdate.sappliedvalue7 = sappliedvalue7
            Thistorymainpart1SaveUpdate.fappliedvaluea7 = fappliedvaluea7
            Thistorymainpart1SaveUpdate.fappliedvalueb7 = fappliedvalueb7
            Thistorymainpart1SaveUpdate.fappliedvaluec7 = fappliedvaluec7
            Thistorymainpart1SaveUpdate.fappliedvalued7 = fappliedvalued7
            Thistorymainpart1SaveUpdate.fappliedvaluee7 = fappliedvaluee7
            Thistorymainpart1SaveUpdate.derrorallowed7 = derrorallowed7
            Thistorymainpart1SaveUpdate.dmax7 = dmax7
            Thistorymainpart1SaveUpdate.dmin7 = dmin7
            Thistorymainpart1SaveUpdate.suom8 = suom8
            Thistorymainpart1SaveUpdate.sappliedvalue8 = sappliedvalue8
            Thistorymainpart1SaveUpdate.fappliedvaluea8 = fappliedvaluea8
            Thistorymainpart1SaveUpdate.fappliedvalueb8 = fappliedvalueb8
            Thistorymainpart1SaveUpdate.fappliedvaluec8 = fappliedvaluec8
            Thistorymainpart1SaveUpdate.fappliedvalued8 = fappliedvalued8
            Thistorymainpart1SaveUpdate.fappliedvaluee8 = fappliedvaluee8
            Thistorymainpart1SaveUpdate.derrorallowed8 = derrorallowed8
            Thistorymainpart1SaveUpdate.dmax8 = dmax8
            Thistorymainpart1SaveUpdate.dmin8 = dmin8
            Thistorymainpart1SaveUpdate.suom9 = suom9
            Thistorymainpart1SaveUpdate.sappliedvalue9 = sappliedvalue9
            Thistorymainpart1SaveUpdate.fappliedvaluea9 = fappliedvaluea9
            Thistorymainpart1SaveUpdate.fappliedvalueb9 = fappliedvalueb9
            Thistorymainpart1SaveUpdate.fappliedvaluec9 = fappliedvaluec9
            Thistorymainpart1SaveUpdate.fappliedvalued9 = fappliedvalued9
            Thistorymainpart1SaveUpdate.fappliedvaluee9 = fappliedvaluee9
            Thistorymainpart1SaveUpdate.derrorallowed9 = derrorallowed9
            Thistorymainpart1SaveUpdate.dmax9 = dmax9
            Thistorymainpart1SaveUpdate.dmin9 = dmin9
            Thistorymainpart1SaveUpdate.suom10 = suom10
            Thistorymainpart1SaveUpdate.sappliedvalue10 = sappliedvalue10
            Thistorymainpart1SaveUpdate.fappliedvaluea10 = fappliedvaluea10
            Thistorymainpart1SaveUpdate.fappliedvalueb10 = fappliedvalueb10
            Thistorymainpart1SaveUpdate.fappliedvaluec10 = fappliedvaluec10
            Thistorymainpart1SaveUpdate.fappliedvalued10 = fappliedvalued10
            Thistorymainpart1SaveUpdate.fappliedvaluee10 = fappliedvaluee10
            Thistorymainpart1SaveUpdate.derrorallowed10 = derrorallowed10
            Thistorymainpart1SaveUpdate.dmax10 = dmax10
            Thistorymainpart1SaveUpdate.dmin10 = dmin10
            Thistorymainpart1SaveUpdate.suom11 = suom11
            Thistorymainpart1SaveUpdate.sappliedvalue11 = sappliedvalue11
            Thistorymainpart1SaveUpdate.fappliedvaluea11 = fappliedvaluea11
            Thistorymainpart1SaveUpdate.fappliedvalueb11 = fappliedvalueb11
            Thistorymainpart1SaveUpdate.fappliedvaluec11 = fappliedvaluec11
            Thistorymainpart1SaveUpdate.fappliedvalued11 = fappliedvalued11
            Thistorymainpart1SaveUpdate.fappliedvaluee11 = fappliedvaluee11
            Thistorymainpart1SaveUpdate.derrorallowed11 = derrorallowed11
            Thistorymainpart1SaveUpdate.dmax11 = dmax11
            Thistorymainpart1SaveUpdate.dmin11 = dmin11
            Thistorymainpart1SaveUpdate.suom12 = suom12
            Thistorymainpart1SaveUpdate.sappliedvalue12 = sappliedvalue12
            Thistorymainpart1SaveUpdate.fappliedvaluea12 = fappliedvaluea12
            Thistorymainpart1SaveUpdate.fappliedvalueb12 = fappliedvalueb12
            Thistorymainpart1SaveUpdate.fappliedvaluec12 = fappliedvaluec12
            Thistorymainpart1SaveUpdate.fappliedvalued12 = fappliedvalued12
            Thistorymainpart1SaveUpdate.fappliedvaluee12 = fappliedvaluee12
            Thistorymainpart1SaveUpdate.derrorallowed12 = derrorallowed12
            Thistorymainpart1SaveUpdate.dmax12 = dmax12
            Thistorymainpart1SaveUpdate.dmin12 = dmin12
            Thistorymainpart1SaveUpdate.suom13 = suom13
            Thistorymainpart1SaveUpdate.sappliedvalue13 = sappliedvalue13
            Thistorymainpart1SaveUpdate.fappliedvaluea13 = fappliedvaluea13
            Thistorymainpart1SaveUpdate.fappliedvalueb13 = fappliedvalueb13
            Thistorymainpart1SaveUpdate.fappliedvaluec13 = fappliedvaluec13
            Thistorymainpart1SaveUpdate.fappliedvalued13 = fappliedvalued13
            Thistorymainpart1SaveUpdate.fappliedvaluee13 = fappliedvaluee13
            Thistorymainpart1SaveUpdate.derrorallowed13 = derrorallowed13
            Thistorymainpart1SaveUpdate.dmax13 = dmax13
            Thistorymainpart1SaveUpdate.dmin13 = dmin13
            Thistorymainpart1SaveUpdate.suom14 = suom14
            Thistorymainpart1SaveUpdate.sappliedvalue14 = sappliedvalue14
            Thistorymainpart1SaveUpdate.fappliedvaluea14 = fappliedvaluea14
            Thistorymainpart1SaveUpdate.fappliedvalueb14 = fappliedvalueb14
            Thistorymainpart1SaveUpdate.fappliedvaluec14 = fappliedvaluec14
            Thistorymainpart1SaveUpdate.fappliedvalued14 = fappliedvalued14
            Thistorymainpart1SaveUpdate.fappliedvaluee14 = fappliedvaluee14
            Thistorymainpart1SaveUpdate.derrorallowed14 = derrorallowed14
            Thistorymainpart1SaveUpdate.dmax14 = dmax14
            Thistorymainpart1SaveUpdate.dmin14 = dmin14
            Thistorymainpart1SaveUpdate.suom15 = suom15
            Thistorymainpart1SaveUpdate.sappliedvalue15 = sappliedvalue15
            Thistorymainpart1SaveUpdate.fappliedvaluea15 = fappliedvaluea15
            Thistorymainpart1SaveUpdate.fappliedvalueb15 = fappliedvalueb15
            Thistorymainpart1SaveUpdate.fappliedvaluec15 = fappliedvaluec15
            Thistorymainpart1SaveUpdate.fappliedvalued15 = fappliedvalued15
            Thistorymainpart1SaveUpdate.fappliedvaluee15 = fappliedvaluee15
            Thistorymainpart1SaveUpdate.derrorallowed15 = derrorallowed15
            Thistorymainpart1SaveUpdate.dmax15 = dmax15
            Thistorymainpart1SaveUpdate.dmin15 = dmin15
            Thistorymainpart1SaveUpdate.suom16 = suom16
            Thistorymainpart1SaveUpdate.sappliedvalue16 = sappliedvalue16
            Thistorymainpart1SaveUpdate.fappliedvaluea16 = fappliedvaluea16
            Thistorymainpart1SaveUpdate.fappliedvalueb16 = fappliedvalueb16
            Thistorymainpart1SaveUpdate.fappliedvaluec16 = fappliedvaluec16
            Thistorymainpart1SaveUpdate.fappliedvalued16 = fappliedvalued16
            Thistorymainpart1SaveUpdate.fappliedvaluee16 = fappliedvaluee16
            Thistorymainpart1SaveUpdate.derrorallowed16 = derrorallowed16
            Thistorymainpart1SaveUpdate.dmax16 = dmax16
            Thistorymainpart1SaveUpdate.dmin16 = dmin16
            Thistorymainpart1SaveUpdate.suom17 = suom17
            Thistorymainpart1SaveUpdate.sappliedvalue17 = sappliedvalue17
            Thistorymainpart1SaveUpdate.fappliedvaluea17 = fappliedvaluea17
            Thistorymainpart1SaveUpdate.fappliedvalueb17 = fappliedvalueb17
            Thistorymainpart1SaveUpdate.fappliedvaluec17 = fappliedvaluec17
            Thistorymainpart1SaveUpdate.fappliedvalued17 = fappliedvalued17
            Thistorymainpart1SaveUpdate.fappliedvaluee17 = fappliedvaluee17
            Thistorymainpart1SaveUpdate.derrorallowed17 = derrorallowed17
            Thistorymainpart1SaveUpdate.dmax17 = dmax17
            Thistorymainpart1SaveUpdate.dmin17 = dmin17
            Thistorymainpart1SaveUpdate.suom18 = suom18
            Thistorymainpart1SaveUpdate.sappliedvalue18 = sappliedvalue18
            Thistorymainpart1SaveUpdate.fappliedvaluea18 = fappliedvaluea18
            Thistorymainpart1SaveUpdate.fappliedvalueb18 = fappliedvalueb18
            Thistorymainpart1SaveUpdate.fappliedvaluec18 = fappliedvaluec18
            Thistorymainpart1SaveUpdate.fappliedvalued18 = fappliedvalued18
            Thistorymainpart1SaveUpdate.fappliedvaluee18 = fappliedvaluee18
            Thistorymainpart1SaveUpdate.derrorallowed18 = derrorallowed18
            Thistorymainpart1SaveUpdate.dmax18 = dmax18
            Thistorymainpart1SaveUpdate.dmin18 = dmin18
            Thistorymainpart1SaveUpdate.suom19 = suom19
            Thistorymainpart1SaveUpdate.sappliedvalue19 = sappliedvalue19
            Thistorymainpart1SaveUpdate.fappliedvaluea19 = fappliedvaluea19
            Thistorymainpart1SaveUpdate.fappliedvalueb19 = fappliedvalueb19
            Thistorymainpart1SaveUpdate.fappliedvaluec19 = fappliedvaluec19
            Thistorymainpart1SaveUpdate.fappliedvalued19 = fappliedvalued19
            Thistorymainpart1SaveUpdate.fappliedvaluee19 = fappliedvaluee19
            Thistorymainpart1SaveUpdate.derrorallowed19 = derrorallowed19
            Thistorymainpart1SaveUpdate.dmax19 = dmax19
            Thistorymainpart1SaveUpdate.dmin19 = dmin19
            Thistorymainpart1SaveUpdate.suom20 = suom20
            Thistorymainpart1SaveUpdate.sappliedvalue20 = sappliedvalue20
            Thistorymainpart1SaveUpdate.fappliedvaluea20 = fappliedvaluea20
            Thistorymainpart1SaveUpdate.fappliedvalueb20 = fappliedvalueb20
            Thistorymainpart1SaveUpdate.fappliedvaluec20 = fappliedvaluec20
            Thistorymainpart1SaveUpdate.fappliedvalued20 = fappliedvalued20
            Thistorymainpart1SaveUpdate.fappliedvaluee20 = fappliedvaluee20
            Thistorymainpart1SaveUpdate.derrorallowed20 = derrorallowed20
            Thistorymainpart1SaveUpdate.dmax20 = dmax20
            Thistorymainpart1SaveUpdate.dmin20 = dmin20
            Thistorymainpart1SaveUpdate.suom21 = suom21
            Thistorymainpart1SaveUpdate.sappliedvalue21 = sappliedvalue21
            Thistorymainpart1SaveUpdate.fappliedvaluea21 = fappliedvaluea21
            Thistorymainpart1SaveUpdate.fappliedvalueb21 = fappliedvalueb21
            Thistorymainpart1SaveUpdate.fappliedvaluec21 = fappliedvaluec21
            Thistorymainpart1SaveUpdate.fappliedvalued21 = fappliedvalued21
            Thistorymainpart1SaveUpdate.fappliedvaluee21 = fappliedvaluee21
            Thistorymainpart1SaveUpdate.derrorallowed21 = derrorallowed21
            Thistorymainpart1SaveUpdate.dmax21 = dmax21
            Thistorymainpart1SaveUpdate.dmin21 = dmin21
            Thistorymainpart1SaveUpdate.suom22 = suom22
            Thistorymainpart1SaveUpdate.sappliedvalue22 = sappliedvalue22
            Thistorymainpart1SaveUpdate.fappliedvaluea22 = fappliedvaluea22
            Thistorymainpart1SaveUpdate.fappliedvalueb22 = fappliedvalueb22
            Thistorymainpart1SaveUpdate.fappliedvaluec22 = fappliedvaluec22
            Thistorymainpart1SaveUpdate.fappliedvalued22 = fappliedvalued22
            Thistorymainpart1SaveUpdate.fappliedvaluee22 = fappliedvaluee22
            Thistorymainpart1SaveUpdate.derrorallowed22 = derrorallowed22
            Thistorymainpart1SaveUpdate.dmax22 = dmax22
            Thistorymainpart1SaveUpdate.dmin22 = dmin22
            Thistorymainpart1SaveUpdate.suom23 = suom23
            Thistorymainpart1SaveUpdate.sappliedvalue23 = sappliedvalue23
            Thistorymainpart1SaveUpdate.fappliedvaluea23 = fappliedvaluea23
            Thistorymainpart1SaveUpdate.fappliedvalueb23 = fappliedvalueb23
            Thistorymainpart1SaveUpdate.fappliedvaluec23 = fappliedvaluec23
            Thistorymainpart1SaveUpdate.fappliedvalued23 = fappliedvalued23
            Thistorymainpart1SaveUpdate.fappliedvaluee23 = fappliedvaluee23
            Thistorymainpart1SaveUpdate.derrorallowed23 = derrorallowed23
            Thistorymainpart1SaveUpdate.dmax23 = dmax23
            Thistorymainpart1SaveUpdate.dmin23 = dmin23
            Thistorymainpart1SaveUpdate.suom24 = suom24
            Thistorymainpart1SaveUpdate.sappliedvalue24 = sappliedvalue24
            Thistorymainpart1SaveUpdate.fappliedvaluea24 = fappliedvaluea24
            Thistorymainpart1SaveUpdate.fappliedvalueb24 = fappliedvalueb24
            Thistorymainpart1SaveUpdate.fappliedvaluec24 = fappliedvaluec24
            Thistorymainpart1SaveUpdate.fappliedvalued24 = fappliedvalued24
            Thistorymainpart1SaveUpdate.fappliedvaluee24 = fappliedvaluee24
            Thistorymainpart1SaveUpdate.derrorallowed24 = derrorallowed24
            Thistorymainpart1SaveUpdate.dmax24 = dmax24
            Thistorymainpart1SaveUpdate.dmin24 = dmin24
            Thistorymainpart1SaveUpdate.suom25 = suom25
            Thistorymainpart1SaveUpdate.sappliedvalue25 = sappliedvalue25
            Thistorymainpart1SaveUpdate.fappliedvaluea25 = fappliedvaluea25
            Thistorymainpart1SaveUpdate.fappliedvalueb25 = fappliedvalueb25
            Thistorymainpart1SaveUpdate.fappliedvaluec25 = fappliedvaluec25
            Thistorymainpart1SaveUpdate.fappliedvalued25 = fappliedvalued25
            Thistorymainpart1SaveUpdate.fappliedvaluee25 = fappliedvaluee25
            Thistorymainpart1SaveUpdate.derrorallowed25 = derrorallowed25
            Thistorymainpart1SaveUpdate.dmax25 = dmax25
            Thistorymainpart1SaveUpdate.dmin25 = dmin25
            Thistorymainpart1SaveUpdate.suom26 = suom26
            Thistorymainpart1SaveUpdate.sappliedvalue26 = sappliedvalue26
            Thistorymainpart1SaveUpdate.fappliedvaluea26 = fappliedvaluea26
            Thistorymainpart1SaveUpdate.fappliedvalueb26 = fappliedvalueb26
            Thistorymainpart1SaveUpdate.fappliedvaluec26 = fappliedvaluec26
            Thistorymainpart1SaveUpdate.fappliedvalued26 = fappliedvalued26
            Thistorymainpart1SaveUpdate.fappliedvaluee26 = fappliedvaluee26
            Thistorymainpart1SaveUpdate.derrorallowed26 = derrorallowed26
            Thistorymainpart1SaveUpdate.dmax26 = dmax26
            Thistorymainpart1SaveUpdate.dmin26 = dmin26
            Thistorymainpart1SaveUpdate.suom27 = suom27
            Thistorymainpart1SaveUpdate.sappliedvalue27 = sappliedvalue27
            Thistorymainpart1SaveUpdate.fappliedvaluea27 = fappliedvaluea27
            Thistorymainpart1SaveUpdate.fappliedvalueb27 = fappliedvalueb27
            Thistorymainpart1SaveUpdate.fappliedvaluec27 = fappliedvaluec27
            Thistorymainpart1SaveUpdate.fappliedvalued27 = fappliedvalued27
            Thistorymainpart1SaveUpdate.fappliedvaluee27 = fappliedvaluee27
            Thistorymainpart1SaveUpdate.derrorallowed27 = derrorallowed27
            Thistorymainpart1SaveUpdate.dmax27 = dmax27
            Thistorymainpart1SaveUpdate.dmin27 = dmin27
            Thistorymainpart1SaveUpdate.suom28 = suom28
            Thistorymainpart1SaveUpdate.sappliedvalue28 = sappliedvalue28
            Thistorymainpart1SaveUpdate.fappliedvaluea28 = fappliedvaluea28
            Thistorymainpart1SaveUpdate.fappliedvalueb28 = fappliedvalueb28
            Thistorymainpart1SaveUpdate.fappliedvaluec28 = fappliedvaluec28
            Thistorymainpart1SaveUpdate.fappliedvalued28 = fappliedvalued28
            Thistorymainpart1SaveUpdate.fappliedvaluee28 = fappliedvaluee28
            Thistorymainpart1SaveUpdate.derrorallowed28 = derrorallowed28
            Thistorymainpart1SaveUpdate.dmax28 = dmax28
            Thistorymainpart1SaveUpdate.dmin28 = dmin28
            Thistorymainpart1SaveUpdate.suom29 = suom29
            Thistorymainpart1SaveUpdate.sappliedvalue29 = sappliedvalue29
            Thistorymainpart1SaveUpdate.fappliedvaluea29 = fappliedvaluea29
            Thistorymainpart1SaveUpdate.fappliedvalueb29 = fappliedvalueb29
            Thistorymainpart1SaveUpdate.fappliedvaluec29 = fappliedvaluec29
            Thistorymainpart1SaveUpdate.fappliedvalued29 = fappliedvalued29
            Thistorymainpart1SaveUpdate.fappliedvaluee29 = fappliedvaluee29
            Thistorymainpart1SaveUpdate.derrorallowed29 = derrorallowed29
            Thistorymainpart1SaveUpdate.dmax29 = dmax29
            Thistorymainpart1SaveUpdate.dmin29 = dmin29
            Thistorymainpart1SaveUpdate.suom30 = suom30
            Thistorymainpart1SaveUpdate.sappliedvalue30 = sappliedvalue30
            Thistorymainpart1SaveUpdate.fappliedvaluea30 = fappliedvaluea30
            Thistorymainpart1SaveUpdate.fappliedvalueb30 = fappliedvalueb30
            Thistorymainpart1SaveUpdate.fappliedvaluec30 = fappliedvaluec30
            Thistorymainpart1SaveUpdate.fappliedvalued30 = fappliedvalued30
            Thistorymainpart1SaveUpdate.fappliedvaluee30 = fappliedvaluee30
            Thistorymainpart1SaveUpdate.derrorallowed30 = derrorallowed30
            Thistorymainpart1SaveUpdate.dmax30 = dmax30
            Thistorymainpart1SaveUpdate.dmin30 = dmin30
            Thistorymainpart1SaveUpdate.lhistorytraceid1 = lhistorytraceid1
            Thistorymainpart1SaveUpdate.lhistorytraceid2 = lhistorytraceid2
            Thistorymainpart1SaveUpdate.lhistorytraceid3 = lhistorytraceid3
            Thistorymainpart1SaveUpdate.lhistorytraceid4 = lhistorytraceid4
            Thistorymainpart1SaveUpdate.lhistorytraceid5 = lhistorytraceid5
            Thistorymainpart1SaveUpdate.shistorytraceid1 = shistorytraceid1
            Thistorymainpart1SaveUpdate.shistorytraceid2 = shistorytraceid2
            Thistorymainpart1SaveUpdate.shistorytraceid3 = shistorytraceid3
            Thistorymainpart1SaveUpdate.shistorytraceid4 = shistorytraceid4
            Thistorymainpart1SaveUpdate.shistorytraceid5 = shistorytraceid5


            Thistorymainpart1SaveUpdate.save() 












            factualvaluea1 = 0
            factualvalueaa1 = 0
            factualvalueb1 = 0
            factualvaluebb1 = 0
            factualvaluec1 = 0
            factualvaluecc1 = 0
            factualvalued1 = 0
            factualvaluedd1 = 0
            factualvaluee1 = 0
            factualvalueee1 = 0
            sbeforeresult1 = ""
            bbeforeok1 = 0
            safterresult1 = ""
            bafterok1 = 0
            factualberror1 = 0
            factualaerror1 = 0
            factualvaluea2 = 0
            factualvalueaa2 = 0
            factualvalueb2 = 0
            factualvaluebb2 = 0
            factualvaluec2 = 0
            factualvaluecc2 = 0
            factualvalued2 = 0
            factualvaluedd2 = 0
            factualvaluee2 = 0
            factualvalueee2 = 0
            sbeforeresult2 = ""
            bbeforeok2 = 0
            safterresult2 = ""
            bafterok2 = 0
            factualberror2 = 0
            factualaerror2 = 0
            factualvaluea3 = 0
            factualvalueaa3 = 0
            factualvalueb3 = 0
            factualvaluebb3 = 0
            factualvaluec3 = 0
            factualvaluecc3 = 0
            factualvalued3 = 0
            factualvaluedd3 = 0
            factualvaluee3 = 0
            factualvalueee3 = 0
            sbeforeresult3 = ""
            bbeforeok3 = 0
            safterresult3 = ""
            bafterok3 = 0
            factualberror3 = 0
            factualaerror3 = 0
            factualvaluea4 = 0
            factualvalueaa4 = 0
            factualvalueb4 = 0
            factualvaluebb4 = 0
            factualvaluec4 = 0
            factualvaluecc4 = 0
            factualvalued4 = 0
            factualvaluedd4 = 0
            factualvaluee4 = 0
            factualvalueee4 = 0
            sbeforeresult4 = ""
            bbeforeok4 = 0
            safterresult4 = ""
            bafterok4 = 0
            factualberror4 = 0
            factualaerror4 = 0
            factualvaluea5 = 0
            factualvalueaa5 = 0
            factualvalueb5 = 0
            factualvaluebb5 = 0
            factualvaluec5 = 0
            factualvaluecc5 = 0
            factualvalued5 = 0
            factualvaluedd5 = 0
            factualvaluee5 = 0
            factualvalueee5 = 0
            sbeforeresult5 = ""
            bbeforeok5 = 0
            safterresult5 = ""
            bafterok5 = 0
            factualberror5 = 0
            factualaerror5 = 0
            factualvaluea6 = 0
            factualvalueaa6 = 0
            factualvalueb6 = 0
            factualvaluebb6 = 0
            factualvaluec6 = 0
            factualvaluecc6 = 0
            factualvalued6 = 0
            factualvaluedd6 = 0
            factualvaluee6 = 0
            factualvalueee6 = 0
            sbeforeresult6 = ""
            bbeforeok6 = 0
            safterresult6 = ""
            bafterok6 = 0
            factualberror6 = 0
            factualaerror6 = 0
            factualvaluea7 = 0
            factualvalueaa7 = 0
            factualvalueb7 = 0
            factualvaluebb7 = 0
            factualvaluec7 = 0
            factualvaluecc7 = 0
            factualvalued7 = 0
            factualvaluedd7 = 0
            factualvaluee7 = 0
            factualvalueee7 = 0
            sbeforeresult7 = ""
            bbeforeok7 = 0
            safterresult7 = ""
            bafterok7 = 0
            factualberror7 = 0
            factualaerror7 = 0
            factualvaluea8 = 0
            factualvalueaa8 = 0
            factualvalueb8 = 0
            factualvaluebb8 = 0
            factualvaluec8 = 0
            factualvaluecc8 = 0
            factualvalued8 = 0
            factualvaluedd8 = 0
            factualvaluee8 = 0
            factualvalueee8 = 0
            sbeforeresult8 = ""
            bbeforeok8 = 0
            safterresult8 = ""
            bafterok8 = 0
            factualberror8 = 0
            factualaerror8 = 0
            factualvaluea9 = 0
            factualvalueaa9 = 0
            factualvalueb9 = 0
            factualvaluebb9 = 0
            factualvaluec9 = 0
            factualvaluecc9 = 0
            factualvalued9 = 0
            factualvaluedd9 = 0
            factualvaluee9 = 0
            factualvalueee9 = 0
            sbeforeresult9 = ""
            bbeforeok9 = 0
            safterresult9 = ""
            bafterok9 = 0
            factualberror9 = 0
            factualaerror9 = 0
            factualvaluea10 = 0
            factualvalueaa10 = 0
            factualvalueb10 = 0
            factualvaluebb10 = 0
            factualvaluec10 = 0
            factualvaluecc10 = 0
            factualvalued10 = 0
            factualvaluedd10 = 0
            factualvaluee10 = 0
            factualvalueee10 = 0
            sbeforeresult10 = ""
            bbeforeok10 = 0
            safterresult10 = ""
            bafterok10 = 0
            factualberror10 = 0
            factualaerror10 = 0
            factualvaluea11 = 0
            factualvalueaa11 = 0
            factualvalueb11 = 0
            factualvaluebb11 = 0
            factualvaluec11 = 0
            factualvaluecc11 = 0
            factualvalued11 = 0
            factualvaluedd11 = 0
            factualvaluee11 = 0
            factualvalueee11 = 0
            sbeforeresult11 = ""
            bbeforeok11 = 0
            safterresult11 = ""
            bafterok11 = 0
            factualberror11 = 0
            factualaerror11 = 0
            factualvaluea12 = 0
            factualvalueaa12 = 0
            factualvalueb12 = 0
            factualvaluebb12 = 0
            factualvaluec12 = 0
            factualvaluecc12 = 0
            factualvalued12 = 0
            factualvaluedd12 = 0
            factualvaluee12 = 0
            factualvalueee12 = 0
            sbeforeresult12 = ""
            bbeforeok12 = 0
            safterresult12 = ""
            bafterok12 = 0
            factualberror12 = 0
            factualaerror12 = 0
            factualvaluea13 = 0
            factualvalueaa13 = 0
            factualvalueb13 = 0
            factualvaluebb13 = 0
            factualvaluec13 = 0
            factualvaluecc13 = 0
            factualvalued13 = 0
            factualvaluedd13 = 0
            factualvaluee13 = 0
            factualvalueee13 = 0
            sbeforeresult13 = ""
            bbeforeok13 = 0
            safterresult13 = ""
            bafterok13 = 0
            factualberror13 = 0
            factualaerror13 = 0
            factualvaluea14 = 0
            factualvalueaa14 = 0
            factualvalueb14 = 0
            factualvaluebb14 = 0
            factualvaluec14 = 0
            factualvaluecc14 = 0
            factualvalued14 = 0
            factualvaluedd14 = 0
            factualvaluee14 = 0
            factualvalueee14 = 0
            sbeforeresult14 = ""
            bbeforeok14 = 0
            safterresult14 = ""
            bafterok14 = 0
            factualberror14 = 0
            factualaerror14 = 0
            factualvaluea15 = 0
            factualvalueaa15 = 0
            factualvalueb15 = 0
            factualvaluebb15 = 0
            factualvaluec15 = 0
            factualvaluecc15 = 0
            factualvalued15 = 0
            factualvaluedd15 = 0
            factualvaluee15 = 0
            factualvalueee15 = 0
            sbeforeresult15 = ""
            bbeforeok15 = 0
            safterresult15 = ""
            bafterok15 = 0
            factualberror15 = 0
            factualaerror15 = 0
            factualvaluea16 = 0
            factualvalueaa16 = 0
            factualvalueb16 = 0
            factualvaluebb16 = 0
            factualvaluec16 = 0
            factualvaluecc16 = 0
            factualvalued16 = 0
            factualvaluedd16 = 0
            factualvaluee16 = 0
            factualvalueee16 = 0
            sbeforeresult16 = ""
            bbeforeok16 = 0
            safterresult16 = ""
            bafterok16 = 0
            factualberror16 = 0
            factualaerror16 = 0
            factualvaluea17 = 0
            factualvalueaa17 = 0
            factualvalueb17 = 0
            factualvaluebb17 = 0
            factualvaluec17 = 0
            factualvaluecc17 = 0
            factualvalued17 = 0
            factualvaluedd17 = 0
            factualvaluee17 = 0
            factualvalueee17 = 0
            sbeforeresult17 = ""
            bbeforeok17 = 0
            safterresult17 = ""
            bafterok17 = 0
            factualberror17 = 0
            factualaerror17 = 0
            factualvaluea18 = 0
            factualvalueaa18 = 0
            factualvalueb18 = 0
            factualvaluebb18 = 0
            factualvaluec18 = 0
            factualvaluecc18 = 0
            factualvalued18 = 0
            factualvaluedd18 = 0
            factualvaluee18 = 0
            factualvalueee18 = 0
            sbeforeresult18 = ""
            bbeforeok18 = 0
            safterresult18 = ""
            bafterok18 = 0
            factualberror18 = 0
            factualaerror18 = 0
            factualvaluea19 = 0
            factualvalueaa19 = 0
            factualvalueb19 = 0
            factualvaluebb19 = 0
            factualvaluec19 = 0
            factualvaluecc19 = 0
            factualvalued19 = 0
            factualvaluedd19 = 0
            factualvaluee19 = 0
            factualvalueee19 = 0
            sbeforeresult19 = ""
            bbeforeok19 = 0
            safterresult19 = ""
            bafterok19 = 0
            factualberror19 = 0
            factualaerror19 = 0
            factualvaluea20 = 0
            factualvalueaa20 = 0
            factualvalueb20 = 0
            factualvaluebb20 = 0
            factualvaluec20 = 0
            factualvaluecc20 = 0
            factualvalued20 = 0
            factualvaluedd20 = 0
            factualvaluee20 = 0
            factualvalueee20 = 0
            sbeforeresult20 = ""
            bbeforeok20 = 0
            safterresult20 = ""
            bafterok20 = 0
            factualberror20 = 0
            factualaerror20 = 0
            factualvaluea21 = 0
            factualvalueaa21 = 0
            factualvalueb21 = 0
            factualvaluebb21 = 0
            factualvaluec21 = 0
            factualvaluecc21 = 0
            factualvalued21 = 0
            factualvaluedd21 = 0
            factualvaluee21 = 0
            factualvalueee21 = 0
            sbeforeresult21 = ""
            bbeforeok21 = 0
            safterresult21 = ""
            bafterok21 = 0
            factualberror21 = 0
            factualaerror21 = 0
            factualvaluea22 = 0
            factualvalueaa22 = 0
            factualvalueb22 = 0
            factualvaluebb22 = 0
            factualvaluec22 = 0
            factualvaluecc22 = 0
            factualvalued22 = 0
            factualvaluedd22 = 0
            factualvaluee22 = 0
            factualvalueee22 = 0
            sbeforeresult22 = ""
            bbeforeok22 = 0
            safterresult22 = ""
            bafterok22 = 0
            factualberror22 = 0
            factualaerror22 = 0
            factualvaluea23 = 0
            factualvalueaa23 = 0
            factualvalueb23 = 0
            factualvaluebb23 = 0
            factualvaluec23 = 0
            factualvaluecc23 = 0
            factualvalued23 = 0
            factualvaluedd23 = 0
            factualvaluee23 = 0
            factualvalueee23 = 0
            sbeforeresult23 = ""
            bbeforeok23 = 0
            safterresult23 = ""
            bafterok23 = 0
            factualberror23 = 0
            factualaerror23 = 0
            factualvaluea24 = 0
            factualvalueaa24 = 0
            factualvalueb24 = 0
            factualvaluebb24 = 0
            factualvaluec24 = 0
            factualvaluecc24 = 0
            factualvalued24 = 0
            factualvaluedd24 = 0
            factualvaluee24 = 0
            factualvalueee24 = 0
            sbeforeresult24 = ""
            bbeforeok24 = 0
            safterresult24 = ""
            bafterok24 = 0
            factualberror24 = 0
            factualaerror24 = 0
            factualvaluea25 = 0
            factualvalueaa25 = 0
            factualvalueb25 = 0
            factualvaluebb25 = 0
            factualvaluec25 = 0
            factualvaluecc25 = 0
            factualvalued25 = 0
            factualvaluedd25 = 0
            factualvaluee25 = 0
            factualvalueee25 = 0
            sbeforeresult25 = ""
            bbeforeok25 = 0
            safterresult25 = ""
            bafterok25 = 0
            factualberror25 = 0
            factualaerror25 = 0
            factualvaluea26 = 0
            factualvalueaa26 = 0
            factualvalueb26 = 0
            factualvaluebb26 = 0
            factualvaluec26 = 0
            factualvaluecc26 = 0
            factualvalued26 = 0
            factualvaluedd26 = 0
            factualvaluee26 = 0
            factualvalueee26 = 0
            sbeforeresult26 = ""
            bbeforeok26 = 0
            safterresult26 = ""
            bafterok26 = 0
            factualberror26 = 0
            factualaerror26 = 0
            factualvaluea27 = 0
            factualvalueaa27 = 0
            factualvalueb27 = 0
            factualvaluebb27 = 0
            factualvaluec27 = 0
            factualvaluecc27 = 0
            factualvalued27 = 0
            factualvaluedd27 = 0
            factualvaluee27 = 0
            factualvalueee27 = 0
            sbeforeresult27 = ""
            bbeforeok27 = 0
            safterresult27 = ""
            bafterok27 = 0
            factualberror27 = 0
            factualaerror27 = 0
            factualvaluea28 = 0
            factualvalueaa28 = 0
            factualvalueb28 = 0
            factualvaluebb28 = 0
            factualvaluec28 = 0
            factualvaluecc28 = 0
            factualvalued28 = 0
            factualvaluedd28 = 0
            factualvaluee28 = 0
            factualvalueee28 = 0
            sbeforeresult28 = ""
            bbeforeok28 = 0
            safterresult28 = ""
            bafterok28 = 0
            factualberror28 = 0
            factualaerror28 = 0
            factualvaluea29 = 0
            factualvalueaa29 = 0
            factualvalueb29 = 0
            factualvaluebb29 = 0
            factualvaluec29 = 0
            factualvaluecc29 = 0
            factualvalued29 = 0
            factualvaluedd29 = 0
            factualvaluee29 = 0
            factualvalueee29 = 0
            sbeforeresult29 = ""
            bbeforeok29 = 0
            safterresult29 = ""
            bafterok29 = 0
            factualberror29 = 0
            factualaerror29 = 0
            factualvaluea30 = 0
            factualvalueaa30 = 0
            factualvalueb30 = 0
            factualvaluebb30 = 0
            factualvaluec30 = 0
            factualvaluecc30 = 0
            factualvalued30 = 0
            factualvaluedd30 = 0
            factualvaluee30 = 0
            factualvalueee30 = 0
            sbeforeresult30 = ""
            bbeforeok30 = 0
            safterresult30 = ""
            bafterok30 = 0
            factualberror30 = 0
            factualaerror30 = 0



            Thistorymainpart2Save = Thistorymainpart2(lhistoryid=lhistorymainid, linstrumentid = linstrumentid )
            Thistorymainpart2Save.save() 

            lid2 =0
            lid2 = Thistorymainpart2Save.lid



            Thistorymainpart2SaveUpdate =  Thistorymainpart2.objects.get(lid =lid2) 
        
        
            Thistorymainpart2SaveUpdate.factualvaluea1 = factualvaluea1
            Thistorymainpart2SaveUpdate.factualvalueaa1 = factualvalueaa1
            Thistorymainpart2SaveUpdate.factualvalueb1 = factualvalueb1
            Thistorymainpart2SaveUpdate.factualvaluebb1 = factualvaluebb1
            Thistorymainpart2SaveUpdate.factualvaluec1 = factualvaluec1
            Thistorymainpart2SaveUpdate.factualvaluecc1 = factualvaluecc1
            Thistorymainpart2SaveUpdate.factualvalued1 = factualvalued1
            Thistorymainpart2SaveUpdate.factualvaluedd1 = factualvaluedd1
            Thistorymainpart2SaveUpdate.factualvaluee1 = factualvaluee1
            Thistorymainpart2SaveUpdate.factualvalueee1 = factualvalueee1
            Thistorymainpart2SaveUpdate.sbeforeresult1 = sbeforeresult1
            Thistorymainpart2SaveUpdate.bbeforeok1 = bbeforeok1
            Thistorymainpart2SaveUpdate.safterresult1 = safterresult1
            Thistorymainpart2SaveUpdate.bafterok1 = bafterok1
            Thistorymainpart2SaveUpdate.factualberror1 = factualberror1
            Thistorymainpart2SaveUpdate.factualaerror1 = factualaerror1
            Thistorymainpart2SaveUpdate.factualvaluea2 = factualvaluea2
            Thistorymainpart2SaveUpdate.factualvalueaa2 = factualvalueaa2
            Thistorymainpart2SaveUpdate.factualvalueb2 = factualvalueb2
            Thistorymainpart2SaveUpdate.factualvaluebb2 = factualvaluebb2
            Thistorymainpart2SaveUpdate.factualvaluec2 = factualvaluec2
            Thistorymainpart2SaveUpdate.factualvaluecc2 = factualvaluecc2
            Thistorymainpart2SaveUpdate.factualvalued2 = factualvalued2
            Thistorymainpart2SaveUpdate.factualvaluedd2 = factualvaluedd2
            Thistorymainpart2SaveUpdate.factualvaluee2 = factualvaluee2
            Thistorymainpart2SaveUpdate.factualvalueee2 = factualvalueee2
            Thistorymainpart2SaveUpdate.sbeforeresult2 = sbeforeresult2
            Thistorymainpart2SaveUpdate.bbeforeok2 = bbeforeok2
            Thistorymainpart2SaveUpdate.safterresult2 = safterresult2
            Thistorymainpart2SaveUpdate.bafterok2 = bafterok2
            Thistorymainpart2SaveUpdate.factualberror2 = factualberror2
            Thistorymainpart2SaveUpdate.factualaerror2 = factualaerror2
            Thistorymainpart2SaveUpdate.factualvaluea3 = factualvaluea3
            Thistorymainpart2SaveUpdate.factualvalueaa3 = factualvalueaa3
            Thistorymainpart2SaveUpdate.factualvalueb3 = factualvalueb3
            Thistorymainpart2SaveUpdate.factualvaluebb3 = factualvaluebb3
            Thistorymainpart2SaveUpdate.factualvaluec3 = factualvaluec3
            Thistorymainpart2SaveUpdate.factualvaluecc3 = factualvaluecc3
            Thistorymainpart2SaveUpdate.factualvalued3 = factualvalued3
            Thistorymainpart2SaveUpdate.factualvaluedd3 = factualvaluedd3
            Thistorymainpart2SaveUpdate.factualvaluee3 = factualvaluee3
            Thistorymainpart2SaveUpdate.factualvalueee3 = factualvalueee3
            Thistorymainpart2SaveUpdate.sbeforeresult3 = sbeforeresult3
            Thistorymainpart2SaveUpdate.bbeforeok3 = bbeforeok3
            Thistorymainpart2SaveUpdate.safterresult3 = safterresult3
            Thistorymainpart2SaveUpdate.bafterok3 = bafterok3
            Thistorymainpart2SaveUpdate.factualberror3 = factualberror3
            Thistorymainpart2SaveUpdate.factualaerror3 = factualaerror3
            Thistorymainpart2SaveUpdate.factualvaluea4 = factualvaluea4
            Thistorymainpart2SaveUpdate.factualvalueaa4 = factualvalueaa4
            Thistorymainpart2SaveUpdate.factualvalueb4 = factualvalueb4
            Thistorymainpart2SaveUpdate.factualvaluebb4 = factualvaluebb4
            Thistorymainpart2SaveUpdate.factualvaluec4 = factualvaluec4
            Thistorymainpart2SaveUpdate.factualvaluecc4 = factualvaluecc4
            Thistorymainpart2SaveUpdate.factualvalued4 = factualvalued4
            Thistorymainpart2SaveUpdate.factualvaluedd4 = factualvaluedd4
            Thistorymainpart2SaveUpdate.factualvaluee4 = factualvaluee4
            Thistorymainpart2SaveUpdate.factualvalueee4 = factualvalueee4
            Thistorymainpart2SaveUpdate.sbeforeresult4 = sbeforeresult4
            Thistorymainpart2SaveUpdate.bbeforeok4 = bbeforeok4
            Thistorymainpart2SaveUpdate.safterresult4 = safterresult4
            Thistorymainpart2SaveUpdate.bafterok4 = bafterok4
            Thistorymainpart2SaveUpdate.factualberror4 = factualberror4
            Thistorymainpart2SaveUpdate.factualaerror4 = factualaerror4
            Thistorymainpart2SaveUpdate.factualvaluea5 = factualvaluea5
            Thistorymainpart2SaveUpdate.factualvalueaa5 = factualvalueaa5
            Thistorymainpart2SaveUpdate.factualvalueb5 = factualvalueb5
            Thistorymainpart2SaveUpdate.factualvaluebb5 = factualvaluebb5
            Thistorymainpart2SaveUpdate.factualvaluec5 = factualvaluec5
            Thistorymainpart2SaveUpdate.factualvaluecc5 = factualvaluecc5
            Thistorymainpart2SaveUpdate.factualvalued5 = factualvalued5
            Thistorymainpart2SaveUpdate.factualvaluedd5 = factualvaluedd5
            Thistorymainpart2SaveUpdate.factualvaluee5 = factualvaluee5
            Thistorymainpart2SaveUpdate.factualvalueee5 = factualvalueee5
            Thistorymainpart2SaveUpdate.sbeforeresult5 = sbeforeresult5
            Thistorymainpart2SaveUpdate.bbeforeok5 = bbeforeok5
            Thistorymainpart2SaveUpdate.safterresult5 = safterresult5
            Thistorymainpart2SaveUpdate.bafterok5 = bafterok5
            Thistorymainpart2SaveUpdate.factualberror5 = factualberror5
            Thistorymainpart2SaveUpdate.factualaerror5 = factualaerror5
            Thistorymainpart2SaveUpdate.factualvaluea6 = factualvaluea6
            Thistorymainpart2SaveUpdate.factualvalueaa6 = factualvalueaa6
            Thistorymainpart2SaveUpdate.factualvalueb6 = factualvalueb6
            Thistorymainpart2SaveUpdate.factualvaluebb6 = factualvaluebb6
            Thistorymainpart2SaveUpdate.factualvaluec6 = factualvaluec6
            Thistorymainpart2SaveUpdate.factualvaluecc6 = factualvaluecc6
            Thistorymainpart2SaveUpdate.factualvalued6 = factualvalued6
            Thistorymainpart2SaveUpdate.factualvaluedd6 = factualvaluedd6
            Thistorymainpart2SaveUpdate.factualvaluee6 = factualvaluee6
            Thistorymainpart2SaveUpdate.factualvalueee6 = factualvalueee6
            Thistorymainpart2SaveUpdate.sbeforeresult6 = sbeforeresult6
            Thistorymainpart2SaveUpdate.bbeforeok6 = bbeforeok6
            Thistorymainpart2SaveUpdate.safterresult6 = safterresult6
            Thistorymainpart2SaveUpdate.bafterok6 = bafterok6
            Thistorymainpart2SaveUpdate.factualberror6 = factualberror6
            Thistorymainpart2SaveUpdate.factualaerror6 = factualaerror6
            Thistorymainpart2SaveUpdate.factualvaluea7 = factualvaluea7
            Thistorymainpart2SaveUpdate.factualvalueaa7 = factualvalueaa7
            Thistorymainpart2SaveUpdate.factualvalueb7 = factualvalueb7
            Thistorymainpart2SaveUpdate.factualvaluebb7 = factualvaluebb7
            Thistorymainpart2SaveUpdate.factualvaluec7 = factualvaluec7
            Thistorymainpart2SaveUpdate.factualvaluecc7 = factualvaluecc7
            Thistorymainpart2SaveUpdate.factualvalued7 = factualvalued7
            Thistorymainpart2SaveUpdate.factualvaluedd7 = factualvaluedd7
            Thistorymainpart2SaveUpdate.factualvaluee7 = factualvaluee7
            Thistorymainpart2SaveUpdate.factualvalueee7 = factualvalueee7
            Thistorymainpart2SaveUpdate.sbeforeresult7 = sbeforeresult7
            Thistorymainpart2SaveUpdate.bbeforeok7 = bbeforeok7
            Thistorymainpart2SaveUpdate.safterresult7 = safterresult7
            Thistorymainpart2SaveUpdate.bafterok7 = bafterok7
            Thistorymainpart2SaveUpdate.factualberror7 = factualberror7
            Thistorymainpart2SaveUpdate.factualaerror7 = factualaerror7
            Thistorymainpart2SaveUpdate.factualvaluea8 = factualvaluea8
            Thistorymainpart2SaveUpdate.factualvalueaa8 = factualvalueaa8
            Thistorymainpart2SaveUpdate.factualvalueb8 = factualvalueb8
            Thistorymainpart2SaveUpdate.factualvaluebb8 = factualvaluebb8
            Thistorymainpart2SaveUpdate.factualvaluec8 = factualvaluec8
            Thistorymainpart2SaveUpdate.factualvaluecc8 = factualvaluecc8
            Thistorymainpart2SaveUpdate.factualvalued8 = factualvalued8
            Thistorymainpart2SaveUpdate.factualvaluedd8 = factualvaluedd8
            Thistorymainpart2SaveUpdate.factualvaluee8 = factualvaluee8
            Thistorymainpart2SaveUpdate.factualvalueee8 = factualvalueee8
            Thistorymainpart2SaveUpdate.sbeforeresult8 = sbeforeresult8
            Thistorymainpart2SaveUpdate.bbeforeok8 = bbeforeok8
            Thistorymainpart2SaveUpdate.safterresult8 = safterresult8
            Thistorymainpart2SaveUpdate.bafterok8 = bafterok8
            Thistorymainpart2SaveUpdate.factualberror8 = factualberror8
            Thistorymainpart2SaveUpdate.factualaerror8 = factualaerror8
            Thistorymainpart2SaveUpdate.factualvaluea9 = factualvaluea9
            Thistorymainpart2SaveUpdate.factualvalueaa9 = factualvalueaa9
            Thistorymainpart2SaveUpdate.factualvalueb9 = factualvalueb9
            Thistorymainpart2SaveUpdate.factualvaluebb9 = factualvaluebb9
            Thistorymainpart2SaveUpdate.factualvaluec9 = factualvaluec9
            Thistorymainpart2SaveUpdate.factualvaluecc9 = factualvaluecc9
            Thistorymainpart2SaveUpdate.factualvalued9 = factualvalued9
            Thistorymainpart2SaveUpdate.factualvaluedd9 = factualvaluedd9
            Thistorymainpart2SaveUpdate.factualvaluee9 = factualvaluee9
            Thistorymainpart2SaveUpdate.factualvalueee9 = factualvalueee9
            Thistorymainpart2SaveUpdate.sbeforeresult9 = sbeforeresult9
            Thistorymainpart2SaveUpdate.bbeforeok9 = bbeforeok9
            Thistorymainpart2SaveUpdate.safterresult9 = safterresult9
            Thistorymainpart2SaveUpdate.bafterok9 = bafterok9
            Thistorymainpart2SaveUpdate.factualberror9 = factualberror9
            Thistorymainpart2SaveUpdate.factualaerror9 = factualaerror9
            Thistorymainpart2SaveUpdate.factualvaluea10 = factualvaluea10
            Thistorymainpart2SaveUpdate.factualvalueaa10 = factualvalueaa10
            Thistorymainpart2SaveUpdate.factualvalueb10 = factualvalueb10
            Thistorymainpart2SaveUpdate.factualvaluebb10 = factualvaluebb10
            Thistorymainpart2SaveUpdate.factualvaluec10 = factualvaluec10
            Thistorymainpart2SaveUpdate.factualvaluecc10 = factualvaluecc10
            Thistorymainpart2SaveUpdate.factualvalued10 = factualvalued10
            Thistorymainpart2SaveUpdate.factualvaluedd10 = factualvaluedd10
            Thistorymainpart2SaveUpdate.factualvaluee10 = factualvaluee10
            Thistorymainpart2SaveUpdate.factualvalueee10 = factualvalueee10
            Thistorymainpart2SaveUpdate.sbeforeresult10 = sbeforeresult10
            Thistorymainpart2SaveUpdate.bbeforeok10 = bbeforeok10
            Thistorymainpart2SaveUpdate.safterresult10 = safterresult10
            Thistorymainpart2SaveUpdate.bafterok10 = bafterok10
            Thistorymainpart2SaveUpdate.factualberror10 = factualberror10
            Thistorymainpart2SaveUpdate.factualaerror10 = factualaerror10
            Thistorymainpart2SaveUpdate.factualvaluea11 = factualvaluea11
            Thistorymainpart2SaveUpdate.factualvalueaa11 = factualvalueaa11
            Thistorymainpart2SaveUpdate.factualvalueb11 = factualvalueb11
            Thistorymainpart2SaveUpdate.factualvaluebb11 = factualvaluebb11
            Thistorymainpart2SaveUpdate.factualvaluec11 = factualvaluec11
            Thistorymainpart2SaveUpdate.factualvaluecc11 = factualvaluecc11
            Thistorymainpart2SaveUpdate.factualvalued11 = factualvalued11
            Thistorymainpart2SaveUpdate.factualvaluedd11 = factualvaluedd11
            Thistorymainpart2SaveUpdate.factualvaluee11 = factualvaluee11
            Thistorymainpart2SaveUpdate.factualvalueee11 = factualvalueee11
            Thistorymainpart2SaveUpdate.sbeforeresult11 = sbeforeresult11
            Thistorymainpart2SaveUpdate.bbeforeok11 = bbeforeok11
            Thistorymainpart2SaveUpdate.safterresult11 = safterresult11
            Thistorymainpart2SaveUpdate.bafterok11 = bafterok11
            Thistorymainpart2SaveUpdate.factualberror11 = factualberror11
            Thistorymainpart2SaveUpdate.factualaerror11 = factualaerror11
            Thistorymainpart2SaveUpdate.factualvaluea12 = factualvaluea12
            Thistorymainpart2SaveUpdate.factualvalueaa12 = factualvalueaa12
            Thistorymainpart2SaveUpdate.factualvalueb12 = factualvalueb12
            Thistorymainpart2SaveUpdate.factualvaluebb12 = factualvaluebb12
            Thistorymainpart2SaveUpdate.factualvaluec12 = factualvaluec12
            Thistorymainpart2SaveUpdate.factualvaluecc12 = factualvaluecc12
            Thistorymainpart2SaveUpdate.factualvalued12 = factualvalued12
            Thistorymainpart2SaveUpdate.factualvaluedd12 = factualvaluedd12
            Thistorymainpart2SaveUpdate.factualvaluee12 = factualvaluee12
            Thistorymainpart2SaveUpdate.factualvalueee12 = factualvalueee12
            Thistorymainpart2SaveUpdate.sbeforeresult12 = sbeforeresult12
            Thistorymainpart2SaveUpdate.bbeforeok12 = bbeforeok12
            Thistorymainpart2SaveUpdate.safterresult12 = safterresult12
            Thistorymainpart2SaveUpdate.bafterok12 = bafterok12
            Thistorymainpart2SaveUpdate.factualberror12 = factualberror12
            Thistorymainpart2SaveUpdate.factualaerror12 = factualaerror12
            Thistorymainpart2SaveUpdate.factualvaluea13 = factualvaluea13
            Thistorymainpart2SaveUpdate.factualvalueaa13 = factualvalueaa13
            Thistorymainpart2SaveUpdate.factualvalueb13 = factualvalueb13
            Thistorymainpart2SaveUpdate.factualvaluebb13 = factualvaluebb13
            Thistorymainpart2SaveUpdate.factualvaluec13 = factualvaluec13
            Thistorymainpart2SaveUpdate.factualvaluecc13 = factualvaluecc13
            Thistorymainpart2SaveUpdate.factualvalued13 = factualvalued13
            Thistorymainpart2SaveUpdate.factualvaluedd13 = factualvaluedd13
            Thistorymainpart2SaveUpdate.factualvaluee13 = factualvaluee13
            Thistorymainpart2SaveUpdate.factualvalueee13 = factualvalueee13
            Thistorymainpart2SaveUpdate.sbeforeresult13 = sbeforeresult13
            Thistorymainpart2SaveUpdate.bbeforeok13 = bbeforeok13
            Thistorymainpart2SaveUpdate.safterresult13 = safterresult13
            Thistorymainpart2SaveUpdate.bafterok13 = bafterok13
            Thistorymainpart2SaveUpdate.factualberror13 = factualberror13
            Thistorymainpart2SaveUpdate.factualaerror13 = factualaerror13
            Thistorymainpart2SaveUpdate.factualvaluea14 = factualvaluea14
            Thistorymainpart2SaveUpdate.factualvalueaa14 = factualvalueaa14
            Thistorymainpart2SaveUpdate.factualvalueb14 = factualvalueb14
            Thistorymainpart2SaveUpdate.factualvaluebb14 = factualvaluebb14
            Thistorymainpart2SaveUpdate.factualvaluec14 = factualvaluec14
            Thistorymainpart2SaveUpdate.factualvaluecc14 = factualvaluecc14
            Thistorymainpart2SaveUpdate.factualvalued14 = factualvalued14
            Thistorymainpart2SaveUpdate.factualvaluedd14 = factualvaluedd14
            Thistorymainpart2SaveUpdate.factualvaluee14 = factualvaluee14
            Thistorymainpart2SaveUpdate.factualvalueee14 = factualvalueee14
            Thistorymainpart2SaveUpdate.sbeforeresult14 = sbeforeresult14
            Thistorymainpart2SaveUpdate.bbeforeok14 = bbeforeok14
            Thistorymainpart2SaveUpdate.safterresult14 = safterresult14
            Thistorymainpart2SaveUpdate.bafterok14 = bafterok14
            Thistorymainpart2SaveUpdate.factualberror14 = factualberror14
            Thistorymainpart2SaveUpdate.factualaerror14 = factualaerror14
            Thistorymainpart2SaveUpdate.factualvaluea15 = factualvaluea15
            Thistorymainpart2SaveUpdate.factualvalueaa15 = factualvalueaa15
            Thistorymainpart2SaveUpdate.factualvalueb15 = factualvalueb15
            Thistorymainpart2SaveUpdate.factualvaluebb15 = factualvaluebb15
            Thistorymainpart2SaveUpdate.factualvaluec15 = factualvaluec15
            Thistorymainpart2SaveUpdate.factualvaluecc15 = factualvaluecc15
            Thistorymainpart2SaveUpdate.factualvalued15 = factualvalued15
            Thistorymainpart2SaveUpdate.factualvaluedd15 = factualvaluedd15
            Thistorymainpart2SaveUpdate.factualvaluee15 = factualvaluee15
            Thistorymainpart2SaveUpdate.factualvalueee15 = factualvalueee15
            Thistorymainpart2SaveUpdate.sbeforeresult15 = sbeforeresult15
            Thistorymainpart2SaveUpdate.bbeforeok15 = bbeforeok15
            Thistorymainpart2SaveUpdate.safterresult15 = safterresult15
            Thistorymainpart2SaveUpdate.bafterok15 = bafterok15
            Thistorymainpart2SaveUpdate.factualberror15 = factualberror15
            Thistorymainpart2SaveUpdate.factualaerror15 = factualaerror15
            Thistorymainpart2SaveUpdate.factualvaluea16 = factualvaluea16
            Thistorymainpart2SaveUpdate.factualvalueaa16 = factualvalueaa16
            Thistorymainpart2SaveUpdate.factualvalueb16 = factualvalueb16
            Thistorymainpart2SaveUpdate.factualvaluebb16 = factualvaluebb16
            Thistorymainpart2SaveUpdate.factualvaluec16 = factualvaluec16
            Thistorymainpart2SaveUpdate.factualvaluecc16 = factualvaluecc16
            Thistorymainpart2SaveUpdate.factualvalued16 = factualvalued16
            Thistorymainpart2SaveUpdate.factualvaluedd16 = factualvaluedd16
            Thistorymainpart2SaveUpdate.factualvaluee16 = factualvaluee16
            Thistorymainpart2SaveUpdate.factualvalueee16 = factualvalueee16
            Thistorymainpart2SaveUpdate.sbeforeresult16 = sbeforeresult16
            Thistorymainpart2SaveUpdate.bbeforeok16 = bbeforeok16
            Thistorymainpart2SaveUpdate.safterresult16 = safterresult16
            Thistorymainpart2SaveUpdate.bafterok16 = bafterok16
            Thistorymainpart2SaveUpdate.factualberror16 = factualberror16
            Thistorymainpart2SaveUpdate.factualaerror16 = factualaerror16
            Thistorymainpart2SaveUpdate.factualvaluea17 = factualvaluea17
            Thistorymainpart2SaveUpdate.factualvalueaa17 = factualvalueaa17
            Thistorymainpart2SaveUpdate.factualvalueb17 = factualvalueb17
            Thistorymainpart2SaveUpdate.factualvaluebb17 = factualvaluebb17
            Thistorymainpart2SaveUpdate.factualvaluec17 = factualvaluec17
            Thistorymainpart2SaveUpdate.factualvaluecc17 = factualvaluecc17
            Thistorymainpart2SaveUpdate.factualvalued17 = factualvalued17
            Thistorymainpart2SaveUpdate.factualvaluedd17 = factualvaluedd17
            Thistorymainpart2SaveUpdate.factualvaluee17 = factualvaluee17
            Thistorymainpart2SaveUpdate.factualvalueee17 = factualvalueee17
            Thistorymainpart2SaveUpdate.sbeforeresult17 = sbeforeresult17
            Thistorymainpart2SaveUpdate.bbeforeok17 = bbeforeok17
            Thistorymainpart2SaveUpdate.safterresult17 = safterresult17
            Thistorymainpart2SaveUpdate.bafterok17 = bafterok17
            Thistorymainpart2SaveUpdate.factualberror17 = factualberror17
            Thistorymainpart2SaveUpdate.factualaerror17 = factualaerror17
            Thistorymainpart2SaveUpdate.factualvaluea18 = factualvaluea18
            Thistorymainpart2SaveUpdate.factualvalueaa18 = factualvalueaa18
            Thistorymainpart2SaveUpdate.factualvalueb18 = factualvalueb18
            Thistorymainpart2SaveUpdate.factualvaluebb18 = factualvaluebb18
            Thistorymainpart2SaveUpdate.factualvaluec18 = factualvaluec18
            Thistorymainpart2SaveUpdate.factualvaluecc18 = factualvaluecc18
            Thistorymainpart2SaveUpdate.factualvalued18 = factualvalued18
            Thistorymainpart2SaveUpdate.factualvaluedd18 = factualvaluedd18
            Thistorymainpart2SaveUpdate.factualvaluee18 = factualvaluee18
            Thistorymainpart2SaveUpdate.factualvalueee18 = factualvalueee18
            Thistorymainpart2SaveUpdate.sbeforeresult18 = sbeforeresult18
            Thistorymainpart2SaveUpdate.bbeforeok18 = bbeforeok18
            Thistorymainpart2SaveUpdate.safterresult18 = safterresult18
            Thistorymainpart2SaveUpdate.bafterok18 = bafterok18
            Thistorymainpart2SaveUpdate.factualberror18 = factualberror18
            Thistorymainpart2SaveUpdate.factualaerror18 = factualaerror18
            Thistorymainpart2SaveUpdate.factualvaluea19 = factualvaluea19
            Thistorymainpart2SaveUpdate.factualvalueaa19 = factualvalueaa19
            Thistorymainpart2SaveUpdate.factualvalueb19 = factualvalueb19
            Thistorymainpart2SaveUpdate.factualvaluebb19 = factualvaluebb19
            Thistorymainpart2SaveUpdate.factualvaluec19 = factualvaluec19
            Thistorymainpart2SaveUpdate.factualvaluecc19 = factualvaluecc19
            Thistorymainpart2SaveUpdate.factualvalued19 = factualvalued19
            Thistorymainpart2SaveUpdate.factualvaluedd19 = factualvaluedd19
            Thistorymainpart2SaveUpdate.factualvaluee19 = factualvaluee19
            Thistorymainpart2SaveUpdate.factualvalueee19 = factualvalueee19
            Thistorymainpart2SaveUpdate.sbeforeresult19 = sbeforeresult19
            Thistorymainpart2SaveUpdate.bbeforeok19 = bbeforeok19
            Thistorymainpart2SaveUpdate.safterresult19 = safterresult19
            Thistorymainpart2SaveUpdate.bafterok19 = bafterok19
            Thistorymainpart2SaveUpdate.factualberror19 = factualberror19
            Thistorymainpart2SaveUpdate.factualaerror19 = factualaerror19
            Thistorymainpart2SaveUpdate.factualvaluea20 = factualvaluea20
            Thistorymainpart2SaveUpdate.factualvalueaa20 = factualvalueaa20
            Thistorymainpart2SaveUpdate.factualvalueb20 = factualvalueb20
            Thistorymainpart2SaveUpdate.factualvaluebb20 = factualvaluebb20
            Thistorymainpart2SaveUpdate.factualvaluec20 = factualvaluec20
            Thistorymainpart2SaveUpdate.factualvaluecc20 = factualvaluecc20
            Thistorymainpart2SaveUpdate.factualvalued20 = factualvalued20
            Thistorymainpart2SaveUpdate.factualvaluedd20 = factualvaluedd20
            Thistorymainpart2SaveUpdate.factualvaluee20 = factualvaluee20
            Thistorymainpart2SaveUpdate.factualvalueee20 = factualvalueee20
            Thistorymainpart2SaveUpdate.sbeforeresult20 = sbeforeresult20
            Thistorymainpart2SaveUpdate.bbeforeok20 = bbeforeok20
            Thistorymainpart2SaveUpdate.safterresult20 = safterresult20
            Thistorymainpart2SaveUpdate.bafterok20 = bafterok20
            Thistorymainpart2SaveUpdate.factualberror20 = factualberror20
            Thistorymainpart2SaveUpdate.factualaerror20 = factualaerror20
            Thistorymainpart2SaveUpdate.factualvaluea21 = factualvaluea21
            Thistorymainpart2SaveUpdate.factualvalueaa21 = factualvalueaa21
            Thistorymainpart2SaveUpdate.factualvalueb21 = factualvalueb21
            Thistorymainpart2SaveUpdate.factualvaluebb21 = factualvaluebb21
            Thistorymainpart2SaveUpdate.factualvaluec21 = factualvaluec21
            Thistorymainpart2SaveUpdate.factualvaluecc21 = factualvaluecc21
            Thistorymainpart2SaveUpdate.factualvalued21 = factualvalued21
            Thistorymainpart2SaveUpdate.factualvaluedd21 = factualvaluedd21
            Thistorymainpart2SaveUpdate.factualvaluee21 = factualvaluee21
            Thistorymainpart2SaveUpdate.factualvalueee21 = factualvalueee21
            Thistorymainpart2SaveUpdate.sbeforeresult21 = sbeforeresult21
            Thistorymainpart2SaveUpdate.bbeforeok21 = bbeforeok21
            Thistorymainpart2SaveUpdate.safterresult21 = safterresult21
            Thistorymainpart2SaveUpdate.bafterok21 = bafterok21
            Thistorymainpart2SaveUpdate.factualberror21 = factualberror21
            Thistorymainpart2SaveUpdate.factualaerror21 = factualaerror21
            Thistorymainpart2SaveUpdate.factualvaluea22 = factualvaluea22
            Thistorymainpart2SaveUpdate.factualvalueaa22 = factualvalueaa22
            Thistorymainpart2SaveUpdate.factualvalueb22 = factualvalueb22
            Thistorymainpart2SaveUpdate.factualvaluebb22 = factualvaluebb22
            Thistorymainpart2SaveUpdate.factualvaluec22 = factualvaluec22
            Thistorymainpart2SaveUpdate.factualvaluecc22 = factualvaluecc22
            Thistorymainpart2SaveUpdate.factualvalued22 = factualvalued22
            Thistorymainpart2SaveUpdate.factualvaluedd22 = factualvaluedd22
            Thistorymainpart2SaveUpdate.factualvaluee22 = factualvaluee22
            Thistorymainpart2SaveUpdate.factualvalueee22 = factualvalueee22
            Thistorymainpart2SaveUpdate.sbeforeresult22 = sbeforeresult22
            Thistorymainpart2SaveUpdate.bbeforeok22 = bbeforeok22
            Thistorymainpart2SaveUpdate.safterresult22 = safterresult22
            Thistorymainpart2SaveUpdate.bafterok22 = bafterok22
            Thistorymainpart2SaveUpdate.factualberror22 = factualberror22
            Thistorymainpart2SaveUpdate.factualaerror22 = factualaerror22
            Thistorymainpart2SaveUpdate.factualvaluea23 = factualvaluea23
            Thistorymainpart2SaveUpdate.factualvalueaa23 = factualvalueaa23
            Thistorymainpart2SaveUpdate.factualvalueb23 = factualvalueb23
            Thistorymainpart2SaveUpdate.factualvaluebb23 = factualvaluebb23
            Thistorymainpart2SaveUpdate.factualvaluec23 = factualvaluec23
            Thistorymainpart2SaveUpdate.factualvaluecc23 = factualvaluecc23
            Thistorymainpart2SaveUpdate.factualvalued23 = factualvalued23
            Thistorymainpart2SaveUpdate.factualvaluedd23 = factualvaluedd23
            Thistorymainpart2SaveUpdate.factualvaluee23 = factualvaluee23
            Thistorymainpart2SaveUpdate.factualvalueee23 = factualvalueee23
            Thistorymainpart2SaveUpdate.sbeforeresult23 = sbeforeresult23
            Thistorymainpart2SaveUpdate.bbeforeok23 = bbeforeok23
            Thistorymainpart2SaveUpdate.safterresult23 = safterresult23
            Thistorymainpart2SaveUpdate.bafterok23 = bafterok23
            Thistorymainpart2SaveUpdate.factualberror23 = factualberror23
            Thistorymainpart2SaveUpdate.factualaerror23 = factualaerror23
            Thistorymainpart2SaveUpdate.factualvaluea24 = factualvaluea24
            Thistorymainpart2SaveUpdate.factualvalueaa24 = factualvalueaa24
            Thistorymainpart2SaveUpdate.factualvalueb24 = factualvalueb24
            Thistorymainpart2SaveUpdate.factualvaluebb24 = factualvaluebb24
            Thistorymainpart2SaveUpdate.factualvaluec24 = factualvaluec24
            Thistorymainpart2SaveUpdate.factualvaluecc24 = factualvaluecc24
            Thistorymainpart2SaveUpdate.factualvalued24 = factualvalued24
            Thistorymainpart2SaveUpdate.factualvaluedd24 = factualvaluedd24
            Thistorymainpart2SaveUpdate.factualvaluee24 = factualvaluee24
            Thistorymainpart2SaveUpdate.factualvalueee24 = factualvalueee24
            Thistorymainpart2SaveUpdate.sbeforeresult24 = sbeforeresult24
            Thistorymainpart2SaveUpdate.bbeforeok24 = bbeforeok24
            Thistorymainpart2SaveUpdate.safterresult24 = safterresult24
            Thistorymainpart2SaveUpdate.bafterok24 = bafterok24
            Thistorymainpart2SaveUpdate.factualberror24 = factualberror24
            Thistorymainpart2SaveUpdate.factualaerror24 = factualaerror24
            Thistorymainpart2SaveUpdate.factualvaluea25 = factualvaluea25
            Thistorymainpart2SaveUpdate.factualvalueaa25 = factualvalueaa25
            Thistorymainpart2SaveUpdate.factualvalueb25 = factualvalueb25
            Thistorymainpart2SaveUpdate.factualvaluebb25 = factualvaluebb25
            Thistorymainpart2SaveUpdate.factualvaluec25 = factualvaluec25
            Thistorymainpart2SaveUpdate.factualvaluecc25 = factualvaluecc25
            Thistorymainpart2SaveUpdate.factualvalued25 = factualvalued25
            Thistorymainpart2SaveUpdate.factualvaluedd25 = factualvaluedd25
            Thistorymainpart2SaveUpdate.factualvaluee25 = factualvaluee25
            Thistorymainpart2SaveUpdate.factualvalueee25 = factualvalueee25
            Thistorymainpart2SaveUpdate.sbeforeresult25 = sbeforeresult25
            Thistorymainpart2SaveUpdate.bbeforeok25 = bbeforeok25
            Thistorymainpart2SaveUpdate.safterresult25 = safterresult25
            Thistorymainpart2SaveUpdate.bafterok25 = bafterok25
            Thistorymainpart2SaveUpdate.factualberror25 = factualberror25
            Thistorymainpart2SaveUpdate.factualaerror25 = factualaerror25
            Thistorymainpart2SaveUpdate.factualvaluea26 = factualvaluea26
            Thistorymainpart2SaveUpdate.factualvalueaa26 = factualvalueaa26
            Thistorymainpart2SaveUpdate.factualvalueb26 = factualvalueb26
            Thistorymainpart2SaveUpdate.factualvaluebb26 = factualvaluebb26
            Thistorymainpart2SaveUpdate.factualvaluec26 = factualvaluec26
            Thistorymainpart2SaveUpdate.factualvaluecc26 = factualvaluecc26
            Thistorymainpart2SaveUpdate.factualvalued26 = factualvalued26
            Thistorymainpart2SaveUpdate.factualvaluedd26 = factualvaluedd26
            Thistorymainpart2SaveUpdate.factualvaluee26 = factualvaluee26
            Thistorymainpart2SaveUpdate.factualvalueee26 = factualvalueee26
            Thistorymainpart2SaveUpdate.sbeforeresult26 = sbeforeresult26
            Thistorymainpart2SaveUpdate.bbeforeok26 = bbeforeok26
            Thistorymainpart2SaveUpdate.safterresult26 = safterresult26
            Thistorymainpart2SaveUpdate.bafterok26 = bafterok26
            Thistorymainpart2SaveUpdate.factualberror26 = factualberror26
            Thistorymainpart2SaveUpdate.factualaerror26 = factualaerror26
            Thistorymainpart2SaveUpdate.factualvaluea27 = factualvaluea27
            Thistorymainpart2SaveUpdate.factualvalueaa27 = factualvalueaa27
            Thistorymainpart2SaveUpdate.factualvalueb27 = factualvalueb27
            Thistorymainpart2SaveUpdate.factualvaluebb27 = factualvaluebb27
            Thistorymainpart2SaveUpdate.factualvaluec27 = factualvaluec27
            Thistorymainpart2SaveUpdate.factualvaluecc27 = factualvaluecc27
            Thistorymainpart2SaveUpdate.factualvalued27 = factualvalued27
            Thistorymainpart2SaveUpdate.factualvaluedd27 = factualvaluedd27
            Thistorymainpart2SaveUpdate.factualvaluee27 = factualvaluee27
            Thistorymainpart2SaveUpdate.factualvalueee27 = factualvalueee27
            Thistorymainpart2SaveUpdate.sbeforeresult27 = sbeforeresult27
            Thistorymainpart2SaveUpdate.bbeforeok27 = bbeforeok27
            Thistorymainpart2SaveUpdate.safterresult27 = safterresult27
            Thistorymainpart2SaveUpdate.bafterok27 = bafterok27
            Thistorymainpart2SaveUpdate.factualberror27 = factualberror27
            Thistorymainpart2SaveUpdate.factualaerror27 = factualaerror27
            Thistorymainpart2SaveUpdate.factualvaluea28 = factualvaluea28
            Thistorymainpart2SaveUpdate.factualvalueaa28 = factualvalueaa28
            Thistorymainpart2SaveUpdate.factualvalueb28 = factualvalueb28
            Thistorymainpart2SaveUpdate.factualvaluebb28 = factualvaluebb28
            Thistorymainpart2SaveUpdate.factualvaluec28 = factualvaluec28
            Thistorymainpart2SaveUpdate.factualvaluecc28 = factualvaluecc28
            Thistorymainpart2SaveUpdate.factualvalued28 = factualvalued28
            Thistorymainpart2SaveUpdate.factualvaluedd28 = factualvaluedd28
            Thistorymainpart2SaveUpdate.factualvaluee28 = factualvaluee28
            Thistorymainpart2SaveUpdate.factualvalueee28 = factualvalueee28
            Thistorymainpart2SaveUpdate.sbeforeresult28 = sbeforeresult28
            Thistorymainpart2SaveUpdate.bbeforeok28 = bbeforeok28
            Thistorymainpart2SaveUpdate.safterresult28 = safterresult28
            Thistorymainpart2SaveUpdate.bafterok28 = bafterok28
            Thistorymainpart2SaveUpdate.factualberror28 = factualberror28
            Thistorymainpart2SaveUpdate.factualaerror28 = factualaerror28
            Thistorymainpart2SaveUpdate.factualvaluea29 = factualvaluea29
            Thistorymainpart2SaveUpdate.factualvalueaa29 = factualvalueaa29
            Thistorymainpart2SaveUpdate.factualvalueb29 = factualvalueb29
            Thistorymainpart2SaveUpdate.factualvaluebb29 = factualvaluebb29
            Thistorymainpart2SaveUpdate.factualvaluec29 = factualvaluec29
            Thistorymainpart2SaveUpdate.factualvaluecc29 = factualvaluecc29
            Thistorymainpart2SaveUpdate.factualvalued29 = factualvalued29
            Thistorymainpart2SaveUpdate.factualvaluedd29 = factualvaluedd29
            Thistorymainpart2SaveUpdate.factualvaluee29 = factualvaluee29
            Thistorymainpart2SaveUpdate.factualvalueee29 = factualvalueee29
            Thistorymainpart2SaveUpdate.sbeforeresult29 = sbeforeresult29
            Thistorymainpart2SaveUpdate.bbeforeok29 = bbeforeok29
            Thistorymainpart2SaveUpdate.safterresult29 = safterresult29
            Thistorymainpart2SaveUpdate.bafterok29 = bafterok29
            Thistorymainpart2SaveUpdate.factualberror29 = factualberror29
            Thistorymainpart2SaveUpdate.factualaerror29 = factualaerror29
            Thistorymainpart2SaveUpdate.factualvaluea30 = factualvaluea30
            Thistorymainpart2SaveUpdate.factualvalueaa30 = factualvalueaa30
            Thistorymainpart2SaveUpdate.factualvalueb30 = factualvalueb30
            Thistorymainpart2SaveUpdate.factualvaluebb30 = factualvaluebb30
            Thistorymainpart2SaveUpdate.factualvaluec30 = factualvaluec30
            Thistorymainpart2SaveUpdate.factualvaluecc30 = factualvaluecc30
            Thistorymainpart2SaveUpdate.factualvalued30 = factualvalued30
            Thistorymainpart2SaveUpdate.factualvaluedd30 = factualvaluedd30
            Thistorymainpart2SaveUpdate.factualvaluee30 = factualvaluee30
            Thistorymainpart2SaveUpdate.factualvalueee30 = factualvalueee30
            Thistorymainpart2SaveUpdate.sbeforeresult30 = sbeforeresult30
            Thistorymainpart2SaveUpdate.bbeforeok30 = bbeforeok30
            Thistorymainpart2SaveUpdate.safterresult30 = safterresult30
            Thistorymainpart2SaveUpdate.bafterok30 = bafterok30
            Thistorymainpart2SaveUpdate.factualberror30 = factualberror30
            Thistorymainpart2SaveUpdate.factualaerror30 = factualaerror30



            Thistorymainpart2SaveUpdate.save()

            request.session['lhistorymainid'] = lhistorymainid


            lhistorymainid=0
            linstrumentid=0
            linstrumentid= linstrumentid
            shistorytype=""
            shistorytype="Inprocess"
            scalibrationvendor=""
            scalibrationvendorid=""
            senteredby=""
            senteredby= semployeename + " (" + semployeeno + ")"
            scalibrationresult=""
            scurrentstatus=""
            scurrentstatus="Calibration Started"
            dtcalibrationdate=datetime.now()
            fcalibcost=0
            llplantid=0
            ssplantname=""
            slplantcode=""
            lcompanyid=0  
            llplantid=lPlantId
            ssplantname=sPlantName
            slplantcode=sPlantCode
            lcompanyid=lcompanyid  
    


            dtreturneddate=datetime.now()
            sinstrumentcode=""
            sinstrumentcode=sinstrumentcode
            sdesc=sinstrumentdesc
            sto=""
            sfrom=""
            dthistorydate=datetime.now()
            shistorydate=""
            sreturneddate=""
            llineid=0
            slinename=""
            scomment=""
 
        
            ThistorytransactionsSave = Thistorytransactions(linstrumentid  = linstrumentid )
            ThistorytransactionsSave.save() 

            lTransID =0
            lTransID = ThistorytransactionsSave.lid
            ThistorytransactionsSaveUpdate =  Thistorytransactions.objects.get(lid =lTransID) 

            ThistorytransactionsSaveUpdate.lhistorymainid=lhistorymainid
            ThistorytransactionsSaveUpdate.linstrumentid=linstrumentid
            ThistorytransactionsSaveUpdate.shistorytype=shistorytype
            ThistorytransactionsSaveUpdate.scalibrationvendor=scalibrationvendor
            ThistorytransactionsSaveUpdate.scalibrationvendorid=scalibrationvendorid
            ThistorytransactionsSaveUpdate.senteredby=senteredby
            ThistorytransactionsSaveUpdate.scalibrationresult=scalibrationresult
            ThistorytransactionsSaveUpdate.scurrentstatus=scurrentstatus
            ThistorytransactionsSaveUpdate.dtcalibrationdate=dtcalibrationdate
            ThistorytransactionsSaveUpdate.fcalibcost=fcalibcost
            ThistorytransactionsSaveUpdate.llplantid=llplantid
            ThistorytransactionsSaveUpdate.ssplantname=ssplantname
            ThistorytransactionsSaveUpdate.slplantcode=slplantcode
            ThistorytransactionsSaveUpdate.lcompanyid=lcompanyid
            ThistorytransactionsSaveUpdate.dtreturneddate=dtreturneddate
            ThistorytransactionsSaveUpdate.sinstrumentcode=sinstrumentcode
            ThistorytransactionsSaveUpdate.sdesc=sdesc
            ThistorytransactionsSaveUpdate.sto=sto
            ThistorytransactionsSaveUpdate.sfrom=sfrom
            ThistorytransactionsSaveUpdate.dthistorydate=dthistorydate
            ThistorytransactionsSaveUpdate.shistorydate=shistorydate
            ThistorytransactionsSaveUpdate.sreturneddate=sreturneddate
            ThistorytransactionsSaveUpdate.llineid=llineid
            ThistorytransactionsSaveUpdate.slinename=slinename
            ThistorytransactionsSaveUpdate.scomment=scomment



            ThistorytransactionsSaveUpdate.save()



            return   redirect('CalibrationPendingDetails')    


    else:

        Masterinstrumentslist_listA =  Masterinstrumentslist.objects.get(  lid=lID)
        if Masterinstrumentslist_listA:

            if(Masterinstrumentslist_listA.bunderrepair == 1):
                historyserviceid =0
                linstrumentid = lID
                historyserviceid = Masterinstrumentslist_listA.lrepairid
                Tservicehistory_listA =  Tservicehistory.objects.get(  historyserviceid=historyserviceid)
                if Tservicehistory_listA:

                    if(Tservicehistory_listA.bapproved == 1):
                        
                        historyserviceid =0

                        linstrumentid = lID
                        lscheduleid = 0
                        sinstrumentcode = Masterinstrumentslist_listA.sinstrumentcode
                        sinstrumentdesc = Masterinstrumentslist_listA.sdescription
                        brepair = 0
                        scurrentstatus = ""
                        sserviceresult = ""
                        dtservicedate = datetime.now()
                        fservicecost = 0
                        stimetaken = ""
                        sdevicecondition = ""
                        lenteredid = 0
                        senteredby = ""
                        lapprovedid = 0
                        sapprovedby = ""
                        dtapprovaldate = datetime.now()
                        scertificateno = ""
                        scomments = ""
                        lservicevendorid = 0
                        sservicevendor = ""
                        spurchaseorderno = ""
                        sservicecertificatefile = ""
                        sservicecertificatepath = ""
                        dtdispatchdate = datetime.now()
                        dtduedate = datetime.now()
                        lusedbyid = 0
                        susedbyname = ""
                        bapproved = 0
                        brefdatail = 0
                        dvendor = datetime.now()
                        drefdate = datetime.now()
                        fpmcost = 0
                        lplantid = 0
                        splantname = ""
                        splantcode = ""
                        lcompanyid = 0
                        lnoticedbyid = 0
                        snoticedbyname = ""
                        sreason = ""
                        dtdateofnotice = datetime.now()
                        llocationid = 0
                        slocationname = ""
                        brejected = 0
                        bsentforrepair = 0
                        ldcrefid = 0
                        sservicedate = ""
                        sapprovaldate = ""
                        sdispatchdate = ""
                        sduedate = ""
                        srefdate = ""
                        sdateofnotice = ""
                        bdvendor = 0


                                
                        TservicehistorySave = Tservicehistory(linstrumentid = linstrumentid, 	lscheduleid = lscheduleid, 	sinstrumentcode = sinstrumentcode, 	sinstrumentdesc = sinstrumentdesc, 	brepair = brepair, 	scurrentstatus = scurrentstatus, 	sserviceresult = sserviceresult, 	dtservicedate = dtservicedate, 	fservicecost = fservicecost, 	stimetaken = stimetaken, 	sdevicecondition = sdevicecondition, 	lenteredid = lenteredid, 	senteredby = senteredby, 	lapprovedid = lapprovedid, 	sapprovedby = sapprovedby, 	dtapprovaldate = dtapprovaldate, 	scertificateno = scertificateno, 	scomments = scomments, 	lservicevendorid = lservicevendorid, 	sservicevendor = sservicevendor, 	spurchaseorderno = spurchaseorderno, 	sservicecertificatefile = sservicecertificatefile, 	sservicecertificatepath = sservicecertificatepath, 	dtdispatchdate = dtdispatchdate, 	dtduedate = dtduedate, 	lusedbyid = lusedbyid, 	susedbyname = susedbyname, 	bapproved = bapproved, 	brefdatail = brefdatail, 	dvendor = dvendor, 	drefdate = drefdate, 	fpmcost = fpmcost, 	lplantid = lplantid, 	splantname = splantname, 	splantcode = splantcode, 	lcompanyid = lcompanyid, 	lnoticedbyid = lnoticedbyid, 	snoticedbyname = snoticedbyname, 	sreason = sreason, 	dtdateofnotice = dtdateofnotice, 	llocationid = llocationid, 	slocationname = slocationname, 	brejected = brejected, 	bsentforrepair = bsentforrepair, 	ldcrefid = ldcrefid, 	sservicedate = sservicedate, 	sapprovaldate = sapprovaldate, 	sdispatchdate = sdispatchdate, 	sduedate = sduedate, 	srefdate = srefdate, 	sdateofnotice = sdateofnotice, 	bdvendor = bdvendor)

                        TservicehistorySave.save()
                        historyserviceid = TservicehistorySave.historyserviceid

                        Masterinstrumentslist_listA.bunderrepair =1
                        Masterinstrumentslist_listA.lrepairid =historyserviceid
                        Masterinstrumentslist_listA.save()
                
                    else:
                        
                        historyserviceid = Tservicehistory_listA.historyserviceid

                else:


                    linstrumentid = lID
                    lscheduleid = 0
                    sinstrumentcode = Masterinstrumentslist_listA.sinstrumentcode
                    sinstrumentdesc = Masterinstrumentslist_listA.sdescription
                    brepair = 0
                    scurrentstatus = ""
                    sserviceresult = ""
                    dtservicedate = datetime.now()
                    fservicecost = 0
                    stimetaken = ""
                    sdevicecondition = ""
                    lenteredid = 0
                    senteredby = ""
                    lapprovedid = 0
                    sapprovedby = ""
                    dtapprovaldate = datetime.now()
                    scertificateno = ""
                    scomments = ""
                    lservicevendorid = 0
                    sservicevendor = ""
                    spurchaseorderno = ""
                    sservicecertificatefile = ""
                    sservicecertificatepath = ""
                    dtdispatchdate = datetime.now()
                    dtduedate = datetime.now()
                    lusedbyid = 0
                    susedbyname = ""
                    bapproved = 0
                    brefdatail = 0
                    dvendor = datetime.now()
                    drefdate = datetime.now()
                    fpmcost = 0
                    lplantid = 0
                    splantname = ""
                    splantcode = ""
                    lcompanyid = 0
                    lnoticedbyid = 0
                    snoticedbyname = ""
                    sreason = ""
                    dtdateofnotice = datetime.now()
                    llocationid = 0
                    slocationname = ""
                    brejected = 0
                    bsentforrepair = 0
                    ldcrefid = 0
                    sservicedate = ""
                    sapprovaldate = ""
                    sdispatchdate = ""
                    sduedate = ""
                    srefdate = ""
                    sdateofnotice = ""
                    bdvendor = 0


                            
                    TservicehistorySave = Tservicehistory(linstrumentid = linstrumentid, 	lscheduleid = lscheduleid, 	sinstrumentcode = sinstrumentcode, 	sinstrumentdesc = sinstrumentdesc, 	brepair = brepair, 	scurrentstatus = scurrentstatus, 	sserviceresult = sserviceresult, 	dtservicedate = dtservicedate, 	fservicecost = fservicecost, 	stimetaken = stimetaken, 	sdevicecondition = sdevicecondition, 	lenteredid = lenteredid, 	senteredby = senteredby, 	lapprovedid = lapprovedid, 	sapprovedby = sapprovedby, 	dtapprovaldate = dtapprovaldate, 	scertificateno = scertificateno, 	scomments = scomments, 	lservicevendorid = lservicevendorid, 	sservicevendor = sservicevendor, 	spurchaseorderno = spurchaseorderno, 	sservicecertificatefile = sservicecertificatefile, 	sservicecertificatepath = sservicecertificatepath, 	dtdispatchdate = dtdispatchdate, 	dtduedate = dtduedate, 	lusedbyid = lusedbyid, 	susedbyname = susedbyname, 	bapproved = bapproved, 	brefdatail = brefdatail, 	dvendor = dvendor, 	drefdate = drefdate, 	fpmcost = fpmcost, 	lplantid = lplantid, 	splantname = splantname, 	splantcode = splantcode, 	lcompanyid = lcompanyid, 	lnoticedbyid = lnoticedbyid, 	snoticedbyname = snoticedbyname, 	sreason = sreason, 	dtdateofnotice = dtdateofnotice, 	llocationid = llocationid, 	slocationname = slocationname, 	brejected = brejected, 	bsentforrepair = bsentforrepair, 	ldcrefid = ldcrefid, 	sservicedate = sservicedate, 	sapprovaldate = sapprovaldate, 	sdispatchdate = sdispatchdate, 	sduedate = sduedate, 	srefdate = srefdate, 	sdateofnotice = sdateofnotice, 	bdvendor = bdvendor)

                    TservicehistorySave.save()
                    historyserviceid = TservicehistorySave.historyserviceid

                    Masterinstrumentslist_listA.bunderrepair =1
                    Masterinstrumentslist_listA.lrepairid =historyserviceid
                    Masterinstrumentslist_listA.save()


            if(Masterinstrumentslist_listA.bunderrepair == 0):
                historyserviceid = 0




                linstrumentid = lID
                lscheduleid = 0
                sinstrumentcode = Masterinstrumentslist_listA.sinstrumentcode
                sinstrumentdesc = Masterinstrumentslist_listA.sdescription
                brepair = 0
                scurrentstatus = ""
                sserviceresult = ""
                dtservicedate = datetime.now()
                fservicecost = 0
                stimetaken = ""
                sdevicecondition = ""
                lenteredid = 0
                senteredby = ""
                lapprovedid = 0
                sapprovedby = ""
                dtapprovaldate = datetime.now()
                scertificateno = ""
                scomments = ""
                lservicevendorid = 0
                sservicevendor = ""
                spurchaseorderno = ""
                sservicecertificatefile = ""
                sservicecertificatepath = ""
                dtdispatchdate = datetime.now()
                dtduedate = datetime.now()
                lusedbyid = 0
                susedbyname = ""
                bapproved = 0
                brefdatail = 0
                dvendor = datetime.now()
                drefdate = datetime.now()
                fpmcost = 0
                lplantid = 0
                splantname = ""
                splantcode = ""
                lcompanyid = 0
                lnoticedbyid = 0
                snoticedbyname = ""
                sreason = ""
                dtdateofnotice = datetime.now()
                llocationid = 0
                slocationname = ""
                brejected = 0
                bsentforrepair = 0
                ldcrefid = 0
                sservicedate = ""
                sapprovaldate = ""
                sdispatchdate = ""
                sduedate = ""
                srefdate = ""
                sdateofnotice = ""
                bdvendor = 0


                         
                TservicehistorySave = Tservicehistory(linstrumentid = linstrumentid, 	lscheduleid = lscheduleid, 	sinstrumentcode = sinstrumentcode, 	sinstrumentdesc = sinstrumentdesc, 	brepair = brepair, 	scurrentstatus = scurrentstatus, 	sserviceresult = sserviceresult, 	dtservicedate = dtservicedate, 	fservicecost = fservicecost, 	stimetaken = stimetaken, 	sdevicecondition = sdevicecondition, 	lenteredid = lenteredid, 	senteredby = senteredby, 	lapprovedid = lapprovedid, 	sapprovedby = sapprovedby, 	dtapprovaldate = dtapprovaldate, 	scertificateno = scertificateno, 	scomments = scomments, 	lservicevendorid = lservicevendorid, 	sservicevendor = sservicevendor, 	spurchaseorderno = spurchaseorderno, 	sservicecertificatefile = sservicecertificatefile, 	sservicecertificatepath = sservicecertificatepath, 	dtdispatchdate = dtdispatchdate, 	dtduedate = dtduedate, 	lusedbyid = lusedbyid, 	susedbyname = susedbyname, 	bapproved = bapproved, 	brefdatail = brefdatail, 	dvendor = dvendor, 	drefdate = drefdate, 	fpmcost = fpmcost, 	lplantid = lplantid, 	splantname = splantname, 	splantcode = splantcode, 	lcompanyid = lcompanyid, 	lnoticedbyid = lnoticedbyid, 	snoticedbyname = snoticedbyname, 	sreason = sreason, 	dtdateofnotice = dtdateofnotice, 	llocationid = llocationid, 	slocationname = slocationname, 	brejected = brejected, 	bsentforrepair = bsentforrepair, 	ldcrefid = ldcrefid, 	sservicedate = sservicedate, 	sapprovaldate = sapprovaldate, 	sdispatchdate = sdispatchdate, 	sduedate = sduedate, 	srefdate = srefdate, 	sdateofnotice = sdateofnotice, 	bdvendor = bdvendor)

                TservicehistorySave.save()
                historyserviceid = TservicehistorySave.historyserviceid

                Masterinstrumentslist_listA.bunderrepair =1
                Masterinstrumentslist_listA.lrepairid =historyserviceid
                Masterinstrumentslist_listA.save()

 
         
        AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
        if AdminunitlistActive:
            sPlantCode = AdminunitlistActive.splantno
            sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
            sPlantNameNameA = AdminunitlistActive.splantname

        request.session['sPlantCode']   =sPlantCode
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:
            Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else: 
            Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
            
        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

        if(sFlowName1 == "Part No1"):
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
        else:  
            Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

        Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
        
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)
 
        
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')

        TservicehistoryActive = Tservicehistory.objects.get(historyserviceid=historyserviceid) 
        


        return render(request, "CloudCaliber/GaugeServiceRepair.html", 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
            
            'CurDateNow':datetime.now(),
            'TservicehistoryActive':TservicehistoryActive,
            'lPlantId':lPlantId,  
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName , 
            'Location': 0 , 
            'semployeename':  semployeename,
            'txtSearch': "" , 
            'sCodeFinal1': "" ,  
            'sCodeFinal2': "" ,  
            'cmbClassificationID': 0 , 
            'cmbCategoryID': 0 ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': "",  
            'cmbFlow2label': "",  
            'cmbFlow3label': "",  
            'cmbFlow4label': "",
            'cmbFlow5label': "",  
            'bNewID': 0 ,  
            'Adminassettypelist_list':Adminassettypelist_list,
            'bSAPCodeDone': bSAPCodeDone, 
            'bSAPCodeNotDone': bSAPCodeNotDone,  
            'sIssueDate': sIssueDate, 
        }) 


 
@csrf_exempt
def GaugeServiceRepairHistory(request, lID):
    
    sCodeFinal1 = ""
    sCodeFinal2 = ""
 
    

    lPlantIdSelect = 0
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

    #semployeename = semployeeno + " | " + semployeename
    request.session['badmin'] =0
    request.session['badmin1'] = 0
    request.session['bstores'] = 0
    request.session['bcalibration'] = 0
    request.session['bservice'] = 0
    request.session['bmsa'] = 0
    request.session['bmasterlistonlyallplant'] = 1  
    request.session['breadonly'] =0
    sPlantCode = ""
    sCategoryCode = ""
    lcontinuousnob  = ""
    bFlow = 0
    sFlowName  = ""
    lcontinuousnoa  =0
    bFlow1 = 0
    sFlowName1  = ""
    lcontinuousnoa1  = 0
    bFlow2 = 0
    sFlowName2  = ""
    lcontinuousnoa2  =0
    bFlow3 = 0
    sFlowName3  = ""
    lcontinuousnoa3  =0
    bFlow4 = 0
    sFlowName4  = ""
    lcontinuousnoa4  =0
    bFlow5 = 0
    sFlowName5  = ""
    lcontinuousnoa5  =0
    bFlow6 = 0
    sFlowName6  = ""
    lcontinuousnoa6  =0
    bFlow7 = 0
    sFlowName7  = ""
    lcontinuousnoa7  =0
    bFlow8 = 0
    sFlowName8  = ""
    lcontinuousnoa8  =0
    bFlow9 = 0
    sFlowName9  = ""
    lcontinuousnoa9  =0
    bFlow10 = 0
    sFlowName10  = ""
    lcontinuousnoa10  =0
    
    bSAPCodeDone = 0
    bSAPCodeNotDone = 0

    cmbClassificationID = 0
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    

    sIssueDate3 = ""
    sIssueDate2 = ""
    sIssueDate1 = ""
    sIssueDate = "" 
    dtIssueDate = datetime.now()
    sIssueDate1 = str(datetime.now()) 
    sIssueDate = sIssueDate1[0:10]


    getFlow1Code = ""
    request.session['getFlow1Code']  =getFlow1Code
    getFlow2Code = ""
    request.session['getFlow2Code']  =getFlow2Code
    getFlow3Code = ""
    request.session['getFlow3Code']  =getFlow3Code
    getFlow4Code = ""
    request.session['getFlow4Code']  =getFlow4Code
    getFlow5Code = ""
    request.session['getFlow5Code']  =getFlow5Code
    getFlowContCode = ""
    request.session['getFlowContCode']  =getFlowContCode


    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
 
    request.session['sPlantCode']   =sPlantCode

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

   
      
    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
        sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
        sPlantNameNameA = AdminunitlistActive.splantname

    request.session['sPlantCode']   =sPlantCode
    
    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    if(sFlowName1 == "Part No1"):
        Adminassetcategorytypelist1_AddNewOBJ1 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
    else:
        Adminassetcategorytypelist1_AddNewOBJ1 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=1 ).values()
        
    if(sFlowName1 == "Part No1"):
        Adminassetcategorytypelist1_AddNewOBJ2 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
    else: 
        Adminassetcategorytypelist1_AddNewOBJ2 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=2 ).values()
        
    if(sFlowName1 == "Part No1"):
        Adminassetcategorytypelist1_AddNewOBJ3 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
    else:  
        Adminassetcategorytypelist1_AddNewOBJ3 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=3 ).values()

    if(sFlowName1 == "Part No1"):
        Adminassetcategorytypelist1_AddNewOBJ4 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
    else:  
        Adminassetcategorytypelist1_AddNewOBJ4 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=4 ).values()

    if(sFlowName1 == "Part No1"):
        Adminassetcategorytypelist1_AddNewOBJ5 =  Adminpartdetailslist.objects.filter(lcompanyid=lcompanyid).order_by('spartno').values()
    else:  
        Adminassetcategorytypelist1_AddNewOBJ5 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=5 ).values()

    Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
    
    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    lunitidA=request.session['lunitid']  
    AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

    Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(  lid=lID)

    
    

    Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



    return render(request, "CloudCaliber/GaugeServiceRepair.html", 
    {
        'Masterinstrumentslist_listA':Masterinstrumentslist_list, 
        
        'CurDateNow':datetime.now(),
        'lPlantId':lPlantId,  
        '30DateNow':datetime.now() + timedelta(days=30),  
        'AreaofUselist_list':AreaofUselist_list,
        'Adminunitlist_list':Adminunitlist_list,
        'title':'User list', 
        'message':'Your User list page.',
        'sPlantName': sPlantName , 
        'Location': 0 , 
        'semployeename':  semployeename,
        'txtSearch': "" , 
        'sCodeFinal1': "" ,  
        'sCodeFinal2': "" ,  
        'cmbClassificationID': 0 , 
        'cmbCategoryID': 0 ,  
        'cmbFlow1ID': 0 ,  
        'cmbFlow2ID': 0 ,  
        'cmbFlow3ID': 0 ,  
        'cmbFlow4ID': 0 ,
        'cmbFlow5ID': 0 ,     
        'cmbFlow1label': "",  
        'cmbFlow2label': "",  
        'cmbFlow3label': "",  
        'cmbFlow4label': "",
        'cmbFlow5label': "",  
        'bNewID': 0 ,  
        'Adminassettypelist_list':Adminassettypelist_list,
        'bSAPCodeDone': bSAPCodeDone, 
        'bSAPCodeNotDone': bSAPCodeNotDone,  
        'sIssueDate': sIssueDate, 
    }) 



