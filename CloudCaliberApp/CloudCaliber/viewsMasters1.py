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
def AdminAdmintoleranceclasslist(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbAdd' in request.POST:  
            
            return   redirect('AdmintoleranceclasslistAdd')  

        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)   
                    Admintoleranceclasslist_list = Admintoleranceclasslist.objects.order_by('stoleranceclass').values()     
                    return render(request,  'CloudCaliber/Admintoleranceclasslist.html', 
                    {
                        'title':request.session['sunitno'], 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintoleranceclasslist_list': Admintoleranceclasslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    lunitidA=request.session['lunitid']  
                    Admintoleranceclasslist_list = Admintoleranceclasslist.objects.filter(stoleranceclass__icontains=txtSearch).order_by('stoleranceclass').values() 
                    return render(request,  'CloudCaliber/Admintoleranceclasslist.html', 
                    {
                        'title':request.session['sunitno'], 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceclasslist_list': Admintoleranceclasslist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:     
        request.session['lToleranceClassId'] =0   
        request.session['txtToleranceClass'] = ""
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)   
            lunitidA=request.session['lunitid']  
            Admintoleranceclasslist_list = Admintoleranceclasslist.objects.order_by('stoleranceclass').values()     
            return render(request,  'CloudCaliber/Admintoleranceclasslist.html', 
                    {
                        'title':request.session['sunitno'], 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintoleranceclasslist_list': Admintoleranceclasslist_list, 
                    }
                    )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')

 




@csrf_exempt
def AdmintoleranceclasslistAdd(request):

    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  
                         
            return   redirect('AdminAdmintoleranceclasslist')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtToleranceClass=data.get('txtToleranceClass') 
            
            lToleranceClassId=request.session['lToleranceClassId']
            if (lToleranceClassId ==0):
                Admintoleranceclasslist_AddNewOBJ = Admintoleranceclasslist(stoleranceclass =txtToleranceClass)
                Admintoleranceclasslist_AddNewOBJ.save()

                request.session['txtToleranceClass'] = txtToleranceClass
                request.session['lToleranceClassId']  = Admintoleranceclasslist_AddNewOBJ.lid
            
                messages.success(request, 'Tolerance Class is Added successfully!') 
            lunitidA=request.session['lunitid']  
                 
            lToleranceClassId=request.session['lToleranceClassId']  
            Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                            
            return render(request, "CloudCaliber/AdmintoleranceclasslistAdd.html",
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'txtToleranceClass':request.session['txtToleranceClass'], 
                                'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                            }
                            ) 



        if 'cmbSaveValues' in request.POST:  

            txtToleranceClass = request.session['txtToleranceClass'] 
            lToleranceClassId = request.session['lToleranceClassId'] 
            data = request.POST
            txtFrom=data.get('txtFrom') 
            txtTo=data.get('txtTo') 
            txtMin=data.get('txtMin') 
            txtMax=data.get('txtMax') 

            

            if (lToleranceClassId !=0):
               Admintoleranceclasschartlist_AddNewOBJ = Admintoleranceclasschartlist(stoleranceclass=txtToleranceClass, dbasicsizemin=txtFrom, dbasicsizemax=txtTo, dtolmax=txtMax, dtolmin=txtMin, ltoneranceclassid=lToleranceClassId)
               Admintoleranceclasschartlist_AddNewOBJ.save()

            lToleranceClassId=request.session['lToleranceClassId']  
            Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                            
            return render(request, "CloudCaliber/AdmintoleranceclasslistAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'txtToleranceClass':request.session['txtToleranceClass'], 
                            'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                        }
                        ) 


    else:          
        lToleranceClassId=request.session['lToleranceClassId']  
        Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                          
        return render(request, "CloudCaliber/AdmintoleranceclasslistAdd.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'txtToleranceClass':request.session['txtToleranceClass'], 
                            'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                        }
                        ) 

@csrf_exempt
def AdmintoleranceclasslistDetails(request,lID):
    
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  
                         
            return   redirect('AdminAdmintoleranceclasslist')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtToleranceClass=data.get('txtToleranceClass') 
            
            lToleranceClassId=request.session['lToleranceClassId']
            if (lToleranceClassId !=0):
                Admintoleranceclasslist_AddNewOBJ = Admintoleranceclasslist.objects.get(lid=lID)
                Admintoleranceclasslist_AddNewOBJ.stoleranceclass = txtToleranceClass
                Admintoleranceclasslist_AddNewOBJ.save()

            request.session['txtToleranceClass'] = txtToleranceClass
            request.session['lToleranceClassId']  =lID
            
            messages.success(request, 'Tolerance Class is Updated successfully!') 
            lunitidA=request.session['lunitid']  
                 
            lToleranceClassId=request.session['lToleranceClassId'] 
            Admintoleranceclasslist_list = Admintoleranceclasslist.objects.get(lid=lToleranceClassId)   
            Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                            
            return render(request, "CloudCaliber/AdmintoleranceclasslistDetails.html",
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'txtToleranceClass':request.session['txtToleranceClass'], 
                                'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                                'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                            }
                            ) 



        if 'cmbSaveValues' in request.POST:  

            txtToleranceClass = request.session['txtToleranceClass'] 
            lToleranceClassId = request.session['lToleranceClassId'] 
            data = request.POST
            txtFrom=data.get('txtFrom') 
            txtTo=data.get('txtTo') 
            txtMin=data.get('txtMin') 
            txtMax=data.get('txtMax') 

            

            if (lToleranceClassId !=0):
               Admintoleranceclasschartlist_AddNewOBJ = Admintoleranceclasschartlist(stoleranceclass=txtToleranceClass, dbasicsizemin=txtFrom, dbasicsizemax=txtTo, dtolmax=txtMax, dtolmin=txtMin, ltoneranceclassid=lToleranceClassId)
               Admintoleranceclasschartlist_AddNewOBJ.save()

            lToleranceClassId=request.session['lToleranceClassId']  
            Admintoleranceclasslist_list = Admintoleranceclasslist.objects.get(lid=lToleranceClassId)  
            Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                            
            return render(request, "CloudCaliber/AdmintoleranceclasslistDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'txtToleranceClass':request.session['txtToleranceClass'], 
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                        }
                        ) 


    else: 
        request.session['lToleranceClassId'] = lID         
        lToleranceClassId=request.session['lToleranceClassId'] 
        Admintoleranceclasslist_list = Admintoleranceclasslist.objects.get(lid=lID)   
        Admintoleranceclasschartlist_list = Admintoleranceclasschartlist.objects.filter(ltoneranceclassid=lToleranceClassId).order_by('lid').values()     
                          
        return render(request, "CloudCaliber/AdmintoleranceclasslistDetails.html",
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'txtToleranceClass':request.session['txtToleranceClass'], 
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'Admintoleranceclasschartlist_list':Admintoleranceclasschartlist_list,  
                        }
                        ) 






@csrf_exempt
def adminCalibConditionsList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    lConditionId =0
    request.session['lConditionId'] =0

    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



        if 'cmbCloseAdd' in request.POST:  

             
            return   redirect('AdminMasterlistDashboard')  
            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0  


                    
                    if (lConditionId==0):
                        if 'txtTemperature' in request.POST:
                            txtTemperature=request.POST['txtTemperature'] 
                        if 'txtHumidity' in request.POST:
                            txtHumidity=request.POST['txtHumidity']  
            

                        Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist(stemperature=txtTemperature, shumidity=txtHumidity)
                        Admincalibconditionslist_AddNewOBJ.save()


                    else:
                        if 'txtTemperature' in request.POST:
                            txtTemperature=request.POST['txtTemperature'] 
                        if 'txtHumidity' in request.POST:
                            txtHumidity=request.POST['txtHumidity']  
                        
                        
                        lConditionId = request.session['lConditionId']

                        Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist.objects.get(lid=lConditionId) 

                        Admincalibconditionslist_AddNewOBJ.stemperature=txtTemperature
                        Admincalibconditionslist_AddNewOBJ.shumidity=txtHumidity 
                        Admincalibconditionslist_AddNewOBJ.save()

                    messages.success(request, 'Room Climatic Default Condition is updated successfully!')

                    assert isinstance(request, HttpRequest) 
                    Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
                    lConditionId =0    
                    if(Admincalibconditionslist_list1):
                        lConditionId =0
                        for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                            if(lConditionId ==0 ):
                                lConditionId = Admincalibconditionslist_listOBJ.lid
                    
                    
                    request.session['lConditionId'] =lConditionId
                    Admincalibconditionslist_list = Admincalibconditionslist.objects.get(lid=lConditionId)  
                    return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                            }
                        )
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        
                        Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
                        lConditionId =0    
                        if(Admincalibconditionslist_list1):
                            lConditionId =0
                            for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                                if(lConditionId ==0 ):
                                    lConditionId = Admincalibconditionslist_listOBJ.lid
                        
                        
                        request.session['lConditionId'] =lConditionId
                        Admincalibconditionslist_list = Admincalibconditionslist.objects.filter(stemperature__icontains=txtSearch).values()
                        
                        return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                            }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0  


                
                if (lConditionId==0):
                    if 'txtTemperature' in request.POST:
                        txtTemperature=request.POST['txtTemperature'] 
                    if 'txtHumidity' in request.POST:
                        txtHumidity=request.POST['txtHumidity']  
        

                    Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist(stemperature=txtTemperature, shumidity=txtHumidity)
                    Admincalibconditionslist_AddNewOBJ.save()


                else:
                    if 'txtTemperature' in request.POST:
                        txtTemperature=request.POST['txtTemperature'] 
                    if 'txtHumidity' in request.POST:
                        txtHumidity=request.POST['txtHumidity']  
                    
                    
                    lConditionId = request.session['lConditionId']

                    Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist.objects.get(lid=lConditionId) 

                    Admincalibconditionslist_AddNewOBJ.stemperature=txtTemperature
                    Admincalibconditionslist_AddNewOBJ.shumidity=txtHumidity 
                    Admincalibconditionslist_AddNewOBJ.save()


                messages.success(request, 'Room Climatic Default Condition is updated successfully!')

                assert isinstance(request, HttpRequest) 
                Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
                lConditionId =0    
                if(Admincalibconditionslist_list1):
                    lConditionId =0
                    for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                        if(lConditionId ==0 ):
                            lConditionId = Admincalibconditionslist_listOBJ.lid
                    
                    
                request.session['lConditionId'] =lConditionId
                Admincalibconditionslist_list = Admincalibconditionslist.objects.get(lid=lConditionId)  
                return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                            }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
                    lConditionId =0    
                    if(Admincalibconditionslist_list1):
                        lConditionId =0
                        for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                            if(lConditionId ==0 ):
                                lConditionId = Admincalibconditionslist_listOBJ.lid
                    
                    if 'txtTemperature' in request.POST:
                        txtTemperature=request.POST['txtTemperature'] 
                    if 'txtHumidity' in request.POST:
                        txtHumidity=request.POST['txtHumidity']  
                    
                     

                    Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist.objects.get(lid=lConditionId) 

                    Admincalibconditionslist_AddNewOBJ.stemperature=txtTemperature
                    Admincalibconditionslist_AddNewOBJ.shumidity=txtHumidity 
                    Admincalibconditionslist_AddNewOBJ.save()
                    
                    messages.success(request, 'Room Climatic Default Condition is updated successfully!')
                    request.session['lConditionId'] =lConditionId
                    Admincalibconditionslist_list = Admincalibconditionslist.objects.get(lid=lConditionId)  
                    return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                            }
                        )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 

                    Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
                    lConditionId =0    
                    if(Admincalibconditionslist_list1):
                        lConditionId =0
                        for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                            if(lConditionId ==0 ):
                                lConditionId = Admincalibconditionslist_listOBJ.lid
                    
                    
                    request.session['lConditionId'] =lConditionId
                    Admincalibconditionslist_list = Admincalibconditionslist.objects.filter(stemperature__icontains=txtSearch).values()
                      
                    return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                            }
                        )
                    
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admincalibconditionslist_list1 = Admincalibconditionslist.objects.order_by('stemperature') 
            lConditionId =0    
            if(Admincalibconditionslist_list1):
                lConditionId =0
                for Admincalibconditionslist_listOBJ in Admincalibconditionslist_list1:
                    if(lConditionId ==0 ):
                        lConditionId = Admincalibconditionslist_listOBJ.lid
            
            
            if (lConditionId==0):
                txtTemperature=0 
                txtHumidity=0 
                if 'txtTemperature' in request.POST:
                    txtTemperature=0 
                if 'txtHumidity' in request.POST:
                    txtHumidity=0 
        

                Admincalibconditionslist_AddNewOBJ = Admincalibconditionslist(stemperature=txtTemperature, shumidity=txtHumidity)
                Admincalibconditionslist_AddNewOBJ.save()
                lConditionId = Admincalibconditionslist_AddNewOBJ.lid


            request.session['lConditionId'] =lConditionId
            Admincalibconditionslist_list = Admincalibconditionslist.objects.get(lid=lConditionId)  
            return render(request,  'CloudCaliber/adminCalibConditionsList.html', 
                {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admincalibconditionslist_list': Admincalibconditionslist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')



            


@csrf_exempt
def adminToleranceDialGaugeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0 
                    txtdrangeto = 0 
                    txtdtolerance1 = 0
                    txtdtolerance2 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 
                        
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom'] 
                        if(str(txtdrangefrom).isnumeric()):
                            txtdrangefrom = txtdrangefrom
                        else:
                            txtdrangefrom=0 

                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                        if(str(txtdrangeto).isnumeric()):
                            txtdrangeto = txtdrangeto
                        else:
                            txtdrangeto=0 
                            
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                        if(str(txtdtolerance1).isnumeric()):
                            txtdtolerance1 = txtdtolerance1
                        else:
                            txtdtolerance1=0 
                            
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']
                        if(str(txtdtolerance2).isnumeric()):
                            txtdtolerance2 = txtdtolerance2
                        else:
                            txtdtolerance2=0 
                              
        

                    Adminunitlist_AddNewOBJ = Admintolerancedialgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2, dtolerance3=0  )
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')

                    assert isinstance(request, HttpRequest)  
                    Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                            {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                            }
                            )
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0 
                txtdrangeto = 0 
                txtdtolerance1 = 0
                txtdtolerance2 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom']  
                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2'] 

                    
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom'] 
                    if(str(txtdrangefrom).isnumeric()):
                        txtdrangefrom = txtdrangefrom
                    else:
                        txtdrangefrom=0 

                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                    if(str(txtdrangeto).isnumeric()):
                        txtdrangeto = txtdrangeto
                    else:
                        txtdrangeto=0 
                        
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                    if(str(txtdtolerance1).isnumeric()):
                        txtdtolerance1 = txtdtolerance1
                    else:
                        txtdtolerance1=0 
                        
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']
                    if(str(txtdtolerance2).isnumeric()):
                        txtdtolerance2 = txtdtolerance2
                    else:
                        txtdtolerance2=0  
    

                Adminunitlist_AddNewOBJ = Admintolerancedialgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2, dtolerance3=0  )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')

                assert isinstance(request, HttpRequest)  
                Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.order_by('stoleranceclass')     
                return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                        }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintolerancedialgaugelist_list = Admintolerancedialgaugelist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminToleranceDialGaugeList.html', 
                {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancedialgaugelist_list': Admintolerancedialgaugelist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')





            


@csrf_exempt
def adminTolerancePressureGaugeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0 
                    txtdrangeto = 0 
                    txtdtolerance1 = 0
                    txtdtolerance2 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom']  
                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']  
        
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom'] 
                        if(str(txtdrangefrom).isnumeric()):
                            txtdrangefrom = txtdrangefrom
                        else:
                            txtdrangefrom=0 

                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                        if(str(txtdrangeto).isnumeric()):
                            txtdrangeto = txtdrangeto
                        else:
                            txtdrangeto=0 
                            
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                        if(str(txtdtolerance1).isnumeric()):
                            txtdtolerance1 = txtdtolerance1
                        else:
                            txtdtolerance1=0 
                            
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']
                        if(str(txtdtolerance2).isnumeric()):
                            txtdtolerance2 = txtdtolerance2
                        else:
                            txtdtolerance2=0 

                    Adminunitlist_AddNewOBJ = Admintolerancepressuregaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')

                    assert isinstance(request, HttpRequest)  
                    Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                            {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                            }
                            ) 
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0 
                txtdrangeto = 0 
                txtdtolerance1 = 0
                txtdtolerance2 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom']  
                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']  

                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom'] 
                    if(str(txtdrangefrom).isnumeric()):
                        txtdrangefrom = txtdrangefrom
                    else:
                        txtdrangefrom=0 

                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                    if(str(txtdrangeto).isnumeric()):
                        txtdrangeto = txtdrangeto
                    else:
                        txtdrangeto=0 
                        
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                    if(str(txtdtolerance1).isnumeric()):
                        txtdtolerance1 = txtdtolerance1
                    else:
                        txtdtolerance1=0 
                        
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']
                    if(str(txtdtolerance2).isnumeric()):
                        txtdtolerance2 = txtdtolerance2
                    else:
                        txtdtolerance2=0 

                Adminunitlist_AddNewOBJ = Admintolerancepressuregaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')

                assert isinstance(request, HttpRequest)  
                Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.order_by('stoleranceclass')     
                return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                        }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintolerancepressuregaugelist_list = Admintolerancepressuregaugelist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminTolerancePressureGaugeList.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancepressuregaugelist_list': Admintolerancepressuregaugelist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')



 
@csrf_exempt
def adminToleranceRadiusGaugeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0 
                    txtdrangeto = 0 
                    txtdtolerance1 = 0
                    txtdtolerance2 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom']  
                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']  
        
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom'] 
                        if(str(txtdrangefrom).isnumeric()):
                            txtdrangefrom = txtdrangefrom
                        else:
                            txtdrangefrom=0 

                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                        if(str(txtdrangeto).isnumeric()):
                            txtdrangeto = txtdrangeto
                        else:
                            txtdrangeto=0 
                            
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                        if(str(txtdtolerance1).isnumeric()):
                            txtdtolerance1 = txtdtolerance1
                        else:
                            txtdtolerance1=0 
                            
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']
                        if(str(txtdtolerance2).isnumeric()):
                            txtdtolerance2 = txtdtolerance2
                        else:
                            txtdtolerance2=0 

                    Adminunitlist_AddNewOBJ = Admintoleranceradiusgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2  , dtolerance3=0)
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')

                    assert isinstance(request, HttpRequest)  
                    Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                            }
                            ) 
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0 
                txtdrangeto = 0 
                txtdtolerance1 = 0
                txtdtolerance2 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom']  
                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']  

                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom'] 
                    if(str(txtdrangefrom).isnumeric()):
                        txtdrangefrom = txtdrangefrom
                    else:
                        txtdrangefrom=0 

                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                    if(str(txtdrangeto).isnumeric()):
                        txtdrangeto = txtdrangeto
                    else:
                        txtdrangeto=0 
                        
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                    if(str(txtdtolerance1).isnumeric()):
                        txtdtolerance1 = txtdtolerance1
                    else:
                        txtdtolerance1=0 
                        
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']
                    if(str(txtdtolerance2).isnumeric()):
                        txtdtolerance2 = txtdtolerance2
                    else:
                        txtdtolerance2=0 

                Adminunitlist_AddNewOBJ = Admintoleranceradiusgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')

                assert isinstance(request, HttpRequest)  
                Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.order_by('stoleranceclass')     
                return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                        }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintoleranceradiusgaugelist_list = Admintoleranceradiusgaugelist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminToleranceRadiusGaugeList.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceradiusgaugelist_list': Admintoleranceradiusgaugelist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')



 
@csrf_exempt
def adminToleranceSettingRingList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0 
                    txtdrangeto = 0 
                    txtdtolerance1 = 0
                    txtdtolerance2 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom']  
                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']  
        

                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom'] 
                        if(str(txtdrangefrom).isnumeric()):
                            txtdrangefrom = txtdrangefrom
                        else:
                            txtdrangefrom=0 

                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                        if(str(txtdrangeto).isnumeric()):
                            txtdrangeto = txtdrangeto
                        else:
                            txtdrangeto=0 
                            
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                        if(str(txtdtolerance1).isnumeric()):
                            txtdtolerance1 = txtdtolerance1
                        else:
                            txtdtolerance1=0 
                            
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']
                        if(str(txtdtolerance2).isnumeric()):
                            txtdtolerance2 = txtdtolerance2
                        else:
                            txtdtolerance2=0 
                    Adminunitlist_AddNewOBJ = Admintolerancesettingringlist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')

                    assert isinstance(request, HttpRequest)  
                    Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                            }
                            ) 
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0 
                txtdrangeto = 0 
                txtdtolerance1 = 0
                txtdtolerance2 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom']  
                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']  
    

                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom'] 
                    if(str(txtdrangefrom).isnumeric()):
                        txtdrangefrom = txtdrangefrom
                    else:
                        txtdrangefrom=0 

                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                    if(str(txtdrangeto).isnumeric()):
                        txtdrangeto = txtdrangeto
                    else:
                        txtdrangeto=0 
                        
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                    if(str(txtdtolerance1).isnumeric()):
                        txtdtolerance1 = txtdtolerance1
                    else:
                        txtdtolerance1=0 
                        
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']
                    if(str(txtdtolerance2).isnumeric()):
                        txtdtolerance2 = txtdtolerance2
                    else:
                        txtdtolerance2=0 

                Adminunitlist_AddNewOBJ = Admintolerancesettingringlist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')

                assert isinstance(request, HttpRequest)  
                Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.order_by('stoleranceclass')     
                return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                        }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintolerancesettingringlist_list = Admintolerancesettingringlist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminToleranceSettingRingList.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintolerancesettingringlist_list': Admintolerancesettingringlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')







 
@csrf_exempt
def adminToleranceSlipGaugeList(request):

    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST:  
               
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']
  
                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdrangefrom = 0 
                    txtdrangeto = 0 
                    txtdtolerance1 = 0
                    txtdtolerance2 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 
                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom']  
                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']  
        

                    if 'txtdrangefrom' in request.POST:
                        txtdrangefrom=request.POST['txtdrangefrom'] 
                        if(str(txtdrangefrom).isnumeric()):
                            txtdrangefrom = txtdrangefrom
                        else:
                            txtdrangefrom=0 

                    if 'txtdrangeto' in request.POST:
                        txtdrangeto=request.POST['txtdrangeto'] 
                        if(str(txtdrangeto).isnumeric()):
                            txtdrangeto = txtdrangeto
                        else:
                            txtdrangeto=0 
                            
                    if 'txtdtolerance1' in request.POST:
                        txtdtolerance1=request.POST['txtdtolerance1'] 
                        if(str(txtdtolerance1).isnumeric()):
                            txtdtolerance1 = txtdtolerance1
                        else:
                            txtdtolerance1=0 
                            
                    if 'txtdtolerance2' in request.POST:
                        txtdtolerance2=request.POST['txtdtolerance2']
                        if(str(txtdtolerance2).isnumeric()):
                            txtdtolerance2 = txtdtolerance2
                        else:
                            txtdtolerance2=0 
                            

                    Adminunitlist_AddNewOBJ = Admintoleranceslipgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2, dtolerance3=0  )
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')

                    assert isinstance(request, HttpRequest)  
                    Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                            {
                                
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                                'message':'Your User list page.',
                                'year':datetime.now().year, 
                                'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                            }
                            ) 
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')


            else:
                txtstoleranceclass = ""
                txtdrangefrom = 0 
                txtdrangeto = 0 
                txtdtolerance1 = 0
                txtdtolerance2 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 
                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom']  
                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']  
    

                if 'txtdrangefrom' in request.POST:
                    txtdrangefrom=request.POST['txtdrangefrom'] 
                    if(str(txtdrangefrom).isnumeric()):
                        txtdrangefrom = txtdrangefrom
                    else:
                        txtdrangefrom=0 

                if 'txtdrangeto' in request.POST:
                    txtdrangeto=request.POST['txtdrangeto'] 
                    if(str(txtdrangeto).isnumeric()):
                        txtdrangeto = txtdrangeto
                    else:
                        txtdrangeto=0 
                        
                if 'txtdtolerance1' in request.POST:
                    txtdtolerance1=request.POST['txtdtolerance1'] 
                    if(str(txtdtolerance1).isnumeric()):
                        txtdtolerance1 = txtdtolerance1
                    else:
                        txtdtolerance1=0 
                        
                if 'txtdtolerance2' in request.POST:
                    txtdtolerance2=request.POST['txtdtolerance2']
                    if(str(txtdtolerance2).isnumeric()):
                        txtdtolerance2 = txtdtolerance2
                    else:
                        txtdtolerance2=0 
                        

                Adminunitlist_AddNewOBJ = Admintoleranceslipgaugelist(stoleranceclass=txtstoleranceclass, drangefrom=txtdrangefrom,drangeto=txtdrangeto, dtolerance1=txtdtolerance1, dtolerance2=txtdtolerance2 , dtolerance3=0 )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')

                assert isinstance(request, HttpRequest)  
                Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.order_by('stoleranceclass')     
                return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                        {
                            
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year, 
                            'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                        }
                        )



        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                    {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintoleranceslipgaugelist_list = Admintoleranceslipgaugelist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminToleranceSlipGaugeList.html', 
                {
                        
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceslipgaugelist_list': Admintoleranceslipgaugelist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')










@csrf_exempt
def adminToleranceISManufacturingStdChartList(request):


    sPlantName = ""  
    semployeename = "" 
    sPlantName = request.session['sunitno']  
    semployeename = request.session['semployeename'] 
    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
         return home(request)

    if request.method == "POST":



            


        if 'cmbSaveValues' in request.POST: 
             
            if 'txtSearch' in request.POST:
                txtSearch = request.POST['txtSearch']

                if(len(txtSearch) == 0):
                        
                    
                    txtstoleranceclass = ""
                    txtdfromdia = 0
                    txtTo = 0
                    txtdtolupto = 0 
                    txtdhby2 = 0
                    txtda1 = 0
                    txtdy = 0
                    txtdz = 0
                    txtda = 0
                    txtdh1by2 = 0
                    txtdy1 = 0
                    txtdz1 = 0 


                    
                    

                    if 'txtstoleranceclass' in request.POST:
                        txtstoleranceclass=request.POST['txtstoleranceclass'] 

                    if 'txtdfromdia' in request.POST:
                        txtdfromdia=request.POST['txtdfromdia'] 
                        if(str(txtdfromdia).isnumeric()):
                            txtdfromdia = txtdfromdia
                        else:
                            txtdfromdia=0

                    if 'txtTo' in request.POST:
                        txtTo=request.POST['txtTo'] 
                        if(str(txtTo).isnumeric()):
                            txtTo = txtTo
                        else:
                            txtTo=0

                    if 'txtdtolupto' in request.POST:
                        txtdtolupto=request.POST['txtdtolupto'] 
                        if(str(txtdtolupto).isnumeric()):
                            txtdtolupto = txtdtolupto
                        else:
                            txtdtolupto=0

                    if 'txtdhby2' in request.POST:
                        txtdhby2=request.POST['txtdhby2'] 
                        if(str(txtdhby2).isnumeric()):
                            txtdhby2 = txtdhby2
                        else:
                            txtdhby2=0

                    if 'txtda1' in request.POST:
                        txtda1=request.POST['txtda1'] 
                        if(str(txtda1).isnumeric()):
                            txtda1 = txtda1
                        else:
                            txtda1=0

                    if 'txtdy' in request.POST:
                        txtdy=request.POST['txtdy'] 
                        if(str(txtdy).isnumeric()):
                            txtdy = txtdy
                        else:
                            txtdy=0

                    if 'txtdz' in request.POST:
                        txtdz=request.POST['txtdz'] 
                        if(str(txtdz).isnumeric()):
                            txtdz = txtdz
                        else:
                            txtdz=0
                            
                    if 'txtda' in request.POST:
                        txtda=request.POST['txtda'] 
                        if(str(txtda).isnumeric()):
                            txtda = txtda
                        else:
                            txtda=0

                    if 'txtdh1by2' in request.POST:
                        txtdh1by2=request.POST['txtdh1by2'] 
                        if(str(txtdh1by2).isnumeric()):
                            txtdh1by2 = txtdh1by2
                        else:
                            txtdh1by2=0

                    if 'txtdy1' in request.POST:
                        txtdy1=request.POST['txtdy1']
                        if(str(txtdy1).isnumeric()):
                            txtdy1 = txtdy1
                        else:
                            txtdy1=0

                    if 'txtdz1' in request.POST:
                        txtdz1=request.POST['txtdz1'] 
                        if(str(txtdz1).isnumeric()):
                            txtdz1 = txtdz1
                        else:
                            txtdz1=0


                    

                    Adminunitlist_AddNewOBJ = Admintoleranceismanufacturingstdchartlist(stoleranceclass=txtstoleranceclass, dfromdia=txtdfromdia, dtodia=txtTo,dtolupto=txtdtolupto, dhby2=txtdhby2, da1=txtda1, dy=txtdy, dz=txtdz, da=txtda, dh1by2=txtdh1by2,  dy1=txtdy1, dz1=txtdz1 )
        
                    Adminunitlist_AddNewOBJ.save()

                    messages.success(request, 'IS Standard is Added successfully!')
                
                    assert isinstance(request, HttpRequest) 
                    Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.order_by('stoleranceclass')     
                            
                            
                    return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                            }
                            )
                else:
                    
                    badmin = request.session['badmin'] 
                    if  badmin: 
                        assert isinstance(request, HttpRequest) 
                        Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                        return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                        {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                        }
                        )
                    else:
                        messages.error(request, 'Access Denied. As user donot have admin rights')

            else:
                txtstoleranceclass = ""
                txtdfromdia = 0
                txtTo = 0
                txtdtolupto = 0 
                txtdhby2 = 0
                txtda1 = 0
                txtdy = 0
                txtdz = 0
                txtda = 0
                txtdh1by2 = 0
                txtdy1 = 0
                txtdz1 = 0 


                
                

                if 'txtstoleranceclass' in request.POST:
                    txtstoleranceclass=request.POST['txtstoleranceclass'] 

                if 'txtdfromdia' in request.POST:
                    txtdfromdia=request.POST['txtdfromdia'] 
                    if(str(txtdfromdia).isnumeric()):
                        txtdfromdia = txtdfromdia
                    else:
                        txtdfromdia=0

                if 'txtTo' in request.POST:
                    txtTo=request.POST['txtTo'] 
                    if(str(txtTo).isnumeric()):
                        txtTo = txtTo
                    else:
                        txtTo=0

                if 'txtdtolupto' in request.POST:
                    txtdtolupto=request.POST['txtdtolupto'] 
                    if(str(txtdtolupto).isnumeric()):
                        txtdtolupto = txtdtolupto
                    else:
                        txtdtolupto=0

                if 'txtdhby2' in request.POST:
                    txtdhby2=request.POST['txtdhby2'] 
                    if(str(txtdhby2).isnumeric()):
                        txtdhby2 = txtdhby2
                    else:
                        txtdhby2=0

                if 'txtda1' in request.POST:
                    txtda1=request.POST['txtda1'] 
                    if(str(txtda1).isnumeric()):
                        txtda1 = txtda1
                    else:
                        txtda1=0

                if 'txtdy' in request.POST:
                    txtdy=request.POST['txtdy'] 
                    if(str(txtdy).isnumeric()):
                        txtdy = txtdy
                    else:
                        txtdy=0

                if 'txtdz' in request.POST:
                    txtdz=request.POST['txtdz'] 
                    if(str(txtdz).isnumeric()):
                        txtdz = txtdz
                    else:
                        txtdz=0
                            
                if 'txtda' in request.POST:
                    txtda=request.POST['txtda'] 
                    if(str(txtda).isnumeric()):
                        txtda = txtda
                    else:
                        txtda=0

                if 'txtdh1by2' in request.POST:
                    txtdh1by2=request.POST['txtdh1by2'] 
                    if(str(txtdh1by2).isnumeric()):
                        txtdh1by2 = txtdh1by2
                    else:
                        txtdh1by2=0

                if 'txtdy1' in request.POST:
                    txtdy1=request.POST['txtdy1']
                    if(str(txtdy1).isnumeric()):
                        txtdy1 = txtdy1
                    else:
                        txtdy1=0

                if 'txtdz1' in request.POST:
                    txtdz1=request.POST['txtdz1'] 
                    if(str(txtdz1).isnumeric()):
                        txtdz1 = txtdz1
                    else:
                        txtdz1=0
    

                Adminunitlist_AddNewOBJ = Admintoleranceismanufacturingstdchartlist(stoleranceclass=txtstoleranceclass, dfromdia=txtdfromdia, dtodia=txtTo,dtolupto=txtdtolupto, dhby2=txtdhby2, da1=txtda1, dy=txtdy, dz=txtdz, da=txtda, dh1by2=txtdh1by2,  dy1=txtdy1, dz1=txtdz1 )
    
                Adminunitlist_AddNewOBJ.save()

                messages.success(request, 'IS Standard is Added successfully!')
            
                assert isinstance(request, HttpRequest) 
                Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.order_by('stoleranceclass')     
                        
                        
                return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                        }
                        )
             
        else:
            data = request.POST
            txtSearch = ""
            if 'txtSearch' in request.POST:
                txtSearch = data.get("txtSearch")


            
            if(len(txtSearch) == 0):
                    
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest)  
                    Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.order_by('stoleranceclass')     
                    return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename, 
                        'message':'Your User list page.',
                        'year':datetime.now().year, 
                        'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')
            else:
                   
                badmin = request.session['badmin'] 
                if  badmin: 
                    assert isinstance(request, HttpRequest) 
                    Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.filter(stoleranceclass__icontains=txtSearch).values()
                    return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                    {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                    }
                    )
                else:
                    messages.error(request, 'Access Denied. As user donot have admin rights')

    else:        
        badmin = request.session['badmin'] 
        if  badmin:
            
                #Renders the contact page."""
            assert isinstance(request, HttpRequest)  
            Admintoleranceismanufacturingstdchartlist_list = Admintoleranceismanufacturingstdchartlist.objects.order_by('stoleranceclass')     
            return render(request,  'CloudCaliber/adminToleranceISManufacturingStdChartList.html', 
                {
                        'title':'User list', 
            'sPlantName': sPlantName ,  
            'semployeename':  semployeename,  
                        'message':'Your User list page.',
                        'year':datetime.now().year,  
                        'Admintoleranceismanufacturingstdchartlist_list': Admintoleranceismanufacturingstdchartlist_list, 
                    }
                )
        else:
            messages.error(request, 'Access Denied. As user donot have admin rights')

