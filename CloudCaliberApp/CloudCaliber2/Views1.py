from django.shortcuts import render
import os
import re
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect


import textutils.settings

import pymssql
import threading as th

from CloudCaliber.models import Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist, Masterinstrumentpreventivemaintenancelist, Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1

from CloudCaliber.models import Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Admintoleranceslipgaugelist, Admintoleranceslipgaugelist, Admintoleranceslipgaugelist, Admintoleranceslipgaugelist, Admintoleranceslipgaugelist, Admintoleranceslipgaugelist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist

from CloudCaliber.serializers import  AdminuserlistSerializer








    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminExternalAgencyListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    lcompanyid = request.session['lcompanyid']
                    assert isinstance(request, HttpRequest)  
                    Adminexternalagencylist_list = Adminexternalagencylist.objects.get(lplantid=lcompanyid).order_by('sdescription')     
                    return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
                    {
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    lcompanyid = request.session['lcompanyid']
                    assert isinstance(request, HttpRequest) 
                    Adminexternalagencylist_list = Adminexternalagencylist.objects.filter(sdescription__icontains=txtSearch,lplantid=lcompanyid).values()
                    return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
                    {
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            lcompanyid = request.session['lcompanyid']
            assert isinstance(request, HttpRequest)  
            Adminexternalagencylist_list = Adminexternalagencylist.objects.get(lplantid=lcompanyid).order_by('sdescription')     
                     
            return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
                {
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')









