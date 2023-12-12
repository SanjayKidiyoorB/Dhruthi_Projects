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
from CloudCaliber import viewsdamaged
from CloudCaliber import viewsduelist
from CloudCaliber import viewsgaugeusagewise
from CloudCaliber import viewsissuereturn
from CloudCaliber import viewsmasterlist
from CloudCaliber import viewsmasterlistdetails
from CloudCaliber import viewsmsastudy
from CloudCaliber import viewsuserlist 
from CloudCaliber import viewscategorycreation

from CloudCaliber.models import Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist
 

def GaugeVerifications(request):
    return render(request, "CloudCaliber/GaugeVerifications.html")

def GaugeVerificationDue(request):
    return render(request, "CloudCaliber/GaugeVerificationDue.html") 

@csrf_exempt
def GaugeValidationList(request):




    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

    sCodeFinal1 = ""
    sCodeFinal2 = ""
 
    

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
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

    if request.method == "POST":


        data = request.POST
        if 'Classification' in request.POST:
            cmbClassificationID=request.POST['Classification'] 

        if 'Category' in request.POST:
            cmbCategoryID=request.POST['Category'] 

        if 'getFlow1' in request.POST:
            cmbgetFlow1ID=request.POST['getFlow1'] 



        request.session['cmbClassificationID'] =cmbClassificationID
        request.session['cmbCategoryID'] =cmbCategoryID
        request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
        request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
        request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
        request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
        request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
        request.session['cmbgetFlow6ID'] =cmbgetFlow6ID
        request.session['sCategoryCode'] = sCategoryCode
        request.session['lcontinuousnob'] = lcontinuousnob
        request.session['bFlow'] = bFlow
        request.session['sFlowName'] = sFlowName
        request.session['lcontinuousnoa'] = lcontinuousnoa
        request.session['bFlow1'] = bFlow1
        request.session['sFlowName1'] = sFlowName1
        request.session['lcontinuousnoa1'] = lcontinuousnoa1
        request.session['bFlow2'] = bFlow2
        request.session['sFlowName2'] = sFlowName2
        request.session['lcontinuousnoa2'] = lcontinuousnoa2
        request.session['bFlow3'] = bFlow3
        request.session['sFlowName3'] = sFlowName3
        request.session['lcontinuousnoa3'] = lcontinuousnoa3
        request.session['bFlow4'] = bFlow4
        request.session['sFlowName4'] = sFlowName4
        request.session['lcontinuousnoa4'] = lcontinuousnoa4
        request.session['bFlow5'] = bFlow5
        request.session['sFlowName5'] = sFlowName5
        request.session['lcontinuousnoa5'] = lcontinuousnoa5
        request.session['bFlow6'] = bFlow6
        request.session['sFlowName6'] = sFlowName6
        request.session['lcontinuousnoa6'] = lcontinuousnoa6
        request.session['bFlow7'] = bFlow7
        request.session['sFlowName7'] = sFlowName7
        request.session['lcontinuousnoa7'] = lcontinuousnoa7
        request.session['bFlow8'] = bFlow8
        request.session['sFlowName8'] = sFlowName8
        request.session['lcontinuousnoa8'] = lcontinuousnoa8
        request.session['bFlow9'] = bFlow9
        request.session['sFlowName9'] = sFlowName9
        request.session['lcontinuousnoa9'] = lcontinuousnoa9
        request.session['bFlow10'] = bFlow10
        request.session['sFlowName10'] = sFlowName10
        request.session['lcontinuousnoa10'] = lcontinuousnoa10
        
        request.session['sCategoryCode'] = sCategoryCode
        request.session['lcontinuousnob'] = lcontinuousnob
        request.session['bFlow'] = bFlow
        request.session['sFlowName'] = sFlowName
        request.session['lcontinuousnoa'] = lcontinuousnoa
        request.session['bFlow1'] = bFlow1
        request.session['sFlowName1'] = sFlowName1
        request.session['lcontinuousnoa1'] = lcontinuousnoa1
        request.session['bFlow2'] = bFlow2
        request.session['sFlowName2'] = sFlowName2
        request.session['lcontinuousnoa2'] = lcontinuousnoa2
        request.session['bFlow3'] = bFlow3
        request.session['sFlowName3'] = sFlowName3
        request.session['lcontinuousnoa3'] = lcontinuousnoa3
        request.session['bFlow4'] = bFlow4
        request.session['sFlowName4'] = sFlowName4
        request.session['lcontinuousnoa4'] = lcontinuousnoa4
        request.session['bFlow5'] = bFlow5
        request.session['sFlowName5'] = sFlowName5
        request.session['lcontinuousnoa5'] = lcontinuousnoa5
        request.session['bFlow6'] = bFlow6
        request.session['sFlowName6'] = sFlowName6
        request.session['lcontinuousnoa6'] = lcontinuousnoa6
        request.session['bFlow7'] = bFlow7
        request.session['sFlowName7'] = sFlowName7
        request.session['lcontinuousnoa7'] = lcontinuousnoa7
        request.session['bFlow8'] = bFlow8
        request.session['sFlowName8'] = sFlowName8
        request.session['lcontinuousnoa8'] = lcontinuousnoa8
        request.session['bFlow9'] = bFlow9
        request.session['sFlowName9'] = sFlowName9
        request.session['lcontinuousnoa9'] = lcontinuousnoa9
        request.session['bFlow10'] = bFlow10
        request.session['sFlowName10'] = sFlowName10
        request.session['lcontinuousnoa10'] = lcontinuousnoa10

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

        return render(request,  'CloudCaliber/GaugeMasterlistCreateID.html', 
        {
            'title':'User list', 
            'message':'Your User list page.',
            'year':datetime.now().year,
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
        })  
    else: 
         
        request.session['cmbClassificationID'] =cmbClassificationID
        request.session['cmbCategoryID'] =cmbCategoryID
        request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
        request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
        request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
        request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
        request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
        request.session['cmbgetFlow6ID'] =cmbgetFlow6ID
        
        request.session['sCategoryCode'] = sCategoryCode
        request.session['lcontinuousnob'] = lcontinuousnob
        request.session['bFlow'] = bFlow
        request.session['sFlowName'] = sFlowName
        request.session['lcontinuousnoa'] = lcontinuousnoa
        request.session['bFlow1'] = bFlow1
        request.session['sFlowName1'] = sFlowName1
        request.session['lcontinuousnoa1'] = lcontinuousnoa1
        request.session['bFlow2'] = bFlow2
        request.session['sFlowName2'] = sFlowName2
        request.session['lcontinuousnoa2'] = lcontinuousnoa2
        request.session['bFlow3'] = bFlow3
        request.session['sFlowName3'] = sFlowName3
        request.session['lcontinuousnoa3'] = lcontinuousnoa3
        request.session['bFlow4'] = bFlow4
        request.session['sFlowName4'] = sFlowName4
        request.session['lcontinuousnoa4'] = lcontinuousnoa4
        request.session['bFlow5'] = bFlow5
        request.session['sFlowName5'] = sFlowName5
        request.session['lcontinuousnoa5'] = lcontinuousnoa5
        request.session['bFlow6'] = bFlow6
        request.session['sFlowName6'] = sFlowName6
        request.session['lcontinuousnoa6'] = lcontinuousnoa6
        request.session['bFlow7'] = bFlow7
        request.session['sFlowName7'] = sFlowName7
        request.session['lcontinuousnoa7'] = lcontinuousnoa7
        request.session['bFlow8'] = bFlow8
        request.session['sFlowName8'] = sFlowName8
        request.session['lcontinuousnoa8'] = lcontinuousnoa8
        request.session['bFlow9'] = bFlow9
        request.session['sFlowName9'] = sFlowName9
        request.session['lcontinuousnoa9'] = lcontinuousnoa9
        request.session['bFlow10'] = bFlow10
        request.session['sFlowName10'] = sFlowName10
        request.session['lcontinuousnoa10'] = lcontinuousnoa10

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

        return render(request,  'CloudCaliber/GaugeMasterlistCreateID.html', 
        {
            'title':'User list', 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
        })



@csrf_exempt
def GMlistClassificationValidationCreate_ID(request):
    cmbClassificationID = request.GET.get('cmbClassificationID', None)
    data = { 
        'is_taken1': Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    } 
        #data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


    
@csrf_exempt
def load_GMlistClassificationValidationCreate_ID(request):

    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

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




    cmbClassificationID = request.GET.get('cmbClassificationID')
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

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode'] 
    request.session['sClassificationCode']=""
    
    Adminassettypelist_listA =  Adminassetcategorytypelist.objects.get(lcategorytypeid=cmbClassificationID)
    request.session['sClassificationCode']=Adminassettypelist_listA.scode
    sClassificationCode=request.session['sClassificationCode']
    sCodeFinal1=sClassificationCode
    sCodeFinal2=sClassificationCode + "-" + sPlantCode + "001"
 
    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
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
    
        #data['error_message'] = 'A user with this username already exists.'
    
    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    request.session['sCategoryCode'] = sCategoryCode
    request.session['lcontinuousnob'] = lcontinuousnob
    request.session['bFlow'] = bFlow
    request.session['sFlowName'] = sFlowName
    request.session['lcontinuousnoa'] = lcontinuousnoa
    request.session['bFlow1'] = bFlow1
    request.session['sFlowName1'] = sFlowName1
    request.session['lcontinuousnoa1'] = lcontinuousnoa1
    request.session['bFlow2'] = bFlow2
    request.session['sFlowName2'] = sFlowName2
    request.session['lcontinuousnoa2'] = lcontinuousnoa2
    request.session['bFlow3'] = bFlow3
    request.session['sFlowName3'] = sFlowName3
    request.session['lcontinuousnoa3'] = lcontinuousnoa3
    request.session['bFlow4'] = bFlow4
    request.session['sFlowName4'] = sFlowName4
    request.session['lcontinuousnoa4'] = lcontinuousnoa4
    request.session['bFlow5'] = bFlow5
    request.session['sFlowName5'] = sFlowName5
    request.session['lcontinuousnoa5'] = lcontinuousnoa5
    request.session['bFlow6'] = bFlow6
    request.session['sFlowName6'] = sFlowName6
    request.session['lcontinuousnoa6'] = lcontinuousnoa6
    request.session['bFlow7'] = bFlow7
    request.session['sFlowName7'] = sFlowName7
    request.session['lcontinuousnoa7'] = lcontinuousnoa7
    request.session['bFlow8'] = bFlow8
    request.session['sFlowName8'] = sFlowName8
    request.session['lcontinuousnoa8'] = lcontinuousnoa8
    request.session['bFlow9'] = bFlow9
    request.session['sFlowName9'] = sFlowName9
    request.session['lcontinuousnoa9'] = lcontinuousnoa9
    request.session['bFlow10'] = bFlow10
    request.session['sFlowName10'] = sFlowName10
    request.session['lcontinuousnoa10'] = lcontinuousnoa10


    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'cmbClassificationID':cmbClassificationID,
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj,
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                         
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })


        
    
@csrf_exempt
def load_GMlisCategoryValidationCreate_ID(request):

    
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


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
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
    

        #data['error_message'] = 'A user with this username already exists.'
    

    AdminassetcategorylistActive = Adminassetcategorylist.objects.get(lcategoryid=cmbCategoryID)
    sCategoryCode = AdminassetcategorylistActive.scode
    lcontinuousnob  = AdminassetcategorylistActive.lcontinuousnob
    lcontinuousnoa  = AdminassetcategorylistActive.lcontinuousnoa
     

    request.session['btyperefascontinuousnoa'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa == 1):
        request.session['btyperefascontinuousnoa'] = 1        
        request.session['bContFlag'] = 1
        

    request.session['btyperefascontinuousnoa1'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa1 == 1):
        request.session['btyperefascontinuousnoa1'] = 1

    request.session['btyperefascontinuousnoa2'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa2 == 1):
        request.session['btyperefascontinuousnoa2'] = 1

    request.session['btyperefascontinuousnoa3'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa3 == 1):
        request.session['btyperefascontinuousnoa3'] = 1

    request.session['btyperefascontinuousnoa4'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa4 == 1):
        request.session['btyperefascontinuousnoa4'] = 1

    request.session['btyperefascontinuousnoa5'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa5 == 1):
        request.session['btyperefascontinuousnoa5'] = 1

    request.session['btyperefascontinuousnoa6'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa6 == 1):
        request.session['btyperefascontinuousnoa6'] = 1

    request.session['btyperefascontinuousnoa7'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa7 == 1):
        request.session['btyperefascontinuousnoa7'] = 1

    request.session['btyperefascontinuousnoa8'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa8 == 1):
        request.session['btyperefascontinuousnoa8'] = 1

    request.session['btyperefascontinuousnoa9'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa9 == 1):
        request.session['btyperefascontinuousnoa9'] = 1

    request.session['btyperefascontinuousnoa10'] = 0
    if (AdminassetcategorylistActive.btyperefascontinuousnoa10 == 1):
        request.session['btyperefascontinuousnoa10'] = 1



    sFlowName1  = AdminassetcategorylistActive.styperefname1
    if (sFlowName1 != ""):
        bFlow1 = 1

    sFlowName2  = AdminassetcategorylistActive.styperefname2
    if (sFlowName2 != ""):
        bFlow2 = 1

    sFlowName3  = AdminassetcategorylistActive.styperefname3
    if (sFlowName3 != ""):
        bFlow3 = 1

    sFlowName4  = AdminassetcategorylistActive.styperefname4
    if (sFlowName4 != ""):
        bFlow4 = 1

    sFlowName5  = AdminassetcategorylistActive.styperefname5
    if (sFlowName5 != ""):
        bFlow5 = 1

    sFlowName6  = AdminassetcategorylistActive.styperefname6
    if (sFlowName6 != ""):
        bFlow6 = 1

    sFlowName7  = AdminassetcategorylistActive.styperefname7
    if (sFlowName7 != ""):
        bFlow7 = 1

    sFlowName8  = AdminassetcategorylistActive.styperefname8
    if (sFlowName8 != ""):
        bFlow8 = 1
    
    sFlowName9  = AdminassetcategorylistActive.styperefname9
    if (sFlowName9 != ""):
        bFlow9 = 1

    sFlowName10  = AdminassetcategorylistActive.styperefname10 
    if (sFlowName10 != ""):
        bFlow10 = 1
    
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']  
    request.session['sCategoryCode']=""
      
    request.session['sCategoryCode']=sCategoryCode
    sClassificationCode=request.session['sClassificationCode']
    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + "-" + sPlantCode[:2] + sRunningNo




    request.session['cmbClassificationID'] =cmbClassificationID
    request.session['cmbCategoryID'] =cmbCategoryID
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    request.session['cmbgetFlow6ID'] =cmbgetFlow6ID

    request.session['sCategoryCode'] = sCategoryCode
    request.session['lcontinuousnob'] = lcontinuousnob
    request.session['bFlow'] = bFlow
    request.session['sFlowName'] = sFlowName
    request.session['lcontinuousnoa'] = lcontinuousnoa
    request.session['bFlow1'] = bFlow1
    request.session['sFlowName1'] = sFlowName1
    request.session['lcontinuousnoa1'] = lcontinuousnoa1
    request.session['bFlow2'] = bFlow2
    request.session['sFlowName2'] = sFlowName2
    request.session['lcontinuousnoa2'] = lcontinuousnoa2
    request.session['bFlow3'] = bFlow3
    request.session['sFlowName3'] = sFlowName3
    request.session['lcontinuousnoa3'] = lcontinuousnoa3
    request.session['bFlow4'] = bFlow4
    request.session['sFlowName4'] = sFlowName4
    request.session['lcontinuousnoa4'] = lcontinuousnoa4
    request.session['bFlow5'] = bFlow5
    request.session['sFlowName5'] = sFlowName5
    request.session['lcontinuousnoa5'] = lcontinuousnoa5
    request.session['bFlow6'] = bFlow6
    request.session['sFlowName6'] = sFlowName6
    request.session['lcontinuousnoa6'] = lcontinuousnoa6
    request.session['bFlow7'] = bFlow7
    request.session['sFlowName7'] = sFlowName7
    request.session['lcontinuousnoa7'] = lcontinuousnoa7
    request.session['bFlow8'] = bFlow8
    request.session['sFlowName8'] = sFlowName8
    request.session['lcontinuousnoa8'] = lcontinuousnoa8
    request.session['bFlow9'] = bFlow9
    request.session['sFlowName9'] = sFlowName9
    request.session['lcontinuousnoa9'] = lcontinuousnoa9
    request.session['bFlow10'] = bFlow10
    request.session['sFlowName10'] = sFlowName10
    request.session['lcontinuousnoa10'] = lcontinuousnoa10
    
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })


    
@csrf_exempt
def load_GMlisFlow1ValidationCreate_ID(request):

    
    request.session['getFlow1Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode']


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow1ID = request.GET.get('cmbgetFlow1ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']
 
    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow1ID)
    getFlow1Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow1Code'] = getFlow1Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (request.session['bContFlag'] != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")  + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "") + sContiNo.replace(" ", "")  + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow1ID = request.GET.get('cmbgetFlow1ID')
  

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    cmbgetFlow2ID =request.session['cmbgetFlow2ID'] 
    cmbgetFlow3ID = request.session['cmbgetFlow3ID'] 
    cmbgetFlow4ID =request.session['cmbgetFlow4ID']
    cmbgetFlow5ID = request.session['cmbgetFlow5ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()

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
    

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })








@csrf_exempt
def load_GMlisFlow2ValidationCreate_ID(request):

    request.session['getFlow2Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode'] 


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow2ID = request.GET.get('cmbgetFlow2ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']


    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow2ID)
    getFlow2Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow2Code'] = getFlow2Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (request.session['bContFlag'] != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  
  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")  + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "") + sContiNo.replace(" ", "")  + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow2ID = request.GET.get('cmbgetFlow2ID')
 

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
    cmbgetFlow1ID =request.session['cmbgetFlow1ID'] 
    cmbgetFlow3ID = request.session['cmbgetFlow3ID'] 
    cmbgetFlow4ID =request.session['cmbgetFlow4ID']
    cmbgetFlow5ID = request.session['cmbgetFlow5ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    
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
    

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })







@csrf_exempt
def load_GMlisFlow3ValidationCreate_ID(request):

    
    request.session['getFlow3Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode']


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow3ID = request.GET.get('cmbgetFlow3ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']


    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow3ID)
    getFlow3Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow3Code'] = getFlow3Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (request.session['bContFlag'] != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  
  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")  + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "") + sContiNo.replace(" ", "")  + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow3ID = request.GET.get('cmbgetFlow3ID')
 

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
    cmbgetFlow2ID =request.session['cmbgetFlow2ID'] 
    cmbgetFlow1ID = request.session['cmbgetFlow1ID'] 
    cmbgetFlow4ID =request.session['cmbgetFlow4ID']
    cmbgetFlow5ID = request.session['cmbgetFlow5ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    
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
    

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })





@csrf_exempt
def load_GMlisFlow4ValidationCreate_ID(request):

    
    request.session['getFlow4Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode']


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow4ID = request.GET.get('cmbgetFlow4ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']


    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow4ID)
    getFlow4Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow4Code'] = getFlow4Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (request.session['bContFlag'] != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  
  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")  + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")  + sContiNo.replace(" ", "")  + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow4ID = request.GET.get('cmbgetFlow4ID')

    request.session['getFlow1Code'] = getFlow1Code

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
    cmbgetFlow2ID =request.session['cmbgetFlow2ID'] 
    cmbgetFlow3ID = request.session['cmbgetFlow3ID'] 
    cmbgetFlow1ID =request.session['cmbgetFlow1ID']
    cmbgetFlow5ID = request.session['cmbgetFlow5ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    
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
    
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })







@csrf_exempt
def load_GMlisFlow5ValidationCreate_ID(request):

    
    request.session['getFlow5Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode']


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow5ID = request.GET.get('cmbgetFlow5ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']


    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow5ID)
    getFlow5Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow5Code'] = getFlow5Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (request.session['bContFlag'] != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "")  + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "") + sContiNo.replace(" ", "")   + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow5ID = request.GET.get('cmbgetFlow5ID')

    request.session['getFlow1Code'] = getFlow1Code

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
    cmbgetFlow2ID =request.session['cmbgetFlow2ID'] 
    cmbgetFlow3ID = request.session['cmbgetFlow3ID'] 
    cmbgetFlow4ID =request.session['cmbgetFlow4ID']
    cmbgetFlow1ID = request.session['cmbgetFlow1ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    
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
    

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })







@csrf_exempt
def load_GMlisFlow6ValidationCreate_ID(request):

    
    request.session['getFlow6Code']  = ""
    getFlow1Code = ""
    getFlow1Code =request.session['getFlow1Code']  
    getFlow2Code = ""
    getFlow2Code = request.session['getFlow2Code'] 
    getFlow3Code = ""
    getFlow3Code =request.session['getFlow3Code'] 
    getFlow4Code = ""
    getFlow4Code =request.session['getFlow4Code'] 
    getFlow5Code = ""
    getFlow5Code =request.session['getFlow5Code'] 
    getFlowContCode = ""
    getFlowContCode =request.session['getFlowContCode']


    sCodeFinal1 = ""
    sCodeFinal2 = ""

    sPlantCode = ""
    sPlantCode=request.session['sPlantCode']  

    bContFlag = 0
    request.session['bContFlag'] =bContFlag

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    cmbClassificationID = request.session['cmbClassificationID']
    cmbCategoryID = 0
    cmbgetFlow1ID = 0
    cmbgetFlow2ID = 0
    cmbgetFlow3ID = 0
    cmbgetFlow4ID = 0
    cmbgetFlow5ID = 0
    cmbgetFlow6ID = 0
    cmbCategoryID = request.GET.get('cmbCategoryID')
    cmbgetFlow1ID = request.GET.get('cmbgetFlow1ID')
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




    AdminunitlistActive =  Adminunitlist.objects.get(lplantid=lPlantId)
    sPlantCode = AdminunitlistActive.splantno
     
 
        #data['error_message'] = 'A user with this username already exists.'
    




     
    lRunningNo = 0
    lContiNo = 0


    sClassificationCode = ""
    sPlantCode=request.session['sPlantCode']   
      
    sCategoryCode=request.session['sCategoryCode']
    sClassificationCode=request.session['sClassificationCode']


    Adminassetcategorytypelist1Active = Adminassetcategorytypelist1.objects.get(lcategorytypeid=cmbgetFlow1ID)
    getFlow1Code = Adminassetcategorytypelist1Active.scode

    request.session['getFlow1Code'] = getFlow1Code


    sCodeFinal1=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "")   


    sRunningNo =""
    sContiNo =""

    AdminassetcontinuousformatlistActive = Adminassetcontinuousformatlist.objects.filter(scontinuousformat=sCodeFinal1).values()
    if AdminassetcontinuousformatlistActive:
        lContiNo = AdminassetcontinuousformatlistActive.lcontinuousformat

    lContiNo  = lContiNo +1

    sContiNo=str(lContiNo)
    if(len(sContiNo)==1):
        sContiNo = "00"+sContiNo
    if(len(sContiNo)==2):
        sContiNo = "0"+sContiNo

    if (lcontinuousnoa1 != 0):
        request.session['bContFlag'] = 1
        request.session['getFlowContCode'] = sContiNo  
    else:
        sContiNo = ""
        sContiNo = request.session['getFlowContCode']  

  

    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode=sCodeFinal1).values()
    if AdminassetserialformatlistActive:
        lRunningNo = AdminassetserialformatlistActive.lserialno
    
    lRunningNo  = lRunningNo   +1


    sRunningNo = str(lRunningNo) 
    if(len(sRunningNo)==1):
        sRunningNo = "00"+sRunningNo
    if(len(sRunningNo)==2):
        sRunningNo = "0"+sRunningNo



    sCodeFinal2=sClassificationCode.replace(" ", "") + sCategoryCode.replace(" ", "") + getFlow1Code.replace(" ", "") + getFlow2Code.replace(" ", "")  + getFlow3Code.replace(" ", "") + getFlow4Code.replace(" ", "")  + getFlow5Code.replace(" ", "") + sContiNo.replace(" ", "")  + "-" + sPlantCode[:2] + sRunningNo




    cmbgetFlow1ID = request.GET.get('cmbgetFlow1ID')

    request.session['getFlow1Code'] = getFlow1Code

    cmbClassificationID =request.session['cmbClassificationID'] 
    cmbCategoryID = request.session['cmbCategoryID'] 
    request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
    cmbgetFlow2ID =request.session['cmbgetFlow2ID'] 
    cmbgetFlow3ID = request.session['cmbgetFlow3ID'] 
    cmbgetFlow4ID =request.session['cmbgetFlow4ID']
    cmbgetFlow5ID = request.session['cmbgetFlow5ID']
    cmbgetFlow6ID = request.session['cmbgetFlow6ID']


    sCategoryCode = request.session['sCategoryCode']
    lcontinuousnob = request.session['lcontinuousnob']
    bFlow = request.session['bFlow']
    sFlowName = request.session['sFlowName']
    lcontinuousnoa = request.session['lcontinuousnoa']

    bFlow1 = request.session['bFlow1']
    sFlowName1 = request.session['sFlowName1']
    lcontinuousnoa1 = request.session['lcontinuousnoa1']

    bFlow2 = request.session['bFlow2']
    sFlowName2 = request.session['sFlowName2']
    lcontinuousnoa2 = request.session['lcontinuousnoa2']

    bFlow3 = request.session['bFlow3']
    sFlowName3 = request.session['sFlowName3']
    lcontinuousnoa3 = request.session['lcontinuousnoa3']

    bFlow4 = request.session['bFlow4']
    sFlowName4 = request.session['sFlowName4']
    lcontinuousnoa4 = request.session['lcontinuousnoa4']

    bFlow5 = request.session['bFlow5']
    sFlowName5 = request.session['sFlowName5']
    lcontinuousnoa5 = request.session['lcontinuousnoa5']

    bFlow6 = request.session['bFlow6']
    sFlowName6 = request.session['sFlowName6']
    lcontinuousnoa6 = request.session['lcontinuousnoa6']

    bFlow7 = request.session['bFlow7']
    sFlowName7 = request.session['sFlowName7']
    lcontinuousnoa7 = request.session['lcontinuousnoa7']

    bFlow8 = request.session['bFlow8']
    sFlowName8 = request.session['sFlowName8']
    lcontinuousnoa8 = request.session['lcontinuousnoa8']

    bFlow9 = request.session['bFlow9']
    sFlowName9 = request.session['sFlowName9']
    lcontinuousnoa9 = request.session['lcontinuousnoa9']

    bFlow10 = request.session['bFlow10']
    sFlowName10 = request.session['sFlowName10']
    lcontinuousnoa10 = request.session['lcontinuousnoa10']
 
    cmbCategoryID = request.session['cmbCategoryID'] 

    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
    Adminassetcategorylistobj = Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()

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

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,      
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Adminassetcategorytypelist1_AddNewOBJ1': Adminassetcategorytypelist1_AddNewOBJ1, 
            'Adminassetcategorytypelist1_AddNewOBJ2': Adminassetcategorytypelist1_AddNewOBJ2, 
            'Adminassetcategorytypelist1_AddNewOBJ3': Adminassetcategorytypelist1_AddNewOBJ3, 
            'Adminassetcategorytypelist1_AddNewOBJ4': Adminassetcategorytypelist1_AddNewOBJ4, 
            'Adminassetcategorytypelist1_AddNewOBJ5': Adminassetcategorytypelist1_AddNewOBJ5, 
            'Adminassetcategorytypelist1_AddNewOBJ6': Adminassetcategorytypelist1_AddNewOBJ6,
            'Adminassetcategorylistobj': Adminassetcategorylistobj, 
                                        'SelectedSeries0':"0",
                                        'SelectedSeries1':"1",
                                        'SelectedSeries2':"2",
                                        'SelectedSeries3':"3",
                                        'SelectedSeries4':"4",
                                        'SelectedSeries5':"5",
                                        'SelectedSeries6':"6",
                                        'SelectedSeries7':"7",
                                        'SelectedSeries8':"8",
                                        'SelectedSeries9':"9",
                                        'SelectedSeries10':"10",
                                        'SelectedSeries11':"11",
                                        'SelectedSeries12':"12",
                                        'SelectedSeries13':"13",
                                        'SelectedSeries14':"14",
                                        'SelectedSeries15':"15",
                                        'SelectedSeries16':"16",                                    
                                            'sCategoryCode': sCategoryCode,
                                            'lcontinuousnob': lcontinuousnob,
                                            'bFlow': bFlow,
                                            'sFlowName' : sFlowName,
                                            'lcontinuousnoa': lcontinuousnoa, 

                                            'bFlow1': bFlow1,
                                            'sFlowName1' : sFlowName1,
                                            'lcontinuousnoa1': lcontinuousnoa1, 
                                            'bFlow2': bFlow2,
                                            'sFlowName2' : sFlowName2,
                                            'lcontinuousnoa2': lcontinuousnoa2, 
                                            'bFlow3': bFlow3,
                                            'sFlowName3' : sFlowName3,
                                            'lcontinuousnoa3': lcontinuousnoa3, 
                                            'bFlow4': bFlow4,
                                            'sFlowName4' : sFlowName4,
                                            'lcontinuousnoa4': lcontinuousnoa4, 
                                            'bFlow5': bFlow5,
                                            'sFlowName5' : sFlowName5,
                                            'lcontinuousnoa5': lcontinuousnoa5, 
                                            'bFlow6': bFlow6,
                                            'sFlowName6' : sFlowName6,
                                            'lcontinuousnoa6': lcontinuousnoa6, 
                                            'bFlow7': bFlow7,
                                            'sFlowName7' : sFlowName7,
                                            'lcontinuousnoa7': lcontinuousnoa7, 
                                            'bFlow8': bFlow8,
                                            'sFlowName8' : sFlowName8,
                                            'lcontinuousnoa8': lcontinuousnoa8, 
                                            'bFlow9': bFlow9,
                                            'sFlowName9' : sFlowName9,
                                            'lcontinuousnoa9': lcontinuousnoa9, 
                                            'bFlow10': bFlow10,
                                            'sFlowName10' : sFlowName10,
                                            'lcontinuousnoa10': lcontinuousnoa10, 
            
        })






 