from django.shortcuts import render
import os
import re
import calendar
from calendar import HTMLCalendar

from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect


import cloudcaliber_project.settings 
#import textutils.settings



import threading as th
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from CloudCaliber.models import Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist

from CloudCaliber.serializers import   AdminuserlistSerializer

@csrf_exempt
def home(request):
    # print(request.POST)

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
    

    CurDateFrom = datetime.today().strftime('%Y-%m-%d')
    request.session['CurDateFrom']  = CurDateFrom
    request.session['CurDateTo']  = CurDateFrom
    request.session['CurDateFromD']  = ""
    request.session['CurDateFromO']  = ""

    request.session['CurDateFromD']  = CurDateFrom
    if request.method == "POST":
        data = request.POST 
        
        lUnitId = 0
        lUnitId1 = 0

        #if request.session:
            #request.session.clear()
        sUnitName = ""
        if 'Plant' in request.POST:
            
            cmbPlant=request.POST['Plant'] #('Machine')
            lUnitId = int(cmbPlant)
            Adminunitlist_AddNewOBJ = Adminunitlist.objects.get(lplantid=lUnitId) 
            if Adminunitlist_AddNewOBJ: 
                sUnitName =  Adminunitlist_AddNewOBJ.splantno + " | " +   Adminunitlist_AddNewOBJ.splantname 
                #sUnitName = "(" + Adminunitlist_AddNewOBJ.splantno + ") " +  Adminunitlist_AddNewOBJ.splantname


        else:       
            
            AdminuserlistPWDAdmin = Adminuserlist.objects.filter(semployeeno=data.get("your_name"), spassword=data.get("your_Password")).values()
            if AdminuserlistPWDAdmin:
                for AdminuserlistPWDAdminA in AdminuserlistPWDAdmin.all():     
                    
                    lUnitId = 0
                    lUnitId1 = 0
                    lunitidDB ="0"
                    lunitidDBCheck ="0"
                    AdminuserlistActive = Adminuserlist.objects.filter(luserid=AdminuserlistPWDAdminA['luserid'],bactive=1,badmin=1).values()
                    if AdminuserlistActive:  
                        lUnitId = 0
                        lUnitId =AdminuserlistPWDAdminA['lunitid'] 
                        lUnitId1 = lUnitId
                        request.session['lCategoryID'] = 0                        
                        request.session['lLoginUserId'] = AdminuserlistPWDAdminA['luserid']
                        request.session['semployeename'] = AdminuserlistPWDAdminA['semployeename']
                        request.session['semployeeno'] = AdminuserlistPWDAdminA['semployeeno']
                        request.session['lunitid'] = lUnitId
                        request.session['sunitno'] = sUnitName
                        request.session['lcompanyid'] = AdminuserlistPWDAdminA['lcompanyid']
                        request.session['scompantname'] = AdminuserlistPWDAdminA['scompanyname']
                        request.session['semailaddress'] = AdminuserlistPWDAdminA['semailaddress']
                        request.session['smobile'] = AdminuserlistPWDAdminA['smobile']
                        request.session['badmin'] = 1
                        request.session['badmin1'] = 1
                        request.session['bstores'] = 0
                        request.session['bcalibration'] = 0
                        request.session['bservice'] = 0
                        request.session['bmsa'] = 0
                        request.session['bmasterlistonlyallplant'] = 0  
                        request.session['breadonly'] =0
                        return AdministratorDashboardA(request) 
                    else:

                        AdminuserlistActive1 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDAdminA['luserid'],bactive=1,bmasterlistonlyallplant=1).values()
                        if AdminuserlistActive1:  
                             
                            request.session['lCategoryID'] = 0                        
                            request.session['lLoginUserId'] = AdminuserlistPWDAdminA['luserid']
                            request.session['semployeename'] = AdminuserlistPWDAdminA['semployeename']
                            request.session['semployeeno'] = AdminuserlistPWDAdminA['semployeeno']
                            request.session['lunitid'] = lUnitId
                            request.session['sunitno'] = sUnitName
                            request.session['lcompanyid'] = AdminuserlistPWDAdminA['lcompanyid']
                            request.session['scompantname'] = AdminuserlistPWDAdminA['scompanyname']
                            request.session['semailaddress'] = AdminuserlistPWDAdminA['semailaddress']
                            request.session['smobile'] = AdminuserlistPWDAdminA['smobile']
                            request.session['badmin'] = 0
                            request.session['badmin1'] = 0
                            request.session['bstores'] = 0
                            request.session['bcalibration'] = 0
                            request.session['bservice'] = 0
                            request.session['bmsa'] = 0
                            request.session['bmasterlistonlyallplant'] = 1 
                            request.session['breadonly'] =0
                            return redirect('PlantAssetViewDashboard') 



                    
                        else: 

                            messages.error(request, 'Plant is not selected. Please Select and then try!')
                            Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
                            return render(request, "CloudCaliber/home.html", 
                                {
                                                    'title':'Issue list', 
                                                    'message':'Your Issue list page.',
                                                    'year':datetime.now().year,   
                                                    'Adminunitlist_list': Adminunitlist_list
                                }
                                                )

            else:

                messages.error(request, 'Plant is not selected. Please Select and then try!')
                Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
                return render(request, "CloudCaliber/home.html", 
                    {
                                        'title':'Issue list', 
                                        'message':'Your Issue list page.',
                                        'year':datetime.now().year,   
                                        'Adminunitlist_list': Adminunitlist_list
                    }
                                        )

        Adminuserlists = Adminuserlist.objects.filter(semployeeno=data.get("your_name")).values()
        if Adminuserlists:
            AdminuserlistPWD = Adminuserlist.objects.filter(semployeeno=data.get("your_name"), spassword=data.get("your_Password")).values()
            if AdminuserlistPWD:
                for AdminuserlistPWDOBJ in AdminuserlistPWD.all():                    
                     
                    lUnitId1 = 0
                    lunitidDB ="0"
                    lunitidDBCheck ="0"
                    AdminuserlistActive = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,badmin=1).values()
                    if AdminuserlistActive:   
                        lUnitId =int(cmbPlant )
                        lUnitId1 = lUnitId
                        request.session['lCategoryID'] = 0                        
                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                        request.session['lunitid'] = lUnitId
                        request.session['sunitno'] = sUnitName
                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                        request.session['badmin'] = 1
                        request.session['badmin1'] = 1
                        request.session['bstores'] = 0
                        request.session['bcalibration'] = 0
                        request.session['bservice'] = 0
                        request.session['bmsa'] = 0
                        request.session['bmasterlistonlyallplant'] = 0  
                        request.session['breadonly'] =0 
                        return redirect('Dashboard') 

                    else:
                        AdminuserlistActive1 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,bmasterlistonlyallplant=1).values()
                        if AdminuserlistActive1:  
                                 
                                request.session['lCategoryID'] = 0                        
                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                request.session['lunitid'] = lUnitId
                                request.session['sunitno'] = sUnitName
                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                request.session['badmin'] = 0
                                request.session['badmin1'] = 0
                                request.session['bstores'] = 0
                                request.session['bcalibration'] = 0
                                request.session['bservice'] = 0
                                request.session['bmsa'] = 0
                                request.session['bmasterlistonlyallplant'] = 1 
                                request.session['breadonly'] =0
                                return redirect('PlantAssetViewDashboard') 

                        else:
                            AdminuserlistActive2 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant11=lUnitId, ballfeatures1=1).values()
                            if AdminuserlistActive2:  
                                     
                                    request.session['lCategoryID'] = 0                        
                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                    request.session['lunitid'] = lUnitId
                                    request.session['sunitno'] = sUnitName
                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                    request.session['badmin'] = 0
                                    request.session['badmin1'] = 0
                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores1']
                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration1']
                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice1']
                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa1']
                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly1']
                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures1']
                                    request.session['bmasterlistonlyallplant'] = 0                                             
                                    if(AdminuserlistPWDOBJ['bstores1'] == 1):
                                        return redirect('Dashboard') 
                                    elif(AdminuserlistPWDOBJ['bcalibration1'] == 1):
                                        return redirect('Dashboard') 
                                    elif(AdminuserlistPWDOBJ['bservice1'] == 1):
                                        return redirect('Dashboard') 
                                    elif(AdminuserlistPWDOBJ['bmsa1'] == 1):
                                        return redirect('Dashboard') 
                                    elif(AdminuserlistPWDOBJ['breadonly1'] == 1):
                                        return redirect('Dashboard') 
                                    elif(AdminuserlistPWDOBJ['ballfeatures1'] == 1):
                                        return redirect('Dashboard') 
                                    else:
                                        return redirect('PlantAssetViewDashboard') 

                            else:
                                AdminuserlistActive3 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant12=lUnitId, ballfeatures2=1).values()
                                if AdminuserlistActive3:  
                                         
                                        request.session['lCategoryID'] = 0                        
                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                        request.session['lunitid'] = lUnitId
                                        request.session['sunitno'] = sUnitName
                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                        request.session['badmin'] = 0
                                        request.session['badmin1'] = 0
                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores2']
                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration2']
                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice2']
                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa2']
                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly2']
                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures2']
                                        request.session['bmasterlistonlyallplant'] = 0                                          
                                        if(AdminuserlistPWDOBJ['bstores2'] == 1):
                                            return redirect('Dashboard') 
                                        elif(AdminuserlistPWDOBJ['bcalibration2'] == 1):
                                            return redirect('Dashboard') 
                                        elif(AdminuserlistPWDOBJ['bservice2'] == 1):
                                            return redirect('Dashboard') 
                                        elif(AdminuserlistPWDOBJ['bmsa2'] == 1):
                                            return redirect('Dashboard') 
                                        elif(AdminuserlistPWDOBJ['breadonly2'] == 1):
                                            return redirect('Dashboard') 
                                        elif(AdminuserlistPWDOBJ['ballfeatures2'] == 1):
                                            return redirect('Dashboard') 
                                        else:
                                            return redirect('PlantAssetViewDashboard') 
        
                                else:	
                                    AdminuserlistActive4 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant13=lUnitId, ballfeatures3=1).values()
                                    if AdminuserlistActive4:  
                                             
                                            request.session['lCategoryID'] = 0                        
                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                            request.session['lunitid'] = lUnitId
                                            request.session['sunitno'] = sUnitName
                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                            request.session['badmin'] = 0
                                            request.session['badmin1'] = 0
                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores3']
                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration3']
                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice3']
                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa3']
                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly3']
                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures3']
                                            request.session['bmasterlistonlyallplant'] = 0                                          
                                            if(AdminuserlistPWDOBJ['bstores3'] == 1):
                                                return redirect('Dashboard') 
                                            elif(AdminuserlistPWDOBJ['bcalibration3'] == 1):
                                                return redirect('Dashboard') 
                                            elif(AdminuserlistPWDOBJ['bservice3'] == 1):
                                                return redirect('Dashboard') 
                                            elif(AdminuserlistPWDOBJ['bmsa3'] == 1):
                                                return redirect('Dashboard') 
                                            elif(AdminuserlistPWDOBJ['breadonly3'] == 1):
                                                return redirect('Dashboard') 
                                            elif(AdminuserlistPWDOBJ['ballfeatures3'] == 1):
                                                return redirect('Dashboard') 
                                            else:
                                                return redirect('PlantAssetViewDashboard') 


                                    else:	
                                        AdminuserlistActive4A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant14=lUnitId, ballfeatures4=1).values()
                                        if AdminuserlistActive4A:  
                                                 
                                                request.session['lCategoryID'] = 0                        
                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                request.session['lunitid'] = lUnitId
                                                request.session['sunitno'] = sUnitName
                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                request.session['badmin'] = 0
                                                request.session['badmin1'] = 0
                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores4']
                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration4']
                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice4']
                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa4']
                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly4']
                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures4']
                                                request.session['bmasterlistonlyallplant'] = 0
                                                if(AdminuserlistPWDOBJ['bstores4'] == 1):
                                                    return redirect('Dashboard') 
                                                elif(AdminuserlistPWDOBJ['bcalibration4'] == 1):
                                                    return redirect('Dashboard') 
                                                elif(AdminuserlistPWDOBJ['bservice4'] == 1):
                                                    return redirect('Dashboard') 
                                                elif(AdminuserlistPWDOBJ['bmsa4'] == 1):
                                                    return redirect('Dashboard') 
                                                elif(AdminuserlistPWDOBJ['breadonly4'] == 1):
                                                    return redirect('Dashboard') 
                                                elif(AdminuserlistPWDOBJ['ballfeatures4'] == 1):
                                                    return redirect('Dashboard') 
                                                else:
                                                    return redirect('PlantAssetViewDashboard') 


                                        else:	
                                            AdminuserlistActive5A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant15=lUnitId, ballfeatures5=1).values()
                                            if AdminuserlistActive5A:  
                                                     
                                                    request.session['lCategoryID'] = 0                        
                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                    request.session['lunitid'] = lUnitId
                                                    request.session['sunitno'] = sUnitName
                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                    request.session['badmin'] = 0
                                                    request.session['badmin1'] = 0
                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores5']
                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration5']
                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice5']
                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa5']
                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly5']
                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures5']
                                                    request.session['bmasterlistonlyallplant'] = 0
                                                    if(AdminuserlistPWDOBJ['bstores5'] == 1):
                                                        return redirect('Dashboard') 
                                                    elif(AdminuserlistPWDOBJ['bcalibration5'] == 1):
                                                        return redirect('Dashboard') 
                                                    elif(AdminuserlistPWDOBJ['bservice5'] == 1):
                                                        return redirect('Dashboard') 
                                                    elif(AdminuserlistPWDOBJ['bmsa5'] == 1):
                                                        return redirect('Dashboard') 
                                                    elif(AdminuserlistPWDOBJ['breadonly5'] == 1):
                                                        return redirect('Dashboard') 
                                                    elif(AdminuserlistPWDOBJ['ballfeatures5'] == 1):
                                                        return redirect('Dashboard') 
                                                    else:
                                                        return redirect('PlantAssetViewDashboard') 


                                            else:	
                                                AdminuserlistActive6A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant16=lUnitId, ballfeatures6=1).values()
                                                if AdminuserlistActive6A:  
                                                         
                                                        request.session['lCategoryID'] = 0                        
                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                        request.session['lunitid'] = lUnitId
                                                        request.session['sunitno'] = sUnitName
                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                        request.session['badmin'] = 0
                                                        request.session['badmin1'] = 0
                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores6']
                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration6']
                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice6']
                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa6']
                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly6']
                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures6']
                                                        request.session['bmasterlistonlyallplant'] = 0
                                                        if(AdminuserlistPWDOBJ['bstores6'] == 1):
                                                            return redirect('Dashboard') 
                                                        elif(AdminuserlistPWDOBJ['bcalibration6'] == 1):
                                                            return redirect('Dashboard') 
                                                        elif(AdminuserlistPWDOBJ['bservice6'] == 1):
                                                            return redirect('Dashboard') 
                                                        elif(AdminuserlistPWDOBJ['bmsa6'] == 1):
                                                            return redirect('Dashboard') 
                                                        elif(AdminuserlistPWDOBJ['breadonly6'] == 1):
                                                            return redirect('Dashboard') 
                                                        elif(AdminuserlistPWDOBJ['ballfeatures6'] == 1):
                                                            return redirect('Dashboard') 
                                                        else:
                                                            return redirect('PlantAssetViewDashboard') 

                                                else:	
                                                    AdminuserlistActive7A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant17=lUnitId, ballfeatures7=1).values()
                                                    if AdminuserlistActive7A:  
                                                             
                                                            request.session['lCategoryID'] = 0                        
                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                            request.session['lunitid'] = lUnitId
                                                            request.session['sunitno'] = sUnitName
                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                            request.session['badmin'] = 0
                                                            request.session['badmin1'] = 0
                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores7']
                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration7']
                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice7']
                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa7']
                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly7']
                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures7']
                                                            request.session['bmasterlistonlyallplant'] = 0
                                                            if(AdminuserlistPWDOBJ['bstores7'] == 1):
                                                                return redirect('Dashboard') 
                                                            elif(AdminuserlistPWDOBJ['bcalibration7'] == 1):
                                                                return redirect('Dashboard') 
                                                            elif(AdminuserlistPWDOBJ['bservice7'] == 1):
                                                                return redirect('Dashboard') 
                                                            elif(AdminuserlistPWDOBJ['bmsa7'] == 1):
                                                                return redirect('Dashboard') 
                                                            elif(AdminuserlistPWDOBJ['breadonly7'] == 1):
                                                                return redirect('Dashboard') 
                                                            elif(AdminuserlistPWDOBJ['ballfeatures7'] == 1):
                                                                return redirect('Dashboard') 
                                                            else:
                                                                return redirect('PlantAssetViewDashboard') 

                                                        
                                                    else:	
                                                        AdminuserlistActive8A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant18=lUnitId, ballfeatures8=1).values()
                                                        if AdminuserlistActive8A:  
                                                                 
                                                                request.session['lCategoryID'] = 0                        
                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                request.session['lunitid'] = lUnitId
                                                                request.session['sunitno'] = sUnitName
                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                request.session['badmin'] = 0
                                                                request.session['badmin1'] = 0
                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores8']
                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration8']
                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice8']
                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa8']
                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly8']
                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures8']
                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                            
                                                                if(AdminuserlistPWDOBJ['bstores8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                elif(AdminuserlistPWDOBJ['bcalibration8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                elif(AdminuserlistPWDOBJ['bservice8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                elif(AdminuserlistPWDOBJ['bmsa8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                elif(AdminuserlistPWDOBJ['breadonly8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                elif(AdminuserlistPWDOBJ['ballfeatures8'] == 1):
                                                                    return redirect('Dashboard') 
                                                                else:
                                                                    return redirect('PlantAssetViewDashboard')  

                                                                
                                                        else:	
                                                            AdminuserlistActive9A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant19=lUnitId, ballfeatures9=1).values()
                                                            if AdminuserlistActive9A:  
                                                                     
                                                                    request.session['lCategoryID'] = 0                        
                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                    request.session['lunitid'] = lUnitId
                                                                    request.session['sunitno'] = sUnitName
                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                    request.session['badmin'] = 0
                                                                    request.session['badmin1'] = 0
                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores9']
                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration9']
                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice9']
                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa9']
                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly9']
                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures9']
                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                    
                                                                    if(AdminuserlistPWDOBJ['bstores9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    elif(AdminuserlistPWDOBJ['bcalibration9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    elif(AdminuserlistPWDOBJ['bservice9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    elif(AdminuserlistPWDOBJ['bmsa9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    elif(AdminuserlistPWDOBJ['breadonly9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    elif(AdminuserlistPWDOBJ['ballfeatures9'] == 1):
                                                                        return redirect('Dashboard') 
                                                                    else:
                                                                        return redirect('PlantAssetViewDashboard')  

        
                                                            else:	
                                                                AdminuserlistActive10A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant110=lUnitId, ballfeatures10=1).values()
                                                                if AdminuserlistActive10A:  
                                                                         
                                                                        request.session['lCategoryID'] = 0                        
                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                        request.session['lunitid'] = lUnitId
                                                                        request.session['sunitno'] = sUnitName
                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                        request.session['badmin'] = 0
                                                                        request.session['badmin1'] = 0
                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores10']
                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration10']
                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice10']
                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa10']
                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly10']
                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures10']
                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                                            
                                                                        if(AdminuserlistPWDOBJ['bstores10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        elif(AdminuserlistPWDOBJ['bcalibration10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        elif(AdminuserlistPWDOBJ['bservice10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        elif(AdminuserlistPWDOBJ['bmsa10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        elif(AdminuserlistPWDOBJ['breadonly10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        elif(AdminuserlistPWDOBJ['ballfeatures10'] == 1):
                                                                            return redirect('Dashboard') 
                                                                        else:
                                                                            return redirect('PlantAssetViewDashboard')  

                                                                else:	
                                                                    AdminuserlistActive11A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant111=lUnitId, ballfeatures11=1).values()
                                                                    if AdminuserlistActive11A:  
                                                                             
                                                                            request.session['lCategoryID'] = 0                        
                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                            request.session['lunitid'] = lUnitId
                                                                            request.session['sunitno'] = sUnitName
                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                            request.session['badmin'] = 0
                                                                            request.session['badmin1'] = 0
                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores11']
                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration11']
                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice11']
                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa11']
                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly11']
                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures11']
                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                                          
                                                                            if(AdminuserlistPWDOBJ['bstores11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            elif(AdminuserlistPWDOBJ['bcalibration11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            elif(AdminuserlistPWDOBJ['bservice11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            elif(AdminuserlistPWDOBJ['bmsa11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            elif(AdminuserlistPWDOBJ['breadonly11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            elif(AdminuserlistPWDOBJ['ballfeatures11'] == 1):
                                                                                return redirect('Dashboard') 
                                                                            else:
                                                                                return redirect('PlantAssetViewDashboard') 


                                                                    else:	
                                                                        AdminuserlistActive12A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant121=lUnitId, ballfeatures12=1).values()
                                                                        if AdminuserlistActive12A:  
                                                                                 
                                                                                request.session['lCategoryID'] = 0                        
                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                request.session['lunitid'] = lUnitId
                                                                                request.session['sunitno'] = sUnitName
                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                request.session['badmin'] = 0
                                                                                request.session['badmin1'] = 0
                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores12']
                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration12']
                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice12']
                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa12']
                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly12']
                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures12']
                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                                    
                                                                                if(AdminuserlistPWDOBJ['bstores12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                elif(AdminuserlistPWDOBJ['bcalibration12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                elif(AdminuserlistPWDOBJ['bservice12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                elif(AdminuserlistPWDOBJ['bmsa12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                elif(AdminuserlistPWDOBJ['breadonly12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                elif(AdminuserlistPWDOBJ['ballfeatures12'] == 1):
                                                                                    return redirect('Dashboard') 
                                                                                else:
                                                                                    return redirect('PlantAssetViewDashboard') 


                                                                        else:	
                                                                            AdminuserlistActive13A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant131=lUnitId, ballfeatures13=1).values()
                                                                            if AdminuserlistActive13A:  
                                                                                     
                                                                                    request.session['lCategoryID'] = 0                        
                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                    request.session['lunitid'] = lUnitId
                                                                                    request.session['sunitno'] = sUnitName
                                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                    request.session['badmin'] = 0
                                                                                    request.session['badmin1'] = 0
                                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores13']
                                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration13']
                                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice13']
                                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa13']
                                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly13']
                                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures13']
                                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                                                            
                                                                                    if(AdminuserlistPWDOBJ['bstores13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    elif(AdminuserlistPWDOBJ['bcalibration13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    elif(AdminuserlistPWDOBJ['bservice13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    elif(AdminuserlistPWDOBJ['bmsa13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    elif(AdminuserlistPWDOBJ['breadonly13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    elif(AdminuserlistPWDOBJ['ballfeatures13'] == 1):
                                                                                        return redirect('Dashboard') 
                                                                                    else:
                                                                                        return redirect('PlantAssetViewDashboard') 


                                                                            else:	
                                                                                AdminuserlistActive14A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant141=lUnitId, ballfeatures14=1).values()
                                                                                if AdminuserlistActive14A:  
                                                                                         
                                                                                        request.session['lCategoryID'] = 0                        
                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                        request.session['lunitid'] = lUnitId
                                                                                        request.session['sunitno'] = sUnitName
                                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                        request.session['badmin'] = 0
                                                                                        request.session['badmin1'] = 0
                                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores14']
                                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration14']
                                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice14']
                                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa14']
                                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly14']
                                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures14']
                                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                                                                    
                                                                                        if(AdminuserlistPWDOBJ['bstores14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        elif(AdminuserlistPWDOBJ['bcalibration14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        elif(AdminuserlistPWDOBJ['bservice14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        elif(AdminuserlistPWDOBJ['bmsa14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        elif(AdminuserlistPWDOBJ['breadonly14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        elif(AdminuserlistPWDOBJ['ballfeatures14'] == 1):
                                                                                            return redirect('Dashboard') 
                                                                                        else:
                                                                                            return redirect('PlantAssetViewDashboard') 
    


                                                                                else:	
                                                                                    AdminuserlistActive15A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant151=lUnitId, ballfeatures15=1).values()
                                                                                    if AdminuserlistActive15A:  
                                                                                             
                                                                                            request.session['lCategoryID'] = 0                        
                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                            request.session['lunitid'] = lUnitId
                                                                                            request.session['sunitno'] = sUnitName
                                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                            request.session['badmin'] = 0
                                                                                            request.session['badmin1'] = 0
                                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores15']
                                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration15']
                                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice15']
                                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa15']
                                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly15']
                                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures15']
                                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                                                                            
                                                                                            if(AdminuserlistPWDOBJ['bstores15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            elif(AdminuserlistPWDOBJ['bcalibration15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            elif(AdminuserlistPWDOBJ['bservice15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            elif(AdminuserlistPWDOBJ['bmsa15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            elif(AdminuserlistPWDOBJ['breadonly15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            elif(AdminuserlistPWDOBJ['ballfeatures15'] == 1):
                                                                                                return redirect('Dashboard') 
                                                                                            else:
                                                                                                return redirect('PlantAssetViewDashboard') 
        

                                                                                        

                                                                                    else:	
                                                                                        AdminuserlistActive16A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant161=lUnitId, ballfeatures16=1).values()
                                                                                        if AdminuserlistActive16A:  
                                                                                                 
                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                request.session['lunitid'] = lUnitId
                                                                                                request.session['sunitno'] = sUnitName
                                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                request.session['badmin'] = 0
                                                                                                request.session['badmin1'] = 0
                                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores16']
                                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration16']
                                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice16']
                                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa16']
                                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly16']
                                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures16']
                                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                    
                                                                                                if(AdminuserlistPWDOBJ['bstores16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                elif(AdminuserlistPWDOBJ['bcalibration16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                elif(AdminuserlistPWDOBJ['bservice16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                elif(AdminuserlistPWDOBJ['bmsa16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                elif(AdminuserlistPWDOBJ['breadonly16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                elif(AdminuserlistPWDOBJ['ballfeatures16'] == 1):
                                                                                                    return redirect('Dashboard') 
                                                                                                else:
                                                                                                    return redirect('PlantAssetViewDashboard') 
 

                                                                                                
                                                                                        else:	
                                                                                            AdminuserlistActive17A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant171=lUnitId, ballfeatures17=1).values()
                                                                                            if AdminuserlistActive17A:  
                                                                                                     
                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                    request.session['lunitid'] = lUnitId
                                                                                                    request.session['sunitno'] = sUnitName
                                                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                    request.session['badmin'] = 0
                                                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores17']
                                                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration17']
                                                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice17']
                                                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa17']
                                                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly17']
                                                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures17']
                                                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                            
                                                                                                    if(AdminuserlistPWDOBJ['bstores17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    elif(AdminuserlistPWDOBJ['bcalibration17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    elif(AdminuserlistPWDOBJ['bservice17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    elif(AdminuserlistPWDOBJ['bmsa17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    elif(AdminuserlistPWDOBJ['breadonly17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    elif(AdminuserlistPWDOBJ['ballfeatures17'] == 1):
                                                                                                        return redirect('Dashboard') 
                                                                                                    else:
                                                                                                        return redirect('PlantAssetViewDashboard') 
    

                                                                                                        
                                                                                            else:	
                                                                                                AdminuserlistActive18A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant181=lUnitId, ballfeatures18=1).values()
                                                                                                if AdminuserlistActive18A:  
                                                                                                         
                                                                                                        request.session['lCategoryID'] = 0                        
                                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                        request.session['lunitid'] = lUnitId
                                                                                                        request.session['sunitno'] = sUnitName
                                                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                        request.session['badmin'] = 0
                                                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores18']
                                                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration18']
                                                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice18']
                                                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa18']
                                                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly18']
                                                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures18']
                                                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                        
                                                                                                        if(AdminuserlistPWDOBJ['bstores18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        elif(AdminuserlistPWDOBJ['bcalibration18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        elif(AdminuserlistPWDOBJ['bservice18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        elif(AdminuserlistPWDOBJ['bmsa18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        elif(AdminuserlistPWDOBJ['breadonly18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        elif(AdminuserlistPWDOBJ['ballfeatures18'] == 1):
                                                                                                            return redirect('Dashboard') 
                                                                                                        else:
                                                                                                            return redirect('PlantAssetViewDashboard') 
 


        
                                                                                                else:	
                                                                                                    AdminuserlistActive19A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant191=lUnitId, ballfeatures19=1).values()
                                                                                                    if AdminuserlistActive19A:  
                                                                                                             
                                                                                                            request.session['lCategoryID'] = 0                        
                                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                            request.session['lunitid'] = lUnitId
                                                                                                            request.session['sunitno'] = sUnitName
                                                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                            request.session['badmin'] = 0
                                                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores19']
                                                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration19']
                                                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice19']
                                                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa19']
                                                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly19']
                                                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures19']
                                                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                
                                                                                                            if(AdminuserlistPWDOBJ['bstores19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            elif(AdminuserlistPWDOBJ['bcalibration19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            elif(AdminuserlistPWDOBJ['bservice19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            elif(AdminuserlistPWDOBJ['bmsa19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            elif(AdminuserlistPWDOBJ['breadonly19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            elif(AdminuserlistPWDOBJ['ballfeatures19'] == 1):
                                                                                                                return redirect('Dashboard') 
                                                                                                            else:
                                                                                                                return redirect('PlantAssetViewDashboard') 
            



                                                                                                    else:	
                                                                                                        AdminuserlistActive20A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant201=lUnitId, ballfeatures20=1).values()
                                                                                                        if AdminuserlistActive20A:  
                                                                                                                 
                                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                request.session['lunitid'] = lUnitId
                                                                                                                request.session['sunitno'] = sUnitName
                                                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                request.session['badmin'] = 0
                                                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores20']
                                                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration20']
                                                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice20']
                                                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa20']
                                                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly20']
                                                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures20']
                                                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                      
                                                                                                                if(AdminuserlistPWDOBJ['bstores20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                elif(AdminuserlistPWDOBJ['bcalibration20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                elif(AdminuserlistPWDOBJ['bservice20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                elif(AdminuserlistPWDOBJ['bmsa20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                elif(AdminuserlistPWDOBJ['breadonly20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                elif(AdminuserlistPWDOBJ['ballfeatures20'] == 1):
                                                                                                                    return redirect('Dashboard') 
                                                                                                                else:
                                                                                                                    return redirect('PlantAssetViewDashboard') 
                


                                                                                                        else:	
                                                                                                            AdminuserlistActive21A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant211=lUnitId, ballfeatures21=1).values()
                                                                                                            if AdminuserlistActive21A:  
                                                                                                                     
                                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                    request.session['lunitid'] = lUnitId
                                                                                                                    request.session['sunitno'] = sUnitName
                                                                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                    request.session['badmin'] = 0
                                                                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores21']
                                                                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration21']
                                                                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice21']
                                                                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa21']
                                                                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly21']
                                                                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures21']
                                                                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                          
                                                                                                                    if(AdminuserlistPWDOBJ['bstores21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    elif(AdminuserlistPWDOBJ['bcalibration21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    elif(AdminuserlistPWDOBJ['bservice21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    elif(AdminuserlistPWDOBJ['bmsa21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    elif(AdminuserlistPWDOBJ['breadonly21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    elif(AdminuserlistPWDOBJ['ballfeatures21'] == 1):
                                                                                                                        return redirect('Dashboard') 
                                                                                                                    else:
                                                                                                                        return redirect('PlantAssetViewDashboard') 
                    


                                                                                                            else:	
                                                                                                                AdminuserlistActive22A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant221=lUnitId, ballfeatures22=1).values()
                                                                                                                if AdminuserlistActive22A:  
                                                                                                                         
                                                                                                                        request.session['lCategoryID'] = 0                        
                                                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                        request.session['lunitid'] = lUnitId
                                                                                                                        request.session['sunitno'] = sUnitName
                                                                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                        request.session['badmin'] = 0
                                                                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores22']
                                                                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration22']
                                                                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice22']
                                                                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa22']
                                                                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly22']
                                                                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures22']
                                                                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                              
                                                                                                                        if(AdminuserlistPWDOBJ['bstores22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        elif(AdminuserlistPWDOBJ['bcalibration22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        elif(AdminuserlistPWDOBJ['bservice22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        elif(AdminuserlistPWDOBJ['bmsa22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        elif(AdminuserlistPWDOBJ['breadonly22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        elif(AdminuserlistPWDOBJ['ballfeatures22'] == 1):
                                                                                                                            return redirect('Dashboard') 
                                                                                                                        else:
                                                                                                                            return redirect('PlantAssetViewDashboard') 
                        


                                                                                                                else:	
                                                                                                                    AdminuserlistActive23A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant231=lUnitId, ballfeatures23=1).values()
                                                                                                                    if AdminuserlistActive23A:  
                                                                                                                             
                                                                                                                            request.session['lCategoryID'] = 0                        
                                                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                            request.session['lunitid'] = lUnitId
                                                                                                                            request.session['sunitno'] = sUnitName
                                                                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                            request.session['badmin'] = 0
                                                                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores23']
                                                                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration23']
                                                                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice23']
                                                                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa23']
                                                                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly23']
                                                                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures23']
                                                                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                                  
                                                                                                                            if(AdminuserlistPWDOBJ['bstores23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            elif(AdminuserlistPWDOBJ['bcalibration23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            elif(AdminuserlistPWDOBJ['bservice23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            elif(AdminuserlistPWDOBJ['bmsa23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            elif(AdminuserlistPWDOBJ['breadonly23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            elif(AdminuserlistPWDOBJ['ballfeatures23'] == 1):
                                                                                                                                return redirect('Dashboard') 
                                                                                                                            else:
                                                                                                                                return redirect('PlantAssetViewDashboard') 
                            


                                                                                                                    else:	
                                                                                                                        AdminuserlistActive24A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant241=lUnitId, ballfeatures24=1).values()
                                                                                                                        if AdminuserlistActive24A:  
                                                                                                                                 
                                                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                                request.session['lunitid'] = lUnitId
                                                                                                                                request.session['sunitno'] = sUnitName
                                                                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                                request.session['badmin'] = 0
                                                                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores24']
                                                                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration24']
                                                                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice24']
                                                                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa24']
                                                                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly24']
                                                                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures24']
                                                                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                                      
                                                                                                                                if(AdminuserlistPWDOBJ['bstores24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                elif(AdminuserlistPWDOBJ['bcalibration24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                elif(AdminuserlistPWDOBJ['bservice24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                elif(AdminuserlistPWDOBJ['bmsa24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                elif(AdminuserlistPWDOBJ['breadonly24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                elif(AdminuserlistPWDOBJ['ballfeatures24'] == 1):
                                                                                                                                    return redirect('Dashboard') 
                                                                                                                                else:
                                                                                                                                    return redirect('PlantAssetViewDashboard') 
                                




                                                                                                                        else:	
                                                                                                                            AdminuserlistActive25A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant251=lUnitId, ballfeatures25=1).values()
                                                                                                                            if AdminuserlistActive25A:  
                                                                                                                                     
                                                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                                    request.session['lunitid'] = lUnitId
                                                                                                                                    request.session['sunitno'] = sUnitName
                                                                                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                                    request.session['badmin'] = 0
                                                                                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores25']
                                                                                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration25']
                                                                                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice25']
                                                                                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa25']
                                                                                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly25']
                                                                                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures25']
                                                                                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                                                                                                                                          
                                                                                                                                    if(AdminuserlistPWDOBJ['bstores25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    elif(AdminuserlistPWDOBJ['bcalibration25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    elif(AdminuserlistPWDOBJ['bservice25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    elif(AdminuserlistPWDOBJ['bmsa25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    elif(AdminuserlistPWDOBJ['breadonly25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    elif(AdminuserlistPWDOBJ['ballfeatures25'] == 1):
                                                                                                                                        return redirect('Dashboard') 
                                                                                                                                    else:
                                                                                                                                        return redirect('PlantAssetViewDashboard') 
                                    

                                                                                                                            else:
                                                                                                                                AdminuserlistActive2 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant11=lUnitId, ballfeatures=1).values()
                                                                                                                                if AdminuserlistActive2:  
                                                                                                                                        
                                                                                                                                        request.session['lCategoryID'] = 0                        
                                                                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                                        request.session['lunitid'] = lUnitId
                                                                                                                                        request.session['sunitno'] = sUnitName
                                                                                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                                                        request.session['badmin'] = 0
                                                                                                                                        request.session['badmin1'] = 0
                                                                                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores']
                                                                                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration']
                                                                                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice']
                                                                                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa']
                                                                                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly']
                                                                                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures']
                                                                                                                                        request.session['bmasterlistonlyallplant'] = 0                                             
                                                                                                                                        if(AdminuserlistPWDOBJ['bstores'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        elif(AdminuserlistPWDOBJ['bcalibration'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        elif(AdminuserlistPWDOBJ['bservice'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        elif(AdminuserlistPWDOBJ['bmsa'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        elif(AdminuserlistPWDOBJ['breadonly'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        elif(AdminuserlistPWDOBJ['ballfeatures'] == 1):
                                                                                                                                            return redirect('Dashboard') 
                                                                                                                                        else:
                                                                                                                                            return redirect('PlantAssetViewDashboard') 








                                                                                                                                else:
                                                                                                                                    messages.error(request, 'You Donot Have access to use Tool Pulse App. Please check with the Tool Pulse Admin!')
                                                                                                                                                
                                                                                                                                    Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
                                                                                                                                    Adminuserlist_list = Adminuserlist.objects.order_by('semployeeno') 
                                                                                                                                    return render(request, "CloudCaliber/home.html", 
                                                                                                                                                            {
                                                                                                                                                                                'title':'Issue list', 
                                                                                                                                                                                'message':'Your Issue list page.',
                                                                                                                                                                                'year':datetime.now().year,   
                                                                                                                                                                                'Adminunitlist_list': Adminunitlist_list
                                                                                                                                                            }
                                                                                                                                                                                )

                
            else:
                messages.error(request, 'Your Password is not Correct. Please re-enter and then try to login!')
                return redirect('home')
                Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
                return render(request, "CloudCaliber/home.html", 
                                    {
                                                        'title':'Login list', 
                                                        'message':'Your Login list page.',
                                                        'year':datetime.now().year,   
                                                        'Adminunitlist_list': Adminunitlist_list
                                    }
                                                        )
        else:
            messages.error(request, 'Your User Name is not Correct. Please re-enter and then try to login!')
            return redirect('home') 
            
            Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
            return render(request, "CloudCaliber/home.html", 
                                    {
                                                        'title':'Login list', 
                                                        'message':'Your Login list page.',
                                                        'year':datetime.now().year,   
                                                        'Adminunitlist_list': Adminunitlist_list
                                    }
                                                        )
    else:
        
        Adminunitlist_list = Adminunitlist.objects.order_by('splantno') 
        return render(request, "CloudCaliber/home.html", 
                    {
                                        'title':'Login list', 
                                        'message':'Your Login list page.',
                                        'year':datetime.now().year,   
                                        'Adminunitlist_list': Adminunitlist_list
                    }
                                        )




@csrf_exempt
def about(request):
    return render(request, "CloudCaliber/about.html")

@csrf_exempt
def contact(request):
    return render(request, "CloudCaliber/contact.html")  

@csrf_exempt
def SignINClicked (request): 
    return render(request, "CloudCaliber/Dashboard.html")




@csrf_exempt
def AdministratorDashboard (request): 

    request.session['CurDateFromD']  = ""
    request.session['CurDateFromO']  = ""
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

    sCodeFinal1 = ""
    sCodeFinal2 = ""
 
    bSAPCodeDone = 0
    

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

    request.session['badmin'] = 1
    request.session['badmin1'] = 1
    request.session['bstores'] = 0
    request.session['bcalibration'] = 0
    request.session['bservice'] = 0
    request.session['bmsa'] = 0
    request.session['bmasterlistonlyallplant'] = 0  
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
        ID_Categories =0
        ID_Categories =0

        sCodeFinal1 = ""
        sCodeFinal2 = ""
        sPlantCode = ""
        sCategoryCode = ""
        styperefnameA1 = ""
        styperefnameA2 = ""
        styperefnameA3 = ""
        styperefnameA4 = ""
        styperefnameA5 = ""
 
        bSAPCodeDone = 0
        if 'bSAPCodeDone1' in request.POST:  
            bSAPCodeDone = 1


        if 'Plant' in request.POST: 
            if(data.get('Plant').isnumeric() ):
                lPlantIdSelect = int(data.get('Plant'))

        lPlantId     = lPlantIdSelect 
        if 'Categories' in request.POST: 
            if(data.get('Categories').isnumeric() ):
                ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            if(data.get('Classification').isnumeric() ):
                ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            if(data.get('Flow1').isnumeric() ):
                Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST:  
            if(data.get('Flow2').isnumeric() ):
                Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST:  
            if(data.get('Flow3').isnumeric() ):
                Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST:  
            if(data.get('Flow4').isnumeric() ):
                Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST:  
            if(data.get('Flow5').isnumeric() ):
                Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST:  
            if(data.get('GaugeClass').isnumeric() ):
                GaugeClass = int(data.get('GaugeClass'))

        Location =0
        if 'Location' in request.POST:  
            if(data.get('Location').isnumeric() ):
                Location = int(data.get('Location'))

        txtSearch = ""
        if 'txtSearchID' in request.POST:
            txtSearch = data.get("txtSearchID")










        if 'cmbGetCategory' in request.POST:  

            #request.session['ID_Classification']  =  ClassificationData 

            #request.session['ID_Categories'] = 0
            #request.session['sFlowCode1']   =""
            #request.session['sFlowCode2']   =""
            #request.session['sFlowCode3']   =""
            #request.session['sFlowCode4']   =""
            #request.session['sFlowCode5']   =""
            sCodeFinal1 = ""
            sCodeFinal2 = ""
        
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 



            
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""

            if(ClassificationData != 0):
                Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
                tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

                if Adminassettypelist_list1:
                    sClasscode = Adminassettypelist_list1.scode

 
         


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
 



        if 'cmbGetFlow' in request.POST:  

           
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""

            if(ClassificationData != 0): 
                Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
                if Adminassettypelist_list1:
                    sClasscode = Adminassettypelist_list1.scode


            if (ID_Categories == 0):
                styperefnameA1 = ""
            else:
                Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                if Adminassetcategorylist_list:
                    sCategoryCode = Adminassetcategorylist_list.scode
                    sClasscode = Adminassetcategorylist_list.styperefname  
                    styperefnameA1 = Adminassetcategorylist_list.styperefname1
                    styperefnameA2 = Adminassetcategorylist_list.styperefname2
                    styperefnameA3 = Adminassetcategorylist_list.styperefname3
                    styperefnameA4 = Adminassetcategorylist_list.styperefname4
                    styperefnameA5 = Adminassetcategorylist_list.styperefname5




        lCode =0
        lcode = len(txtSearch)


        if (bSAPCodeDone == 0):
            if (lcode != 0):

            
                    
                if  (Location != 0):

                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            if(Flow3Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid') 
                                    else:
                                        if(ID_Categories != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):

                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location).order_by('sinstrumentid')   

                else:
                    
                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                        else:
                            if(Flow3Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid') 
                                    else:
                                        if(ID_Categories != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):

                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId).order_by('sinstrumentid')   


            else:
    
                if  (Location != 0):

                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   
                        
                        else:
                            
                            if(Flow3Data != 0):
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                
                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        if(ID_Categories != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):


                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ldefaultlocationid=Location).order_by('sinstrumentid')   

                else:
                    
                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   
                        
                        else:
                            
                            if(Flow3Data != 0):
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                
                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                    else:
                                        if(ID_Categories != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):


                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId).order_by('sinstrumentid')   

        else:
                
                
            if (lcode != 0):

            
                    
                if  (Location != 0):

                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                        else:
                            if(Flow3Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid') 
                                    else:
                                        if(ID_Categories != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):

                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                else:
                    
                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                        else:
                            if(Flow3Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid') 
                                    else:
                                        if(ID_Categories != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):

                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0 ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId).order_by('sinstrumentid')   


            else:
    
                if  (Location != 0):

                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   
                        
                        else:
                            
                            if(Flow3Data != 0):
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                
                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                    else:
                                        if(ID_Categories != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):


                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ldefaultlocationid=Location, bsapcodegenerate=0).order_by('sinstrumentid')   

                else:
                    
                    if(Flow5Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        if(Flow4Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   
                        
                        else:
                            
                            if(Flow3Data != 0):
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(  bsapcodegenerate =0, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                if(Flow2Data != 0):

                                
                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,  lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    if(Flow1Data != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(bsapcodegenerate =0, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                    else:
                                        if(ID_Categories != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(bsapcodegenerate =0, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            if(ClassificationData != 0):


                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( bsapcodegenerate =0,lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                if(GaugeClass != 0):

                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(bsapcodegenerate =0, lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                                else:
                                                    
                                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, bsapcodegenerate =0).order_by('sinstrumentid')   





        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
        AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
        if AdminunitlistActive:
            sPlantCode = AdminunitlistActive.splantno
            sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
            sPlantNameNameA = AdminunitlistActive.splantname

        request.session['sPlantCode']   =sPlantCode
        





 
             

 
 
        if (styperefnameA1 == "Part No"):
            Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Equipment"):
            Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Operation"):
            Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Material"):
            Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        else:
            Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                
        if (styperefnameA2 == "Part No"):
            Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
        elif (styperefnameA2 == "Equipment"):
            Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
        elif (styperefnameA2 == "Operation"):
            Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
        elif (styperefnameA2 == "Material"):
            Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
        else:
            Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



        if (styperefnameA3 == "Part No"):
            Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Equipment"):
            Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Operation"):
            Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Material"):
            Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        else:
            Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

        if (styperefnameA4 == "Part No"):
            Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Equipment"):
            Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Operation"):
            Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Material"):
            Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
        else:
            Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

        if (styperefnameA5 == "Part No"):
            Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
        elif (styperefnameA5 == "Equipment"):
            Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        elif (styperefnameA5 == "Operation"):
            Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        elif (styperefnameA5 == "Material"):
            Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        else:
            Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })





        Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
        
        tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 =0

        if (lRecCount > 500): 
            lRecCount1 = int((lRecCount * 5/100) )
        else:
            lRecCount1 =lRecCount
            
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



        return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            'bSAPCodeDone':bSAPCodeDone,            
            'CurDateNow':datetime.today(), 
            'lPlantId':lPlantId,
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list, 
            'Adminunitlist_list':Adminunitlist_list,
            'Location':Location,
            'txtSearch':txtSearch,
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': styperefnameA1,  
            'cmbFlow2label': styperefnameA2,  
            'cmbFlow3label': styperefnameA3,  
            'cmbFlow4label': styperefnameA4,
            'cmbFlow5label': styperefnameA5,    
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ,
            'Adminassetcategorytypelist2_AddNew1OBJ': Adminassetcategorytypelist2_AddNew1OBJ,
            'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ,
            'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ,
            'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ,
            'bNewID': 0 ,  
            
            }) 

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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(  scurrentstatus='ISSUED').order_by('sinstrumentid')

           
        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 =0

        page_number  = request.GET.get('page')


        if (lRecCount > 500): 
            lRecCount1 = int((lRecCount * 7/100) )
        else:
            lRecCount1 =lRecCount
            
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')




        return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            'bSAPCodeDone':bSAPCodeDone,            
            'CurDateNow':datetime.now(),
            'lPlantId':lPlantId,  
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'Location': 0 , 
            'semployeename':  request.session['semployeename'] ,
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
        }) 




@csrf_exempt
def AdministratorDashboardA (request): 
    request.method = ""
    return redirect('AdministratorDashboard')  





@csrf_exempt
def Dashboard (request): 
    txtSearch = ""
    semployeename = request.session['semployeename']

    request.session['CurDateFromD']  = ""
    request.session['CurDateFromO']  = ""

    CurDateFrom = datetime.today().strftime('%Y-%m-%d')
    
    CurToDate = datetime.now()
    calibToDate1 = CurToDate  + timedelta(days=30)
    calibToDate = calibToDate1.strftime('%Y-%m-%d')


    request.session['CurDateFrom']  = CurDateFrom
    request.session['CurDateTo']  = calibToDate
    request.session['CurDateFromD']  = ""
    request.session['CurDateFromO']  = ""

    request.session['CurDateFromD']  = CurDateFrom

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
 
    lCategoryID = request.session['lCategoryID']                       
    lLoginUserId = request.session['lLoginUserId']   
    semployeeno = request.session['semployeeno']  
    lunitid = request.session['lunitid']  
    sunitno = request.session['sunitno']  
    lcompanyid = request.session['lcompanyid']  
    scompantname = request.session['scompantname']  
    semailaddress = request.session['semailaddress']  
    smobile = request.session['smobile']
    CurDate = datetime.now()
    calibDate = CurDate  + timedelta(days=30)
    
    YesterdayDate = CurDate  + timedelta(days=-1)
    sRangeDate1 = str(CurDate.strftime("%d-%m-%Y")) + " to " + str(calibDate.strftime("%d-%m-%Y"))

    month = CurDate.month
    year = CurDate.year

    #month_number = list(calendar.month_name).index(month)

    cal = HTMLCalendar().formatmonth(year, month)

    MasterinstrumentslistUnderPur_list =  Masterinstrumentslist.objects.filter(lplantid=lPlantId,  scurrentstatus='PURCHASE INITIATED').order_by('sinstrumentid')     


    page_number  = request.GET.get('page')

    lRecCount =0 
    lRecCount = MasterinstrumentslistUnderPur_list.count()
    lRecCount1 =0

    if (lRecCount > 500): 
        lRecCount1 = int((lRecCount * 5/100) )
    else:
        lRecCount1 =lRecCount
        
    if (lRecCount1 == 0):
        lRecCount1 =1
    paginator = Paginator(MasterinstrumentslistUnderPur_list, lRecCount1)
    try:
        MasterinstrumentslistUnderPur_lists = paginator.get_page(page_number )
    except PageNotAnInteger:
        MasterinstrumentslistUnderPur_lists = paginator.page(1)
    except EmptyPage:
        MasterinstrumentslistUnderPur_lists = paginator.page(paginator.num_pages)


    MasterinstrumentslistCount1 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId).count()    

    MasterinstrumentslistCount_list =  Masterinstrumentslist.objects.filter(lplantid=lPlantId,  scurrentstatus='PURCHASE INITIATED').count()    

    MasterinstrumentslistCount2 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId,bissedtosupplier=0, scurrentstatus='ISSUED').count()  


    MasterinstrumentslistCount3 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='IDLE').count()  
    MasterinstrumentslistCount4 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='SPARE').count() 
    MasterinstrumentslistCount5 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='SCRAPPED').count()
    MasterinstrumentslistCount_VendorIssue =  Masterinstrumentslist.objects.filter(lplantid=lPlantId,bissedtosupplier=1, scurrentstatus='ISSUED').count()

    MasterinstrumentslistCount6 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='TRANSFERRED').count()
    MasterinstrumentslistCount7 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, bsapcodegenerate=1).count()
    MasterinstrumentslistCount8 =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, bsapcodegenerate=0).count()


    MasterinstrumentslistCount_Qua =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='QUARANTINE').count()  

    MasterinstrumentslistCount_Limited =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, blimitedusage=1).count()
    MasterinstrumentslistCount_Damaged =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='ERROR - DAMAGED').count()
    # MasterinstrumentslistCount_UnderCalibration =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='ERROR - DAMAGED').count()

    MasterinstrumentslistCount_listUC =   Masterinstrumentslist.objects.filter(lplantid=lPlantId,  scurrentstatus='UNDER CALIBRATION').order_by('sinstrumentid')     
 
    MasterinstrumentslistCount_OverDue =   Masterinstrumentslist.objects.exclude(snextcalibdate ="").filter(lplantid=lPlantId,   dtnextcalib__lte=CurDate, scurrentstatus='ISSUED').count()
 
 
    MasterinstrumentslistCount_UnderCalibration =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus='UNDER CALIBRATION').count()


    Masterinstrumentslist30DayDue_list =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, bshowlistascalibrate=1,  dtnextcalib__gte=CurDate,   dtnextcalib__lte=calibDate).order_by('sinstrumentid').order_by('dtnextcalib')     


    page_numberS  = request.GET.get('page')

    lRecCountS =0 
    lRecCountS = Masterinstrumentslist30DayDue_list.count()
    lRecCountS1 =0

    if (lRecCountS > 30): 
        lRecCountS1 = int((lRecCountS * 5/100) )
    else:
        lRecCountS1 =lRecCountS
        
    if (lRecCountS1 == 0):
        lRecCountS1 =1
    paginatorS = Paginator(Masterinstrumentslist30DayDue_list, lRecCountS1)
    try:
        Masterinstrumentslist30DayDue_listS = paginatorS.get_page(page_numberS )
    except PageNotAnInteger:
        Masterinstrumentslist30DayDue_listS = paginatorS.page(1)
    except EmptyPage:
        Masterinstrumentslist30DayDue_listS = paginatorS.page(paginatorS.num_pages)

   

    MasterinstrumentslistUnderCalibration_list =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus="UNDER CALIBRATION").order_by('sinstrumentid').order_by('dtnextcalib')     


    # page_numberUC  = request.GET.get('page')

    # lRecCountUC =0 
    # lRecCountUC = MasterinstrumentslistUnderCalibration_list.count()
    # lRecCountUC1 =0

    # if (lRecCountUC > 30): 
    #     lRecCountUC1 = int((lRecCountUC * 5/100) )
    # else:
    #     lRecCountUC1 =lRecCountUC
        
    # if (lRecCountUC1 == 0):
    #     lRecCountUC1 =1
    # paginatorCU = Paginator(MasterinstrumentslistUnderCalibration_list, lRecCountUC1)
    # try:
    #     MasterinstrumentslistUnderCalibration_list = paginatorCU.get_page(page_numberUC )
    # except PageNotAnInteger:
    #     MasterinstrumentslistUnderCalibration_list = paginatorCU.page(1)
    # except EmptyPage:
    #     MasterinstrumentslistUnderCalibration_list = paginatorCU.page(paginatorCU.num_pages)
     
 
    MasterinstrumentslistDamaged_list =  Masterinstrumentslist.objects.filter(lplantid=lPlantId, scurrentstatus="DAMAGED").order_by('sinstrumentid').order_by('dtnextcalib')     


    page_numberD  = request.GET.get('page')

    lRecCountD =0 
    lRecCountD = MasterinstrumentslistDamaged_list.count()
    lRecCountD1 =0

    if (lRecCountD > 30): 
        lRecCountD1 = int((lRecCountD * 5/100) )
    else:
        lRecCountD1 =lRecCountD
        
    if (lRecCountD1 == 0):
        lRecCountD1 =1
    paginatorD = Paginator(MasterinstrumentslistDamaged_list, lRecCountD1)
    try:
        MasterinstrumentslistDamaged_list = paginatorD.get_page(page_numberD )
    except PageNotAnInteger:
        MasterinstrumentslistDamaged_list = paginatorD.page(1)
    except EmptyPage:
        MasterinstrumentslistDamaged_list = paginatorD.page(paginatorD.num_pages)
     


    return render(request, "CloudCaliber/Dashboard.html", 
            { 
            'sRangeDate1': sRangeDate1 ,
            'YesterdayDate': str(YesterdayDate.strftime("%d-%m-%Y")) ,
            'cal': cal ,
            'sPlantName':sPlantName,
            'semployeename': semployeename ,
            'txtSearch':txtSearch,
            'MasterinstrumentslistUnderPur_list': MasterinstrumentslistUnderPur_lists, 
            'MasterinstrumentslistCount1': "{:,}".format(MasterinstrumentslistCount1),
            'MasterinstrumentslistCount2': "{:,}".format(MasterinstrumentslistCount2),
            'MasterinstrumentslistCount3': "{:,}".format(MasterinstrumentslistCount3),
            'MasterinstrumentslistCount4': "{:,}".format(MasterinstrumentslistCount4),
            'MasterinstrumentslistCount5': "{:,}".format(MasterinstrumentslistCount5),
 
            'MasterinstrumentslistCount_Qua': "{:,}".format(MasterinstrumentslistCount_Qua),
            'MasterinstrumentslistCount_Limited': "{:,}".format(MasterinstrumentslistCount_Limited),
            'MasterinstrumentslistCount_Damaged': "{:,}".format(MasterinstrumentslistCount_Damaged),

            
            'MasterinstrumentslistCount6': "{:,}".format(MasterinstrumentslistCount6),
            'MasterinstrumentslistCount7': "{:,}".format(MasterinstrumentslistCount7),
            'MasterinstrumentslistCount8': "{:,}".format(MasterinstrumentslistCount8),
            'MasterinstrumentslistCount_UnderCalibration': "{:,}".format(MasterinstrumentslistCount_UnderCalibration),
            'MasterinstrumentslistCount_OverDue': "{:,}".format(MasterinstrumentslistCount_OverDue),

            'MasterinstrumentslistCount_VendorIssue': "{:,}".format(MasterinstrumentslistCount_VendorIssue),



            'Masterinstrumentslist30DayDue_listS':Masterinstrumentslist30DayDue_listS,
            'MasterinstrumentslistUnderCalibration_listS':MasterinstrumentslistUnderCalibration_list,
            'MasterinstrumentslistDamaged_listS':MasterinstrumentslistDamaged_list,
            
              })



@csrf_exempt
def PlantAssetViewDashboard(request):

    sCodeFinal1 = ""
    sCodeFinal2 = ""
 
    request.session['CurDateFromD']  = ""
    request.session['CurDateFromO']  = ""
    

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
        ID_Categories =0
        ID_Categories =0

        sCodeFinal1 = ""
        sCodeFinal2 = ""
        sPlantCode = ""
        sCategoryCode = ""
        styperefnameA1 = ""
        styperefnameA2 = ""
        styperefnameA3 = ""
        styperefnameA4 = ""
        styperefnameA5 = ""

        if 'Plant' in request.POST: 
            if(data.get('Plant').isnumeric() ):
                lPlantIdSelect = int(data.get('Plant'))
        
        lPlantId     = lPlantIdSelect 
        if 'Categories' in request.POST: 
            if(data.get('Categories').isnumeric() ):
                ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            if(data.get('Classification').isnumeric() ):
                ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            if(data.get('Flow1').isnumeric() ):
                Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST:  
            if(data.get('Flow2').isnumeric() ):
                Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST:  
            if(data.get('Flow3').isnumeric() ):
                Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST:  
            if(data.get('Flow4').isnumeric() ):
                Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST:  
            if(data.get('Flow5').isnumeric() ):
                Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST:  
            if(data.get('GaugeClass').isnumeric() ):
                GaugeClass = int(data.get('GaugeClass'))

        Location =0
        if 'Location' in request.POST:  
            if(data.get('Location').isnumeric() ):
                Location = int(data.get('Location'))

        txtSearch = ""
        if 'txtSearchID' in request.POST:
            txtSearch = data.get("txtSearchID")





        if 'cmbGetCategory' in request.POST:  

            #request.session['ID_Classification']  =  ClassificationData 

            #request.session['ID_Categories'] = 0
            #request.session['sFlowCode1']   =""
            #request.session['sFlowCode2']   =""
            #request.session['sFlowCode3']   =""
            #request.session['sFlowCode4']   =""
            #request.session['sFlowCode5']   =""
            sCodeFinal1 = ""
            sCodeFinal2 = ""
         
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 



            
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""

            if(ClassificationData != 0):
                Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
                tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

                if Adminassettypelist_list1:
                    sClasscode = Adminassettypelist_list1.scode

 
         


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
 



        if 'cmbGetFlow' in request.POST:  

           
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""

            if(ClassificationData != 0): 
                Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
                if Adminassettypelist_list1:
                    sClasscode = Adminassettypelist_list1.scode


            if (ID_Categories == 0):
                styperefnameA1 = ""
            else:
                Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                if Adminassetcategorylist_list:
                    sCategoryCode = Adminassetcategorylist_list.scode
                    sClasscode = Adminassetcategorylist_list.styperefname  
                    styperefnameA1 = Adminassetcategorylist_list.styperefname1
                    styperefnameA2 = Adminassetcategorylist_list.styperefname2
                    styperefnameA3 = Adminassetcategorylist_list.styperefname3
                    styperefnameA4 = Adminassetcategorylist_list.styperefname4
                    styperefnameA5 = Adminassetcategorylist_list.styperefname5




        lCode =0
        lcode = len(txtSearch)


        if (lcode != 0):

         
                
            if  (Location != 0):

                if(Flow5Data != 0):

                    if(GaugeClass != 0):

                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                    else:
                        
                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                else:
                    if(Flow4Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                    else:
                        if(Flow3Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            if(Flow2Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                if(Flow1Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid') 
                                else:
                                    if(ID_Categories != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        if(ClassificationData != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location).order_by('sinstrumentid')   

            else:
                
                if(Flow5Data != 0):

                    if(GaugeClass != 0):

                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        
                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                else:
                    if(Flow4Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                    else:
                        if(Flow3Data != 0):

                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                        else:
                            if(Flow2Data != 0):

                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                            else:
                                if(Flow1Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid') 
                                else:
                                    if(ID_Categories != 0):

                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                    else:
                                        if(ClassificationData != 0):

                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                        else:
                                            
                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(sinstrumentid__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(sdescription__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(sassettype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(splanttype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(categorytype__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname1__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname2__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname3__icontains=txtSearch, lplantid=lPlantId, ldefaultlocationid=Location ) | Masterinstrumentslist.objects.filter(styperefname4__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(styperefname5__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(smake__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(slocationname__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(scurrentstatus__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(spartno__icontains=txtSearch, lplantid=lPlantId) | Masterinstrumentslist.objects.filter(oldinstrument_id__icontains=txtSearch, lplantid=lPlantId).order_by('sinstrumentid')   


        else:
 
            if  (Location != 0):

                if(Flow5Data != 0):

                    if(GaugeClass != 0):

                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                    else:
                        
                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                else:
                    if(Flow4Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, ldefaultlocationid=Location).order_by('sinstrumentid')   
                    
                    else:
                        
                        if(Flow3Data != 0):
                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                        else:
                            if(Flow2Data != 0):

                               
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                            else:
                                if(Flow1Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                else:
                                    if(ID_Categories != 0):


                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                    else:
                                        if(ClassificationData != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                        else:
                                            
                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, ldefaultlocationid=Location).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ldefaultlocationid=Location).order_by('sinstrumentid')   

            else:
                
                if(Flow5Data != 0):

                    if(GaugeClass != 0):

                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                    else:
                        
                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data, lfolowid5=Flow5Data).order_by('sinstrumentid')   

                else:
                    if(Flow4Data != 0):

                        if(GaugeClass != 0):

                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   

                        else:
                            
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data, lfolowid4=Flow4Data).order_by('sinstrumentid')   
                    
                    else:
                        
                        if(Flow3Data != 0):
                            if(GaugeClass != 0):

                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                            else:
                                
                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data, lfolowid3=Flow3Data).order_by('sinstrumentid')   

                        else:
                            if(Flow2Data != 0):

                               
                                if(GaugeClass != 0):

                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                                else:
                                    
                                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data, lfolowid2=Flow2Data).order_by('sinstrumentid')   

                            else:
                                if(Flow1Data != 0):

                                    if(GaugeClass != 0):

                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                    else:
                                        
                                        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories, lfolowid1=Flow1Data).order_by('sinstrumentid')   

                                else:
                                    if(ID_Categories != 0):


                                        if(GaugeClass != 0):

                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                        else:
                                            
                                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData, lcategoryid=ID_Categories).order_by('sinstrumentid')   

                                    else:
                                        if(ClassificationData != 0):


                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass, lassetid=ClassificationData).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, lassetid=ClassificationData).order_by('sinstrumentid')   

                                        else:
                                            
                                            if(GaugeClass != 0):

                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId, ltolid = GaugeClass).order_by('sinstrumentid')   

                                            else:
                                                
                                                Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId).order_by('sinstrumentid')   



        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
        AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
        if AdminunitlistActive:
            sPlantCode = AdminunitlistActive.splantno
            sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
            sPlantNameNameA = AdminunitlistActive.splantname

        request.session['sPlantCode']   =sPlantCode
        





 
             

 


        if (styperefnameA1 == "Part No"):
            Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Equipment"):
            Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Operation"):
            Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        elif (styperefnameA1 == "Material"):
            Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
        else:
            Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                
        if (styperefnameA2 == "Part No"):
            Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
        elif (styperefnameA2 == "Equipment"):
            Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
        elif (styperefnameA2 == "Operation"):
            Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
        elif (styperefnameA2 == "Material"):
            Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
        else:
            Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



        if (styperefnameA3 == "Part No"):
            Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Equipment"):
            Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Operation"):
            Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        elif (styperefnameA3 == "Material"):
            Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
        else:
            Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

        if (styperefnameA4 == "Part No"):
            Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Equipment"):
            Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Operation"):
            Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
        elif (styperefnameA4 == "Material"):
            Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
        else:
            Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

        if (styperefnameA5 == "Part No"):
            Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
        elif (styperefnameA5 == "Equipment"):
            Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        elif (styperefnameA5 == "Operation"):
            Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        elif (styperefnameA5 == "Material"):
            Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
        else:
            Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
            # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })





        Adminassetcategorytypelist1_AddNewOBJ6 =  Adminassetcategorytypelist1.objects.filter(lcategorytype1=cmbCategoryID, lcode5=6 ).values()

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
        
        tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 =0

        if (lRecCount > 500): 
            lRecCount1 = int((lRecCount * 5/100) )
        else:
            lRecCount1 =lRecCount
            
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            'CurDateNow':datetime.today(), 
            'lPlantId':lPlantId,
            '30DateNow':datetime.now() + timedelta(days=30),  
            'AreaofUselist_list':AreaofUselist_list, 
            'Adminunitlist_list':Adminunitlist_list,
            'Location':Location,
            'txtSearch':txtSearch,
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': styperefnameA1,  
            'cmbFlow2label': styperefnameA2,  
            'cmbFlow3label': styperefnameA3,  
            'cmbFlow4label': styperefnameA4,
            'cmbFlow5label': styperefnameA5,    
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ,
            'Adminassetcategorytypelist2_AddNew1OBJ': Adminassetcategorytypelist2_AddNew1OBJ,
            'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ,
            'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ,
            'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ,
            'bNewID': 0 ,  
            
            }) 

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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter( lplantid=lPlantId).order_by('sinstrumentid')

           
        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 =0

        page_number  = request.GET.get('page')


        if (lRecCount > 500): 
            lRecCount1 = int((lRecCount * 7/100) )
        else:
            lRecCount1 =lRecCount
            
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')




        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists,  
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
        }) 




@csrf_exempt
def PlantAssetViewDashboard1 (request): 
    
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return home(request)

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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


       
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        



        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'title':'User list', 
            'Masterinstrumentslist_lists': Masterinstrumentslist_lists,
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list, 
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
         
        request.session['lSerialNo'] = 0
        request.session['sCodeFinal1AK'] = 0

        request.session['lContNo'] = 0
        request.session['ID_Categories'] = 0
        request.session['sCategoryCode'] = ""
        request.session['categorytype'] = ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5'] = ""
        request.session['sCodeFinal1A'] = sCodeFinal1
        request.session['sCodeFinal2A'] = sCodeFinal2
    
        request.session['sFlowCode1a'] = ""
        request.session['sFlowCode2a'] = ""
        request.session['sFlowCode3a'] = ""
        request.session['sFlowCode4a'] = ""
        request.session['sFlowCode5a'] = ""
        
        request.session['sFlowCode1']   =""
        request.session['sFlowCode2']   =""
        request.session['sFlowCode3']   =""
        request.session['sFlowCode4']   =""
        request.session['sFlowCode5']   =""

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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        




        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':'Masterinstrumentslist_lists', 
            'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list,
            'semployeename':  semployeename,
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


       
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        



        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'title':'User list', 
            'Masterinstrumentslist_lists': Masterinstrumentslist_lists,
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list,
            'semployeename':  semployeename,
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
         
        request.session['lSerialNo'] = 0
        request.session['sCodeFinal1AK'] = 0

        request.session['lContNo'] = 0
        request.session['ID_Categories'] = 0
        request.session['sCategoryCode'] = ""
        request.session['categorytype'] = ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5'] = ""
        request.session['sCodeFinal1A'] = sCodeFinal1
        request.session['sCodeFinal2A'] = sCodeFinal2
    
        request.session['sFlowCode1a'] = ""
        request.session['sFlowCode2a'] = ""
        request.session['sFlowCode3a'] = ""
        request.session['sFlowCode4a'] = ""
        request.session['sFlowCode5a'] = ""
        
        request.session['sFlowCode1']   =""
        request.session['sFlowCode2']   =""
        request.session['sFlowCode3']   =""
        request.session['sFlowCode4']   =""
        request.session['sFlowCode5']   =""

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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        




        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':'Masterinstrumentslist_lists', 
            'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list,
            'semployeename':  semployeename,
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
def PlantAssetViewDashboardAA(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    
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
        ID_Categories =0
        if 'Categories' in request.POST: 
            ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST: 
            Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST: 
            Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST: 
            Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST: 
            Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST: 
            GaugeClass = int(data.get('GaugeClass'))

 


        if 'cmbGetCategory' in request.POST:  

            #request.session['ID_Classification']  =  ClassificationData 

            #request.session['ID_Categories'] = 0
            #request.session['sFlowCode1']   =""
            #request.session['sFlowCode2']   =""
            #request.session['sFlowCode3']   =""
            #request.session['sFlowCode4']   =""
            #request.session['sFlowCode5']   =""
            sCodeFinal1 = ""
            sCodeFinal2 = ""
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""
            Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
            if Adminassettypelist_list1:
                sClasscode = Adminassettypelist_list1.scode

 
         


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='ISSUED').order_by('sinstrumentid')

            

            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = Masterinstrumentslist_list.count()
            lRecCount1 = int((lRecCount * 5/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1
            paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
            try:
                Masterinstrumentslist_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                Masterinstrumentslist_lists = paginator.page(1)
            except EmptyPage:
                Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
            




            return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
            {
                'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
                
                'AreaofUselist_list':AreaofUselist_list,
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'semployeename':  semployeename,
            'cmbClassificationID': ClassificationData , 
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
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'bNewID': 0 ,  
                
            })
  







        if 'cmbGetFlow' in request.POST:  

           
            sCodeFinal1 = ""
            sCodeFinal2 = ""
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""
            Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
            if Adminassettypelist_list1:
                sClasscode = Adminassettypelist_list1.scode

            sCategoryCode = ""
            styperefnameA1 = ""
            styperefnameA2 = ""
            styperefnameA3 = ""
            styperefnameA4 = ""
            styperefnameA5 = ""

            if (ID_Categories == 0):
                styperefnameA1 = ""
            else:
                Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                if Adminassetcategorylist_list:
                    sCategoryCode = Adminassetcategorylist_list.scode
                    sClasscode = Adminassetcategorylist_list.styperefname  
                    styperefnameA1 = Adminassetcategorylist_list.styperefname1
                    styperefnameA2 = Adminassetcategorylist_list.styperefname2
                    styperefnameA3 = Adminassetcategorylist_list.styperefname3
                    styperefnameA4 = Adminassetcategorylist_list.styperefname4
                    styperefnameA5 = Adminassetcategorylist_list.styperefname5





 
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/PlantAssetViewDashboardCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })




            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

            
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='ISSUED').order_by('sinstrumentid')

            

            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = Masterinstrumentslist_list.count()
            lRecCount1 = int((lRecCount * 5/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1
            paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
            try:
                Masterinstrumentslist_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                Masterinstrumentslist_lists = paginator.page(1)
            except EmptyPage:
                Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
            




            return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
            {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'sPlantName': sPlantName ,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'semployeename':  semployeename,
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': styperefnameA1,  
            'cmbFlow2label': styperefnameA2,  
            'cmbFlow3label': styperefnameA3,  
            'cmbFlow4label': styperefnameA4,
            'cmbFlow5label': styperefnameA5,    
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ,
            'Adminassetcategorytypelist2_AddNew1OBJ': Adminassetcategorytypelist2_AddNew1OBJ,
            'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ,
            'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ,
            'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ,
            'bNewID': 0 ,  
            
        })
            








 
        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='ISSUED').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        




        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,
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
        }) 
    else: 
         



        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='ISSUED').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        




        return render(request,  'CloudCaliber/PlantAssetViewDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,
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
        }) 




@csrf_exempt
def AdminMasterlistDashboard(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    
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
        ID_Categories =0
        if 'Categories' in request.POST: 
            ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST: 
            Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST: 
            Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST: 
            Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST: 
            Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST: 
            GaugeClass = int(data.get('GaugeClass'))

 


        if 'cmbGetCategory' in request.POST:  

            #request.session['ID_Classification']  =  ClassificationData 

            #request.session['ID_Categories'] = 0
            #request.session['sFlowCode1']   =""
            #request.session['sFlowCode2']   =""
            #request.session['sFlowCode3']   =""
            #request.session['sFlowCode4']   =""
            #request.session['sFlowCode5']   =""
            sCodeFinal1 = ""
            sCodeFinal2 = ""
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""
            Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
            if Adminassettypelist_list1:
                sClasscode = Adminassettypelist_list1.scode

 
         


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

            


            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = Masterinstrumentslist_list.count()
            lRecCount1 = int((lRecCount * 5/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1
            paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
            try:
                Masterinstrumentslist_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                Masterinstrumentslist_lists = paginator.page(1)
            except EmptyPage:
                Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
            
            

            Adminunitlist_list = Adminunitlist.objects.order_by('splantno')




            return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
            {
                'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
                
                'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'lPlantId':lPlantId,
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'semployeename':  request.session['semployeename'] ,
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
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'bNewID': 0 ,  
                
            })
  







        if 'cmbGetFlow' in request.POST:  

           
            sCodeFinal1 = ""
            sCodeFinal2 = ""
        
            lPlantId = request.session['lunitid']  
            sPlantName = request.session['sunitno'] 
            lcompanyid = request.session['lcompanyid']  
            scompantname =  request.session['scompantname']   
            sPlantCode = ""
 

            AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
            if AdminunitlistActive:
                sPlantCode = AdminunitlistActive.splantno 

            sClasscode = ""
            Adminassettypelist_list1 =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ClassificationData) 
            if Adminassettypelist_list1:
                sClasscode = Adminassettypelist_list1.scode

            sCategoryCode = ""
            styperefnameA1 = ""
            styperefnameA2 = ""
            styperefnameA3 = ""
            styperefnameA4 = ""
            styperefnameA5 = ""

            if (ID_Categories == 0):
                styperefnameA1 = ""
            else:
                Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                if Adminassetcategorylist_list:
                    sCategoryCode = Adminassetcategorylist_list.scode
                    sClasscode = Adminassetcategorylist_list.styperefname  
                    styperefnameA1 = Adminassetcategorylist_list.styperefname1
                    styperefnameA2 = Adminassetcategorylist_list.styperefname2
                    styperefnameA3 = Adminassetcategorylist_list.styperefname3
                    styperefnameA4 = Adminassetcategorylist_list.styperefname4
                    styperefnameA5 = Adminassetcategorylist_list.styperefname5





 
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/AdminMasterlistDashboardCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })




            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')

            
            lunitidA=request.session['lunitid']  
            AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     

            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

            

            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = Masterinstrumentslist_list.count()
            lRecCount1 = int((lRecCount * 5/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1
            paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
            try:
                Masterinstrumentslist_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                Masterinstrumentslist_lists = paginator.page(1)
            except EmptyPage:
                Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
            


            Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



            return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
            {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'lPlantId':lPlantId,
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'semployeename':  request.session['semployeename'] ,
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': 0 ,  
            'cmbFlow2ID': 0 ,  
            'cmbFlow3ID': 0 ,  
            'cmbFlow4ID': 0 ,
            'cmbFlow5ID': 0 ,     
            'cmbFlow1label': styperefnameA1,  
            'cmbFlow2label': styperefnameA2,  
            'cmbFlow3label': styperefnameA3,  
            'cmbFlow4label': styperefnameA4,
            'cmbFlow5label': styperefnameA5,    
            'Adminassettypelist_list':Adminassettypelist_list,
            'tcategoriesLst': tcategoriesLst, 
            'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ,
            'Adminassetcategorytypelist2_AddNew1OBJ': Adminassetcategorytypelist2_AddNew1OBJ,
            'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ,
            'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ,
            'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ,
            'bNewID': 0 ,  
            
        })
            








 
        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        

        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')




        return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'lPlantId':lPlantId,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,   
            'semployeename':  request.session['semployeename'] , 
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
        }) 
    else: 
         



        request.session['bContFlag'] =0

        request.session['sPlantCode']   = ""
        request.session['cmbClassificationID'] =""
        request.session['cmbCategoryID'] =""
        request.session['cmbgetFlow1ID'] =""
        request.session['cmbgetFlow2ID'] =""
        request.session['cmbgetFlow3ID'] =""
        request.session['cmbgetFlow4ID'] =""
        request.session['cmbgetFlow5ID'] =""
        request.session['cmbgetFlow6ID'] =""
        request.session['getFlow1Code']  =""
        request.session['getFlow2Code']  =""
        request.session['getFlow3Code']  =""
        request.session['getFlow4Code']  =""
        request.session['getFlowContCode']  =""
        request.session['getFlow5Code']  =""
        request.session['sCategoryCode'] = ""
        request.session['categorytype']= ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5']= ""
        request.session['sSAPCode']  = ""
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

        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus', 'styperefname1', 'styperefname2', 'styperefname3', 'styperefname4', 'styperefname5').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        


        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')



        return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
        {
            'Masterinstrumentslist_lists':Masterinstrumentslist_lists, 
            
            'AreaofUselist_list':AreaofUselist_list,
            'Adminunitlist_list':Adminunitlist_list,
            'lPlantId':lPlantId,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,    
            'semployeename':  request.session['semployeename'] ,
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
        }) 








@csrf_exempt
def AdminMasterlistDashboard1(request):
    request.method = ""
    return AdminMasterlistDashboard(request)

   
























@csrf_exempt
def AdminMasterlistDashboardAA(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboard.html")

@csrf_exempt
def GaugeScheduler(request):
    return render(request, "CloudCaliber/GaugeScheduler.html")

@csrf_exempt
def GaugeIssueReturn(request):
    return render(request, "CloudCaliber/GaugeIssueReturn.html")

@csrf_exempt
def GaugeIssue(request):
    return render(request, "CloudCaliber/GaugeIssue.html")

@csrf_exempt
def GaugeReturn(request):
    return render(request, "CloudCaliber/GaugeReturn.html")

@csrf_exempt
def GaugeMSA(request):
    return render(request, "CloudCaliber/GaugeMSA.html")

@csrf_exempt
def GaugeUtility(request):
    return render(request, "CloudCaliber/GaugeUtility.html")

@csrf_exempt
def GaugeMasters(request):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return home(request)

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

        if request.session:
            request.session.clear()
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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


       
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        


        Adminunitlist_list = Adminunitlist.objects.order_by('splantno')


        return render(request,  'CloudCaliber/AdminMasterlistDashboard.html', 
        {
            'title':'User list', 
            'lPlantId':lPlantId,
            'Adminunitlist_list':Adminunitlist_list,
            'Masterinstrumentslist_lists': Masterinstrumentslist_lists,
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list,
            'cmbClassificationID': int(cmbClassificationID) ,   
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
         
        if request.session:
            request.session.clear()
        request.session['lSerialNo'] = 0
        request.session['sCodeFinal1AK'] = 0

        request.session['lContNo'] = 0
        request.session['ID_Categories'] = 0
        request.session['sCategoryCode'] = ""
        request.session['categorytype'] = ""
        request.session['styperefname1'] = ""
        request.session['styperefname2'] = ""
        request.session['styperefname3'] = ""
        request.session['styperefname4'] = ""
        request.session['styperefname5'] = ""
        request.session['sCodeFinal1A'] = sCodeFinal1
        request.session['sCodeFinal2A'] = sCodeFinal2
    
        request.session['sFlowCode1a'] = ""
        request.session['sFlowCode2a'] = ""
        request.session['sFlowCode3a'] = ""
        request.session['sFlowCode4a'] = ""
        request.session['sFlowCode5a'] = ""
        
        request.session['sFlowCode1']   =""
        request.session['sFlowCode2']   =""
        request.session['sFlowCode3']   =""
        request.session['sFlowCode4']   =""
        request.session['sFlowCode5']   =""

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
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                   

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


        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values('lid', 'sinstrumentid', 'sdescription', 'slocationname',  'splanttype', 'scurrentstatus').filter(scurrentstatus='IDLE').order_by('sinstrumentid')

        

        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Masterinstrumentslist_list.count()
        lRecCount1 = int((lRecCount * 5/100) )
        if (lRecCount1 == 0):
            lRecCount1 =1
        paginator = Paginator(Masterinstrumentslist_list, lRecCount1)
        try:
            Masterinstrumentslist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Masterinstrumentslist_lists = paginator.page(1)
        except EmptyPage:
            Masterinstrumentslist_lists = paginator.page(paginator.num_pages)
        




        return render(request,  'CloudCaliber/GaugeMasters.html', 
        {
            'Masterinstrumentslist_lists':'Masterinstrumentslist_lists', 
            'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'AreaofUselist_list':AreaofUselist_list,
            'cmbClassificationID': int(cmbClassificationID) ,  
            'cmbCategoryID': int(cmbCategoryID) ,   
            'cmbgetFlow1ID': int(cmbgetFlow1ID) ,   
            'cmbgetFlow2ID': int(cmbgetFlow2ID) ,   
            'cmbgetFlow3ID': int(cmbgetFlow3ID) ,   
            'cmbgetFlow4ID': int(cmbgetFlow4ID) ,   
            'cmbgetFlow5ID': int(cmbgetFlow5ID) ,   
            'cmbgetFlow6ID': int(cmbgetFlow6ID) ,    
            'Adminassettypelist_list': Adminassettypelist_list, 
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,


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
def GaugeAdministrator(request):
    return render(request, "CloudCaliber/GaugeAdministrator.html")

 

@csrf_exempt
def CalibrationHistoryDetails(request):
    return render(request, "CloudCaliber/CalibrationHistoryDetails.html")

























@csrf_exempt
def  adminCustomerList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminCustomerListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admincustomerlist_list =  Admincustomerlist.objects.order_by('scustomername')     
                    return render(request,  'CloudCaliber/adminCustomerList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admincustomerlist_list':  Admincustomerlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admincustomerlist_list =  Admincustomerlist.objects.filter(scustomername__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminCustomerList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admincustomerlist_list':  Admincustomerlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admincustomerlist_list =  Admincustomerlist.objects.order_by('scustomername')     
            return render(request,  'CloudCaliber/adminCustomerList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admincustomerlist_list':  Admincustomerlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminCustomerListAdd(request):
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminCustomerList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsCustomer=data.get('txtsCustomer') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Admincustomerlist_AddNewOBJ =  Admincustomerlist(scustomername =txtsCustomer, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            Admincustomerlist_AddNewOBJ.save()

            messages.success(request, 'Customer is Added successfully!')
           
            return   redirect('adminCustomerList')  
            

    else:               
        return render(request, "CloudCaliber/adminCustomerListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminCustomerListDetails(request,lID):
    
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminCustomerList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsCustomer=data.get('txtsCustomer') 

            Admincustomerlist_AddNewOBJ =  Admincustomerlist.objects.get(lid=lID) 

            Admincustomerlist_AddNewOBJ.scustomername =txtsCustomer
            Admincustomerlist_AddNewOBJ.save()

            messages.success(request, 'Customer is Updated successfully!')
            Admincustomerlist_list =  Admincustomerlist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminCustomerListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admincustomerlist_list':  Admincustomerlist_list,  
                        }
                        )

    else: 
        Admincustomerlist_list =  Admincustomerlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminCustomerListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admincustomerlist_list':  Admincustomerlist_list,  
                        }
                        )








































@csrf_exempt
def MasterList(request):
    return render(request, "CloudCaliber/MasterList.html")

















@csrf_exempt
def DueScheduleList(request):
    return render(request, "CloudCaliber/DueScheduleList.html")

















@csrf_exempt
def DueCalendarList(request):
    return render(request, "CloudCaliber/DueCalendarList.html")

















@csrf_exempt
def DuePeriodicList(request):
    return render(request, "CloudCaliber/DuePeriodicList.html")



 










@csrf_exempt
def StartCalibrationList(request):
    return render(request, "CloudCaliber/StartCalibrationList.html")

















@csrf_exempt
def PostponeCalibrationList(request):
    return render(request, "CloudCaliber/PostponeCalibrationList.html")

















@csrf_exempt
def PreponeCalibrationList(request):
    return render(request, "CloudCaliber/PreponeCalibrationList.html")

















@csrf_exempt
def CalibrationPendingDetails(request):
    return render(request, "CloudCaliber/CalibrationPendingDetails.html")

















@csrf_exempt
def CalibrationApprovalDetails(request):
    return render(request, "CloudCaliber/CalibrationApprovalDetails.html")












 






































            






    













@csrf_exempt
def UserListDetails(request,lID):



    lUnitId =["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    sUnitName = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

    iCount =0

    semployeename = ""
    sPlantName = ""
     
    lcompanyId = request.session['lcompanyid']
    
    Unitlist_listStart = Adminunitlist.objects.filter(lcompanyid=lcompanyId).values()     
    if Unitlist_listStart:
        for Adminunitlist_listOBJGetOBJ in Unitlist_listStart.all():            
            lUnitId[iCount]  = Adminunitlist_listOBJGetOBJ['lplantid']
            sUnitName[iCount] = Adminunitlist_listOBJGetOBJ['splantno'] + " | " + Adminunitlist_listOBJGetOBJ['splantname'] 
            iCount += 1


    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('GaugeUserList') 


        if 'cmbReset' in request.POST:  

            semployeeno = request.POST['txtEmployeeId']
            AdminUserlist_AddNewOBJReset = Adminuserlist.objects.get(luserid=lID)
            #AdminUserlist_AddNewOBJReset.boperator = 0 
            AdminUserlist_AddNewOBJReset.bchangepassword = 0
            AdminUserlist_AddNewOBJReset.spassword = semployeeno
            AdminUserlist_AddNewOBJReset.save()
                    
            messages.success(request, 'User Password is Re-set successfully!')

            Unitlist_list = Adminunitlist.objects.order_by('splantno')  
            AdminUser_list = Adminuserlist.objects.get(luserid=lID)              
            return render(request, "CloudCaliber/UserlistDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list, 
                            'AdminUser_listOBJ': AdminUser_list, 
                            'lUnitId1': lUnitId[0],
                            'sUnitName1': sUnitName[0],
                            'lUnitId2': lUnitId[1],
                            'sUnitName2': sUnitName[1],
                            'lUnitId3': lUnitId[2],
                            'sUnitName3': sUnitName[2],
                            'lUnitId4': lUnitId[3],
                            'sUnitName4': sUnitName[3],
                            'lUnitId5': lUnitId[4],
                            'sUnitName5': sUnitName[4],
                            'lUnitId6': lUnitId[5],
                            'sUnitName6': sUnitName[5],
                            'lUnitId7': lUnitId[6],
                            'sUnitName7': sUnitName[6],
                            'lUnitId8': lUnitId[7],
                            'sUnitName8': sUnitName[7],
                            'lUnitId9': lUnitId[8],
                            'sUnitName9': sUnitName[8],
                            'lUnitId10': lUnitId[9],
                            'sUnitName10': sUnitName[9],
                            'lUnitId11': lUnitId[10],
                            'sUnitName11': sUnitName[10],
                            'lUnitId12': lUnitId[11],
                            'sUnitName12': sUnitName[11],
                            'lUnitId13': lUnitId[12],
                            'sUnitName13': sUnitName[12],
                            'lUnitId14': lUnitId[13],
                            'sUnitName14': sUnitName[13],
                            'lUnitId15': lUnitId[14],
                            'sUnitName15': sUnitName[14],
                            'lUnitId16': lUnitId[15],
                            'sUnitName16': sUnitName[15],
                            'lUnitId17': lUnitId[16],
                            'sUnitName17': sUnitName[16],
                            'lUnitId18': lUnitId[17],
                            'sUnitName18': sUnitName[17],
                            'lUnitId19': lUnitId[18],
                            'sUnitName19': sUnitName[18],
                            'lUnitId20': lUnitId[19],
                            'sUnitName20': sUnitName[19],
                            'lUnitId21': lUnitId[20],
                            'sUnitName21': sUnitName[20],
                            'lUnitId22': lUnitId[21],
                            'sUnitName22': sUnitName[21],
                            'lUnitId23': lUnitId[22],
                            'sUnitName23': sUnitName[22],
                            'lUnitId24': lUnitId[23],
                            'sUnitName24': sUnitName[23],
                            'lUnitId25': lUnitId[24],
                            'sUnitName25': sUnitName[24],
                            'lUnitId26': lUnitId[25],
                            'sUnitName26': sUnitName[25],
                            'lUnitId27': lUnitId[26],
                            'sUnitName27': sUnitName[26],
                            'lUnitId28': lUnitId[27],
                            'sUnitName28': sUnitName[27],
                            'lUnitId29': lUnitId[28],
                            'sUnitName29': sUnitName[28],
                            'lUnitId30': lUnitId[29],
                            'sUnitName30': sUnitName[29],
                            'lUnitIdA':'0',
                        }
                        )

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST  
            cmbPlant1 =0 
            cmbPlant2 =0 
            cmbPlant3 =0
            cmbPlantA =0

            if 'cmbPlant1' in request.POST:
                cmbPlant1=request.POST['cmbPlant1'] #('Machine')
                cmbPlantA = 1 
 
 
                    
                semployeename = request.POST['txtUserName']
                semployeeno = request.POST['txtEmployeeId']
                spassword = request.POST['txtPassword']
                semailaddress = request.POST['txtEmailAddress']
                smobile = request.POST['txtMobile']
                sUnit = ""
                sUnit1 = ""
                sUnit2 = ""

                Adminunitlist_listOBJGet = Adminunitlist.objects.filter(lplantid=cmbPlant1).values()
                if Adminunitlist_listOBJGet:
                    for Adminunitlist_listOBJGetOBJ in Adminunitlist_listOBJGet.all():
                        sUnit = Adminunitlist_listOBJGetOBJ['splantno'] + " | " + Adminunitlist_listOBJGetOBJ['splantname'] 
  

                                   
                    
                    bactive = 0
                    if 'bactive' in request.POST:
                        bactive =1 
                    badmin = 0
                    if 'badmin' in request.POST:
                        badmin =1 
                    bmasterlistonlyallplant = 0
                    if 'bmasterlistonlyallplant' in request.POST:
                        bmasterlistonlyallplant =1  
                    bmatrix = 0
                    if 'bmatrix' in request.POST:
                        bmatrix =1 
                    ballfeatures = 0
                    if 'ballfeatures' in request.POST:
                        ballfeatures =1 
                    lUnitId1 = 0
                    if 'lUnitId1' in request.POST:
                        lUnitId1 = int(request.POST['lUnitId1'])
                    lUnitId2 = 0
                    if 'lUnitId2' in request.POST:
                        lUnitId2 = int(request.POST['lUnitId2']) 
                    lUnitId3 = 0
                    if 'lUnitId3' in request.POST:
                        lUnitId3 = int(request.POST['lUnitId3'])  
                    lUnitId4 = 0
                    if 'lUnitId4' in request.POST:
                        lUnitId4 = int(request.POST['lUnitId4']) 
                    lUnitId5 = 0
                    if 'lUnitId5' in request.POST:
                        lUnitId5 = int(request.POST['lUnitId5'])  
                    lUnitId6 = 0
                    if 'lUnitId6' in request.POST:
                        lUnitId6 = int(request.POST['lUnitId6']) 
                    lUnitId7 = 0
                    if 'lUnitId7' in request.POST:
                        lUnitId7 = int(request.POST['lUnitId7']) 
                    lUnitId8 = 0
                    if 'lUnitId8' in request.POST:
                        lUnitId8 = int(request.POST['lUnitId8']) 
                    lUnitId9 = 0
                    if 'lUnitId9' in request.POST:
                        lUnitId9 = int(request.POST['lUnitId9'])  
                    lUnitId10 = 0
                    if 'lUnitId10' in request.POST:
                        lUnitId10 = int(request.POST['lUnitId10'])  
                    lUnitId11 = 0
                    if 'lUnitId11' in request.POST:
                        lUnitId11 = int(request.POST['lUnitId11'])  
                    lUnitId12 = 0
                    if 'lUnitId12' in request.POST:
                        lUnitId12 = int(request.POST['lUnitId12'])  
                    lUnitId13 = 0
                    if 'lUnitId13' in request.POST:
                        lUnitId13 = int(request.POST['lUnitId13'])  
                    lUnitId14 = 0
                    if 'lUnitId14' in request.POST:
                        lUnitId14 = int(request.POST['lUnitId14'])  
                    lUnitId15 = 0
                    if 'lUnitId15' in request.POST:
                        lUnitId15 = int(request.POST['lUnitId15'])  
                    lUnitId16 = 0
                    if 'lUnitId16' in request.POST:
                        lUnitId16 = int(request.POST['lUnitId16'])  
                    lUnitId17 = 0
                    if 'lUnitId17' in request.POST:
                        lUnitId17 = int(request.POST['lUnitId17'])  
                    lUnitId18 = 0
                    if 'lUnitId18' in request.POST:
                        lUnitId18 = int(request.POST['lUnitId18'])  
                    lUnitId19 = 0
                    if 'lUnitId19' in request.POST:
                        lUnitId19 = int(request.POST['lUnitId19'])  
                    lUnitId20 = 0
                    if 'lUnitId20' in request.POST:
                        lUnitId20 = int(request.POST['lUnitId20'])  
                    lUnitId21 = 0
                    if 'lUnitId21' in request.POST:
                        lUnitId21 = int(request.POST['lUnitId21'])  
                    lUnitId22 = 0
                    if 'lUnitId22' in request.POST:
                        lUnitId22 = int(request.POST['lUnitId22'])  
                    lUnitId23 = 0
                    if 'lUnitId23' in request.POST:
                        lUnitId23 = int(request.POST['lUnitId23'])  
                    lUnitId24 = 0
                    if 'lUnitId24' in request.POST:
                        lUnitId24 = int(request.POST['lUnitId24'])  
                    lUnitId25 = 0
                    if 'lUnitId25' in request.POST:
                        lUnitId25 = int(request.POST['lUnitId25'])  
                    lUnitId26 = 0
                    if 'lUnitId26' in request.POST:
                        lUnitId26 = int(request.POST['lUnitId26'])  
                    lUnitId27 = 0
                    if 'lUnitId27' in request.POST:
                        lUnitId27 = int(request.POST['lUnitId27'])  
                    lUnitId28 = 0
                    if 'lUnitId28' in request.POST:
                        lUnitId28 = int(request.POST['lUnitId28'])  
                    lUnitId29 = 0
                    if 'lUnitId29' in request.POST:
                        lUnitId29 = int(request.POST['lUnitId29'])  
                    lUnitId30 = 0
                    if 'lUnitId30' in request.POST:
                        lUnitId30 = int(request.POST['lUnitId30'])
                    ballfeatures1 = 0
                    if 'ballfeatures1' in request.POST:
                        ballfeatures1 =1 
                    ballfeatures2 = 0
                    if 'ballfeatures2' in request.POST:
                        ballfeatures2 =1 
                    ballfeatures3 = 0
                    if 'ballfeatures3' in request.POST:
                        ballfeatures3 =1 
                    ballfeatures4 = 0
                    if 'ballfeatures4' in request.POST:
                        ballfeatures4 =1 
                    ballfeatures5 = 0
                    if 'ballfeatures5' in request.POST:
                        ballfeatures5 =1 
                    ballfeatures6 = 0
                    if 'ballfeatures6' in request.POST:
                        ballfeatures6 =1 
                    ballfeatures7 = 0
                    if 'ballfeatures7' in request.POST:
                        ballfeatures7 =1 
                    ballfeatures8 = 0
                    if 'ballfeatures8' in request.POST:
                        ballfeatures8 =1 
                    ballfeatures9 = 0
                    if 'ballfeatures9' in request.POST:
                        ballfeatures9 =1 
                    ballfeatures10 = 0
                    if 'ballfeatures10' in request.POST:
                        ballfeatures10 =1 
                    ballfeatures11 = 0
                    if 'ballfeatures11' in request.POST:
                        ballfeatures11 =1 
                    ballfeatures12 = 0
                    if 'ballfeatures12' in request.POST:
                        ballfeatures12 =1 
                    ballfeatures13 = 0
                    if 'ballfeatures13' in request.POST:
                        ballfeatures13 =1 
                    ballfeatures14 = 0
                    if 'ballfeatures14' in request.POST:
                        ballfeatures14 =1 
                    ballfeatures15 = 0
                    if 'ballfeatures15' in request.POST:
                        ballfeatures15 =1 
                    ballfeatures16 = 0
                    if 'ballfeatures16' in request.POST:
                        ballfeatures16 =1 
                    ballfeatures17 = 0
                    if 'ballfeatures17' in request.POST:
                        ballfeatures17 =1 
                    ballfeatures18 = 0
                    if 'ballfeatures18' in request.POST:
                        ballfeatures18 =1 
                    ballfeatures19 = 0
                    if 'ballfeatures19' in request.POST:
                        ballfeatures19 =1 
                    ballfeatures20 = 0
                    if 'ballfeatures20' in request.POST:
                        ballfeatures20 =1 
                    ballfeatures21 = 0
                    if 'ballfeatures21' in request.POST:
                        ballfeatures21 =1 
                    ballfeatures22 = 0
                    if 'ballfeatures22' in request.POST:
                        ballfeatures22 =1 
                    ballfeatures23 = 0
                    if 'ballfeatures23' in request.POST:
                        ballfeatures23 =1 
                    ballfeatures24 = 0
                    if 'ballfeatures24' in request.POST:
                        ballfeatures24 =1 
                    ballfeatures25 = 0
                    if 'ballfeatures25' in request.POST:
                        ballfeatures25 =1 
                    ballfeatures26 = 0
                    if 'ballfeatures26' in request.POST:
                        ballfeatures26 =1 
                    ballfeatures27 = 0
                    if 'ballfeatures27' in request.POST:
                        ballfeatures27 =1 
                    ballfeatures28 = 0
                    if 'ballfeatures28' in request.POST:
                        ballfeatures28 =1 
                    ballfeatures29 = 0
                    if 'ballfeatures29' in request.POST:
                        ballfeatures29 =1 
                    ballfeatures30 = 0
                    if 'ballfeatures30' in request.POST:
                        ballfeatures30 =1 
                    bcalibration1 = 0
                    if 'bcalibration1' in request.POST:
                        bcalibration1 =1 
                    bcalibration2 = 0
                    if 'bcalibration2' in request.POST:
                        bcalibration2 =1 
                    bcalibration3 = 0
                    if 'bcalibration3' in request.POST:
                        bcalibration3 =1 
                    bcalibration4 = 0
                    if 'bcalibration4' in request.POST:
                        bcalibration4 =1 
                    bcalibration5 = 0
                    if 'bcalibration5' in request.POST:
                        bcalibration5 =1 
                    bcalibration6 = 0
                    if 'bcalibration6' in request.POST:
                        bcalibration6 =1 
                    bcalibration7 = 0
                    if 'bcalibration7' in request.POST:
                        bcalibration7 =1 
                    bcalibration8 = 0
                    if 'bcalibration8' in request.POST:
                        bcalibration8 =1 
                    bcalibration9 = 0
                    if 'bcalibration9' in request.POST:
                        bcalibration9 =1 
                    bcalibration10 = 0
                    if 'bcalibration10' in request.POST:
                        bcalibration10 =1 
                    bcalibration11 = 0
                    if 'bcalibration11' in request.POST:
                        bcalibration11 =1 
                    bcalibration12 = 0
                    if 'bcalibration12' in request.POST:
                        bcalibration12 =1 
                    bcalibration13 = 0
                    if 'bcalibration13' in request.POST:
                        bcalibration13 =1 
                    bcalibration14 = 0
                    if 'bcalibration14' in request.POST:
                        bcalibration14 =1 
                    bcalibration15 = 0
                    if 'bcalibration15' in request.POST:
                        bcalibration15 =1 
                    bcalibration16 = 0
                    if 'bcalibration16' in request.POST:
                        bcalibration16 =1 
                    bcalibration17 = 0
                    if 'bcalibration17' in request.POST:
                        bcalibration17 =1 
                    bcalibration18 = 0
                    if 'bcalibration18' in request.POST:
                        bcalibration18 =1 
                    bcalibration19 = 0
                    if 'bcalibration19' in request.POST:
                        bcalibration19 =1 
                    bcalibration20 = 0
                    if 'bcalibration20' in request.POST:
                        bcalibration20 =1 
                    bcalibration21 = 0
                    if 'bcalibration21' in request.POST:
                        bcalibration21 =1 
                    bcalibration22 = 0
                    if 'bcalibration22' in request.POST:
                        bcalibration22 =1 
                    bcalibration23 = 0
                    if 'bcalibration23' in request.POST:
                        bcalibration23 =1 
                    bcalibration24 = 0
                    if 'bcalibration24' in request.POST:
                        bcalibration24 =1 
                    bcalibration25 = 0
                    if 'bcalibration25' in request.POST:
                        bcalibration25 =1 
                    bcalibration26 = 0
                    if 'bcalibration26' in request.POST:
                        bcalibration26 =1 
                    bcalibration27 = 0
                    if 'bcalibration27' in request.POST:
                        bcalibration27 =1 
                    bcalibration28 = 0
                    if 'bcalibration28' in request.POST:
                        bcalibration28 =1 
                    bcalibration29 = 0
                    if 'bcalibration29' in request.POST:
                        bcalibration29 =1 
                    bcalibration30 = 0
                    if 'bcalibration30' in request.POST:
                        bcalibration30 =1 
                    bmsa1 = 0
                    if 'bmsa1' in request.POST:
                        bmsa1 =1 
                    bmsa2 = 0
                    if 'bmsa2' in request.POST:
                        bmsa2 =1 
                    bmsa3 = 0
                    if 'bmsa3' in request.POST:
                        bmsa3 =1 
                    bmsa4 = 0
                    if 'bmsa4' in request.POST:
                        bmsa4 =1 
                    bmsa5 = 0
                    if 'bmsa5' in request.POST:
                        bmsa5 =1 
                    bmsa6 = 0
                    if 'bmsa6' in request.POST:
                        bmsa6 =1 
                    bmsa7 = 0
                    if 'bmsa7' in request.POST:
                        bmsa7 =1 
                    bmsa8 = 0
                    if 'bmsa8' in request.POST:
                        bmsa8 =1 
                    bmsa9 = 0
                    if 'bmsa9' in request.POST:
                        bmsa9 =1 
                    bmsa10 = 0
                    if 'bmsa10' in request.POST:
                        bmsa10 =1 
                    bmsa11 = 0
                    if 'bmsa11' in request.POST:
                        bmsa11 =1 
                    bmsa12 = 0
                    if 'bmsa12' in request.POST:
                        bmsa12 =1 
                    bmsa13 = 0
                    if 'bmsa13' in request.POST:
                        bmsa13 =1 
                    bmsa14 = 0
                    if 'bmsa14' in request.POST:
                        bmsa14 =1 
                    bmsa15 = 0
                    if 'bmsa15' in request.POST:
                        bmsa15 =1 
                    bmsa16 = 0
                    if 'bmsa16' in request.POST:
                        bmsa16 =1 
                    bmsa17 = 0
                    if 'bmsa17' in request.POST:
                        bmsa17 =1 
                    bmsa18 = 0
                    if 'bmsa18' in request.POST:
                        bmsa18 =1 
                    bmsa19 = 0
                    if 'bmsa19' in request.POST:
                        bmsa19 =1 
                    bmsa20 = 0
                    if 'bmsa20' in request.POST:
                        bmsa20 =1 
                    bmsa21 = 0
                    if 'bmsa21' in request.POST:
                        bmsa21 =1 
                    bmsa22 = 0
                    if 'bmsa22' in request.POST:
                        bmsa22 =1 
                    bmsa23 = 0
                    if 'bmsa23' in request.POST:
                        bmsa23 =1 
                    bmsa24 = 0
                    if 'bmsa24' in request.POST:
                        bmsa24 =1 
                    bmsa25 = 0
                    if 'bmsa25' in request.POST:
                        bmsa25 =1 
                    bmsa26 = 0
                    if 'bmsa26' in request.POST:
                        bmsa26 =1 
                    bmsa27 = 0
                    if 'bmsa27' in request.POST:
                        bmsa27 =1 
                    bmsa28 = 0
                    if 'bmsa28' in request.POST:
                        bmsa28 =1 
                    bmsa29 = 0
                    if 'bmsa29' in request.POST:
                        bmsa29 =1 
                    bmsa30 = 0
                    if 'bmsa30' in request.POST:
                        bmsa30 =1 
                    bstores1 = 0
                    if 'bstores1' in request.POST:
                        bstores1 =1 
                    bstores2 = 0
                    if 'bstores2' in request.POST:
                        bstores2 =1 
                    bstores3 = 0
                    if 'bstores3' in request.POST:
                        bstores3 =1 
                    bstores4 = 0
                    if 'bstores4' in request.POST:
                        bstores4 =1 
                    bstores5 = 0
                    if 'bstores5' in request.POST:
                        bstores5 =1 
                    bstores6 = 0
                    if 'bstores6' in request.POST:
                        bstores6 =1 
                    bstores7 = 0
                    if 'bstores7' in request.POST:
                        bstores7 =1 
                    bstores8 = 0
                    if 'bstores8' in request.POST:
                        bstores8 =1 
                    bstores9 = 0
                    if 'bstores9' in request.POST:
                        bstores9 =1 
                    bstores10 = 0
                    if 'bstores10' in request.POST:
                        bstores10 =1 
                    bstores11 = 0
                    if 'bstores11' in request.POST:
                        bstores11 =1 
                    bstores12 = 0
                    if 'bstores12' in request.POST:
                        bstores12 =1 
                    bstores13 = 0
                    if 'bstores13' in request.POST:
                        bstores13 =1 
                    bstores14 = 0
                    if 'bstores14' in request.POST:
                        bstores14 =1 
                    bstores15 = 0
                    if 'bstores15' in request.POST:
                        bstores15 =1 
                    bstores16 = 0
                    if 'bstores16' in request.POST:
                        bstores16 =1 
                    bstores17 = 0
                    if 'bstores17' in request.POST:
                        bstores17 =1 
                    bstores18 = 0
                    if 'bstores18' in request.POST:
                        bstores18 =1 
                    bstores19 = 0
                    if 'bstores19' in request.POST:
                        bstores19 =1 
                    bstores20 = 0
                    if 'bstores20' in request.POST:
                        bstores20 =1 
                    bstores21 = 0
                    if 'bstores21' in request.POST:
                        bstores21 =1 
                    bstores22 = 0
                    if 'bstores22' in request.POST:
                        bstores22 =1 
                    bstores23 = 0
                    if 'bstores23' in request.POST:
                        bstores23 =1 
                    bstores24 = 0
                    if 'bstores24' in request.POST:
                        bstores24 =1 
                    bstores25 = 0
                    if 'bstores25' in request.POST:
                        bstores25 =1 
                    bstores26 = 0
                    if 'bstores26' in request.POST:
                        bstores26 =1 
                    bstores27 = 0
                    if 'bstores27' in request.POST:
                        bstores27 =1 
                    bstores28 = 0
                    if 'bstores28' in request.POST:
                        bstores28 =1 
                    bstores29 = 0
                    if 'bstores29' in request.POST:
                        bstores29 =1 
                    bstores30 = 0
                    if 'bstores30' in request.POST:
                        bstores30 =1 
                    breadonly1 = 0
                    if 'breadonly1' in request.POST:
                        breadonly1 =1 
                    breadonly2 = 0
                    if 'breadonly2' in request.POST:
                        breadonly2 =1 
                    breadonly3 = 0
                    if 'breadonly3' in request.POST:
                        breadonly3 =1 
                    breadonly4 = 0
                    if 'breadonly4' in request.POST:
                        breadonly4 =1 
                    breadonly5 = 0
                    if 'breadonly5' in request.POST:
                        breadonly5 =1 
                    breadonly6 = 0
                    if 'breadonly6' in request.POST:
                        breadonly6 =1 
                    breadonly7 = 0
                    if 'breadonly7' in request.POST:
                        breadonly7 =1 
                    breadonly8 = 0
                    if 'breadonly8' in request.POST:
                        breadonly8 =1 
                    breadonly9 = 0
                    if 'breadonly9' in request.POST:
                        breadonly9 =1 
                    breadonly10 = 0
                    if 'breadonly10' in request.POST:
                        breadonly10 =1 
                    breadonly11 = 0
                    if 'breadonly11' in request.POST:
                        breadonly11 =1 
                    breadonly12 = 0
                    if 'breadonly12' in request.POST:
                        breadonly12 =1 
                    breadonly13 = 0
                    if 'breadonly13' in request.POST:
                        breadonly13 =1 
                    breadonly14 = 0
                    if 'breadonly14' in request.POST:
                        breadonly14 =1 
                    breadonly15 = 0
                    if 'breadonly15' in request.POST:
                        breadonly15 =1 
                    breadonly16 = 0
                    if 'breadonly16' in request.POST:
                        breadonly16 =1 
                    breadonly17 = 0
                    if 'breadonly17' in request.POST:
                        breadonly17 =1 
                    breadonly18 = 0
                    if 'breadonly18' in request.POST:
                        breadonly18 =1 
                    breadonly19 = 0
                    if 'breadonly19' in request.POST:
                        breadonly19 =1 
                    breadonly20 = 0
                    if 'breadonly20' in request.POST:
                        breadonly20 =1 
                    breadonly21 = 0
                    if 'breadonly21' in request.POST:
                        breadonly21 =1 
                    breadonly22 = 0
                    if 'breadonly22' in request.POST:
                        breadonly22 =1 
                    breadonly23 = 0
                    if 'breadonly23' in request.POST:
                        breadonly23 =1 
                    breadonly24 = 0
                    if 'breadonly24' in request.POST:
                        breadonly24 =1 
                    breadonly25 = 0
                    if 'breadonly25' in request.POST:
                        breadonly25 =1 
                    breadonly26 = 0
                    if 'breadonly26' in request.POST:
                        breadonly26 =1 
                    breadonly27 = 0
                    if 'breadonly27' in request.POST:
                        breadonly27 =1 
                    breadonly28 = 0
                    if 'breadonly28' in request.POST:
                        breadonly28 =1 
                    breadonly29 = 0
                    if 'breadonly29' in request.POST:
                        breadonly29 =1 
                    breadonly30 = 0
                    if 'breadonly30' in request.POST:
                        breadonly30 =1 

                lroleid =0
                srolename = ""
                lgradeid =0
                sgradename = ""

                AdminUserlist_AddNewOBJ = Adminuserlist.objects.get(luserid=lID) 

                
                AdminUserlist_AddNewOBJ.semployeename = semployeename
                AdminUserlist_AddNewOBJ.semployeeno = semployeeno
                AdminUserlist_AddNewOBJ.spassword = spassword
                AdminUserlist_AddNewOBJ.smobile = smobile
                AdminUserlist_AddNewOBJ.badmin = badmin
                AdminUserlist_AddNewOBJ.boperator = 0
                AdminUserlist_AddNewOBJ.bchangepassword = 0
                AdminUserlist_AddNewOBJ.bmasterlistonlyallplant = bmasterlistonlyallplant
                AdminUserlist_AddNewOBJ.lunitid = cmbPlant1
                AdminUserlist_AddNewOBJ.sunitno = sUnit
                AdminUserlist_AddNewOBJ.sunitname = sUnit
                AdminUserlist_AddNewOBJ.lroleid = 0
                AdminUserlist_AddNewOBJ.srolename = ""
                AdminUserlist_AddNewOBJ.lgradeid = 0
                AdminUserlist_AddNewOBJ.sgradename = ""
                AdminUserlist_AddNewOBJ.semailaddress = semailaddress
                AdminUserlist_AddNewOBJ.bmatrix = bmatrix
                AdminUserlist_AddNewOBJ.lplant1 = 0
                AdminUserlist_AddNewOBJ.bstores = 0
                AdminUserlist_AddNewOBJ.bcalibration = 0
                AdminUserlist_AddNewOBJ.bservice = 0
                AdminUserlist_AddNewOBJ.bmsa = 0
                AdminUserlist_AddNewOBJ.breadwrite = 0
                AdminUserlist_AddNewOBJ.breadonly = 0
                AdminUserlist_AddNewOBJ.ballfeatures = ballfeatures
                AdminUserlist_AddNewOBJ.bactive = bactive
                AdminUserlist_AddNewOBJ.lplant11 = lUnitId1
                AdminUserlist_AddNewOBJ.bstores1 = bstores1
                AdminUserlist_AddNewOBJ.bcalibration1 = bcalibration1
                AdminUserlist_AddNewOBJ.bservice1 = 0
                AdminUserlist_AddNewOBJ.bmsa1 = bmsa1
                AdminUserlist_AddNewOBJ.breadwrite1 = 0
                AdminUserlist_AddNewOBJ.breadonly1 = breadonly1
                AdminUserlist_AddNewOBJ.ballfeatures1 = ballfeatures1
                AdminUserlist_AddNewOBJ.bactive1 = 0
                AdminUserlist_AddNewOBJ.lplant12 = lUnitId2
                AdminUserlist_AddNewOBJ.bstores2 = bstores2
                AdminUserlist_AddNewOBJ.bcalibration2 = bcalibration2
                AdminUserlist_AddNewOBJ.bservice2 = 0
                AdminUserlist_AddNewOBJ.bmsa2 = bmsa2
                AdminUserlist_AddNewOBJ.breadwrite2 = 0
                AdminUserlist_AddNewOBJ.breadonly2 = breadonly2
                AdminUserlist_AddNewOBJ.ballfeatures2 = ballfeatures2
                AdminUserlist_AddNewOBJ.bactive2 = 0
                AdminUserlist_AddNewOBJ.lplant13 = lUnitId3
                AdminUserlist_AddNewOBJ.bstores3 = bstores3
                AdminUserlist_AddNewOBJ.bcalibration3 = bcalibration3
                AdminUserlist_AddNewOBJ.bservice3 = 0
                AdminUserlist_AddNewOBJ.bmsa3 = bmsa3
                AdminUserlist_AddNewOBJ.breadwrite3 = 0
                AdminUserlist_AddNewOBJ.breadonly3 = breadonly3
                AdminUserlist_AddNewOBJ.ballfeatures3 = ballfeatures3
                AdminUserlist_AddNewOBJ.bactive3 = 0
                AdminUserlist_AddNewOBJ.lplant14 = lUnitId4
                AdminUserlist_AddNewOBJ.bstores4 = bstores4
                AdminUserlist_AddNewOBJ.bcalibration4 = bcalibration4
                AdminUserlist_AddNewOBJ.bservice4 = 0
                AdminUserlist_AddNewOBJ.bmsa4 = bmsa4
                AdminUserlist_AddNewOBJ.breadwrite4 = 0
                AdminUserlist_AddNewOBJ.breadonly4 = breadonly4
                AdminUserlist_AddNewOBJ.ballfeatures4 = ballfeatures4
                AdminUserlist_AddNewOBJ.bactive4 = 0
                AdminUserlist_AddNewOBJ.lplant15 = lUnitId5
                AdminUserlist_AddNewOBJ.bstores5 = bstores5
                AdminUserlist_AddNewOBJ.bcalibration5 = bcalibration5
                AdminUserlist_AddNewOBJ.bservice5 = 0
                AdminUserlist_AddNewOBJ.bmsa5 = bmsa5
                AdminUserlist_AddNewOBJ.breadwrite5 = 0
                AdminUserlist_AddNewOBJ.breadonly5 = breadonly5
                AdminUserlist_AddNewOBJ.ballfeatures5 = ballfeatures5
                AdminUserlist_AddNewOBJ.bactive5 = 0
                AdminUserlist_AddNewOBJ.lplant16 = lUnitId6
                AdminUserlist_AddNewOBJ.bstores6 = bstores6
                AdminUserlist_AddNewOBJ.bcalibration6 = bcalibration6
                AdminUserlist_AddNewOBJ.bservice6 = 0
                AdminUserlist_AddNewOBJ.bmsa6 = bmsa6
                AdminUserlist_AddNewOBJ.breadwrite6 = 0
                AdminUserlist_AddNewOBJ.breadonly6 = breadonly6
                AdminUserlist_AddNewOBJ.ballfeatures6 = ballfeatures6
                AdminUserlist_AddNewOBJ.bactive6 = 0
                AdminUserlist_AddNewOBJ.lplant17 = lUnitId7
                AdminUserlist_AddNewOBJ.bstores7 = bstores7
                AdminUserlist_AddNewOBJ.bcalibration7 = bcalibration7
                AdminUserlist_AddNewOBJ.bservice7 = 0
                AdminUserlist_AddNewOBJ.bmsa7 = bmsa7
                AdminUserlist_AddNewOBJ.breadwrite7 = 0
                AdminUserlist_AddNewOBJ.breadonly7 = breadonly7
                AdminUserlist_AddNewOBJ.ballfeatures7 = ballfeatures7
                AdminUserlist_AddNewOBJ.bactive7 = 0
                AdminUserlist_AddNewOBJ.lplant18 = lUnitId8
                AdminUserlist_AddNewOBJ.bstores8 = bstores8
                AdminUserlist_AddNewOBJ.bcalibration8 = bcalibration8
                AdminUserlist_AddNewOBJ.bservice8 = 0
                AdminUserlist_AddNewOBJ.bmsa8 = bmsa8
                AdminUserlist_AddNewOBJ.breadwrite8 = 0
                AdminUserlist_AddNewOBJ.breadonly8 = breadonly8
                AdminUserlist_AddNewOBJ.ballfeatures8 = ballfeatures8
                AdminUserlist_AddNewOBJ.bactive8 = 0
                AdminUserlist_AddNewOBJ.lplant19 = lUnitId9
                AdminUserlist_AddNewOBJ.bstores9 = bstores9
                AdminUserlist_AddNewOBJ.bcalibration9 = bcalibration9
                AdminUserlist_AddNewOBJ.bservice9 = 0
                AdminUserlist_AddNewOBJ.bmsa9 = bmsa9
                AdminUserlist_AddNewOBJ.breadwrite9 = 0
                AdminUserlist_AddNewOBJ.breadonly9 = breadonly9
                AdminUserlist_AddNewOBJ.ballfeatures9 = ballfeatures9
                AdminUserlist_AddNewOBJ.bactive9 = 0
                AdminUserlist_AddNewOBJ.lplant110 = lUnitId10
                AdminUserlist_AddNewOBJ.bstores10 = bstores10
                AdminUserlist_AddNewOBJ.bcalibration10 = bcalibration10
                AdminUserlist_AddNewOBJ.bservice10 = 0
                AdminUserlist_AddNewOBJ.bmsa10 = bmsa10
                AdminUserlist_AddNewOBJ.breadwrite10 = 0
                AdminUserlist_AddNewOBJ.breadonly10 = breadonly10
                AdminUserlist_AddNewOBJ.ballfeatures10 = ballfeatures10
                AdminUserlist_AddNewOBJ.bactive10 = 0
                AdminUserlist_AddNewOBJ.lplant111 = lUnitId11
                AdminUserlist_AddNewOBJ.bstores11 = bstores11
                AdminUserlist_AddNewOBJ.bcalibration11 = bcalibration11
                AdminUserlist_AddNewOBJ.bservice11 = 0
                AdminUserlist_AddNewOBJ.bmsa11 = bmsa11
                AdminUserlist_AddNewOBJ.breadwrite11 = 0
                AdminUserlist_AddNewOBJ.breadonly11 = breadonly11
                AdminUserlist_AddNewOBJ.ballfeatures11 = ballfeatures11
                AdminUserlist_AddNewOBJ.bactive11 = 0
                AdminUserlist_AddNewOBJ.lplant112 = lUnitId12
                AdminUserlist_AddNewOBJ.bstores12 = bstores12
                AdminUserlist_AddNewOBJ.bcalibration12 = bcalibration12
                AdminUserlist_AddNewOBJ.bservice12 = 0
                AdminUserlist_AddNewOBJ.bmsa12 = bmsa12
                AdminUserlist_AddNewOBJ.breadwrite12 = 0
                AdminUserlist_AddNewOBJ.breadonly12 = breadonly12
                AdminUserlist_AddNewOBJ.ballfeatures12 = ballfeatures12
                AdminUserlist_AddNewOBJ.bactive12 = 0
                AdminUserlist_AddNewOBJ.lplant113 = lUnitId13
                AdminUserlist_AddNewOBJ.bstores13 = bstores13
                AdminUserlist_AddNewOBJ.bcalibration13 = bcalibration13
                AdminUserlist_AddNewOBJ.bservice13 = 0
                AdminUserlist_AddNewOBJ.bmsa13 = bmsa13
                AdminUserlist_AddNewOBJ.breadwrite13 = 0
                AdminUserlist_AddNewOBJ.breadonly13 = breadonly13
                AdminUserlist_AddNewOBJ.ballfeatures13 = ballfeatures13
                AdminUserlist_AddNewOBJ.bactive13 = 0
                AdminUserlist_AddNewOBJ.lplant114 = lUnitId14
                AdminUserlist_AddNewOBJ.bstores14 = bstores14
                AdminUserlist_AddNewOBJ.bcalibration14 = bcalibration14
                AdminUserlist_AddNewOBJ.bservice14 = 0
                AdminUserlist_AddNewOBJ.bmsa14 = bmsa14
                AdminUserlist_AddNewOBJ.breadwrite14 = 0
                AdminUserlist_AddNewOBJ.breadonly14 = breadonly14
                AdminUserlist_AddNewOBJ.ballfeatures14 = ballfeatures14
                AdminUserlist_AddNewOBJ.bactive14 = 0
                AdminUserlist_AddNewOBJ.lplant115 = lUnitId15
                AdminUserlist_AddNewOBJ.bstores15 = bstores15
                AdminUserlist_AddNewOBJ.bcalibration15 = bcalibration15
                AdminUserlist_AddNewOBJ.bservice15 = 0
                AdminUserlist_AddNewOBJ.bmsa15 = bmsa15
                AdminUserlist_AddNewOBJ.breadwrite15 = 0
                AdminUserlist_AddNewOBJ.breadonly15 = breadonly15
                AdminUserlist_AddNewOBJ.ballfeatures15 = ballfeatures15
                AdminUserlist_AddNewOBJ.bactive15 = 0
                AdminUserlist_AddNewOBJ.lplant116 = lUnitId16
                AdminUserlist_AddNewOBJ.bstores16 = bstores16
                AdminUserlist_AddNewOBJ.bcalibration16 = bcalibration16
                AdminUserlist_AddNewOBJ.bservice16 = 0
                AdminUserlist_AddNewOBJ.bmsa16 = bmsa16
                AdminUserlist_AddNewOBJ.breadwrite16 = 0
                AdminUserlist_AddNewOBJ.breadonly16 = breadonly16
                AdminUserlist_AddNewOBJ.ballfeatures16 = ballfeatures16
                AdminUserlist_AddNewOBJ.bactive16 = 0
                AdminUserlist_AddNewOBJ.lplant117 = lUnitId17
                AdminUserlist_AddNewOBJ.bstores17 = bstores17
                AdminUserlist_AddNewOBJ.bcalibration17 = bcalibration17
                AdminUserlist_AddNewOBJ.bservice17 = 0
                AdminUserlist_AddNewOBJ.bmsa17 = bmsa17
                AdminUserlist_AddNewOBJ.breadwrite17 = 0
                AdminUserlist_AddNewOBJ.breadonly17 = breadonly17
                AdminUserlist_AddNewOBJ.ballfeatures17 = ballfeatures17
                AdminUserlist_AddNewOBJ.bactive17 = 0
                AdminUserlist_AddNewOBJ.lplant118 = lUnitId18
                AdminUserlist_AddNewOBJ.bstores18 = bstores18
                AdminUserlist_AddNewOBJ.bcalibration18 = bcalibration18
                AdminUserlist_AddNewOBJ.bservice18 = 0
                AdminUserlist_AddNewOBJ.bmsa18 = bmsa18
                AdminUserlist_AddNewOBJ.breadwrite18 = 0
                AdminUserlist_AddNewOBJ.breadonly18 = breadonly18
                AdminUserlist_AddNewOBJ.ballfeatures18 = ballfeatures18
                AdminUserlist_AddNewOBJ.bactive18 = 0
                AdminUserlist_AddNewOBJ.lplant119 = lUnitId19
                AdminUserlist_AddNewOBJ.bstores19 = bstores19
                AdminUserlist_AddNewOBJ.bcalibration19 = bcalibration19
                AdminUserlist_AddNewOBJ.bservice19 = 0
                AdminUserlist_AddNewOBJ.bmsa19 = bmsa19
                AdminUserlist_AddNewOBJ.breadwrite19 = 0
                AdminUserlist_AddNewOBJ.breadonly19 = breadonly19
                AdminUserlist_AddNewOBJ.ballfeatures19 = ballfeatures19
                AdminUserlist_AddNewOBJ.bactive19 = 0
                AdminUserlist_AddNewOBJ.lplant120 = lUnitId20
                AdminUserlist_AddNewOBJ.bstores20 = bstores20
                AdminUserlist_AddNewOBJ.bcalibration20 = bcalibration20
                AdminUserlist_AddNewOBJ.bservice20 = 0
                AdminUserlist_AddNewOBJ.bmsa20 = bmsa20
                AdminUserlist_AddNewOBJ.breadwrite20 = 0
                AdminUserlist_AddNewOBJ.breadonly20 = breadonly20
                AdminUserlist_AddNewOBJ.ballfeatures20 = ballfeatures20
                AdminUserlist_AddNewOBJ.bactive20 = 0
                AdminUserlist_AddNewOBJ.lplant121 = lUnitId21
                AdminUserlist_AddNewOBJ.bstores21 = bstores21
                AdminUserlist_AddNewOBJ.bcalibration21 = bcalibration21
                AdminUserlist_AddNewOBJ.bservice21 = 0
                AdminUserlist_AddNewOBJ.bmsa21 = bmsa21
                AdminUserlist_AddNewOBJ.breadwrite21 = 0
                AdminUserlist_AddNewOBJ.breadonly21 = breadonly21
                AdminUserlist_AddNewOBJ.ballfeatures21 = ballfeatures21
                AdminUserlist_AddNewOBJ.bactive21 = 0
                AdminUserlist_AddNewOBJ.lplant122 = lUnitId22
                AdminUserlist_AddNewOBJ.bstores22 = bstores22
                AdminUserlist_AddNewOBJ.bcalibration22 = bcalibration22
                AdminUserlist_AddNewOBJ.bservice22 = 0
                AdminUserlist_AddNewOBJ.bmsa22 = bmsa22
                AdminUserlist_AddNewOBJ.breadwrite22 = 0
                AdminUserlist_AddNewOBJ.breadonly22 = breadonly22
                AdminUserlist_AddNewOBJ.ballfeatures22 = ballfeatures22
                AdminUserlist_AddNewOBJ.bactive22 = 0
                AdminUserlist_AddNewOBJ.lplant123 = lUnitId23
                AdminUserlist_AddNewOBJ.bstores23 = bstores23
                AdminUserlist_AddNewOBJ.bcalibration23 = bcalibration23
                AdminUserlist_AddNewOBJ.bservice23 = 0
                AdminUserlist_AddNewOBJ.bmsa23 = bmsa23
                AdminUserlist_AddNewOBJ.breadwrite23 = 0
                AdminUserlist_AddNewOBJ.breadonly23 = breadonly23
                AdminUserlist_AddNewOBJ.ballfeatures23 = ballfeatures23
                AdminUserlist_AddNewOBJ.bactive23 = 0
                AdminUserlist_AddNewOBJ.lplant124 = lUnitId24
                AdminUserlist_AddNewOBJ.bstores24 = bstores24
                AdminUserlist_AddNewOBJ.bcalibration24 = bcalibration24
                AdminUserlist_AddNewOBJ.bservice24 = 0
                AdminUserlist_AddNewOBJ.bmsa24 = bmsa24
                AdminUserlist_AddNewOBJ.breadwrite24 = 0
                AdminUserlist_AddNewOBJ.breadonly24 = breadonly24
                AdminUserlist_AddNewOBJ.ballfeatures24 = ballfeatures24
                AdminUserlist_AddNewOBJ.bactive24 = 0
                AdminUserlist_AddNewOBJ.lplant125 = lUnitId25
                AdminUserlist_AddNewOBJ.bstores25 = bstores25
                AdminUserlist_AddNewOBJ.bcalibration25 = bcalibration25
                AdminUserlist_AddNewOBJ.bservice25 = 0
                AdminUserlist_AddNewOBJ.bmsa25 = bmsa25
                AdminUserlist_AddNewOBJ.breadwrite25 = 0
                AdminUserlist_AddNewOBJ.breadonly25 = breadonly25
                AdminUserlist_AddNewOBJ.ballfeatures25 = ballfeatures25
                AdminUserlist_AddNewOBJ.bactive25 = 0
                AdminUserlist_AddNewOBJ.lplant126 = lUnitId26
                AdminUserlist_AddNewOBJ.bstores26 = bstores26
                AdminUserlist_AddNewOBJ.bcalibration26 = bcalibration26
                AdminUserlist_AddNewOBJ.bservice26 = 0
                AdminUserlist_AddNewOBJ.bmsa26 = bmsa26
                AdminUserlist_AddNewOBJ.breadwrite26 = 0
                AdminUserlist_AddNewOBJ.breadonly26 = breadonly26
                AdminUserlist_AddNewOBJ.ballfeatures26 = ballfeatures26
                AdminUserlist_AddNewOBJ.bactive26 = 0
                AdminUserlist_AddNewOBJ.lplant127 = lUnitId27
                AdminUserlist_AddNewOBJ.bstores27 = bstores27
                AdminUserlist_AddNewOBJ.bcalibration27 = bcalibration27
                AdminUserlist_AddNewOBJ.bservice27 = 0
                AdminUserlist_AddNewOBJ.bmsa27 = bmsa27
                AdminUserlist_AddNewOBJ.breadwrite27 = 0
                AdminUserlist_AddNewOBJ.breadonly27 = breadonly27
                AdminUserlist_AddNewOBJ.ballfeatures27 = ballfeatures27
                AdminUserlist_AddNewOBJ.bactive27 = 0
                AdminUserlist_AddNewOBJ.lplant128 = lUnitId28
                AdminUserlist_AddNewOBJ.bstores28 = bstores28
                AdminUserlist_AddNewOBJ.bcalibration28 = bcalibration28
                AdminUserlist_AddNewOBJ.bservice28 = 0
                AdminUserlist_AddNewOBJ.bmsa28 = bmsa28
                AdminUserlist_AddNewOBJ.breadwrite28 = 0
                AdminUserlist_AddNewOBJ.breadonly28 = breadonly28
                AdminUserlist_AddNewOBJ.ballfeatures28 = ballfeatures28
                AdminUserlist_AddNewOBJ.bactive28 = 0
                AdminUserlist_AddNewOBJ.lplant129 = lUnitId29
                AdminUserlist_AddNewOBJ.bstores29 = bstores29
                AdminUserlist_AddNewOBJ.bcalibration29 = bcalibration29
                AdminUserlist_AddNewOBJ.bservice29 = 0
                AdminUserlist_AddNewOBJ.bmsa29 = bmsa29
                AdminUserlist_AddNewOBJ.breadwrite29 = 0
                AdminUserlist_AddNewOBJ.breadonly29 = breadonly29
                AdminUserlist_AddNewOBJ.ballfeatures29 = ballfeatures29
                AdminUserlist_AddNewOBJ.bactive29 = 0
                AdminUserlist_AddNewOBJ.lplant130 = lUnitId30
                AdminUserlist_AddNewOBJ.bstores30 = bstores30
                AdminUserlist_AddNewOBJ.bcalibration30 = bcalibration30
                AdminUserlist_AddNewOBJ.bservice30 = 0
                AdminUserlist_AddNewOBJ.bmsa30 = bmsa30
                AdminUserlist_AddNewOBJ.breadwrite30 = 0
                AdminUserlist_AddNewOBJ.breadonly30 = breadonly30
                AdminUserlist_AddNewOBJ.ballfeatures30 = ballfeatures30
                AdminUserlist_AddNewOBJ.bactive30 = 0


                AdminUserlist_AddNewOBJ.save()
                    
                messages.success(request, 'User is Updated successfully!')

                Unitlist_list = Adminunitlist.objects.order_by('splantno') 
                AdminUser_list = Adminuserlist.objects.get(luserid=lID) 
                

                return render(request, "CloudCaliber/UserlistDetails.html",
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Unitlist_list': Unitlist_list, 
                                'AdminUser_listOBJ': AdminUser_list,
                            'lUnitId1': lUnitId[0],
                            'sUnitName1': sUnitName[0],
                            'lUnitId2': lUnitId[1],
                            'sUnitName2': sUnitName[1],
                            'lUnitId3': lUnitId[2],
                            'sUnitName3': sUnitName[2],
                            'lUnitId4': lUnitId[3],
                            'sUnitName4': sUnitName[3],
                            'lUnitId5': lUnitId[4],
                            'sUnitName5': sUnitName[4],
                            'lUnitId6': lUnitId[5],
                            'sUnitName6': sUnitName[5],
                            'lUnitId7': lUnitId[6],
                            'sUnitName7': sUnitName[6],
                            'lUnitId8': lUnitId[7],
                            'sUnitName8': sUnitName[7],
                            'lUnitId9': lUnitId[8],
                            'sUnitName9': sUnitName[8],
                            'lUnitId10': lUnitId[9],
                            'sUnitName10': sUnitName[9],
                            'lUnitId11': lUnitId[10],
                            'sUnitName11': sUnitName[10],
                            'lUnitId12': lUnitId[11],
                            'sUnitName12': sUnitName[11],
                            'lUnitId13': lUnitId[12],
                            'sUnitName13': sUnitName[12],
                            'lUnitId14': lUnitId[13],
                            'sUnitName14': sUnitName[13],
                            'lUnitId15': lUnitId[14],
                            'sUnitName15': sUnitName[14],
                            'lUnitId16': lUnitId[15],
                            'sUnitName16': sUnitName[15],
                            'lUnitId17': lUnitId[16],
                            'sUnitName17': sUnitName[16],
                            'lUnitId18': lUnitId[17],
                            'sUnitName18': sUnitName[17],
                            'lUnitId19': lUnitId[18],
                            'sUnitName19': sUnitName[18],
                            'lUnitId20': lUnitId[19],
                            'sUnitName20': sUnitName[19],
                            'lUnitId21': lUnitId[20],
                            'sUnitName21': sUnitName[20],
                            'lUnitId22': lUnitId[21],
                            'sUnitName22': sUnitName[21],
                            'lUnitId23': lUnitId[22],
                            'sUnitName23': sUnitName[22],
                            'lUnitId24': lUnitId[23],
                            'sUnitName24': sUnitName[23],
                            'lUnitId25': lUnitId[24],
                            'sUnitName25': sUnitName[24],
                            'lUnitId26': lUnitId[25],
                            'sUnitName26': sUnitName[25],
                            'lUnitId27': lUnitId[26],
                            'sUnitName27': sUnitName[26],
                            'lUnitId28': lUnitId[27],
                            'sUnitName28': sUnitName[27],
                            'lUnitId29': lUnitId[28],
                            'sUnitName29': sUnitName[28],
                            'lUnitId30': lUnitId[29],
                            'sUnitName30': sUnitName[29], 
                            'lUnitIdA':'0',
                            }
                            )
    
    
            else:              
                messages.error(request, 'Plant is not selected. Please Select and then try!')
    else:
        Unitlist_list = Adminunitlist.objects.order_by('splantno')  
        AdminUser_list = Adminuserlist.objects.get(luserid=lID)              
        return render(request, "CloudCaliber/UserlistDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list, 
                            'AdminUser_listOBJ': AdminUser_list, 
                            'lUnitId1': lUnitId[0],
                            'sUnitName1': sUnitName[0],
                            'lUnitId2': lUnitId[1],
                            'sUnitName2': sUnitName[1],
                            'lUnitId3': lUnitId[2],
                            'sUnitName3': sUnitName[2],
                            'lUnitId4': lUnitId[3],
                            'sUnitName4': sUnitName[3],
                            'lUnitId5': lUnitId[4],
                            'sUnitName5': sUnitName[4],
                            'lUnitId6': lUnitId[5],
                            'sUnitName6': sUnitName[5],
                            'lUnitId7': lUnitId[6],
                            'sUnitName7': sUnitName[6],
                            'lUnitId8': lUnitId[7],
                            'sUnitName8': sUnitName[7],
                            'lUnitId9': lUnitId[8],
                            'sUnitName9': sUnitName[8],
                            'lUnitId10': lUnitId[9],
                            'sUnitName10': sUnitName[9],
                            'lUnitId11': lUnitId[10],
                            'sUnitName11': sUnitName[10],
                            'lUnitId12': lUnitId[11],
                            'sUnitName12': sUnitName[11],
                            'lUnitId13': lUnitId[12],
                            'sUnitName13': sUnitName[12],
                            'lUnitId14': lUnitId[13],
                            'sUnitName14': sUnitName[13],
                            'lUnitId15': lUnitId[14],
                            'sUnitName15': sUnitName[14],
                            'lUnitId16': lUnitId[15],
                            'sUnitName16': sUnitName[15],
                            'lUnitId17': lUnitId[16],
                            'sUnitName17': sUnitName[16],
                            'lUnitId18': lUnitId[17],
                            'sUnitName18': sUnitName[17],
                            'lUnitId19': lUnitId[18],
                            'sUnitName19': sUnitName[18],
                            'lUnitId20': lUnitId[19],
                            'sUnitName20': sUnitName[19],
                            'lUnitId21': lUnitId[20],
                            'sUnitName21': sUnitName[20],
                            'lUnitId22': lUnitId[21],
                            'sUnitName22': sUnitName[21],
                            'lUnitId23': lUnitId[22],
                            'sUnitName23': sUnitName[22],
                            'lUnitId24': lUnitId[23],
                            'sUnitName24': sUnitName[23],
                            'lUnitId25': lUnitId[24],
                            'sUnitName25': sUnitName[24],
                            'lUnitId26': lUnitId[25],
                            'sUnitName26': sUnitName[25],
                            'lUnitId27': lUnitId[26],
                            'sUnitName27': sUnitName[26],
                            'lUnitId28': lUnitId[27],
                            'sUnitName28': sUnitName[27],
                            'lUnitId29': lUnitId[28],
                            'sUnitName29': sUnitName[28],
                            'lUnitId30': lUnitId[29],
                            'sUnitName30': sUnitName[29],
                            'lUnitIdA':'0',
                        }
                        )




@csrf_exempt
def UserListAdd(request): 


    lUnitId1 ="0"
    sUnitName1 = ""
    lUnitId2 ="0"
    sUnitName2 = ""
    lUnitId3 ="0"
    sUnitName3 = ""
    lUnitId4 ="0"
    sUnitName4 = ""
    lUnitId5 ="0"
    sUnitName5 = ""
    lUnitId6 ="0"
    sUnitName6 = ""
    lUnitId7 ="0"
    sUnitName7 = ""
    lUnitId8 ="0"
    sUnitName8 = ""
    lUnitId9 ="0"
    sUnitName9 = ""
    lUnitId10 ="0"
    sUnitName10 = ""
    sUnitName11 = ""
    lUnitId12 ="0"
    sUnitName12 = ""
    lUnitId13 ="0"
    sUnitName13 = ""
    lUnitId14 ="0"
    sUnitName14 = ""
    lUnitId15 ="0"
    sUnitName15 = ""
    lUnitId16 ="0"
    sUnitName16 = ""
    lUnitId17 ="0"
    sUnitName17 = ""
    lUnitId18 ="0"
    sUnitName18 = ""
    lUnitId19 ="0"
    sUnitName19 = ""
    lUnitId20 ="0"
    sUnitName20 = ""
    sUnitName21 = ""
    lUnitId22 ="0"
    sUnitName22 = ""
    lUnitId23 ="0"
    sUnitName23 = ""
    lUnitId24 ="0"
    sUnitName24 = ""
    lUnitId25 ="0"
    sUnitName25 = ""
    lUnitId26 ="0"
    sUnitName26 = ""
    lUnitId27 ="0"
    sUnitName27 = ""
    lUnitId28 ="0"
    sUnitName28 = ""
    lUnitId29 ="0"
    sUnitName29 = ""
    lUnitId30 ="0"
    sUnitName30 = ""

    lUnitId =["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    sUnitName = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

    iCount =0
    
    lcompanyId = request.session['lcompanyid']
    Unitlist_listStart = Adminunitlist.objects.filter(lcompanyid=lcompanyId).values()     
    if Unitlist_listStart:
        for Adminunitlist_listOBJGetOBJ in Unitlist_listStart.all():            
            lUnitId[iCount]  = Adminunitlist_listOBJGetOBJ['lplantid']
            sUnitName[iCount] = Adminunitlist_listOBJGetOBJ['splantno'] + " | " + Adminunitlist_listOBJGetOBJ['splantname'] 
            iCount += 1

    
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('GaugeUserList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST 
            AdminuserlistsFind = Adminuserlist.objects.filter(semployeeno=data.get("txtEmployeeId")).values()
            if AdminuserlistsFind:
            
                messages.error(request, 'User is Duplicate and cannot be createds!')

                Unitlist_list = Adminunitlist.objects.order_by('splantno')               
                return render(request, "CloudCaliber/UserlistAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list, 
                            'lUnitId1': lUnitId[0],
                            'sUnitName1': sUnitName[0],
                            'lUnitId2': lUnitId[1],
                            'sUnitName2': sUnitName[1],
                            'lUnitId3': lUnitId[2],
                            'sUnitName3': sUnitName[2],
                            'lUnitId4': lUnitId[3],
                            'sUnitName4': sUnitName[3],
                            'lUnitId5': lUnitId[4],
                            'sUnitName5': sUnitName[4],
                            'lUnitId6': lUnitId[5],
                            'sUnitName6': sUnitName[5],
                            'lUnitId7': lUnitId[6],
                            'sUnitName7': sUnitName[6],
                            'lUnitId8': lUnitId[7],
                            'sUnitName8': sUnitName[7],
                            'lUnitId9': lUnitId[8],
                            'sUnitName9': sUnitName[8],
                            'lUnitId10': lUnitId[9],
                            'sUnitName10': sUnitName[9],
                            'lUnitId11': lUnitId[10],
                            'sUnitName11': sUnitName[10],
                            'lUnitId12': lUnitId[11],
                            'sUnitName12': sUnitName[11],
                            'lUnitId13': lUnitId[12],
                            'sUnitName13': sUnitName[12],
                            'lUnitId14': lUnitId[13],
                            'sUnitName14': sUnitName[13],
                            'lUnitId15': lUnitId[14],
                            'sUnitName15': sUnitName[14],
                            'lUnitId16': lUnitId[15],
                            'sUnitName16': sUnitName[15],
                            'lUnitId17': lUnitId[16],
                            'sUnitName17': sUnitName[16],
                            'lUnitId18': lUnitId[17],
                            'sUnitName18': sUnitName[17],
                            'lUnitId19': lUnitId[18],
                            'sUnitName19': sUnitName[18],
                            'lUnitId20': lUnitId[19],
                            'sUnitName20': sUnitName[19],
                            'lUnitId21': lUnitId[20],
                            'sUnitName21': sUnitName[20],
                            'lUnitId22': lUnitId[21],
                            'sUnitName22': sUnitName[21],
                            'lUnitId23': lUnitId[22],
                            'sUnitName23': sUnitName[22],
                            'lUnitId24': lUnitId[23],
                            'sUnitName24': sUnitName[23],
                            'lUnitId25': lUnitId[24],
                            'sUnitName25': sUnitName[24],
                            'lUnitId26': lUnitId[25],
                            'sUnitName26': sUnitName[25],
                            'lUnitId27': lUnitId[26],
                            'sUnitName27': sUnitName[26],
                            'lUnitId28': lUnitId[27],
                            'sUnitName28': sUnitName[27],
                            'lUnitId29': lUnitId[28],
                            'sUnitName29': sUnitName[28],
                            'lUnitId30': lUnitId[29],
                            'sUnitName30': sUnitName[29],
                            'lUnitIdA':'0',

                        }
                        )
            else:
                cmbPlant1 =0 
                cmbPlant2 =0 
                cmbPlant3 =0
                cmbPlantA =0

                if 'cmbPlant1' in request.POST:
                    cmbPlant1=request.POST['cmbPlant1'] #('Machine')
                    cmbPlantA = 1 
 
                    
                    semployeename = request.POST['txtUserName']
                    semployeeno = request.POST['txtEmployeeId']
                    spassword = request.POST['txtPassword']
                    semailaddress = request.POST['txtEmailAddress']
                    smobile = request.POST['txtMobile']
                    sUnit = ""
                    sUnit1 = ""
                    sUnit2 = ""

                    Adminunitlist_listOBJGet = Adminunitlist.objects.filter(lplantid=cmbPlant1).values()
                    if Adminunitlist_listOBJGet:
                        for Adminunitlist_listOBJGetOBJ in Adminunitlist_listOBJGet.all():
                            sUnit = Adminunitlist_listOBJGetOBJ['splantno'] + " | " + Adminunitlist_listOBJGetOBJ['splantname'] 
                    
                    
                    bactive = 0
                    if 'bactive' in request.POST:
                        bactive =1 
                    badmin = 0
                    if 'badmin' in request.POST:
                        badmin =1 
                    bmasterlistonlyallplant = 0
                    if 'bmasterlistonlyallplant' in request.POST:
                        bmasterlistonlyallplant =1 
                    bmatrix = 0
                    if 'bmatrix' in request.POST:
                        bmatrix =1 
                    ballfeatures = 0
                    if 'ballfeatures' in request.POST:
                        ballfeatures =1 
                    lUnitId1 = 0
                    if 'lUnitId1' in request.POST:
                        lUnitId1 = int(request.POST['lUnitId1'])
                    lUnitId2 = 0
                    if 'lUnitId2' in request.POST:
                        lUnitId2 = int(request.POST['lUnitId2']) 
                    lUnitId3 = 0
                    if 'lUnitId3' in request.POST:
                        lUnitId3 = int(request.POST['lUnitId3'])  
                    lUnitId4 = 0
                    if 'lUnitId4' in request.POST:
                        lUnitId4 = int(request.POST['lUnitId4']) 
                    lUnitId5 = 0
                    if 'lUnitId5' in request.POST:
                        lUnitId5 = int(request.POST['lUnitId5'])  
                    lUnitId6 = 0
                    if 'lUnitId6' in request.POST:
                        lUnitId6 = int(request.POST['lUnitId6']) 
                    lUnitId7 = 0
                    if 'lUnitId7' in request.POST:
                        lUnitId7 = int(request.POST['lUnitId7']) 
                    lUnitId8 = 0
                    if 'lUnitId8' in request.POST:
                        lUnitId8 = int(request.POST['lUnitId8']) 
                    lUnitId9 = 0
                    if 'lUnitId9' in request.POST:
                        lUnitId9 = int(request.POST['lUnitId9'])  
                    lUnitId10 = 0
                    if 'lUnitId10' in request.POST:
                        lUnitId10 = int(request.POST['lUnitId10'])  
                    lUnitId11 = 0
                    if 'lUnitId11' in request.POST:
                        lUnitId11 = int(request.POST['lUnitId11'])  
                    lUnitId12 = 0
                    if 'lUnitId12' in request.POST:
                        lUnitId12 = int(request.POST['lUnitId12'])  
                    lUnitId13 = 0
                    if 'lUnitId13' in request.POST:
                        lUnitId13 = int(request.POST['lUnitId13'])  
                    lUnitId14 = 0
                    if 'lUnitId14' in request.POST:
                        lUnitId14 = int(request.POST['lUnitId14'])  
                    lUnitId15 = 0
                    if 'lUnitId15' in request.POST:
                        lUnitId15 = int(request.POST['lUnitId15'])  
                    lUnitId16 = 0
                    if 'lUnitId16' in request.POST:
                        lUnitId16 = int(request.POST['lUnitId16'])  
                    lUnitId17 = 0
                    if 'lUnitId17' in request.POST:
                        lUnitId17 = int(request.POST['lUnitId17'])  
                    lUnitId18 = 0
                    if 'lUnitId18' in request.POST:
                        lUnitId18 = int(request.POST['lUnitId18'])  
                    lUnitId19 = 0
                    if 'lUnitId19' in request.POST:
                        lUnitId19 = int(request.POST['lUnitId19'])  
                    lUnitId20 = 0
                    if 'lUnitId20' in request.POST:
                        lUnitId20 = int(request.POST['lUnitId20'])  
                    lUnitId21 = 0
                    if 'lUnitId21' in request.POST:
                        lUnitId21 = int(request.POST['lUnitId21'])  
                    lUnitId22 = 0
                    if 'lUnitId22' in request.POST:
                        lUnitId22 = int(request.POST['lUnitId22'])  
                    lUnitId23 = 0
                    if 'lUnitId23' in request.POST:
                        lUnitId23 = int(request.POST['lUnitId23'])  
                    lUnitId24 = 0
                    if 'lUnitId24' in request.POST:
                        lUnitId24 = int(request.POST['lUnitId24'])  
                    lUnitId25 = 0
                    if 'lUnitId25' in request.POST:
                        lUnitId25 = int(request.POST['lUnitId25'])  
                    lUnitId26 = 0
                    if 'lUnitId26' in request.POST:
                        lUnitId26 = int(request.POST['lUnitId26'])  
                    lUnitId27 = 0
                    if 'lUnitId27' in request.POST:
                        lUnitId27 = int(request.POST['lUnitId27'])  
                    lUnitId28 = 0
                    if 'lUnitId28' in request.POST:
                        lUnitId28 = int(request.POST['lUnitId28'])  
                    lUnitId29 = 0
                    if 'lUnitId29' in request.POST:
                        lUnitId29 = int(request.POST['lUnitId29'])  
                    lUnitId30 = 0
                    if 'lUnitId30' in request.POST:
                        lUnitId30 = int(request.POST['lUnitId30'])
                    ballfeatures1 = 0
                    if 'ballfeatures1' in request.POST:
                        ballfeatures1 =1 
                    ballfeatures2 = 0
                    if 'ballfeatures2' in request.POST:
                        ballfeatures2 =1 
                    ballfeatures3 = 0
                    if 'ballfeatures3' in request.POST:
                        ballfeatures3 =1 
                    ballfeatures4 = 0
                    if 'ballfeatures4' in request.POST:
                        ballfeatures4 =1 
                    ballfeatures5 = 0
                    if 'ballfeatures5' in request.POST:
                        ballfeatures5 =1 
                    ballfeatures6 = 0
                    if 'ballfeatures6' in request.POST:
                        ballfeatures6 =1 
                    ballfeatures7 = 0
                    if 'ballfeatures7' in request.POST:
                        ballfeatures7 =1 
                    ballfeatures8 = 0
                    if 'ballfeatures8' in request.POST:
                        ballfeatures8 =1 
                    ballfeatures9 = 0
                    if 'ballfeatures9' in request.POST:
                        ballfeatures9 =1 
                    ballfeatures10 = 0
                    if 'ballfeatures10' in request.POST:
                        ballfeatures10 =1 
                    ballfeatures11 = 0
                    if 'ballfeatures11' in request.POST:
                        ballfeatures11 =1 
                    ballfeatures12 = 0
                    if 'ballfeatures12' in request.POST:
                        ballfeatures12 =1 
                    ballfeatures13 = 0
                    if 'ballfeatures13' in request.POST:
                        ballfeatures13 =1 
                    ballfeatures14 = 0
                    if 'ballfeatures14' in request.POST:
                        ballfeatures14 =1 
                    ballfeatures15 = 0
                    if 'ballfeatures15' in request.POST:
                        ballfeatures15 =1 
                    ballfeatures16 = 0
                    if 'ballfeatures16' in request.POST:
                        ballfeatures16 =1 
                    ballfeatures17 = 0
                    if 'ballfeatures17' in request.POST:
                        ballfeatures17 =1 
                    ballfeatures18 = 0
                    if 'ballfeatures18' in request.POST:
                        ballfeatures18 =1 
                    ballfeatures19 = 0
                    if 'ballfeatures19' in request.POST:
                        ballfeatures19 =1 
                    ballfeatures20 = 0
                    if 'ballfeatures20' in request.POST:
                        ballfeatures20 =1 
                    ballfeatures21 = 0
                    if 'ballfeatures21' in request.POST:
                        ballfeatures21 =1 
                    ballfeatures22 = 0
                    if 'ballfeatures22' in request.POST:
                        ballfeatures22 =1 
                    ballfeatures23 = 0
                    if 'ballfeatures23' in request.POST:
                        ballfeatures23 =1 
                    ballfeatures24 = 0
                    if 'ballfeatures24' in request.POST:
                        ballfeatures24 =1 
                    ballfeatures25 = 0
                    if 'ballfeatures25' in request.POST:
                        ballfeatures25 =1 
                    ballfeatures26 = 0
                    if 'ballfeatures26' in request.POST:
                        ballfeatures26 =1 
                    ballfeatures27 = 0
                    if 'ballfeatures27' in request.POST:
                        ballfeatures27 =1 
                    ballfeatures28 = 0
                    if 'ballfeatures28' in request.POST:
                        ballfeatures28 =1 
                    ballfeatures29 = 0
                    if 'ballfeatures29' in request.POST:
                        ballfeatures29 =1 
                    ballfeatures30 = 0
                    if 'ballfeatures30' in request.POST:
                        ballfeatures30 =1 
                    bcalibration1 = 0
                    if 'bcalibration1' in request.POST:
                        bcalibration1 =1 
                    bcalibration2 = 0
                    if 'bcalibration2' in request.POST:
                        bcalibration2 =1 
                    bcalibration3 = 0
                    if 'bcalibration3' in request.POST:
                        bcalibration3 =1 
                    bcalibration4 = 0
                    if 'bcalibration4' in request.POST:
                        bcalibration4 =1 
                    bcalibration5 = 0
                    if 'bcalibration5' in request.POST:
                        bcalibration5 =1 
                    bcalibration6 = 0
                    if 'bcalibration6' in request.POST:
                        bcalibration6 =1 
                    bcalibration7 = 0
                    if 'bcalibration7' in request.POST:
                        bcalibration7 =1 
                    bcalibration8 = 0
                    if 'bcalibration8' in request.POST:
                        bcalibration8 =1 
                    bcalibration9 = 0
                    if 'bcalibration9' in request.POST:
                        bcalibration9 =1 
                    bcalibration10 = 0
                    if 'bcalibration10' in request.POST:
                        bcalibration10 =1 
                    bcalibration11 = 0
                    if 'bcalibration11' in request.POST:
                        bcalibration11 =1 
                    bcalibration12 = 0
                    if 'bcalibration12' in request.POST:
                        bcalibration12 =1 
                    bcalibration13 = 0
                    if 'bcalibration13' in request.POST:
                        bcalibration13 =1 
                    bcalibration14 = 0
                    if 'bcalibration14' in request.POST:
                        bcalibration14 =1 
                    bcalibration15 = 0
                    if 'bcalibration15' in request.POST:
                        bcalibration15 =1 
                    bcalibration16 = 0
                    if 'bcalibration16' in request.POST:
                        bcalibration16 =1 
                    bcalibration17 = 0
                    if 'bcalibration17' in request.POST:
                        bcalibration17 =1 
                    bcalibration18 = 0
                    if 'bcalibration18' in request.POST:
                        bcalibration18 =1 
                    bcalibration19 = 0
                    if 'bcalibration19' in request.POST:
                        bcalibration19 =1 
                    bcalibration20 = 0
                    if 'bcalibration20' in request.POST:
                        bcalibration20 =1 
                    bcalibration21 = 0
                    if 'bcalibration21' in request.POST:
                        bcalibration21 =1 
                    bcalibration22 = 0
                    if 'bcalibration22' in request.POST:
                        bcalibration22 =1 
                    bcalibration23 = 0
                    if 'bcalibration23' in request.POST:
                        bcalibration23 =1 
                    bcalibration24 = 0
                    if 'bcalibration24' in request.POST:
                        bcalibration24 =1 
                    bcalibration25 = 0
                    if 'bcalibration25' in request.POST:
                        bcalibration25 =1 
                    bcalibration26 = 0
                    if 'bcalibration26' in request.POST:
                        bcalibration26 =1 
                    bcalibration27 = 0
                    if 'bcalibration27' in request.POST:
                        bcalibration27 =1 
                    bcalibration28 = 0
                    if 'bcalibration28' in request.POST:
                        bcalibration28 =1 
                    bcalibration29 = 0
                    if 'bcalibration29' in request.POST:
                        bcalibration29 =1 
                    bcalibration30 = 0
                    if 'bcalibration30' in request.POST:
                        bcalibration30 =1 
                    bmsa1 = 0
                    if 'bmsa1' in request.POST:
                        bmsa1 =1 
                    bmsa2 = 0
                    if 'bmsa2' in request.POST:
                        bmsa2 =1 
                    bmsa3 = 0
                    if 'bmsa3' in request.POST:
                        bmsa3 =1 
                    bmsa4 = 0
                    if 'bmsa4' in request.POST:
                        bmsa4 =1 
                    bmsa5 = 0
                    if 'bmsa5' in request.POST:
                        bmsa5 =1 
                    bmsa6 = 0
                    if 'bmsa6' in request.POST:
                        bmsa6 =1 
                    bmsa7 = 0
                    if 'bmsa7' in request.POST:
                        bmsa7 =1 
                    bmsa8 = 0
                    if 'bmsa8' in request.POST:
                        bmsa8 =1 
                    bmsa9 = 0
                    if 'bmsa9' in request.POST:
                        bmsa9 =1 
                    bmsa10 = 0
                    if 'bmsa10' in request.POST:
                        bmsa10 =1 
                    bmsa11 = 0
                    if 'bmsa11' in request.POST:
                        bmsa11 =1 
                    bmsa12 = 0
                    if 'bmsa12' in request.POST:
                        bmsa12 =1 
                    bmsa13 = 0
                    if 'bmsa13' in request.POST:
                        bmsa13 =1 
                    bmsa14 = 0
                    if 'bmsa14' in request.POST:
                        bmsa14 =1 
                    bmsa15 = 0
                    if 'bmsa15' in request.POST:
                        bmsa15 =1 
                    bmsa16 = 0
                    if 'bmsa16' in request.POST:
                        bmsa16 =1 
                    bmsa17 = 0
                    if 'bmsa17' in request.POST:
                        bmsa17 =1 
                    bmsa18 = 0
                    if 'bmsa18' in request.POST:
                        bmsa18 =1 
                    bmsa19 = 0
                    if 'bmsa19' in request.POST:
                        bmsa19 =1 
                    bmsa20 = 0
                    if 'bmsa20' in request.POST:
                        bmsa20 =1 
                    bmsa21 = 0
                    if 'bmsa21' in request.POST:
                        bmsa21 =1 
                    bmsa22 = 0
                    if 'bmsa22' in request.POST:
                        bmsa22 =1 
                    bmsa23 = 0
                    if 'bmsa23' in request.POST:
                        bmsa23 =1 
                    bmsa24 = 0
                    if 'bmsa24' in request.POST:
                        bmsa24 =1 
                    bmsa25 = 0
                    if 'bmsa25' in request.POST:
                        bmsa25 =1 
                    bmsa26 = 0
                    if 'bmsa26' in request.POST:
                        bmsa26 =1 
                    bmsa27 = 0
                    if 'bmsa27' in request.POST:
                        bmsa27 =1 
                    bmsa28 = 0
                    if 'bmsa28' in request.POST:
                        bmsa28 =1 
                    bmsa29 = 0
                    if 'bmsa29' in request.POST:
                        bmsa29 =1 
                    bmsa30 = 0
                    if 'bmsa30' in request.POST:
                        bmsa30 =1 
                    bstores1 = 0
                    if 'bstores1' in request.POST:
                        bstores1 =1 
                    bstores2 = 0
                    if 'bstores2' in request.POST:
                        bstores2 =1 
                    bstores3 = 0
                    if 'bstores3' in request.POST:
                        bstores3 =1 
                    bstores4 = 0
                    if 'bstores4' in request.POST:
                        bstores4 =1 
                    bstores5 = 0
                    if 'bstores5' in request.POST:
                        bstores5 =1 
                    bstores6 = 0
                    if 'bstores6' in request.POST:
                        bstores6 =1 
                    bstores7 = 0
                    if 'bstores7' in request.POST:
                        bstores7 =1 
                    bstores8 = 0
                    if 'bstores8' in request.POST:
                        bstores8 =1 
                    bstores9 = 0
                    if 'bstores9' in request.POST:
                        bstores9 =1 
                    bstores10 = 0
                    if 'bstores10' in request.POST:
                        bstores10 =1 
                    bstores11 = 0
                    if 'bstores11' in request.POST:
                        bstores11 =1 
                    bstores12 = 0
                    if 'bstores12' in request.POST:
                        bstores12 =1 
                    bstores13 = 0
                    if 'bstores13' in request.POST:
                        bstores13 =1 
                    bstores14 = 0
                    if 'bstores14' in request.POST:
                        bstores14 =1 
                    bstores15 = 0
                    if 'bstores15' in request.POST:
                        bstores15 =1 
                    bstores16 = 0
                    if 'bstores16' in request.POST:
                        bstores16 =1 
                    bstores17 = 0
                    if 'bstores17' in request.POST:
                        bstores17 =1 
                    bstores18 = 0
                    if 'bstores18' in request.POST:
                        bstores18 =1 
                    bstores19 = 0
                    if 'bstores19' in request.POST:
                        bstores19 =1 
                    bstores20 = 0
                    if 'bstores20' in request.POST:
                        bstores20 =1 
                    bstores21 = 0
                    if 'bstores21' in request.POST:
                        bstores21 =1 
                    bstores22 = 0
                    if 'bstores22' in request.POST:
                        bstores22 =1 
                    bstores23 = 0
                    if 'bstores23' in request.POST:
                        bstores23 =1 
                    bstores24 = 0
                    if 'bstores24' in request.POST:
                        bstores24 =1 
                    bstores25 = 0
                    if 'bstores25' in request.POST:
                        bstores25 =1 
                    bstores26 = 0
                    if 'bstores26' in request.POST:
                        bstores26 =1 
                    bstores27 = 0
                    if 'bstores27' in request.POST:
                        bstores27 =1 
                    bstores28 = 0
                    if 'bstores28' in request.POST:
                        bstores28 =1 
                    bstores29 = 0
                    if 'bstores29' in request.POST:
                        bstores29 =1 
                    bstores30 = 0
                    if 'bstores30' in request.POST:
                        bstores30 =1 
                    breadonly1 = 0
                    if 'breadonly1' in request.POST:
                        breadonly1 =1 
                    breadonly2 = 0
                    if 'breadonly2' in request.POST:
                        breadonly2 =1 
                    breadonly3 = 0
                    if 'breadonly3' in request.POST:
                        breadonly3 =1 
                    breadonly4 = 0
                    if 'breadonly4' in request.POST:
                        breadonly4 =1 
                    breadonly5 = 0
                    if 'breadonly5' in request.POST:
                        breadonly5 =1 
                    breadonly6 = 0
                    if 'breadonly6' in request.POST:
                        breadonly6 =1 
                    breadonly7 = 0
                    if 'breadonly7' in request.POST:
                        breadonly7 =1 
                    breadonly8 = 0
                    if 'breadonly8' in request.POST:
                        breadonly8 =1 
                    breadonly9 = 0
                    if 'breadonly9' in request.POST:
                        breadonly9 =1 
                    breadonly10 = 0
                    if 'breadonly10' in request.POST:
                        breadonly10 =1 
                    breadonly11 = 0
                    if 'breadonly11' in request.POST:
                        breadonly11 =1 
                    breadonly12 = 0
                    if 'breadonly12' in request.POST:
                        breadonly12 =1 
                    breadonly13 = 0
                    if 'breadonly13' in request.POST:
                        breadonly13 =1 
                    breadonly14 = 0
                    if 'breadonly14' in request.POST:
                        breadonly14 =1 
                    breadonly15 = 0
                    if 'breadonly15' in request.POST:
                        breadonly15 =1 
                    breadonly16 = 0
                    if 'breadonly16' in request.POST:
                        breadonly16 =1 
                    breadonly17 = 0
                    if 'breadonly17' in request.POST:
                        breadonly17 =1 
                    breadonly18 = 0
                    if 'breadonly18' in request.POST:
                        breadonly18 =1 
                    breadonly19 = 0
                    if 'breadonly19' in request.POST:
                        breadonly19 =1 
                    breadonly20 = 0
                    if 'breadonly20' in request.POST:
                        breadonly20 =1 
                    breadonly21 = 0
                    if 'breadonly21' in request.POST:
                        breadonly21 =1 
                    breadonly22 = 0
                    if 'breadonly22' in request.POST:
                        breadonly22 =1 
                    breadonly23 = 0
                    if 'breadonly23' in request.POST:
                        breadonly23 =1 
                    breadonly24 = 0
                    if 'breadonly24' in request.POST:
                        breadonly24 =1 
                    breadonly25 = 0
                    if 'breadonly25' in request.POST:
                        breadonly25 =1 
                    breadonly26 = 0
                    if 'breadonly26' in request.POST:
                        breadonly26 =1 
                    breadonly27 = 0
                    if 'breadonly27' in request.POST:
                        breadonly27 =1 
                    breadonly28 = 0
                    if 'breadonly28' in request.POST:
                        breadonly28 =1 
                    breadonly29 = 0
                    if 'breadonly29' in request.POST:
                        breadonly29 =1 
                    breadonly30 = 0
                    if 'breadonly30' in request.POST:
                        breadonly30 =1 
                    lroleid =0
                    srolename = ""
                    lgradeid =0
                    sgradename = ""






                    
                    lroleid =0
                    srolename = ""
                    lgradeid =0
                    lcompanyid = request.session['lcompanyid']
                    scompantname = request.session['scompantname']



                    AdminUserlist_AddNewOBJ = Adminuserlist(semployeename=semployeename,semployeeno=semployeeno,spassword=semployeeno, lcompanyid=lcompanyid, scompanyname=scompantname,smobile=smobile,badmin=badmin, bmasterlistonlyallplant=bmasterlistonlyallplant,ballfeatures=ballfeatures,bactive=bactive,lunitid=cmbPlant1,sunitno=sUnit,lroleid=0,srolename="",lgradeid=0,semailaddress=semailaddress)
                    AdminUserlist_AddNewOBJ.save()
  
                    luserid  = AdminUserlist_AddNewOBJ.luserid
                    

                    AdminUserlist_AddNewOBJSave = Adminuserlist.objects.get(luserid=luserid) 


                    AdminUserlist_AddNewOBJSave.semployeename = semployeename
                    AdminUserlist_AddNewOBJSave.semployeeno = semployeeno
                    AdminUserlist_AddNewOBJSave.spassword = semployeeno
                    AdminUserlist_AddNewOBJSave.smobile = smobile
                    AdminUserlist_AddNewOBJSave.badmin = badmin
                    AdminUserlist_AddNewOBJSave.boperator = 0
                    AdminUserlist_AddNewOBJSave.bchangepassword = 1
                    AdminUserlist_AddNewOBJSave.bmasterlistonlyallplant = bmasterlistonlyallplant
                    AdminUserlist_AddNewOBJSave.lunitid = cmbPlant1
                    AdminUserlist_AddNewOBJSave.sunitno = sUnit
                    AdminUserlist_AddNewOBJSave.sunitname = sUnit
                    AdminUserlist_AddNewOBJSave.lroleid = 0
                    AdminUserlist_AddNewOBJSave.srolename = ""
                    AdminUserlist_AddNewOBJSave.lgradeid = 0
                    AdminUserlist_AddNewOBJSave.sgradename = ""
                    AdminUserlist_AddNewOBJSave.lcompanyid = lcompanyid
                    AdminUserlist_AddNewOBJSave.scompanyname = scompantname
                    AdminUserlist_AddNewOBJSave.semailaddress = semailaddress
                    AdminUserlist_AddNewOBJSave.bmatrix = bmatrix
                    AdminUserlist_AddNewOBJSave.lplant1 = 0
                    AdminUserlist_AddNewOBJSave.bstores = 0
                    AdminUserlist_AddNewOBJSave.bcalibration = 0
                    AdminUserlist_AddNewOBJSave.bservice = 0
                    AdminUserlist_AddNewOBJSave.bmsa = 0
                    AdminUserlist_AddNewOBJSave.breadwrite = 0
                    AdminUserlist_AddNewOBJSave.breadonly = 0
                    AdminUserlist_AddNewOBJSave.ballfeatures = ballfeatures
                    AdminUserlist_AddNewOBJSave.bactive = bactive
                    AdminUserlist_AddNewOBJSave.lplant11 = lUnitId1
                    AdminUserlist_AddNewOBJSave.bstores1 = bstores1
                    AdminUserlist_AddNewOBJSave.bcalibration1 = bcalibration1
                    AdminUserlist_AddNewOBJSave.bservice1 = 0
                    AdminUserlist_AddNewOBJSave.bmsa1 = bmsa1
                    AdminUserlist_AddNewOBJSave.breadwrite1 = 0
                    AdminUserlist_AddNewOBJSave.breadonly1 = breadonly1
                    AdminUserlist_AddNewOBJSave.ballfeatures1 = ballfeatures1
                    AdminUserlist_AddNewOBJSave.bactive1 = 0
                    AdminUserlist_AddNewOBJSave.lplant12 = lUnitId2
                    AdminUserlist_AddNewOBJSave.bstores2 = bstores2
                    AdminUserlist_AddNewOBJSave.bcalibration2 = bcalibration2
                    AdminUserlist_AddNewOBJSave.bservice2 = 0
                    AdminUserlist_AddNewOBJSave.bmsa2 = bmsa2
                    AdminUserlist_AddNewOBJSave.breadwrite2 = 0
                    AdminUserlist_AddNewOBJSave.breadonly2 = breadonly2
                    AdminUserlist_AddNewOBJSave.ballfeatures2 = ballfeatures2
                    AdminUserlist_AddNewOBJSave.bactive2 = 0
                    AdminUserlist_AddNewOBJSave.lplant13 = lUnitId3
                    AdminUserlist_AddNewOBJSave.bstores3 = bstores3
                    AdminUserlist_AddNewOBJSave.bcalibration3 = bcalibration3
                    AdminUserlist_AddNewOBJSave.bservice3 = 0
                    AdminUserlist_AddNewOBJSave.bmsa3 = bmsa3
                    AdminUserlist_AddNewOBJSave.breadwrite3 = 0
                    AdminUserlist_AddNewOBJSave.breadonly3 = breadonly3
                    AdminUserlist_AddNewOBJSave.ballfeatures3 = ballfeatures3
                    AdminUserlist_AddNewOBJSave.bactive3 = 0
                    AdminUserlist_AddNewOBJSave.lplant14 = lUnitId4
                    AdminUserlist_AddNewOBJSave.bstores4 = bstores4
                    AdminUserlist_AddNewOBJSave.bcalibration4 = bcalibration4
                    AdminUserlist_AddNewOBJSave.bservice4 = 0
                    AdminUserlist_AddNewOBJSave.bmsa4 = bmsa4
                    AdminUserlist_AddNewOBJSave.breadwrite4 = 0
                    AdminUserlist_AddNewOBJSave.breadonly4 = breadonly4
                    AdminUserlist_AddNewOBJSave.ballfeatures4 = ballfeatures4
                    AdminUserlist_AddNewOBJSave.bactive4 = 0
                    AdminUserlist_AddNewOBJSave.lplant15 = lUnitId5
                    AdminUserlist_AddNewOBJSave.bstores5 = bstores5
                    AdminUserlist_AddNewOBJSave.bcalibration5 = bcalibration5
                    AdminUserlist_AddNewOBJSave.bservice5 = 0
                    AdminUserlist_AddNewOBJSave.bmsa5 = bmsa5
                    AdminUserlist_AddNewOBJSave.breadwrite5 = 0
                    AdminUserlist_AddNewOBJSave.breadonly5 = breadonly5
                    AdminUserlist_AddNewOBJSave.ballfeatures5 = ballfeatures5
                    AdminUserlist_AddNewOBJSave.bactive5 = 0
                    AdminUserlist_AddNewOBJSave.lplant16 = lUnitId6
                    AdminUserlist_AddNewOBJSave.bstores6 = bstores6
                    AdminUserlist_AddNewOBJSave.bcalibration6 = bcalibration6
                    AdminUserlist_AddNewOBJSave.bservice6 = 0
                    AdminUserlist_AddNewOBJSave.bmsa6 = bmsa6
                    AdminUserlist_AddNewOBJSave.breadwrite6 = 0
                    AdminUserlist_AddNewOBJSave.breadonly6 = breadonly6
                    AdminUserlist_AddNewOBJSave.ballfeatures6 = ballfeatures6
                    AdminUserlist_AddNewOBJSave.bactive6 = 0
                    AdminUserlist_AddNewOBJSave.lplant17 = lUnitId7
                    AdminUserlist_AddNewOBJSave.bstores7 = bstores7
                    AdminUserlist_AddNewOBJSave.bcalibration7 = bcalibration7
                    AdminUserlist_AddNewOBJSave.bservice7 = 0
                    AdminUserlist_AddNewOBJSave.bmsa7 = bmsa7
                    AdminUserlist_AddNewOBJSave.breadwrite7 = 0
                    AdminUserlist_AddNewOBJSave.breadonly7 = breadonly7
                    AdminUserlist_AddNewOBJSave.ballfeatures7 = ballfeatures7
                    AdminUserlist_AddNewOBJSave.bactive7 = 0
                    AdminUserlist_AddNewOBJSave.lplant18 = lUnitId8
                    AdminUserlist_AddNewOBJSave.bstores8 = bstores8
                    AdminUserlist_AddNewOBJSave.bcalibration8 = bcalibration8
                    AdminUserlist_AddNewOBJSave.bservice8 = 0
                    AdminUserlist_AddNewOBJSave.bmsa8 = bmsa8
                    AdminUserlist_AddNewOBJSave.breadwrite8 = 0
                    AdminUserlist_AddNewOBJSave.breadonly8 = breadonly8
                    AdminUserlist_AddNewOBJSave.ballfeatures8 = ballfeatures8
                    AdminUserlist_AddNewOBJSave.bactive8 = 0
                    AdminUserlist_AddNewOBJSave.lplant19 = lUnitId9
                    AdminUserlist_AddNewOBJSave.bstores9 = bstores9
                    AdminUserlist_AddNewOBJSave.bcalibration9 = bcalibration9
                    AdminUserlist_AddNewOBJSave.bservice9 = 0
                    AdminUserlist_AddNewOBJSave.bmsa9 = bmsa9
                    AdminUserlist_AddNewOBJSave.breadwrite9 = 0
                    AdminUserlist_AddNewOBJSave.breadonly9 = breadonly9
                    AdminUserlist_AddNewOBJSave.ballfeatures9 = ballfeatures9
                    AdminUserlist_AddNewOBJSave.bactive9 = 0
                    AdminUserlist_AddNewOBJSave.lplant110 = lUnitId10
                    AdminUserlist_AddNewOBJSave.bstores10 = bstores10
                    AdminUserlist_AddNewOBJSave.bcalibration10 = bcalibration10
                    AdminUserlist_AddNewOBJSave.bservice10 = 0
                    AdminUserlist_AddNewOBJSave.bmsa10 = bmsa10
                    AdminUserlist_AddNewOBJSave.breadwrite10 = 0
                    AdminUserlist_AddNewOBJSave.breadonly10 = breadonly10
                    AdminUserlist_AddNewOBJSave.ballfeatures10 = ballfeatures10
                    AdminUserlist_AddNewOBJSave.bactive10 = 0
                    AdminUserlist_AddNewOBJSave.lplant111 = lUnitId11
                    AdminUserlist_AddNewOBJSave.bstores11 = bstores11
                    AdminUserlist_AddNewOBJSave.bcalibration11 = bcalibration11
                    AdminUserlist_AddNewOBJSave.bservice11 = 0
                    AdminUserlist_AddNewOBJSave.bmsa11 = bmsa11
                    AdminUserlist_AddNewOBJSave.breadwrite11 = 0
                    AdminUserlist_AddNewOBJSave.breadonly11 = breadonly11
                    AdminUserlist_AddNewOBJSave.ballfeatures11 = ballfeatures11
                    AdminUserlist_AddNewOBJSave.bactive11 = 0
                    AdminUserlist_AddNewOBJSave.lplant112 = lUnitId12
                    AdminUserlist_AddNewOBJSave.bstores12 = bstores12
                    AdminUserlist_AddNewOBJSave.bcalibration12 = bcalibration12
                    AdminUserlist_AddNewOBJSave.bservice12 = 0
                    AdminUserlist_AddNewOBJSave.bmsa12 = bmsa12
                    AdminUserlist_AddNewOBJSave.breadwrite12 = 0
                    AdminUserlist_AddNewOBJSave.breadonly12 = breadonly12
                    AdminUserlist_AddNewOBJSave.ballfeatures12 = ballfeatures12
                    AdminUserlist_AddNewOBJSave.bactive12 = 0
                    AdminUserlist_AddNewOBJSave.lplant113 = lUnitId13
                    AdminUserlist_AddNewOBJSave.bstores13 = bstores13
                    AdminUserlist_AddNewOBJSave.bcalibration13 = bcalibration13
                    AdminUserlist_AddNewOBJSave.bservice13 = 0
                    AdminUserlist_AddNewOBJSave.bmsa13 = bmsa13
                    AdminUserlist_AddNewOBJSave.breadwrite13 = 0
                    AdminUserlist_AddNewOBJSave.breadonly13 = breadonly13
                    AdminUserlist_AddNewOBJSave.ballfeatures13 = ballfeatures13
                    AdminUserlist_AddNewOBJSave.bactive13 = 0
                    AdminUserlist_AddNewOBJSave.lplant114 = lUnitId14
                    AdminUserlist_AddNewOBJSave.bstores14 = bstores14
                    AdminUserlist_AddNewOBJSave.bcalibration14 = bcalibration14
                    AdminUserlist_AddNewOBJSave.bservice14 = 0
                    AdminUserlist_AddNewOBJSave.bmsa14 = bmsa14
                    AdminUserlist_AddNewOBJSave.breadwrite14 = 0
                    AdminUserlist_AddNewOBJSave.breadonly14 = breadonly14
                    AdminUserlist_AddNewOBJSave.ballfeatures14 = ballfeatures14
                    AdminUserlist_AddNewOBJSave.bactive14 = 0
                    AdminUserlist_AddNewOBJSave.lplant115 = lUnitId15
                    AdminUserlist_AddNewOBJSave.bstores15 = bstores15
                    AdminUserlist_AddNewOBJSave.bcalibration15 = bcalibration15
                    AdminUserlist_AddNewOBJSave.bservice15 = 0
                    AdminUserlist_AddNewOBJSave.bmsa15 = bmsa15
                    AdminUserlist_AddNewOBJSave.breadwrite15 = 0
                    AdminUserlist_AddNewOBJSave.breadonly15 = breadonly15
                    AdminUserlist_AddNewOBJSave.ballfeatures15 = ballfeatures15
                    AdminUserlist_AddNewOBJSave.bactive15 = 0
                    AdminUserlist_AddNewOBJSave.lplant116 = lUnitId16
                    AdminUserlist_AddNewOBJSave.bstores16 = bstores16
                    AdminUserlist_AddNewOBJSave.bcalibration16 = bcalibration16
                    AdminUserlist_AddNewOBJSave.bservice16 = 0
                    AdminUserlist_AddNewOBJSave.bmsa16 = bmsa16
                    AdminUserlist_AddNewOBJSave.breadwrite16 = 0
                    AdminUserlist_AddNewOBJSave.breadonly16 = breadonly16
                    AdminUserlist_AddNewOBJSave.ballfeatures16 = ballfeatures16
                    AdminUserlist_AddNewOBJSave.bactive16 = 0
                    AdminUserlist_AddNewOBJSave.lplant117 = lUnitId17
                    AdminUserlist_AddNewOBJSave.bstores17 = bstores17
                    AdminUserlist_AddNewOBJSave.bcalibration17 = bcalibration17
                    AdminUserlist_AddNewOBJSave.bservice17 = 0
                    AdminUserlist_AddNewOBJSave.bmsa17 = bmsa17
                    AdminUserlist_AddNewOBJSave.breadwrite17 = 0
                    AdminUserlist_AddNewOBJSave.breadonly17 = breadonly17
                    AdminUserlist_AddNewOBJSave.ballfeatures17 = ballfeatures17
                    AdminUserlist_AddNewOBJSave.bactive17 = 0
                    AdminUserlist_AddNewOBJSave.lplant118 = lUnitId18
                    AdminUserlist_AddNewOBJSave.bstores18 = bstores18
                    AdminUserlist_AddNewOBJSave.bcalibration18 = bcalibration18
                    AdminUserlist_AddNewOBJSave.bservice18 = 0
                    AdminUserlist_AddNewOBJSave.bmsa18 = bmsa18
                    AdminUserlist_AddNewOBJSave.breadwrite18 = 0
                    AdminUserlist_AddNewOBJSave.breadonly18 = breadonly18
                    AdminUserlist_AddNewOBJSave.ballfeatures18 = ballfeatures18
                    AdminUserlist_AddNewOBJSave.bactive18 = 0
                    AdminUserlist_AddNewOBJSave.lplant119 = lUnitId19
                    AdminUserlist_AddNewOBJSave.bstores19 = bstores19
                    AdminUserlist_AddNewOBJSave.bcalibration19 = bcalibration19
                    AdminUserlist_AddNewOBJSave.bservice19 = 0
                    AdminUserlist_AddNewOBJSave.bmsa19 = bmsa19
                    AdminUserlist_AddNewOBJSave.breadwrite19 = 0
                    AdminUserlist_AddNewOBJSave.breadonly19 = breadonly19
                    AdminUserlist_AddNewOBJSave.ballfeatures19 = ballfeatures19
                    AdminUserlist_AddNewOBJSave.bactive19 = 0
                    AdminUserlist_AddNewOBJSave.lplant120 = lUnitId20
                    AdminUserlist_AddNewOBJSave.bstores20 = bstores20
                    AdminUserlist_AddNewOBJSave.bcalibration20 = bcalibration20
                    AdminUserlist_AddNewOBJSave.bservice20 = 0
                    AdminUserlist_AddNewOBJSave.bmsa20 = bmsa20
                    AdminUserlist_AddNewOBJSave.breadwrite20 = 0
                    AdminUserlist_AddNewOBJSave.breadonly20 = breadonly20
                    AdminUserlist_AddNewOBJSave.ballfeatures20 = ballfeatures20
                    AdminUserlist_AddNewOBJSave.bactive20 = 0
                    AdminUserlist_AddNewOBJSave.lplant121 = lUnitId21
                    AdminUserlist_AddNewOBJSave.bstores21 = bstores21
                    AdminUserlist_AddNewOBJSave.bcalibration21 = bcalibration21
                    AdminUserlist_AddNewOBJSave.bservice21 = 0
                    AdminUserlist_AddNewOBJSave.bmsa21 = bmsa21
                    AdminUserlist_AddNewOBJSave.breadwrite21 = 0
                    AdminUserlist_AddNewOBJSave.breadonly21 = breadonly21
                    AdminUserlist_AddNewOBJSave.ballfeatures21 = ballfeatures21
                    AdminUserlist_AddNewOBJSave.bactive21 = 0
                    AdminUserlist_AddNewOBJSave.lplant122 = lUnitId22
                    AdminUserlist_AddNewOBJSave.bstores22 = bstores22
                    AdminUserlist_AddNewOBJSave.bcalibration22 = bcalibration22
                    AdminUserlist_AddNewOBJSave.bservice22 = 0
                    AdminUserlist_AddNewOBJSave.bmsa22 = bmsa22
                    AdminUserlist_AddNewOBJSave.breadwrite22 = 0
                    AdminUserlist_AddNewOBJSave.breadonly22 = breadonly22
                    AdminUserlist_AddNewOBJSave.ballfeatures22 = ballfeatures22
                    AdminUserlist_AddNewOBJSave.bactive22 = 0
                    AdminUserlist_AddNewOBJSave.lplant123 = lUnitId23
                    AdminUserlist_AddNewOBJSave.bstores23 = bstores23
                    AdminUserlist_AddNewOBJSave.bcalibration23 = bcalibration23
                    AdminUserlist_AddNewOBJSave.bservice23 = 0
                    AdminUserlist_AddNewOBJSave.bmsa23 = bmsa23
                    AdminUserlist_AddNewOBJSave.breadwrite23 = 0
                    AdminUserlist_AddNewOBJSave.breadonly23 = breadonly23
                    AdminUserlist_AddNewOBJSave.ballfeatures23 = ballfeatures23
                    AdminUserlist_AddNewOBJSave.bactive23 = 0
                    AdminUserlist_AddNewOBJSave.lplant124 = lUnitId24
                    AdminUserlist_AddNewOBJSave.bstores24 = bstores24
                    AdminUserlist_AddNewOBJSave.bcalibration24 = bcalibration24
                    AdminUserlist_AddNewOBJSave.bservice24 = 0
                    AdminUserlist_AddNewOBJSave.bmsa24 = bmsa24
                    AdminUserlist_AddNewOBJSave.breadwrite24 = 0
                    AdminUserlist_AddNewOBJSave.breadonly24 = breadonly24
                    AdminUserlist_AddNewOBJSave.ballfeatures24 = ballfeatures24
                    AdminUserlist_AddNewOBJSave.bactive24 = 0
                    AdminUserlist_AddNewOBJSave.lplant125 = lUnitId25
                    AdminUserlist_AddNewOBJSave.bstores25 = bstores25
                    AdminUserlist_AddNewOBJSave.bcalibration25 = bcalibration25
                    AdminUserlist_AddNewOBJSave.bservice25 = 0
                    AdminUserlist_AddNewOBJSave.bmsa25 = bmsa25
                    AdminUserlist_AddNewOBJSave.breadwrite25 = 0
                    AdminUserlist_AddNewOBJSave.breadonly25 = breadonly25
                    AdminUserlist_AddNewOBJSave.ballfeatures25 = ballfeatures25
                    AdminUserlist_AddNewOBJSave.bactive25 = 0
                    AdminUserlist_AddNewOBJSave.lplant126 = lUnitId26
                    AdminUserlist_AddNewOBJSave.bstores26 = bstores26
                    AdminUserlist_AddNewOBJSave.bcalibration26 = bcalibration26
                    AdminUserlist_AddNewOBJSave.bservice26 = 0
                    AdminUserlist_AddNewOBJSave.bmsa26 = bmsa26
                    AdminUserlist_AddNewOBJSave.breadwrite26 = 0
                    AdminUserlist_AddNewOBJSave.breadonly26 = breadonly26
                    AdminUserlist_AddNewOBJSave.ballfeatures26 = ballfeatures26
                    AdminUserlist_AddNewOBJSave.bactive26 = 0
                    AdminUserlist_AddNewOBJSave.lplant127 = lUnitId27
                    AdminUserlist_AddNewOBJSave.bstores27 = bstores27
                    AdminUserlist_AddNewOBJSave.bcalibration27 = bcalibration27
                    AdminUserlist_AddNewOBJSave.bservice27 = 0
                    AdminUserlist_AddNewOBJSave.bmsa27 = bmsa27
                    AdminUserlist_AddNewOBJSave.breadwrite27 = 0
                    AdminUserlist_AddNewOBJSave.breadonly27 = breadonly27
                    AdminUserlist_AddNewOBJSave.ballfeatures27 = ballfeatures27
                    AdminUserlist_AddNewOBJSave.bactive27 = 0
                    AdminUserlist_AddNewOBJSave.lplant128 = lUnitId28
                    AdminUserlist_AddNewOBJSave.bstores28 = bstores28
                    AdminUserlist_AddNewOBJSave.bcalibration28 = bcalibration28
                    AdminUserlist_AddNewOBJSave.bservice28 = 0
                    AdminUserlist_AddNewOBJSave.bmsa28 = bmsa28
                    AdminUserlist_AddNewOBJSave.breadwrite28 = 0
                    AdminUserlist_AddNewOBJSave.breadonly28 = breadonly28
                    AdminUserlist_AddNewOBJSave.ballfeatures28 = ballfeatures28
                    AdminUserlist_AddNewOBJSave.bactive28 = 0
                    AdminUserlist_AddNewOBJSave.lplant129 = lUnitId29
                    AdminUserlist_AddNewOBJSave.bstores29 = bstores29
                    AdminUserlist_AddNewOBJSave.bcalibration29 = bcalibration29
                    AdminUserlist_AddNewOBJSave.bservice29 = 0
                    AdminUserlist_AddNewOBJSave.bmsa29 = bmsa29
                    AdminUserlist_AddNewOBJSave.breadwrite29 = 0
                    AdminUserlist_AddNewOBJSave.breadonly29 = breadonly29
                    AdminUserlist_AddNewOBJSave.ballfeatures29 = ballfeatures29
                    AdminUserlist_AddNewOBJSave.bactive29 = 0
                    AdminUserlist_AddNewOBJSave.lplant130 = lUnitId30
                    AdminUserlist_AddNewOBJSave.bstores30 = bstores30
                    AdminUserlist_AddNewOBJSave.bcalibration30 = bcalibration30
                    AdminUserlist_AddNewOBJSave.bservice30 = 0
                    AdminUserlist_AddNewOBJSave.bmsa30 = bmsa30
                    AdminUserlist_AddNewOBJSave.breadwrite30 = 0
                    AdminUserlist_AddNewOBJSave.breadonly30 = breadonly30
                    AdminUserlist_AddNewOBJSave.ballfeatures30 = ballfeatures30
                    AdminUserlist_AddNewOBJSave.bactive30 = 0

                    AdminUserlist_AddNewOBJSave.save()


                    messages.success(request, 'User is created successfully!')

                    return   redirect('GaugeUserList')  
    
                else:              
                    messages.error(request, 'Plant is not selected. Please Select and then try!')
 
    
    else:
        Unitlist_list = Adminunitlist.objects.order_by('splantno')               
        return render(request, "CloudCaliber/UserlistAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list, 
                            'lUnitId1': lUnitId[0],
                            'sUnitName1': sUnitName[0],
                            'lUnitId2': lUnitId[1],
                            'sUnitName2': sUnitName[1],
                            'lUnitId3': lUnitId[2],
                            'sUnitName3': sUnitName[2],
                            'lUnitId4': lUnitId[3],
                            'sUnitName4': sUnitName[3],
                            'lUnitId5': lUnitId[4],
                            'sUnitName5': sUnitName[4],
                            'lUnitId6': lUnitId[5],
                            'sUnitName6': sUnitName[5],
                            'lUnitId7': lUnitId[6],
                            'sUnitName7': sUnitName[6],
                            'lUnitId8': lUnitId[7],
                            'sUnitName8': sUnitName[7],
                            'lUnitId9': lUnitId[8],
                            'sUnitName9': sUnitName[8],
                            'lUnitId10': lUnitId[9],
                            'sUnitName10': sUnitName[9],
                            'lUnitId11': lUnitId[10],
                            'sUnitName11': sUnitName[10],
                            'lUnitId12': lUnitId[11],
                            'sUnitName12': sUnitName[11],
                            'lUnitId13': lUnitId[12],
                            'sUnitName13': sUnitName[12],
                            'lUnitId14': lUnitId[13],
                            'sUnitName14': sUnitName[13],
                            'lUnitId15': lUnitId[14],
                            'sUnitName15': sUnitName[14],
                            'lUnitId16': lUnitId[15],
                            'sUnitName16': sUnitName[15],
                            'lUnitId17': lUnitId[16],
                            'sUnitName17': sUnitName[16],
                            'lUnitId18': lUnitId[17],
                            'sUnitName18': sUnitName[17],
                            'lUnitId19': lUnitId[18],
                            'sUnitName19': sUnitName[18],
                            'lUnitId20': lUnitId[19],
                            'sUnitName20': sUnitName[19],
                            'lUnitId21': lUnitId[20],
                            'sUnitName21': sUnitName[20],
                            'lUnitId22': lUnitId[21],
                            'sUnitName22': sUnitName[21],
                            'lUnitId23': lUnitId[22],
                            'sUnitName23': sUnitName[22],
                            'lUnitId24': lUnitId[23],
                            'sUnitName24': sUnitName[23],
                            'lUnitId25': lUnitId[24],
                            'sUnitName25': sUnitName[24],
                            'lUnitId26': lUnitId[25],
                            'sUnitName26': sUnitName[25],
                            'lUnitId27': lUnitId[26],
                            'sUnitName27': sUnitName[26],
                            'lUnitId28': lUnitId[27],
                            'sUnitName28': sUnitName[27],
                            'lUnitId29': lUnitId[28],
                            'sUnitName29': sUnitName[28],
                            'lUnitId30': lUnitId[29],
                            'sUnitName30': sUnitName[29],
                            'lUnitIdA':'0',
                        }
                        )



@csrf_exempt
def GaugeUserList (request):  

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('UserListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                   
                assert isinstance(request, HttpRequest) 

                Unitlist_list = Adminunitlist.objects.order_by('splantno') 
                AdminUser_list = Adminuserlist.objects.order_by('semployeename') 


                page_number  = request.GET.get('page')

                lRecCount =0 
                lRecCount = AdminUser_list.count()
                lRecCount1 = int((lRecCount * 10/100) )
                if (lRecCount1 == 0):
                    lRecCount1 =1
                paginator = Paginator(AdminUser_list, lRecCount1)
                try:
                    AdminUser_lists = paginator.get_page(page_number )
                except PageNotAnInteger:
                    AdminUser_lists = paginator.page(1)
                except EmptyPage:
                    AdminUser_lists = paginator.page(paginator.num_pages)
                




                return render(request,  'CloudCaliber/Userlist.html', 
                    {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'AdminUser_lists': AdminUser_lists,
                            'Unitlist_list': Unitlist_list, 
                        }
                    ) 
            else:
                  
                assert isinstance(request, HttpRequest) 
                Unitlist_list = Adminunitlist.objects.order_by('splantno')    

                AdminUser_list = Adminuserlist.objects.filter(semployeeno__icontains=txtSearch) | Adminuserlist.objects.filter(semployeename__icontains=txtSearch) | Adminuserlist.objects.filter(sunitno__icontains=txtSearch).values()      #   or if statement
                

                page_number  = request.GET.get('page')

                lRecCount =0 
                lRecCount = AdminUser_list.count()
                lRecCount1 = int((lRecCount * 10/100) )
                if (lRecCount1 == 0):
                    lRecCount1 =1
                paginator = Paginator(AdminUser_list, lRecCount1)
                try:
                    AdminUser_lists = paginator.get_page(page_number )
                except PageNotAnInteger:
                    AdminUser_lists = paginator.page(1)
                except EmptyPage:
                    AdminUser_lists = paginator.page(paginator.num_pages)
                




                return render(request,  'CloudCaliber/Userlist.html', 
                    {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'AdminUser_lists': AdminUser_lists,
                            'Unitlist_list': Unitlist_list, 
                        }
                    ) 

    else:     
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest) 
            Unitlist_list = Adminunitlist.objects.order_by('splantno')  
            AdminUser_list = Adminuserlist.objects.order_by('semployeename') 


            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = AdminUser_list.count()
            lRecCount1 = int((lRecCount * 10/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1
            paginator = Paginator(AdminUser_list, lRecCount1)
            try:
                AdminUser_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                AdminUser_lists = paginator.page(1)
            except EmptyPage:
                AdminUser_lists = paginator.page(paginator.num_pages)
            




            return render(request,  'CloudCaliber/Userlist.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'AdminUser_lists': AdminUser_lists,
                        'Unitlist_list': Unitlist_list, 
                    }
                )   





def GaugeCalibration30DaysDue(request):
    return render(request, "CloudCaliber/GaugeCalibration30DaysDue.html")

def GaugeCalibrationDueOverDue(request):
    return render(request, "CloudCaliber/GaugeCalibrationDueOverDue.html")

def GaugeCalibrationUnder(request):
    return render(request, "CloudCaliber/GaugeCalibrationUnder.html")

def GaugeMSADue1Year(request):
    return render(request, "CloudCaliber/GaugeMSADue1Year.html")

def GaugeCalibrationHistory(request):
    return render(request, "CloudCaliber/GaugeCalibrationHistory.html")

def GaugeMSAHistory(request):
    return render(request, "CloudCaliber/GaugeMSAHistory.html")

def Gauge8DHistory(request):
    return render(request, "CloudCaliber/Gauge8DHistory.html")

def PlantAssetViewDashboardIdle(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardIdle.html")

def PlantAssetViewDashboardSpare(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardSpare.html")

def PlantAssetViewDashboardIssued(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardIssued.html")

def PlantAssetViewDashboardDamaged(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardDamaged.html")

def PlantAssetViewDashboardMissing(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardMissing.html")

def PlantAssetViewDashboardLimitedUsage(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardLimitedUsage.html")

def PlantAssetViewDashboardOutofCalibration(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardOutofCalibration.html")

def PlantAssetViewDashboardScraped(request):
    return render(request, "CloudCaliber/PlantAssetViewDashboardScraped.html") 

def GaugeVerifications(request):
    return render(request, "CloudCaliber/GaugeVerifications.html")

def GaugeVerificationDue(request):
    return render(request, "CloudCaliber/GaugeVerificationDue.html") 

def hello_here(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)



def PlantAssetViewDashboardUnderPurchase(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        return render(request,  'CloudCaliber/PlantAssetViewDashboardUnderPurchase.html', 
        {
            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'Adminassettypelist_list': Adminassettypelist_list, 
        })  
    else: 
         
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        return render(request,  'CloudCaliber/PlantAssetViewDashboardUnderPurchase.html', 
        {
            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'Adminassettypelist_list': Adminassettypelist_list, 
        })



def PlantAssetViewDashboardCreateID(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        return render(request,  'CloudCaliber/PlantAssetViewDashboardCreateID.html', 
        {
            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'Adminassettypelist_list': Adminassettypelist_list, 
        })  
    else: 
         
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
        return render(request,  'CloudCaliber/PlantAssetViewDashboardCreateID.html', 
        {
            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'Adminassettypelist_list': Adminassettypelist_list, 
        })
    
@csrf_exempt
def AdminuserlistApi(request,id=0):
    if request.method=='GET':
        Adminuserlists = Adminuserlist.objects.all()
        AdminuserlistSerializerOBJ=AdminuserlistSerializer(Adminuserlists,many=True)
        return JsonResponse(AdminuserlistSerializerOBJ.data,safe=False)
    elif request.method=='POST':
        AdminuserlistData = JSONParser().parse(request)
        AdminuserlistSerializerOBJ=AdminuserlistSerializer(data=AdminuserlistData)
        if AdminuserlistSerializerOBJ.is_valid():
            AdminuserlistSerializerOBJ.save
            return JsonResponse("User is Added Successfully!",safe=False)        
        return JsonResponse("User to be Added Failed!",safe=False)        
    elif request.method=='PUT':
        AdminuserlistData = JSONParser().parse(request)
        AdminuserlistOBJ=Adminuserlist.objects.get(lUserId=AdminuserlistData['lUserId'])
        AdminuserlistSerializerOBJ=AdminuserlistSerializer(AdminuserlistOBJ,data=AdminuserlistData)
        if AdminuserlistSerializerOBJ.is_valid():
            AdminuserlistSerializerOBJ.save
            return JsonResponse("User is Updated Successfully!",safe=False)        
        return JsonResponse("User to be Updated Failed!",safe=False)        
    elif request.method=='DELETE': 
        AdminuserlistOBJ=Adminuserlist.objects.get(lUserId=id)
        AdminuserlistOBJ.delete()
        return JsonResponse("User to be Added Failed!",safe=False)

