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
from CloudCaliber import viewsvalidations
from CloudCaliber import viewscategorycreation

from CloudCaliber.models import Adminoperatorlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist
 


@csrf_exempt
def home(request):
    # print(request.POST)


    if request.method == "POST":
        data = request.POST 
        
        lUnitId = 0
        lUnitId1 = 0

        
        if 'Plant' in request.POST:
            cmbPlant=request.POST['Plant'] #('Machine')
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
                    
                    lUnitId = 0
                    lUnitId1 = 0
                    lunitidDB ="0"
                    lunitidDBCheck ="0"
                    AdminuserlistActive = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,badmin=1).values()
                    if AdminuserlistActive:  
                        lUnitId = 0
                        lUnitId =AdminuserlistPWDOBJ['lunitid'] 
                        lUnitId1 = lUnitId
                        request.session['lCategoryID'] = 0                        
                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                        request.session['badmin'] = 1
                        request.session['bstores'] = 0
                        request.session['bcalibration'] = 0
                        request.session['bservice'] = 0
                        request.session['bmsa'] = 0
                        request.session['bmasterlistonlyallplant'] = 0  
                        request.session['breadonly'] =0
                        return Dashboard(request) 

                    else:
                        AdminuserlistActive1 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,bmasterlistonlyallplant=1).values()
                        if AdminuserlistActive1:  
                                lUnitId = 0 
                                request.session['lCategoryID'] = 0                        
                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                request.session['badmin'] = 0
                                request.session['bstores'] = 0
                                request.session['bcalibration'] = 0
                                request.session['bservice'] = 0
                                request.session['bmsa'] = 0
                                request.session['bmasterlistonlyallplant'] = 1 
                                request.session['breadonly'] =0
                                return Dashboard(request) 

                        else:
                            AdminuserlistActive2 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant11=cmbPlant).values()
                            if AdminuserlistActive2:  
                                    lUnitId = 0 
                                    request.session['lCategoryID'] = 0                        
                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                    request.session['badmin'] = 0
                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores1']
                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration1']
                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice1']
                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa1']
                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly1']
                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures1']
                                    request.session['bmasterlistonlyallplant'] = 0
                                    return Dashboard(request) 
 
                            else:
                                AdminuserlistActive3 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant12=cmbPlant).values()
                                if AdminuserlistActive3:  
                                        lUnitId = 0 
                                        request.session['lCategoryID'] = 0                        
                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                        request.session['badmin'] = 0
                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores2']
                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration2']
                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice2']
                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa2']
                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly2']
                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures2']
                                        request.session['bmasterlistonlyallplant'] = 0
                                        return Dashboard(request) 
        
                                else:	
                                    AdminuserlistActive4 = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant13=cmbPlant).values()
                                    if AdminuserlistActive4:  
                                            lUnitId = 0 
                                            request.session['lCategoryID'] = 0                        
                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                            request.session['badmin'] = 0
                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores3']
                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration3']
                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice3']
                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa3']
                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly3']
                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures3']
                                            request.session['bmasterlistonlyallplant'] = 0
                                            return Dashboard(request) 


                                    else:	
                                        AdminuserlistActive4A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant14=cmbPlant).values()
                                        if AdminuserlistActive4A:  
                                                lUnitId = 0 
                                                request.session['lCategoryID'] = 0                        
                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                request.session['badmin'] = 0
                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores4']
                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration4']
                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice4']
                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa4']
                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly4']
                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures4']
                                                request.session['bmasterlistonlyallplant'] = 0
                                                return Dashboard(request)

                                        else:	
                                            AdminuserlistActive5A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant15=cmbPlant).values()
                                            if AdminuserlistActive5A:  
                                                    lUnitId = 0 
                                                    request.session['lCategoryID'] = 0                        
                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                    request.session['badmin'] = 0
                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores5']
                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration5']
                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice5']
                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa5']
                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly5']
                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures5']
                                                    request.session['bmasterlistonlyallplant'] = 0
                                                    return Dashboard(request) 


                                            else:	
                                                AdminuserlistActive6A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant16=cmbPlant).values()
                                                if AdminuserlistActive6A:  
                                                        lUnitId = 0 
                                                        request.session['lCategoryID'] = 0                        
                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                        request.session['badmin'] = 0
                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores6']
                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration6']
                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice6']
                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa6']
                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly6']
                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures6']
                                                        request.session['bmasterlistonlyallplant'] = 0
                                                        return Dashboard(request)

                                                else:	
                                                    AdminuserlistActive7A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant17=cmbPlant).values()
                                                    if AdminuserlistActive7A:  
                                                            lUnitId = 0 
                                                            request.session['lCategoryID'] = 0                        
                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                            request.session['badmin'] = 0
                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores7']
                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration7']
                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice7']
                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa7']
                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly7']
                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures7']
                                                            request.session['bmasterlistonlyallplant'] = 0
                                                            return Dashboard(request)

                                                        
                                                    else:	
                                                        AdminuserlistActive8A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant18=cmbPlant).values()
                                                        if AdminuserlistActive8A:  
                                                                lUnitId = 0 
                                                                request.session['lCategoryID'] = 0                        
                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                request.session['badmin'] = 0
                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores8']
                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration8']
                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice8']
                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa8']
                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly8']
                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures8']
                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                return Dashboard(request)

                                                                
                                                        else:	
                                                            AdminuserlistActive9A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant19=cmbPlant).values()
                                                            if AdminuserlistActive9A:  
                                                                    lUnitId = 0 
                                                                    request.session['lCategoryID'] = 0                        
                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                    request.session['badmin'] = 0
                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores9']
                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration9']
                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice9']
                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa9']
                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly9']
                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures9']
                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                    return Dashboard(request)

        
                                                            else:	
                                                                AdminuserlistActive10A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant110=cmbPlant).values()
                                                                if AdminuserlistActive10A:  
                                                                        lUnitId = 0 
                                                                        request.session['lCategoryID'] = 0                        
                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                        request.session['badmin'] = 0
                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores10']
                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration10']
                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice10']
                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa10']
                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly10']
                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures10']
                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                        return Dashboard(request)

                                                                else:	
                                                                    AdminuserlistActive11A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant111=cmbPlant).values()
                                                                    if AdminuserlistActive11A:  
                                                                            lUnitId = 0 
                                                                            request.session['lCategoryID'] = 0                        
                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                            request.session['badmin'] = 0
                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores11']
                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration11']
                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice11']
                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa11']
                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly11']
                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures11']
                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                            return Dashboard(request)


                                                                    else:	
                                                                        AdminuserlistActive12A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant121=cmbPlant).values()
                                                                        if AdminuserlistActive12A:  
                                                                                lUnitId = 0 
                                                                                request.session['lCategoryID'] = 0                        
                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                request.session['badmin'] = 0
                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores12']
                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration12']
                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice12']
                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa12']
                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly12']
                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures12']
                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                return Dashboard(request)


                                                                        else:	
                                                                            AdminuserlistActive13A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant131=cmbPlant).values()
                                                                            if AdminuserlistActive13A:  
                                                                                    lUnitId = 0 
                                                                                    request.session['lCategoryID'] = 0                        
                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                                    request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                    request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                    request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                    request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                    request.session['badmin'] = 0
                                                                                    request.session['bstores'] = AdminuserlistPWDOBJ['bstores13']
                                                                                    request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration13']
                                                                                    request.session['bservice'] = AdminuserlistPWDOBJ['bservice13']
                                                                                    request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa13']
                                                                                    request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly13']
                                                                                    request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures13']
                                                                                    request.session['bmasterlistonlyallplant'] = 0
                                                                                    return Dashboard(request)


                                                                            else:	
                                                                                AdminuserlistActive14A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant141=cmbPlant).values()
                                                                                if AdminuserlistActive14A:  
                                                                                        lUnitId = 0 
                                                                                        request.session['lCategoryID'] = 0                        
                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                                        request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                        request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                        request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                        request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                        request.session['badmin'] = 0
                                                                                        request.session['bstores'] = AdminuserlistPWDOBJ['bstores14']
                                                                                        request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration14']
                                                                                        request.session['bservice'] = AdminuserlistPWDOBJ['bservice14']
                                                                                        request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa14']
                                                                                        request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly14']
                                                                                        request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures14']
                                                                                        request.session['bmasterlistonlyallplant'] = 0
                                                                                        return Dashboard(request)
                                                                                    

                                                                                else:	
                                                                                    AdminuserlistActive15A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant151=cmbPlant).values()
                                                                                    if AdminuserlistActive15A:  
                                                                                            lUnitId = 0 
                                                                                            request.session['lCategoryID'] = 0                        
                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                                            request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                            request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                            request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                            request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                            request.session['badmin'] = 0
                                                                                            request.session['bstores'] = AdminuserlistPWDOBJ['bstores15']
                                                                                            request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration15']
                                                                                            request.session['bservice'] = AdminuserlistPWDOBJ['bservice15']
                                                                                            request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa15']
                                                                                            request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly15']
                                                                                            request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures15']
                                                                                            request.session['bmasterlistonlyallplant'] = 0
                                                                                            return Dashboard(request)
                                                                                        

                                                                                    else:	
                                                                                        AdminuserlistActive16A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant161=cmbPlant).values()
                                                                                        if AdminuserlistActive16A:  
                                                                                                lUnitId = 0 
                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
                                                                                                request.session['lcompanyid'] = AdminuserlistPWDOBJ['lcompanyid']
                                                                                                request.session['scompantname'] = AdminuserlistPWDOBJ['scompanyname']
                                                                                                request.session['semailaddress'] = AdminuserlistPWDOBJ['semailaddress']
                                                                                                request.session['smobile'] = AdminuserlistPWDOBJ['smobile']
                                                                                                request.session['badmin'] = 0
                                                                                                request.session['bstores'] = AdminuserlistPWDOBJ['bstores16']
                                                                                                request.session['bcalibration'] = AdminuserlistPWDOBJ['bcalibration16']
                                                                                                request.session['bservice'] = AdminuserlistPWDOBJ['bservice16']
                                                                                                request.session['bmsa'] = AdminuserlistPWDOBJ['bmsa16']
                                                                                                request.session['breadonly'] = AdminuserlistPWDOBJ['breadonly16']
                                                                                                request.session['ballfeatures'] = AdminuserlistPWDOBJ['ballfeatures16']
                                                                                                request.session['bmasterlistonlyallplant'] = 0
                                                                                                return Dashboard(request)
                                                                                                
                                                                                        else:	
                                                                                            AdminuserlistActive17A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant171=cmbPlant).values()
                                                                                            if AdminuserlistActive17A:  
                                                                                                    lUnitId = 0 
                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                    return Dashboard(request)
                                                                                                        
                                                                                            else:	
                                                                                                AdminuserlistActive18A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant181=cmbPlant).values()
                                                                                                if AdminuserlistActive18A:  
                                                                                                        lUnitId = 0 
                                                                                                        request.session['lCategoryID'] = 0                        
                                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                        return Dashboard(request)

        
                                                                                                else:	
                                                                                                    AdminuserlistActive19A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant191=cmbPlant).values()
                                                                                                    if AdminuserlistActive19A:  
                                                                                                            lUnitId = 0 
                                                                                                            request.session['lCategoryID'] = 0                        
                                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                            return Dashboard(request)


                                                                                                    else:	
                                                                                                        AdminuserlistActive20A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant201=cmbPlant).values()
                                                                                                        if AdminuserlistActive20A:  
                                                                                                                lUnitId = 0 
                                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                return Dashboard(request)

                                                                                                        else:	
                                                                                                            AdminuserlistActive21A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant211=cmbPlant).values()
                                                                                                            if AdminuserlistActive21A:  
                                                                                                                    lUnitId = 0 
                                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                    return Dashboard(request)

                                                                                                            else:	
                                                                                                                AdminuserlistActive22A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant221=cmbPlant).values()
                                                                                                                if AdminuserlistActive22A:  
                                                                                                                        lUnitId = 0 
                                                                                                                        request.session['lCategoryID'] = 0                        
                                                                                                                        request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                        request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                        request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                        request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                        request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                        return Dashboard(request)

                                                                                                                else:	
                                                                                                                    AdminuserlistActive23A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant231=cmbPlant).values()
                                                                                                                    if AdminuserlistActive23A:  
                                                                                                                            lUnitId = 0 
                                                                                                                            request.session['lCategoryID'] = 0                        
                                                                                                                            request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                            request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                            request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                            request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                            request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                            return Dashboard(request)

                                                                                                                    else:	
                                                                                                                        AdminuserlistActive24A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant241=cmbPlant).values()
                                                                                                                        if AdminuserlistActive24A:  
                                                                                                                                lUnitId = 0 
                                                                                                                                request.session['lCategoryID'] = 0                        
                                                                                                                                request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                                request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                                request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                                request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                                request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                                return Dashboard(request)



                                                                                                                        else:	
                                                                                                                            AdminuserlistActive25A = Adminuserlist.objects.filter(luserid=AdminuserlistPWDOBJ['luserid'],bactive=1,lplant251=cmbPlant).values()
                                                                                                                            if AdminuserlistActive25A:  
                                                                                                                                    lUnitId = 0 
                                                                                                                                    request.session['lCategoryID'] = 0                        
                                                                                                                                    request.session['lLoginUserId'] = AdminuserlistPWDOBJ['luserid']
                                                                                                                                    request.session['semployeename'] = AdminuserlistPWDOBJ['semployeename']
                                                                                                                                    request.session['semployeeno'] = AdminuserlistPWDOBJ['semployeeno']
                                                                                                                                    request.session['lunitid'] = AdminuserlistPWDOBJ['lunitid']
                                                                                                                                    request.session['sunitno'] = AdminuserlistPWDOBJ['sunitno']
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
                                                                                                                                    return Dashboard(request)








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

 