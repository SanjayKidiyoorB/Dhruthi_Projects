
from django.shortcuts import render
#import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
import re
import calendar
from calendar import HTMLCalendar

from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect


import BillingSol_project.settings
import threading as th
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from BillingSol.models import Userlist, Unotevalues, Tserviceinvoicelist, Tserviceinvoicedetailslist, Trentinvoicelist
from BillingSol.models import Trentinvoicedetailslist, Tpurchaseorderlist, Tpurchaseorderdetailslist, Torderacceptancelist, Torderacceptancedetailslist
from BillingSol.models import Tinvoicelist, Tinvoicedetailslist, Tdebitnotelist, Tdebitnotedetailslist, Tcreditnotelist
from BillingSol.models import Tcreditnotedetailslist, Msupplierlist,  Mpartdetailslist, Msitelist
from BillingSol.models import Mcustomerlist, Mcompanylist, Aemailescallationlist, Alogoimage 

@csrf_exempt
def CompanyList(request):
    if request.method == "POST":
        data = request.POST 

    if 'cmbAdd' in request.POST:  
        
        return   redirect('CompanyListAdd')  
    
    else:
        
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        return render(request, "BillingSol/CompanyList.html",
                      {
                          'Mcompanylistlist_list':Mcompanylistlist_list,

                      })


    
@csrf_exempt
def CompanyListAdd(request):
    

    locationid=0
    scompanyname=""
    slocation=""
    contactperson=""
    department=""
    emailid=""
    contactno=""
    smobile=""
    splace=""
    username=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstatecode=""
    lsupervisorid=0
    ssupervisorname=""
    ltempid1=0
    stempname1=""
    ltempid2=0
    stempname2=""
    ltempid3=0
    stempname3=""
    ltempid4=0
    stempname4=""
    ltempid5=0
    stempname5=""
    bcritical=0
    bnoncritical=0
    sgstno=""
    spanno=""
    scomments=""
    stype1=""
    sfile1=""
    sfolder1=""
    binactive=0
    linvoice1=0
    linvoice2=0
    linvoice3=0
    linvoice4=0
    linvoice5=0
    linvoice6=0
    linvoice7=0
    linvoice8=0
    linvoice9=0
    linvoice10=0
    linvoice11=0
    linvoice12=0
    linvoice13=0
    linvoice14=0
    linvoice15=0
    linvoice16=0
    linvoice17=0
    linvoice18=0
    linvoice19=0
    linvoice20=0
    lmonth=0
    lyear=0
    sformat=""
    sformat1=""
    sformat2=""
    sformat3=""
    sformat4=""
    sformat5=""
    sformat6=""
    sformat7=""
    sformat8=""
    sformat9=""
    sformat10=""
    sformat11=""
    sformat12=""
    sformat13=""
    sformat14=""
    sformat15=""
    sformat16=""
    sformat17=""
    sformat18=""
    sformat19=""
    sformat20=""
    scomments1=""
    scomments2=""
    scomments3=""
    scomments4=""
    scomments5=""
    scomments6=""
    scomments7=""
    scomments8=""
    scomments9=""
    scomments10=""
    scomments11=""
    scomments12=""
    scomments13=""
    scomments14=""
    scomments15=""
    scomments16=""
    scomments17=""
    scomments18=""
    scomments19=""
    scomments20=""
    sterms=""
    sterms1=""
    sterms2=""
    sterms3=""
    sterms4=""
    sterms5=""
    sterms6=""
    sterms7=""
    sterms8=""
    sterms9=""
    sterms10=""
    sterms11=""
    sterms12=""
    sterms13=""
    sterms14=""
    sterms15=""
    sterms16=""
    sterms17=""
    sterms18=""
    sterms19=""
    sterms20=""
 


    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('CompanyList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            scompanyname=data.get('txtCompany') 
            slocation=data.get('txtsLocation') 
            address1=data.get('txtAddress1') 
            address2=data.get('txtAddress2') 
            address3=data.get('txtAddress3') 
            scity=data.get('txtCity') 
            lpin=data.get('txtPincode') 
            sstate=data.get('txtState') 
            sgstno=data.get('txtGST') 
            spanno=data.get('txtPAN') 
            sstatecode=data.get('txtStateCode') 

            
            contactperson=data.get('txtContactPerson') 
            contactno=data.get('txtContactNumber') 
            emailid=data.get('txtEMailAddress') 

            linvoice1=0 #data.get('txtMaintenanceNo') 
            linvoice2=0 #data.get('txtProjectNo') 
            linvoice3=0 #data.get('txtPONo') 


            scomments1=data.get('txtMaintenanceInvDefault1') 
            sterms1=data.get('txtMaintenanceInvDefault2') 
             
            scomments2=data.get('txtProjectInvDefault1') 
            sterms2=data.get('txtProjectInvDefault2')  
            
            scomments3=data.get('txtPOInvDefault1') 
            sterms3=data.get('txtPOInvDefault2') 

            
            sformat1=data.get('txtMaintenanceFormat') 
            sformat2=data.get('txtProjectFormat') 
            sformat3=data.get('txtPOFormat') 


            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                binactive = 0
            else:
                binactive = 1
 

            Mcompanylistlist_AddNewOBJ = Mcompanylist(scompanyname=scompanyname, 	slocation=slocation, 	contactperson=contactperson, 	department=department, 	emailid=emailid, 	contactno=contactno, 	smobile=smobile, 	splace=splace, 	username=username, 	address1=address1, 	address2=address2, 	address3=address3, 	scity=scity, 	lpin=lpin, 	sstate=sstate, 	sstatecode=sstatecode, 	lsupervisorid=lsupervisorid, 	ssupervisorname=ssupervisorname, 	ltempid1=ltempid1, 	stempname1=stempname1, 	ltempid2=ltempid2, 	stempname2=stempname2, 	ltempid3=ltempid3, 	stempname3=stempname3, 	ltempid4=ltempid4, 	stempname4=stempname4, 	ltempid5=ltempid5, 	stempname5=stempname5, 	bcritical=bcritical, 	bnoncritical=bnoncritical, 	sgstno=sgstno, 	spanno=spanno, 	scomments=scomments, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	binactive=binactive, 	linvoice1=linvoice1, 	linvoice2=linvoice2, 	linvoice3=linvoice3, 	linvoice4=linvoice4, 	linvoice5=linvoice5, 	linvoice6=linvoice6, 	linvoice7=linvoice7, 	linvoice8=linvoice8, 	linvoice9=linvoice9, 	linvoice10=linvoice10, 	linvoice11=linvoice11, 	linvoice12=linvoice12, 	linvoice13=linvoice13, 	linvoice14=linvoice14, 	linvoice15=linvoice15, 	linvoice16=linvoice16, 	linvoice17=linvoice17, 	linvoice18=linvoice18, 	linvoice19=linvoice19, 	linvoice20=linvoice20, 	lmonth=lmonth, 	lyear=lyear, 	sformat=sformat, 	sformat1=sformat1, 	sformat2=sformat2, 	sformat3=sformat3, 	sformat4=sformat4, 	sformat5=sformat5, 	sformat6=sformat6, 	sformat7=sformat7, 	sformat8=sformat8, 	sformat9=sformat9, 	sformat10=sformat10, 	sformat11=sformat11, 	sformat12=sformat12, 	sformat13=sformat13, 	sformat14=sformat14, 	sformat15=sformat15, 	sformat16=sformat16, 	sformat17=sformat17, 	sformat18=sformat18, 	sformat19=sformat19, 	sformat20=sformat20, 	scomments1=scomments1, 	scomments2=scomments2, 	scomments3=scomments3, 	scomments4=scomments4, 	scomments5=scomments5, 	scomments6=scomments6, 	scomments7=scomments7, 	scomments8=scomments8, 	scomments9=scomments9, 	scomments10=scomments10, 	scomments11=scomments11, 	scomments12=scomments12, 	scomments13=scomments13, 	scomments14=scomments14, 	scomments15=scomments15, 	scomments16=scomments16, 	scomments17=scomments17, 	scomments18=scomments18, 	scomments19=scomments19, 	scomments20=scomments20, 	sterms=sterms, 	sterms1=sterms1, 	sterms2=sterms2, 	sterms3=sterms3, 	sterms4=sterms4, 	sterms5=sterms5, 	sterms6=sterms6, 	sterms7=sterms7, 	sterms8=sterms8, 	sterms9=sterms9, 	sterms10=sterms10, 	sterms11=sterms11, 	sterms12=sterms12, 	sterms13=sterms13, 	sterms14=sterms14, 	sterms15=sterms15, 	sterms16=sterms16, 	sterms17=sterms17, 	sterms18=sterms18, 	sterms19=sterms19, 	sterms20=sterms20 )
 
            Mcompanylistlist_AddNewOBJ.save()

            messages.success(request, 'Company List is Added successfully!')
            
            return   redirect('CompanyList')  


    else:               
        return render(request, "BillingSol/CompanyListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

    
@csrf_exempt
def CompanyListDetails(request,lID):
    
    locationid=0
    scompanyname=""
    slocation=""
    contactperson=""
    department=""
    emailid=""
    contactno=""
    smobile=""
    splace=""
    username=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstatecode=""
    lsupervisorid=0
    ssupervisorname=""
    ltempid1=0
    stempname1=""
    ltempid2=0
    stempname2=""
    ltempid3=0
    stempname3=""
    ltempid4=0
    stempname4=""
    ltempid5=0
    stempname5=""
    bcritical=0
    bnoncritical=0
    sgstno=""
    spanno=""
    scomments=""
    stype1=""
    sfile1=""
    sfolder1=""
    binactive=0
    linvoice1=0
    linvoice2=0
    linvoice3=0
    linvoice4=0
    linvoice5=0
    linvoice6=0
    linvoice7=0
    linvoice8=0
    linvoice9=0
    linvoice10=0
    linvoice11=0
    linvoice12=0
    linvoice13=0
    linvoice14=0
    linvoice15=0
    linvoice16=0
    linvoice17=0
    linvoice18=0
    linvoice19=0
    linvoice20=0
    lmonth=0
    lyear=0
    sformat=""
    sformat1=""
    sformat2=""
    sformat3=""
    sformat4=""
    sformat5=""
    sformat6=""
    sformat7=""
    sformat8=""
    sformat9=""
    sformat10=""
    sformat11=""
    sformat12=""
    sformat13=""
    sformat14=""
    sformat15=""
    sformat16=""
    sformat17=""
    sformat18=""
    sformat19=""
    sformat20=""
    scomments1=""
    scomments2=""
    scomments3=""
    scomments4=""
    scomments5=""
    scomments6=""
    scomments7=""
    scomments8=""
    scomments9=""
    scomments10=""
    scomments11=""
    scomments12=""
    scomments13=""
    scomments14=""
    scomments15=""
    scomments16=""
    scomments17=""
    scomments18=""
    scomments19=""
    scomments20=""
    sterms=""
    sterms1=""
    sterms2=""
    sterms3=""
    sterms4=""
    sterms5=""
    sterms6=""
    sterms7=""
    sterms8=""
    sterms9=""
    sterms10=""
    sterms11=""
    sterms12=""
    sterms13=""
    sterms14=""
    sterms15=""
    sterms16=""
    sterms17=""
    sterms18=""
    sterms19=""
    sterms20=""
 
    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('CompanyList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            scompanyname=data.get('txtCompany') 
            slocation=data.get('txtsLocation') 
            address1=data.get('txtAddress1') 
            address2=data.get('txtAddress2') 
            address3=data.get('txtAddress3') 
            scity=data.get('txtCity') 
            lpin=data.get('txtPincode') 
            sstate=data.get('txtState') 
            sgstno=data.get('txtGST') 
            spanno=data.get('txtPAN') 
            sstatecode=data.get('txtStateCode') 

            contactperson=data.get('txtContactPerson') 
            contactno=data.get('txtContactNumber') 
            emailid=data.get('txtEMailAddress') 

            #linvoice1=0 #data.get('txtMaintenanceNo') 
            #linvoice2=0 #data.get('txtProjectNo') 
            #linvoice3=0 #data.get('txtPONo') 


            scomments1=data.get('txtMaintenanceInvDefault1') 
            sterms1=data.get('txtMaintenanceInvDefault2') 
             
            scomments2=data.get('txtProjectInvDefault1') 
            sterms2=data.get('txtProjectInvDefault2')  
            
            scomments3=data.get('txtPOInvDefault1') 
            sterms3=data.get('txtPOInvDefault2') 

            
            sformat1=data.get('txtMaintenanceFormat') 
            sformat2=data.get('txtProjectFormat') 
            sformat3=data.get('txtPOFormat') 


            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                binactive = 0
            else:
                binactive = 1
 

            Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=lID) 
            Mcompanylist_AddNewOBJ.scompanyname=scompanyname 
            Mcompanylist_AddNewOBJ.slocation=slocation 
            Mcompanylist_AddNewOBJ.address1=address1 
            Mcompanylist_AddNewOBJ.address2=address2 
            Mcompanylist_AddNewOBJ.address3=address3 
            Mcompanylist_AddNewOBJ.scity=scity 
            Mcompanylist_AddNewOBJ.lpin=lpin 
            Mcompanylist_AddNewOBJ.sstate=sstate 
            Mcompanylist_AddNewOBJ.sgstno=sgstno 
            Mcompanylist_AddNewOBJ.spanno=spanno  
            Mcompanylist_AddNewOBJ.binactive=binactive 
            Mcompanylist_AddNewOBJ.sstatecode=sstatecode 


            Mcompanylist_AddNewOBJ.contactperson=contactperson 
            Mcompanylist_AddNewOBJ.contactno=contactno 
            Mcompanylist_AddNewOBJ.emailid=emailid 



            Mcompanylist_AddNewOBJ.scomments1=scomments1 
            Mcompanylist_AddNewOBJ.scomments2=scomments2 
            Mcompanylist_AddNewOBJ.scomments3=scomments3 
            Mcompanylist_AddNewOBJ.sterms1=sterms1 
            Mcompanylist_AddNewOBJ.sterms2=sterms2 
            Mcompanylist_AddNewOBJ.sterms3=sterms3 
            Mcompanylist_AddNewOBJ.sformat1=sformat1 
            Mcompanylist_AddNewOBJ.sformat2=sformat2 
            Mcompanylist_AddNewOBJ.sformat3=sformat3  

  

            Mcompanylist_AddNewOBJ.save()

            messages.success(request, 'Client List is Updated successfully!') 
            Mcompanylist_list = Mcompanylist.objects.get(locationid=lID) 
            binactive = Mcompanylist_list.binactive
            binactive1 =0
            if(binactive == True):
                binactive1 =1    
            return render(request, "BillingSol/CompanyListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Mcompanylist_list': Mcompanylist_list, 
                            'binactive':binactive1, 
                        }
                        )

    else: 
        Mcompanylist_list = Mcompanylist.objects.get(locationid=lID)   
        binactive = Mcompanylist_list.binactive
        binactive1 =0
        if(binactive == True):
            binactive1 =1
        return render(request, "BillingSol/CompanyListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylist_list': Mcompanylist_list,  
                            'binactive':binactive1, 
                        }
                        )


 
@csrf_exempt
def ClientList(request): 
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ClientListAdd')  
        
    else:
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
        return render(request, "BillingSol/ClientList.html",
                    {
                        'Mcustomerlist_list':Mcustomerlist_list,

                    })

    
@csrf_exempt
def ClientListAdd(request):

    customerid=0
    customername=""
    sstatus=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstd=""
    scontactno=""
    sfax=""
    username=""
    customersalestax=""
    slocation=""
    cst=0
    panno=""
    gstno=""
    sstatecode=""




    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('ClientList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsClient=data.get('txtsClient') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState') 
            txtGST=data.get('txtGST') 
            txtPAN=data.get('txtPAN') 
            sstatecode=data.get('txtStateCode') 


            username=data.get('txtContactPerson') 
            scontactno=data.get('txtContactNumber') 
            sfax=data.get('txtEMailAddress') 

            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                cst = 1
            else:
                cst = 0


            customername = txtsClient
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState
            panno = txtPAN
            gstno = txtGST
 

            Mcustomerlist_AddNewOBJ = Mcustomerlist(customername=customername, 	sstatus=sstatus, 	address1=address1, 	address2=address2, 	address3=address3, 	scity=scity, 	lpin=lpin, 	sstate=sstate, 	sstd=sstd, 	scontactno=scontactno, 	sfax=sfax, 	username=username, 	customersalestax=customersalestax, 	slocation=slocation, 	cst=cst, 	panno=panno, 	gstno=gstno, 	sstatecode=sstatecode)
 
            Mcustomerlist_AddNewOBJ.save()

            messages.success(request, 'Client List is Added successfully!')
            
            return   redirect('ClientList')  


    else:               
        return render(request, "BillingSol/ClientListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

    
@csrf_exempt
def ClientListDetails(request,lID):
    customerid=0
    customername=""
    sstatus=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstd=""
    scontactno=""
    sfax=""
    username=""
    customersalestax=""
    slocation=""
    cst=0
    panno=""
    gstno=""
    sstatecode=""
    bactive=0
    binactive=0
    saccounttype=""
    soperationtype=""
    lcompanyid=0
    lcompanylocationid=0 

    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('ClientList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsClient=data.get('txtsClient') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState') 
            txtGST=data.get('txtGST') 
            txtPAN=data.get('txtPAN') 
            sstatecode=data.get('txtStateCode') 

            username=data.get('txtContactPerson') 
            scontactno=data.get('txtContactNumber') 
            sfax=data.get('txtEMailAddress') 


            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                cst = 1
            else:
                cst = 0


            customername = txtsClient
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState
            panno = txtPAN
            gstno = txtGST

            Mcustomerlist_AddNewOBJ = Mcustomerlist.objects.get(customerid=lID) 
            Mcustomerlist_AddNewOBJ.customername=customername 
            Mcustomerlist_AddNewOBJ.address1=address1 
            Mcustomerlist_AddNewOBJ.address2=address2 
            Mcustomerlist_AddNewOBJ.address3=address3 
            Mcustomerlist_AddNewOBJ.scity=scity 
            Mcustomerlist_AddNewOBJ.lpin=lpin 
            Mcustomerlist_AddNewOBJ.sstate=sstate 
            Mcustomerlist_AddNewOBJ.panno=panno 
            Mcustomerlist_AddNewOBJ.gstno=gstno 
            Mcustomerlist_AddNewOBJ.cst=cst 
            Mcustomerlist_AddNewOBJ.sstatecode=sstatecode   

            Mcustomerlist_AddNewOBJ.username=username  
            Mcustomerlist_AddNewOBJ.scontactno=scontactno  
            Mcustomerlist_AddNewOBJ.sfax=sfax  
 

            Mcustomerlist_AddNewOBJ.save()

            messages.success(request, 'Client List is Updated successfully!') 
            Mcustomerlist_list = Mcustomerlist.objects.get(customerid=lID)     
            return render(request, "BillingSol/ClientListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Mcustomerlist_list': Mcustomerlist_list,  
                        }
                        )

    else: 
        Mcustomerlist_list = Mcustomerlist.objects.get(customerid=lID)              
        return render(request, "BillingSol/ClientListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcustomerlist_list': Mcustomerlist_list,  
                        }
                        )
 

@csrf_exempt
def SiteList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('SiteListAdd')  
        
    else:
        
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace')  
        return render(request, "BillingSol/SiteList.html",
                    {
                        'Msitelist_list':Msitelist_list,

                    })


    
@csrf_exempt
def SiteListAdd(request):

    lcontactdetailnoid=0
    customerid=0
    contactperson=""
    department=""
    emailid=""
    contactno=""
    smobile=""
    splace=""
    username=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    slocation=""
    sstatecode=""
    lsupervisorid=0
    ssupervisorname=""
    ltempid1=0
    stempname1=""
    ltempid2=0
    stempname2=""
    ltempid3=0
    stempname3=""
    ltempid4=0
    stempname4=""
    ltempid5=0
    stempname5=""
    bcritical=0
    bnoncritical=0





    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('SiteList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        slocation = McustomerlistGet.customername 


            
            splace=data.get('txtsSiteLocation') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState')  
            sstatecode=data.get('txtStateCode') 

            contactperson=data.get('txtContactPerson') 
            contactno=data.get('txtContactNumber') 
            emailid=data.get('txtEMailAddress') 
            stempname1=data.get('txtGST') 
            stempname2=data.get('txtPAN') 

 

 
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState 
 

            Msitelist_AddNewOBJ = Msitelist(customerid=customerid, 	contactperson=contactperson, 	department=department, 	emailid=emailid, 	contactno=contactno, 	smobile=smobile, 	splace=splace, 	username=username, 	address1=address1, 	address2=address2, 	address3=address3, 	scity=scity, 	lpin=lpin, 	sstate=sstate, 	slocation=slocation, 	sstatecode=sstatecode, 	lsupervisorid=lsupervisorid, 	ssupervisorname=ssupervisorname, 	ltempid1=ltempid1, 	stempname1=stempname1, 	ltempid2=ltempid2, 	stempname2=stempname2, 	ltempid3=ltempid3, 	stempname3=stempname3, 	ltempid4=ltempid4, 	stempname4=stempname4, 	ltempid5=ltempid5, 	stempname5=stempname5, 	bcritical=bcritical, 	bnoncritical=bnoncritical)
 
            Msitelist_AddNewOBJ.save()

            messages.success(request, 'Site List is Added successfully!')
            
            return   redirect('SiteList')  


    else:               
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
        return render(request, "BillingSol/SiteListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Mcustomerlist_list': Mcustomerlist_list,
                            'CustomerID':0,
                        }
                        ) 

    
@csrf_exempt
def SiteListDetails(request,lID):
    
    lcontactdetailnoid=0
    customerid=0
    contactperson=""
    department=""
    emailid=""
    contactno=""
    smobile=""
    splace=""
    username=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    slocation=""
    sstatecode=""
    lsupervisorid=0
    ssupervisorname=""
    ltempid1=0
    stempname1=""
    ltempid2=0
    stempname2=""
    ltempid3=0
    stempname3=""
    ltempid4=0
    stempname4=""
    ltempid5=0
    stempname5=""
    bcritical=0
    bnoncritical=0

    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('SiteList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        slocation = McustomerlistGet.customername 


            
            splace=data.get('txtsSiteLocation') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState')  
            sstatecode=data.get('txtStateCode') 

            contactperson=data.get('txtContactPerson') 
            contactno=data.get('txtContactNumber') 
            emailid=data.get('txtEMailAddress') 
            stempname1=data.get('txtGST') 
            stempname2=data.get('txtPAN') 

 

 
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState 
 

            Msitelist_AddNewOBJ = Msitelist.objects.get(lcontactdetailnoid=lID) 
            Msitelist_AddNewOBJ.customerid=customerid 
            Msitelist_AddNewOBJ.customerid=customerid 
            Msitelist_AddNewOBJ.customerid=customerid 
            Msitelist_AddNewOBJ.address1=address1 
            Msitelist_AddNewOBJ.address2=address2 
            Msitelist_AddNewOBJ.address3=address3 
            Msitelist_AddNewOBJ.scity=scity 
            Msitelist_AddNewOBJ.lpin=lpin 
            Msitelist_AddNewOBJ.sstate=sstate 
            Msitelist_AddNewOBJ.panno=stempname2 
            Msitelist_AddNewOBJ.gstno=stempname1  
            Msitelist_AddNewOBJ.sstatecode=sstatecode  


            Msitelist_AddNewOBJ.contactperson=contactperson 
            Msitelist_AddNewOBJ.contactno=contactno 
            Msitelist_AddNewOBJ.emailid=emailid 


            Msitelist_AddNewOBJ.save()

            messages.success(request, 'Site List is Updated successfully!') 
            Msitelist_list = Msitelist.objects.get(lcontactdetailnoid=lID)     
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername') 
            return render(request, "BillingSol/SiteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Msitelist_list': Msitelist_list, 
                            'Mcustomerlist_list': Mcustomerlist_list,  
                        }
                        )

    else: 
        Msitelist_list = Msitelist.objects.get(lcontactdetailnoid=lID)     
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')               
        return render(request, "BillingSol/SiteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcustomerlist_list': Mcustomerlist_list,  
                            'Msitelist_list': Msitelist_list, 
                        }
                        )
 

   
@csrf_exempt
def SupplierList(request): 
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('SupplierListAdd')  
        
    else:
        
        Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')  
        return render(request, "BillingSol/SupplierList.html",
                    {
                        'Msupplierlist_list':Msupplierlist_list,

                    })

    
@csrf_exempt
def SupplierListAdd(request):

    supplierid=0
    suppliername=""
    sstatus=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstd=""
    scontactno=""
    sfax=""
    username=""
    suppliersalestax=""
    slocation=""
    cst=0
    panno=""
    gstno=""
    sstatecode=""





    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('SupplierList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsSupplier=data.get('txtsSupplier') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState') 
            txtGST=data.get('txtGST') 
            txtPAN=data.get('txtPAN') 
            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                cst = 1
            else:
                cst = 0


            suppliername = txtsSupplier
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState
            panno = txtPAN
            gstno = txtGST
 

            Msupplierlist_AddNewOBJ = Msupplierlist(  	suppliername=suppliername, 	sstatus=sstatus, 	address1=address1, 	address2=address2, 	address3=address3, 	scity=scity, 	lpin=lpin, 	sstate=sstate, 	sstd=sstd, 	scontactno=scontactno, 	sfax=sfax, 	username=username, 	suppliersalestax=suppliersalestax, 	slocation=slocation, 	cst=cst, 	panno=panno, 	gstno=gstno, 	sstatecode=sstatecode)
 
            Msupplierlist_AddNewOBJ.save()

            messages.success(request, 'Supplier List is Added successfully!')
            
            return   redirect('SupplierList')  


    else:               
        return render(request, "BillingSol/SupplierListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 

    
@csrf_exempt
def SupplierListDetails(request,lID):
    
    supplierid=0
    suppliername=""
    sstatus=""
    address1=""
    address2=""
    address3=""
    scity=""
    lpin=""
    sstate=""
    sstd=""
    scontactno=""
    sfax=""
    username=""
    suppliersalestax=""
    slocation=""
    cst=0
    panno=""
    gstno=""
    sstatecode=""

    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('SupplierList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtsSupplier=data.get('txtsSupplier') 
            txtAddress1=data.get('txtAddress1') 
            txtAddress2=data.get('txtAddress2') 
            txtAddress3=data.get('txtAddress3') 
            txtCity=data.get('txtCity') 
            txtPincode=data.get('txtPincode') 
            txtState=data.get('txtState') 
            txtGST=data.get('txtGST') 
            txtPAN=data.get('txtPAN') 
            fav_language=data.get('fav_language') 

            if(fav_language == 'Active'):
                cst = 1
            else:
                cst = 0


            suppliername = txtsSupplier
            address1 = txtAddress1
            address2 = txtAddress2
            address3 = txtAddress3
            scity = txtCity
            lpin = txtPincode
            sstate = txtState
            panno = txtPAN
            gstno = txtGST

            Msupplierlist_AddNewOBJ = Msupplierlist.objects.get(supplierid=lID) 
            Msupplierlist_AddNewOBJ.suppliername=suppliername 
            Msupplierlist_AddNewOBJ.address1=address1 
            Msupplierlist_AddNewOBJ.address2=address2 
            Msupplierlist_AddNewOBJ.address3=address3 
            Msupplierlist_AddNewOBJ.scity=scity 
            Msupplierlist_AddNewOBJ.lpin=lpin 
            Msupplierlist_AddNewOBJ.sstate=sstate 
            Msupplierlist_AddNewOBJ.panno=panno 
            Msupplierlist_AddNewOBJ.gstno=gstno 
            Msupplierlist_AddNewOBJ.cst=cst  

            Msupplierlist_AddNewOBJ.save()

            messages.success(request, 'Supplier List is Updated successfully!') 
            Msupplierlist_list = Msupplierlist.objects.get(supplierid=lID)     
            return render(request, "BillingSol/SupplierListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Msupplierlist_list': Msupplierlist_list,  
                        }
                        )

    else: 
        Msupplierlist_list = Msupplierlist.objects.get(supplierid=lID)              
        return render(request, "BillingSol/SupplierListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msupplierlist_list': Msupplierlist_list,  
                        }
                        )
 
@csrf_exempt
def UserList(request):
    if request.method == "POST":
        data = request.POST 

    if 'cmbAdd' in request.POST:  
        
        return   redirect('UserListAdd')  
    
    else:
        
        Userlist_list = Userlist.objects.order_by('sname')  
        return render(request, "BillingSol/UserList.html",
                      {
                          'Userlist_list':Userlist_list,

                      })
 


    
@csrf_exempt
def UserListAdd(request):
    luserid=0
    u1_username=""
    u1_password=""
    u1_short=""
    bcustomer=0
    bsupplier=0
    bitem=0
    bmaintenancebill=0
    bworkcontractbill=0
    breadwrite=0
    breadonly=0
    ball=0
    bpo=0
    smodify=0
    bblock=0
    sreport=0
    sadmin=0
    u1_sregion=""
    bho=0
    sname=""
    ldepartmentid=0
    sdepartment=""



    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('UserList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            txtEmployeeName=data.get('txtEmployeeName')
            txtEmployeeID=data.get('txtEmployeeID') 
            txtPassword=data.get('txtPassword') 
            fav_language=data.get('fav_language') 

            
            sname= txtEmployeeName
            u1_username= txtEmployeeID
            u1_password= txtPassword 
            if(fav_language == 'SoftwareAdmin'):
                sadmin = 1
            else:
                sadmin = 0
            if(fav_language == 'HREntry'):
                baddhrdetails = 1
            else:
                baddhrdetails = 0
            if(fav_language == 'SalaryCompliance'):
                bcompliance = 1
            else:
                bcompliance = 0
            if(fav_language == 'ApproverManagement'):
                bapprovalrights = 1
            else:
                bapprovalrights = 0
            if(fav_language == 'Block'):
                bblock = 1
            else:
                bblock = 0
 
 

            Userlist_AddNewOBJ = Userlist(u1_username=u1_username, 	u1_password=u1_password, 	u1_short=u1_short, 	bcustomer=bcustomer, 	bsupplier=bsupplier, 	bitem=bitem, 	bmaintenancebill=bmaintenancebill, 	bworkcontractbill=bworkcontractbill, 	breadwrite=breadwrite, 	breadonly=breadonly, 	ball=ball, 	bpo=bpo, 	smodify=smodify, 	bblock=bblock, 	sreport=sreport, 	sadmin=sadmin, 	u1_sregion=u1_sregion, 	bho=bho, 	sname=sname, 	ldepartmentid=ldepartmentid, 	sdepartment=sdepartment )
 
            Userlist_AddNewOBJ.save()

            messages.success(request, 'User List is Added successfully!')
            
            return   redirect('UserList')  


    else:               
        return render(request, "BillingSol/UserListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                        }
                        ) 
    
@csrf_exempt
def UserListDetails(request,lID):
    
    luserid=0
    u1_username=""
    u1_password=""
    u1_short=""
    bcustomer=0
    bsupplier=0
    bitem=0
    bmaintenancebill=0
    bworkcontractbill=0
    breadwrite=0
    breadonly=0
    ball=0
    bpo=0
    smodify=0
    bblock=0
    sreport=0
    sadmin=0
    u1_sregion=""
    bho=0
    sname=""
    ldepartmentid=0
    sdepartment=""



    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('UserList')  

        if 'cmbSaveAdd' in request.POST:  


            data = request.POST
            data = request.POST
            txtEmployeeName=data.get('txtEmployeeName')
            txtEmployeeID=data.get('txtEmployeeID') 
            txtPassword=data.get('txtPassword') 
            fav_language=data.get('fav_language') 

            
            sname= txtEmployeeName
            u1_username= txtEmployeeID
            u1_password= txtPassword 
            if(fav_language == 'SoftwareAdmin'):
                sadmin = 1
            else:
                sadmin = 0
            if(fav_language == 'HREntry'):
                bmaintenancebill = 1
            else:
                bmaintenancebill = 0
            if(fav_language == 'SalaryCompliance'):
                bpo = 1
            else:
                bpo = 0 
            if(fav_language == 'Block'):
                bblock = 1
            else:
                bblock = 0


            Userlist_AddNewOBJ = Userlist.objects.get(luserid=lID) 
            Userlist_AddNewOBJ.sname=sname 
            Userlist_AddNewOBJ.u1_username=u1_username 
            Userlist_AddNewOBJ.u1_password=u1_password 
            Userlist_AddNewOBJ.sadmin=sadmin 
            Userlist_AddNewOBJ.bmaintenancebill=bmaintenancebill 
            Userlist_AddNewOBJ.bpo=bpo  
            Userlist_AddNewOBJ.bblock=bblock 

            Userlist_AddNewOBJ.save()

            messages.success(request, 'User List is Updated successfully!') 
            Userlist_list = Userlist.objects.get(luserid=lID)     
            return render(request, "BillingSol/UserListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,   
                            'Userlist_list': Userlist_list,  
                        }
                        )

    else: 
        Userlist_list = Userlist.objects.get(luserid=lID)              
        return render(request, "BillingSol/UserListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Userlist_list': Userlist_list,  
                        })