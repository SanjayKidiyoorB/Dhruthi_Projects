from django.shortcuts import render
import os
import re
import calendar
import mimetypes
from pathlib import Path
from calendar import HTMLCalendar

from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage


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
def AdminUnitList(request):

 
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
 

    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminUnitAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Unitlist_list = Adminunitlist.objects.order_by('splantno')     
                    return render(request,  'CloudCaliber/AdminUnitList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Unitlist_list': Unitlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Unitlist_list = Adminunitlist.objects.filter(splantno__icontains=txtSearch) | Adminunitlist.objects.filter(splantname__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/AdminUnitList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Unitlist_list': Unitlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Unitlist_list = Adminunitlist.objects.order_by('splantno')     
            return render(request,  'CloudCaliber/AdminUnitList.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Unitlist_list': Unitlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')

 

@csrf_exempt
def AdminUnitAdd(request):
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('AdminUnitList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtUnitName=data.get('txtUnitName')
            txtLocation=data.get('txtLocation') 

            txtCCEmailName1=data.get('txtCCEmailName1') 
            txtCCEmailAddress1=data.get('txtCCEmailAddress1') 
            txtCCEmailName2=data.get('txtCCEmailName2') 
            txtCCEmailAddress2=data.get('txtCCEmailAddress2')
            txtCCEmailName3=data.get('txtCCEmailName3') 
            txtCCEmailAddress3=data.get('txtCCEmailAddress3')
            txtCCEmailName4=data.get('txtCCEmailName4') 
            txtCCEmailAddress4=data.get('txtCCEmailAddress4')
            txtCCEmailName5=data.get('txtCCEmailName5') 
            txtCCEmailAddress5=data.get('txtCCEmailAddress5')

            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']

            Adminunitlist_AddNewOBJ = Adminunitlist(splantno =txtUnitName, splantname =txtLocation, sccname1 = txtCCEmailName1, sccemailadd1 = txtCCEmailAddress1, sccname2 = txtCCEmailName2, sccemailadd2 = txtCCEmailAddress2, sccname3 = txtCCEmailName3, sccemailadd3 = txtCCEmailAddress3,sccname4 = txtCCEmailName4, sccemailadd4 = txtCCEmailAddress4,sccname5 = txtCCEmailName5, sccemailadd5 = txtCCEmailAddress5, lcompanyid=lcompanyid, scompantname=scompantname, scode ="N A")
 
            Adminunitlist_AddNewOBJ.save()

            messages.success(request, 'Unit is Added successfully!')
           
            return   redirect('AdminUnitList')  
            

    else:               
        return render(request, "CloudCaliber/AdminUnitAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def AdminUnitDetails(request,lID):
    
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('AdminUnitList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtUnitName=data.get('txtUnitName')
            txtLocation=data.get('txtLocation')  
            txtCCEmailName1=data.get('txtCCEmailName1') 
            txtCCEmailAddress1=data.get('txtCCEmailAddress1') 
            txtCCEmailName2=data.get('txtCCEmailName2') 
            txtCCEmailAddress2=data.get('txtCCEmailAddress2')
            txtCCEmailName3=data.get('txtCCEmailName3') 
            txtCCEmailAddress3=data.get('txtCCEmailAddress3')
            txtCCEmailName4=data.get('txtCCEmailName4') 
            txtCCEmailAddress4=data.get('txtCCEmailAddress4')
            txtCCEmailName5=data.get('txtCCEmailName5') 
            txtCCEmailAddress5=data.get('txtCCEmailAddress5')


            Adminunitlist_AddNewOBJ = Adminunitlist.objects.get(lplantid=lID) 

            Adminunitlist_AddNewOBJ.splantno =txtUnitName
            Adminunitlist_AddNewOBJ.splantname =txtLocation

            Adminunitlist_AddNewOBJ.sccname1 =txtCCEmailName1
            Adminunitlist_AddNewOBJ.sccemailadd1 =txtCCEmailAddress1
            Adminunitlist_AddNewOBJ.sccname2 =txtCCEmailName2
            Adminunitlist_AddNewOBJ.sccemailadd2 =txtCCEmailAddress2
            Adminunitlist_AddNewOBJ.sccname3 =txtCCEmailName3
            Adminunitlist_AddNewOBJ.sccemailadd3 =txtCCEmailAddress3
            Adminunitlist_AddNewOBJ.sccname4 =txtCCEmailName4
            Adminunitlist_AddNewOBJ.sccemailadd4 =txtCCEmailAddress4
            Adminunitlist_AddNewOBJ.sccname5 =txtCCEmailName5
            Adminunitlist_AddNewOBJ.sccemailadd5 =txtCCEmailAddress5


            Adminunitlist_AddNewOBJ.scode ="N A"
            Adminunitlist_AddNewOBJ.save()

            messages.success(request, 'Unit is Updated successfully!')
            Unitlist_list = Adminunitlist.objects.get(lplantid=lID)              
            return render(request, "CloudCaliber/AdminUnitDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list,  
                        }
                        )

    else: 
        Unitlist_list = Adminunitlist.objects.get(lplantid=lID)              
        return render(request, "CloudCaliber/AdminUnitDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Unitlist_list': Unitlist_list,  
                        }
                        )





@csrf_exempt
def AdminAreaofUseList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminAreaofUseAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    lunitidA=request.session['lunitid']  
                    AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
                    return render(request,  'CloudCaliber/Adminlocationlist.html', 
                    {
                        'title':request.session['sunitno'], 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'AreaofUselist_list': AreaofUselist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    lunitidA=request.session['lunitid']  
                    AreaofUselist_list = Adminlocationlist.objects.filter(slocationname__icontains=txtSearch, lplantid=lunitidA) | Adminlocationlist.objects.filter(scontactperson__icontains=txtSearch, lplantid=lunitidA) & Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values() 
                    return render(request,  'CloudCaliber/Adminlocationlist.html', 
                    {
                        'title':request.session['sunitno'], 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AreaofUselist_list': AreaofUselist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:      
            
                #Renders the contact page."""
        assert isinstance(request, HttpRequest)   
        lunitidA=request.session['lunitid']  
        AreaofUselist_list = Adminlocationlist.objects.filter(lplantid=lunitidA).order_by('slocationname').values()     
        return render(request,  'CloudCaliber/Adminlocationlist.html', 
                {
                    'title':request.session['sunitno'], 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                    'message':'Your User list page.',
                    'year':datetime.now().year, 
                    'AreaofUselist_list': AreaofUselist_list, 
                }
                ) 

 

@csrf_exempt
def adminLocationListDelete(request,lID):
    lCatID = 0
    
     
    
    Adminlocationlist_list =  Adminlocationlist.objects.get(lid=lID).delete()    
    # Details.objects.filter(id=pk).delete()
    return   redirect('AdminAreaofUseList')  




@csrf_exempt
def AdminAreaofUseAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  
                         
            return   redirect('AdminAreaofUseList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtAreaName=data.get('txtAreaName')
            txtOwner=data.get('txtOwner')  
            txtOwnerEmail=data.get('txtOwnerEmail')
            lunitid=request.session['lunitid']  
             
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']

            Adminlocationlist_AddNewOBJ = Adminlocationlist(slocationname =txtAreaName, lcompanyid=lcompanyid, scompantname=scompantname, scontactperson =txtOwner, scontactemailid =txtOwnerEmail, lplantid= lunitid)
 
            Adminlocationlist_AddNewOBJ.save()

            messages.success(request, 'Area of Use is Added successfully!') 
            lunitidA=request.session['lunitid']  
                 
            return   redirect('AdminAreaofUseList')  


    else:               
        return render(request, "CloudCaliber/AdminAreaofUseAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def AdminAreaofUseDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
                 
            return   redirect('AdminAreaofUseList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtAreaName=data.get('txtAreaName')
            txtOwner=data.get('txtOwner')  
            txtOwnerEmail=data.get('txtOwnerEmail')
            lunitid=request.session['lunitid']   

            Adminlocationlist_AddNewOBJ = Adminlocationlist.objects.get(lid=lID) 

            Adminlocationlist_AddNewOBJ.slocationname =txtAreaName
            Adminlocationlist_AddNewOBJ.scontactperson =txtOwner
            Adminlocationlist_AddNewOBJ.scontactemailid = txtOwnerEmail
            Adminlocationlist_AddNewOBJ.save()

            messages.success(request, 'AreaofUse is Updated successfully!')
            AreaofUselist_list = Adminlocationlist.objects.get(lplantid=lID)              
            return render(request, "CloudCaliber/AdminAreaofUseDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AreaofUselist_list': AreaofUselist_list,  
                        }
                        )

    else: 
        AreaofUselist_list = Adminlocationlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/AdminAreaofUseDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AreaofUselist_list': AreaofUselist_list,  
                        }
                        )





      

@csrf_exempt
def AdminUOMList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminUOMAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    UOMlist_list = Adminunitofmeasurelist.objects.order_by('sunitofmeasure')     
                    return render(request,  'CloudCaliber/Adminunitofmeasurelist.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'UOMlist_list': UOMlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    UOMlist_list = Adminunitofmeasurelist.objects.filter(sunitofmeasure__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/Adminunitofmeasurelist.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'UOMlist_list': UOMlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            UOMlist_list = Adminunitofmeasurelist.objects.order_by('sunitofmeasure')     
            return render(request,  'CloudCaliber/Adminunitofmeasurelist.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'UOMlist_list': UOMlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')

 

@csrf_exempt
def AdminUOMAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('AdminUOMList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtUnitName=data.get('txtUnitName')
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']  

            Adminunitofmeasurelist_AddNewOBJ = Adminunitofmeasurelist(sunitofmeasure =txtUnitName,sshort="", lcompanyid=lcompanyid, scompantname=scompantname)
 
            Adminunitofmeasurelist_AddNewOBJ.save()

            messages.success(request, 'Unit of Measure is Added successfully!')
            
            return   redirect('AdminUOMList')  


    else:               
        return render(request, "CloudCaliber/AdminunitofmeasureAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def AdminUOMDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('AdminUOMList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtUnitName=data.get('txtUnitName')   

            Adminunitofmeasurelist_AddNewOBJ = Adminunitofmeasurelist.objects.get(lid=lID) 

            Adminunitofmeasurelist_AddNewOBJ.sunitofmeasure = txtUnitName 
            Adminunitofmeasurelist_AddNewOBJ.save()

            messages.success(request, 'Uniot of Measure is Updated successfully!')
            UOMlist_list = Adminunitofmeasurelist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/AdminunitofmeasureDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'UOMlist_list': UOMlist_list,  
                        }
                        )

    else: 
        UOMlist_list = Adminunitofmeasurelist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/AdminunitofmeasureDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'UOMlist_list': UOMlist_list,  
                        }
                        )




@csrf_exempt
def adminExternalAgencyList(request):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 

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
                    Adminexternalagencylist_list = Adminexternalagencylist.objects.filter(lcompanyid=lcompanyid).order_by('sdescription')     
                    return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
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
                    Adminexternalagencylist_list = Adminexternalagencylist.objects.filter(sdescription__icontains=txtSearch,lcompanyid=lcompanyid).values()
                    return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:    
            
            #Renders the contact page."""
        lcompanyid = request.session['lcompanyid']
        assert isinstance(request, HttpRequest)  
        Adminexternalagencylist_list = Adminexternalagencylist.objects.filter(lcompanyid=lcompanyid).order_by('sdescription')     
                    
        return render(request,  'CloudCaliber/adminExternalAgencyList.html', 
            {
                    'title':'User list', 
                    'sPlantName': sPlantName ,  
                    'semployeename':  semployeename, 
                    'message':'Your User list page.',
                    'year':datetime.now().year,  
                    'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                }
            ) 










@csrf_exempt
def adminExternalAgencyListAdd(request):
    lcompanyid = request.session['lcompanyid']
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 

 
    lunitid = request.session['lunitid']

    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":

        txtVendorName = ""
        bCalibration1 = 0
        bPurchaseVendor1 = 0
        bService1 = 0
        bInspection1 = 0
        txtScopeofCalibration = ""
        cmbBasisofApproval = 0
        sBasisofApproval = ""
        dtnablcertificatevalidity = ""
        txtNABLCertNo = ""
        txtUncertainityVal = ""
        txtVendorCode = ""
        txtContaqctPerson = ""
        txtContactNumber = ""
        txtEmailAddress = ""
        txtAddress = ""
        txtCity = ""
        txtPin = ""
        txtState = ""
        txtCountry = ""


        dtnablcertificatevalidity1  = ""
        dtnablcertificatevalidity2 = ""
        dtnablcertificatevalidity3 = ""
        dtnablcertificatevalidity1Date = datetime.now()

        data = request.POST
        if 'txtVendorName' in request.POST:
            txtVendorName=request.POST['txtVendorName'] 
        if 'bCalibration' in request.POST:
            bCalibration1=1
        if 'bPurchaseVendor' in request.POST:
            bPurchaseVendor1=1
        if 'bService' in request.POST:
            bService1=1
        if 'bInspection' in request.POST:
            bInspection1=1
        if 'BasisofApproval' in request.POST:
            cmbBasisofApproval=int(request.POST['BasisofApproval'])

        if cmbBasisofApproval == 0:
            sBasisofApproval = "NABL Certified"
        if cmbBasisofApproval == 1:
            sBasisofApproval = "Other Certification"
        if cmbBasisofApproval == 2:
                sBasisofApproval = "Certification N. A."

        if 'txtScopeofCalibration' in request.POST:
            txtScopeofCalibration=request.POST['txtScopeofCalibration']
        if 'dtnablcertificatevalidity' in request.POST:
            dtnablcertificatevalidity=request.POST['dtnablcertificatevalidity']

        dtnablcertificatevalidity1 =dtnablcertificatevalidity
        dtnablcertificatevalidity2  = dtnablcertificatevalidity1.split("-")
        dtnablcertificatevalidity3 = dtnablcertificatevalidity2[2] + "-" + dtnablcertificatevalidity2[1] + "-" + dtnablcertificatevalidity2[0] 

        dtnablcertificatevalidity1Date = datetime.strptime(dtnablcertificatevalidity3, '%d-%m-%Y').date()

        if 'txtNABLCertNo' in request.POST:
            txtNABLCertNo=request.POST['txtNABLCertNo']
        if 'txtUncertainityVal' in request.POST:
            txtUncertainityVal=request.POST['txtUncertainityVal']
        if 'txtVendorCode' in request.POST:
            txtVendorCode=request.POST['txtVendorCode']
        if 'txtContaqctPerson' in request.POST:
            txtContaqctPerson=request.POST['txtContaqctPerson']
        if 'txtContactNumber' in request.POST:
            txtContactNumber=request.POST['txtContactNumber']
        if 'txtEmailAddress' in request.POST:
            txtEmailAddress=request.POST['txtEmailAddress']
        if 'txtAddress' in request.POST:
            txtAddress=request.POST['txtAddress']
        if 'txtCity' in request.POST:
            txtCity=request.POST['txtCity']
        if 'txtPin' in request.POST:
            txtPin=request.POST['txtPin']
        if 'txtState' in request.POST:
            txtState=request.POST['txtState']
        if 'txtCountry' in request.POST:
            txtCountry=request.POST['txtCountry']

    
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminExternalAgencyList')  

        if 'cmbSaveAdd' in request.POST:  


            Adminexternalagencylist_AddNewOBJ = Adminexternalagencylist(txtVendorName =txtVendorName, svendorid = txtVendorCode)
            Adminexternalagencylist_AddNewOBJ.save()

            lagencyid =0
            lagencyid = Adminexternalagencylist_AddNewOBJ.lagencyid


            Adminexternalagencylist_listSaveUpdate =  Adminexternalagencylist.objects.get(lagencyid =lagencyid) 
        
            Adminexternalagencylist_listSaveUpdate.sdescription = txtVendorName
            Adminexternalagencylist_listSaveUpdate.saddress1 = txtAddress
            Adminexternalagencylist_listSaveUpdate.saddress2 = ""
            Adminexternalagencylist_listSaveUpdate.saddress3 = txtCountry
            Adminexternalagencylist_listSaveUpdate.scity = txtCity
            Adminexternalagencylist_listSaveUpdate.sstate = txtState
            Adminexternalagencylist_listSaveUpdate.pin = txtPin
            Adminexternalagencylist_listSaveUpdate.scontact_no = txtContactNumber
            Adminexternalagencylist_listSaveUpdate.semail = txtEmailAddress
            Adminexternalagencylist_listSaveUpdate.scontact_person = txtContaqctPerson
            Adminexternalagencylist_listSaveUpdate.s_o_calib = txtScopeofCalibration
            Adminexternalagencylist_listSaveUpdate.sbasisofaffiliation = sBasisofApproval
            Adminexternalagencylist_listSaveUpdate.svendorid = txtVendorCode
            Adminexternalagencylist_listSaveUpdate.bmaker = bPurchaseVendor1
            Adminexternalagencylist_listSaveUpdate.bservice = bService1
            Adminexternalagencylist_listSaveUpdate.bcalib = bCalibration1
            Adminexternalagencylist_listSaveUpdate.bcustomers = 0
            Adminexternalagencylist_listSaveUpdate.bmeasurement = bInspection1
            Adminexternalagencylist_listSaveUpdate.bcmm = 0
            Adminexternalagencylist_listSaveUpdate.calib_rate = 0
            Adminexternalagencylist_listSaveUpdate.dconfidencelevel = 0
            Adminexternalagencylist_listSaveUpdate.sconfidencelevel = txtUncertainityVal
            Adminexternalagencylist_listSaveUpdate.dtnablcertificatevalidity = dtnablcertificatevalidity3
            Adminexternalagencylist_listSaveUpdate.scertificateno = txtNABLCertNo
            Adminexternalagencylist_listSaveUpdate.snablcertificatedate = dtnablcertificatevalidity3
            Adminexternalagencylist_listSaveUpdate.snablcertificatefile = ""
            Adminexternalagencylist_listSaveUpdate.snablcertificatepath = ""
            Adminexternalagencylist_listSaveUpdate.llocationid = 0
            Adminexternalagencylist_listSaveUpdate.sgst = ""
            Adminexternalagencylist_listSaveUpdate.span = ""
            Adminexternalagencylist_listSaveUpdate.lplantid = 0
            Adminexternalagencylist_listSaveUpdate.splantname = ""
            Adminexternalagencylist_listSaveUpdate.lcompanyid = lcompanyid
            Adminexternalagencylist_listSaveUpdate.scompantname = ""


            Adminexternalagencylist_listSaveUpdate.save()
            messages.success(request, 'Agency Details is Added successfully!')
        
        # Adminexternalagencylist_AddNewOBJ = Adminexternalagencylist(stoleranceclass =txtToleranceClass)
        # Adminexternalagencylist_AddNewOBJ.save()


 
                        
    

        return redirect('adminExternalAgencyList')  

    else:


        Adminexternalagencylist_list = Adminexternalagencylist.objects.filter(lcompanyid=lcompanyid).order_by('sdescription')     
        
        sExpiryDate = ""  
        sExpiryDate1 = ""
        sExpiryDate2 = ""
        sExpiryDate3 = "" 
        sExpiryDate4 = ""    
        dtExpiryDate = datetime.now()   
        sExpiryDate2 = str(dtExpiryDate)


        sExpiryDate3  = sExpiryDate2.split("-")
        sExpiryDate4  = sExpiryDate3[2].split(" ")
        sExpiryDate = sExpiryDate3[0] + "-" + sExpiryDate3[1] + "-" + sExpiryDate4[0] 


 

        
        return render(request,  'CloudCaliber/adminExternalAgencyListAdd.html', 
            {
                    'title':'User list', 
                    'sPlantName': sPlantName ,  
                    'semployeename':  semployeename,
                    'sExpiryDate': sExpiryDate,
                    'message':'Your User list page.',
                    'year':datetime.now().year,  
                    'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                }
        )  





@csrf_exempt
def adminExternalAgencyListDetails(request,lID):
    lcompanyid = request.session['lcompanyid']
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)


    
    if request.method == "POST":

        txtVendorName = ""
        bCalibration1 = 0
        bPurchaseVendor1 = 0
        bService1 = 0
        bInspection1 = 0
        txtScopeofCalibration = ""
        cmbBasisofApproval = 0
        sBasisofApproval = ""
        dtnablcertificatevalidity = ""
        txtNABLCertNo = ""
        txtUncertainityVal = ""
        txtVendorCode = ""
        txtContaqctPerson = ""
        txtContactNumber = ""
        txtEmailAddress = ""
        txtAddress = ""
        txtCity = ""
        txtPin = ""
        txtState = ""
        txtCountry = ""
        uploaded_file_url = ""

        dtnablcertificatevalidity1  = ""
        dtnablcertificatevalidity2 = ""
        dtnablcertificatevalidity3 = ""
        dtnablcertificatevalidity1Date = datetime.now()


        data = request.POST
        if 'txtVendorName' in request.POST:
            txtVendorName=request.POST['txtVendorName'] 
        if 'bCalibration' in request.POST:
            bCalibration1=1
        if 'bPurchaseVendor' in request.POST:
            bPurchaseVendor1=1
        if 'bService' in request.POST:
            bService1=1
        if 'bInspection' in request.POST:
            bInspection1=1
        if 'BasisofApproval' in request.POST:
            cmbBasisofApproval=int(request.POST['BasisofApproval'])

        if cmbBasisofApproval == 0:
            sBasisofApproval = "NABL Certified"
        if cmbBasisofApproval == 1:
            sBasisofApproval = "Other Certification"
        if cmbBasisofApproval == 2:
                sBasisofApproval = "Certification N. A."

        if 'txtScopeofCalibration' in request.POST:
            txtScopeofCalibration=request.POST['txtScopeofCalibration']
        if 'dtnablcertificatevalidity' in request.POST:
            dtnablcertificatevalidity=request.POST['dtnablcertificatevalidity']

        dtnablcertificatevalidity1 =dtnablcertificatevalidity
        dtnablcertificatevalidity2  = dtnablcertificatevalidity1.split("-")
        dtnablcertificatevalidity3 = dtnablcertificatevalidity2[2] + "-" + dtnablcertificatevalidity2[1] + "-" + dtnablcertificatevalidity2[0] 

        dtnablcertificatevalidity1Date = datetime.strptime(dtnablcertificatevalidity3, '%d-%m-%Y').date()

        if 'txtNABLCertNo' in request.POST:
            txtNABLCertNo=request.POST['txtNABLCertNo']
        if 'txtUncertainityVal' in request.POST:
            txtUncertainityVal=request.POST['txtUncertainityVal']
        if 'txtVendorCode' in request.POST:
            txtVendorCode=request.POST['txtVendorCode']
        if 'txtContaqctPerson' in request.POST:
            txtContaqctPerson=request.POST['txtContaqctPerson']
        if 'txtContactNumber' in request.POST:
            txtContactNumber=request.POST['txtContactNumber']
        if 'txtEmailAddress' in request.POST:
            txtEmailAddress=request.POST['txtEmailAddress']
        if 'txtAddress' in request.POST:
            txtAddress=request.POST['txtAddress']
        if 'txtCity' in request.POST:
            txtCity=request.POST['txtCity']
        if 'txtPin' in request.POST:
            txtPin=request.POST['txtPin']
        if 'txtState' in request.POST:
            txtState=request.POST['txtState']
        if 'txtCountry' in request.POST:
            txtCountry=request.POST['txtCountry']


    
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminExternalAgencyList')  

        if 'cmbSaveAdd' in request.POST:  


            Adminexternalagencylist_listSaveUpdate =  Adminexternalagencylist.objects.get(lagencyid =lID) 
        
            Adminexternalagencylist_listSaveUpdate.sdescription = txtVendorName
            Adminexternalagencylist_listSaveUpdate.saddress1 = txtAddress
            Adminexternalagencylist_listSaveUpdate.saddress2 = ""
            Adminexternalagencylist_listSaveUpdate.saddress3 = txtCountry
            Adminexternalagencylist_listSaveUpdate.scity = txtCity
            Adminexternalagencylist_listSaveUpdate.sstate = txtState
            Adminexternalagencylist_listSaveUpdate.pin = txtPin
            Adminexternalagencylist_listSaveUpdate.scontact_no = txtContactNumber
            Adminexternalagencylist_listSaveUpdate.semail = txtEmailAddress
            Adminexternalagencylist_listSaveUpdate.scontact_person = txtContaqctPerson
            Adminexternalagencylist_listSaveUpdate.s_o_calib = txtScopeofCalibration
            Adminexternalagencylist_listSaveUpdate.sbasisofaffiliation = sBasisofApproval
            Adminexternalagencylist_listSaveUpdate.svendorid = txtVendorCode
            Adminexternalagencylist_listSaveUpdate.bmaker = bPurchaseVendor1
            Adminexternalagencylist_listSaveUpdate.bservice = bService1
            Adminexternalagencylist_listSaveUpdate.bcalib = bCalibration1
            Adminexternalagencylist_listSaveUpdate.bcustomers = 0
            Adminexternalagencylist_listSaveUpdate.bmeasurement = bInspection1
            Adminexternalagencylist_listSaveUpdate.bcmm = 0
            Adminexternalagencylist_listSaveUpdate.calib_rate = 0
            Adminexternalagencylist_listSaveUpdate.dconfidencelevel = 0
            Adminexternalagencylist_listSaveUpdate.sconfidencelevel = txtUncertainityVal
            Adminexternalagencylist_listSaveUpdate.dtnablcertificatevalidity = dtnablcertificatevalidity3
            Adminexternalagencylist_listSaveUpdate.scertificateno = txtNABLCertNo
            Adminexternalagencylist_listSaveUpdate.snablcertificatedate = dtnablcertificatevalidity3
            #Adminexternalagencylist_listSaveUpdate.snablcertificatefile = ""
            #Adminexternalagencylist_listSaveUpdate.snablcertificatepath = ""
            Adminexternalagencylist_listSaveUpdate.llocationid = 0
            Adminexternalagencylist_listSaveUpdate.sgst = ""
            Adminexternalagencylist_listSaveUpdate.span = ""
            Adminexternalagencylist_listSaveUpdate.lplantid = 0
            Adminexternalagencylist_listSaveUpdate.splantname = ""
            Adminexternalagencylist_listSaveUpdate.lcompanyid = lcompanyid
            Adminexternalagencylist_listSaveUpdate.scompantname = ""


            Adminexternalagencylist_listSaveUpdate.save()
            messages.success(request, 'Agency Details is Updated successfully!')
        


            sExpiryDate = ""  
            sExpiryDate1 = ""
            sExpiryDate2 = ""
            sExpiryDate3 = "" 
            sExpiryDate4 = ""    
            dtExpiryDate = datetime.now()  

            Adminexternalagencylist_list = Adminexternalagencylist.objects.get(lagencyid=lID) 
            if Adminexternalagencylist_list:
                sExpiryDate2 = Adminexternalagencylist_list.dtnablcertificatevalidity
            else:
                sExpiryDate2 = str(dtExpiryDate)


            sExpiryDate3  = sExpiryDate2.split("-")
            sExpiryDate4  = sExpiryDate3[2].split(" ")
            if len(sExpiryDate4) == 1:

                sExpiryDate = sExpiryDate3[2] + "-" + sExpiryDate3[1] + "-" + sExpiryDate3[0]
            else:
                sExpiryDate = sExpiryDate3[0] + "-" + sExpiryDate3[1] + "-" + sExpiryDate4[0]    
                            
        

            return render(request,  'CloudCaliber/adminExternalAgencyListDetails.html', 
                {
                        'title':'User list',  
                        'sPlantName': sPlantName ,
                        'sExpiryDate': sExpiryDate,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                ) 
        
        if 'cmdDownloadCertificate' in request.POST:  

            sFile = ""
            Adminexternalagencylist_listQ = Adminexternalagencylist.objects.get(lagencyid=lID) 
            if Adminexternalagencylist_listQ:
                sFile = Adminexternalagencylist_listQ.snablcertificatefile
            #fs = FileSystemStorage()
            #file_path = fs.url(sFile)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # Define text file name
            filename = "/media/" + sFile
            # Define the full file path
            filepath =  BASE_DIR + filename


            # filepath = str(BASE_DIR)
            # filepath = filepath + filename

            # Open the file for reading content
            path = open(filepath, 'rb')
            # Set the mime type
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            #response['Content-Disposition'] = "attachment; sFile=%s" % sFile
            response['Content-Disposition'] = "inline; sFile=%s" % sFile
            # Return the response value
            return response

 
            
        if request.method == 'POST' and request.FILES['UploadFiles']: 
            

            myfile = request.FILES['UploadFiles']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            Adminexternalagencylist_listSaveUpdate =  Adminexternalagencylist.objects.get(lagencyid =lID) 
            Adminexternalagencylist_listSaveUpdate.snablcertificatefile = filename
            Adminexternalagencylist_listSaveUpdate.snablcertificatepath =uploaded_file_url
            Adminexternalagencylist_listSaveUpdate.save()
            messages.success(request, 'Agency NABL Certificate is Updated successfully!')
        

            sExpiryDate = ""  
            sExpiryDate1 = ""
            sExpiryDate2 = ""
            sExpiryDate3 = "" 
            sExpiryDate4 = ""    
            dtExpiryDate = datetime.now()  

            Adminexternalagencylist_list = Adminexternalagencylist.objects.get(lagencyid=lID) 
            if Adminexternalagencylist_list:
                sExpiryDate2 = Adminexternalagencylist_list.dtnablcertificatevalidity
            else:
                sExpiryDate2 = str(dtExpiryDate)


            sExpiryDate3  = sExpiryDate2.split("-")
            sExpiryDate4  = sExpiryDate3[2].split(" ")
            if len(sExpiryDate4) == 1:

                sExpiryDate = sExpiryDate3[2] + "-" + sExpiryDate3[1] + "-" + sExpiryDate3[0]
            else:
                sExpiryDate = sExpiryDate3[0] + "-" + sExpiryDate3[1] + "-" + sExpiryDate4[0]    
                            
        

            return render(request,  'CloudCaliber/adminExternalAgencyListDetails.html', 
                {
                        'title':'User list',  
                        'sPlantName': sPlantName ,
                        'sExpiryDate': sExpiryDate,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                    }
                ) 




    else:


        sExpiryDate = ""  
        sExpiryDate1 = ""
        sExpiryDate2 = ""
        sExpiryDate3 = "" 
        sExpiryDate4 = ""    
        dtExpiryDate = datetime.now()  

        Adminexternalagencylist_list = Adminexternalagencylist.objects.get(lagencyid=lID) 
        if Adminexternalagencylist_list:
            sExpiryDate2 = Adminexternalagencylist_list.dtnablcertificatevalidity
        else:
            sExpiryDate2 = str(dtExpiryDate)


        sExpiryDate3  = sExpiryDate2.split("-")
        sExpiryDate4  = sExpiryDate3[2].split(" ")
        if len(sExpiryDate4) == 1:

            sExpiryDate = sExpiryDate3[2] + "-" + sExpiryDate3[1] + "-" + sExpiryDate3[0]
        else:
            sExpiryDate = sExpiryDate3[0] + "-" + sExpiryDate3[1] + "-" + sExpiryDate4[0]               
    

        return render(request,  'CloudCaliber/adminExternalAgencyListDetails.html', 
            {
                    'title':'User list', 
                    'sPlantName': sPlantName , 
                    'sExpiryDate': sExpiryDate,
                    'semployeename':  semployeename, 
                    'message':'Your User list page.',
                    'year':datetime.now().year,  
                    'Adminexternalagencylist_list': Adminexternalagencylist_list, 
                }
            )  




@csrf_exempt
def adminOperatorList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminOperatorListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Adminoperatorlist_list = Adminoperatorlist.objects.order_by('soperator')     
                    return render(request,  'CloudCaliber/adminOperatorList.html', 
                    {
                        'title':'User list',
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Adminoperatorlist_list': Adminoperatorlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Adminoperatorlist_list = Adminoperatorlist.objects.filter(soperator__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminOperatorList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminoperatorlist_list': Adminoperatorlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Adminoperatorlist_list = Adminoperatorlist.objects.order_by('soperator')     
            return render(request,  'CloudCaliber/adminOperatorList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminoperatorlist_list': Adminoperatorlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminOperatorListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminOperatorList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsoperator=data.get('txtsoperator') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            adminOperatorList_AddNewOBJ = Adminoperatorlist(soperator =txtsoperator, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            adminOperatorList_AddNewOBJ.save()

            messages.success(request, 'Operator is Added successfully!')
           
            return   redirect('adminOperatorList')  
            

    else:               
        return render(request, "CloudCaliber/adminOperatorListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminOperatorListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminOperatorList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsoperator=data.get('txtsoperator') 

            adminOperatorList_AddNewOBJ = Adminoperatorlist.objects.get(lid=lID) 

            adminOperatorList_AddNewOBJ.soperator =txtsoperator
            adminOperatorList_AddNewOBJ.save()

            messages.success(request, 'Operator is Updated successfully!')
            adminOperatorList_list = Adminoperatorlist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminOperatorListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminOperatorList_list': adminOperatorList_list,  
                        }
                        )

    else: 
        adminOperatorList_list = Adminoperatorlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminOperatorListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminOperatorList_list': adminOperatorList_list,  
                        }
                        )



@csrf_exempt
def adminSparepartsList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminSparepartsListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Adminassetsparepartslist_list = Adminassetsparepartslist.objects.order_by('sdescription')     
                    return render(request,  'CloudCaliber/adminSparepartsList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'adminSparepartsList_list': Adminassetsparepartslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Adminassetsparepartslist_list = Adminassetsparepartslist.objects.filter(sdescription__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminSparepartsList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'adminSparepartsList_list': Adminassetsparepartslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Adminassetsparepartslist_list = Adminassetsparepartslist.objects.order_by('sdescription')     
            return render(request,  'CloudCaliber/adminSparepartsList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'adminSparepartsList_list': Adminassetsparepartslist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminSparepartsListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminSparepartsList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsdescription=data.get('txtsSpareParts') 
            txtsSparePartsQty=data.get('txtsSparePartsQty')
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            if data.get('txtsSparePartsQty').isnumeric():
                txtsSparePartsQty=data.get('txtsSparePartsQty')
            else:
                txtsSparePartsQty=0

            Adminassetsparepartslist_AddNewOBJ = Adminassetsparepartslist(sdescription =txtsdescription,ltotqty = txtsSparePartsQty, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname, srevetails ="", bstock=0, drate =0, lopenbal =0, linward =0, loutward=0, suom="", scode="",bpartno=0, bequipment=0, bmachine=0, brange2variable=0, brange3variable=0, bmaterial=0, bcontinuousno=0, btype=0, btype1=0, btype2=0, btype3=0, btype4=0, btype5=0, btype6=0, lcode=0, lcode3=0, lcode4=0, lcode5=0, stitle="", stitle1="", stitle2="", stitle3="", stitle4="", stitle5="")
 
            Adminassetsparepartslist_AddNewOBJ.save()

            messages.success(request, 'Spare Parts is Added successfully!')
           
            return   redirect('adminSparepartsList')  
            

    else:               
        return render(request, "CloudCaliber/adminSparepartsListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminSparepartsListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminSparepartsList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsdescription=data.get('txtsSpareParts') 
            txtsSparePartsQty=data.get('txtsSparePartsQty')

            Adminassetsparepartslist_AddNewOBJ = Adminassetsparepartslist.objects.get(lid=lID) 

            Adminassetsparepartslist_AddNewOBJ.sdescription =txtsdescription
            Adminassetsparepartslist_AddNewOBJ.ltotqty =txtsSparePartsQty
            Adminassetsparepartslist_AddNewOBJ.save()

            messages.success(request, 'Spare Parts is Updated successfully!')
            Adminassetsparepartslist_list = Adminassetsparepartslist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminSparepartsListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminSparepartsList_list': Adminassetsparepartslist_list,  
                        }
                        )

    else: 
        Adminassetsparepartslist_list = Adminassetsparepartslist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminSparepartsListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminSparepartsList_list': Adminassetsparepartslist_list,  
                        }
                        )



 

 





 





@csrf_exempt
def adminMakeListDelete(request,lID):
    lCatID = 0
    
     
    
    Adminmakelist_list =  Adminmakelist.objects.get(lid=lID).delete()    
    # Details.objects.filter(id=pk).delete()
    return   redirect('adminMakeList') 





@csrf_exempt
def  adminMakeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminMakeListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    adminMakeList_list =  Adminmakelist.objects.order_by('smake')     
                    return render(request,  'CloudCaliber/adminMakeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'adminMakeList_list':  adminMakeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    adminMakeList_list =  Adminmakelist.objects.filter(smake__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminMakeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'adminMakeList_list':  adminMakeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:    
        
            
            #Renders the contact page."""
        assert isinstance(request, HttpRequest)  
        adminMakeList_list =  Adminmakelist.objects.order_by('smake')     
        return render(request,  'CloudCaliber/adminMakeList.html', 
            {
                    'title':'User list', 
                    'sPlantName': sPlantName ,  
                    'semployeename':  semployeename, 
                    'message':'Your User list page.',
                    'year':datetime.now().year,  
                    'adminMakeList_list':  adminMakeList_list, 
                }
            ) 


 




 




@csrf_exempt
def adminMakeListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminMakeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsmake=data.get('txtsMake') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            adminMakeList_AddNewOBJ =  Adminmakelist(smake =txtsmake, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            adminMakeList_AddNewOBJ.save()

            messages.success(request, 'Make is Added successfully!')
           
            return   redirect('adminMakeList')  
            

    else:               
        return render(request, "CloudCaliber/adminMakeListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminMakeListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminMakeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsmake=data.get('txtsMake') 

            adminMakeList_AddNewOBJ =  Adminmakelist.objects.get(lid=lID) 

            adminMakeList_AddNewOBJ.smake =txtsmake
            adminMakeList_AddNewOBJ.save()

            messages.success(request, 'Make is Updated successfully!')
            adminMakeList_list =  Adminmakelist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminMakeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminMakeList_list':  adminMakeList_list,  
                        }
                        )

    else: 
        adminMakeList_list =  Adminmakelist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminMakeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'adminMakeList_list':  adminMakeList_list,  
                        }
                        )












@csrf_exempt
def adminStorageLocationListDelete(request,lID):
    lCatID = 0
    
     
    
    Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.get(lid=lID).delete()    
    # Details.objects.filter(id=pk).delete()
    return   redirect('adminStorageLocationList') 







@csrf_exempt
def  adminStorageLocationList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminStorageLocationListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.order_by('sstoragelocation')     
                    return render(request,  'CloudCaliber/adminStorageLocationList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Adminstoragelocationlist_list':  Adminstoragelocationlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.filter(sstoragelocation__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminStorageLocationList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminstoragelocationlist_list':  Adminstoragelocationlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
            
            #Renders the contact page."""
        assert isinstance(request, HttpRequest)  
        Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.order_by('sstoragelocation')     
        return render(request,  'CloudCaliber/adminStorageLocationList.html', 
            {
                    'title':'User list', 
                    'sPlantName': sPlantName ,  
                    'semployeename':  semployeename, 
                    'message':'Your User list page.',
                    'year':datetime.now().year,  
                    'Adminstoragelocationlist_list':  Adminstoragelocationlist_list, 
                }
            ) 


 




 




@csrf_exempt
def adminStorageLocationListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminStorageLocationList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsStorage=data.get('txtsStorage') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Adminstoragelocationlist_AddNewOBJ =  Adminstoragelocationlist(sstoragelocation =txtsStorage, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid)
 
            Adminstoragelocationlist_AddNewOBJ.save()

            messages.success(request, 'Storage Location is Added successfully!')
           
            return   redirect('adminStorageLocationList')  
            

    else:               
        return render(request, "CloudCaliber/adminStorageLocationListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminStorageLocationListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminStorageLocationList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsStorage=data.get('txtsStorage') 

            Adminstoragelocationlist_AddNewOBJ =  Adminstoragelocationlist.objects.get(lid=lID) 

            Adminstoragelocationlist_AddNewOBJ.sstoragelocation =txtsStorage
            Adminstoragelocationlist_AddNewOBJ.save()

            messages.success(request, 'Storage location is Updated successfully!')
            Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminStorageLocationListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminstoragelocationlist_list':  Adminstoragelocationlist_list,  
                        }
                        )

    else: 
        Adminstoragelocationlist_list =  Adminstoragelocationlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminStorageLocationListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminstoragelocationlist_list':  Adminstoragelocationlist_list,  
                        }
                        )
















@csrf_exempt
def  adminPartDetailsListList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminPartDetailsListListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Adminpartdetailslist_list =  Adminpartdetailslist.objects.order_by('spartno')   
                    page_number  = request.GET.get('page')

                    lRecCount =0 
                    lRecCount = Adminpartdetailslist_list.count()
                    lRecCount1 = int((lRecCount * 10/100) )
                    if (lRecCount1 == 0):
                        lRecCount1 =1
                    paginator = Paginator(Adminpartdetailslist_list, lRecCount1)
                    try:
                        Adminpartdetailslist_lists = paginator.get_page(page_number )
                    except PageNotAnInteger:
                        Adminpartdetailslist_lists = paginator.page(1)
                    except EmptyPage:
                        Adminpartdetailslist_lists = paginator.page(paginator.num_pages)
                    
                    
                    return render(request,  'CloudCaliber/adminPartDetailsListList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminpartdetailslist_lists':  Adminpartdetailslist_lists, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Adminpartdetailslist_list =  Adminpartdetailslist.objects.filter(spartno__icontains=txtSearch)  | Adminpartdetailslist.objects.filter(spartname__icontains=txtSearch).values()
                    
                    page_number  = request.GET.get('page')

                    lRecCount =0 
                    lRecCount = Adminpartdetailslist_list.count()
                    lRecCount1 = int((lRecCount * 10/100) )
                    if (lRecCount1 == 0):
                        lRecCount1 =1

                    paginator = Paginator(Adminpartdetailslist_list, lRecCount1)
                    try:
                        Adminpartdetailslist_lists = paginator.get_page(page_number )
                    except PageNotAnInteger:
                        Adminpartdetailslist_lists = paginator.page(1)
                    except EmptyPage:
                        Adminpartdetailslist_lists = paginator.page(paginator.num_pages)
                    
                    
                    return render(request,  'CloudCaliber/adminPartDetailsListList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminpartdetailslist_lists':  Adminpartdetailslist_lists, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
            Adminpartdetailslist_list =  Adminpartdetailslist.objects.order_by('spartno')   
            
            page_number  = request.GET.get('page')

            lRecCount =0 
            lRecCount = Adminpartdetailslist_list.count()
            lRecCount1 = int((lRecCount * 10/100) )
            if (lRecCount1 == 0):
                lRecCount1 =1

            paginator = Paginator(Adminpartdetailslist_list, lRecCount1)
            try:
                Adminpartdetailslist_lists = paginator.get_page(page_number )
            except PageNotAnInteger:
                Adminpartdetailslist_lists = paginator.page(1)
            except EmptyPage:
                Adminpartdetailslist_lists = paginator.page(paginator.num_pages)
            
            
            return render(request,  'CloudCaliber/adminPartDetailsListList.html', 
            {
                'title':'User list', 
                'sPlantName': sPlantName ,  
                'semployeename':  semployeename,
                'message':'Your User list page.',
                'year':datetime.now().year,  
                'Adminpartdetailslist_lists':  Adminpartdetailslist_lists, 
            }
            )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminPartDetailsListListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminPartDetailsListList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsPartNo=data.get('txtsPartNo') 
            txtsPartName=data.get('txtsPartName') 
            txtCode=data.get('txtCode') 
            cmbCustomer=0 
            if 'cmbCustomer' in request.POST:
                cmbCustomer=request.POST['cmbCustomer'] 

            txtInterval=data.get('txtInterval') 
            cmbMSAPeriod=data.get('cmbMSAPeriod') 
            txtLast=data.get('txtLast') 
            #txtNext=data.get('txtNext') 
            txtNext=datetime.today()

            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Adminpartdetailslist_AddNewOBJ =  Adminpartdetailslist(spartno =txtsPartNo,  spartname =txtsPartName,  scode =txtCode, sprojectname ="", lcustomerid =cmbCustomer,  lintervalrnr =txtInterval,  sintervalperiodrnr =cmbMSAPeriod,  dlastrnr =txtLast,  dnextrnr =txtNext,  lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname,  lpantid  =0,    brnr   =0,    lalertinterval =0,    dtrnrdisplaydate  = datetime.today(),    smsasopfile ="",    ldueday  =0,    lduemonth  =0,    ldueyear =0,    ldueday1  =0,    lduemonth1  =0,    ldueyear1  =0,    ldueday2  =0,    lduemonth2  =0,    ldueyear2   =0,    ldueday3   =0,    lduemonth3   =0,    ldueyear3   =0,    ldueday4   =0,    lduemonth4   =0,    ldueyear4   =0,    ldueday5   =0,    lduemonth5   =0,    ldueyear5   =0,    ldueday6   =0,    lduemonth6  =0,     ldueyear6   =0,  bvisualinspection   =0,    lintervalrnr1  =0,sintervalperiodrnr1    ="",    dlastrnr1   = datetime.today(),    dnextrnr1   = datetime.today(),    lalertinterval1  =0,     dtrnrdisplaydate1   = datetime.today(),    bstability   =0,    lintervalrnr2   =0,    sintervalperiodrnr2    ="",    dlastrnr2   = datetime.today(),    dnextrnr2   = datetime.today(),    lalertinterval2  =0,    dtrnrdisplaydate2  = datetime.today(),     bbias  =0,    lintervalrnr3   =0,    sintervalperiodrnr3    ="",    dlastrnr3  = datetime.today(),    dnextrnr3  = datetime.today(),    lalertinterval3   =0,    dtrnrdisplaydate3   = datetime.today(),    blinearity   =0,lintervalrnr4  =0,sintervalperiodrnr4    ="",    dlastrnr4  = datetime.today(), dnextrnr4  = datetime.today(), lalertinterval4  =0,    dtrnrdisplaydate4  = datetime.today(),    battribute=0, lintervalrnr5=0, sintervalperiodrnr5  ="",    dlastrnr5  = datetime.today(),    dnextrnr5  = datetime.today(),    lalertinterval5 =0,    dtrnrdisplaydate5   = datetime.today(),    dcostofwork =0,    dnextrnrdisplay   = datetime.today(),    dnextrnralert  = datetime.today())
 
            Adminpartdetailslist_AddNewOBJ.save()

            messages.success(request, 'Part Details is Added successfully!')
           
            return   redirect('adminPartDetailsListList')  
            

    else:     
        
        Admincustomerlist_list =  Admincustomerlist.objects.order_by('scustomername')           
        return render(request, "CloudCaliber/adminPartDetailsListListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admincustomerlist_list': Admincustomerlist_list,
                        }
                        ) 

@csrf_exempt
def adminPartDetailsListListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminPartDetailsListList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsPartNo=data.get('txtsPartNo') 
            txtsPartName=data.get('txtsPartName') 
            txtCode=data.get('txtCode') 
            cmbCustomer=data.get('cmbCustomer') 
            txtInterval=data.get('txtInterval') 
            cmbMSAPeriod=data.get('cmbMSAPeriod') 
            txtLast=data.get('txtLast') 
            #txtNext=data.get('txtNext') 
            txtNext=datetime.today()

            Adminpartdetailslist_AddNewOBJ =  Adminpartdetailslist.objects.get(lid=lID) 

            Adminpartdetailslist_AddNewOBJ.spartno =txtsPartNo
            Adminpartdetailslist_AddNewOBJ.spartname =txtsPartName
            Adminpartdetailslist_AddNewOBJ.scode =txtCode
            Adminpartdetailslist_AddNewOBJ.lcustomerid =cmbCustomer
            Adminpartdetailslist_AddNewOBJ.lintervalrnr =txtInterval
            Adminpartdetailslist_AddNewOBJ.sintervalperiodrnr =cmbMSAPeriod
            Adminpartdetailslist_AddNewOBJ.dlastrnr =txtLast
            Adminpartdetailslist_AddNewOBJ.dnextrnr =txtNext 
            Adminpartdetailslist_AddNewOBJ.save()

            messages.success(request, 'Part Details is Updated successfully!')
            Adminpartdetailslist_list =  Adminpartdetailslist.objects.get(lid=lID)             
            Admincustomerlist_list =  Admincustomerlist.objects.order_by('scustomername')    
            return render(request, "CloudCaliber/adminPartDetailsListListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminpartdetailslist_list':  Adminpartdetailslist_list,  
                            'Admincustomerlist_list': Admincustomerlist_list,  
                        }
                        )

    else: 
        Adminpartdetailslist_list =  Adminpartdetailslist.objects.get(lid=lID)          
        Admincustomerlist_list =  Admincustomerlist.objects.order_by('scustomername')             
        return render(request, "CloudCaliber/adminPartDetailsListListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminpartdetailslist_list':  Adminpartdetailslist_list,
                            'Admincustomerlist_list': Admincustomerlist_list,    
                        }
                        )




@csrf_exempt
def  adminInstrumentOperationList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminInstrumentOperationListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admininstrumentoperationlist_list =  Admininstrumentoperationlist.objects.order_by('soperation')     
                    return render(request,  'CloudCaliber/adminInstrumentOperationList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admininstrumentoperationlist_list':  Admininstrumentoperationlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admininstrumentoperationlist_list =  Admininstrumentoperationlist.objects.filter(soperation__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminInstrumentOperationList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admininstrumentoperationlist_list':  Admininstrumentoperationlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admininstrumentoperationlist_list =  Admininstrumentoperationlist.objects.order_by('soperation')     
            return render(request,  'CloudCaliber/adminInstrumentOperationList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admininstrumentoperationlist_list':  Admininstrumentoperationlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminInstrumentOperationListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminInstrumentOperationList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsOperation=data.get('txtsOperation') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']
            txtsOperationscode=data.get('txtsOperationscode') 

            Admininstrumentoperationlist_AddNewOBJ =  Admininstrumentoperationlist(soperation =txtsOperation, scode = txtsOperationscode, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            Admininstrumentoperationlist_AddNewOBJ.save()

            messages.success(request, 'Operation is Added successfully!')
           
            return   redirect('adminInstrumentOperationList')  
            

    else:               
        return render(request, "CloudCaliber/adminInstrumentOperationListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminInstrumentOperationListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminInstrumentOperationList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsOperation=data.get('txtsOperation') 
            txtsOperationscode=data.get('txtsOperationscode') 

            Admininstrumentoperationlist_AddNewOBJ =  Admininstrumentoperationlist.objects.get(lid=lID) 

            Admininstrumentoperationlist_AddNewOBJ.scode =txtsOperationscode
            Admininstrumentoperationlist_AddNewOBJ.soperation =txtsOperation
            Admininstrumentoperationlist_AddNewOBJ.save()

            messages.success(request, 'Operation is Updated successfully!')
            Admininstrumentoperationlist_list =  Admininstrumentoperationlist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminInstrumentOperationListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admininstrumentoperationlist_list':  Admininstrumentoperationlist_list,  
                        }
                        )

    else: 
        Admininstrumentoperationlist_list =  Admininstrumentoperationlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminInstrumentOperationListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admininstrumentoperationlist_list':  Admininstrumentoperationlist_list,  
                        }
                        )





@csrf_exempt
def  AdminRangeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminRangeListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    AdminRangeList_list =  Adminrangelist.objects.order_by('srange')     
                    return render(request,  'CloudCaliber/AdminRangeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'AdminRangeList_list':  AdminRangeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    AdminRangeList_list =  Adminrangelist.objects.filter(srange__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/AdminRangeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminRangeList_list':  AdminRangeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            AdminRangeList_list =  Adminrangelist.objects.order_by('srange')     
            return render(request,  'CloudCaliber/AdminRangeList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminRangeList_list':  AdminRangeList_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def AdminRangeListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('AdminRangeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsrange=data.get('txtsrange') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']
            txtsrangescode=data.get('txtsrangescode') 

            AdminRangeList_AddNewOBJ =  Adminrangelist(srange =txtsrange, scode = txtsrangescode , lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            AdminRangeList_AddNewOBJ.save()

            messages.success(request, 'Range is Added successfully!')
           
            return   redirect('AdminRangeList')  
            

    else:               
        return render(request, "CloudCaliber/AdminRangeListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def AdminRangeListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('AdminRangeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsrange=data.get('txtsrange') 
            txtsrangescode=data.get('txtsrangescode') 

            AdminRangeList_AddNewOBJ =  Adminrangelist.objects.get(lid=lID) 

            AdminRangeList_AddNewOBJ.scode =txtsrangescode
            AdminRangeList_AddNewOBJ.srange =txtsrange
            AdminRangeList_AddNewOBJ.save()

            messages.success(request, 'Range is Updated successfully!')
            AdminRangeList_list =  Adminrangelist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/AdminRangeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminRangeList_list':  AdminRangeList_list,  
                        }
                        )

    else: 
        AdminRangeList_list =  Adminrangelist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/AdminRangeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminRangeList_list':  AdminRangeList_list,  
                        }
                        )









@csrf_exempt
def  AdminInstrumentTypeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminInstrumentTypeListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    AdminInstrumentTypeList_list =  Admininstrumenttypelist.objects.order_by('sinstrumenttype')     
                    return render(request,  'CloudCaliber/AdminInstrumentTypeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'AdminInstrumentTypeList_list':  AdminInstrumentTypeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    AdminInstrumentTypeList_list =  AdminInstrumentTypeList.objects.filter(sinstrumenttype__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/AdminInstrumentTypeList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminInstrumentTypeList_list':  AdminInstrumentTypeList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            AdminInstrumentTypeList_list =  Admininstrumenttypelist.objects.order_by('sinstrumenttype')     
            return render(request,  'CloudCaliber/AdminInstrumentTypeList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminInstrumentTypeList_list':  AdminInstrumentTypeList_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def AdminInstrumentTypeListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('AdminInstrumentTypeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsinstrumenttype=data.get('txtsinstrumenttype') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']
            txtsinstrumenttypescode=data.get('txtsinstrumenttypescode') 

            AdminInstrumentTypeList_AddNewOBJ =  Admininstrumenttypelist(sinstrumenttype =txtsinstrumenttype, scode = txtsinstrumenttypescode, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname )
 
            AdminInstrumentTypeList_AddNewOBJ.save()

            messages.success(request, 'Instrument Type is Added successfully!')
           
            return   redirect('AdminInstrumentTypeList')  
            

    else:               
        return render(request, "CloudCaliber/AdminInstrumentTypeListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def AdminInstrumentTypeListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('AdminInstrumentTypeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsinstrumenttype=data.get('txtsinstrumenttype') 
            txtsinstrumenttypescode=data.get('txtsinstrumenttypescode') 

            AdminInstrumentTypeList_AddNewOBJ =  Admininstrumenttypelist.objects.get(lid=lID) 

            AdminInstrumentTypeList_AddNewOBJ.scode =txtsinstrumenttypescode
            AdminInstrumentTypeList_AddNewOBJ.sinstrumenttype =txtsinstrumenttype
            AdminInstrumentTypeList_AddNewOBJ.save()

            messages.success(request, 'Instrument Type is Updated successfully!')
            AdminInstrumentTypeList_list =  Admininstrumenttypelist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/AdminInstrumentTypeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminInstrumentTypeList_list':  AdminInstrumentTypeList_list,  
                        }
                        )

    else: 
        AdminInstrumentTypeList_list =  Admininstrumenttypelist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/AdminInstrumentTypeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminInstrumentTypeList_list':  AdminInstrumentTypeList_list,  
                        }
                        )



 


@csrf_exempt
def  AdminEquipmentList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdminEquipmentListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    AdminEquipmentList_list =  Adminequipmentlist.objects.order_by('sequipmentname')     
                    return render(request,  'CloudCaliber/AdminEquipmentList.html', 
                    {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'AdminEquipmentList_list':  AdminEquipmentList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    AdminEquipmentList_list =  Adminequipmentlist.objects.filter(sequipmentname__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/AdminEquipmentList.html', 
                    {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminEquipmentList_list':  AdminEquipmentList_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            AdminEquipmentList_list =  Adminequipmentlist.objects.order_by('sequipmentname')     
            return render(request,  'CloudCaliber/AdminEquipmentList.html', 
                {
                        'title':'User list', 
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'AdminEquipmentList_list':  AdminEquipmentList_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def AdminEquipmentListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('AdminEquipmentList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsequipmentname=data.get('txtsEquipment') 
            txtsequipmentnamescode=data.get('txtsEquipmentscode') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno'] 

            AdminEquipmentList_AddNewOBJ =  Adminequipmentlist(sequipmentname =txtsequipmentname, scode = txtsequipmentnamescode, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname )
 
            AdminEquipmentList_AddNewOBJ.save()

            messages.success(request, 'Equipment is Added successfully!')
           
            return   redirect('AdminEquipmentList')  
            

    else:               
        return render(request, "CloudCaliber/AdminEquipmentListAdd.html",
                        {
                            'title':'User list', 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 


@csrf_exempt
def AdminEquipmentLisDelete(request,lID):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    AdminEquipmentList_list =  Adminequipmentlist.objects.get(lid=lID).delete()    
    # Details.objects.filter(id=pk).delete()
    return AdminEquipmentList(request) 




@csrf_exempt
def AdminEquipmentListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('AdminEquipmentList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsequipmentname=data.get('txtsEquipment') 
            txtsequipmentnamescode=data.get('txtsEquipmentscode') 

            AdminEquipmentList_AddNewOBJ =  Adminequipmentlist.objects.get(lid=lID) 

            AdminEquipmentList_AddNewOBJ.scode =txtsequipmentnamescode
            AdminEquipmentList_AddNewOBJ.sequipmentname =txtsequipmentname
            AdminEquipmentList_AddNewOBJ.save()

            messages.success(request, 'Equipment is Updated successfully!')
            AdminEquipmentList_list =  Adminequipmentlist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/AdminEquipmentListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminEquipmentList_list':  AdminEquipmentList_list,  
                        }
                        )

    else: 
        AdminEquipmentList_list =  Adminequipmentlist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/AdminEquipmentListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'AdminEquipmentList_list':  AdminEquipmentList_list,  
                        }
                        )






@csrf_exempt
def  adminInstrumentMaterialList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminInstrumentMaterialListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admininstrumentmateriallist_list =  Admininstrumentmateriallist.objects.order_by('smaterial')     
                    return render(request,  'CloudCaliber/adminInstrumentMaterialList.html', 
                    {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admininstrumentmateriallist_list':  Admininstrumentmateriallist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admininstrumentmateriallist_list =  Admininstrumentmateriallist.objects.filter(smaterial__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminInstrumentMaterialList.html', 
                    {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admininstrumentmateriallist_list':  Admininstrumentmateriallist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admininstrumentmateriallist_list =  Admininstrumentmateriallist.objects.order_by('smaterial')     
            return render(request,  'CloudCaliber/adminInstrumentMaterialList.html', 
                {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        'title':'User list', 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admininstrumentmateriallist_list':  Admininstrumentmateriallist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminInstrumentMaterialListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminInstrumentMaterialList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsMaterial=data.get('txtsMaterial') 
            txtsMaterialCode=data.get('txtsMaterialCode') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Admininstrumentmateriallist_AddNewOBJ =  Admininstrumentmateriallist(smaterial =txtsMaterial, scode =txtsMaterialCode, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            Admininstrumentmateriallist_AddNewOBJ.save()

            messages.success(request, 'Material is Added successfully!')
           
            return   redirect('adminInstrumentMaterialList')  
            

    else:               
        return render(request, "CloudCaliber/adminInstrumentMaterialListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminInstrumentMaterialListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminInstrumentMaterialList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsMaterial=data.get('txtsMaterial') 
            txtsMaterialCode=data.get('txtsMaterialCode') 

            Admininstrumentmateriallist_AddNewOBJ =  Admininstrumentmateriallist.objects.get(lid=lID) 

            Admininstrumentmateriallist_AddNewOBJ.smaterial =txtsMaterial
            Admininstrumentmateriallist_AddNewOBJ.scode =txtsMaterialCode
            Admininstrumentmateriallist_AddNewOBJ.save()

            messages.success(request, 'Material is Updated successfully!')
            Admininstrumentmateriallist_list =  Admininstrumentmateriallist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/adminInstrumentMaterialListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admininstrumentmateriallist_list':  Admininstrumentmateriallist_list,  
                        }
                        )

    else: 
        Admininstrumentmateriallist_list =  Admininstrumentmateriallist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/adminInstrumentMaterialListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admininstrumentmateriallist_list':  Admininstrumentmateriallist_list,  
                        }
                        )














@csrf_exempt
def  adminAssetTypeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('adminAssetTypeListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')     
                    return render(request,  'CloudCaliber/adminAssetTypeList.html', 
                    {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Adminassettypelist_list':  Adminassettypelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Adminassettypelist_list =  Adminassetcategorytypelist.objects.filter(scategorytype__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminAssetTypeList.html', 
                    {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminassettypelist_list':  Adminassettypelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')     
            return render(request,  'CloudCaliber/adminAssetTypeList.html', 
                {
                        'sPlantName': sPlantName ,  
                        'semployeename':  semployeename,
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Adminassettypelist_list':  Adminassettypelist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def adminAssetTypeListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('adminAssetTypeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtassettype=data.get('txtsAssetType') 
            scode = data.get('txtsAssetCode') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Adminassettypelist_AddNewOBJ =  Adminassetcategorytypelist(scategorytype =txtassettype, scode =scode, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname, lcategorytype1 = 0,     lcategorytype2 = 0,      lcode1 =  0,     lcode2 = 0,     styperefname =  "",     btyperefasstring =  0,     btyperefasint = 0,     btyperefasrange =  0,     btyperefascontinuousnoa =  0,     btyperefascontinuousnob =  0,     lcontinuousnoa =  0,     lcontinuousnob =  0,     bpartno =  0,     bequipment =  0,     bmachine =  0,     brange2variable =  0,     brange3variable =  0,     bmaterial =  0,     boperation =  0,    bcontinuousno =  0,     btype =  0,     btype1 = 0,     btype2 =  0,    btype3 =  0,     btype4 = 0,     btype5 =  0,     btype6 = 0,     lcode =  0,     lcode3 = 0,     lcode4 = 0,     lcode5 = 0,     stitle =  "",     stitle1 =  "",     stitle2 =  "",     stitle3 =  "",     stitle4 =  "",     stitle5  =  "")
 
            Adminassettypelist_AddNewOBJ.save()

            messages.success(request, 'Asset Classification is Added successfully!')
           
            return   redirect('adminAssetTypeList')  
            

    else:               
        return render(request, "CloudCaliber/adminAssetTypeListAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def adminAssetTypeListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('adminAssetTypeList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST 

            Adminassettypelist_AddNewOBJ =  Adminassetcategorytypelist.objects.get(lcategorytypeid=lID) 

            txtassettype=data.get('txtsAssetType') 
            scode = data.get('txtsAssetCode') 
            Adminassettypelist_AddNewOBJ.scategorytype =txtassettype
            Adminassettypelist_AddNewOBJ.scode =scode
            Adminassettypelist_AddNewOBJ.save()

            messages.success(request, 'Asset Classification is Updated successfully!')
            Adminassettypelist_list =  Adminassetcategorytypelist.objects.get(lcategorytypeid=lID)              
            return render(request, "CloudCaliber/adminAssetTypeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminassettypelist_list':  Adminassettypelist_list,  
                        }
                        )

    else: 
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.get(lcategorytypeid=lID)              
        return render(request, "CloudCaliber/adminAssetTypeListDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Adminassettypelist_list':  Adminassettypelist_list,  
                        }
                        )





@csrf_exempt
def  MasterInstrumentsList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('MasterInstrumentsListAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.order_by('smake')     
                    return render(request,  'CloudCaliber/Masterinstrumentslist.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Masterinstrumentslist_list':  Masterinstrumentslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Masterinstrumentslist_list =  Masterinstrumentslist.objects.filter(smake__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/Masterinstrumentslist.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Masterinstrumentslist_list':  Masterinstrumentslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.order_by('smake')     
            return render(request,  'CloudCaliber/Masterinstrumentslist.html', 
                {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Masterinstrumentslist_list':  Masterinstrumentslist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')


 




 




@csrf_exempt
def MasterInstrumentsListAdd(request):
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('MasterInstrumentsList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsmake=data.get('txtsMake') 
            lcompanyid = request.session['lcompanyid']
            scompantname = request.session['scompantname']
            lplantid=request.session['lunitid']
            splantname=request.session['sunitno']

            Masterinstrumentslist_AddNewOBJ =  Masterinstrumentslist(smake =txtsmake, lcompanyid=lcompanyid, scompantname=scompantname, lplantid=lplantid, splantname=splantname)
 
            Masterinstrumentslist_AddNewOBJ.save()

            messages.success(request, 'Instrument / Gauge is Added successfully!')
           
            return   redirect('MasterInstrumentsList')  
            

    else:               
        return render(request, "CloudCaliber/MasterInstrumentsListAdd.html",
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

@csrf_exempt
def MasterInstrumentsListDetails(request,lID):
    
    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('MasterInstrumentsList')  
            
        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsmake=data.get('txtsMake') 

            Masterinstrumentslist_AddNewOBJ =  Masterinstrumentslist.objects.get(lid=lID) 

            Masterinstrumentslist_AddNewOBJ.smake =txtsmake
            Masterinstrumentslist_AddNewOBJ.save()

            messages.success(request, 'Instrument / Gauge is Updated successfully!')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(lid=lID)              
            return render(request, "CloudCaliber/MasterInstrumentsListDetails.html",
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Masterinstrumentslist_list':  Masterinstrumentslist_list,  
                        }
                        )

    else: 
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.get(lid=lID)              
        return render(request, "CloudCaliber/MasterInstrumentsListDetails.html",
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Masterinstrumentslist_list':  Masterinstrumentslist_list,  
                        }
                        )












 
 



 




