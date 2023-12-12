from django.shortcuts import render
import json
import os
import re  
import webbrowser

from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import get_template


import cloudcaliber_project.settings 
#import textutils.settings

from django.conf import settings
from django.shortcuts import get_object_or_404 

from CloudCaliber.utils import render_to_pdf

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

from CloudCaliber.models import Adminoperatorlist, Admincategoryidcontinuousnolist, Masterinstrumentslistpart2, Adminassetserialformatlist, Masterinstrumentattachmentslist, Masterinstrumentcalibrationmasterslist, Masterinstrumentcalibrationsettingslist, Masterinstrumentenvironmentconditionlist, Masterinstrumentpartprojectslist,  Masterinstrumentpurchasechecklist, Masterinstrumentsparepartslist, Masterinstrumentslist 
# 
#from CloudCaliber.models import Admininstrumentmateriallist, Thistorytransactions, Thistorytransactionsmsa, Tmsaattributedatalist, Tmsabiasdatalist, Tmsalinearitydatalist, Tmsarnrdatalist, Tmsastabilitydatalist Tcalibrationhistorydetailslist, Tcalibrationhistorylist, Tcalibrationhistorymasterschecklistlist, Tcalibrationhistorymastersusedlist, Tdevicedamaged, Tdevicemissing, Tservicehistorylist, Ttraceissuereturnlist, Tutility8D0Emergencyactionlist, Tutility8D1Documentslist, Tutility8D1Teamdlist, Tutility8D3Containmentactionlist, Tutility8D4Rootcauselist, Tutility8D5Correctiveactionlist, Tutility8D6Implementcorrectiveactionlist, Tutility8D7Apreventiveactionlist, Tutility8D7Bprocesslist, Tutility8D7Creviewlist
#$, Tmsavisualdatalist Tpostpone, Tprepone, Tusagegaugedaily, Tverificationmain, Admin1Atrack, Admin1Companyinfo, Adminassetcategorylist, Adminassetcategorytypelist, Adminassetcategorytypelist1
from CloudCaliber.models import  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
#from CloudCaliber.models import Tutility8D8Followupmeetingslist, Tutility8Dlist, Tutilitydcdetailslist, Tutilitydclist
 

bNewIDwithfirstSerial = 0
 




@csrf_exempt
def GaugeMasterlistCreateID(request):
 


    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

    sCodeFinal1 = ""
    sCodeFinal2 = ""
   

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname'] 
    semployeename = request.session['semployeename']

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
    getFlow2Code = ""
    getFlow3Code = ""
    getFlow4Code = ""
    getFlow5Code = ""
    getFlowContCode = ""

    bContFlag = 0

    bSpareA =0 


    sPlantNameName = ""
    sPlantNameNameA = ""
    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
        sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
        sPlantNameNameA = AdminunitlistActive.splantname
 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode




    if request.method == "POST":

        data = request.POST
        ID_Categories =0
        if 'Categories' in request.POST: 
            if(data.get('Categories').isnumeric()):
                ID_Categories = int(data.get('Categories'))

        if 'bSpare' in request.POST: 
            bSpareA = 1
            
        ClassificationData =0
        if 'Classification' in request.POST:
            if(data.get('Classification').isnumeric()):
                ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST:
            if(data.get('Flow1').isnumeric()):
                Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST: 
            if(data.get('Flow2').isnumeric()):
                Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST: 
            if(data.get('Flow3').isnumeric()):
                Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST: 
            if(data.get('Flow4').isnumeric()):
                Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST: 
            if(data.get('Flow5').isnumeric()):
                Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST: 
            GaugeClass = int(data.get('GaugeClass'))

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('Dashboard')







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


            sCodeFinal1 = sClasscode
            sCodeFinal2 = sClasscode + " " + sPlantCode
         
            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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







            sCodeFinal1 = sClasscode + sCategoryCode
            sCodeFinal2 = sClasscode  + sCategoryCode + " " + sPlantCode
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })




            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })
            






        if 'cmbGetID' in request.POST:  
               
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
 
            Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_list:
                sCategoryCode = Adminassetcategorylist_list.scode
                sClasscode = Adminassetcategorylist_list.styperefname  
                styperefnameA1 = Adminassetcategorylist_list.styperefname1
                styperefnameA2 = Adminassetcategorylist_list.styperefname2
                styperefnameA3 = Adminassetcategorylist_list.styperefname3
                styperefnameA4 = Adminassetcategorylist_list.styperefname4
                styperefnameA5 = Adminassetcategorylist_list.styperefname5



            sCodeFlow1 = ""
            sCodeFlow2 = ""
            sCodeFlow3 = ""
            sCodeFlow4 = ""
            sCodeFlow5 = ""

            if(Flow1Data !=0):
                if (styperefnameA1 == "Part No"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Equipment"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Operation"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Material"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                else:
                    Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                    


            if(Flow2Data !=0):
                if (styperefnameA2 == "Part No"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Equipment"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Operation"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Material"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                else:
                    Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                    


            if(Flow3Data !=0):
                if (styperefnameA3 == "Part No"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Equipment"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Operation"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Material"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                else:
                    Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                 


            if(Flow4Data !=0):
                if (styperefnameA4 == "Part No"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Equipment"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Operation"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Material"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                else:
                    Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                 

            if(Flow5Data !=0):
                if (styperefnameA5 == "Part No"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Equipment"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Operation"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Material"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                else:
                    Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                 

            sContNo = ""
            sContNo1 = ""
            lContNo = 0
            lContNoVB = 0
            lContNoVBC = 0
        
            lassetidA =0

            sCategoryCode = "" 
            Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_listH:
                sCategoryCode = Adminassetcategorylist_listH.scode 
                sClasscode = Adminassetcategorylist_listH.styperefname 
                lassetidA = Adminassetcategorylist_listH.lassetid
                lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
        
 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')



            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
          

            AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
            if AdmincategoryidcontinuousnolistActivw:
                for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                    lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                    lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            else:
                lContNo  = lContNoVB
 

            if (lContNoVBC == 0 ):
                if (lassetidA == 6): 
                    
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0
            else:
                if (lassetidA == 6):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8):  
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0

 

            if(sContNo1 != ''):
                if(len(sContNo1) == 1):
                    sContNo = "000" + sContNo1
                elif(len(sContNo1) == 2):
                    sContNo = "00" + sContNo1
                elif(len(sContNo1) == 3):
                    sContNo = "0" + sContNo1
                else:
                    sContNo =  sContNo1

 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')


            sCodeFinal1 = ""
            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  #+  sContNo.strip()
        

            lSerialNo =0
            
            AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
            if AdminassetserialformatlistActive:
                for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                    lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


            lSerialNo = lSerialNo +1
 

            
            bNewIDwithfirstSerial = 0
            if (lSerialNo == 1):
                bNewIDwithfirstSerial = 1

 
            sSerialNo = ""
            sSerialNo1 = ""
            sSerialNo=str(lSerialNo)
            if (len(sSerialNo) == 1):
                sSerialNo1 = "00" + sSerialNo
            elif (len(sSerialNo) == 2):
                sSerialNo1 = "0" + sSerialNo 
            else:
                sSerialNo1 =   sSerialNo 


           # sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
            sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()    + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
             


    
 
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })


            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            return render(request, 'CloudCaliber/GaugeMasterlistCreateID.html',
        {     
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': Flow1Data ,  
            'cmbFlow2ID': Flow2Data ,  
            'cmbFlow3ID': Flow3Data ,  
            'cmbFlow4ID': Flow4Data ,
            'cmbFlow5ID': Flow5Data ,     
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })






        if 'cmbSaveAdd' in request.POST:  


             


            sGaugeClass = ""
            if (GaugeClass != 0):
                Admintoleranceclasslist_listGet =  Admintoleranceclasslist.objects.get(lid = GaugeClass)
                if (Admintoleranceclasslist_listGet):
                    sGaugeClass = Admintoleranceclasslist_listGet.stoleranceclass
                

             
            bFlag = 0

            sFlow1 = ""
            sFlow2 =  ""
            sFlow3 =  ""
            sFlow4 =  ""
            sFlow5 =  ""
            sFlowDesc1 = ""
            sFlowDesc2 =  ""
            sFlowDesc3 =  ""
            sFlowDesc4 =  ""
            sFlowDesc5 =  "" 
            sCategorytype = ""

            sAssetCategory = ""

            if (ClassificationData == 0):
                bFlag = 1
                messages.error(request, 'Asset Classification is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
            else :
                if (ID_Categories == 0):
                    bFlag = 1
                    messages.error(request, 'Asset Category is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
                else :

                    Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                    if Adminassetcategorylist_list:
                        sCategoryCode = Adminassetcategorylist_list.scode
                        sCategorytype = Adminassetcategorylist_list.categorytype
                        sClasscode = Adminassetcategorylist_list.styperefname
                        sAssetCategory = Adminassetcategorylist_list.assettype 
                        #request.session['sCategoryCode'] = Adminassetcategorylist_list.scode
                        #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                        #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                        #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                        #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                        #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                        #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                        styperefnameA1 = Adminassetcategorylist_list.styperefname1
                        styperefnameA2 = Adminassetcategorylist_list.styperefname2
                        styperefnameA3 = Adminassetcategorylist_list.styperefname3
                        styperefnameA4 = Adminassetcategorylist_list.styperefname4
                        styperefnameA5 = Adminassetcategorylist_list.styperefname5
                        sCodeDescA = Adminassetcategorylist_list.categorytype
                        sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                        sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                        sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                        sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                        sCodeDesc5 = Adminassetcategorylist_list.styperefname5
                

                    if( styperefnameA1 != ''):
                        if(Flow1Data == 0):
                            bFlag = 1
                            sFlow1Message = styperefnameA1 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow1Message)

 
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                             

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {   
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'bcalibrateidle':bcalibrateidle,  
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA2 != ''):
                        if(Flow2Data == 0):
                            bFlag = 1
                            sFlow2Message = styperefnameA2 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow2Message)
                            
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                             

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {   
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'bcalibrateidle':bcalibrateidle,  
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA3 != ''):
                        if(Flow3Data == 0):
                            bFlag = 1
                            sFlow3Message = styperefnameA3 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow3Message)

                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            
                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,   
                            'bcalibrateidle':bcalibrateidle,  
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA4 != ''):
                        if(Flow4Data == 0):
                            bFlag = 1
                            sFlow4Message = styperefnameA4 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow4Message)
                           
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                          
                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {   
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,   
                            'bcalibrateidle':bcalibrateidle,  
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA5 != ''):
                        if(Flow5Data == 0):
                            bFlag = 1
                            sFlow5Message = styperefnameA5 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow5Message)

                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            
                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {   
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories , 
                            'bcalibrateidle':bcalibrateidle,  
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if (bFlag == 0):
                    
                        
                        sCodeDescription = ""
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
                        sCategoryDesc = ""
            
                        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_list:
                            sCategoryCode = Adminassetcategorylist_list.scode
                            sCategorytype = Adminassetcategorylist_list.categorytype
                            sClasscode = Adminassetcategorylist_list.styperefname
                            sAssetCategory = Adminassetcategorylist_list.assettype 
                            #['sCategoryCode'] = Adminassetcategorylist_list.scode
                            #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                            #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                            #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                            #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                            #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                            #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                            styperefnameA1 = Adminassetcategorylist_list.styperefname1
                            styperefnameA2 = Adminassetcategorylist_list.styperefname2
                            styperefnameA3 = Adminassetcategorylist_list.styperefname3
                            styperefnameA4 = Adminassetcategorylist_list.styperefname4
                            styperefnameA5 = Adminassetcategorylist_list.styperefname5
                            sCodeDescA = Adminassetcategorylist_list.categorytype
                            sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                            sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                            sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                            sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                            sCodeDesc5 = Adminassetcategorylist_list.styperefname5

                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   

                        sCategoryDesc = sCategorytype
                        sCodeFlow1 = ""
                        sCodeFlow2 = ""
                        sCodeFlow3 = ""
                        sCodeFlow4 = ""
                        sCodeFlow5 = ""

                        if(Flow1Data !=0):
                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                                


                        if(Flow2Data !=0):
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                                


                        if(Flow3Data !=0):
                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                            


                        if(Flow4Data !=0):
                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                            

                        if(Flow5Data !=0):
                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                            
 
                        sCodeDesc1 = sCodeFlow1
                        sCodeDesc2 = sCodeFlow2
                        sCodeDesc3 = sCodeFlow3
                        sCodeDesc4 = sCodeFlow4
                        sCodeDesc5 = sCodeFlow5
                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   
                        sContNo = ""
                        sContNo1 = ""
                        lContNo = 0
                        lContNoVB = 0
                        lContNoVBC = 0
                    
                        lassetidA =0

                        sCategoryCode = "" 
                        Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_listH:
                            sCategoryCode = Adminassetcategorylist_listH.scode 
                            sClasscode = Adminassetcategorylist_listH.styperefname 
                            lassetidA = Adminassetcategorylist_listH.lassetid
                            lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
                    
                        
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')

                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
                    
                        sCodeFinal1AK = sCodeFinal1

                        AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
                        if AdmincategoryidcontinuousnolistActivw:
                            for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                                lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                                lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                        else:
                            lContNo  = lContNoVB
            

                        if (lContNoVBC == 0 ):
                            if (lassetidA == 6): 
                                
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0
                        else:
                            if (lassetidA == 6):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8):  
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0

            

                        if(sContNo1 != ''):
                            if(len(sContNo1) == 1):
                                sContNo = "000" + sContNo1
                            elif(len(sContNo1) == 2):
                                sContNo = "00" + sContNo1
                            elif(len(sContNo1) == 3):
                                sContNo = "0" + sContNo1
                            else:
                                sContNo =  sContNo1


                        sContNo = ""
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')


                        sCodeFinal1 = ""
                        #sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() +  sContNo.strip()
                    
                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  
                    

                        lSerialNo =0
                        
                        AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
                        if AdminassetserialformatlistActive:
                            for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                                lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


                        lSerialNo = lSerialNo +1
            

                        
                        bNewIDwithfirstSerial = 0
                        if (lSerialNo == 1):
                            bNewIDwithfirstSerial = 1

            
                        sSerialNo = ""
                        sSerialNo1 = ""
                        sSerialNo=str(lSerialNo)
                        if (len(sSerialNo) == 1):
                            sSerialNo1 = "00" + sSerialNo
                        elif (len(sSerialNo) == 2):
                            sSerialNo1 = "0" + sSerialNo 
                        else:
                            sSerialNo1 =   sSerialNo 


                        #sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
                    
                        sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  + "-" + sPlantCode[:2] + sSerialNo1.strip()
                
                    


                        if(lContNoVBC == 1): 
                                Adminassetserialformatlistsave = Admincategoryidcontinuousnolist(scode =sCodeFinal1AK, lserialno=lContNo)
                                Adminassetserialformatlistsave.save()
                                
                                AdminassetcategorylistGet =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories)
                                 

                                Adminassetcategorylistsave =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                                Adminassetcategorylistsave.lcontinuousnoa  =lContNo
                                Adminassetcategorylistsave.save()
 


                        if (lSerialNo == 1):
                            Adminassetserialformatlistsave = Adminassetserialformatlist(scode =sCodeFinal1, lserialno=lSerialNo)
                            Adminassetserialformatlistsave.save()
                        else:         
                            AdminassetserialformatlistGet =  Adminassetserialformatlist.objects.filter(scode = sCodeFinal1).values()
                            lIDCodeABC =0
                            if AdminassetserialformatlistGet:
                                for AdminassetserialformatlistGetOBJ in AdminassetserialformatlistGet.all():
                                    lIDCodeABC = AdminassetserialformatlistGetOBJ['lid']

                            Adminassetserialformatlistsave =  Adminassetserialformatlist.objects.get(lid = lIDCodeABC) 
                            Adminassetserialformatlistsave.lserialno =lSerialNo
                            Adminassetserialformatlistsave.save()

 


   
                        lid = 0
                        sinstrumentid = sCodeFinal2
                        sdescription = sCategoryDesc
                        sassettype = sAssetCategory
                        lplantid = lPlantId
                        splanttype = sPlantName
                        lcategoryid = ID_Categories
                        categorytype = sCategorytype
                        assettype = sAssetCategory
                        lassetid = ClassificationData
                        btyperef1 = 0
                        if (styperefnameA1 != ''):
                            btyperef1 = 1
                        scategorytype1 = styperefnameA1
                        styperefname1 = sCodeFlow1
                        btyperef2 = 0
                        if (styperefnameA2 != ''):
                            btyperef2 = 1
                        scategorytype2 = styperefnameA2
                        styperefname2 = sCodeFlow2
                        btyperef3 = 0
                        if (styperefnameA3 != ''):
                            btyperef3 = 1
                        scategorytype3 = styperefnameA3
                        styperefname3 = sCodeFlow3
                        btyperef4 = 0
                        if (styperefnameA4 != ''):
                            btyperef4 = 1
                        scategorytype4 =styperefnameA4
                        styperefname4 = sCodeFlow4
                        btyperef5 = 0
                        if (styperefnameA5 != ''):
                            btyperef5 = 1
                        scategorytype5 = styperefnameA5
                        styperefname5 = sCodeFlow5
                        smake = ""
                        ldefaultlocationid = 0
                        slocationname = ""
                        scurrentstatus = "PURCHASE INITIATED"
                        if(bSpareA == 1):
                            scurrentstatus = "SPARE"
                        bcalib = 0
                        dtlastcalib = datetime.now()
                        dtnextcalib = datetime.now()
                        slastcalibdate = ""
                        snextcalibdate = ""
                        dtcalibdisplaydate = datetime.now()
                        ldueday = 0
                        lduemonth = 0
                        ldueyear = 0
                        sfreqtype = ""
                        busagewise = 0
                        lcalibrationvendorid = 0
                        scalibvendor = ""
                        bcheckin = 0
                        busage = 0
                        blimitedusage = 0
                        bdamaged = 0
                        battribute = 0
                        bfreezecalib = 0
                        bvalidation = 0
                        bsentforcalibration = 0
                        oldinstrument_id = ""
                        sinstrumentcode = sCodeFinal2
                        bpurchaseclosed = 0
                        bidlecalibration = 0
                        bsamplepartusage = 0
                        bregularpartusage = 0
                        bcalibstandards = 0
                        spartno = ""
                        lcompanyid = lcompanyid
                        bplanned = 1
                        serpcode = sCodeFinal1
                        lhistorycard = 0
                        lfolowid1 = Flow1Data
                        lfolowid2 = Flow2Data
                        lfolowid3 = Flow3Data
                        lfolowid4 = Flow4Data
                        lfolowid5 = Flow5Data



                        sstoragerack = ""
                        sdrawingno = ""
                        sdrawingrevno = ""
                        sdrawingfile = ""
                        sunitofmeasure = ""
                        srevisionno = ""
                        sproperty = ""
                        scatalogueno = ""
                        frangefrom = 0
                        frangeto = 0
                        fleastcount = 0
                        scheckmethod = ""
                        dtlastservice = datetime.now()
                        dtnextservice = datetime.now()
                        slastservicedate = ""
                        snextservicedate = ""
                        smanualduernr = ""
                        ldayremainrnr = 0
                        dtlastrnr = datetime.now()
                        dtnextrnr = datetime.now()
                        slastrnrdate = ""
                        snextrnrdate = ""
                        srange = ""
                        frange3 = 0
                        dcalibrationcost = 0
                        dpurchaseprice = 0
                        smodelno = ""
                        sserialno = ""
                        saccuracy = ""
                        scertificateno = ""
                        straceability = ""
                        ssize1 = ""
                        llusagedefault = 0
                        llusagecount = 0
                        smounted = ""
                        fproducttolerance = 0
                        sproducttolerance = 0
                        facconstant = 0
                        sagencyservice = ""
                        sprocuredate = ""
                        brejected = 0
                        srejecteddate = ""
                        breplaced = 0
                        lreplacedinstrumentid = 0
                        bduechanged = 0
                        dtduechangedate = datetime.now()
                        slastchangedate = datetime.now()
                        blanova = 0
                        srevno = ""
                        scommentchangecalibstd = ""
                        bverifyforpurchase = 0
                        dtsendforverificationforpurchaseon = datetime.now()
                        dtverifiedforpurchaseon = datetime.now()
                        ssendforverificationforpurchaseon = ""
                        sverifiedforpurchaseon = ""
                        spreferredvendor = ""
                        sbondnumber = ""
                        dgo = 0
                        dnogo = 0
                        dtoldiff = 0
                        dtolallowed = 0
                        bmanufacturingstd = 0
                        dplusofminus = 0
                        dz = 0
                        bpartno = 0
                        gageserialno = ""
                        sdrawingno2 = ""
                        lcontinuousnoa2 = 0
                        lcontinuousnob2 = 0
                        lcategorytype1 = 0
                        lcategorytype2 = 0
                        bcustomer = 0
                        lservicealert = 0
                        ferrorallowed = 0
                        splannedby = ""
                        bidchanged = 0
                        scode1 = sCategoryCode
                        scode2 = sGaugeClass
                        scode3 = ""
                        scode4 = ""
                        scode5 = ""
                        ssstatus = ""
                        ssize = ""
                        lintervalservice = 0
                        sintervalperiodservice = ""
                        smanufacturer = ""
                        ddateofprocure = datetime.now()
                        sdateofprocure = ""
                        soperation = ""
                        scompantname = ""
                        lcontinuousnoa1 = 0
                        lcontinuousnob1 = 0
                        lcontinuousnoa = 0
                        lcontinuousnob = 0
                        btyperef = 0
                        btyperefascontinuousnoa = 0
                        btyperefascontinuousnob = 0
                        scomment = ""
                        lpurchasevendorid = 0
                        lservicevendorid = 0
                        sagencycalib = ""
                        scode = sCategoryCode
                        lcurrentlocationid = 0
                        bservice = 0
                        lcalibalert = 0
                        lintervalcalib = 0
                        sintervalperiodcalib = ""
                        lalertinterval = 0
                        ldayremaincalib = 0
                        lusageinterval = 0
                        lusageintervaldisplay = 0
                        lusagecurrent = 0
                        lidlecalibfrequency = 0
                        dtplanneddate = datetime.now()
                        splanneddate = ""
                        dtvalidationlastdate = datetime.now()
                        svalidationlastdate = ""
                        dtvalidationnextdate = datetime.now()
                        svalidationnextdate = ""
                        schangeoldid = ""
                        llusagecountalerts = 0
                        btnextidlecalibration = datetime.now()
                        snextidlecalibration = ""
                        dtidleon = datetime.now()
                        sidleon = ""
                        b1monthvalidation = 0
                        dtnextvalidation = datetime.now()
                        snextvalidation = ""
                        dtlastvalidation = datetime.now()
                        slastvalidation = ""
                        bcalibrateidle =0

                        lidA = 0


                         
                        MasterinstrumentslistSave = Masterinstrumentslist(sinstrumentid  = sinstrumentid,  lrepairid =  0, bunderrepair =  0, lvalibationid =  0, bundervalidation =  0, l8did =  0, bunder8d =  0, lmsarnrid =  0, bunderrnr =  0, bunderattribute =  0, lstabilityid =  0, bunderstability =  0, lbiasid = 0,  bunderbias = 0, llinearityid = 0, bunderlinearity = 0, btransferred=0, bissedtosupplier=0 )
                        MasterinstrumentslistSave.save() 
                    
                        lInstId =0
                        lInstId = MasterinstrumentslistSave.lid
                    
                        Masterinstrumentslistpart2Save = Masterinstrumentslistpart2(linstrumentid  = lInstId )
                        Masterinstrumentslistpart2Save.save()
                   
                        Masterinstrumentslistpart3Save = Masterinstrumentslistpart2(linstrumentid  = lInstId )
                        Masterinstrumentslistpart3Save.save()

                        Masterinstrumentslistpart4Save = Masterinstrumentslistpart2(linstrumentid  = lInstId )
                        Masterinstrumentslistpart4Save.save()


                        lInstIdA =0
                        lInstIdA = Masterinstrumentslistpart2Save.lid
                        lInstIdB =0
                        iCou =0
                        Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.values().filter(serpcode =sCodeFinal1)
                        #Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.filter(lcategoryid =ID_Categories).order_by('-lid')[:1]
                        if Masterinstrumentslist_listcOPY:
                            for Masterinstrumentslist_listcOPY in Masterinstrumentslist_listcOPY.all():  
                                if (iCou == 0):
                                    iCou = iCou + 1
                                    lInstIdB =Masterinstrumentslist_listcOPY['lid'] 
                                    sdescription = Masterinstrumentslist_listcOPY['sdescription'] 
                                    smake = Masterinstrumentslist_listcOPY['smake']
                                    ldefaultlocationid  = Masterinstrumentslist_listcOPY['ldefaultlocationid']
                                    slocationname  = Masterinstrumentslist_listcOPY['slocationname'] 
                                    bcalib = Masterinstrumentslist_listcOPY['bcalib']   
                                    sfreqtype = Masterinstrumentslist_listcOPY['sfreqtype']
                                    busagewise = Masterinstrumentslist_listcOPY['busagewise']
                                    lcalibrationvendorid = Masterinstrumentslist_listcOPY['lcalibrationvendorid']
                                    scalibvendor = Masterinstrumentslist_listcOPY['scalibvendor'] 
                                    busage = Masterinstrumentslist_listcOPY['busage']  
                                    battribute = Masterinstrumentslist_listcOPY['battribute'] 
                                    bvalidation = Masterinstrumentslist_listcOPY['bvalidation']   
                                    bidlecalibration = Masterinstrumentslist_listcOPY['bidlecalibration']   
                                    bsamplepartusage = Masterinstrumentslist_listcOPY['bsamplepartusage']   
                                    bregularpartusage = Masterinstrumentslist_listcOPY['bregularpartusage']   
                                    bcalibstandards = Masterinstrumentslist_listcOPY['bcalibstandards']   
                                    spartno = Masterinstrumentslist_listcOPY['spartno'] 
                                    if(Masterinstrumentslist_listcOPY['bcalibrateidle'] == 1):
                                        bcalibrateidle = 1  
                                    else:
                                        bcalibrateidle =0



                        sstoragerack = ""
                        sdrawingno = ""
                        sdrawingrevno = ""
                        sdrawingfile = ""
                        sunitofmeasure = ""
                        srevisionno = ""
                        sproperty = ""
                        scatalogueno = ""
                        frangefrom = 0
                        frangeto = 0
                        fleastcount = 0
                        scheckmethod = ""
                        dtlastservice = datetime.now()
                        dtnextservice = datetime.now()
                        slastservicedate = ""
                        snextservicedate = ""
                        smanualduernr = ""
                        ldayremainrnr = 0
                        dtlastrnr = datetime.now()
                        dtnextrnr = datetime.now()
                        slastrnrdate = ""
                        snextrnrdate = ""
                        srange = ""
                        frange3 = 0
                        dcalibrationcost = 0
                        dpurchaseprice = 0
                        smodelno = ""
                        sserialno = ""
                        saccuracy = ""
                        scertificateno = ""
                        straceability = ""
                        ssize1 = ""
                        llusagedefault = 0
                        llusagecount = 0
                        smounted = ""
                        fproducttolerance = 0
                        sproducttolerance = ""
                        facconstant = 0
                        sagencyservice = ""
                        sagencyservice = ""
                        sprocuredate = ""
                        brejected = 0
                        srejecteddate = ""
                        breplaced = 0
                        lreplacedinstrumentid = 0
                        bduechanged = 0
                        dtduechangedate = datetime.now()
                        slastchangedate = ""
                        blanova = 0
                        srevno = ""
                        scommentchangecalibstd = ""
                        bverifyforpurchase = 0
                        dtsendforverificationforpurchaseon = datetime.now()
                        dtverifiedforpurchaseon = datetime.now()
                        ssendforverificationforpurchaseon = ""
                        sdateofprocure = ""
                        spreferredvendor = ""
                        sbondnumber = ""
                        dgo = 0
                        dnogo = 0
                        dtoldiff = 0
                        dtolallowed = 0
                        bmanufacturingstd = 0
                        dplusofminus = 0
                        dz = 0
                        bpartno = 0
                        gageserialno = ""
                        sdrawingno2 = ""
                        lcontinuousnoa2 = 0
                        lcontinuousnob2 = 0
                        lcategorytype1 = 0
                        lcategorytype2 = 0
                        bcustomer = 0
                        lservicealert = 0
                        ferrorallowed = 0
                        splannedby = ""
                        bidchanged = 0
                        scode1 = ""
                        scode2 = ""
                        scode3 = ""
                        scode4 = ""
                        scode5 = ""
                        ssstatus = ""
                        ssize = ""
                        lintervalservice = 0
                        sintervalperiodservice = ""
                        smanufacturer = ""
                        ddateofprocure = datetime.now()
                        sdateofprocure = ""
                        soperation = ""
                        scompantname = ""
                        lcontinuousnoa1 = 0
                        lcontinuousnob1 = 0
                        lcontinuousnoa = 0
                        lcontinuousnob = 0
                        btyperef = 0
                        btyperefascontinuousnoa = 0
                        btyperefascontinuousnob = 0
                        scomment = ""
                        lpurchasevendorid = 0
                        lservicevendorid = 0
                        sagencycalib = ""
                        scode = ""
                        lcurrentlocationid = 0
                        bservice = 0
                        lcalibalert = 0
                        lintervalcalib = 0
                        sintervalperiodcalib = ""
                        lalertinterval = 0
                        ldayremaincalib = 0
                        lusageinterval = 0
                        lusageintervaldisplay = 0
                        lusagecurrent = 0
                        lidlecalibfrequency = 0
                        dtplanneddate = datetime.now()
                        splanneddate = ""
                        dtvalidationlastdate = datetime.now()
                        svalidationlastdate = ""
                        dtvalidationnextdate = datetime.now()
                        svalidationnextdate = ""
                        schangeoldid = ""
                        llusagecountalerts = 0
                        btnextidlecalibration = datetime.now()
                        snextidlecalibration = ""
                        dtidleon = datetime.now()
                        sidleon = ""
                        b1monthvalidation = 0
                        dtnextvalidation = datetime.now()
                        snextvalidation = ""
                        dtlastvalidation = datetime.now()
                        slastvalidation = ""


                        Masterinstrumentslist_listcOPY2 =  Masterinstrumentslistpart2.objects.filter(linstrumentid =lInstIdB)
                        if Masterinstrumentslist_listcOPY2:
                            for Masterinstrumentslist_listcOPY2 in Masterinstrumentslist_listcOPY2.all():  
                                sstoragerack = Masterinstrumentslist_listcOPY2.sstoragerack 
                                sdrawingno = Masterinstrumentslist_listcOPY2.sdrawingno 
                                sdrawingrevno = Masterinstrumentslist_listcOPY2.sdrawingrevno 
                                sdrawingfile = Masterinstrumentslist_listcOPY2.sdrawingfile 
                                sunitofmeasure = Masterinstrumentslist_listcOPY2.sunitofmeasure 
                                srevisionno = Masterinstrumentslist_listcOPY2.srevisionno 
                                sproperty = Masterinstrumentslist_listcOPY2.sproperty 
                                scatalogueno = Masterinstrumentslist_listcOPY2.scatalogueno 
                                frangefrom = Masterinstrumentslist_listcOPY2.frangefrom 
                                frangeto = Masterinstrumentslist_listcOPY2.frangeto 
                                fleastcount = Masterinstrumentslist_listcOPY2.fleastcount 
                                scheckmethod = Masterinstrumentslist_listcOPY2.scheckmethod  
                                smanualduernr = Masterinstrumentslist_listcOPY2.smanualduernr 
                                ldayremainrnr = Masterinstrumentslist_listcOPY2.ldayremainrnr  
                                srange = Masterinstrumentslist_listcOPY2.srange 
                                frange3 = Masterinstrumentslist_listcOPY2.frange3 
                                dcalibrationcost = Masterinstrumentslist_listcOPY2.dcalibrationcost 
                                dpurchaseprice = Masterinstrumentslist_listcOPY2.dpurchaseprice 
                                
                                saccuracy = Masterinstrumentslist_listcOPY2.saccuracy   
                                ssize1 = Masterinstrumentslist_listcOPY2.ssize1 
                                llusagedefault = Masterinstrumentslist_listcOPY2.llusagedefault  
                                smounted = Masterinstrumentslist_listcOPY2.smounted 
                                fproducttolerance = Masterinstrumentslist_listcOPY2.fproducttolerance 
                                sproducttolerance = Masterinstrumentslist_listcOPY2.sproducttolerance 
                                facconstant = Masterinstrumentslist_listcOPY2.facconstant 
                                sagencyservice = Masterinstrumentslist_listcOPY2.sagencyservice 
                                 
                                srevno = Masterinstrumentslist_listcOPY2.srevno  
                                spreferredvendor = Masterinstrumentslist_listcOPY2.spreferredvendor 
                                sbondnumber = Masterinstrumentslist_listcOPY2.sbondnumber 
                                dgo = Masterinstrumentslist_listcOPY2.dgo 
                                dnogo = Masterinstrumentslist_listcOPY2.dnogo 
                                dtoldiff = Masterinstrumentslist_listcOPY2.dtoldiff 
                                dtolallowed = Masterinstrumentslist_listcOPY2.dtolallowed 
                                bmanufacturingstd = Masterinstrumentslist_listcOPY2.bmanufacturingstd 
                                dplusofminus = Masterinstrumentslist_listcOPY2.dplusofminus 
                                dz = Masterinstrumentslist_listcOPY2.dz 
                                
                                sdrawingno2 = Masterinstrumentslist_listcOPY2.sdrawingno2   
                                ferrorallowed = Masterinstrumentslist_listcOPY2.ferrorallowed 
                                splannedby = Masterinstrumentslist_listcOPY2.splannedby   
                                ssize = Masterinstrumentslist_listcOPY2.ssize  
                                smanufacturer = Masterinstrumentslist_listcOPY2.smanufacturer       
                                lpurchasevendorid = Masterinstrumentslist_listcOPY2.lpurchasevendorid 
                                lservicevendorid = Masterinstrumentslist_listcOPY2.lservicevendorid 
                                sagencycalib = Masterinstrumentslist_listcOPY2.sagencycalib  
                                lcalibalert = Masterinstrumentslist_listcOPY2.lcalibalert 
                                lintervalcalib = Masterinstrumentslist_listcOPY2.lintervalcalib 
                                sintervalperiodcalib = Masterinstrumentslist_listcOPY2.sintervalperiodcalib 
                                lalertinterval = Masterinstrumentslist_listcOPY2.lalertinterval  
                                lusageinterval = Masterinstrumentslist_listcOPY2.lusageinterval 
                                lusageintervaldisplay = Masterinstrumentslist_listcOPY2.lusageintervaldisplay  
                                lidlecalibfrequency = Masterinstrumentslist_listcOPY2.lidlecalibfrequency   
                                llusagecountalerts = Masterinstrumentslist_listcOPY2.llusagecountalerts  
                                b1monthvalidation = Masterinstrumentslist_listcOPY2.b1monthvalidation  



                        Masterinstrumentslist_listSaveUpdate =  Masterinstrumentslist.objects.get(lid =lInstId) 
                    

                        Masterinstrumentslist_listSaveUpdate.sinstrumentid = sCodeFinal2
                        Masterinstrumentslist_listSaveUpdate.sdescription = sdescription
                        Masterinstrumentslist_listSaveUpdate.sassettype = sAssetCategory
                        Masterinstrumentslist_listSaveUpdate.lplantid = lPlantId
                        Masterinstrumentslist_listSaveUpdate.splanttype = sPlantName
                        Masterinstrumentslist_listSaveUpdate.lcategoryid = ID_Categories
                        Masterinstrumentslist_listSaveUpdate.categorytype = sCategorytype
                        Masterinstrumentslist_listSaveUpdate.assettype = sAssetCategory
                        Masterinstrumentslist_listSaveUpdate.lassetid = ClassificationData
                        Masterinstrumentslist_listSaveUpdate.btyperef1 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype1 = styperefnameA1
                        Masterinstrumentslist_listSaveUpdate.styperefname1 = sCodeFlow1
                        Masterinstrumentslist_listSaveUpdate.btyperef2 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype2 = styperefnameA2
                        Masterinstrumentslist_listSaveUpdate.styperefname2 = sCodeFlow2
                        Masterinstrumentslist_listSaveUpdate.btyperef3 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype3 = styperefnameA3
                        Masterinstrumentslist_listSaveUpdate.styperefname3 = sCodeFlow3
                        Masterinstrumentslist_listSaveUpdate.btyperef4 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype4 =styperefnameA4
                        Masterinstrumentslist_listSaveUpdate.styperefname4 = sCodeFlow4
                        Masterinstrumentslist_listSaveUpdate.btyperef5 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype5 = styperefnameA5
                        Masterinstrumentslist_listSaveUpdate.styperefname5 = sCodeFlow5
                        Masterinstrumentslist_listSaveUpdate.smake = smake
                        Masterinstrumentslist_listSaveUpdate.ldefaultlocationid = ldefaultlocationid
                        Masterinstrumentslist_listSaveUpdate.slocationname = slocationname
                        Masterinstrumentslist_listSaveUpdate.scurrentstatus = scurrentstatus
                        Masterinstrumentslist_listSaveUpdate.bcalib = bcalib
                        Masterinstrumentslist_listSaveUpdate.dtlastcalib = datetime.now()
                        Masterinstrumentslist_listSaveUpdate.dtnextcalib = datetime.now()
                        Masterinstrumentslist_listSaveUpdate.slastcalibdate = ""
                        Masterinstrumentslist_listSaveUpdate.snextcalibdate = ""
                        Masterinstrumentslist_listSaveUpdate.dtcalibdisplaydate = datetime.now()
                        Masterinstrumentslist_listSaveUpdate.ldueday = 0
                        Masterinstrumentslist_listSaveUpdate.lduemonth = 0
                        Masterinstrumentslist_listSaveUpdate.ldueyear = 0
                        Masterinstrumentslist_listSaveUpdate.sfreqtype = sfreqtype
                        Masterinstrumentslist_listSaveUpdate.busagewise = busagewise
                        Masterinstrumentslist_listSaveUpdate.lcalibrationvendorid = lcalibrationvendorid
                        Masterinstrumentslist_listSaveUpdate.scalibvendor = scalibvendor
                        Masterinstrumentslist_listSaveUpdate.bcheckin = 0
                        Masterinstrumentslist_listSaveUpdate.busage = busage
                        Masterinstrumentslist_listSaveUpdate.blimitedusage = 0
                        Masterinstrumentslist_listSaveUpdate.bdamaged = 0
                        Masterinstrumentslist_listSaveUpdate.battribute = battribute
                        Masterinstrumentslist_listSaveUpdate.bfreezecalib = 0
                        Masterinstrumentslist_listSaveUpdate.bvalidation = bvalidation
                        Masterinstrumentslist_listSaveUpdate.bsentforcalibration = 0
                        Masterinstrumentslist_listSaveUpdate.oldinstrument_id = ""
                        Masterinstrumentslist_listSaveUpdate.sinstrumentcode = sinstrumentcode
                        Masterinstrumentslist_listSaveUpdate.bpurchaseclosed = bpurchaseclosed
                        Masterinstrumentslist_listSaveUpdate.bidlecalibration = bidlecalibration
                        Masterinstrumentslist_listSaveUpdate.bsamplepartusage = bsamplepartusage
                        Masterinstrumentslist_listSaveUpdate.bregularpartusage = bregularpartusage
                        Masterinstrumentslist_listSaveUpdate.bcalibstandards = bcalibstandards
                        Masterinstrumentslist_listSaveUpdate.spartno = spartno
                        Masterinstrumentslist_listSaveUpdate.lcompanyid = lcompanyid
                        Masterinstrumentslist_listSaveUpdate.bplanned = bplanned
                        Masterinstrumentslist_listSaveUpdate.serpcode = serpcode
                        Masterinstrumentslist_listSaveUpdate.lhistorycard = 0
                        Masterinstrumentslist_listSaveUpdate.lfolowid1 = lfolowid1
                        Masterinstrumentslist_listSaveUpdate.lfolowid2 = lfolowid2
                        Masterinstrumentslist_listSaveUpdate.lfolowid3 = lfolowid3
                        Masterinstrumentslist_listSaveUpdate.lfolowid4 = lfolowid4
                        Masterinstrumentslist_listSaveUpdate.lfolowid5 = lfolowid5
                        Masterinstrumentslist_listSaveUpdate.ltolid = 0
                        Masterinstrumentslist_listSaveUpdate.sissueddate = ""
                        Masterinstrumentslist_listSaveUpdate.sreturneddate = ""
                        Masterinstrumentslist_listSaveUpdate.bsapcodegenerate = 1
                        Masterinstrumentslist_listSaveUpdate.bcalibrateidle = bcalibrateidle
                        Masterinstrumentslist_listSaveUpdate.scalibrationstartdate = ""
                        Masterinstrumentslist_listSaveUpdate.smsastartdate = ""
                        Masterinstrumentslist_listSaveUpdate.bshowlistascalibrate = 0
                        Masterinstrumentslist_listSaveUpdate.breferencegauge = 0 
                        Masterinstrumentslist_listSaveUpdate.scalibrationstartdate = "" 
                        Masterinstrumentslist_listSaveUpdate.svalidationstartdate = "" 
                        Masterinstrumentslist_listSaveUpdate.sdamagedon = ""
                        Masterinstrumentslist_listSaveUpdate.smissingon = ""
                        sinitiatedon = str(datetime.now())
                        sinitiatedon = sinitiatedon[8:10] + "-" + sinitiatedon[5:7] + "-" + sinitiatedon[0:4]
                        Masterinstrumentslist_listSaveUpdate.sinitiatedon = sinitiatedon
                        Masterinstrumentslist_listSaveUpdate.spurchaseon = ""
                        Masterinstrumentslist_listSaveUpdate.breferencegauge =0
                        Masterinstrumentslist_listSaveUpdate.slimitedcomment =""
                        Masterinstrumentslist_listSaveUpdate.ssize =""
                        Masterinstrumentslist_listSaveUpdate.size =""
                        Masterinstrumentslist_listSaveUpdate.ssizea =""
                        Masterinstrumentslist_listSaveUpdate.sissuedto =""
                        Masterinstrumentslist_listSaveUpdate.sissuedmachineto =""
                        Masterinstrumentslist_listSaveUpdate.sissuedpartno =""

                        Masterinstrumentslist_listSaveUpdate.save()


                        Masterinstrumentslistpart2SaveUpdate =  Masterinstrumentslistpart2.objects.get(lid =lInstIdA) 
 

 
                        if sstoragerack is None :
                            sstoragerack = ""
 
                        if sdrawingno is None :
                            sdrawingno = ""
 
                        if sdrawingrevno is None :
                            sdrawingrevno = ""
 
                        if sdrawingfile is None :
                            sdrawingfile = ""
 
                        if sunitofmeasure is None :
                            sunitofmeasure = ""
 
                        if srevisionno is None :
                            srevisionno = ""
 
                        if sproperty is None :
                            sproperty = ""
 
                        if scatalogueno is None :
                            scatalogueno = ""
 
                        if frangefrom is None :
                            frangefrom = 0
 
                        if frangeto is None :
                            frangeto = 0
 
                        if fleastcount is None :
                            fleastcount = 0
 
                        if scheckmethod is None :
                            scheckmethod = ""
 
                        if dtlastservice is None :
                            dtlastservice = datetime.now()
 
                        if dtnextservice is None :
                            dtnextservice = datetime.now()
 
                        if slastservicedate is None :
                            slastservicedate = ""
 
                        if snextservicedate is None :
                            snextservicedate = ""
 
                        if smanualduernr is None :
                            smanualduernr = ""
 
                        if ldayremainrnr is None :
                            ldayremainrnr = 0
 
                        if dtlastrnr is None :
                            dtlastrnr = datetime.now()
 
                        if dtnextrnr is None :
                            dtnextrnr = datetime.now()
 
                        if slastrnrdate is None :
                            slastrnrdate = ""
 
                        if snextrnrdate is None :
                            snextrnrdate = ""
 
                        if srange is None :
                            srange = ""
 
                        if frange3 is None :
                            frange3 = 0
 
                        if dcalibrationcost is None :
                            dcalibrationcost = 0
 
                        if dpurchaseprice is None :
                            dpurchaseprice = 0
 
                        if smodelno is None :
                            smodelno = ""
 
                        if sserialno is None :
                            sserialno = ""
 
                        if saccuracy is None :
                            saccuracy = ""
 
                        if scertificateno is None :
                            scertificateno = ""
 
                        if straceability is None :
                            straceability = ""
 
                        if ssize1 is None :
                            ssize1 = ""
 
                        if llusagedefault is None :
                            llusagedefault = 0
 
                        if llusagecount is None :
                            llusagecount = 0

                        smounted = Masterinstrumentslistpart2SaveUpdate.smounted
                        if smounted is None :
                            smounted = ""

                        fproducttolerance = Masterinstrumentslistpart2SaveUpdate.fproducttolerance
                        if fproducttolerance is None :
                            fproducttolerance = 0

                        sproducttolerance = Masterinstrumentslistpart2SaveUpdate.sproducttolerance
                        if sproducttolerance is None :
                            sproducttolerance = ""

                        facconstant = Masterinstrumentslistpart2SaveUpdate.facconstant
                        if facconstant is None :
                            facconstant = 0

                        sagencyservice = Masterinstrumentslistpart2SaveUpdate.sagencyservice
                        if sagencyservice is None :
                            sagencyservice = ""

                        sagencyservice = Masterinstrumentslistpart2SaveUpdate.sagencyservice
                        if sagencyservice is None :
                            sagencyservice = ""

                        sprocuredate = Masterinstrumentslistpart2SaveUpdate.sprocuredate
                        if sprocuredate is None :
                            sprocuredate = ""

                        brejected = Masterinstrumentslistpart2SaveUpdate.brejected
                        if brejected is None :
                            brejected = 0

                        srejecteddate = Masterinstrumentslistpart2SaveUpdate.srejecteddate
                        if srejecteddate is None :
                            srejecteddate = ""

                        breplaced = Masterinstrumentslistpart2SaveUpdate.breplaced
                        if breplaced is None :
                            breplaced = 0

                        lreplacedinstrumentid = Masterinstrumentslistpart2SaveUpdate.lreplacedinstrumentid
                        if lreplacedinstrumentid is None :
                            lreplacedinstrumentid = 0

                        bduechanged = Masterinstrumentslistpart2SaveUpdate.bduechanged
                        if bduechanged is None :
                            bduechanged = 0

                        dtduechangedate = Masterinstrumentslistpart2SaveUpdate.dtduechangedate
                        if dtduechangedate is None :
                            dtduechangedate = datetime.now()

                        slastchangedate = Masterinstrumentslistpart2SaveUpdate.slastchangedate
                        if slastchangedate is None :
                            slastchangedate = ""

                        blanova = Masterinstrumentslistpart2SaveUpdate.blanova
                        if blanova is None :
                            blanova = 0

                        srevno = Masterinstrumentslistpart2SaveUpdate.srevno
                        if srevno is None :
                            srevno = ""

                        scommentchangecalibstd = Masterinstrumentslistpart2SaveUpdate.scommentchangecalibstd
                        if scommentchangecalibstd is None :
                            scommentchangecalibstd = ""

                        bverifyforpurchase = Masterinstrumentslistpart2SaveUpdate.bverifyforpurchase
                        if bverifyforpurchase is None :
                            bverifyforpurchase = 0

                        dtsendforverificationforpurchaseon = Masterinstrumentslistpart2SaveUpdate.dtsendforverificationforpurchaseon
                        if dtsendforverificationforpurchaseon is None :
                            dtsendforverificationforpurchaseon = datetime.now()

                        dtverifiedforpurchaseon = Masterinstrumentslistpart2SaveUpdate.dtverifiedforpurchaseon
                        if dtverifiedforpurchaseon is None :
                            dtverifiedforpurchaseon = datetime.now()

                        ssendforverificationforpurchaseon = Masterinstrumentslistpart2SaveUpdate.ssendforverificationforpurchaseon
                        if ssendforverificationforpurchaseon is None :
                            ssendforverificationforpurchaseon = ""

                        sdateofprocure = Masterinstrumentslistpart2SaveUpdate.sdateofprocure
                        if sdateofprocure is None :
                            sdateofprocure = ""

                        spreferredvendor = Masterinstrumentslistpart2SaveUpdate.spreferredvendor
                        if spreferredvendor is None :
                            spreferredvendor = ""

                        sbondnumber = Masterinstrumentslistpart2SaveUpdate.sbondnumber
                        if sbondnumber is None :
                            sbondnumber = ""

                        dgo = Masterinstrumentslistpart2SaveUpdate.dgo
                        if dgo is None :
                            dgo = 0

                        dnogo = Masterinstrumentslistpart2SaveUpdate.dnogo
                        if dnogo is None :
                            dnogo = 0

                        dtoldiff = Masterinstrumentslistpart2SaveUpdate.dtoldiff
                        if dtoldiff is None :
                            dtoldiff = 0

                        dtolallowed = Masterinstrumentslistpart2SaveUpdate.dtolallowed
                        if dtolallowed is None :
                            dtolallowed = 0

                        bmanufacturingstd = Masterinstrumentslistpart2SaveUpdate.bmanufacturingstd
                        if bmanufacturingstd is None :
                            bmanufacturingstd = 0

                        dplusofminus = Masterinstrumentslistpart2SaveUpdate.dplusofminus
                        if dplusofminus is None :
                            dplusofminus = 0

                        dz = Masterinstrumentslistpart2SaveUpdate.dz
                        if dz is None :
                            dz = 0

                        bpartno = Masterinstrumentslistpart2SaveUpdate.bpartno
                        if bpartno is None :
                            bpartno = 0

                        gageserialno = Masterinstrumentslistpart2SaveUpdate.gageserialno
                        if gageserialno is None :
                            gageserialno = ""

                        sdrawingno2 = Masterinstrumentslistpart2SaveUpdate.sdrawingno2
                        if sdrawingno2 is None :
                            sdrawingno2 = ""

                        lcontinuousnoa2 = Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa2
                        if lcontinuousnoa2 is None :
                            lcontinuousnoa2 = 0

                        lcontinuousnob2 = Masterinstrumentslistpart2SaveUpdate.lcontinuousnob2
                        if lcontinuousnob2 is None :
                            lcontinuousnob2 = 0

                        lcategorytype1 = Masterinstrumentslistpart2SaveUpdate.lcategorytype1
                        if lcategorytype1 is None :
                            lcategorytype1 = 0

                        lcategorytype2 = Masterinstrumentslistpart2SaveUpdate.lcategorytype2
                        if lcategorytype2 is None :
                            lcategorytype2 = 0

                        bcustomer = Masterinstrumentslistpart2SaveUpdate.bcustomer
                        if bcustomer is None :
                            bcustomer = 0

                        lservicealert = Masterinstrumentslistpart2SaveUpdate.lservicealert
                        if lservicealert is None :
                            lservicealert = 0

                        ferrorallowed = Masterinstrumentslistpart2SaveUpdate.ferrorallowed
                        if ferrorallowed is None :
                            ferrorallowed = 0

                        splannedby = Masterinstrumentslistpart2SaveUpdate.splannedby
                        if splannedby is None :
                            splannedby = ""

                        bidchanged = Masterinstrumentslistpart2SaveUpdate.bidchanged
                        if bidchanged is None :
                            bidchanged = 0

                        scode1 = Masterinstrumentslistpart2SaveUpdate.scode1
                        if scode1 is None :
                            scode1 = ""

                        scode2 = Masterinstrumentslistpart2SaveUpdate.scode2
                        if scode2 is None :
                            scode2 = ""

                        scode3 = Masterinstrumentslistpart2SaveUpdate.scode3
                        if scode3 is None :
                            scode3 = ""

                        scode4 = Masterinstrumentslistpart2SaveUpdate.scode4
                        if scode4 is None :
                            scode4 = ""

                        scode5 = Masterinstrumentslistpart2SaveUpdate.scode5
                        if scode5 is None :
                            scode5 = ""

                        ssstatus = Masterinstrumentslistpart2SaveUpdate.ssstatus
                        if ssstatus is None :
                            ssstatus = ""

                        ssize = Masterinstrumentslistpart2SaveUpdate.ssize
                        if ssize is None :
                            ssize = ""

                        lintervalservice = Masterinstrumentslistpart2SaveUpdate.lintervalservice
                        if lintervalservice is None :
                            lintervalservice = 0

                        sintervalperiodservice = Masterinstrumentslistpart2SaveUpdate.sintervalperiodservice
                        if sintervalperiodservice is None :
                            sintervalperiodservice = ""

                        smanufacturer = Masterinstrumentslistpart2SaveUpdate.smanufacturer
                        if smanufacturer is None :
                            smanufacturer = ""

                        ddateofprocure = Masterinstrumentslistpart2SaveUpdate.ddateofprocure
                        if ddateofprocure is None :
                            ddateofprocure = datetime.now()

                        sdateofprocure = Masterinstrumentslistpart2SaveUpdate.sdateofprocure
                        if sdateofprocure is None :
                            sdateofprocure = ""

                        soperation = Masterinstrumentslistpart2SaveUpdate.soperation
                        if soperation is None :
                            soperation = ""

                        scompantname = Masterinstrumentslistpart2SaveUpdate.scompantname
                        if scompantname is None :
                            scompantname = ""

                        lcontinuousnoa1 = Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa1
                        if lcontinuousnoa1 is None :
                            lcontinuousnoa1 = 0

                        lcontinuousnob1 = Masterinstrumentslistpart2SaveUpdate.lcontinuousnob1
                        if lcontinuousnob1 is None :
                            lcontinuousnob1 = 0

                        lcontinuousnoa = Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa
                        if lcontinuousnoa is None :
                            lcontinuousnoa = 0

                        lcontinuousnob = Masterinstrumentslistpart2SaveUpdate.lcontinuousnob
                        if lcontinuousnob is None :
                            lcontinuousnob = 0

                        btyperef = Masterinstrumentslistpart2SaveUpdate.btyperef
                        if btyperef is None :
                            btyperef = 0

                        btyperefascontinuousnoa = Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnoa
                        if btyperefascontinuousnoa is None :
                            btyperefascontinuousnoa = 0

                        btyperefascontinuousnob = Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnob
                        if btyperefascontinuousnob is None :
                            btyperefascontinuousnob = 0

                        scomment = Masterinstrumentslistpart2SaveUpdate.scomment
                        if scomment is None :
                            scomment = ""

                        lpurchasevendorid = Masterinstrumentslistpart2SaveUpdate.lpurchasevendorid
                        if lpurchasevendorid is None :
                            lpurchasevendorid = 0

                        lservicevendorid = Masterinstrumentslistpart2SaveUpdate.lservicevendorid
                        if lservicevendorid is None :
                            lservicevendorid = 0

                        sagencycalib = Masterinstrumentslistpart2SaveUpdate.sagencycalib
                        if sagencycalib is None :
                            sagencycalib = ""

                        scode = Masterinstrumentslistpart2SaveUpdate.scode
                        if scode is None :
                            scode = ""

                        lcurrentlocationid = Masterinstrumentslistpart2SaveUpdate.lcurrentlocationid
                        if lcurrentlocationid is None :
                            lcurrentlocationid = 0

                        bservice = Masterinstrumentslistpart2SaveUpdate.bservice
                        if bservice is None :
                            bservice = 0
                        lcalibalert = Masterinstrumentslistpart2SaveUpdate.lcalibalert
                        if lcalibalert is None :
                            lcalibalert = 0
                        lintervalcalib = Masterinstrumentslistpart2SaveUpdate.lintervalcalib
                        if lintervalcalib is None :
                            lintervalcalib = 0
                        sintervalperiodcalib = Masterinstrumentslistpart2SaveUpdate.sintervalperiodcalib
                        if sintervalperiodcalib is None :
                            sintervalperiodcalib = ""
                        lalertinterval = Masterinstrumentslistpart2SaveUpdate.lalertinterval
                        if lalertinterval is None :
                            lalertinterval = 0
                        ldayremaincalib = Masterinstrumentslistpart2SaveUpdate.ldayremaincalib
                        if ldayremaincalib is None :
                            ldayremaincalib = 0
                        lusageinterval = Masterinstrumentslistpart2SaveUpdate.lusageinterval
                        if lusageinterval is None :
                            lusageinterval = 0
                        lusageintervaldisplay = Masterinstrumentslistpart2SaveUpdate.lusageintervaldisplay
                        if lusageintervaldisplay is None :
                            lusageintervaldisplay = 0
                        lusagecurrent = Masterinstrumentslistpart2SaveUpdate.lusagecurrent
                        if lusagecurrent is None :
                            lusagecurrent = 0
                        lidlecalibfrequency = Masterinstrumentslistpart2SaveUpdate.lidlecalibfrequency
                        if lidlecalibfrequency is None :
                            lidlecalibfrequency = 0
                        dtplanneddate = Masterinstrumentslistpart2SaveUpdate.dtplanneddate
                        if dtplanneddate is None :
                            dtplanneddate = datetime.now()
                        splanneddate = Masterinstrumentslistpart2SaveUpdate.splanneddate
                        if splanneddate is None :
                            splanneddate = ""
                        dtvalidationlastdate = Masterinstrumentslistpart2SaveUpdate.dtvalidationlastdate
                        if dtvalidationlastdate is None :
                            dtvalidationlastdate = datetime.now()
                        svalidationlastdate = Masterinstrumentslistpart2SaveUpdate.svalidationlastdate
                        if svalidationlastdate is None :
                            svalidationlastdate = ""
                        dtvalidationnextdate = Masterinstrumentslistpart2SaveUpdate.dtvalidationnextdate
                        if dtvalidationnextdate is None :
                            dtvalidationnextdate = datetime.now()
                        svalidationnextdate = Masterinstrumentslistpart2SaveUpdate.svalidationnextdate
                        if svalidationnextdate is None :
                            svalidationnextdate = ""
                        schangeoldid = Masterinstrumentslistpart2SaveUpdate.schangeoldid
                        if schangeoldid is None :
                            schangeoldid = ""
                        llusagecountalerts = Masterinstrumentslistpart2SaveUpdate.llusagecountalerts
                        if llusagecountalerts is None :
                            llusagecountalerts = 0
                        btnextidlecalibration = Masterinstrumentslistpart2SaveUpdate.btnextidlecalibration
                        if btnextidlecalibration is None :
                            btnextidlecalibration = datetime.now()
                        snextidlecalibration = Masterinstrumentslistpart2SaveUpdate.snextidlecalibration
                        if snextidlecalibration is None :
                            snextidlecalibration = ""
                        dtidleon = Masterinstrumentslistpart2SaveUpdate.dtidleon
                        if dtidleon is None :
                            dtidleon = datetime.now()
                        idleon = Masterinstrumentslistpart2SaveUpdate.sidleon
                        if sidleon is None :
                            sidleon = ""
                        b1monthvalidation = Masterinstrumentslistpart2SaveUpdate.b1monthvalidation
                        if b1monthvalidation is None :
                            b1monthvalidation = 0
                        dtnextvalidation = Masterinstrumentslistpart2SaveUpdate.dtnextvalidation
                        if dtnextvalidation is None :
                            dtnextvalidation = datetime.now()
                        snextvalidation = Masterinstrumentslistpart2SaveUpdate.snextvalidation
                        if snextvalidation is None :
                            snextvalidation = ""
                        dtlastvalidation = Masterinstrumentslistpart2SaveUpdate.dtlastvalidation
                        if dtlastvalidation is None :
                            dtlastvalidation = datetime.now()
                        slastvalidation = Masterinstrumentslistpart2SaveUpdate.slastvalidation
                        if slastvalidation is None :
                            slastvalidation = ""


                        Masterinstrumentslistpart2SaveUpdate.sstoragerack =sstoragerack
                        Masterinstrumentslistpart2SaveUpdate.sdrawingno = sdrawingno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingrevno = sdrawingrevno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingfile =sdrawingfile
                        Masterinstrumentslistpart2SaveUpdate.sunitofmeasure = sunitofmeasure
                        Masterinstrumentslistpart2SaveUpdate.srevisionno = srevisionno
                        Masterinstrumentslistpart2SaveUpdate.sproperty = sproperty
                        Masterinstrumentslistpart2SaveUpdate.scatalogueno = scatalogueno
                        Masterinstrumentslistpart2SaveUpdate.frangefrom = frangefrom
                        Masterinstrumentslistpart2SaveUpdate.frangeto = frangeto
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.fleastcount = fleastcount
                        Masterinstrumentslistpart2SaveUpdate.scheckmethod = scheckmethod
                        Masterinstrumentslistpart2SaveUpdate.dtlastservice = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.dtnextservice = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.slastservicedate = ""
                        Masterinstrumentslistpart2SaveUpdate.snextservicedate = ""
                        Masterinstrumentslistpart2SaveUpdate.smanualduernr = smanualduernr
                        Masterinstrumentslistpart2SaveUpdate.ldayremainrnr = 0
                        Masterinstrumentslistpart2SaveUpdate.dtlastrnr = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.dtnextrnr = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.slastrnrdate = ""
                        Masterinstrumentslistpart2SaveUpdate.snextrnrdate = ""
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.srange = srange
                        Masterinstrumentslistpart2SaveUpdate.frange3 = frange3
                        Masterinstrumentslistpart2SaveUpdate.dcalibrationcost = dcalibrationcost
                        Masterinstrumentslistpart2SaveUpdate.dpurchaseprice = dpurchaseprice
                        Masterinstrumentslistpart2SaveUpdate.smodelno = ""
                        Masterinstrumentslistpart2SaveUpdate.sserialno = ""
                        Masterinstrumentslistpart2SaveUpdate.saccuracy = saccuracy
                        Masterinstrumentslistpart2SaveUpdate.scertificateno = ""
                        Masterinstrumentslistpart2SaveUpdate.straceability = ""
                        Masterinstrumentslistpart2SaveUpdate.ssize1 =ssize1
                        Masterinstrumentslistpart2SaveUpdate.llusagedefault = llusagedefault
                        Masterinstrumentslistpart2SaveUpdate.llusagecount = llusagecount
                        Masterinstrumentslistpart2SaveUpdate.smounted = smounted
                        Masterinstrumentslistpart2SaveUpdate.fproducttolerance = fproducttolerance
                        Masterinstrumentslistpart2SaveUpdate.sproducttolerance = sproducttolerance
                        Masterinstrumentslistpart2SaveUpdate.facconstant = facconstant
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.sagencyservice = sagencyservice
                        Masterinstrumentslistpart2SaveUpdate.sprocuredate = ddateofprocure.strftime("%m/%d/%Y")
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.brejected = 0
                        Masterinstrumentslistpart2SaveUpdate.srejecteddate = ""
                        Masterinstrumentslistpart2SaveUpdate.breplaced = 0
                        Masterinstrumentslistpart2SaveUpdate.lreplacedinstrumentid = 0
                        Masterinstrumentslistpart2SaveUpdate.bduechanged = 0
                        Masterinstrumentslistpart2SaveUpdate.dtduechangedate = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.slastchangedate =  ""
                        Masterinstrumentslistpart2SaveUpdate.blanova = 0
                        Masterinstrumentslistpart2SaveUpdate.srevno = srevno
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.scommentchangecalibstd = scommentchangecalibstd
                        Masterinstrumentslistpart2SaveUpdate.bverifyforpurchase = 0
                        Masterinstrumentslistpart2SaveUpdate.dtsendforverificationforpurchaseon = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.dtverifiedforpurchaseon = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.ssendforverificationforpurchaseon = ""
                        Masterinstrumentslistpart2SaveUpdate.sverifiedforpurchaseon = ""
                        Masterinstrumentslistpart2SaveUpdate.spreferredvendor = spreferredvendor
                        Masterinstrumentslistpart2SaveUpdate.sbondnumber = sbondnumber
                        Masterinstrumentslistpart2SaveUpdate.dgo = dgo
                        Masterinstrumentslistpart2SaveUpdate.dnogo = dnogo
                        Masterinstrumentslistpart2SaveUpdate.dtoldiff = dtoldiff
                        Masterinstrumentslistpart2SaveUpdate.dtolallowed = dtolallowed
                        Masterinstrumentslistpart2SaveUpdate.bmanufacturingstd = bmanufacturingstd
                        Masterinstrumentslistpart2SaveUpdate.dplusofminus = dplusofminus
                        Masterinstrumentslistpart2SaveUpdate.dz = dz
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.bpartno =bpartno
                        Masterinstrumentslistpart2SaveUpdate.gageserialno = gageserialno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingno2 = sdrawingno2
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa2 = lcontinuousnoa2
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob2 = lcontinuousnob2
                        Masterinstrumentslistpart2SaveUpdate.lcategorytype1 = lcategorytype1
                        Masterinstrumentslistpart2SaveUpdate.lcategorytype2 = lcategorytype2
                        Masterinstrumentslistpart2SaveUpdate.bcustomer = bcustomer
                        Masterinstrumentslistpart2SaveUpdate.lservicealert = lservicealert
                        Masterinstrumentslistpart2SaveUpdate.ferrorallowed = ferrorallowed
                        Masterinstrumentslistpart2SaveUpdate.splannedby = request.session['semployeename'] 
                        Masterinstrumentslistpart2SaveUpdate.bidchanged = 0
                        Masterinstrumentslistpart2SaveUpdate.scode1 = scode1
                        Masterinstrumentslistpart2SaveUpdate.scode2 = scode2
                        Masterinstrumentslistpart2SaveUpdate.scode3 = scode3
                        Masterinstrumentslistpart2SaveUpdate.scode4 = scode4
                        Masterinstrumentslistpart2SaveUpdate.scode5 = scode5
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.ssstatus = scurrentstatus
                        Masterinstrumentslistpart2SaveUpdate.ssize = ssize
                        Masterinstrumentslistpart2SaveUpdate.lintervalservice = lintervalservice
                        Masterinstrumentslistpart2SaveUpdate.sintervalperiodservice = sintervalperiodservice
                        Masterinstrumentslistpart2SaveUpdate.smanufacturer = smanufacturer
                        Masterinstrumentslistpart2SaveUpdate.ddateofprocure = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.sdateofprocure = ""
                        Masterinstrumentslistpart2SaveUpdate.soperation = soperation
                        Masterinstrumentslistpart2SaveUpdate.scompantname = scompantname
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa1 = lcontinuousnoa1
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob1 = lcontinuousnob1
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa = lcontinuousnoa
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob = lcontinuousnob
                        Masterinstrumentslistpart2SaveUpdate.btyperef = btyperef
                        Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnoa = btyperefascontinuousnoa
                        Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnob = btyperefascontinuousnob
                        Masterinstrumentslistpart2SaveUpdate.scomment = ""
                        Masterinstrumentslistpart2SaveUpdate.lpurchasevendorid = lpurchasevendorid
                        Masterinstrumentslistpart2SaveUpdate.lservicevendorid = lservicevendorid
                        Masterinstrumentslistpart2SaveUpdate.sagencycalib = sagencycalib
                        Masterinstrumentslistpart2SaveUpdate.scode = scode
                        Masterinstrumentslistpart2SaveUpdate.lcurrentlocationid = lcurrentlocationid
                        Masterinstrumentslistpart2SaveUpdate.bservice = bservice
                        Masterinstrumentslistpart2SaveUpdate.lcalibalert = lcalibalert
                        Masterinstrumentslistpart2SaveUpdate.lintervalcalib = lintervalcalib
                        Masterinstrumentslistpart2SaveUpdate.sintervalperiodcalib = sintervalperiodcalib
                        Masterinstrumentslistpart2SaveUpdate.lalertinterval = lalertinterval
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.ldayremaincalib = 0
                        Masterinstrumentslistpart2SaveUpdate.lusageinterval = lusageinterval
                        Masterinstrumentslistpart2SaveUpdate.lusageintervaldisplay = lusageintervaldisplay
                        Masterinstrumentslistpart2SaveUpdate.lusagecurrent = 0
                        Masterinstrumentslistpart2SaveUpdate.lidlecalibfrequency = lidlecalibfrequency
                        Masterinstrumentslistpart2SaveUpdate.dtplanneddate = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.splanneddate = ""
                        Masterinstrumentslistpart2SaveUpdate.dtvalidationlastdate = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.svalidationlastdate = ""
                        Masterinstrumentslistpart2SaveUpdate.dtvalidationnextdate = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.svalidationnextdate = ""
                        Masterinstrumentslistpart2SaveUpdate.schangeoldid = ""
                        Masterinstrumentslistpart2SaveUpdate.llusagecountalerts = llusagecountalerts
                        Masterinstrumentslistpart2SaveUpdate.btnextidlecalibration = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.snextidlecalibration = ""
                        Masterinstrumentslistpart2SaveUpdate.dtidleon = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.sidleon = ""
                        Masterinstrumentslistpart2SaveUpdate.b1monthvalidation = b1monthvalidation
                        Masterinstrumentslistpart2SaveUpdate.dtnextvalidation = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.save()
                        Masterinstrumentslistpart2SaveUpdate.snextvalidation = ""
                        Masterinstrumentslistpart2SaveUpdate.dtlastvalidation = datetime.now()
                        Masterinstrumentslistpart2SaveUpdate.slastvalidation = ""
 
                        Masterinstrumentslistpart2SaveUpdate.sstoragerack = sstoragerack
                        Masterinstrumentslistpart2SaveUpdate.sdrawingno = sdrawingno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingrevno = sdrawingrevno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingfile = sdrawingfile
                        Masterinstrumentslistpart2SaveUpdate.sunitofmeasure = sunitofmeasure
                        Masterinstrumentslistpart2SaveUpdate.srevisionno = srevisionno
                        Masterinstrumentslistpart2SaveUpdate.sproperty = sproperty
                        Masterinstrumentslistpart2SaveUpdate.scatalogueno = scatalogueno
                        Masterinstrumentslistpart2SaveUpdate.frangefrom = frangefrom
                        Masterinstrumentslistpart2SaveUpdate.frangeto = frangeto
                        Masterinstrumentslistpart2SaveUpdate.fleastcount = fleastcount
                        Masterinstrumentslistpart2SaveUpdate.scheckmethod = scheckmethod
                        Masterinstrumentslistpart2SaveUpdate.dtlastservice = dtlastservice
                        Masterinstrumentslistpart2SaveUpdate.dtnextservice = dtnextservice
                        Masterinstrumentslistpart2SaveUpdate.slastservicedate = slastservicedate
                        Masterinstrumentslistpart2SaveUpdate.snextservicedate = snextservicedate
                        Masterinstrumentslistpart2SaveUpdate.smanualduernr = smanualduernr
                        Masterinstrumentslistpart2SaveUpdate.ldayremainrnr = ldayremainrnr
                        Masterinstrumentslistpart2SaveUpdate.dtlastrnr = dtlastrnr
                        Masterinstrumentslistpart2SaveUpdate.dtnextrnr = dtnextrnr
                        Masterinstrumentslistpart2SaveUpdate.slastrnrdate = slastrnrdate
                        Masterinstrumentslistpart2SaveUpdate.snextrnrdate = snextrnrdate
                        Masterinstrumentslistpart2SaveUpdate.srange = srange
                        Masterinstrumentslistpart2SaveUpdate.frange3 = frange3
                        Masterinstrumentslistpart2SaveUpdate.dcalibrationcost = dcalibrationcost
                        Masterinstrumentslistpart2SaveUpdate.dpurchaseprice = dpurchaseprice
                        Masterinstrumentslistpart2SaveUpdate.smodelno = smodelno
                        Masterinstrumentslistpart2SaveUpdate.sserialno = sserialno
                        Masterinstrumentslistpart2SaveUpdate.saccuracy = saccuracy
                        Masterinstrumentslistpart2SaveUpdate.scertificateno = scertificateno
                        Masterinstrumentslistpart2SaveUpdate.straceability = straceability
                        Masterinstrumentslistpart2SaveUpdate.ssize1 = ssize1
                        Masterinstrumentslistpart2SaveUpdate.llusagedefault = llusagedefault
                        Masterinstrumentslistpart2SaveUpdate.llusagecount = llusagecount
                        Masterinstrumentslistpart2SaveUpdate.smounted = smounted
                        Masterinstrumentslistpart2SaveUpdate.fproducttolerance = fproducttolerance
                        Masterinstrumentslistpart2SaveUpdate.sproducttolerance = sproducttolerance
                        Masterinstrumentslistpart2SaveUpdate.facconstant = facconstant
                        Masterinstrumentslistpart2SaveUpdate.sagencyservice = sagencyservice
                        Masterinstrumentslistpart2SaveUpdate.sprocuredate = sprocuredate
                        Masterinstrumentslistpart2SaveUpdate.brejected = brejected
                        Masterinstrumentslistpart2SaveUpdate.srejecteddate = srejecteddate
                        Masterinstrumentslistpart2SaveUpdate.breplaced = breplaced
                        Masterinstrumentslistpart2SaveUpdate.lreplacedinstrumentid = lreplacedinstrumentid
                        Masterinstrumentslistpart2SaveUpdate.bduechanged = bduechanged
                        Masterinstrumentslistpart2SaveUpdate.dtduechangedate = dtduechangedate
                        Masterinstrumentslistpart2SaveUpdate.slastchangedate = slastchangedate
                        Masterinstrumentslistpart2SaveUpdate.blanova = blanova
                        Masterinstrumentslistpart2SaveUpdate.srevno = srevno
                        Masterinstrumentslistpart2SaveUpdate.scommentchangecalibstd = scommentchangecalibstd
                        Masterinstrumentslistpart2SaveUpdate.bverifyforpurchase = bverifyforpurchase
                        Masterinstrumentslistpart2SaveUpdate.dtsendforverificationforpurchaseon = dtsendforverificationforpurchaseon
                        Masterinstrumentslistpart2SaveUpdate.dtverifiedforpurchaseon = dtverifiedforpurchaseon
                        Masterinstrumentslistpart2SaveUpdate.ssendforverificationforpurchaseon = ssendforverificationforpurchaseon
                        Masterinstrumentslistpart2SaveUpdate.sdateofprocure = sdateofprocure
                        Masterinstrumentslistpart2SaveUpdate.spreferredvendor = spreferredvendor
                        Masterinstrumentslistpart2SaveUpdate.sbondnumber = sbondnumber
                        Masterinstrumentslistpart2SaveUpdate.dgo = dgo
                        Masterinstrumentslistpart2SaveUpdate.dnogo = dnogo
                        Masterinstrumentslistpart2SaveUpdate.dtoldiff = dtoldiff
                        Masterinstrumentslistpart2SaveUpdate.dtolallowed = dtolallowed
                        Masterinstrumentslistpart2SaveUpdate.bmanufacturingstd = bmanufacturingstd
                        Masterinstrumentslistpart2SaveUpdate.dplusofminus = dplusofminus
                        Masterinstrumentslistpart2SaveUpdate.dz = dz
                        Masterinstrumentslistpart2SaveUpdate.bpartno = bpartno
                        Masterinstrumentslistpart2SaveUpdate.gageserialno = gageserialno
                        Masterinstrumentslistpart2SaveUpdate.sdrawingno2 = sdrawingno2
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa2 = lcontinuousnoa2
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob2 = lcontinuousnob2
                        Masterinstrumentslistpart2SaveUpdate.lcategorytype1 = lcategorytype1
                        Masterinstrumentslistpart2SaveUpdate.lcategorytype2 = lcategorytype2
                        Masterinstrumentslistpart2SaveUpdate.bcustomer = bcustomer
                        Masterinstrumentslistpart2SaveUpdate.lservicealert = lservicealert
                        Masterinstrumentslistpart2SaveUpdate.ferrorallowed = ferrorallowed
                        Masterinstrumentslistpart2SaveUpdate.splannedby = splannedby
                        Masterinstrumentslistpart2SaveUpdate.bidchanged = bidchanged
                        Masterinstrumentslistpart2SaveUpdate.scode1 = scode1
                        Masterinstrumentslistpart2SaveUpdate.scode2 = scode2
                        Masterinstrumentslistpart2SaveUpdate.scode3 = scode3
                        Masterinstrumentslistpart2SaveUpdate.scode4 = scode4
                        Masterinstrumentslistpart2SaveUpdate.scode5 = scode5
                        Masterinstrumentslistpart2SaveUpdate.ssstatus = ssstatus
                        Masterinstrumentslistpart2SaveUpdate.ssize = ssize
                        Masterinstrumentslistpart2SaveUpdate.lintervalservice = lintervalservice
                        Masterinstrumentslistpart2SaveUpdate.sintervalperiodservice = sintervalperiodservice
                        Masterinstrumentslistpart2SaveUpdate.smanufacturer = smanufacturer
                        Masterinstrumentslistpart2SaveUpdate.ddateofprocure = ddateofprocure
                        Masterinstrumentslistpart2SaveUpdate.sdateofprocure = sdateofprocure
                        Masterinstrumentslistpart2SaveUpdate.soperation = soperation
                        Masterinstrumentslistpart2SaveUpdate.scompantname = scompantname
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa1 = lcontinuousnoa1
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob1 = lcontinuousnob1
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa = lcontinuousnoa
                        Masterinstrumentslistpart2SaveUpdate.lcontinuousnob = lcontinuousnob
                        Masterinstrumentslistpart2SaveUpdate.btyperef = btyperef
                        Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnoa = btyperefascontinuousnoa
                        Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnob = btyperefascontinuousnob
                        Masterinstrumentslistpart2SaveUpdate.scomment = scomment
                        Masterinstrumentslistpart2SaveUpdate.lpurchasevendorid = lpurchasevendorid
                        Masterinstrumentslistpart2SaveUpdate.lservicevendorid = lservicevendorid
                        Masterinstrumentslistpart2SaveUpdate.sagencycalib = sagencycalib
                        Masterinstrumentslistpart2SaveUpdate.scode = scode
                        Masterinstrumentslistpart2SaveUpdate.lcurrentlocationid = lcurrentlocationid
                        Masterinstrumentslistpart2SaveUpdate.bservice = bservice
                        Masterinstrumentslistpart2SaveUpdate.lcalibalert = lcalibalert
                        Masterinstrumentslistpart2SaveUpdate.lintervalcalib = lintervalcalib
                        Masterinstrumentslistpart2SaveUpdate.sintervalperiodcalib = sintervalperiodcalib
                        Masterinstrumentslistpart2SaveUpdate.lalertinterval = lalertinterval
                        Masterinstrumentslistpart2SaveUpdate.ldayremaincalib = ldayremaincalib
                        Masterinstrumentslistpart2SaveUpdate.lusageinterval = lusageinterval
                        Masterinstrumentslistpart2SaveUpdate.lusageintervaldisplay = lusageintervaldisplay
                        Masterinstrumentslistpart2SaveUpdate.lusagecurrent = lusagecurrent
                        Masterinstrumentslistpart2SaveUpdate.lidlecalibfrequency = lidlecalibfrequency
                        Masterinstrumentslistpart2SaveUpdate.dtplanneddate = dtplanneddate
                        Masterinstrumentslistpart2SaveUpdate.splanneddate = splanneddate
                        Masterinstrumentslistpart2SaveUpdate.dtvalidationlastdate = dtvalidationlastdate
                        Masterinstrumentslistpart2SaveUpdate.svalidationlastdate = svalidationlastdate
                        Masterinstrumentslistpart2SaveUpdate.dtvalidationnextdate = dtvalidationnextdate
                        Masterinstrumentslistpart2SaveUpdate.svalidationnextdate = svalidationnextdate
                        Masterinstrumentslistpart2SaveUpdate.schangeoldid = schangeoldid
                        Masterinstrumentslistpart2SaveUpdate.llusagecountalerts = llusagecountalerts
                        Masterinstrumentslistpart2SaveUpdate.btnextidlecalibration = btnextidlecalibration
                        Masterinstrumentslistpart2SaveUpdate.snextidlecalibration = snextidlecalibration
                        Masterinstrumentslistpart2SaveUpdate.dtidleon = dtidleon
                        Masterinstrumentslistpart2SaveUpdate.sidleon = sidleon
                        Masterinstrumentslistpart2SaveUpdate.b1monthvalidation = b1monthvalidation
                        Masterinstrumentslistpart2SaveUpdate.dtnextvalidation = dtnextvalidation
                        Masterinstrumentslistpart2SaveUpdate.snextvalidation = snextvalidation
                        Masterinstrumentslistpart2SaveUpdate.dtlastvalidation = dtlastvalidation
                        Masterinstrumentslistpart2SaveUpdate.slastvalidation = slastvalidation


                        Masterinstrumentslistpart2SaveUpdate.save()
  
                        


 
 


                        sCreatedBy = ""

                        sCreatedBy = request.session['semployeename'] + " (" + request.session['semployeeno']  + ") "



                        sNewSAPCode = "NO"
                        if (bNewIDwithfirstSerial == 1):
                            sNewSAPCode = "YES"
                        
                        sCompanyName = ""
                        sCompanyName =   "Maini Group - " + sPlantNameName
                        #Admin1Companyinfo_list =  Admin1Companyinfo.objects.get(lid=1)
                        #if (Admin1C
                        request.session['sSAPCode']  = sNewSAPCode
                        #return render(request,  'CloudCaliber/GaugeMasterlistCreateIDPrint.html', 
                        #{
                            #'title':'User list', 
                            #'sCompanyName':sCompanyName, 
                            #'sPlantName':sPlantNameNameA, 
                            #'sPlantCode':sPlantCode[:2],
                            #'sAssetCode':  sCodeFinal1, 
                            #'sNewSAPCode':sNewSAPCode,
                            #'sCodeDescription':sCodeDescription,
                            #'sFlow1':sFlow1,
                            #'sFlow2':sFlow2,
                            #'sFlow3':sFlow3,
                            #'sFlow4':sFlow4,
                            #'sFlow5':sFlow5,
                            #'sFlowDesc1':sCodeFlow1.strip(),
                            #'sFlowDesc2':sCodeFlow2.strip(),
                            #'sFlowDesc3':sCodeFlow3.strip(),
                            #'sFlowDesc4':sCodeFlow4.strip(),
                            #'sFlowDesc5':sCodeFlow5.strip(),
                            #'sDate':datetime.now(),
                            #'sCreatedBy':sCreatedBy,
                        #}) 

                        #template = get_template('CloudCaliber/GaugeMasterlistCreateIDPrint.html')
                        context = {
                            'title':'Print New SAP Code', 
                            'sCompanyName':sCompanyName, 
                            'sPlantName':sPlantNameNameA, 
                            'sPlantCode':sPlantCode[:2],
                            'sAssetCode':  sCodeFinal1, 
                            'sNewSAPCode':sNewSAPCode,
                            'sCodeDescription':sCodeDescription,
                            'sFlow1':styperefnameA1,
                            'sFlow2':styperefnameA2,
                            'sFlow3':styperefnameA3,
                            'sFlow4':styperefnameA4,
                            'sFlow5':styperefnameA5,
                            'sFlowDesc1':sCodeFlow1.strip(),
                            'sFlowDesc2':sCodeFlow2.strip(),
                            'sFlowDesc3':sCodeFlow3.strip(),
                            'sFlowDesc4':sCodeFlow4.strip(),
                            'sFlowDesc5':sCodeFlow5.strip(),
                            'sDate':datetime.now(),
                            'sCreatedBy':sCreatedBy,
                        }
                        pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateIDPrint.html', context)
                        return HttpResponse(pdf, content_type='application/pdf')
                        html = template.render(context)
                        pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateIDPrint.html', context)
                        if pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')

                        filename = "GaugeSAPCode_" + sCodeFinal1 + str(ddateofprocure.day) + str(ddateofprocure.monthth) + str(ddateofprocure.year)  + ".pdf"  
                        content = "inline; filename='%s'" %(filename)
                        download = request.GET.get("download")
                        if download:
                            content = "attachment; filename='%s'" %(filename)
                            response['Content-Disposition'] = content
                            return response
                        return HttpResponse("Not found")



        data = request.POST
        if 'Classification' in request.POST:
            cmbClassificationID=request.POST['Classification'] 

        if 'Category' in request.POST:
            cmbCategoryID=request.POST['Category'] 

        if 'getFlow1' in request.POST:
            cmbgetFlow1ID=request.POST['getFlow1'] 


        #request.session['cmbClassificationID'] =cmbClassificationID
        #request.session['cmbCategoryID'] =cmbCategoryID
        #request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
        #request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
        #request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
        #request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
        #request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
        #request.session['cmbgetFlow6ID'] =cmbgetFlow6ID
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10
        
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10

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
  
        
        return render(request,  'CloudCaliber/GaugeMasterlistCreateID.html', 
        {
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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
        return render(request,  'CloudCaliber/GaugeMasterlistCreateID.html', 
        {
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
        })





 
@csrf_exempt
def GaugeMasterlistCreateOLDID(request,lID):
 
    lInstrumentID = lID

    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

    sCodeFinal1 = ""
    sCodeFinal2 = ""
    sLastDate = ""
    sNextDate = ""
    sLastDate1 = ""
    sNextDate1 = ""
    sLastDate2 = ""
    sNextDate2 = ""

    bcalibrateidle = 0
    bsapcodegenerate =0

    
    MasterinstrumentslistCheck = Masterinstrumentslist.objects.get(lid=lInstrumentID) 
    if MasterinstrumentslistCheck:
        sLastDate1 = MasterinstrumentslistCheck.slastcalibdate 
        sNextDate1 = MasterinstrumentslistCheck.snextcalibdate 
        bcalibrateidle = MasterinstrumentslistCheck.bcalibrateidle
        bsapcodegenerate = MasterinstrumentslistCheck.bsapcodegenerate
    
    date_time_Main = datetime.now()
    if (sLastDate2 == ""):
        sLastDate2 = datetime.strftime(date_time_Main, '%d-%m-%Y')
    if (sNextDate2 == ""):
        sNextDate2 = datetime.strftime(date_time_Main, '%d-%m-%Y')

    sLastDate2  = sLastDate1.split("/")
    sNextDate2  = sNextDate1.split("/")

    if(len(sLastDate2) > 1):
        sLastDate = sLastDate2[2] + "-" + sLastDate2[1] + "-" + sLastDate2[0]
    else:
        sLastDate2  = sLastDate1.split("-") 
        if(len(sLastDate2) > 1):
            sLastDate = sLastDate2[2] + "-" + sLastDate2[1] + "-" + sLastDate2[0] 
    
    if(len(sNextDate2) > 1):
        sNextDate = sNextDate2[2] + "-" + sNextDate2[1] + "-" + sNextDate2[0] 
    else:
        sNextDate2  = sNextDate1.split("-")
    
        if(len(sNextDate2) > 1):
            sNextDate = sNextDate2[2] + "-" + sNextDate2[1] + "-" + sNextDate2[0] 

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname'] 
    semployeename = request.session['semployeename']

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
    getFlow2Code = ""
    getFlow3Code = ""
    getFlow4Code = ""
    getFlow5Code = ""
    getFlowContCode = ""

    bContFlag = 0


    sPlantNameName = ""
    sPlantNameNameA = ""
    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
        sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
        sPlantNameNameA = AdminunitlistActive.splantname
 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode




    if request.method == "POST":

        data = request.POST

        lInstrumentID =0
        if 'txtID' in request.POST: 
            lInstrumentID = int(data.get('txtID'))


        txtLastCalibrationDate =0
        if 'txtLastCalibrationDate' in request.POST: 
            txtLastCalibrationDate = data.get('txtLastCalibrationDate')


            
        txtNextCalibrationDate =0
        if 'txtNextCalibrationDate' in request.POST: 
            txtNextCalibrationDate = data.get('txtNextCalibrationDate')


            
        bCalibrateWhenIdle =0
        if 'bCalibrateWhenIdle1' in request.POST: 
            bCalibrateWhenIdle = 1


        ID_Categories =0
        if 'Categories' in request.POST: 
            if(data.get('Categories').isnumeric()):
                ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            if(data.get('Classification').isnumeric()):
                ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            if(data.get('Flow1').isnumeric()):
                Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST: 
            if(data.get('Flow2').isnumeric()):
                Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST: 
            if(data.get('Flow3').isnumeric()):
                Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST:
            if(data.get('Flow4').isnumeric()):
                Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST: 
            if(data.get('Flow5').isnumeric()):
                Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST: 
            GaugeClass = int(data.get('GaugeClass'))

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('Dashboard')







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


            sCodeFinal1 = sClasscode
            sCodeFinal2 = sClasscode + " " + sPlantCode
         
            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': 0 ,  
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate, 
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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







            sCodeFinal1 = sClasscode + sCategoryCode
            sCodeFinal2 = sClasscode  + sCategoryCode + " " + sPlantCode
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })




            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })
            






        if 'cmbGetID' in request.POST:  
               
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
 
            Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_list:
                sCategoryCode = Adminassetcategorylist_list.scode
                sClasscode = Adminassetcategorylist_list.styperefname  
                styperefnameA1 = Adminassetcategorylist_list.styperefname1
                styperefnameA2 = Adminassetcategorylist_list.styperefname2
                styperefnameA3 = Adminassetcategorylist_list.styperefname3
                styperefnameA4 = Adminassetcategorylist_list.styperefname4
                styperefnameA5 = Adminassetcategorylist_list.styperefname5


            sCodeFlow1 = ""
            sCodeFlow2 = ""
            sCodeFlow3 = ""
            sCodeFlow4 = ""
            sCodeFlow5 = ""

            if(Flow1Data !=0):
                if (styperefnameA1 == "Part No"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Equipment"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Operation"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Material"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                else:
                    Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                    


            if(Flow2Data !=0):
                if (styperefnameA2 == "Part No"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Equipment"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Operation"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Material"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                else:
                    Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                    


            if(Flow3Data !=0):
                if (styperefnameA3 == "Part No"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Equipment"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Operation"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Material"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                else:
                    Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                 


            if(Flow4Data !=0):
                if (styperefnameA4 == "Part No"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Equipment"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Operation"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Material"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                else:
                    Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                 

            if(Flow5Data !=0):
                if (styperefnameA5 == "Part No"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Equipment"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Operation"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Material"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                else:
                    Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                 

            sContNo = ""
            sContNo1 = ""
            lContNo = 0
            lContNoVB = 0
            lContNoVBC = 0
        
            lassetidA =0

            sCategoryCode = "" 
            Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_listH:
                sCategoryCode = Adminassetcategorylist_listH.scode 
                sClasscode = Adminassetcategorylist_listH.styperefname 
                lassetidA = Adminassetcategorylist_listH.lassetid
                lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
        
 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')



            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
          

            AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
            if AdmincategoryidcontinuousnolistActivw:
                for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                    lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                    lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            else:
                lContNo  = lContNoVB
 

            if (lContNoVBC == 0 ):
                if (lassetidA == 6): 
                    
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0
            else:
                if (lassetidA == 6):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8):  
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0

 

            if(sContNo1 != ''):
                if(len(sContNo1) == 1):
                    sContNo = "000" + sContNo1
                elif(len(sContNo1) == 2):
                    sContNo = "00" + sContNo1
                elif(len(sContNo1) == 3):
                    sContNo = "0" + sContNo1
                else:
                    sContNo =  sContNo1

 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')


            sCodeFinal1 = ""
            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  #+  sContNo.strip()
        

            lSerialNo =0
            
            AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
            if AdminassetserialformatlistActive:
                for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                    lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


            lSerialNo = lSerialNo +1
 

            
            bNewIDwithfirstSerial = 0
            if (lSerialNo == 1):
                bNewIDwithfirstSerial = 1

 
            sSerialNo = ""
            sSerialNo1 = ""
            sSerialNo=str(lSerialNo)
            if (len(sSerialNo) == 1):
                sSerialNo1 = "00" + sSerialNo
            elif (len(sSerialNo) == 2):
                sSerialNo1 = "0" + sSerialNo 
            else:
                sSerialNo1 =   sSerialNo 


           # sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
            sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()    + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
             


    
 
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })


            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': Flow1Data ,  
            'cmbFlow2ID': Flow2Data ,  
            'cmbFlow3ID': Flow3Data ,  
            'cmbFlow4ID': Flow4Data ,
            'cmbFlow5ID': Flow5Data ,     
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })






        if 'cmbSaveAdd' in request.POST:  




            sGaugeClass = ""
            if (GaugeClass != 0):
                Admintoleranceclasslist_listGet =  Admintoleranceclasslist.objects.get(lid = GaugeClass)
                if (Admintoleranceclasslist_listGet):
                    sGaugeClass = Admintoleranceclasslist_listGet.stoleranceclass
                

             
            bFlag = 0

            sFlow1 = ""
            sFlow2 =  ""
            sFlow3 =  ""
            sFlow4 =  ""
            sFlow5 =  ""
            sFlowDesc1 = ""
            sFlowDesc2 =  ""
            sFlowDesc3 =  ""
            sFlowDesc4 =  ""
            sFlowDesc5 =  "" 
            sCategorytype = ""

            sAssetCategory = ""

            if (ClassificationData == 0):
                bFlag = 1
                messages.error(request, 'Asset Classification is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
            else :
                if (ID_Categories == 0):
                    bFlag = 1
                    messages.error(request, 'Asset Category is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
                else :

                    Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                    if Adminassetcategorylist_list:
                        sCategoryCode = Adminassetcategorylist_list.scode
                        sCategorytype = Adminassetcategorylist_list.categorytype
                        sClasscode = Adminassetcategorylist_list.styperefname
                        sAssetCategory = Adminassetcategorylist_list.assettype 
                        #request.session['sCategoryCode'] = Adminassetcategorylist_list.scode
                        #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                        #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                        #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                        #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                        #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                        #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                        styperefnameA1 = Adminassetcategorylist_list.styperefname1
                        styperefnameA2 = Adminassetcategorylist_list.styperefname2
                        styperefnameA3 = Adminassetcategorylist_list.styperefname3
                        styperefnameA4 = Adminassetcategorylist_list.styperefname4
                        styperefnameA5 = Adminassetcategorylist_list.styperefname5
                        sCodeDescA = Adminassetcategorylist_list.categorytype
                        sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                        sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                        sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                        sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                        sCodeDesc5 = Adminassetcategorylist_list.styperefname5
                

                    if( styperefnameA1 != ''):
                        if(Flow1Data == 0):
                            bFlag = 1
                            sFlow1Message = styperefnameA1 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow1Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA2 != ''):
                        if(Flow2Data == 0):
                            bFlag = 1
                            sFlow2Message = styperefnameA2 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow2Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })
                            
                    if( styperefnameA3 != ''):
                        if(Flow3Data == 0):
                            bFlag = 1
                            sFlow3Message = styperefnameA3 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow3Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if( styperefnameA4 != ''):
                        if(Flow4Data == 0):
                            bFlag = 1
                            sFlow4Message = styperefnameA4 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow4Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })
                            
                    if( styperefnameA5 != ''):
                        if(Flow5Data == 0):
                            bFlag = 1
                            sFlow5Message = styperefnameA5 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow5Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })


                    if (bFlag == 0):
                    
                        
                        sCodeDescription = ""
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
                        sCategoryDesc = ""
            
                        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_list:
                            sCategoryCode = Adminassetcategorylist_list.scode
                            sCategorytype = Adminassetcategorylist_list.categorytype
                            sClasscode = Adminassetcategorylist_list.styperefname
                            sAssetCategory = Adminassetcategorylist_list.assettype 
                            #['sCategoryCode'] = Adminassetcategorylist_list.scode
                            #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                            #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                            #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                            #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                            #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                            #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                            styperefnameA1 = Adminassetcategorylist_list.styperefname1
                            styperefnameA2 = Adminassetcategorylist_list.styperefname2
                            styperefnameA3 = Adminassetcategorylist_list.styperefname3
                            styperefnameA4 = Adminassetcategorylist_list.styperefname4
                            styperefnameA5 = Adminassetcategorylist_list.styperefname5
                            sCodeDescA = Adminassetcategorylist_list.categorytype
                            sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                            sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                            sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                            sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                            sCodeDesc5 = Adminassetcategorylist_list.styperefname5

                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   

                        sCategoryDesc = sCategorytype
                        sCodeFlow1 = ""
                        sCodeFlow2 = ""
                        sCodeFlow3 = ""
                        sCodeFlow4 = ""
                        sCodeFlow5 = ""

                        if(Flow1Data !=0):
                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                                


                        if(Flow2Data !=0):
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                                


                        if(Flow3Data !=0):
                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                            


                        if(Flow4Data !=0):
                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                            

                        if(Flow5Data !=0):
                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                            
 
                        sCodeDesc1 = sCodeFlow1
                        sCodeDesc2 = sCodeFlow2
                        sCodeDesc3 = sCodeFlow3
                        sCodeDesc4 = sCodeFlow4
                        sCodeDesc5 = sCodeFlow5
                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   
                        sContNo = ""
                        sContNo1 = ""
                        lContNo = 0
                        lContNoVB = 0
                        lContNoVBC = 0
                    
                        lassetidA =0

                        sCategoryCode = "" 
                        Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_listH:
                            sCategoryCode = Adminassetcategorylist_listH.scode 
                            sClasscode = Adminassetcategorylist_listH.styperefname 
                            lassetidA = Adminassetcategorylist_listH.lassetid
                            lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
                    
                        
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')

                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
                    
                        sCodeFinal1AK = sCodeFinal1

                        AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
                        if AdmincategoryidcontinuousnolistActivw:
                            for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                                lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                                lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                        else:
                            lContNo  = lContNoVB
            

                        if (lContNoVBC == 0 ):
                            if (lassetidA == 6): 
                                
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0
                        else:
                            if (lassetidA == 6):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8):  
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0

            

                        if(sContNo1 != ''):
                            if(len(sContNo1) == 1):
                                sContNo = "000" + sContNo1
                            elif(len(sContNo1) == 2):
                                sContNo = "00" + sContNo1
                            elif(len(sContNo1) == 3):
                                sContNo = "0" + sContNo1
                            else:
                                sContNo =  sContNo1


                        
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')


                        sCodeFinal1 = ""
                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  #+  sContNo.strip()
                    

                        lSerialNo =0
                        
                        AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
                        if AdminassetserialformatlistActive:
                            for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                                lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


                        lSerialNo = lSerialNo +1
            

                        
                        bNewIDwithfirstSerial = 0
                        if (lSerialNo == 1):
                            bNewIDwithfirstSerial = 1

            
                        sSerialNo = ""
                        sSerialNo1 = ""
                        sSerialNo=str(lSerialNo)
                        if (len(sSerialNo) == 1):
                            sSerialNo1 = "00" + sSerialNo
                        elif (len(sSerialNo) == 2):
                            sSerialNo1 = "0" + sSerialNo 
                        else:
                            sSerialNo1 =   sSerialNo 


                       # sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
                    
                    
                        sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()   + "-" + sPlantCode[:2] + sSerialNo1.strip()
                 


                        if(lContNoVBC == 1): 
                                Adminassetserialformatlistsave = Admincategoryidcontinuousnolist(scode =sCodeFinal1AK, lserialno=lContNo)
                                Adminassetserialformatlistsave.save()
                                
                                AdminassetcategorylistGet =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories)
                                 

                                Adminassetcategorylistsave =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                                Adminassetcategorylistsave.lcontinuousnoa  =lContNo
                                Adminassetcategorylistsave.save()
 


                        if (lSerialNo == 1):
                            Adminassetserialformatlistsave = Adminassetserialformatlist(scode =sCodeFinal1, lserialno=lSerialNo)
                            Adminassetserialformatlistsave.save()
                        else:         
                            AdminassetserialformatlistGet =  Adminassetserialformatlist.objects.filter(scode = sCodeFinal1).values()
                            lIDCodeABC =0
                            if AdminassetserialformatlistGet:
                                for AdminassetserialformatlistGetOBJ in AdminassetserialformatlistGet.all():
                                    lIDCodeABC = AdminassetserialformatlistGetOBJ['lid']

                            Adminassetserialformatlistsave =  Adminassetserialformatlist.objects.get(lid = lIDCodeABC) 
                            Adminassetserialformatlistsave.lserialno =lSerialNo
                            Adminassetserialformatlistsave.save()

 


   
                        lid = 0
                        sinstrumentid = sCodeFinal2
                        sdescription = sCategoryDesc
                        sassettype = sAssetCategory
                        lplantid = lPlantId
                        splanttype = sPlantName
                        lcategoryid = ID_Categories
                        categorytype = sCategorytype
                        assettype = sAssetCategory
                        lassetid = ClassificationData
                        btyperef1 = 0
                        if (styperefnameA1 != ''):
                            btyperef1 = 1
                        scategorytype1 = styperefnameA1
                        styperefname1 = sCodeFlow1
                        btyperef2 = 0
                        if (styperefnameA2 != ''):
                            btyperef2 = 1
                        scategorytype2 = styperefnameA2
                        styperefname2 = sCodeFlow2
                        btyperef3 = 0
                        if (styperefnameA3 != ''):
                            btyperef3 = 1
                        scategorytype3 = styperefnameA3
                        styperefname3 = sCodeFlow3
                        btyperef4 = 0
                        if (styperefnameA4 != ''):
                            btyperef4 = 1
                        scategorytype4 =styperefnameA4
                        styperefname4 = sCodeFlow4
                        btyperef5 = 0
                        if (styperefnameA5 != ''):
                            btyperef5 = 1
                        scategorytype5 = styperefnameA5
                        styperefname5 = sCodeFlow5
                        smake = ""
                        ldefaultlocationid = 0
                        slocationname = ""
                        scurrentstatus = "PURCHASE INITIATED"
                        bcalib = 0
                        dtlastcalib = datetime.now()
                        dtnextcalib = datetime.now()
                        slastcalibdate = ""
                        snextcalibdate = ""

                        slastcalibdate1 = ""
                        snextcalibdate1 = ""
                        slastcalibdate1 = txtLastCalibrationDate
                        snextcalibdate1 = txtNextCalibrationDate
                        slastcalibdate2 = ""
                        snextcalibdate2 = ""


                        date_time_Main = datetime.now()
                        # if (slastcalibdate1 == ""):
                        #     slastcalibdate1 = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # if (snextcalibdate1 == ""):
                        #     snextcalibdate1 = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        
                        # slastcalibdate2  = slastcalibdate1.split("-")
                        # snextcalibdate2  = snextcalibdate1.split("-")

                        # slastcalibdate = slastcalibdate2[2] + "-" + slastcalibdate2[1] + "-" + slastcalibdate2[0] 
                        # snextcalibdate = snextcalibdate2[2] + "-" + snextcalibdate2[1] + "-" + snextcalibdate2[0] 

                        # slastcalibdate = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # slastcalibdate = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # dtlastcalib = datetime.strptime(slastcalibdate, '%d-%m-%Y').date()
                        # dtnextcalib = datetime.strptime(snextcalibdate, '%d-%m-%Y').date()


                        dtcalibdisplaydate = datetime.now()

                        sStatusIdle = "IDLE"

                        ldueday = 0
                        lduemonth = 0
                        ldueyear = 0
                        sfreqtype = ""
                        busagewise = 0
                        lcalibrationvendorid = 0
                        scalibvendor = ""
                        bcheckin = 0
                        busage = 0
                        blimitedusage = 0
                        bdamaged = 0
                        battribute = 0
                        bfreezecalib = 0
                        bvalidation = 0
                        bsentforcalibration = 0
                        oldinstrument_id = ""
                        sinstrumentcode = sCodeFinal2
                        bpurchaseclosed = 0
                        bidlecalibration = 0
                        bsamplepartusage = 0
                        bregularpartusage = 0
                        bcalibstandards = 0
                        spartno = ""
                        lcompanyid = lcompanyid
                        bplanned = 1
                        serpcode = sCodeFinal1
                        lhistorycard = 0
                        lfolowid1 = Flow1Data
                        lfolowid2 = Flow2Data
                        lfolowid3 = Flow3Data
                        lfolowid4 = Flow4Data
                        lfolowid5 = Flow5Data



                        sstoragerack = ""
                        sdrawingno = ""
                        sdrawingrevno = ""
                        sdrawingfile = ""
                        sunitofmeasure = ""
                        srevisionno = ""
                        sproperty = ""
                        scatalogueno = ""
                        frangefrom = 0
                        frangeto = 0
                        fleastcount = 0
                        scheckmethod = ""
                        dtlastservice = datetime.now()
                        dtnextservice = datetime.now()


                        slastservicedate = ""
                        snextservicedate = ""

                        slastservicedate1 = ""
                        snextservicedate1 = ""
                        slastservicedate2 = ""
                        snextservicedate2 = ""


                        slastservicedate = ""
                        snextservicedate = ""
                        smanualduernr = ""
                        ldayremainrnr = 0
                        dtlastrnr = datetime.now()
                        dtnextrnr = datetime.now()
                        slastrnrdate = ""
                        snextrnrdate = ""

                        slastrnrdate1 = ""
                        snextrnrdate1 = ""
                        slastrnrdate2 = ""
                        snextrnrdate2 = ""

                        



                        srange = ""
                        frange3 = 0
                        dcalibrationcost = 0
                        dpurchaseprice = 0
                        smodelno = ""
                        sserialno = ""
                        saccuracy = ""
                        scertificateno = ""
                        straceability = ""
                        ssize1 = ""
                        llusagedefault = 0
                        llusagecount = 0
                        smounted = ""
                        fproducttolerance = 0
                        sproducttolerance = 0
                        facconstant = 0
                        sagencyservice = ""
                        sprocuredate = ""
                        brejected = 0
                        srejecteddate = ""
                        breplaced = 0
                        lreplacedinstrumentid = 0
                        bduechanged = 0
                        dtduechangedate = datetime.now()
                        slastchangedate = datetime.now()
                        blanova = 0
                        srevno = ""
                        scommentchangecalibstd = ""
                        bverifyforpurchase = 0
                        dtsendforverificationforpurchaseon = datetime.now()
                        dtverifiedforpurchaseon = datetime.now()
                        ssendforverificationforpurchaseon = ""
                        sverifiedforpurchaseon = ""
                        spreferredvendor = ""
                        sbondnumber = ""
                        dgo = 0
                        dnogo = 0
                        dtoldiff = 0
                        dtolallowed = 0
                        bmanufacturingstd = 0
                        dplusofminus = 0
                        dz = 0
                        bpartno = 0
                        gageserialno = ""
                        sdrawingno2 = ""
                        lcontinuousnoa2 = 0
                        lcontinuousnob2 = 0
                        lcategorytype1 = 0
                        lcategorytype2 = 0
                        bcustomer = 0
                        lservicealert = 0
                        ferrorallowed = 0
                        splannedby = ""
                        bidchanged = 0
                        scode1 = sCategoryCode
                        scode2 = sGaugeClass
                        scode3 = ""
                        scode4 = ""
                        scode5 = ""
                        ssstatus = ""
                        ssize = ""
                        lintervalservice = 0
                        sintervalperiodservice = ""
                        smanufacturer = ""
                        ddateofprocure = datetime.now()
                        sdateofprocure = ""
                        soperation = ""
                        scompantname = ""
                        lcontinuousnoa1 = 0
                        lcontinuousnob1 = 0
                        lcontinuousnoa = 0
                        lcontinuousnob = 0
                        btyperef = 0
                        btyperefascontinuousnoa = 0
                        btyperefascontinuousnob = 0
                        scomment = ""
                        lpurchasevendorid = 0
                        lservicevendorid = 0
                        sagencycalib = ""
                        scode = sCategoryCode
                        lcurrentlocationid = 0
                        bservice = 0
                        lcalibalert = 0
                        lintervalcalib = 0
                        sintervalperiodcalib = ""
                        lalertinterval = 0
                        ldayremaincalib = 0
                        lusageinterval = 0
                        lusageintervaldisplay = 0
                        lusagecurrent = 0
                        lidlecalibfrequency = 0
                        dtplanneddate = datetime.now()
                        splanneddate = ""
                        dtvalidationlastdate = datetime.now()
                        svalidationlastdate = ""
                        dtvalidationnextdate = datetime.now()
                        svalidationnextdate = ""
                        schangeoldid = ""
                        llusagecountalerts = 0
                        btnextidlecalibration = datetime.now()
                        snextidlecalibration = ""
                        dtidleon = datetime.now()
                        sidleon = ""
                        b1monthvalidation = 0
                        dtnextvalidation = datetime.now()
                        snextvalidation = ""
                        dtlastvalidation = datetime.now()
                        slastvalidation = ""

                        lidA = 0


                         
                        # MasterinstrumentslistSave = Masterinstrumentslist(sinstrumentid  = sinstrumentid )
                        # MasterinstrumentslistSave.save() 
                    
                        # lInstId =0
                        # lInstId = MasterinstrumentslistSave.lid
                    
                        # Masterinstrumentslistpart2Save = Masterinstrumentslistpart2(linstrumentid  = lInstId )
                        # Masterinstrumentslistpart2Save.save()
                   
                        lInstIdA =0
                        lInstIdA = lInstrumentID
                        lInstIdB =0

                        # Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.filter(lcategoryid =ID_Categories).order_by('lid')[:1]
                        # #Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.filter(lcategoryid =ID_Categories).order_by('-lid')[:1]
                        # if Masterinstrumentslist_listcOPY:
                        #     for Masterinstrumentslist_listcOPY in Masterinstrumentslist_listcOPY.all():  
                        #         lInstIdB =Masterinstrumentslist_listcOPY.lid 
                        #         sdescription = Masterinstrumentslist_listcOPY.sdescription
                        #         smake = Masterinstrumentslist_listcOPY.smake
                        #         ldefaultlocationid  = Masterinstrumentslist_listcOPY.ldefaultlocationid
                        #         slocationname  = Masterinstrumentslist_listcOPY.slocationname 
                        #         bcalib = Masterinstrumentslist_listcOPY.bcalib   
                        #         sfreqtype = Masterinstrumentslist_listcOPY.sfreqtype
                        #         busagewise = Masterinstrumentslist_listcOPY.busagewise
                        #         lcalibrationvendorid = Masterinstrumentslist_listcOPY.lcalibrationvendorid
                        #         scalibvendor = Masterinstrumentslist_listcOPY.scalibvendor 
                        #         busage = Masterinstrumentslist_listcOPY.busage  
                        #         battribute = Masterinstrumentslist_listcOPY.battribute 
                        #         bvalidation = Masterinstrumentslist_listcOPY.bvalidation   
                        #         bidlecalibration = Masterinstrumentslist_listcOPY.bidlecalibration   
                        #         bsamplepartusage = Masterinstrumentslist_listcOPY.bsamplepartusage   
                        #         bregularpartusage = Masterinstrumentslist_listcOPY.bregularpartusage   
                        #         bcalibstandards = Masterinstrumentslist_listcOPY.bcalibstandards   
                        #         spartno = Masterinstrumentslist_listcOPY.spartno   

                        # Masterinstrumentslist_listcOPY2 =  Masterinstrumentslistpart2.objects.filter(linstrumentid =lInstIdB)
                        # if Masterinstrumentslist_listcOPY2:
                        #     for Masterinstrumentslist_listcOPY2 in Masterinstrumentslist_listcOPY2.all():  
                        #         sstoragerack = Masterinstrumentslist_listcOPY2.sstoragerack 
                        #         sdrawingno = Masterinstrumentslist_listcOPY2.sdrawingno 
                        #         sdrawingrevno = Masterinstrumentslist_listcOPY2.sdrawingrevno 
                        #         sdrawingfile = Masterinstrumentslist_listcOPY2.sdrawingfile 
                        #         sunitofmeasure = Masterinstrumentslist_listcOPY2.sunitofmeasure 
                        #         srevisionno = Masterinstrumentslist_listcOPY2.srevisionno 
                        #         sproperty = Masterinstrumentslist_listcOPY2.sproperty 
                        #         scatalogueno = Masterinstrumentslist_listcOPY2.scatalogueno 
                        #         frangefrom = Masterinstrumentslist_listcOPY2.frangefrom 
                        #         frangeto = Masterinstrumentslist_listcOPY2.frangeto 
                        #         fleastcount = Masterinstrumentslist_listcOPY2.fleastcount 
                        #         scheckmethod = Masterinstrumentslist_listcOPY2.scheckmethod  
                        #         smanualduernr = Masterinstrumentslist_listcOPY2.smanualduernr 
                        #         ldayremainrnr = Masterinstrumentslist_listcOPY2.ldayremainrnr  
                        #         srange = Masterinstrumentslist_listcOPY2.srange 
                        #         frange3 = Masterinstrumentslist_listcOPY2.frange3 
                        #         dcalibrationcost = Masterinstrumentslist_listcOPY2.dcalibrationcost 
                        #         dpurchaseprice = Masterinstrumentslist_listcOPY2.dpurchaseprice 
                                
                        #         saccuracy = Masterinstrumentslist_listcOPY2.saccuracy   
                        #         ssize1 = Masterinstrumentslist_listcOPY2.ssize1 
                        #         llusagedefault = Masterinstrumentslist_listcOPY2.llusagedefault  
                        #         smounted = Masterinstrumentslist_listcOPY2.smounted 
                        #         fproducttolerance = Masterinstrumentslist_listcOPY2.fproducttolerance 
                        #         sproducttolerance = Masterinstrumentslist_listcOPY2.sproducttolerance 
                        #         facconstant = Masterinstrumentslist_listcOPY2.facconstant 
                        #         sagencyservice = Masterinstrumentslist_listcOPY2.sagencyservice 
                                 
                        #         srevno = Masterinstrumentslist_listcOPY2.srevno  
                        #         spreferredvendor = Masterinstrumentslist_listcOPY2.spreferredvendor 
                        #         sbondnumber = Masterinstrumentslist_listcOPY2.sbondnumber 
                        #         dgo = Masterinstrumentslist_listcOPY2.dgo 
                        #         dnogo = Masterinstrumentslist_listcOPY2.dnogo 
                        #         dtoldiff = Masterinstrumentslist_listcOPY2.dtoldiff 
                        #         dtolallowed = Masterinstrumentslist_listcOPY2.dtolallowed 
                        #         bmanufacturingstd = Masterinstrumentslist_listcOPY2.bmanufacturingstd 
                        #         dplusofminus = Masterinstrumentslist_listcOPY2.dplusofminus 
                        #         dz = Masterinstrumentslist_listcOPY2.dz 
                                
                        #         sdrawingno2 = Masterinstrumentslist_listcOPY2.sdrawingno2   
                        #         ferrorallowed = Masterinstrumentslist_listcOPY2.ferrorallowed 
                        #         splannedby = Masterinstrumentslist_listcOPY2.splannedby   
                        #         ssize = Masterinstrumentslist_listcOPY2.ssize  
                        #         smanufacturer = Masterinstrumentslist_listcOPY2.smanufacturer       
                        #         lpurchasevendorid = Masterinstrumentslist_listcOPY2.lpurchasevendorid 
                        #         lservicevendorid = Masterinstrumentslist_listcOPY2.lservicevendorid 
                        #         sagencycalib = Masterinstrumentslist_listcOPY2.sagencycalib  
                        #         lcalibalert = Masterinstrumentslist_listcOPY2.lcalibalert 
                        #         lintervalcalib = Masterinstrumentslist_listcOPY2.lintervalcalib 
                        #         sintervalperiodcalib = Masterinstrumentslist_listcOPY2.sintervalperiodcalib 
                        #         lalertinterval = Masterinstrumentslist_listcOPY2.lalertinterval  
                        #         lusageinterval = Masterinstrumentslist_listcOPY2.lusageinterval 
                        #         lusageintervaldisplay = Masterinstrumentslist_listcOPY2.lusageintervaldisplay  
                        #         lidlecalibfrequency = Masterinstrumentslist_listcOPY2.lidlecalibfrequency   
                        #         llusagecountalerts = Masterinstrumentslist_listcOPY2.llusagecountalerts  
                        #         b1monthvalidation = Masterinstrumentslist_listcOPY2.b1monthvalidation  



                        Masterinstrumentslist_listSaveUpdate =  Masterinstrumentslist.objects.get(lid =lInstrumentID) 
                    

                        Masterinstrumentslist_listSaveUpdate.sinstrumentid = sCodeFinal2
                        Masterinstrumentslist_listSaveUpdate.sdescription = sdescription
                        Masterinstrumentslist_listSaveUpdate.sassettype = sAssetCategory
                        # Masterinstrumentslist_listSaveUpdate.lplantid = lPlantId
                        # Masterinstrumentslist_listSaveUpdate.splanttype = sPlantName
                        Masterinstrumentslist_listSaveUpdate.lcategoryid = ID_Categories
                        Masterinstrumentslist_listSaveUpdate.categorytype = sCategorytype
                        Masterinstrumentslist_listSaveUpdate.assettype = sAssetCategory
                        Masterinstrumentslist_listSaveUpdate.lassetid = ClassificationData
                        Masterinstrumentslist_listSaveUpdate.btyperef1 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype1 = styperefnameA1
                        Masterinstrumentslist_listSaveUpdate.styperefname1 = sCodeFlow1
                        Masterinstrumentslist_listSaveUpdate.btyperef2 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype2 = styperefnameA2
                        Masterinstrumentslist_listSaveUpdate.styperefname2 = sCodeFlow2
                        Masterinstrumentslist_listSaveUpdate.btyperef3 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype3 = styperefnameA3
                        Masterinstrumentslist_listSaveUpdate.styperefname3 = sCodeFlow3
                        Masterinstrumentslist_listSaveUpdate.btyperef4 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype4 =styperefnameA4
                        Masterinstrumentslist_listSaveUpdate.styperefname4 = sCodeFlow4
                        Masterinstrumentslist_listSaveUpdate.btyperef5 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype5 = styperefnameA5
                        Masterinstrumentslist_listSaveUpdate.styperefname5 = sCodeFlow5
                        # Masterinstrumentslist_listSaveUpdate.smake = smake
                        # Masterinstrumentslist_listSaveUpdate.ldefaultlocationid = ldefaultlocationid
                        # Masterinstrumentslist_listSaveUpdate.slocationname = slocationname
                        Masterinstrumentslist_listSaveUpdate.scurrentstatus = sStatusIdle
                        # Masterinstrumentslist_listSaveUpdate.bcalib = bcalib
                        Masterinstrumentslist_listSaveUpdate.dtlastcalib = dtlastcalib
                        Masterinstrumentslist_listSaveUpdate.dtnextcalib = dtnextcalib
                        Masterinstrumentslist_listSaveUpdate.slastcalibdate = slastcalibdate
                        Masterinstrumentslist_listSaveUpdate.snextcalibdate = snextcalibdate
                        Masterinstrumentslist_listSaveUpdate.dtcalibdisplaydate = dtnextcalib  + timedelta(days=15)
                        Masterinstrumentslist_listSaveUpdate.ldueday = dtnextcalib.day
                        Masterinstrumentslist_listSaveUpdate.lduemonth = dtnextcalib.month
                        Masterinstrumentslist_listSaveUpdate.ldueyear = dtnextcalib.year
                        # Masterinstrumentslist_listSaveUpdate.sfreqtype = sfreqtype
                        # Masterinstrumentslist_listSaveUpdate.busagewise = busagewise
                        # Masterinstrumentslist_listSaveUpdate.lcalibrationvendorid = lcalibrationvendorid
                        # Masterinstrumentslist_listSaveUpdate.scalibvendor = scalibvendor
                        # Masterinstrumentslist_listSaveUpdate.bcheckin = 0
                        # Masterinstrumentslist_listSaveUpdate.busage = busage
                        # Masterinstrumentslist_listSaveUpdate.blimitedusage = 0
                        # Masterinstrumentslist_listSaveUpdate.bdamaged = 0
                        # Masterinstrumentslist_listSaveUpdate.battribute = battribute
                        # Masterinstrumentslist_listSaveUpdate.bfreezecalib = 0
                        # Masterinstrumentslist_listSaveUpdate.bvalidation = bvalidation
                        # Masterinstrumentslist_listSaveUpdate.bsentforcalibration = 0
                        # Masterinstrumentslist_listSaveUpdate.oldinstrument_id = ""
                        Masterinstrumentslist_listSaveUpdate.sinstrumentcode = sinstrumentcode
                        Masterinstrumentslist_listSaveUpdate.bpurchaseclosed = bpurchaseclosed
                        Masterinstrumentslist_listSaveUpdate.bsapcodegenerate = 1

                        Masterinstrumentslist_listSaveUpdate.bidlecalibration = 0
                        Masterinstrumentslist_listSaveUpdate.bcalibrateidle = 0
                        if(bCalibrateWhenIdle == 1):
                            Masterinstrumentslist_listSaveUpdate.bidlecalibration = 1
                            Masterinstrumentslist_listSaveUpdate.bcalibrateidle = 1
                        # Masterinstrumentslist_listSaveUpdate.bsamplepartusage = bsamplepartusage
                        # Masterinstrumentslist_listSaveUpdate.bregularpartusage = bregularpartusage
                        # Masterinstrumentslist_listSaveUpdate.bcalibstandards = bcalibstandards
                        Masterinstrumentslist_listSaveUpdate.spartno = spartno
                        # Masterinstrumentslist_listSaveUpdate.lcompanyid = lcompanyid
                        # Masterinstrumentslist_listSaveUpdate.bplanned = bplanned
                        Masterinstrumentslist_listSaveUpdate.serpcode = serpcode
                        # Masterinstrumentslist_listSaveUpdate.lhistorycard = 0
                        Masterinstrumentslist_listSaveUpdate.lfolowid1 = lfolowid1
                        Masterinstrumentslist_listSaveUpdate.lfolowid2 = lfolowid2
                        Masterinstrumentslist_listSaveUpdate.lfolowid3 = lfolowid3
                        Masterinstrumentslist_listSaveUpdate.lfolowid4 = lfolowid4
                        Masterinstrumentslist_listSaveUpdate.lfolowid5 = lfolowid5
                        Masterinstrumentslist_listSaveUpdate.bshowlistascalibrate = 1 
                        # Masterinstrumentslist_listSaveUpdate.ltolid = 0
                        # Masterinstrumentslist_listSaveUpdate.sissueddate = ""
                        # Masterinstrumentslist_listSaveUpdate.sreturneddate = ""

                        Masterinstrumentslist_listSaveUpdate.save()


                        # Masterinstrumentslistpart2SaveUpdate =  Masterinstrumentslistpart2.objects.get(lid =lInstIdA) 
 




                        # Masterinstrumentslistpart2SaveUpdate.sstoragerack =sstoragerack
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingno = sdrawingno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingrevno = sdrawingrevno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingfile =sdrawingfile
                        # Masterinstrumentslistpart2SaveUpdate.sunitofmeasure = sunitofmeasure
                        # Masterinstrumentslistpart2SaveUpdate.srevisionno = srevisionno
                        # Masterinstrumentslistpart2SaveUpdate.sproperty = sproperty
                        # Masterinstrumentslistpart2SaveUpdate.scatalogueno = scatalogueno
                        # Masterinstrumentslistpart2SaveUpdate.frangefrom = frangefrom
                        # Masterinstrumentslistpart2SaveUpdate.frangeto = frangeto
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.fleastcount = fleastcount
                        # Masterinstrumentslistpart2SaveUpdate.scheckmethod = scheckmethod
                        # Masterinstrumentslistpart2SaveUpdate.dtlastservice = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtnextservice = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastservicedate = ""
                        # Masterinstrumentslistpart2SaveUpdate.snextservicedate = ""
                        # Masterinstrumentslistpart2SaveUpdate.smanualduernr = smanualduernr
                        # Masterinstrumentslistpart2SaveUpdate.ldayremainrnr = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtlastrnr = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtnextrnr = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastrnrdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.snextrnrdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.srange = srange
                        # Masterinstrumentslistpart2SaveUpdate.frange3 = frange3
                        # Masterinstrumentslistpart2SaveUpdate.dcalibrationcost = dcalibrationcost
                        # Masterinstrumentslistpart2SaveUpdate.dpurchaseprice = dpurchaseprice
                        # Masterinstrumentslistpart2SaveUpdate.smodelno = ""
                        # Masterinstrumentslistpart2SaveUpdate.sserialno = ""
                        # Masterinstrumentslistpart2SaveUpdate.saccuracy = saccuracy
                        # Masterinstrumentslistpart2SaveUpdate.scertificateno = ""
                        # Masterinstrumentslistpart2SaveUpdate.straceability = ""
                        # Masterinstrumentslistpart2SaveUpdate.ssize1 =ssize1
                        # Masterinstrumentslistpart2SaveUpdate.llusagedefault = llusagedefault
                        # Masterinstrumentslistpart2SaveUpdate.llusagecount = llusagecount
                        # Masterinstrumentslistpart2SaveUpdate.smounted = smounted
                        # Masterinstrumentslistpart2SaveUpdate.fproducttolerance = fproducttolerance
                        # Masterinstrumentslistpart2SaveUpdate.sproducttolerance = sproducttolerance
                        # Masterinstrumentslistpart2SaveUpdate.facconstant = facconstant
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.sagencyservice = sagencyservice
                        # Masterinstrumentslistpart2SaveUpdate.sprocuredate = ddateofprocure.strftime("%m/%d/%Y")
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.brejected = 0
                        # Masterinstrumentslistpart2SaveUpdate.srejecteddate = ""
                        # Masterinstrumentslistpart2SaveUpdate.breplaced = 0
                        # Masterinstrumentslistpart2SaveUpdate.lreplacedinstrumentid = 0
                        # Masterinstrumentslistpart2SaveUpdate.bduechanged = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtduechangedate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastchangedate =  ""
                        # Masterinstrumentslistpart2SaveUpdate.blanova = 0
                        # Masterinstrumentslistpart2SaveUpdate.srevno = srevno
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.scommentchangecalibstd = scommentchangecalibstd
                        # Masterinstrumentslistpart2SaveUpdate.bverifyforpurchase = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtsendforverificationforpurchaseon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtverifiedforpurchaseon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.ssendforverificationforpurchaseon = ""
                        # Masterinstrumentslistpart2SaveUpdate.sverifiedforpurchaseon = ""
                        # Masterinstrumentslistpart2SaveUpdate.spreferredvendor = spreferredvendor
                        # Masterinstrumentslistpart2SaveUpdate.sbondnumber = sbondnumber
                        # Masterinstrumentslistpart2SaveUpdate.dgo = dgo
                        # Masterinstrumentslistpart2SaveUpdate.dnogo = dnogo
                        # Masterinstrumentslistpart2SaveUpdate.dtoldiff = dtoldiff
                        # Masterinstrumentslistpart2SaveUpdate.dtolallowed = dtolallowed
                        # Masterinstrumentslistpart2SaveUpdate.bmanufacturingstd = bmanufacturingstd
                        # Masterinstrumentslistpart2SaveUpdate.dplusofminus = dplusofminus
                        # Masterinstrumentslistpart2SaveUpdate.dz = dz
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.bpartno =bpartno
                        # Masterinstrumentslistpart2SaveUpdate.gageserialno = gageserialno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingno2 = sdrawingno2
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa2 = lcontinuousnoa2
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob2 = lcontinuousnob2
                        # Masterinstrumentslistpart2SaveUpdate.lcategorytype1 = lcategorytype1
                        # Masterinstrumentslistpart2SaveUpdate.lcategorytype2 = lcategorytype2
                        # Masterinstrumentslistpart2SaveUpdate.bcustomer = bcustomer
                        # Masterinstrumentslistpart2SaveUpdate.lservicealert = lservicealert
                        # Masterinstrumentslistpart2SaveUpdate.ferrorallowed = ferrorallowed
                        # Masterinstrumentslistpart2SaveUpdate.splannedby = request.session['semployeename'] 
                        # Masterinstrumentslistpart2SaveUpdate.bidchanged = 0
                        # Masterinstrumentslistpart2SaveUpdate.scode1 = scode1
                        # Masterinstrumentslistpart2SaveUpdate.scode2 = scode2
                        # Masterinstrumentslistpart2SaveUpdate.scode3 = scode3
                        # Masterinstrumentslistpart2SaveUpdate.scode4 = scode4
                        # Masterinstrumentslistpart2SaveUpdate.scode5 = scode5
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.ssstatus = scurrentstatus
                        # Masterinstrumentslistpart2SaveUpdate.ssize = ssize
                        # Masterinstrumentslistpart2SaveUpdate.lintervalservice = lintervalservice
                        # Masterinstrumentslistpart2SaveUpdate.sintervalperiodservice = sintervalperiodservice
                        # Masterinstrumentslistpart2SaveUpdate.smanufacturer = smanufacturer
                        # Masterinstrumentslistpart2SaveUpdate.ddateofprocure = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.sdateofprocure = ""
                        # Masterinstrumentslistpart2SaveUpdate.soperation = soperation
                        # Masterinstrumentslistpart2SaveUpdate.scompantname = scompantname
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa1 = lcontinuousnoa1
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob1 = lcontinuousnob1
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa = lcontinuousnoa
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob = lcontinuousnob
                        # Masterinstrumentslistpart2SaveUpdate.btyperef = btyperef
                        # Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnoa = btyperefascontinuousnoa
                        # Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnob = btyperefascontinuousnob
                        # Masterinstrumentslistpart2SaveUpdate.scomment = ""
                        # Masterinstrumentslistpart2SaveUpdate.lpurchasevendorid = lpurchasevendorid
                        # Masterinstrumentslistpart2SaveUpdate.lservicevendorid = lservicevendorid
                        # Masterinstrumentslistpart2SaveUpdate.sagencycalib = sagencycalib
                        # Masterinstrumentslistpart2SaveUpdate.scode = scode
                        # Masterinstrumentslistpart2SaveUpdate.lcurrentlocationid = lcurrentlocationid
                        # Masterinstrumentslistpart2SaveUpdate.bservice = bservice
                        # Masterinstrumentslistpart2SaveUpdate.lcalibalert = lcalibalert
                        # Masterinstrumentslistpart2SaveUpdate.lintervalcalib = lintervalcalib
                        # Masterinstrumentslistpart2SaveUpdate.sintervalperiodcalib = sintervalperiodcalib
                        # Masterinstrumentslistpart2SaveUpdate.lalertinterval = lalertinterval
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.ldayremaincalib = 0
                        # Masterinstrumentslistpart2SaveUpdate.lusageinterval = lusageinterval
                        # Masterinstrumentslistpart2SaveUpdate.lusageintervaldisplay = lusageintervaldisplay
                        # Masterinstrumentslistpart2SaveUpdate.lusagecurrent = 0
                        # Masterinstrumentslistpart2SaveUpdate.lidlecalibfrequency = lidlecalibfrequency
                        # Masterinstrumentslistpart2SaveUpdate.dtplanneddate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.splanneddate = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtvalidationlastdate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.svalidationlastdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtvalidationnextdate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.svalidationnextdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.schangeoldid = ""
                        # Masterinstrumentslistpart2SaveUpdate.llusagecountalerts = llusagecountalerts
                        # Masterinstrumentslistpart2SaveUpdate.btnextidlecalibration = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.snextidlecalibration = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtidleon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.sidleon = ""
                        # Masterinstrumentslistpart2SaveUpdate.b1monthvalidation = b1monthvalidation
                        # Masterinstrumentslistpart2SaveUpdate.dtnextvalidation = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.snextvalidation = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtlastvalidation = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastvalidation = ""



                        # Masterinstrumentslistpart2SaveUpdate.save()
  
                        


 
 


                        sCreatedBy = ""

                        sCreatedBy = request.session['semployeename'] + " (" + request.session['semployeeno']  + ") "



                        sNewSAPCode = "NO"
                        if (bNewIDwithfirstSerial == 1):
                            sNewSAPCode = "YES"
                        
                        sCompanyName = ""
                        sCompanyName =   "Maini Group - " + sPlantNameName
                        #Admin1Companyinfo_list =  Admin1Companyinfo.objects.get(lid=1)
                        #if (Admin1C
                        request.session['sSAPCode']  = sNewSAPCode
                        #return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDIDPrint.html', 
                        #{
                            #'title':'User list', 
                            #'sCompanyName':sCompanyName, 
                            #'sPlantName':sPlantNameNameA, 
                            #'sPlantCode':sPlantCode[:2],
                            #'sAssetCode':  sCodeFinal1, 
                            #'sNewSAPCode':sNewSAPCode,
                            #'sCodeDescription':sCodeDescription,
                            #'sFlow1':sFlow1,
                            #'sFlow2':sFlow2,
                            #'sFlow3':sFlow3,
                            #'sFlow4':sFlow4,
                            #'sFlow5':sFlow5,
                            #'sFlowDesc1':sCodeFlow1.strip(),
                            #'sFlowDesc2':sCodeFlow2.strip(),
                            #'sFlowDesc3':sCodeFlow3.strip(),
                            #'sFlowDesc4':sCodeFlow4.strip(),
                            #'sFlowDesc5':sCodeFlow5.strip(),
                            #'sDate':datetime.now(),
                            #'sCreatedBy':sCreatedBy,
                        #}) 

                        #template = get_template('CloudCaliber/GaugeMasterlistCreateOLDIDPrint.html')
                        context = {
                            'title':'Print New SAP Code', 
                            'sCompanyName':sCompanyName, 
                            'sPlantName':sPlantNameNameA, 
                            'sPlantCode':sPlantCode[:2],
                            'sAssetCode':  sCodeFinal1, 
                            'sNewSAPCode':sNewSAPCode,
                            'sCodeDescription':sCodeDescription,
                            'sFlow1':styperefnameA1,
                            'sFlow2':styperefnameA2,
                            'sFlow3':styperefnameA3,
                            'sFlow4':styperefnameA4,
                            'sFlow5':styperefnameA5,
                            'sFlowDesc1':sCodeFlow1.strip(),
                            'sFlowDesc2':sCodeFlow2.strip(),
                            'sFlowDesc3':sCodeFlow3.strip(),
                            'sFlowDesc4':sCodeFlow4.strip(),
                            'sFlowDesc5':sCodeFlow5.strip(),
                            'sDate':datetime.now(),
                            'sCreatedBy':sCreatedBy,
                        }
                        pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateIDPrint.html', context)
                        return HttpResponse(pdf, content_type='application/pdf')
                        html = template.render(context)
                        pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateOLDIDPrint.html', context)
                        if pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')

                        filename = "GaugeSAPCode_" + sCodeFinal1 + str(ddateofprocure.day) + str(ddateofprocure.monthth) + str(ddateofprocure.year)  + ".pdf"  
                        content = "inline; filename='%s'" %(filename)
                        download = request.GET.get("download")
                        if download:
                            content = "attachment; filename='%s'" %(filename)
                            response['Content-Disposition'] = content
                            return response
                        return HttpResponse("Not found")



        data = request.POST
        if 'Classification' in request.POST:
            cmbClassificationID=request.POST['Classification'] 

        if 'Category' in request.POST:
            cmbCategoryID=request.POST['Category'] 

        if 'getFlow1' in request.POST:
            cmbgetFlow1ID=request.POST['getFlow1'] 


        #request.session['cmbClassificationID'] =cmbClassificationID
        #request.session['cmbCategoryID'] =cmbCategoryID
        #request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
        #request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
        #request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
        #request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
        #request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
        #request.session['cmbgetFlow6ID'] =cmbgetFlow6ID
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10
        
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10

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
  
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
        return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': "" ,  
            'sCodeFinal2': "" ,  
            'cmbClassificationID': 0 , 
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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

            
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)



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
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

    
        return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,
        })







 
@csrf_exempt
def GaugeMasterlistCreateOLDUserID(request,lID):
 
    lInstrumentID = lID

    lLoginUserIdA = request.session['lLoginUserId'] 
    if(lLoginUserIdA==0):
        return views.home(request)

    sCodeFinal1 = ""
    sCodeFinal2 = ""
    sLastDate = ""
    sNextDate = ""
    sLastDate1 = ""
    sNextDate1 = ""
    sLastDate2 = ""
    sNextDate2 = ""

    bcalibrateidle = 0
    bsapcodegenerate =0

    
    MasterinstrumentslistCheck = Masterinstrumentslist.objects.get(lid=lInstrumentID) 
    if MasterinstrumentslistCheck:
        sLastDate1 = MasterinstrumentslistCheck.slastcalibdate 
        sNextDate1 = MasterinstrumentslistCheck.snextcalibdate 
        bcalibrateidle = MasterinstrumentslistCheck.bcalibrateidle
        bsapcodegenerate = MasterinstrumentslistCheck.bsapcodegenerate
    
    date_time_Main = datetime.now()
    if (sLastDate2 == ""):
        sLastDate2 = datetime.strftime(date_time_Main, '%d-%m-%Y')
    if (sNextDate2 == ""):
        sNextDate2 = datetime.strftime(date_time_Main, '%d-%m-%Y')

    sLastDate2  = sLastDate1.split("/")
    sNextDate2  = sNextDate1.split("/")

    if(len(sLastDate2) > 1):
        sLastDate = sLastDate2[2] + "-" + sLastDate2[1] + "-" + sLastDate2[0]
    else:
        sLastDate2  = sLastDate1.split("-") 
        if(len(sLastDate2) > 1):
            sLastDate = sLastDate2[2] + "-" + sLastDate2[1] + "-" + sLastDate2[0] 
    
    if(len(sNextDate2) > 1):
        sNextDate = sNextDate2[2] + "-" + sNextDate2[1] + "-" + sNextDate2[0] 
    else:
        sNextDate2  = sNextDate1.split("-")
    
        if(len(sNextDate2) > 1):
            sNextDate = sNextDate2[2] + "-" + sNextDate2[1] + "-" + sNextDate2[0] 

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname'] 
    semployeename = request.session['semployeename']

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
    getFlow2Code = ""
    getFlow3Code = ""
    getFlow4Code = ""
    getFlow5Code = ""
    getFlowContCode = ""

    bContFlag = 0


    sPlantNameName = ""
    sPlantNameNameA = ""
    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
        sPlantNameName = AdminunitlistActive.splantname + " (" + AdminunitlistActive.scode.strip() + ")"
        sPlantNameNameA = AdminunitlistActive.splantname
 

    sCodeFinal1=""
    sCodeFinal2="-" + sPlantCode




    if request.method == "POST":

        data = request.POST

        lInstrumentID =0
        if 'txtID' in request.POST: 
            lInstrumentID = int(data.get('txtID'))


        txtLastCalibrationDate =0
        if 'txtLastCalibrationDate' in request.POST: 
            txtLastCalibrationDate = data.get('txtLastCalibrationDate')


            
        txtNextCalibrationDate =0
        if 'txtNextCalibrationDate' in request.POST: 
            txtNextCalibrationDate = data.get('txtNextCalibrationDate')


            
        bCalibrateWhenIdle =0
        if 'bCalibrateWhenIdle1' in request.POST: 
            bCalibrateWhenIdle = 1


        ID_Categories =0
        if 'Categories' in request.POST: 
            if(data.get('Categories').isnumeric()):
                ID_Categories = int(data.get('Categories'))

            
        ClassificationData =0
        if 'Classification' in request.POST: 
            if(data.get('Classification').isnumeric()):
                ClassificationData= int(data.get('Classification'))

        Flow1Data =0
        if 'Flow1' in request.POST: 
            if(data.get('Flow1').isnumeric()):
                Flow1Data = int(data.get('Flow1'))

        Flow2Data =0
        if 'Flow2' in request.POST: 
            if(data.get('Flow2').isnumeric()):
                Flow2Data = int(data.get('Flow2'))


        Flow3Data =0
        if 'Flow3' in request.POST: 
            if(data.get('Flow3').isnumeric()):
                Flow3Data = int(data.get('Flow3'))


        Flow4Data =0
        if 'Flow4' in request.POST:
            if(data.get('Flow4').isnumeric()):
                Flow4Data = int(data.get('Flow4'))

        Flow5Data =0
        if 'Flow5' in request.POST: 
            if(data.get('Flow5').isnumeric()):
                Flow5Data = int(data.get('Flow5'))

        GaugeClass =0
        if 'GaugeClass' in request.POST: 
            GaugeClass = int(data.get('GaugeClass'))

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('Dashboard')







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


            sCodeFinal1 = sClasscode
            sCodeFinal2 = sClasscode + " " + sPlantCode
         
            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': 0 ,  
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate, 
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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







            sCodeFinal1 = sClasscode + sCategoryCode
            sCodeFinal2 = sClasscode  + sCategoryCode + " " + sPlantCode
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })




            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'cmbCategoryID': ID_Categories ,  
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })
            






        if 'cmbGetID' in request.POST:  
               
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
 
            Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_list:
                sCategoryCode = Adminassetcategorylist_list.scode
                sClasscode = Adminassetcategorylist_list.styperefname  
                styperefnameA1 = Adminassetcategorylist_list.styperefname1
                styperefnameA2 = Adminassetcategorylist_list.styperefname2
                styperefnameA3 = Adminassetcategorylist_list.styperefname3
                styperefnameA4 = Adminassetcategorylist_list.styperefname4
                styperefnameA5 = Adminassetcategorylist_list.styperefname5


            sCodeFlow1 = ""
            sCodeFlow2 = ""
            sCodeFlow3 = ""
            sCodeFlow4 = ""
            sCodeFlow5 = ""

            if(Flow1Data !=0):
                if (styperefnameA1 == "Part No"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Equipment"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Operation"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                elif (styperefnameA1 == "Material"):
                    Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                else:
                    Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                    if (Adminassetcategorytypelist1_AddNew1OBJ1):
                        sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                    


            if(Flow2Data !=0):
                if (styperefnameA2 == "Part No"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Equipment"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Operation"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                elif (styperefnameA2 == "Material"):
                    Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                else:
                    Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                    if (Adminassetcategorytypelist2_AddNew1OBJ1):
                        sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                    


            if(Flow3Data !=0):
                if (styperefnameA3 == "Part No"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Equipment"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Operation"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                elif (styperefnameA3 == "Material"):
                    Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                else:
                    Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                    if (Adminassetcategorytypelist3_AddNew1OBJ1):
                        sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                 


            if(Flow4Data !=0):
                if (styperefnameA4 == "Part No"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Equipment"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Operation"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                elif (styperefnameA4 == "Material"):
                    Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                else:
                    Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                    if (Adminassetcategorytypelist4_AddNew1OBJ1):
                        sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                 

            if(Flow5Data !=0):
                if (styperefnameA5 == "Part No"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Equipment"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Operation"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                elif (styperefnameA5 == "Material"):
                    Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                    #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                else:
                    Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                    if (Adminassetcategorytypelist5_AddNew1OBJ1):
                        sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                 

            sContNo = ""
            sContNo1 = ""
            lContNo = 0
            lContNoVB = 0
            lContNoVBC = 0
        
            lassetidA =0

            sCategoryCode = "" 
            Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
            if Adminassetcategorylist_listH:
                sCategoryCode = Adminassetcategorylist_listH.scode 
                sClasscode = Adminassetcategorylist_listH.styperefname 
                lassetidA = Adminassetcategorylist_listH.lassetid
                lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
        
 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')



            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
          

            AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
            if AdmincategoryidcontinuousnolistActivw:
                for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                    lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                    lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            else:
                lContNo  = lContNoVB
 

            if (lContNoVBC == 0 ):
                if (lassetidA == 6): 
                    
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8): 
                    #request.session['lContNoVBC'] = 1
                    lContNo = lContNo +1
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0
            else:
                if (lassetidA == 6):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 7):  
                    sContNo1 = str(lContNo)
                elif (lassetidA == 8):  
                    sContNo1 = str(lContNo)
                else:
                    lContNo =0

 

            if(sContNo1 != ''):
                if(len(sContNo1) == 1):
                    sContNo = "000" + sContNo1
                elif(len(sContNo1) == 2):
                    sContNo = "00" + sContNo1
                elif(len(sContNo1) == 3):
                    sContNo = "0" + sContNo1
                else:
                    sContNo =  sContNo1

 
            s1 = sCodeFlow1.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow1 =s2.replace('.','')
            
            s1 = sCodeFlow2.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow2 =s2.replace('.','')

            
            s1 = sCodeFlow3.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow3 =s2.replace('.','')

            
            s1 = sCodeFlow4.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow4 =s2.replace('.','')


            s1 = sCodeFlow5.split(" ")
            s2 = ""
            
            if (len(s1) == 1):
                s2 = s1[0]
            elif (len(s1) == 2):
                s2 = s1[1]
            elif (len(s1) == 3):
                s2 = s1[2]
            elif (len(s1) == 4):
                s2 = s1[3]
            elif (len(s1) == 5):
                s2 = s1[4]
            elif (len(s1) == 6):
                s2 = s1[5]
            elif (len(s1) == 7):
                s2 = s1[6]
            elif (len(s1) == 8):
                s2 = s1[7]
            elif (len(s1) == 9):
                s2 = s1[8]
            elif (len(s1) == 10):
                s2 = s1[9]

            sCodeFlow5 =s2.replace('.','')


            sCodeFinal1 = ""
            sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  #+  sContNo.strip()
        

            lSerialNo =0
            
            AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
            if AdminassetserialformatlistActive:
                for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                    lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


            lSerialNo = lSerialNo +1
 

            
            bNewIDwithfirstSerial = 0
            if (lSerialNo == 1):
                bNewIDwithfirstSerial = 1

 
            sSerialNo = ""
            sSerialNo1 = ""
            sSerialNo=str(lSerialNo)
            if (len(sSerialNo) == 1):
                sSerialNo1 = "00" + sSerialNo
            elif (len(sSerialNo) == 2):
                sSerialNo1 = "0" + sSerialNo 
            else:
                sSerialNo1 =   sSerialNo 


           # sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
            sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()    + "-" + sPlantCode[:2] + sSerialNo1.strip()
        
             


    
 
         

            if (styperefnameA1 == "Part No"):
                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Equipment"):
                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Operation"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            elif (styperefnameA1 == "Material"):
                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
            else:
                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                 
            if (styperefnameA2 == "Part No"):
                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
               # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            elif (styperefnameA2 == "Equipment"):
                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Operation"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
            elif (styperefnameA2 == "Material"):
                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
            else:
                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



            if (styperefnameA3 == "Part No"):
                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Equipment"):
                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Operation"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            elif (styperefnameA3 == "Material"):
                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
            else:
                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

            if (styperefnameA4 == "Part No"):
                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Equipment"):
                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Operation"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
            elif (styperefnameA4 == "Material"):
                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
            else:
                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

            if (styperefnameA5 == "Part No"):
                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
            elif (styperefnameA5 == "Equipment"):
                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Operation"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            elif (styperefnameA5 == "Material"):
                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
            else:
                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })


            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')


            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserID.html', 
            {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': sCodeFinal1 ,  
            'sCodeFinal2': sCodeFinal2 ,  
            'cmbClassificationID': ClassificationData , 
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
            'cmbCategoryID': ID_Categories ,  
            'cmbFlow1ID': Flow1Data ,  
            'cmbFlow2ID': Flow2Data ,  
            'cmbFlow3ID': Flow3Data ,  
            'cmbFlow4ID': Flow4Data ,
            'cmbFlow5ID': Flow5Data ,     
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'bNewID': 0 ,  
            
        })






        if 'cmbSaveAdd' in request.POST:  




            sGaugeClass = ""
            if (GaugeClass != 0):
                Admintoleranceclasslist_listGet =  Admintoleranceclasslist.objects.get(lid = GaugeClass)
                if (Admintoleranceclasslist_listGet):
                    sGaugeClass = Admintoleranceclasslist_listGet.stoleranceclass
                

             
            bFlag = 0

            sFlow1 = ""
            sFlow2 =  ""
            sFlow3 =  ""
            sFlow4 =  ""
            sFlow5 =  ""
            sFlowDesc1 = ""
            sFlowDesc2 =  ""
            sFlowDesc3 =  ""
            sFlowDesc4 =  ""
            sFlowDesc5 =  "" 
            sCategorytype = ""

            sAssetCategory = ""

            if (ClassificationData == 0):
                bFlag = 1
                messages.error(request, 'Asset Classification is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
            else :
                if (ID_Categories == 0):
                    bFlag = 1
                    messages.error(request, 'Asset Category is not selected. Please select & then create ID. ID IS NOT CREATED!!!')
                else :

                    Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                    if Adminassetcategorylist_list:
                        sCategoryCode = Adminassetcategorylist_list.scode
                        sCategorytype = Adminassetcategorylist_list.categorytype
                        sClasscode = Adminassetcategorylist_list.styperefname
                        sAssetCategory = Adminassetcategorylist_list.assettype 
                        #request.session['sCategoryCode'] = Adminassetcategorylist_list.scode
                        #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                        #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                        #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                        #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                        #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                        #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                        styperefnameA1 = Adminassetcategorylist_list.styperefname1
                        styperefnameA2 = Adminassetcategorylist_list.styperefname2
                        styperefnameA3 = Adminassetcategorylist_list.styperefname3
                        styperefnameA4 = Adminassetcategorylist_list.styperefname4
                        styperefnameA5 = Adminassetcategorylist_list.styperefname5
                        sCodeDescA = Adminassetcategorylist_list.categorytype
                        sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                        sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                        sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                        sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                        sCodeDesc5 = Adminassetcategorylist_list.styperefname5
                

                    if( styperefnameA1 != ''):
                        if(Flow1Data == 0):
                            bFlag = 1
                            sFlow1Message = styperefnameA1 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow1Message)

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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })



                    if( styperefnameA2 != ''):
                        if(Flow2Data == 0):
                            bFlag = 1
                            sFlow2Message = styperefnameA2 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow2Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })
                    if( styperefnameA3 != ''):
                        if(Flow3Data == 0):
                            bFlag = 1
                            sFlow3Message = styperefnameA3 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow3Message)

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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })
                    if( styperefnameA4 != ''):
                        if(Flow4Data == 0):
                            bFlag = 1
                            sFlow4Message = styperefnameA4 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow4Message)
                            
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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })
                    if( styperefnameA5 != ''):
                        if(Flow5Data == 0):
                            bFlag = 1
                            sFlow5Message = styperefnameA5 + ' is not selected. Please select & then create ID. ID IS NOT CREATED!!!'
                            messages.error(request, sFlow5Message)

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


                            sCodeFinal1 = sClasscode
                            sCodeFinal2 = sClasscode + " " + sPlantCode
                        
                            Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')



                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 1).order_by('scategorytype').values()  
                                
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2  })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 2).order_by('scategorytype').values()  



                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':styperefnameA3  })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 3).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow3.html', {'Adminassetcategorytypelist3_AddNew1OBJ': Adminassetcategorytypelist3_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })

                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4  })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 4).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow4.html', {'Adminassetcategorytypelist4_AddNew1OBJ': Adminassetcategorytypelist4_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })

                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowPartNo.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5  })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowEquipment.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowOperation.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlowMaterial.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist5_AddNew1OBJ, 'styperefnameA1':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =ID_Categories, lcode5 = 5).order_by('scategorytype').values()  
                                # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDID_stypeFlow5.html', {'Adminassetcategorytypelist5_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



 
                            Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype')
                            tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ClassificationData).order_by('categorytype')
                            Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

                        
                            return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDID.html', 
                            {
                            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
                            'sPlantName': sPlantName ,  
                            'semployeename':semployeename,
                            'sCodeFinal1': sCodeFinal1 ,  
                            'sCodeFinal2': sCodeFinal2 ,  
                            'cmbClassificationID': ClassificationData , 
                            'cmbCategoryID': ID_Categories ,  
                            'sLastDate':sLastDate,  
                            'sNextDate':sNextDate,
                            'bcalibrateidle':bcalibrateidle, 
                            'bsapcodegenerate':bsapcodegenerate,
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
                            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
                            'bNewID': 0 ,  
                            
                        })

                    if (bFlag == 0):
                    
                        
                        sCodeDescription = ""
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
                        sCategoryDesc = ""
            
                        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_list:
                            sCategoryCode = Adminassetcategorylist_list.scode
                            sCategorytype = Adminassetcategorylist_list.categorytype
                            sClasscode = Adminassetcategorylist_list.styperefname
                            sAssetCategory = Adminassetcategorylist_list.assettype 
                            #['sCategoryCode'] = Adminassetcategorylist_list.scode
                            #request.session['categorytype'] = Adminassetcategorylist_list.categorytype
                            #request.session['styperefname1'] = Adminassetcategorylist_list.styperefname1
                            #request.session['styperefname2'] = Adminassetcategorylist_list.styperefname2
                            #request.session['styperefname3'] = Adminassetcategorylist_list.styperefname3
                            #request.session['styperefname4'] = Adminassetcategorylist_list.styperefname4
                            #request.session['styperefname5'] = Adminassetcategorylist_list.styperefname5
                            styperefnameA1 = Adminassetcategorylist_list.styperefname1
                            styperefnameA2 = Adminassetcategorylist_list.styperefname2
                            styperefnameA3 = Adminassetcategorylist_list.styperefname3
                            styperefnameA4 = Adminassetcategorylist_list.styperefname4
                            styperefnameA5 = Adminassetcategorylist_list.styperefname5
                            sCodeDescA = Adminassetcategorylist_list.categorytype
                            sCodeDesc1 = Adminassetcategorylist_list.styperefname1
                            sCodeDesc2 = Adminassetcategorylist_list.styperefname2
                            sCodeDesc3 = Adminassetcategorylist_list.styperefname3
                            sCodeDesc4 = Adminassetcategorylist_list.styperefname4
                            sCodeDesc5 = Adminassetcategorylist_list.styperefname5

                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   

                        sCategoryDesc = sCategorytype
                        sCodeFlow1 = ""
                        sCodeFlow2 = ""
                        sCodeFlow3 = ""
                        sCodeFlow4 = ""
                        sCodeFlow5 = ""

                        if(Flow1Data !=0):
                            if (styperefnameA1 == "Part No"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Equipment"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow1Data) 
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Operation"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            elif (styperefnameA1 == "Material"):
                                Adminassetcategorytypelist1_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow1Data)
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':styperefnameA1 })
                            else:
                                Adminassetcategorytypelist1_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow1Data)  
                                if (Adminassetcategorytypelist1_AddNew1OBJ1):
                                    sCodeFlow1 = Adminassetcategorytypelist1_AddNew1OBJ1.scategorytype
                                


                        if(Flow2Data !=0):
                            if (styperefnameA2 == "Part No"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Equipment"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow2Data) 
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Operation"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            elif (styperefnameA2 == "Material"):
                                Adminassetcategorytypelist2_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow2Data)
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA2':styperefnameA2 })
                            else:
                                Adminassetcategorytypelist2_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow2Data)  
                                if (Adminassetcategorytypelist2_AddNew1OBJ1):
                                    sCodeFlow2 = Adminassetcategorytypelist2_AddNew1OBJ1.scategorytype
                                


                        if(Flow3Data !=0):
                            if (styperefnameA3 == "Part No"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Equipment"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow3Data) 
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Operation"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            elif (styperefnameA3 == "Material"):
                                Adminassetcategorytypelist3_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow3Data)
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA3':styperefnameA3 })
                            else:
                                Adminassetcategorytypelist3_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow3Data)  
                                if (Adminassetcategorytypelist3_AddNew1OBJ1):
                                    sCodeFlow3 = Adminassetcategorytypelist3_AddNew1OBJ1.scategorytype
                            


                        if(Flow4Data !=0):
                            if (styperefnameA4 == "Part No"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Equipment"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow4Data) 
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Operation"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            elif (styperefnameA4 == "Material"):
                                Adminassetcategorytypelist4_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow4Data)
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA4':styperefnameA4 })
                            else:
                                Adminassetcategorytypelist4_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow4Data)  
                                if (Adminassetcategorytypelist4_AddNew1OBJ1):
                                    sCodeFlow4 = Adminassetcategorytypelist4_AddNew1OBJ1.scategorytype
                            

                        if(Flow5Data !=0):
                            if (styperefnameA5 == "Part No"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =   Adminpartdetailslist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.spartno[2:]
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Equipment"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =    Adminequipmentlist.objects.get(lid = Flow5Data) 
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                            # return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Operation"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentoperationlist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            elif (styperefnameA5 == "Material"):
                                Adminassetcategorytypelist5_AddNew1OBJ1 =     Admininstrumentmateriallist.objects.get(lid = Flow5Data)
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scode
                                #return render(request, 'CloudCaliber/GaugeMasterlistCreateOLDUserID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA5':styperefnameA5 })
                            else:
                                Adminassetcategorytypelist5_AddNew1OBJ1 =  Adminassetcategorytypelist1.objects.get(lcategorytypeid = Flow5Data)  
                                if (Adminassetcategorytypelist5_AddNew1OBJ1):
                                    sCodeFlow5 = Adminassetcategorytypelist5_AddNew1OBJ1.scategorytype
                            
 
                        sCodeDesc1 = sCodeFlow1
                        sCodeDesc2 = sCodeFlow2
                        sCodeDesc3 = sCodeFlow3
                        sCodeDesc4 = sCodeFlow4
                        sCodeDesc5 = sCodeFlow5
                        sCodeDescription = sCodeDescA + " " + sCodeDesc1 + " " + sCodeDesc2 + " " + sCodeDesc3 + " " + sCodeDesc4 + " " + sCodeDesc5
   
                        sContNo = ""
                        sContNo1 = ""
                        lContNo = 0
                        lContNoVB = 0
                        lContNoVBC = 0
                    
                        lassetidA =0

                        sCategoryCode = "" 
                        Adminassetcategorylist_listH =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                        if Adminassetcategorylist_listH:
                            sCategoryCode = Adminassetcategorylist_listH.scode 
                            sClasscode = Adminassetcategorylist_listH.styperefname 
                            lassetidA = Adminassetcategorylist_listH.lassetid
                            lContNoVB = Adminassetcategorylist_listH.lcontinuousnoa
                    
                        
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')

                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip() 
                    
                        sCodeFinal1AK = sCodeFinal1

                        AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
                        if AdmincategoryidcontinuousnolistActivw:
                            for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
                                lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                                lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
                        else:
                            lContNo  = lContNoVB
            

                        if (lContNoVBC == 0 ):
                            if (lassetidA == 6): 
                                
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8): 
                                #request.session['lContNoVBC'] = 1
                                lContNo = lContNo +1
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0
                        else:
                            if (lassetidA == 6):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 7):  
                                sContNo1 = str(lContNo)
                            elif (lassetidA == 8):  
                                sContNo1 = str(lContNo)
                            else:
                                lContNo =0

            

                        if(sContNo1 != ''):
                            if(len(sContNo1) == 1):
                                sContNo = "000" + sContNo1
                            elif(len(sContNo1) == 2):
                                sContNo = "00" + sContNo1
                            elif(len(sContNo1) == 3):
                                sContNo = "0" + sContNo1
                            else:
                                sContNo =  sContNo1


                        
 
                        s1 = sCodeFlow1.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow1 =s2.replace('.','')
                        
                        s1 = sCodeFlow2.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow2 =s2.replace('.','')

                        
                        s1 = sCodeFlow3.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow3 =s2.replace('.','')

                        
                        s1 = sCodeFlow4.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow4 =s2.replace('.','')


                        s1 = sCodeFlow5.split(" ")
                        s2 = ""
                        
                        if (len(s1) == 1):
                            s2 = s1[0]
                        elif (len(s1) == 2):
                            s2 = s1[1]
                        elif (len(s1) == 3):
                            s2 = s1[2]
                        elif (len(s1) == 4):
                            s2 = s1[3]
                        elif (len(s1) == 5):
                            s2 = s1[4]
                        elif (len(s1) == 6):
                            s2 = s1[5]
                        elif (len(s1) == 7):
                            s2 = s1[6]
                        elif (len(s1) == 8):
                            s2 = s1[7]
                        elif (len(s1) == 9):
                            s2 = s1[8]
                        elif (len(s1) == 10):
                            s2 = s1[9]

                        sCodeFlow5 =s2.replace('.','')


                        sCodeFinal1 = ""
                        sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  #+  sContNo.strip()
                    

                        lSerialNo =0
                        
                        AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
                        if AdminassetserialformatlistActive:
                            for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
                                lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


                        lSerialNo = lSerialNo +1
            

                        
                        bNewIDwithfirstSerial = 0
                        if (lSerialNo == 1):
                            bNewIDwithfirstSerial = 1

            
                        sSerialNo = ""
                        sSerialNo1 = ""
                        sSerialNo=str(lSerialNo)
                        if (len(sSerialNo) == 1):
                            sSerialNo1 = "00" + sSerialNo
                        elif (len(sSerialNo) == 2):
                            sSerialNo1 = "0" + sSerialNo 
                        else:
                            sSerialNo1 =   sSerialNo 


                       # sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
                    
                    
                        sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sCodeFlow1.strip() +  sCodeFlow2.strip() +  sCodeFlow3.strip() +  sCodeFlow4.strip() +  sCodeFlow5.strip()   + "-" + sPlantCode[:2] + sSerialNo1.strip()
                 


                        if(lContNoVBC == 1): 
                                Adminassetserialformatlistsave = Admincategoryidcontinuousnolist(scode =sCodeFinal1AK, lserialno=lContNo)
                                Adminassetserialformatlistsave.save()
                                
                                AdminassetcategorylistGet =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories)
                                 

                                Adminassetcategorylistsave =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
                                Adminassetcategorylistsave.lcontinuousnoa  =lContNo
                                Adminassetcategorylistsave.save()
 


                        if (lSerialNo == 1):
                            Adminassetserialformatlistsave = Adminassetserialformatlist(scode =sCodeFinal1, lserialno=lSerialNo)
                            Adminassetserialformatlistsave.save()
                        else:         
                            AdminassetserialformatlistGet =  Adminassetserialformatlist.objects.filter(scode = sCodeFinal1).values()
                            lIDCodeABC =0
                            if AdminassetserialformatlistGet:
                                for AdminassetserialformatlistGetOBJ in AdminassetserialformatlistGet.all():
                                    lIDCodeABC = AdminassetserialformatlistGetOBJ['lid']

                            Adminassetserialformatlistsave =  Adminassetserialformatlist.objects.get(lid = lIDCodeABC) 
                            Adminassetserialformatlistsave.lserialno =lSerialNo
                            Adminassetserialformatlistsave.save()

 


   
                        lid = 0
                        sinstrumentid = sCodeFinal2
                        sdescription = sCategoryDesc
                        sassettype = sAssetCategory
                        lplantid = lPlantId
                        splanttype = sPlantName
                        lcategoryid = ID_Categories
                        categorytype = sCategorytype
                        assettype = sAssetCategory
                        lassetid = ClassificationData
                        btyperef1 = 0
                        if (styperefnameA1 != ''):
                            btyperef1 = 1
                        scategorytype1 = styperefnameA1
                        styperefname1 = sCodeFlow1
                        btyperef2 = 0
                        if (styperefnameA2 != ''):
                            btyperef2 = 1
                        scategorytype2 = styperefnameA2
                        styperefname2 = sCodeFlow2
                        btyperef3 = 0
                        if (styperefnameA3 != ''):
                            btyperef3 = 1
                        scategorytype3 = styperefnameA3
                        styperefname3 = sCodeFlow3
                        btyperef4 = 0
                        if (styperefnameA4 != ''):
                            btyperef4 = 1
                        scategorytype4 =styperefnameA4
                        styperefname4 = sCodeFlow4
                        btyperef5 = 0
                        if (styperefnameA5 != ''):
                            btyperef5 = 1
                        scategorytype5 = styperefnameA5
                        styperefname5 = sCodeFlow5
                        smake = ""
                        ldefaultlocationid = 0
                        slocationname = ""
                        scurrentstatus = "PURCHASE INITIATED"
                        bcalib = 0
                        dtlastcalib = datetime.now()
                        dtnextcalib = datetime.now()
                        slastcalibdate = ""
                        snextcalibdate = ""

                        slastcalibdate1 = ""
                        snextcalibdate1 = ""
                        slastcalibdate1 = txtLastCalibrationDate
                        if (slastcalibdate1 == ""):
                            slastcalibdate1 = datetime.now()


                        snextcalibdate1 = txtNextCalibrationDate
                        if (snextcalibdate1 == ""):
                            snextcalibdate1 = datetime.now()

                        slastcalibdate2 = ""
                        snextcalibdate2 = ""

                        date_time_Main = datetime.now()
                        # if (slastcalibdate1 == ""):
                        #     slastcalibdate1 = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # if (snextcalibdate1 == ""):
                        #     snextcalibdate1 = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        
                        # slastcalibdate2  = slastcalibdate1.split("-")
                        # snextcalibdate2  = snextcalibdate1.split("-")

                        # slastcalibdate = slastcalibdate2[2] + "-" + slastcalibdate2[1] + "-" + slastcalibdate2[0] 
                        # snextcalibdate = snextcalibdate2[2] + "-" + snextcalibdate2[1] + "-" + snextcalibdate2[0] 

                        # slastcalibdate = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # slastcalibdate = datetime.strftime(date_time_Main, '%d-%m-%Y')
                        # dtlastcalib = datetime.strptime(slastcalibdate, '%d-%m-%Y').date()
                        # dtnextcalib = datetime.strptime(snextcalibdate, '%d-%m-%Y').date()


                        dtcalibdisplaydate = datetime.now()

                        sStatusIdle = "IDLE"

                        ldueday = 0
                        lduemonth = 0
                        ldueyear = 0
                        sfreqtype = ""
                        busagewise = 0
                        lcalibrationvendorid = 0
                        scalibvendor = ""
                        bcheckin = 0
                        busage = 0
                        blimitedusage = 0
                        bdamaged = 0
                        battribute = 0
                        bfreezecalib = 0
                        bvalidation = 0
                        bsentforcalibration = 0
                        oldinstrument_id = ""
                        sinstrumentcode = sCodeFinal2
                        bpurchaseclosed = 0
                        bidlecalibration = 0
                        bsamplepartusage = 0
                        bregularpartusage = 0
                        bcalibstandards = 0
                        spartno = ""
                        lcompanyid = lcompanyid
                        bplanned = 1
                        serpcode = sCodeFinal1
                        lhistorycard = 0
                        lfolowid1 = Flow1Data
                        lfolowid2 = Flow2Data
                        lfolowid3 = Flow3Data
                        lfolowid4 = Flow4Data
                        lfolowid5 = Flow5Data



                        sstoragerack = ""
                        sdrawingno = ""
                        sdrawingrevno = ""
                        sdrawingfile = ""
                        sunitofmeasure = ""
                        srevisionno = ""
                        sproperty = ""
                        scatalogueno = ""
                        frangefrom = 0
                        frangeto = 0
                        fleastcount = 0
                        scheckmethod = ""
                        dtlastservice = datetime.now()
                        dtnextservice = datetime.now()


                        slastservicedate = ""
                        snextservicedate = ""

                        slastservicedate1 = ""
                        snextservicedate1 = ""
                        slastservicedate2 = ""
                        snextservicedate2 = ""


                        slastservicedate = ""
                        snextservicedate = ""
                        smanualduernr = ""
                        ldayremainrnr = 0
                        dtlastrnr = datetime.now()
                        dtnextrnr = datetime.now()
                        slastrnrdate = ""
                        snextrnrdate = ""

                        slastrnrdate1 = ""
                        snextrnrdate1 = ""
                        slastrnrdate2 = ""
                        snextrnrdate2 = ""

                        



                        srange = ""
                        frange3 = 0
                        dcalibrationcost = 0
                        dpurchaseprice = 0
                        smodelno = ""
                        sserialno = ""
                        saccuracy = ""
                        scertificateno = ""
                        straceability = ""
                        ssize1 = ""
                        llusagedefault = 0
                        llusagecount = 0
                        smounted = ""
                        fproducttolerance = 0
                        sproducttolerance = 0
                        facconstant = 0
                        sagencyservice = ""
                        sprocuredate = ""
                        brejected = 0
                        srejecteddate = ""
                        breplaced = 0
                        lreplacedinstrumentid = 0
                        bduechanged = 0
                        dtduechangedate = datetime.now()
                        slastchangedate = datetime.now()
                        blanova = 0
                        srevno = ""
                        scommentchangecalibstd = ""
                        bverifyforpurchase = 0
                        dtsendforverificationforpurchaseon = datetime.now()
                        dtverifiedforpurchaseon = datetime.now()
                        ssendforverificationforpurchaseon = ""
                        sverifiedforpurchaseon = ""
                        spreferredvendor = ""
                        sbondnumber = ""
                        dgo = 0
                        dnogo = 0
                        dtoldiff = 0
                        dtolallowed = 0
                        bmanufacturingstd = 0
                        dplusofminus = 0
                        dz = 0
                        bpartno = 0
                        gageserialno = ""
                        sdrawingno2 = ""
                        lcontinuousnoa2 = 0
                        lcontinuousnob2 = 0
                        lcategorytype1 = 0
                        lcategorytype2 = 0
                        bcustomer = 0
                        lservicealert = 0
                        ferrorallowed = 0
                        splannedby = ""
                        bidchanged = 0
                        scode1 = sCategoryCode
                        scode2 = sGaugeClass
                        scode3 = ""
                        scode4 = ""
                        scode5 = ""
                        ssstatus = ""
                        ssize = ""
                        lintervalservice = 0
                        sintervalperiodservice = ""
                        smanufacturer = ""
                        ddateofprocure = datetime.now()
                        sdateofprocure = ""
                        soperation = ""
                        scompantname = ""
                        lcontinuousnoa1 = 0
                        lcontinuousnob1 = 0
                        lcontinuousnoa = 0
                        lcontinuousnob = 0
                        btyperef = 0
                        btyperefascontinuousnoa = 0
                        btyperefascontinuousnob = 0
                        scomment = ""
                        lpurchasevendorid = 0
                        lservicevendorid = 0
                        sagencycalib = ""
                        scode = sCategoryCode
                        lcurrentlocationid = 0
                        bservice = 0
                        lcalibalert = 0
                        lintervalcalib = 0
                        sintervalperiodcalib = ""
                        lalertinterval = 0
                        ldayremaincalib = 0
                        lusageinterval = 0
                        lusageintervaldisplay = 0
                        lusagecurrent = 0
                        lidlecalibfrequency = 0
                        dtplanneddate = datetime.now()
                        splanneddate = ""
                        dtvalidationlastdate = datetime.now()
                        svalidationlastdate = ""
                        dtvalidationnextdate = datetime.now()
                        svalidationnextdate = ""
                        schangeoldid = ""
                        llusagecountalerts = 0
                        btnextidlecalibration = datetime.now()
                        snextidlecalibration = ""
                        dtidleon = datetime.now()
                        sidleon = ""
                        b1monthvalidation = 0
                        dtnextvalidation = datetime.now()
                        snextvalidation = ""
                        dtlastvalidation = datetime.now()
                        slastvalidation = ""

                        lidA = 0


                         
                        # MasterinstrumentslistSave = Masterinstrumentslist(sinstrumentid  = sinstrumentid )
                        # MasterinstrumentslistSave.save() 
                    
                        # lInstId =0
                        # lInstId = MasterinstrumentslistSave.lid
                    
                        # Masterinstrumentslistpart2Save = Masterinstrumentslistpart2(linstrumentid  = lInstId )
                        # Masterinstrumentslistpart2Save.save()
                   
                        lInstIdA =0
                        lInstIdA = lInstrumentID
                        lInstIdB =0

                        # Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.filter(lcategoryid =ID_Categories).order_by('lid')[:1]
                        # #Masterinstrumentslist_listcOPY =  Masterinstrumentslist.objects.filter(lcategoryid =ID_Categories).order_by('-lid')[:1]
                        # if Masterinstrumentslist_listcOPY:
                        #     for Masterinstrumentslist_listcOPY in Masterinstrumentslist_listcOPY.all():  
                        #         lInstIdB =Masterinstrumentslist_listcOPY.lid 
                        #         sdescription = Masterinstrumentslist_listcOPY.sdescription
                        #         smake = Masterinstrumentslist_listcOPY.smake
                        #         ldefaultlocationid  = Masterinstrumentslist_listcOPY.ldefaultlocationid
                        #         slocationname  = Masterinstrumentslist_listcOPY.slocationname 
                        #         bcalib = Masterinstrumentslist_listcOPY.bcalib   
                        #         sfreqtype = Masterinstrumentslist_listcOPY.sfreqtype
                        #         busagewise = Masterinstrumentslist_listcOPY.busagewise
                        #         lcalibrationvendorid = Masterinstrumentslist_listcOPY.lcalibrationvendorid
                        #         scalibvendor = Masterinstrumentslist_listcOPY.scalibvendor 
                        #         busage = Masterinstrumentslist_listcOPY.busage  
                        #         battribute = Masterinstrumentslist_listcOPY.battribute 
                        #         bvalidation = Masterinstrumentslist_listcOPY.bvalidation   
                        #         bidlecalibration = Masterinstrumentslist_listcOPY.bidlecalibration   
                        #         bsamplepartusage = Masterinstrumentslist_listcOPY.bsamplepartusage   
                        #         bregularpartusage = Masterinstrumentslist_listcOPY.bregularpartusage   
                        #         bcalibstandards = Masterinstrumentslist_listcOPY.bcalibstandards   
                        #         spartno = Masterinstrumentslist_listcOPY.spartno   

                        # Masterinstrumentslist_listcOPY2 =  Masterinstrumentslistpart2.objects.filter(linstrumentid =lInstIdB)
                        # if Masterinstrumentslist_listcOPY2:
                        #     for Masterinstrumentslist_listcOPY2 in Masterinstrumentslist_listcOPY2.all():  
                        #         sstoragerack = Masterinstrumentslist_listcOPY2.sstoragerack 
                        #         sdrawingno = Masterinstrumentslist_listcOPY2.sdrawingno 
                        #         sdrawingrevno = Masterinstrumentslist_listcOPY2.sdrawingrevno 
                        #         sdrawingfile = Masterinstrumentslist_listcOPY2.sdrawingfile 
                        #         sunitofmeasure = Masterinstrumentslist_listcOPY2.sunitofmeasure 
                        #         srevisionno = Masterinstrumentslist_listcOPY2.srevisionno 
                        #         sproperty = Masterinstrumentslist_listcOPY2.sproperty 
                        #         scatalogueno = Masterinstrumentslist_listcOPY2.scatalogueno 
                        #         frangefrom = Masterinstrumentslist_listcOPY2.frangefrom 
                        #         frangeto = Masterinstrumentslist_listcOPY2.frangeto 
                        #         fleastcount = Masterinstrumentslist_listcOPY2.fleastcount 
                        #         scheckmethod = Masterinstrumentslist_listcOPY2.scheckmethod  
                        #         smanualduernr = Masterinstrumentslist_listcOPY2.smanualduernr 
                        #         ldayremainrnr = Masterinstrumentslist_listcOPY2.ldayremainrnr  
                        #         srange = Masterinstrumentslist_listcOPY2.srange 
                        #         frange3 = Masterinstrumentslist_listcOPY2.frange3 
                        #         dcalibrationcost = Masterinstrumentslist_listcOPY2.dcalibrationcost 
                        #         dpurchaseprice = Masterinstrumentslist_listcOPY2.dpurchaseprice 
                                
                        #         saccuracy = Masterinstrumentslist_listcOPY2.saccuracy   
                        #         ssize1 = Masterinstrumentslist_listcOPY2.ssize1 
                        #         llusagedefault = Masterinstrumentslist_listcOPY2.llusagedefault  
                        #         smounted = Masterinstrumentslist_listcOPY2.smounted 
                        #         fproducttolerance = Masterinstrumentslist_listcOPY2.fproducttolerance 
                        #         sproducttolerance = Masterinstrumentslist_listcOPY2.sproducttolerance 
                        #         facconstant = Masterinstrumentslist_listcOPY2.facconstant 
                        #         sagencyservice = Masterinstrumentslist_listcOPY2.sagencyservice 
                                 
                        #         srevno = Masterinstrumentslist_listcOPY2.srevno  
                        #         spreferredvendor = Masterinstrumentslist_listcOPY2.spreferredvendor 
                        #         sbondnumber = Masterinstrumentslist_listcOPY2.sbondnumber 
                        #         dgo = Masterinstrumentslist_listcOPY2.dgo 
                        #         dnogo = Masterinstrumentslist_listcOPY2.dnogo 
                        #         dtoldiff = Masterinstrumentslist_listcOPY2.dtoldiff 
                        #         dtolallowed = Masterinstrumentslist_listcOPY2.dtolallowed 
                        #         bmanufacturingstd = Masterinstrumentslist_listcOPY2.bmanufacturingstd 
                        #         dplusofminus = Masterinstrumentslist_listcOPY2.dplusofminus 
                        #         dz = Masterinstrumentslist_listcOPY2.dz 
                                
                        #         sdrawingno2 = Masterinstrumentslist_listcOPY2.sdrawingno2   
                        #         ferrorallowed = Masterinstrumentslist_listcOPY2.ferrorallowed 
                        #         splannedby = Masterinstrumentslist_listcOPY2.splannedby   
                        #         ssize = Masterinstrumentslist_listcOPY2.ssize  
                        #         smanufacturer = Masterinstrumentslist_listcOPY2.smanufacturer       
                        #         lpurchasevendorid = Masterinstrumentslist_listcOPY2.lpurchasevendorid 
                        #         lservicevendorid = Masterinstrumentslist_listcOPY2.lservicevendorid 
                        #         sagencycalib = Masterinstrumentslist_listcOPY2.sagencycalib  
                        #         lcalibalert = Masterinstrumentslist_listcOPY2.lcalibalert 
                        #         lintervalcalib = Masterinstrumentslist_listcOPY2.lintervalcalib 
                        #         sintervalperiodcalib = Masterinstrumentslist_listcOPY2.sintervalperiodcalib 
                        #         lalertinterval = Masterinstrumentslist_listcOPY2.lalertinterval  
                        #         lusageinterval = Masterinstrumentslist_listcOPY2.lusageinterval 
                        #         lusageintervaldisplay = Masterinstrumentslist_listcOPY2.lusageintervaldisplay  
                        #         lidlecalibfrequency = Masterinstrumentslist_listcOPY2.lidlecalibfrequency   
                        #         llusagecountalerts = Masterinstrumentslist_listcOPY2.llusagecountalerts  
                        #         b1monthvalidation = Masterinstrumentslist_listcOPY2.b1monthvalidation  



                        Masterinstrumentslist_listSaveUpdate =  Masterinstrumentslist.objects.get(lid =lInstrumentID) 
                    

                        Masterinstrumentslist_listSaveUpdate.sinstrumentid = sCodeFinal2
                        Masterinstrumentslist_listSaveUpdate.sdescription = sdescription
                        Masterinstrumentslist_listSaveUpdate.sassettype = sAssetCategory
                        # Masterinstrumentslist_listSaveUpdate.lplantid = lPlantId
                        # Masterinstrumentslist_listSaveUpdate.splanttype = sPlantName
                        Masterinstrumentslist_listSaveUpdate.lcategoryid = ID_Categories
                        Masterinstrumentslist_listSaveUpdate.categorytype = sCategorytype
                        Masterinstrumentslist_listSaveUpdate.assettype = sAssetCategory
                        Masterinstrumentslist_listSaveUpdate.lassetid = ClassificationData
                        Masterinstrumentslist_listSaveUpdate.btyperef1 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype1 = styperefnameA1
                        Masterinstrumentslist_listSaveUpdate.styperefname1 = sCodeFlow1
                        Masterinstrumentslist_listSaveUpdate.btyperef2 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype2 = styperefnameA2
                        Masterinstrumentslist_listSaveUpdate.styperefname2 = sCodeFlow2
                        Masterinstrumentslist_listSaveUpdate.btyperef3 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype3 = styperefnameA3
                        Masterinstrumentslist_listSaveUpdate.styperefname3 = sCodeFlow3
                        Masterinstrumentslist_listSaveUpdate.btyperef4 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype4 =styperefnameA4
                        Masterinstrumentslist_listSaveUpdate.styperefname4 = sCodeFlow4
                        Masterinstrumentslist_listSaveUpdate.btyperef5 = 0 
                        Masterinstrumentslist_listSaveUpdate.scategorytype5 = styperefnameA5
                        Masterinstrumentslist_listSaveUpdate.styperefname5 = sCodeFlow5
                        # Masterinstrumentslist_listSaveUpdate.smake = smake
                        # Masterinstrumentslist_listSaveUpdate.ldefaultlocationid = ldefaultlocationid
                        # Masterinstrumentslist_listSaveUpdate.slocationname = slocationname
                        Masterinstrumentslist_listSaveUpdate.scurrentstatus = sStatusIdle
                        # Masterinstrumentslist_listSaveUpdate.bcalib = bcalib
                        Masterinstrumentslist_listSaveUpdate.dtlastcalib = dtlastcalib
                        Masterinstrumentslist_listSaveUpdate.dtnextcalib = dtnextcalib
                        Masterinstrumentslist_listSaveUpdate.slastcalibdate = slastcalibdate
                        Masterinstrumentslist_listSaveUpdate.snextcalibdate = snextcalibdate
                        Masterinstrumentslist_listSaveUpdate.dtcalibdisplaydate = dtnextcalib  + timedelta(days=15)
                        Masterinstrumentslist_listSaveUpdate.ldueday = dtnextcalib.day
                        Masterinstrumentslist_listSaveUpdate.lduemonth = dtnextcalib.month
                        Masterinstrumentslist_listSaveUpdate.ldueyear = dtnextcalib.year
                        # Masterinstrumentslist_listSaveUpdate.sfreqtype = sfreqtype
                        # Masterinstrumentslist_listSaveUpdate.busagewise = busagewise
                        # Masterinstrumentslist_listSaveUpdate.lcalibrationvendorid = lcalibrationvendorid
                        # Masterinstrumentslist_listSaveUpdate.scalibvendor = scalibvendor
                        # Masterinstrumentslist_listSaveUpdate.bcheckin = 0
                        # Masterinstrumentslist_listSaveUpdate.busage = busage
                        # Masterinstrumentslist_listSaveUpdate.blimitedusage = 0
                        # Masterinstrumentslist_listSaveUpdate.bdamaged = 0
                        # Masterinstrumentslist_listSaveUpdate.battribute = battribute
                        # Masterinstrumentslist_listSaveUpdate.bfreezecalib = 0
                        # Masterinstrumentslist_listSaveUpdate.bvalidation = bvalidation
                        # Masterinstrumentslist_listSaveUpdate.bsentforcalibration = 0
                        # Masterinstrumentslist_listSaveUpdate.oldinstrument_id = ""
                        Masterinstrumentslist_listSaveUpdate.sinstrumentcode = sinstrumentcode
                        Masterinstrumentslist_listSaveUpdate.bpurchaseclosed = bpurchaseclosed
                        Masterinstrumentslist_listSaveUpdate.bsapcodegenerate = 1

                        Masterinstrumentslist_listSaveUpdate.bidlecalibration = 0
                        Masterinstrumentslist_listSaveUpdate.bcalibrateidle = 0
                        if(bCalibrateWhenIdle == 1):
                            Masterinstrumentslist_listSaveUpdate.bidlecalibration = 1
                            Masterinstrumentslist_listSaveUpdate.bcalibrateidle = 1
                        # Masterinstrumentslist_listSaveUpdate.bsamplepartusage = bsamplepartusage
                        # Masterinstrumentslist_listSaveUpdate.bregularpartusage = bregularpartusage
                        # Masterinstrumentslist_listSaveUpdate.bcalibstandards = bcalibstandards
                        Masterinstrumentslist_listSaveUpdate.spartno = spartno
                        # Masterinstrumentslist_listSaveUpdate.lcompanyid = lcompanyid
                        # Masterinstrumentslist_listSaveUpdate.bplanned = bplanned
                        Masterinstrumentslist_listSaveUpdate.serpcode = serpcode
                        # Masterinstrumentslist_listSaveUpdate.lhistorycard = 0
                        Masterinstrumentslist_listSaveUpdate.lfolowid1 = lfolowid1
                        Masterinstrumentslist_listSaveUpdate.lfolowid2 = lfolowid2
                        Masterinstrumentslist_listSaveUpdate.lfolowid3 = lfolowid3
                        Masterinstrumentslist_listSaveUpdate.lfolowid4 = lfolowid4
                        Masterinstrumentslist_listSaveUpdate.lfolowid5 = lfolowid5
                        # Masterinstrumentslist_listSaveUpdate.ltolid = 0
                        # Masterinstrumentslist_listSaveUpdate.sissueddate = ""
                        # Masterinstrumentslist_listSaveUpdate.sreturneddate = ""

                        Masterinstrumentslist_listSaveUpdate.save()


                        # Masterinstrumentslistpart2SaveUpdate =  Masterinstrumentslistpart2.objects.get(lid =lInstIdA) 
 




                        # Masterinstrumentslistpart2SaveUpdate.sstoragerack =sstoragerack
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingno = sdrawingno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingrevno = sdrawingrevno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingfile =sdrawingfile
                        # Masterinstrumentslistpart2SaveUpdate.sunitofmeasure = sunitofmeasure
                        # Masterinstrumentslistpart2SaveUpdate.srevisionno = srevisionno
                        # Masterinstrumentslistpart2SaveUpdate.sproperty = sproperty
                        # Masterinstrumentslistpart2SaveUpdate.scatalogueno = scatalogueno
                        # Masterinstrumentslistpart2SaveUpdate.frangefrom = frangefrom
                        # Masterinstrumentslistpart2SaveUpdate.frangeto = frangeto
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.fleastcount = fleastcount
                        # Masterinstrumentslistpart2SaveUpdate.scheckmethod = scheckmethod
                        # Masterinstrumentslistpart2SaveUpdate.dtlastservice = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtnextservice = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastservicedate = ""
                        # Masterinstrumentslistpart2SaveUpdate.snextservicedate = ""
                        # Masterinstrumentslistpart2SaveUpdate.smanualduernr = smanualduernr
                        # Masterinstrumentslistpart2SaveUpdate.ldayremainrnr = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtlastrnr = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtnextrnr = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastrnrdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.snextrnrdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.srange = srange
                        # Masterinstrumentslistpart2SaveUpdate.frange3 = frange3
                        # Masterinstrumentslistpart2SaveUpdate.dcalibrationcost = dcalibrationcost
                        # Masterinstrumentslistpart2SaveUpdate.dpurchaseprice = dpurchaseprice
                        # Masterinstrumentslistpart2SaveUpdate.smodelno = ""
                        # Masterinstrumentslistpart2SaveUpdate.sserialno = ""
                        # Masterinstrumentslistpart2SaveUpdate.saccuracy = saccuracy
                        # Masterinstrumentslistpart2SaveUpdate.scertificateno = ""
                        # Masterinstrumentslistpart2SaveUpdate.straceability = ""
                        # Masterinstrumentslistpart2SaveUpdate.ssize1 =ssize1
                        # Masterinstrumentslistpart2SaveUpdate.llusagedefault = llusagedefault
                        # Masterinstrumentslistpart2SaveUpdate.llusagecount = llusagecount
                        # Masterinstrumentslistpart2SaveUpdate.smounted = smounted
                        # Masterinstrumentslistpart2SaveUpdate.fproducttolerance = fproducttolerance
                        # Masterinstrumentslistpart2SaveUpdate.sproducttolerance = sproducttolerance
                        # Masterinstrumentslistpart2SaveUpdate.facconstant = facconstant
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.sagencyservice = sagencyservice
                        # Masterinstrumentslistpart2SaveUpdate.sprocuredate = ddateofprocure.strftime("%m/%d/%Y")
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.brejected = 0
                        # Masterinstrumentslistpart2SaveUpdate.srejecteddate = ""
                        # Masterinstrumentslistpart2SaveUpdate.breplaced = 0
                        # Masterinstrumentslistpart2SaveUpdate.lreplacedinstrumentid = 0
                        # Masterinstrumentslistpart2SaveUpdate.bduechanged = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtduechangedate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastchangedate =  ""
                        # Masterinstrumentslistpart2SaveUpdate.blanova = 0
                        # Masterinstrumentslistpart2SaveUpdate.srevno = srevno
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.scommentchangecalibstd = scommentchangecalibstd
                        # Masterinstrumentslistpart2SaveUpdate.bverifyforpurchase = 0
                        # Masterinstrumentslistpart2SaveUpdate.dtsendforverificationforpurchaseon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.dtverifiedforpurchaseon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.ssendforverificationforpurchaseon = ""
                        # Masterinstrumentslistpart2SaveUpdate.sverifiedforpurchaseon = ""
                        # Masterinstrumentslistpart2SaveUpdate.spreferredvendor = spreferredvendor
                        # Masterinstrumentslistpart2SaveUpdate.sbondnumber = sbondnumber
                        # Masterinstrumentslistpart2SaveUpdate.dgo = dgo
                        # Masterinstrumentslistpart2SaveUpdate.dnogo = dnogo
                        # Masterinstrumentslistpart2SaveUpdate.dtoldiff = dtoldiff
                        # Masterinstrumentslistpart2SaveUpdate.dtolallowed = dtolallowed
                        # Masterinstrumentslistpart2SaveUpdate.bmanufacturingstd = bmanufacturingstd
                        # Masterinstrumentslistpart2SaveUpdate.dplusofminus = dplusofminus
                        # Masterinstrumentslistpart2SaveUpdate.dz = dz
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.bpartno =bpartno
                        # Masterinstrumentslistpart2SaveUpdate.gageserialno = gageserialno
                        # Masterinstrumentslistpart2SaveUpdate.sdrawingno2 = sdrawingno2
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa2 = lcontinuousnoa2
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob2 = lcontinuousnob2
                        # Masterinstrumentslistpart2SaveUpdate.lcategorytype1 = lcategorytype1
                        # Masterinstrumentslistpart2SaveUpdate.lcategorytype2 = lcategorytype2
                        # Masterinstrumentslistpart2SaveUpdate.bcustomer = bcustomer
                        # Masterinstrumentslistpart2SaveUpdate.lservicealert = lservicealert
                        # Masterinstrumentslistpart2SaveUpdate.ferrorallowed = ferrorallowed
                        # Masterinstrumentslistpart2SaveUpdate.splannedby = request.session['semployeename'] 
                        # Masterinstrumentslistpart2SaveUpdate.bidchanged = 0
                        # Masterinstrumentslistpart2SaveUpdate.scode1 = scode1
                        # Masterinstrumentslistpart2SaveUpdate.scode2 = scode2
                        # Masterinstrumentslistpart2SaveUpdate.scode3 = scode3
                        # Masterinstrumentslistpart2SaveUpdate.scode4 = scode4
                        # Masterinstrumentslistpart2SaveUpdate.scode5 = scode5
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.ssstatus = scurrentstatus
                        # Masterinstrumentslistpart2SaveUpdate.ssize = ssize
                        # Masterinstrumentslistpart2SaveUpdate.lintervalservice = lintervalservice
                        # Masterinstrumentslistpart2SaveUpdate.sintervalperiodservice = sintervalperiodservice
                        # Masterinstrumentslistpart2SaveUpdate.smanufacturer = smanufacturer
                        # Masterinstrumentslistpart2SaveUpdate.ddateofprocure = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.sdateofprocure = ""
                        # Masterinstrumentslistpart2SaveUpdate.soperation = soperation
                        # Masterinstrumentslistpart2SaveUpdate.scompantname = scompantname
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa1 = lcontinuousnoa1
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob1 = lcontinuousnob1
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnoa = lcontinuousnoa
                        # Masterinstrumentslistpart2SaveUpdate.lcontinuousnob = lcontinuousnob
                        # Masterinstrumentslistpart2SaveUpdate.btyperef = btyperef
                        # Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnoa = btyperefascontinuousnoa
                        # Masterinstrumentslistpart2SaveUpdate.btyperefascontinuousnob = btyperefascontinuousnob
                        # Masterinstrumentslistpart2SaveUpdate.scomment = ""
                        # Masterinstrumentslistpart2SaveUpdate.lpurchasevendorid = lpurchasevendorid
                        # Masterinstrumentslistpart2SaveUpdate.lservicevendorid = lservicevendorid
                        # Masterinstrumentslistpart2SaveUpdate.sagencycalib = sagencycalib
                        # Masterinstrumentslistpart2SaveUpdate.scode = scode
                        # Masterinstrumentslistpart2SaveUpdate.lcurrentlocationid = lcurrentlocationid
                        # Masterinstrumentslistpart2SaveUpdate.bservice = bservice
                        # Masterinstrumentslistpart2SaveUpdate.lcalibalert = lcalibalert
                        # Masterinstrumentslistpart2SaveUpdate.lintervalcalib = lintervalcalib
                        # Masterinstrumentslistpart2SaveUpdate.sintervalperiodcalib = sintervalperiodcalib
                        # Masterinstrumentslistpart2SaveUpdate.lalertinterval = lalertinterval
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.ldayremaincalib = 0
                        # Masterinstrumentslistpart2SaveUpdate.lusageinterval = lusageinterval
                        # Masterinstrumentslistpart2SaveUpdate.lusageintervaldisplay = lusageintervaldisplay
                        # Masterinstrumentslistpart2SaveUpdate.lusagecurrent = 0
                        # Masterinstrumentslistpart2SaveUpdate.lidlecalibfrequency = lidlecalibfrequency
                        # Masterinstrumentslistpart2SaveUpdate.dtplanneddate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.splanneddate = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtvalidationlastdate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.svalidationlastdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtvalidationnextdate = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.svalidationnextdate = ""
                        # Masterinstrumentslistpart2SaveUpdate.schangeoldid = ""
                        # Masterinstrumentslistpart2SaveUpdate.llusagecountalerts = llusagecountalerts
                        # Masterinstrumentslistpart2SaveUpdate.btnextidlecalibration = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.snextidlecalibration = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtidleon = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.sidleon = ""
                        # Masterinstrumentslistpart2SaveUpdate.b1monthvalidation = b1monthvalidation
                        # Masterinstrumentslistpart2SaveUpdate.dtnextvalidation = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.save()
                        # Masterinstrumentslistpart2SaveUpdate.snextvalidation = ""
                        # Masterinstrumentslistpart2SaveUpdate.dtlastvalidation = datetime.now()
                        # Masterinstrumentslistpart2SaveUpdate.slastvalidation = ""



                        # Masterinstrumentslistpart2SaveUpdate.save()
  
                        


 
 


                        sCreatedBy = ""

                        sCreatedBy = request.session['semployeename'] + " (" + request.session['semployeeno']  + ") "



                        sNewSAPCode = "NO"
                        if (bNewIDwithfirstSerial == 1):
                            sNewSAPCode = "YES"
                        
                        sCompanyName = ""
                        sCompanyName =   "Maini Group - " + sPlantNameName
                        #Admin1Companyinfo_list =  Admin1Companyinfo.objects.get(lid=1)
                        #if (Admin1C
                        request.session['sSAPCode']  = sNewSAPCode
                        return redirect("GaugeMasterlistDetails", lID=lInstrumentID)
                        #return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserIDPrint.html', 
                        #{
                            #'title':'User list', 
                            #'sCompanyName':sCompanyName, 
                            #'sPlantName':sPlantNameNameA, 
                            #'sPlantCode':sPlantCode[:2],
                            #'sAssetCode':  sCodeFinal1, 
                            #'sNewSAPCode':sNewSAPCode,
                            #'sCodeDescription':sCodeDescription,
                            #'sFlow1':sFlow1,
                            #'sFlow2':sFlow2,
                            #'sFlow3':sFlow3,
                            #'sFlow4':sFlow4,
                            #'sFlow5':sFlow5,
                            #'sFlowDesc1':sCodeFlow1.strip(),
                            #'sFlowDesc2':sCodeFlow2.strip(),
                            #'sFlowDesc3':sCodeFlow3.strip(),
                            #'sFlowDesc4':sCodeFlow4.strip(),
                            #'sFlowDesc5':sCodeFlow5.strip(),
                            #'sDate':datetime.now(),
                            #'sCreatedBy':sCreatedBy,
                        #}) 

                        #template = get_template('CloudCaliber/GaugeMasterlistCreateOLDUserIDPrint.html')
                        # context = {
                        #     'title':'Print New SAP Code', 
                        #     'sCompanyName':sCompanyName, 
                        #     'sPlantName':sPlantNameNameA, 
                        #     'sPlantCode':sPlantCode[:2],
                        #     'sAssetCode':  sCodeFinal1, 
                        #     'sNewSAPCode':sNewSAPCode,
                        #     'sCodeDescription':sCodeDescription,
                        #     'sFlow1':styperefnameA1,
                        #     'sFlow2':styperefnameA2,
                        #     'sFlow3':styperefnameA3,
                        #     'sFlow4':styperefnameA4,
                        #     'sFlow5':styperefnameA5,
                        #     'sFlowDesc1':sCodeFlow1.strip(),
                        #     'sFlowDesc2':sCodeFlow2.strip(),
                        #     'sFlowDesc3':sCodeFlow3.strip(),
                        #     'sFlowDesc4':sCodeFlow4.strip(),
                        #     'sFlowDesc5':sCodeFlow5.strip(),
                        #     'sDate':datetime.now(),
                        #     'sCreatedBy':sCreatedBy,
                        # }
                        # pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateIDPrint.html', context)
                        # return HttpResponse(pdf, content_type='application/pdf')
                        # html = template.render(context)
                        # pdf = render_to_pdf('CloudCaliber/GaugeMasterlistCreateOLDUserIDPrint.html', context)
                        # if pdf:
                        #     response = HttpResponse(pdf, content_type='application/pdf')

                        # filename = "GaugeSAPCode_" + sCodeFinal1 + str(ddateofprocure.day) + str(ddateofprocure.monthth) + str(ddateofprocure.year)  + ".pdf"  
                        # content = "inline; filename='%s'" %(filename)
                        # download = request.GET.get("download")
                        # if download:
                        #     content = "attachment; filename='%s'" %(filename)
                        #     response['Content-Disposition'] = content
                        #     return response
                        # return HttpResponse("Not found")



        data = request.POST
        if 'Classification' in request.POST:
            cmbClassificationID=request.POST['Classification'] 

        if 'Category' in request.POST:
            cmbCategoryID=request.POST['Category'] 

        if 'getFlow1' in request.POST:
            cmbgetFlow1ID=request.POST['getFlow1'] 


        #request.session['cmbClassificationID'] =cmbClassificationID
        #request.session['cmbCategoryID'] =cmbCategoryID
        #request.session['cmbgetFlow1ID'] =cmbgetFlow1ID
        #request.session['cmbgetFlow2ID'] =cmbgetFlow2ID
        #request.session['cmbgetFlow3ID'] =cmbgetFlow3ID
        #request.session['cmbgetFlow4ID'] =cmbgetFlow4ID
        #request.session['cmbgetFlow5ID'] =cmbgetFlow5ID
        #request.session['cmbgetFlow6ID'] =cmbgetFlow6ID
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10
        
        #request.session['sCategoryCode'] = sCategoryCode
        #request.session['lcontinuousnob'] = lcontinuousnob
        #request.session['bFlow'] = bFlow
        #request.session['sFlowName'] = sFlowName
        #request.session['lcontinuousnoa'] = lcontinuousnoa
        #request.session['bFlow1'] = bFlow1
        #request.session['sFlowName1'] = sFlowName1
        #request.session['lcontinuousnoa1'] = lcontinuousnoa1
        #request.session['bFlow2'] = bFlow2
        #request.session['sFlowName2'] = sFlowName2
        #request.session['lcontinuousnoa2'] = lcontinuousnoa2
        #request.session['bFlow3'] = bFlow3
        #request.session['sFlowName3'] = sFlowName3
        #request.session['lcontinuousnoa3'] = lcontinuousnoa3
        #request.session['bFlow4'] = bFlow4
        #request.session['sFlowName4'] = sFlowName4
        #request.session['lcontinuousnoa4'] = lcontinuousnoa4
        #request.session['bFlow5'] = bFlow5
        #request.session['sFlowName5'] = sFlowName5
        #request.session['lcontinuousnoa5'] = lcontinuousnoa5
        #request.session['bFlow6'] = bFlow6
        #request.session['sFlowName6'] = sFlowName6
        #request.session['lcontinuousnoa6'] = lcontinuousnoa6
        #request.session['bFlow7'] = bFlow7
        #request.session['sFlowName7'] = sFlowName7
        #request.session['lcontinuousnoa7'] = lcontinuousnoa7
        #request.session['bFlow8'] = bFlow8
        #request.session['sFlowName8'] = sFlowName8
        #request.session['lcontinuousnoa8'] = lcontinuousnoa8
        #request.session['bFlow9'] = bFlow9
        #request.session['sFlowName9'] = sFlowName9
        #request.session['lcontinuousnoa9'] = lcontinuousnoa9
        #request.session['bFlow10'] = bFlow10
        #request.session['sFlowName10'] = sFlowName10
        #request.session['lcontinuousnoa10'] = lcontinuousnoa10

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
  
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

        
        return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserID.html', 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sCodeFinal1': "" ,  
            'sCodeFinal2': "" ,  
            'cmbClassificationID': 0 , 
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
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

            
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)



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
        Masterinstrumentslist_list =  Masterinstrumentslist.objects.values().get(lid=lInstrumentID)

    
        return render(request,  'CloudCaliber/GaugeMasterlistCreateOLDUserID.html', 
        {
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,  
            'title':'User list', 
            'message':'Your User list page.',
            'sPlantName': sPlantName ,  
            'semployeename':semployeename,
            'sLastDate':sLastDate,  
            'sNextDate':sNextDate,
            'bcalibrateidle':bcalibrateidle, 
            'bsapcodegenerate':bsapcodegenerate,
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
            'Admintoleranceclasslist_list':Admintoleranceclasslist_list,
            'Masterinstrumentslist_listA':Masterinstrumentslist_list,
        })







@csrf_exempt
def GMlistClassificationCreate_ID(request):
    cmbClassificationID = request.GET.get('cmbClassificationID', None)
    data = { 
        'is_taken1': Adminassetcategorylist.objects.filter(lassetid=cmbClassificationID).values()
    } 
        #data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


    
@csrf_exempt
def load_GMlistClassificationCreate_ID(request):

    sCodeFinal1 = ""
    sCodeFinal2 = ""

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
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



    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisCategoryCreate_ID(request):

    
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

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2

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
    if (sFlowName1 != ''):
        bFlow1 = 1

    sFlowName2  = AdminassetcategorylistActive.styperefname2
    if (sFlowName2 != ''):
        bFlow2 = 1

    sFlowName3  = AdminassetcategorylistActive.styperefname3
    if (sFlowName3 != ''):
        bFlow3 = 1

    sFlowName4  = AdminassetcategorylistActive.styperefname4
    if (sFlowName4 != ''):
        bFlow4 = 1

    sFlowName5  = AdminassetcategorylistActive.styperefname5
    if (sFlowName5 != ''):
        bFlow5 = 1

    sFlowName6  = AdminassetcategorylistActive.styperefname6
    if (sFlowName6 != ''):
        bFlow6 = 1

    sFlowName7  = AdminassetcategorylistActive.styperefname7
    if (sFlowName7 != ''):
        bFlow7 = 1

    sFlowName8  = AdminassetcategorylistActive.styperefname8
    if (sFlowName8 != ''):
        bFlow8 = 1
    
    sFlowName9  = AdminassetcategorylistActive.styperefname9
    if (sFlowName9 != ''):
        bFlow9 = 1

    sFlowName10  = AdminassetcategorylistActive.styperefname10 
    if (sFlowName10 != ''):
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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')
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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow1Create_ID(request):

    
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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
   
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass') 

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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow2Create_ID(request):

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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')

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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow3Create_ID(request):

    
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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2

    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')    

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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow4Create_ID(request):

    
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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')    

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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow5Create_ID(request):

    
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
    

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')    


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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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
def load_GMlisFlow6Create_ID(request):

    request.session['sCategoryCode'] = ""
    request.session['categorytype'] = ""
    request.session['styperefnameA1'] = ""
    request.session['styperefnameA2'] = ""
    request.session['styperefnameA3'] = ""
    request.session['styperefnameA4'] = ""
    request.session['styperefnameA5'] = "" 
    
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


    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2
    
    Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')    

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
            'Admintoleranceclasslist_list': Admintoleranceclasslist_list,
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






def load_Code_FlowValue1(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
    
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories


    sCodeSelected = request.GET.get('sCode')
    if (sCodeSelected == "0"):
        sCodeSelected = ""
    
    sCodeSelected = sCodeSelected.strip()

    s1 = sCodeSelected.split(" ")
    s2 = ""
    
    if (len(s1) == 1):
        s2 = s1[0]
    elif (len(s1) == 2):
        s2 = s1[1]
    elif (len(s1) == 3):
        s2 = s1[2]
    elif (len(s1) == 4):
        s2 = s1[3]
    elif (len(s1) == 5):
        s2 = s1[4]
    elif (len(s1) == 6):
        s2 = s1[5]
    elif (len(s1) == 7):
        s2 = s1[6]
    elif (len(s1) == 8):
        s2 = s1[7]
    elif (len(s1) == 9):
        s2 = s1[8]
    elif (len(s1) == 10):
        s2 = s1[9]
 

    request.session['sFlowCode1a']  = s1[0] 
    request.session['sFlowCode1']  = s2 
    s3 = request.session['sFlowCode1']  

    sCodeFinal1 = ""
    sCodeFinal2 = ""
    
    sClasscode = request.session['sClasscode']  

    sCategoryCode = request.session['sCategoryCode'] 
    
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
 

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno

    request.session['sPlantCode']   =sPlantCode

 
    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 

    
    sFlowCode1 = s2
    sFlowCode2 = "" 
    sFlowCode3 ="" 
    sFlowCode4 = ""
    sFlowCode5 = "" 

    
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa
 



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB

    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0


    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""
    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   

    lSerialNo =0
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


    lSerialNo = lSerialNo +1

    request.session['lSerialNo'] = lSerialNo

    
    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1


    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial


    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()
 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })



def load_Code_FlowValue2(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
    
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories


    sCodeSelected = request.GET.get('sCode')
    if (sCodeSelected == "0"):
        sCodeSelected = ""
    
    sCodeSelected = sCodeSelected.strip()

    s1 = sCodeSelected.split(" ")
    s2 = ""
    
    if (len(s1) == 1):
        s2 = s1[0]
    elif (len(s1) == 2):
        s2 = s1[1]
    elif (len(s1) == 3):
        s2 = s1[2]
    elif (len(s1) == 4):
        s2 = s1[3]
    elif (len(s1) == 5):
        s2 = s1[4]
    elif (len(s1) == 6):
        s2 = s1[5]
    elif (len(s1) == 7):
        s2 = s1[6]
    elif (len(s1) == 8):
        s2 = s1[7]
    elif (len(s1) == 9):
        s2 = s1[8]
    elif (len(s1) == 10):
        s2 = s1[9]
 

    request.session['sFlowCode2a']  = s1[0] 
    request.session['sFlowCode2']   = s2

    sCodeFinal1 = ""
    sCodeFinal2 = ""
    
    sClasscode = request.session['sClasscode']  

    sCategoryCode = request.session['sCategoryCode'] 
    
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
 

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode


    sFlowCode1 = request.session['sFlowCode1'] 
    sFlowCode2 = s2
    sFlowCode3 ="" 
    sFlowCode4 = ""
    sFlowCode5 = "" 
 
 
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB


    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0



    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""

    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   

    lSerialNo =0
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


    lSerialNo = lSerialNo +1

    
    request.session['lSerialNo'] = lSerialNo

    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1

    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial

    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()
 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })


def load_Code_FlowValue3(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
    
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories


    sCodeSelected = request.GET.get('sCode')
    if (sCodeSelected == "0"):
        sCodeSelected = ""
    
    sCodeSelected = sCodeSelected.strip()

    s1 = sCodeSelected.split(" ")
    s2 = ""
    
    if (len(s1) == 1):
        s2 = s1[0]
    elif (len(s1) == 2):
        s2 = s1[1]
    elif (len(s1) == 3):
        s2 = s1[2]
    elif (len(s1) == 4):
        s2 = s1[3]
    elif (len(s1) == 5):
        s2 = s1[4]
    elif (len(s1) == 6):
        s2 = s1[5]
    elif (len(s1) == 7):
        s2 = s1[6]
    elif (len(s1) == 8):
        s2 = s1[7]
    elif (len(s1) == 9):
        s2 = s1[8]
    elif (len(s1) == 10):
        s2 = s1[9]
 

    request.session['sFlowCode3a']  = s1[0] 
    request.session['sFlowCode3']   = s2

    sClasscode = request.session['sClasscode']  

    sCategoryCode = request.session['sCategoryCode'] 
    
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
 

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode


    sFlowCode1 = request.session['sFlowCode1'] 
    sFlowCode2 = request.session['sFlowCode2']
    sFlowCode3 = s2  
    sFlowCode4 = ""
    sFlowCode5 = "" 
 
 
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB

    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0


    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""

    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   

    lSerialNo =0
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']

    lSerialNo = lSerialNo +1

    
    request.session['lSerialNo'] = lSerialNo

    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1

    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial

    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()
 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })




def load_Code_FlowValue4(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
  
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories  


    sCodeSelected = request.GET.get('sCode')
    if (sCodeSelected == "0"):
        sCodeSelected = ""
    
    sCodeSelected = sCodeSelected.strip()

    s1 = sCodeSelected.split(" ")
    s2 = ""
    
    if (len(s1) == 1):
        s2 = s1[0]
    elif (len(s1) == 2):
        s2 = s1[1]
    elif (len(s1) == 3):
        s2 = s1[2]
    elif (len(s1) == 4):
        s2 = s1[3]
    elif (len(s1) == 5):
        s2 = s1[4]
    elif (len(s1) == 6):
        s2 = s1[5]
    elif (len(s1) == 7):
        s2 = s1[6]
    elif (len(s1) == 8):
        s2 = s1[7]
    elif (len(s1) == 9):
        s2 = s1[8]
    elif (len(s1) == 10):
        s2 = s1[9]
 

    request.session['sFlowCode4a']  = s1[0] 
    request.session['sFlowCode4']   = s2

    sClasscode = request.session['sClasscode']  

    sCategoryCode = request.session['sCategoryCode'] 
    
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
 

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode


    sFlowCode1 = request.session['sFlowCode1'] 
    sFlowCode2 = request.session['sFlowCode2']
    sFlowCode3 = request.session['sFlowCode3']
    sFlowCode4 = s2
    sFlowCode5 = "" 
 
 
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB

    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0


    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""

    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   

    lSerialNo =0
    
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']

    lSerialNo = lSerialNo +1

    request.session['lSerialNo'] = lSerialNo

    
    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1

    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial

    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()
 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })





def load_Code_FlowValue5(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
    
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories


    sCodeSelected = request.GET.get('sCode')
    if (sCodeSelected == "0"):
        sCodeSelected = ""
    
    sCodeSelected = sCodeSelected.strip()

    s1 = sCodeSelected.split(" ")
    s2 = ""
    
    if (len(s1) == 1):
        s2 = s1[0]
    elif (len(s1) == 2):
        s2 = s1[1]
    elif (len(s1) == 3):
        s2 = s1[2]
    elif (len(s1) == 4):
        s2 = s1[3]
    elif (len(s1) == 5):
        s2 = s1[4]
    elif (len(s1) == 6):
        s2 = s1[5]
    elif (len(s1) == 7):
        s2 = s1[6]
    elif (len(s1) == 8):
        s2 = s1[7]
    elif (len(s1) == 9):
        s2 = s1[8]
    elif (len(s1) == 10):
        s2 = s1[9]
 

    request.session['sFlowCode5a']  = s1[0] 
    request.session['sFlowCode5']   = s2

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
 

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode

    sClasscode = request.session['sClasscode']  

    sCategoryCode = request.session['sCategoryCode'] 
    

    sFlowCode1 = request.session['sFlowCode1'] 
    sFlowCode2 = request.session['sFlowCode2']
    sFlowCode3 = request.session['sFlowCode3']
    sFlowCode4 = request.session['sFlowCode4']
    sFlowCode5 = s2
 
  
 
 
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB

    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0


    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""

    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   

    lSerialNo =0
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


    lSerialNo = lSerialNo +1

    request.session['lSerialNo'] = lSerialNo

    
    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1

    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial

    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()
 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })



def load_Classification_Details(request):
    
    request.session['sCategoryCode'] = ""
    request.session['categorytype'] = ""
    request.session['styperefnameA1'] = ""
    request.session['styperefnameA2'] = ""
    request.session['styperefnameA3'] = ""
    request.session['styperefnameA4'] = ""
    request.session['styperefnameA5'] = ""
    request.session['sFlowCode1']   =""
    request.session['sFlowCode2']   =""
    request.session['sFlowCode3']   =""
    request.session['sFlowCode4']   =""
    request.session['sFlowCode5']   =""

    if request.method == 'GET':
        ID_Categories = request.GET.get('IDCategories')
        Adminassettypelist_list =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ID_Categories) 
        #data = [{'name': 'Peter', 'email': 'peter@example.org'},
                #{'name': 'Julia', 'email': 'julia@example.org'}]
        data = [{'scode': Adminassettypelist_list.scode.strip()} ]
        
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

 

        sCategoryCode = ""

        request.session['sCategoryCode'] = ""
        request.session['categorytype'] = ""
        request.session['styperefnameA1'] = ""
        request.session['styperefnameA2'] = ""
        request.session['styperefnameA3'] = ""
        request.session['styperefnameA4'] = ""
        request.session['styperefnameA5'] = ""
        styperefnameA1 = ""
        styperefnameA2 = ""
        styperefnameA3 = ""
        styperefnameA4 = ""
        styperefnameA5 = ""


        
        request.session['cmbClassificationID'] =ID_Categories 

        Adminassettypelist_list =  Adminassetcategorytypelist.objects.order_by('scategorytype') 
        tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ID_Categories).order_by('categorytype')

        Admintoleranceclasslist_list =  Admintoleranceclasslist.objects.order_by('stoleranceclass')    

        return render(request,  'CloudCaliber/GaugeMasterlistCreateID.html', 
        {
            'title':'User list', 
            'message':'Your User list page.',
            'year':datetime.now().year,  
            'sPlantName': sPlantName ,   
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
                                            'tcategoriesLst': tcategoriesLst,
        })
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def load_Categories(request):
    ID_Classification = int(request.GET.get('IDClassificationId'))
    
    request.session['ID_Classification']  =  ID_Classification 

    request.session['ID_Categories'] = 0
    request.session['sFlowCode1']   =""
    request.session['sFlowCode2']   =""
    request.session['sFlowCode3']   =""
    request.session['sFlowCode4']   =""
    request.session['sFlowCode5']   =""
    sCodeFinal1 = ""
    sCodeFinal2 = ""
   
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode

    sClasscode = ""
    Adminassettypelist_list =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ID_Classification) 
    if Adminassettypelist_list:
        sClasscode = Adminassettypelist_list.scode


    sCodeFinal1 = sClasscode
    sCodeFinal2 = sClasscode + " " + sPlantCode
   
    request.session['sClasscode'] = sClasscode
    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2


    tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ID_Classification).order_by('categorytype')
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Categoriesdropdown.html', {'tcategoriesLst': tcategoriesLst})


def load_Code_ForAsset(request):
    ID_Classification = request.session['ID_Classification']
    
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories 

    request.session['ID_Classification']  =  ID_Classification 
    sCodeFinal1 = ""
    sCodeFinal2 = ""
   
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""

    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2

    AdminunitlistActive = Adminunitlist.objects.get(lplantid=lPlantId) 
    if AdminunitlistActive:
        sPlantCode = AdminunitlistActive.splantno
    request.session['sPlantCode']   =sPlantCode

    sClasscode = ""
    request.session['sClassification']   =""
    


    Adminassettypelist_list =  Adminassetcategorytypelist.objects.get(lcategorytypeid = ID_Classification) 
    if Adminassettypelist_list:
        sClasscode = Adminassettypelist_list.scode
        request.session['sClassification']   =Adminassettypelist_list.scategorytype


    request.session['sClasscode']   =sClasscode

    sCategoryCode = request.session['sCategoryCode'] 
    
    sFlowCode1 = request.session['sFlowCode1'] 
    sFlowCode2 = request.session['sFlowCode2']
    sFlowCode3 = request.session['sFlowCode3']
    sFlowCode4 = request.session['sFlowCode4']
    sFlowCode5 = request.session['sFlowCode5']  

    
    sFlowCode1 = "" 
    sFlowCode2 = "" 
    sFlowCode3 = "" 
    sFlowCode4 = "" 
    sFlowCode5 = "" 
    
    sContNo = ""
    sContNo1 = ""
    lContNo = 0
    lContNoVB = 0
    lContNoVBC = 0
 
 
    lassetidA =0

    sCategoryCode = ""
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode 
            sClasscode = Adminassetcategorylist_list.styperefname 
            lassetidA = Adminassetcategorylist_list.lassetid
            lContNoVB = Adminassetcategorylist_list.lcontinuousnoa



    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() 
   
    request.session['sCodeFinal1AK'] = sCodeFinal1.strip()

    AdmincategoryidcontinuousnolistActivw = Admincategoryidcontinuousnolist.objects.filter(scode= sCodeFinal1).values() 
    if AdmincategoryidcontinuousnolistActivw:
        for AdmincategoryidcontinuousnolistActivweOBJ in AdmincategoryidcontinuousnolistActivw.all():
            lContNo = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
            lContNoVBC = AdmincategoryidcontinuousnolistActivweOBJ['lserialno']
    else:
        lContNo  = lContNoVB

    request.session['lContNoVBC'] = 0

    if (lContNoVBC == 0 ):
        if (lassetidA == 6): 
            
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 7): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        elif (lassetidA == 8): 
            request.session['lContNoVBC'] = 1
            lContNo = lContNo +1
            sContNo1 = str(lContNo)
        else:
            lContNo =0
    else:
        if (lassetidA == 6):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 7):  
            sContNo1 = str(lContNo)
        elif (lassetidA == 8):  
            sContNo1 = str(lContNo)
        else:
            lContNo =0


    request.session['lContNo'] = lContNo

    if(sContNo1 != ''):
        if(len(sContNo1) == 1):
            sContNo = "000" + sContNo1
        elif(len(sContNo1) == 2):
            sContNo = "00" + sContNo1
        elif(len(sContNo1) == 3):
            sContNo = "0" + sContNo1
        else:
            sContNo =  sContNo1



    sCodeFinal1 = ""

    sCodeFinal1 = sClasscode.strip() +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip() +  sContNo.strip()
   
 
    lSerialNo =0
    
    AdminassetserialformatlistActive = Adminassetserialformatlist.objects.filter(scode= sCodeFinal1).values() 
    if AdminassetserialformatlistActive:
        for AdminassetserialformatlistActiveOBJ in AdminassetserialformatlistActive.all():
            lSerialNo = AdminassetserialformatlistActiveOBJ['lserialno']


    lSerialNo = lSerialNo +1

    request.session['lSerialNo'] = lSerialNo

    
    bNewIDwithfirstSerial = 0
    if (lSerialNo == 1):
        bNewIDwithfirstSerial = 1

    request.session['bNewIDwithfirstSerial']  = bNewIDwithfirstSerial

    sSerialNo = ""
    sSerialNo1 = ""
    sSerialNo=str(lSerialNo)
    if (len(sSerialNo) == 1):
        sSerialNo1 = "00" + sSerialNo
    elif (len(sSerialNo) == 2):
        sSerialNo1 = "0" + sSerialNo 
    else:
        sSerialNo1 =   sSerialNo 


    sCodeFinal2 = sClasscode.strip()  +  sCategoryCode.strip() +  sFlowCode1.strip() +  sFlowCode2.strip() +  sFlowCode3.strip() +  sFlowCode4.strip() +  sFlowCode5.strip()  +  sContNo.strip() + "-" + sPlantCode[:2] + sSerialNo1.strip()
   

    request.session['sClasscode'] = sClasscode.strip()
    request.session['sCodeFinal1A'] = sCodeFinal1.strip()
    request.session['sCodeFinal2A'] = sCodeFinal2.strip()


    tcategoriesLst = Adminassetcategorylist.objects.filter(lassetid= ID_Classification).order_by('categorytype')
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_Code1.html', {'sCodeFinal1': sCodeFinal1,'sCodeFinal2': sCodeFinal2 })




def load_Code_FlowLabel1(request):
    
    request.session['sCategoryCode'] = ""
    request.session['categorytype'] = ""
    request.session['styperefnameA1'] = ""
    request.session['styperefnameA2'] = ""
    request.session['styperefnameA3'] = ""
    request.session['styperefnameA4'] = ""
    request.session['styperefnameA5'] = ""
    ID_Categories = request.GET.get('IDCategories')
    request.session['ID_Categories'] = ID_Categories
    ID_Classification = request.session['ID_Classification']
    
    sCodeFinal1 = ""
    sCodeFinal2 = ""
   
    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    request.session['sPlantCode']   = ""
    sPlantCode = ""
  

    sClasscode = ""
    sPlantCode = request.session['sPlantCode']  
    sClasscode = request.session['sClasscode']  

    sCategoryCode = ""

    request.session['sCategoryCode'] = ""
    request.session['categorytype'] = ""
    request.session['styperefnameA1'] = ""
    request.session['styperefnameA2'] = ""
    request.session['styperefnameA3'] = ""
    request.session['styperefnameA4'] = ""
    request.session['styperefnameA5'] = ""
    styperefnameA1 = ""
    styperefnameA2 = ""
    styperefnameA3 = ""
    styperefnameA4 = ""
    styperefnameA5 = ""


    request.session['ID_Categories'] = ID_Categories
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list:
            sCategoryCode = Adminassetcategorylist_list.scode
            sClasscode = Adminassetcategorylist_list.styperefname 
            request.session['sCategoryCode'] = Adminassetcategorylist_list.scode
            request.session['categorytype'] = Adminassetcategorylist_list.categorytype
            request.session['styperefnameA1'] = Adminassetcategorylist_list.styperefname1
            request.session['styperefnameA2'] = Adminassetcategorylist_list.styperefname2
            request.session['styperefnameA3'] = Adminassetcategorylist_list.styperefname3
            request.session['styperefnameA4'] = Adminassetcategorylist_list.styperefname4
            request.session['styperefnameA5'] = Adminassetcategorylist_list.styperefname5
            styperefnameA1 = Adminassetcategorylist_list.styperefname1
            styperefnameA2 = Adminassetcategorylist_list.styperefname2
            styperefnameA3 = Adminassetcategorylist_list.styperefname3
            styperefnameA4 = Adminassetcategorylist_list.styperefname4
            styperefnameA5 = Adminassetcategorylist_list.styperefname5



    sCodeFinal1 = sClasscode + sCategoryCode
    sCodeFinal2 = sClasscode  + sCategoryCode + " " + sPlantCode
   
    request.session['sClasscode'] = sClasscode
    request.session['sCodeFinal1A'] = sCodeFinal1
    request.session['sCodeFinal2A'] = sCodeFinal2

 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_styperefnameA1.html', {'styperefnameA1': styperefnameA1  })


def load_Code_FlowLabel2(request):   
    styperefnameA2 = request.session['styperefnameA2'] 
    
    ID_Categories = request.GET.get('IDCategories')
    if (ID_Categories == "0"):
        styperefnameA2 = ""
    
    if (ID_Categories == "0"):
        styperefnameA2 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA2'] = Adminassetcategorylist_list.styperefname2  
            styperefnameA2 = Adminassetcategorylist_list.styperefname2 

    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_styperefnameA2.html', {'styperefnameA2': styperefnameA2 })



def load_Code_FlowLabel3(request):   
    styperefnameA3 = request.session['styperefnameA3'] 
    ID_Categories = request.GET.get('IDCategories')
    if (ID_Categories =="0"):
        styperefnameA3 = ""
    
    
    if (ID_Categories == "0"):
        styperefnameA3 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA3'] = Adminassetcategorylist_list.styperefname3  
            styperefnameA3 = Adminassetcategorylist_list.styperefname3 


    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_styperefnameA3.html', {'styperefnameA3': styperefnameA3 })


def load_Code_FlowLabel4(request):   
    styperefnameA4 = request.session['styperefnameA4'] 
    ID_Categories = request.GET.get('IDCategories')
    if (ID_Categories == "0"):
        styperefnameA4 = ""

    
    if (ID_Categories == "0"):
        styperefnameA4 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA4'] = Adminassetcategorylist_list.styperefname4  
            styperefnameA4 = Adminassetcategorylist_list.styperefname4 


    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_styperefnameA4.html', {'styperefnameA4': styperefnameA4 })



def load_Code_FlowLabel5(request):   
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    if (ID_Categories == "0"):
        styperefnameA5 = ""
    
    if (ID_Categories == "0"):
        styperefnameA5 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA5'] = Adminassetcategorylist_list.styperefname5  
            styperefnameA5 = Adminassetcategorylist_list.styperefname5 
    return render(request, 'CloudCaliber/GaugeMasterlistCreateID_styperefnameA5.html', {'styperefnameA5': styperefnameA5 })


def load_Code_Flow1(request):   
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    iID =0
    if (ID_Categories =="0"):
        iID = 0
        request.session['styperefnameA1'] = ""
    else:
        iID=ID_Categories
    styperefnameA1 = request.session['styperefnameA1'] 

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    
    if (ID_Categories == "0"):
        styperefnameA1 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA1'] = Adminassetcategorylist_list.styperefname1  
            styperefnameA1 = Adminassetcategorylist_list.styperefname1 



    if (request.session['styperefnameA1'] == "Part No"):
        Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA1'] })
    elif (request.session['styperefnameA1'] == "Equipment"):
        Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA1'] })
    elif (request.session['styperefnameA1'] == "Operation"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA1'] })
    elif (request.session['styperefnameA1'] == "Material"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA1'] })
    else:
        Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =iID, lcode5 = 1).order_by('scategorytype').values()  
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow1.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA1']  })

def load_Code_Flow2(request):     
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    iID =0
    if (ID_Categories =="0"):
        iID = 0
        request.session['styperefnameA2'] = ""
    else:
        iID=ID_Categories

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  
    
    if (ID_Categories == "0"):
        styperefnameA2 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA2'] = Adminassetcategorylist_list.styperefname2  
            styperefnameA2 = Adminassetcategorylist_list.styperefname2 


    if (request.session['styperefnameA2'] == "Part No"):
        Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA2'] })
    elif (request.session['styperefnameA2'] == "Equipment"):
        Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA2']  })
    elif (request.session['styperefnameA2'] == "Operation"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA2']  })
    elif (request.session['styperefnameA2'] == "Material"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA2'] })
    else:
        Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =iID, lcode5 = 2).order_by('scategorytype').values()  
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow2.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA2']  })



def load_Code_Flow3(request):     
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    iID =0
    if (ID_Categories =="0"):
        iID = 0
        request.session['styperefnameA3'] = ""
    else:
        iID=ID_Categories

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    if (ID_Categories == "0"):
        styperefnameA3 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA3'] = Adminassetcategorylist_list.styperefname3  
            styperefnameA3 = Adminassetcategorylist_list.styperefname3 

    if (request.session['styperefnameA3'] == "Part No"):
        Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3']  })
    elif (request.session['styperefnameA3'] == "Equipment"):
        Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3']  })
    elif (request.session['styperefnameA3'] == "Operation"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3']  })
    elif (request.session['styperefnameA3'] == "Material"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3']  })
    else:
        Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =iID, lcode5 = 3).order_by('scategorytype').values()  
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow3.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA3'] })



def load_Code_Flow4(request):     
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    iID =0
    if (ID_Categories =="0"):
        iID = 0
        request.session['styperefnameA4'] = ""
    else:
        iID=ID_Categories

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    if (ID_Categories == "0"):
        styperefnameA4 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA4'] = Adminassetcategorylist_list.styperefname4  
            styperefnameA4 = Adminassetcategorylist_list.styperefname4 

    if (request.session['styperefnameA4'] == "Part No"):
        Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4']  })
    elif (request.session['styperefnameA4'] == "Equipment"):
        Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4']  })
    elif (request.session['styperefnameA4'] == "Operation"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4']  })
    elif (request.session['styperefnameA4'] == "Material"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })
    else:
        Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =iID, lcode5 = 4).order_by('scategorytype').values()  
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow4.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA4'] })


def load_Code_Flow5(request):     
    styperefnameA5 = request.session['styperefnameA5'] 
    ID_Categories = request.GET.get('IDCategories')
    iID =0
    if (ID_Categories =="0"):
        iID = 0
        request.session['styperefnameA5'] = ""
    else:
        iID=ID_Categories

    lPlantId = request.session['lunitid']  
    sPlantName = request.session['sunitno'] 
    lcompanyid = request.session['lcompanyid']  
    scompantname =  request.session['scompantname']  

    if (ID_Categories == "0"):
        styperefnameA5 = ""
    else:
        Adminassetcategorylist_list =  Adminassetcategorylist.objects.get(lcategoryid = ID_Categories) 
        if Adminassetcategorylist_list: 
            request.session['styperefnameA5'] = Adminassetcategorylist_list.styperefname5  
            styperefnameA5 = Adminassetcategorylist_list.styperefname5 

    if (request.session['styperefnameA5'] == "Part No"):
        Adminassetcategorytypelist1_AddNew1OBJ =   Adminpartdetailslist.objects.order_by('spartno') 
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowPartNo.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })
    elif (request.session['styperefnameA5'] == "Equipment"):
        Adminassetcategorytypelist1_AddNew1OBJ =    Adminequipmentlist.objects.order_by('sequipmentname')   
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowEquipment.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5'] })
    elif (request.session['styperefnameA5'] == "Operation"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentoperationlist.objects.filter(lcompanyid=lcompanyid).order_by('soperation').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowOperation.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5'] })
    elif (request.session['styperefnameA5'] == "Material"):
        Adminassetcategorytypelist1_AddNew1OBJ =     Admininstrumentmateriallist.objects.filter(lcompanyid=lcompanyid).order_by('smaterial').values()
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlowMaterial.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5'] })
    else:
        Adminassetcategorytypelist1_AddNew1OBJ =  Adminassetcategorytypelist1.objects.filter(lcategorytype1 =iID, lcode5 = 5).order_by('scategorytype').values()  
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_stypeFlow5.html', {'Adminassetcategorytypelist1_AddNew1OBJ': Adminassetcategorytypelist1_AddNew1OBJ, 'styperefnameA1':request.session['styperefnameA5']  })



def load_loadCodeIDNewChecked_ForAsset(request): 
 
 
    request.session['bNewIDwithfirstSerial']  

    bNewIDwithfirstSerial1 = request.session['bNewIDwithfirstSerial']   

    if (bNewIDwithfirstSerial1 == 1):
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_NewIDorNot.html', {'bNewIDwithfirstSerial': bNewIDwithfirstSerial1  })
    else:
        return render(request, 'CloudCaliber/GaugeMasterlistCreateID_NotNewIDorNot.html', {'bNewIDwithfirstSerial': bNewIDwithfirstSerial1  })
    

