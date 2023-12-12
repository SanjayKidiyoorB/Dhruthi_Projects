from django.shortcuts import render
#import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
import re
import calendar
from calendar import HTMLCalendar
from barcode import EAN13
from barcode.writer import ImageWriter

from num2words import num2words

from django.utils.timezone import datetime
from django.utils.timezone import  timedelta
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

from BillingSol.utils import render_to_pdf

import BillingSol_project.settings
import threading as th
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from BillingSol.models import Userlist, Unotevalues, Tserviceinvoicelist, Tserviceinvoicedetailslist, Trentinvoicelist
from BillingSol.models import Trentinvoicedetailslist, Tpurchaseorderlist, Tpurchaseorderdetailslist, Torderacceptancelist, Torderacceptancedetailslist
from BillingSol.models import Tinvoicelist, Tinvoicedetailslist, Tdebitnotelist, Tdebitnotedetailslist, Tcreditnotelist
from BillingSol.models import Tcreditnotedetailslist, Msupplierlist, Mpartdetailslist,  Msitelist
from BillingSol.models import Mcustomerlist, Mcompanylist, Aemailescallationlist, Alogoimage 


@csrf_exempt
def MaintenanceList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('MaintenanceListAdd')  
        
    else:
        
        Tserviceinvoicelist_list = Tserviceinvoicelist.objects.order_by('-invoicedate', '-salesbillno')  


        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tserviceinvoicelist_list.count()
        lRecCount1 =0

        if lRecCount > 500 : 
            lRecCount1 = int((lRecCount * 5/100) )
            #if lRecCount1 < 1000 : 
                #lRecCount1 = int(lRecCount /7)
            
            #elif lRecCount1 < 5000 : 
                #lRecCount1 = int(lRecCount /25)
        else:
            lRecCount1 =lRecCount
            
        if lRecCount1 == 0 :
            lRecCount1 =1
        paginator = Paginator(Tserviceinvoicelist_list, lRecCount1)
        try:
            Tserviceinvoicelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tserviceinvoicelist_lists = paginator.page(1)
        except EmptyPage:
            Tserviceinvoicelist_lists = paginator.page(paginator.num_pages)


        return render(request, "BillingSol/MaintenanceInvoiceList.html",
                    {
                        'Tserviceinvoicelist_list':Tserviceinvoicelist_lists,

                    })


    
@csrf_exempt
def MaintenanceListAdd(request):

    salesbillid=0
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Maintenance & Repair"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0




    salesordermultiid=0
    #salesbillid=0
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""

    if request.method == "POST":

        if 'cmbCloseAdd' in request.POST:  

            return   redirect('MaintenanceList') 

        if 'cmbSaveAdd' in request.POST:  
            
            llocationid =0
            data = request.POST
            

            
            if 'cmbCompany' in request.POST: 
                if(data.get('cmbCompany').isnumeric()):
                    llocationid = int(data.get('cmbCompany'))
                    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
                    if McompanylistGet:
                        slocation = McompanylistGet.scompanyname  
                        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
                         
                        slocationgstno=McompanylistGet.sgstno 
                        slocationpanno=McompanylistGet.spanno
                        slocationstatecode=McompanylistGet.sstatecode

                        salesbillno=McompanylistGet.linvoice1 + 1
                        finyear=McompanylistGet.lyear
                        if(McompanylistGet.lyear < 4):
                            if(datetime.today().month >= 4):
                                finyear=datetime.today().month
                                salesbillno = 1

                        ssalesbillno = ""
                        ssalesbillno = str(salesbillno)
                        if(len(ssalesbillno) == 1):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "0" + ssalesbillno
                        sinvoicerefno=McompanylistGet.sformat1 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice1 = salesbillno
                        Mcompanylist_AddNewOBJ.lyear = finyear 
                        
                        Mcompanylist_AddNewOBJ.save()


            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode
            
            Tserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
            Tserviceinvoicelist_AddNewOBJ.save()
            salesbillid = Tserviceinvoicelist_AddNewOBJ.salesbillid

            return   redirect('MaintenanceListDetails', lID=salesbillid)  
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/MaintenanceListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                        }
                        ) 


    
  
@csrf_exempt
def MaintenanceListDetailsDelete(request,lID):
    lCatID = 0
    
    lDetId =0

    Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tserviceinvoicedetailslist_list.salesbillid
    
    # if Tserviceinvoicedetailslist_list:
    #     for Tserviceinvoicedetailslist_listQ in Tserviceinvoicedetailslist_list:
    #         lDetId = Tserviceinvoicedetailslist_listQ['salesbillid']

    Tserviceinvoicelist_listOBJ =  Tserviceinvoicedetailslist.objects.get(salesordermultiid=lID).delete()
          


    Tserviceinvoicelist_listSave = Tserviceinvoicelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tserviceinvoicedetailslist_listG = Tserviceinvoicedetailslist.objects.filter(salesbillid=lDetId).values() 



    if Tserviceinvoicedetailslist_listG:
        for Tserviceinvoicedetailslist_listGT in Tserviceinvoicedetailslist_listG:
            dtotal =dtotal + float(Tserviceinvoicedetailslist_listGT['ddescitemtotal'])
            ltaxrateamt =ltaxrateamt + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt'])
            digst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt'])
            dsgst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt1'])
            dcgst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
            dtotalfinal =dtotalfinal + float(Tserviceinvoicedetailslist_listGT['dtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    Tserviceinvoicelist_listSave.dtotal = dtotal
    Tserviceinvoicelist_listSave.dgsttrate = ltaxrateamt

    Tserviceinvoicelist_listSave.dsgst0 = 0
    Tserviceinvoicelist_listSave.dcgst0 = 0 
    Tserviceinvoicelist_listSave.digst0 = 0
    if(Tserviceinvoicelist_listSave.sstatecode == Tserviceinvoicelist_listSave.slocationstatecode):
        Tserviceinvoicelist_listSave.dsgst0 = ltaxrateamt/2
        Tserviceinvoicelist_listSave.dcgst0 = ltaxrateamt/2 
    else:
        Tserviceinvoicelist_listSave.digst0 = ltaxrateamt

    Tserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tserviceinvoicelist_listSave.swords= swords.upper()

 
    Tserviceinvoicelist_listSave.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('MaintenanceListDetails', lID=lDetId)  


@csrf_exempt
def MaintenanceListDetails(request,lID):
    
    salesbillid=0
    salesbillid=lID
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Maintenance & Repair"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0

    
    salesordermultiid=0
    #salesbillid=0
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""
    dtotal=0
    ltaxrate=0
    ltaxrateamt=0
    ltaxrateamt1=0 
    ltaxrateamt2=0  


    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('CompanyList')  
        
        if 'cmdGetClient' in request.POST:  

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

                        TserviceinvoicelistSave_list.customerid = customerid
                        TserviceinvoicelistSave_list.customername = customername
                        TserviceinvoicelistSave_list.saddressclient = saddressclient
                        TserviceinvoicelistSave_list.scustomerpan = scustomerpan
                        TserviceinvoicelistSave_list.scustomergst = scustomergst
                        TserviceinvoicelistSave_list.sstatecode = sstatecode
                        TserviceinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
                Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/MaintenanceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        #sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

                        TserviceinvoicelistSave_list.customersiteid = customersiteid
                        TserviceinvoicelistSave_list.customernamesite = customernamesite
                        TserviceinvoicelistSave_list.saddresssite = saddresssite 

                        TserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        TserviceinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tserviceinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/MaintenanceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                            
                        TserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                # sworkfrom=data.get('txtFrom') 
                # sworkfromA = sworkfrom.split("-")
                # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                # sworkfto=data.get('txtTo') 
                # sworkftoA = sworkfto.split("-")
                # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  



                TserviceinvoicelistSave_list.ackdate1 = ackdate1
                TserviceinvoicelistSave_list.ackdate = ackdate
                TserviceinvoicelistSave_list.ewaydate1 = ewaydate1
                TserviceinvoicelistSave_list.ewaydate = ewaydate
                TserviceinvoicelistSave_list.sdate1 = sdate1
                TserviceinvoicelistSave_list.sdate = sdate
                TserviceinvoicelistSave_list.podate1 = podate1
                TserviceinvoicelistSave_list.podate = podate
                TserviceinvoicelistSave_list.sworkfrom = sworkfrom
                TserviceinvoicelistSave_list.sfromdate = sfromdate
                TserviceinvoicelistSave_list.sworkfto = sworkfto
                TserviceinvoicelistSave_list.stodate = stodate
                TserviceinvoicelistSave_list.sworkfto = sworkfto
                TserviceinvoicelistSave_list.inrno = inrno
                TserviceinvoicelistSave_list.ackno = ackno
                TserviceinvoicelistSave_list.ewayno = ewayno
                TserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
                TserviceinvoicelistSave_list.stype1 = stype1
                TserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TserviceinvoicelistSave_list.pono = pono
                TserviceinvoicelistSave_list.note1 = note1 

                TserviceinvoicelistSave_list.customerid = customerid
                TserviceinvoicelistSave_list.customername = customername
                TserviceinvoicelistSave_list.saddressclient = saddressclient
                TserviceinvoicelistSave_list.scustomerpan = scustomerpan
                TserviceinvoicelistSave_list.scustomergst = scustomergst
                TserviceinvoicelistSave_list.sstatecode = sstatecode
                
                TserviceinvoicelistSave_list.customersiteid = customersiteid
                TserviceinvoicelistSave_list.customernamesite = customernamesite
                TserviceinvoicelistSave_list.saddresssite = saddresssite  

                TserviceinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
                Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/MaintenanceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/MaintenanceListDetailsPrint.html', context)
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

        if 'cmdItemSave' in request.POST:  

            TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                #sworkfrom=data.get('txtFrom') 
                #sworkfromA = sworkfrom.split("-")
                # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                # sworkfto=data.get('txtTo') 
                # sworkftoA = sworkfto.split("-")
                # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                sdesc=data.get('txtItemDesc')  
                qty=data.get('txtQuantity')  
                unitprice=data.get('txtRate')
                units=data.get('txtUnits')
                ddescitemtotal=data.get('txtItemAmt')
                shsn=data.get('txtHSNCode')
                dtotal=data.get('txtItemTotalAmt')
                ltaxrate=data.get('txtGSTRate')  
                ltaxrateamt=data.get('txtGSTAmt')  
                staxnotify=data.get('txtPOAMt')  
                ltaxrateamt1=0 
                ltaxrateamt2=0  



                ddescitemtotal =float(unitprice) * float(qty)
                ltaxrateamt =ddescitemtotal * float(ltaxrate)/100
                if(TserviceinvoicelistSave_list.sstatecode == TserviceinvoicelistSave_list.slocationstatecode):
                    ltaxrateamt1 =ltaxrateamt/2
                    ltaxrateamt1 =ltaxrateamt/2

                dtotal = round(ddescitemtotal + ltaxrateamt)


                
                Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)
    
                Tserviceinvoicedetailslist_AddNewOBJ.save()

                messages.success(request, 'Item is Added successfully!')


                Tserviceinvoicedetailslist_listG = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 

                ltaxrateamt =0
                digst0 = 0
                dsgst0 = 0
                dcgst0 = 0
                dgsttrate = 0
                dtotalfinal = 0
                dtotal=0

                            

                if Tserviceinvoicedetailslist_listG:
                    for Tserviceinvoicedetailslist_listGT in Tserviceinvoicedetailslist_listG:
                        dtotal =dtotal + float(Tserviceinvoicedetailslist_listGT['ddescitemtotal'])
                        ltaxrateamt =ltaxrateamt + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt'])
                        digst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt'])
                        dsgst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt1'])
                        dcgst0 =dgsttrate + float(Tserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
                        dtotalfinal =dtotalfinal + float(Tserviceinvoicedetailslist_listGT['dtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TserviceinvoicelistSave_list.dtotal = dtotal
                TserviceinvoicelistSave_list.dgsttrate = ltaxrateamt

                TserviceinvoicelistSave_list.dsgst0 = 0
                TserviceinvoicelistSave_list.dcgst0 = 0 
                TserviceinvoicelistSave_list.digst0 = 0 


                if(TserviceinvoicelistSave_list.sstatecode == TserviceinvoicelistSave_list.slocationstatecode):
                    TserviceinvoicelistSave_list.dsgst0 = ltaxrateamt/2
                    TserviceinvoicelistSave_list.dcgst0 = ltaxrateamt/2
                else:
                    TserviceinvoicelistSave_list.digst0 = ltaxrateamt

                TserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
                TserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
                TserviceinvoicelistSave_list.swords = swords.upper()  

                TserviceinvoicelistSave_list.ackdate1 = ackdate1
                TserviceinvoicelistSave_list.ackdate = ackdate
                TserviceinvoicelistSave_list.ewaydate1 = ewaydate1
                TserviceinvoicelistSave_list.ewaydate = ewaydate
                TserviceinvoicelistSave_list.sdate1 = sdate1
                TserviceinvoicelistSave_list.sdate = sdate
                TserviceinvoicelistSave_list.podate1 = podate1
                TserviceinvoicelistSave_list.podate = podate
                TserviceinvoicelistSave_list.sworkfrom = sworkfrom
                TserviceinvoicelistSave_list.sfromdate = sfromdate
                TserviceinvoicelistSave_list.sworkfto = sworkfto
                TserviceinvoicelistSave_list.stodate = stodate
                TserviceinvoicelistSave_list.sworkfto = sworkfto
                TserviceinvoicelistSave_list.inrno = inrno
                TserviceinvoicelistSave_list.ackno = ackno
                TserviceinvoicelistSave_list.ewayno = ewayno
                TserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
                TserviceinvoicelistSave_list.stype1 = stype1
                TserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TserviceinvoicelistSave_list.pono = pono
                TserviceinvoicelistSave_list.note1 = note1 

                TserviceinvoicelistSave_list.customerid = customerid
                TserviceinvoicelistSave_list.customername = customername
                TserviceinvoicelistSave_list.saddressclient = saddressclient
                TserviceinvoicelistSave_list.scustomerpan = scustomerpan
                TserviceinvoicelistSave_list.scustomergst = scustomergst
                TserviceinvoicelistSave_list.sstatecode = sstatecode
                
                TserviceinvoicelistSave_list.customersiteid = customersiteid
                TserviceinvoicelistSave_list.customernamesite = customernamesite
                TserviceinvoicelistSave_list.saddresssite = saddresssite 
                TserviceinvoicelistSave_list.swords= swords.upper()
                TserviceinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
                Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/MaintenanceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                                }
                                ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
        Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tserviceinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/MaintenanceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                        }
                        ) 

    
@csrf_exempt
def ProjectList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProjectListAdd')  
        
    else:
        
        Tinvoicelist_list = Tinvoicelist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tinvoicelist_list.count()
        lRecCount1 =0

        if lRecCount > 500 : 
            lRecCount1 = int((lRecCount * 5/100) )
            #if lRecCount1 < 1000 : 
                #lRecCount1 = int(lRecCount /7)
            
            #elif lRecCount1 < 5000 : 
                #lRecCount1 = int(lRecCount /25)
        else:
            lRecCount1 =lRecCount
            
        if lRecCount1 == 0 :
            lRecCount1 =1
        paginator = Paginator(Tinvoicelist_list, lRecCount1)
        try:
            Tinvoicelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tinvoicelist_lists = paginator.page(1)
        except EmptyPage:
            Tinvoicelist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/ProjectInvoiceList.html",
                    {
                        'Tinvoicelist_list':Tinvoicelist_lists,

                    })


    
@csrf_exempt
def ProjectListAdd(request):
    
    salesbillid=0
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Project"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0

    salesordermultiid=0
    #salesbillid=0
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0
    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            return   redirect('ProjectList') 

        if 'cmbSaveAdd' in request.POST:  
            

            llocationid =0
            data = request.POST


            if 'cmbCompany' in request.POST: 
                if(data.get('cmbCompany').isnumeric()):
                    llocationid = int(data.get('cmbCompany'))
                    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
                    if McompanylistGet:
                        slocation = McompanylistGet.scompanyname  
                        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
                         
                        slocationgstno=McompanylistGet.sgstno 
                        slocationpanno=McompanylistGet.spanno
                        slocationstatecode=McompanylistGet.sstatecode

                        salesbillno=McompanylistGet.linvoice2 + 1
                        finyear=McompanylistGet.lyear
                        if(McompanylistGet.lyear < 4):
                            if(datetime.today().month >= 4):
                                finyear=datetime.today().month
                                salesbillno = 1

                        ssalesbillno = ""
                        ssalesbillno = str(salesbillno)
                        if(len(ssalesbillno) == 1):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "0" + ssalesbillno
                        sinvoicerefno=McompanylistGet.sformat2 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice2 = salesbillno
                        Mcompanylist_AddNewOBJ.lyear = finyear 
                        
                        Mcompanylist_AddNewOBJ.save()


            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode
            
            
            Tinvoicelist_AddNewOBJ = Tinvoicelist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
            Tinvoicelist_AddNewOBJ.save()
            salesbillid = Tinvoicelist_AddNewOBJ.salesbillid

            return   redirect('ProjectListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProjectListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                        }
                        ) 


  
@csrf_exempt
def ProjectListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tinvoicedetailslist_list = Tinvoicedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tinvoicedetailslist_list.salesbillid
    
    # if Tinvoicedetailslist_list:
    #     for Tinvoicedetailslist_listQ in Tinvoicedetailslist_list:
    #         lDetId = Tinvoicedetailslist_listQ['salesbillid']

    Tinvoicelist_listOBJ =  Tinvoicedetailslist.objects.get(salesordermultiid=lID).delete()
          


    TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lDetId).values() 

    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal=0
    dcgst01 =0
    dcgst5 =0
    dsgst5 =0
    dcgst12 =0
    dsgst12 =0
    dcgst18 =0
    dsgst18 =0
    dcgst28 =0
    dsgst28 =0

    


    dcgst01 =0
    dcgst5 =0
    dsgst5 =0
    dcgst12 =0
    dsgst12 =0
    dcgst18 =0
    dsgst18 =0
    dcgst28 =0
    dsgst28 =0
    dsgst01 =0

                

    if Tinvoicedetailslist_listG:
        for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
            dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst50'])
            dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst120'])
            dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst180'])
            dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst280'])
            dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
            
            dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TinvoicelistSave_list.dtotal = dtotal
    TinvoicelistSave_list.dgsttrate = ltaxrateamt

    TinvoicelistSave_list.dsgst0 = 0
    TinvoicelistSave_list.dcgst0 = 0 
    TinvoicelistSave_list.digst0 = 0 




    TinvoicelistSave_list.dcgst01 = 0 
    TinvoicelistSave_list.dcgst5 = 0 
    TinvoicelistSave_list.dcgst12 = 0 
    TinvoicelistSave_list.dcgst18 = 0 
    TinvoicelistSave_list.dcgst28 = 0 

    TinvoicelistSave_list.dcgst01 = 0 
    TinvoicelistSave_list.dsgst5 = 0 
    TinvoicelistSave_list.dsgst12 = 0 
    TinvoicelistSave_list.dsgst18 = 0 
    TinvoicelistSave_list.dsgst28 = 0 

    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
        

        TinvoicelistSave_list.dsgst01 = dsgst01 
        TinvoicelistSave_list.dsgst5 = dsgst5 
        TinvoicelistSave_list.dsgst12 = dsgst12 
        TinvoicelistSave_list.dsgst18 = dsgst18 
        TinvoicelistSave_list.dsgst28 = dsgst28 
    else:

        TinvoicelistSave_list.dcgst01 =dcgst01 
        TinvoicelistSave_list.dcgst5 = dcgst5 
        TinvoicelistSave_list.dcgst12 =dcgst12
        TinvoicelistSave_list.dcgst18 = dcgst18 
        TinvoicelistSave_list.dcgst28 = dcgst28

    TinvoicelistSave_list.dtotalfinal = dtotalfinal
    TinvoicelistSave_list.dtotalfinal = dtotalfinal
    TinvoicelistSave_list.swords = swords.upper()  


    TinvoicelistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('ProjectListDetails', lID=lDetId)  


@csrf_exempt
def ProjectListDetails(request,lID):
    
    salesbillid=0
    salesbillid=lID
    
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0 



    salesbillid=lID
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Maintenance & Repair"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0



    
    salesordermultiid=0
    #salesbillid=0salesordermultiid=0 
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0



    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('CompanyList')  
        
        if 'cmdGetClient' in request.POST:  

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customerid = customerid
                        TinvoicelistSave_list.customername = customername
                        TinvoicelistSave_list.saddressclient = saddressclient
                        TinvoicelistSave_list.scustomerpan = scustomerpan
                        TinvoicelistSave_list.scustomergst = scustomergst
                        TinvoicelistSave_list.sstatecode = sstatecode
                        TinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customersiteid = customersiteid
                        TinvoicelistSave_list.customernamesite = customernamesite
                        TinvoicelistSave_list.saddresssite = saddresssite 
                        

                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2



                        TinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom=data.get('txtFrom') 
                sworkfromA = sworkfrom.split("-")
                sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA = sworkfto.split("-")
                stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                TinvoicelistSave_list.ackdate1 = ackdate1
                TinvoicelistSave_list.ackdate = ackdate
                TinvoicelistSave_list.ewaydate1 = ewaydate1
                TinvoicelistSave_list.ewaydate = ewaydate
                TinvoicelistSave_list.sdate1 = sdate1
                TinvoicelistSave_list.sdate = sdate
                TinvoicelistSave_list.podate1 = podate1
                TinvoicelistSave_list.podate = podate
                TinvoicelistSave_list.sworkfrom = sworkfrom
                TinvoicelistSave_list.sfromdate = sfromdate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.stodate = stodate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.inrno = inrno
                TinvoicelistSave_list.ackno = ackno
                TinvoicelistSave_list.ewayno = ewayno
                TinvoicelistSave_list.scategoryofservice = scategoryofservice
                TinvoicelistSave_list.stype1 = stype1
                TinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TinvoicelistSave_list.pono = pono
                TinvoicelistSave_list.note1 = note1 

                TinvoicelistSave_list.customerid = customerid
                TinvoicelistSave_list.customername = customername
                TinvoicelistSave_list.saddressclient = saddressclient
                TinvoicelistSave_list.scustomerpan = scustomerpan
                TinvoicelistSave_list.scustomergst = scustomergst
                TinvoicelistSave_list.sstatecode = sstatecode
                
                TinvoicelistSave_list.customersiteid = customersiteid
                TinvoicelistSave_list.customernamesite = customernamesite
                TinvoicelistSave_list.saddresssite = saddresssite 
                TinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProjectListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom=data.get('txtFrom') 
                sworkfromA = sworkfrom.split("-")
                sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA = sworkfto.split("-")
                stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                sdesc=data.get('txtItemDesc')  
                qty=data.get('txtQuantity')  
                unitprice=data.get('txtRate')
                units=data.get('txtUnits')
                ddescitemtotal=data.get('txtItemAmt')
                shsn=data.get('txtHSNCode')
                dtotal=data.get('txtItemTotalAmt')
                ltaxrate=data.get('txtGSTRate')  
                ltaxrateamt=data.get('txtGSTAmt')  
                staxnotify=data.get('txtPOAMt')  
                ltaxrateamt1=0 
                ltaxrateamt2=0  

                TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 


                dcgst1pt00 =float(unitprice) * float(qty)
                ltaxrate=float(ltaxrate)
                dsgst01=ltaxrate
                ltaxrateamt =dcgst1pt00 * ltaxrate/100
                dcgst1pt0 = ltaxrateamt
                if(ltaxrate == 0):
                    dcgst01 =0
                elif(ltaxrate == 5):
                    dcgst5 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst5 = dcgst5/2
                    else:
                       dcgst50  =ltaxrateamt
                elif(ltaxrate == 12):
                    dcgst12 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst12 = dcgst12/2
                    else:
                       dcgst120  =ltaxrateamt
                elif(ltaxrate == 18):
                    dcgst18 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst18 = dcgst18/2
                    else:
                       dcgst180  =ltaxrateamt
                elif(ltaxrate == 28):
                    dcgst28 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst28 = dcgst28/2
                    else:
                       dcgst280  =ltaxrateamt


                    

                ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



                
                Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)
    
                Tinvoicedetailslist_AddNewOBJ.save()

                messages.success(request, 'Item is Added successfully!')


                ltaxrateamt =0
                digst0 = 0
                dsgst0 = 0
                dcgst0 = 0
                dgsttrate = 0
                dtotalfinal = 0
                dtotal=0
                dcgst01 =0
                dcgst5 =0
                dsgst5 =0
                dcgst12 =0
                dsgst12 =0
                dcgst18 =0
                dsgst18 =0
                dcgst28 =0
                dsgst28 =0

                dcgst01 =0
                dcgst5 =0
                dsgst5 =0
                dcgst12 =0
                dsgst12 =0
                dcgst18 =0
                dsgst18 =0
                dcgst28 =0
                dsgst28 =0
                

                            

                if Tinvoicedetailslist_listG:
                    for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                        dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst50'])
                        dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst120'])
                        dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst180'])
                        dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst280'])
                        dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                        
                        dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TinvoicelistSave_list.dtotal = dtotal
                TinvoicelistSave_list.dgsttrate = ltaxrateamt

                TinvoicelistSave_list.dsgst0 = 0
                TinvoicelistSave_list.dcgst0 = 0 
                TinvoicelistSave_list.digst0 = 0 

 


                TinvoicelistSave_list.dcgst01 = 0 
                TinvoicelistSave_list.dcgst5 = 0 
                TinvoicelistSave_list.dcgst12 = 0 
                TinvoicelistSave_list.dcgst18 = 0 
                TinvoicelistSave_list.dcgst28 = 0 

                TinvoicelistSave_list.dcgst01 = 0 
                TinvoicelistSave_list.dsgst5 = 0 
                TinvoicelistSave_list.dsgst12 = 0 
                TinvoicelistSave_list.dsgst18 = 0 
                TinvoicelistSave_list.dsgst28 = 0 

                if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                   

                    TinvoicelistSave_list.dsgst01 = dsgst01 
                    TinvoicelistSave_list.dsgst5 = dsgst5 
                    TinvoicelistSave_list.dsgst12 = dsgst12 
                    TinvoicelistSave_list.dsgst18 = dsgst18 
                    TinvoicelistSave_list.dsgst28 = dsgst28 
                else:

                    TinvoicelistSave_list.dcgst01 =dcgst01 
                    TinvoicelistSave_list.dcgst5 = dcgst5 
                    TinvoicelistSave_list.dcgst12 =dcgst12
                    TinvoicelistSave_list.dcgst18 = dcgst18 
                    TinvoicelistSave_list.dcgst28 = dcgst28

                TinvoicelistSave_list.dtotalfinal = dtotalfinal
                TinvoicelistSave_list.dtotalfinal = dtotalfinal
                TinvoicelistSave_list.swords = swords.upper()  

                TinvoicelistSave_list.ackdate1 = ackdate1
                TinvoicelistSave_list.ackdate = ackdate
                TinvoicelistSave_list.ewaydate1 = ewaydate1
                TinvoicelistSave_list.ewaydate = ewaydate
                TinvoicelistSave_list.sdate1 = sdate1
                TinvoicelistSave_list.sdate = sdate
                TinvoicelistSave_list.podate1 = podate1
                TinvoicelistSave_list.podate = podate
                TinvoicelistSave_list.sworkfrom = sworkfrom
                TinvoicelistSave_list.sfromdate = sfromdate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.stodate = stodate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.inrno = inrno
                TinvoicelistSave_list.ackno = ackno
                TinvoicelistSave_list.ewayno = ewayno
                TinvoicelistSave_list.scategoryofservice = scategoryofservice
                TinvoicelistSave_list.stype1 = stype1
                TinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TinvoicelistSave_list.pono = pono
                TinvoicelistSave_list.note1 = note1 

                TinvoicelistSave_list.customerid = customerid
                TinvoicelistSave_list.customername = customername
                TinvoicelistSave_list.saddressclient = saddressclient
                TinvoicelistSave_list.scustomerpan = scustomerpan
                TinvoicelistSave_list.scustomergst = scustomergst
                TinvoicelistSave_list.sstatecode = sstatecode
                
                TinvoicelistSave_list.customersiteid = customersiteid
                TinvoicelistSave_list.customernamesite = customernamesite
                TinvoicelistSave_list.saddresssite = saddresssite 
                TinvoicelistSave_list.swords= swords.upper()
                TinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
        Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        ) 



def ProjectListDetails1(request,lID):
    
    salesbillid=0
    salesbillid=lID
    
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0 



    salesbillid=lID
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Maintenance & Repair"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0



    
    salesordermultiid=0
    #salesbillid=0salesordermultiid=0 
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0



    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('CompanyList')  
        
        if 'cmdGetClient' in request.POST:  

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customerid = customerid
                        TinvoicelistSave_list.customername = customername
                        TinvoicelistSave_list.saddressclient = saddressclient
                        TinvoicelistSave_list.scustomerpan = scustomerpan
                        TinvoicelistSave_list.scustomergst = scustomergst
                        TinvoicelistSave_list.sstatecode = sstatecode
                        TinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customersiteid = customersiteid
                        TinvoicelistSave_list.customernamesite = customernamesite
                        TinvoicelistSave_list.saddresssite = saddresssite 
                        

                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2



                        TinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom=data.get('txtFrom') 
                sworkfromA = sworkfrom.split("-")
                sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA = sworkfto.split("-")
                stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                TinvoicelistSave_list.ackdate1 = ackdate1
                TinvoicelistSave_list.ackdate = ackdate
                TinvoicelistSave_list.ewaydate1 = ewaydate1
                TinvoicelistSave_list.ewaydate = ewaydate
                TinvoicelistSave_list.sdate1 = sdate1
                TinvoicelistSave_list.sdate = sdate
                TinvoicelistSave_list.podate1 = podate1
                TinvoicelistSave_list.podate = podate
                TinvoicelistSave_list.sworkfrom = sworkfrom
                TinvoicelistSave_list.sfromdate = sfromdate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.stodate = stodate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.inrno = inrno
                TinvoicelistSave_list.ackno = ackno
                TinvoicelistSave_list.ewayno = ewayno
                TinvoicelistSave_list.scategoryofservice = scategoryofservice
                TinvoicelistSave_list.stype1 = stype1
                TinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TinvoicelistSave_list.pono = pono
                TinvoicelistSave_list.note1 = note1 

                TinvoicelistSave_list.customerid = customerid
                TinvoicelistSave_list.customername = customername
                TinvoicelistSave_list.saddressclient = saddressclient
                TinvoicelistSave_list.scustomerpan = scustomerpan
                TinvoicelistSave_list.scustomergst = scustomergst
                TinvoicelistSave_list.sstatecode = sstatecode
                
                TinvoicelistSave_list.customersiteid = customersiteid
                TinvoicelistSave_list.customernamesite = customernamesite
                TinvoicelistSave_list.saddresssite = saddresssite 
                TinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProjectListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom=data.get('txtFrom') 
                sworkfromA = sworkfrom.split("-")
                sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA = sworkfto.split("-")
                stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                sdesc=data.get('txtItemDesc')  
                qty=data.get('txtQuantity')  
                unitprice=data.get('txtRate')
                units=data.get('txtUnits')
                ddescitemtotal=data.get('txtItemAmt')
                shsn=data.get('txtHSNCode')
                dtotal=data.get('txtItemTotalAmt')
                ltaxrate=data.get('txtGSTRate')  
                ltaxrateamt=data.get('txtGSTAmt')  
                staxnotify=data.get('txtPOAMt')  
                ltaxrateamt1=0 
                ltaxrateamt2=0  

                TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 


                dcgst1pt00 =float(unitprice) * float(qty)
                ltaxrate=float(ltaxrate)
                dsgst01=ltaxrate
                ltaxrateamt =dcgst1pt00 * ltaxrate/100
                dcgst1pt0 = ltaxrateamt
                if(ltaxrate == 0):
                    dcgst01 =0
                elif(ltaxrate == 5):
                    dcgst5 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst5 = dcgst5/2
                    else:
                       dcgst50  =ltaxrateamt
                elif(ltaxrate == 12):
                    dcgst12 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst12 = dcgst12/2
                    else:
                       dcgst120  =ltaxrateamt
                elif(ltaxrate == 18):
                    dcgst18 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst18 = dcgst18/2
                    else:
                       dcgst180  =ltaxrateamt
                elif(ltaxrate == 28):
                    dcgst28 =ltaxrateamt 
                    if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                        dsgst28 = dcgst28/2
                    else:
                       dcgst280  =ltaxrateamt


                    

                ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



                
                Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)
    
                Tinvoicedetailslist_AddNewOBJ.save()

                messages.success(request, 'Item is Added successfully!')


                ltaxrateamt =0
                digst0 = 0
                dsgst0 = 0
                dcgst0 = 0
                dgsttrate = 0
                dtotalfinal = 0
                dtotal=0
                dcgst01 =0
                dcgst5 =0
                dsgst5 =0
                dcgst12 =0
                dsgst12 =0
                dcgst18 =0
                dsgst18 =0
                dcgst28 =0
                dsgst28 =0

                dcgst01 =0
                dcgst5 =0
                dsgst5 =0
                dcgst12 =0
                dsgst12 =0
                dcgst18 =0
                dsgst18 =0
                dcgst28 =0
                dsgst28 =0
                

                            

                if Tinvoicedetailslist_listG:
                    for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                        dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst50'])
                        dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst120'])
                        dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst180'])
                        dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst280'])
                        dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                        
                        dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TinvoicelistSave_list.dtotal = dtotal
                TinvoicelistSave_list.dgsttrate = ltaxrateamt

                TinvoicelistSave_list.dsgst0 = 0
                TinvoicelistSave_list.dcgst0 = 0 
                TinvoicelistSave_list.digst0 = 0 

 


                TinvoicelistSave_list.dcgst01 = 0 
                TinvoicelistSave_list.dcgst5 = 0 
                TinvoicelistSave_list.dcgst12 = 0 
                TinvoicelistSave_list.dcgst18 = 0 
                TinvoicelistSave_list.dcgst28 = 0 

                TinvoicelistSave_list.dcgst01 = 0 
                TinvoicelistSave_list.dsgst5 = 0 
                TinvoicelistSave_list.dsgst12 = 0 
                TinvoicelistSave_list.dsgst18 = 0 
                TinvoicelistSave_list.dsgst28 = 0 

                if(TinvoicelistSave_list.sstatecode == TinvoicelistSave_list.slocationstatecode):
                   

                    TinvoicelistSave_list.dsgst01 = dsgst01 
                    TinvoicelistSave_list.dsgst5 = dsgst5 
                    TinvoicelistSave_list.dsgst12 = dsgst12 
                    TinvoicelistSave_list.dsgst18 = dsgst18 
                    TinvoicelistSave_list.dsgst28 = dsgst28 
                else:

                    TinvoicelistSave_list.dcgst01 =dcgst01 
                    TinvoicelistSave_list.dcgst5 = dcgst5 
                    TinvoicelistSave_list.dcgst12 =dcgst12
                    TinvoicelistSave_list.dcgst18 = dcgst18 
                    TinvoicelistSave_list.dcgst28 = dcgst28

                TinvoicelistSave_list.dtotalfinal = dtotalfinal
                TinvoicelistSave_list.dtotalfinal = dtotalfinal
                TinvoicelistSave_list.swords = swords.upper()  

                TinvoicelistSave_list.ackdate1 = ackdate1
                TinvoicelistSave_list.ackdate = ackdate
                TinvoicelistSave_list.ewaydate1 = ewaydate1
                TinvoicelistSave_list.ewaydate = ewaydate
                TinvoicelistSave_list.sdate1 = sdate1
                TinvoicelistSave_list.sdate = sdate
                TinvoicelistSave_list.podate1 = podate1
                TinvoicelistSave_list.podate = podate
                TinvoicelistSave_list.sworkfrom = sworkfrom
                TinvoicelistSave_list.sfromdate = sfromdate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.stodate = stodate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.inrno = inrno
                TinvoicelistSave_list.ackno = ackno
                TinvoicelistSave_list.ewayno = ewayno
                TinvoicelistSave_list.scategoryofservice = scategoryofservice
                TinvoicelistSave_list.stype1 = stype1
                TinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TinvoicelistSave_list.pono = pono
                TinvoicelistSave_list.note1 = note1 

                TinvoicelistSave_list.customerid = customerid
                TinvoicelistSave_list.customername = customername
                TinvoicelistSave_list.saddressclient = saddressclient
                TinvoicelistSave_list.scustomerpan = scustomerpan
                TinvoicelistSave_list.scustomergst = scustomergst
                TinvoicelistSave_list.sstatecode = sstatecode
                
                TinvoicelistSave_list.customersiteid = customersiteid
                TinvoicelistSave_list.customernamesite = customernamesite
                TinvoicelistSave_list.saddresssite = saddresssite 
                TinvoicelistSave_list.swords= swords.upper()
                TinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
        Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        ) 



    
@csrf_exempt
def ProjectListDetails12(request,lID):
    
    salesbillid=0
    salesbillid=lID
    salesbillno=0
    finyear=0
    sinvoicerefno=""
    invoicedate=datetime.today()
    customerid=0
    customername=""
    saddress1=""
    saddress2=""
    saddress3=""
    spin=""
    scity=""
    sstate=""
    scustomerpan=""
    scustomergst=""
    customernamesite=""
    saddress1site=""
    saddress2site=""
    saddress3site=""
    spinsite=""
    scitysite=""
    sstatesite=""
    pono=""
    podate=datetime.today().strftime('%d-%m-%Y')
    dtotal=0
    dgsttrate=0
    dgst=0
    dtotalfinal=0
    swords=""
    sgstsplit=""
    note1=""
    note2=""
    inr=0
    scategoryofservice="B2B  Project"
    username=""
    stype1=""
    sfile1=""
    sfolder1=""
    snumber1=0
    customersiteid=0
    sstatecode=""
    sfromdate=datetime.today().strftime('%d-%m-%Y')
    stodate=datetime.today().strftime('%d-%m-%Y')
    dsgst0=0
    dcgst0=0
    digst0=0
    lnoofedit=0
    ddateofedit=""
    ldepartmentid=0
    sdepartmentname=""
    bdelete=0
    bcancelcopy=0
    bapproval0=0
    bapproval01=0
    bapproval02=0
    bapproval03=0
    bapproval04=0
    bapproval05=0
    bapproval06=0
    bapproval07=0
    bapproval08=0
    bapproval09=0
    bapproval010=0
    scomments=""
    scommentsdelete=""
    lorderid=0
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0
    saddressclient=""
    saddresssite=""
    scompanyaddress=""
    inrno=""
    ackno=""
    ewayno=""
    ewaydate=datetime.today().strftime('%d-%m-%Y')
    ewaydate1=datetime.today().strftime('%Y-%m-%d')
    sdate=datetime.today().strftime('%d-%m-%Y')
    sdate1=datetime.today().strftime('%Y-%m-%d')
    llocationid=0
    slocation=""
    slocationstatecode=""
    slocationgstno=""
    slocationpanno=""
    slocationformat=""
    bsitesez=0
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate =0


    salesordermultiid=0
    #salesbillid=0
    sdesc=""
    partid=0
    partno=""
    qty=0
    unitprice=0
    units=""
    ddescitemtotal=0
    shsn=""
    ssac=""
    smanrate=""
    staxnotify=""
    dsgst01=0
    dcgst01=0
    dcgst00=0
    dsgst5=0
    dcgst5=0
    dcgst50=0
    dsgst12=0
    dcgst12=0
    dcgst120=0
    dsgst18=0
    dcgst18=0
    dcgst180=0
    dsgst28=0
    dcgst28=0
    dcgst280=0
    dgst28cess=0
    dsgst0pt5=0
    dcgst0pt5=0
    dcgst0pt50=0
    dsgst2pt0=0
    dcgst2pt0=0
    dcgst2pt00=0
    dsgst2pt5=0
    dcgst2pt5=0
    dcgst2pt50=0
    dsgst1p0=0
    dcgst1pt0=0
    dcgst1pt00=0


    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            
            return   redirect('CompanyList')  

        if 'cmdGetClient' in request.POST:  

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customerid = customerid
                        TinvoicelistSave_list.customername = customername
                        TinvoicelistSave_list.saddressclient = saddressclient
                        TinvoicelistSave_list.scustomerpan = scustomerpan
                        TinvoicelistSave_list.scustomergst = scustomergst
                        TinvoicelistSave_list.sstatecode = sstatecode
                        TinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customersiteid = customersiteid
                        TinvoicelistSave_list.customernamesite = customernamesite
                        TinvoicelistSave_list.saddresssite = saddresssite 
                        if (sstatecode != ""):
                            TinvoicelistSave_list.sstatecode = sstatecode
                        TinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.customername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        if (MsitelistGet.sstatecode != ""):
                            sstatecode=MsitelistGet.sstatecode 
                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                ackdate1A = ackdate1.split("-")
                ackdate =ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A = podate1.split("-")
                podate =podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom=data.get('txtFrom') 
                sworkfromA = sworkfrom.split("-")
                sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA = sworkfto.split("-")
                stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                TinvoicelistSave_list.ackdate1 = ackdate1
                TinvoicelistSave_list.ackdate = ackdate
                TinvoicelistSave_list.ewaydate1 = ewaydate1
                TinvoicelistSave_list.ewaydate = ewaydate
                TinvoicelistSave_list.sdate1 = sdate1
                TinvoicelistSave_list.sdate = sdate
                TinvoicelistSave_list.podate1 = podate1
                TinvoicelistSave_list.podate = podate
                TinvoicelistSave_list.sworkfrom = sworkfrom
                TinvoicelistSave_list.sfromdate = sfromdate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.stodate = stodate
                TinvoicelistSave_list.sworkfto = sworkfto
                TinvoicelistSave_list.inrno = inrno
                TinvoicelistSave_list.ackno = ackno
                TinvoicelistSave_list.ewayno = ewayno
                TinvoicelistSave_list.scategoryofservice = scategoryofservice
                TinvoicelistSave_list.stype1 = stype1
                TinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TinvoicelistSave_list.pono = pono
                TinvoicelistSave_list.note1 = note1 

                TinvoicelistSave_list.customerid = customerid
                TinvoicelistSave_list.customername = customername
                TinvoicelistSave_list.saddressclient = saddressclient
                TinvoicelistSave_list.scustomerpan = scustomerpan
                TinvoicelistSave_list.scustomergst = scustomergst
                TinvoicelistSave_list.sstatecode = sstatecode
                
                TinvoicelistSave_list.customersiteid = customersiteid
                TinvoicelistSave_list.customernamesite = customernamesite
                TinvoicelistSave_list.saddresssite = saddresssite 
                TinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
                Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProjectListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tinvoicedetailslist_list,
                                }
                                ) 

    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername') 
        
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     

        Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID)  
        Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

        return render(request, "BillingSol/ProjectListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        }
                        ) 



    
@csrf_exempt
def POList(request):
    request.session['lID']  =0


    
@csrf_exempt
def POListAdd(request):
    request.session['lID']  =0

    
@csrf_exempt
def POListDetails(request,lID):
    request.session['lID']  =0


