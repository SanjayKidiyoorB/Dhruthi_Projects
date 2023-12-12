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
from CloudCaliber.models import  Admincategoryidcontinuousnolist, Adminassetcontinuousformatlist, Adminassetserialformatlist,  Adminassetcategorytypelist1, Adminassetcategorylist, Adminassetcategorytypelist, Adminequipmentlist, Adminrangelist, Admininstrumenttypelist, Thistorytransactions, Adminassetsparepartslist, Adminassettypelist, Admincalibconditionslist, Adminexternalagencylist, Adminexternalagencytraceabilitylist, Admingradelist, Admininstrumentcattypelist, Admininstrumentequipmentlist, Admininstrumentmateriallist, Admininstrumentoperationlist, Admininstrumentrangelist, Adminlocationlist, Adminmakelist, Adminpartdetailslist, Adminpartdetailsforinstrumentlist, Adminpurchasechecklist, Adminrolelist, Adminstoragelocationlist, Admintoleranceclasschartlist, Admintoleranceclasslist, Admintoleranceclasschartlist
from CloudCaliber.models import Adminuseraccesslist, Adminassetcontinuousformatlist, Admininstrumentmateriallist, Admincustomerlist, Admintolerancedialgaugelist, Admintoleranceismanufacturingstdchartlist, Admintolerancepressuregaugelist, Admintoleranceradiusgaugelist, Admintolerancesettingringlist, Admintoleranceslipgaugelist, Adminunitlist, Adminunitofmeasurelist, Adminuserlist
from CloudCaliber.models import Masterinstrumentslistpart2, Masterinstrumentslistpart3, Masterinstrumentslistpart4


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
def GaugeIssueReturn(request):
    return render(request, "CloudCaliber/GaugeIssueReturn.html")





@csrf_exempt
def GaugeIssue(request, lID):
    
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

        txtIssuedDate1 = ""
        txtIssuedDate2 = ""
        txtIssuedDate3 = ""
        txtIssuedDate = ""
        if 'txtIssuedDate' in request.POST:
            txtIssuedDate = data.get("txtIssuedDate")

            txtIssuedDate1 = txtIssuedDate
            txtIssuedDate2  = txtIssuedDate1.split("/")
            txtIssuedDate = ""
            
            if(len(txtIssuedDate2) > 1):
                txtIssuedDate = txtIssuedDate2[2] + "-" + txtIssuedDate2[1] + "-" + txtIssuedDate2[0]
            else:
                txtIssuedDate2  = txtIssuedDate1.split("-") 
                if(len(txtIssuedDate2) > 1):
                    txtIssuedDate = txtIssuedDate2[2] + "-" + txtIssuedDate2[1] + "-" + txtIssuedDate2[0] 

 




        if(txtIssuedDate == ''): 
            txtIssuedDate =str(datetime.now()) 
            txtIssuedDate = txtIssuedDate[0:10] 

        cmbLocationNew = 0
        if 'cmbLocationNew' in request.POST:
            cmbLocationNew = int(data.get("cmbLocationNew"))

        txtIssuedTo = ""
        if 'txtIssuedTo' in request.POST:
            txtIssuedTo = data.get("txtIssuedTo")

        txtMachineTo = ""
        if 'txtMachineTo' in request.POST:
            txtMachineTo = data.get("txtMachineTo")
            
        txtPartNo = ""
        if 'txtPartNo' in request.POST:
            txtPartNo = data.get("txtPartNo")


        if 'cmbClose' in request.POST: 
            return   redirect('Dashboard')  

            
        if 'cmbIssued' in request.POST: 
        
        
            shistorytype=""
            shistorytype="ISSUED"
            scalibrationvendor=""
            scalibrationvendorid=""
            senteredby=""
            senteredby= semployeename + " (" + semployeeno + ")"
            scalibrationresult="" 

              
            scurrentstatus=""
            scurrentstatus="ISSUED"
            dtcalibrationdate=datetime.now()
            dtcalibrationdate=datetime.strptime(txtIssuedDate, '%d-%m-%Y').date()
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
            llineid=cmbLocationNew
            slinename=""

            AreaofUselist_listAQ =  Adminlocationlist.objects.get(  lid=llineid)
            if AreaofUselist_listAQ:  
                slinename =  AreaofUselist_listAQ.slocationname


            sto= "Issued To : " + slinename + " Received by : "+ txtIssuedTo + "  Machine Ref : " + txtMachineTo + "  Part Ref : " + txtPartNo
  

            MasterinstrumentslistSaveOBJA =  Masterinstrumentslist.objects.get(lid=linstrumentid) 
             
        
            MasterinstrumentslistSaveOBJA.scurrentstatus ="ISSUED"

            sissueddate = ""
            sreturneddate = ""
            if MasterinstrumentslistSaveOBJA.bcalibrateidle == 0:
                lGapDays =0
                if ((len(MasterinstrumentslistSaveOBJA.sreturneddate)) != 0):
                    if ((len(MasterinstrumentslistSaveOBJA.sissueddate)) != 0):
                        lGapDays =0
                        sissueddate = txtIssuedDate
                        sreturneddate = MasterinstrumentslistSaveOBJA.sreturneddate
                        
                        dtissueddate=datetime.now()
                        dtissueddate=datetime.strptime(sissueddate, '%d-%m-%Y').date()
                        dtreturneddate=datetime.now()
                        dtreturneddate=datetime.strptime(sreturneddate, '%d-%m-%Y').date()
                        lGapDays =  dtissueddate - dtreturneddate
                        dtnextcalib1 = datetime.now() 
                        dtnextcalib = datetime.now() 
                        dtnextcalib1 = MasterinstrumentslistSaveOBJA.dtnextcalib
                        dtnextcalib = dtnextcalib1  + timedelta(days=lGapDays.days) 
                        snextcalib1 = ""
                        snextcalib1 = dtnextcalib.strftime('%d-%m-%Y')
                        MasterinstrumentslistSaveOBJA.dtnextcalib = dtnextcalib
                        MasterinstrumentslistSaveOBJA.snextcalibdate = snextcalib1
                        MasterinstrumentslistSaveOBJA.dtcalibdisplaydate = dtnextcalib  + timedelta(days=-10) 

 
 
            MasterinstrumentslistSaveOBJA.ldefaultlocationid =llineid

            MasterinstrumentslistSaveOBJA.slocationname =slinename
            MasterinstrumentslistSaveOBJA.sreturneddate =""
            MasterinstrumentslistSaveOBJA.sissuedto =txtIssuedTo
            MasterinstrumentslistSaveOBJA.sissuedmachineto =txtMachineTo
            MasterinstrumentslistSaveOBJA.sissuedpartno =txtPartNo

            MasterinstrumentslistSaveOBJA.sissueddate =txtIssuedDate
            MasterinstrumentslistSaveOBJA.bshowlistascalibrate =1
            MasterinstrumentslistSaveOBJA.bcheckin =1
            
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


            
            
            return   redirect('Dashboard')  


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



        return render(request, "CloudCaliber/GaugeIssueDetails.html", 
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






@csrf_exempt
def GaugeReturn(request, lID):
    
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
        bSAPCodeDone = 0

        txtIssuedDate1 = ""
        txtIssuedDate2 = ""
        txtIssuedDate3 = ""
        txtIssuedDate = ""
        if 'txtReceivedDate' in request.POST:
            txtIssuedDate = data.get("txtReceivedDate")

            txtIssuedDate1 = txtIssuedDate
            txtIssuedDate2  = txtIssuedDate1.split("/")
            txtIssuedDate = ""
            
            if(len(txtIssuedDate2) > 1):
                txtIssuedDate = txtIssuedDate2[2] + "-" + txtIssuedDate2[1] + "-" + txtIssuedDate2[0]
            else:
                txtIssuedDate2  = txtIssuedDate1.split("-") 
                if(len(txtIssuedDate2) > 1):
                    txtIssuedDate = txtIssuedDate2[2] + "-" + txtIssuedDate2[1] + "-" + txtIssuedDate2[0] 


        if(txtIssuedDate == ''): 
            txtIssuedDate =str(datetime.now()) 
            txtIssuedDate = txtIssuedDate[0:10] 

        cmbLocationNew = 0

        cmbReturnStatus = 0
        if 'cmbReturnStatus' in request.POST:
            cmbReturnStatus = int(data.get("cmbReturnStatus"))

        txtIssuedTo = ""
        if 'txtIssuedTo' in request.POST:
            txtIssuedTo = data.get("txtReceivedfrom")

        txtMachineTo = ""
        if 'txtMachineTo' in request.POST:
            txtMachineTo = data.get("txtMachineTo")
            
        txtPartNo = ""
        if 'txtPartNo' in request.POST:
            txtPartNo = data.get("txtPartNo")


        if 'cmbClose' in request.POST: 
            return   redirect('Dashboard')  

            
        if 'cmbReceived' in request.POST: 
        
            shistorytype=""
            shistorytype="RETURNED"
            scalibrationvendor=""
            scalibrationvendorid=""
            senteredby=""
            senteredby= semployeename + " (" + semployeeno + ")"
            scalibrationresult="" 

              
            scurrentstatus=""
            scurrentstatus1=""

            if(int(cmbReturnStatus) == 1):
                scurrentstatus="GOOD CONDITION - IDLE"
                scurrentstatus1="IDLE"
            elif(int(cmbReturnStatus) == 2):
                scurrentstatus="ERROR - DAMAGED"
                scurrentstatus1="IDLE"
            elif(int(cmbReturnStatus) == 3):
                scurrentstatus="ERROR - QUARANTINE"
                scurrentstatus1="QUARANTINE"
            elif(int(cmbReturnStatus) == 4):
                scurrentstatus="ERROR - SCRAPPED"
                scurrentstatus1="SCRAPPED"
            elif(int(cmbReturnStatus) == 5):
                scurrentstatus="MISSING"
                scurrentstatus1="MISSING"
            elif(int(cmbReturnStatus) == 6):
                scurrentstatus="TRANSFERRED - OTHER PLANT"
                scurrentstatus1="TRANSFERRED - OTHER PLANT"

            dtcalibrationdate=datetime.now()
            dtcalibrationdate=datetime.strptime(txtIssuedDate, '%d-%m-%Y').date()
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
            sto="Received From : " + txtIssuedTo  
            sfrom=""
            dthistorydate=datetime.now()
            shistorydate=""
            sreturneddate=""
            scomment=""
            llineid=0
            slinename=""
            slinename="Standard Room"

            AreaofUselist_listAQ =  Adminlocationlist.objects.filter(lplantid=llplantid, slocationname = slinename ).values()
            if AreaofUselist_listAQ:  
                for AreaofUselist_listAQGet in AreaofUselist_listAQ.all(): 
                    cmbLocationNew = AreaofUselist_listAQGet['lid'] 


            llineid=cmbLocationNew
 


  

            MasterinstrumentslistSaveOBJA =  Masterinstrumentslist.objects.get(lid=linstrumentid)  
        
            MasterinstrumentslistSaveOBJA.scurrentstatus =scurrentstatus1
            MasterinstrumentslistSaveOBJA.sreturneddate =txtIssuedDate
            MasterinstrumentslistSaveOBJA.bshowlistascalibrate =0
            if(int(cmbReturnStatus) == 1):
                if(MasterinstrumentslistSaveOBJA.bcalibrateidle == 1): 
                    MasterinstrumentslistSaveOBJA.bshowlistascalibrate =1

            MasterinstrumentslistSaveOBJA.bcheckin =0
            

            MasterinstrumentslistSaveOBJA.ldefaultlocationid =llineid
            MasterinstrumentslistSaveOBJA.slocationname ="Standard Room"
            # MasterinstrumentslistSaveOBJA.sreturneddate =""
            # MasterinstrumentslistSaveOBJA.sissuedto =txtIssuedTo
            # MasterinstrumentslistSaveOBJA.sissuedmachineto =txtMachineTo
            # MasterinstrumentslistSaveOBJA.sissuedpartno =txtPartNo


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


            
            return   redirect('Dashboard')  



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


        return render(request, "CloudCaliber/GaugeReturnDetails.html", 
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
def GaugeIssueList(request):
    return render(request, "CloudCaliber/GaugeIssuelist.html")
@csrf_exempt
def GaugeIssueHistory(request):
    return render(request, "CloudCaliber/GaugeIssueHistory.html")

@csrf_exempt
def GaugeReturnList(request):
    return render(request, "CloudCaliber/GaugeReturnlist.html")

@csrf_exempt
def GaugeReturnHistory(request):
    return render(request, "CloudCaliber/GaugeReturnHistory.html")


@csrf_exempt
def GaugeIssueReturnList(request):




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


 

 