from django.shortcuts import render
#import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
import re
import calendar
from calendar import HTMLCalendar
from barcode import EAN13
from barcode.writer import ImageWriter
import mimetypes

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

from BillingSol.models import Userlist, Unotevalues, Tserviceinvoicelist, Tserviceinvoicedetailslist 
from BillingSol.models import   Tpurchaseorderlist, Tpurchaseorderdetailslist, Torderacceptancelist, Torderacceptancedetailslist
from BillingSol.models import Tinvoicelist, Tinvoicedetailslist, Tdebitnotelist, Tdebitnotedetailslist, Tcreditnotelist
from BillingSol.models import Tcreditnotedetailslist, Msupplierlist, Mpartdetailslist,  Msitelist
from BillingSol.models import Tdclist, Tdcdetailslist, Tgrnlist, Tgrndetailslist
from BillingSol.models import Tproposallist, Tproposaldetailslist, Tproformalist, Tproformadetailslist
from BillingSol.models import Mcustomerlist, Mcompanylist, Aemailescallationlist, Alogoimage
from BillingSol.models import Tproformaserviceinvoicelist, Tproformaserviceinvoicedetailslist,  Trentinvoicelist, Trentinvoicedetailslist



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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=""


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
                            ssalesbillno = "000" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 3):
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
                        spinsite =McustomerlistGet.slocation
            
            Tserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
def MaintenanceListCopyDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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
 

    Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tserviceinvoicelist_list.customerid
    customername=Tserviceinvoicelist_list.customername
    saddress1=Tserviceinvoicelist_list.saddress1
    saddress2=Tserviceinvoicelist_list.saddress2
    saddress3=Tserviceinvoicelist_list.saddress3
    spin=Tserviceinvoicelist_list.spin
    scity=Tserviceinvoicelist_list.scity
    sstate=Tserviceinvoicelist_list.sstate
    scustomerpan=Tserviceinvoicelist_list.scustomerpan
    scustomergst=Tserviceinvoicelist_list.scustomergst
    customernamesite=Tserviceinvoicelist_list.customernamesite
    saddress1site=Tserviceinvoicelist_list.saddress1site
    saddress2site=Tserviceinvoicelist_list.saddress2site
    saddress3site=Tserviceinvoicelist_list.saddress3site
    spinsite=Tserviceinvoicelist_list.spinsite
    scitysite=Tserviceinvoicelist_list.scitysite
    sstatesite=Tserviceinvoicelist_list.sstatesite
    pono=Tserviceinvoicelist_list.pono
    podate=Tserviceinvoicelist_list.podate
    dtotal=Tserviceinvoicelist_list.dtotal
    dgsttrate=Tserviceinvoicelist_list.dgsttrate
    dgst=Tserviceinvoicelist_list.dgst
    dtotalfinal=Tserviceinvoicelist_list.dtotalfinal
    swords=Tserviceinvoicelist_list.swords
    sgstsplit=Tserviceinvoicelist_list.sgstsplit
    note1=Tserviceinvoicelist_list.note1
    note2=Tserviceinvoicelist_list.note2
    inr=Tserviceinvoicelist_list.inr
    scategoryofservice=Tserviceinvoicelist_list.scategoryofservice
    username=Tserviceinvoicelist_list.username
    stype1=Tserviceinvoicelist_list.stype1
    sfile1=Tserviceinvoicelist_list.sfile1
    sfolder1=Tserviceinvoicelist_list.sfolder1
    snumber1=Tserviceinvoicelist_list.snumber1
    customersiteid=Tserviceinvoicelist_list.customersiteid
    sstatecode=Tserviceinvoicelist_list.sstatecode
    sfromdate=Tserviceinvoicelist_list.sfromdate
    stodate=Tserviceinvoicelist_list.stodate
    dsgst0=Tserviceinvoicelist_list.dsgst0
    dcgst0=Tserviceinvoicelist_list.dcgst0
    digst0=Tserviceinvoicelist_list.digst0
    lnoofedit=Tserviceinvoicelist_list.lnoofedit
    ddateofedit=Tserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tserviceinvoicelist_list.sdepartmentname
    bdelete=Tserviceinvoicelist_list.bdelete
    bcancelcopy=Tserviceinvoicelist_list.bcancelcopy
    bapproval0=Tserviceinvoicelist_list.bapproval0
    bapproval01=Tserviceinvoicelist_list.bapproval01
    bapproval02=Tserviceinvoicelist_list.bapproval02
    bapproval03=Tserviceinvoicelist_list.bapproval03
    bapproval04=Tserviceinvoicelist_list.bapproval04
    bapproval05=Tserviceinvoicelist_list.bapproval05
    bapproval06=Tserviceinvoicelist_list.bapproval06
    bapproval07=Tserviceinvoicelist_list.bapproval07
    bapproval08=Tserviceinvoicelist_list.bapproval08
    bapproval09=Tserviceinvoicelist_list.bapproval09
    bapproval010=Tserviceinvoicelist_list.bapproval010
    scomments=Tserviceinvoicelist_list.scomments
    scommentsdelete=Tserviceinvoicelist_list.scommentsdelete
    lorderid=Tserviceinvoicelist_list.lorderid
    saddressclient=Tserviceinvoicelist_list.saddressclient
    saddresssite=Tserviceinvoicelist_list.saddresssite
    scompanyaddress=Tserviceinvoicelist_list.scompanyaddress
    llocationid=Tserviceinvoicelist_list.llocationid
    slocation=Tserviceinvoicelist_list.slocation
    slocationstatecode=Tserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tserviceinvoicelist_list.slocationgstno
    slocationpanno=Tserviceinvoicelist_list.slocationpanno
    slocationformat=Tserviceinvoicelist_list.slocationformat
    bsitesez=Tserviceinvoicelist_list.bsitesez
    sworkfrom=Tserviceinvoicelist_list.sworkfrom
    sworkfto=Tserviceinvoicelist_list.sworkfto
    podate1=Tserviceinvoicelist_list.podate1
    bsamestate =Tserviceinvoicelist_list.bsamestate 




 
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
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat1 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice1 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Tserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tserviceinvoicelist_AddNewOBJ.salesbillid
  

    Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tserviceinvoicedetailslist_list:
        for Tserviceinvoicedetailslist_listQ in Tserviceinvoicedetailslist_list:
            sdesc=Tserviceinvoicedetailslist_listQ['sdesc']
            partid=Tserviceinvoicedetailslist_listQ['partid']
            partno=Tserviceinvoicedetailslist_listQ['partno']
            qty=Tserviceinvoicedetailslist_listQ['qty']
            unitprice=Tserviceinvoicedetailslist_listQ['unitprice']
            units=Tserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tserviceinvoicedetailslist_listQ['shsn']
            ssac=Tserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('MaintenanceListDetails', lID=salesbillid)  


@csrf_exempt
def MaintenanceListDetailsPrint(request,lID):

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""

    
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
    lLoopFinal =0
    lLoopFinal = Tserviceinvoicedetailslist_list.count()

    lLoopFinal1 =0
    lLoopFinal2 =0
    lLoopFinal3 =0
    lLoopFinal4 =0
    lLoopFinal5 =0
    lLoopFinal6 =0
    lLoopFinal7 =0
    lLoopFinal8 =0
    lLoopFinal9 =0
    lLoopFinal10 =0 

    if(lLoopFinal == 0):
        lLoopFinal10 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
        lLoopFinal5 = 1
        lLoopFinal6 = 1
        lLoopFinal7 = 1
        lLoopFinal8 = 1
        lLoopFinal9 = 1
    if(lLoopFinal == 1):
        lLoopFinal9 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
        lLoopFinal5 = 1
        lLoopFinal6 = 1
        lLoopFinal7 = 1
        lLoopFinal8 = 1
    if(lLoopFinal == 2):
        lLoopFinal8 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
        lLoopFinal5 = 1
        lLoopFinal6 = 1
        lLoopFinal7 = 1
    if(lLoopFinal == 3):
        lLoopFinal7 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
        lLoopFinal5 = 1
        lLoopFinal6 = 1
    if(lLoopFinal == 4):
        lLoopFinal6 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
        lLoopFinal5 = 1
    if(lLoopFinal == 5):
        lLoopFinal5 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
        lLoopFinal4 = 1
    if(lLoopFinal == 6):
        lLoopFinal4 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
        lLoopFinal3 = 1
    if(lLoopFinal == 7):
        lLoopFinal3 =1
        lLoopFinal1 = 1
        lLoopFinal2 = 1
    if(lLoopFinal == 8):
        lLoopFinal2 =1
        lLoopFinal1 = 1
    if(lLoopFinal == 9):
        lLoopFinal1 =1 

    iCountDetails =0
    iCountDetails = Tserviceinvoicedetailslist_list.count

    context = {
            
        'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,   
            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
            'lLoopFinal':lLoopFinal, 
            'lLoopFinal1':lLoopFinal1, 
            'lLoopFinal2':lLoopFinal2, 
            'lLoopFinal3':lLoopFinal3, 
            'lLoopFinal4':lLoopFinal4, 
            'lLoopFinal5':lLoopFinal5, 
            'lLoopFinal6':lLoopFinal6, 
            'lLoopFinal7':lLoopFinal7, 
            'lLoopFinal8':0, 
            'lLoopFinal9':0, 
            'lLoopFinal10':0,
            'iCountDetails' : iCountDetails,
        } 
    
    
    pdf = render_to_pdf('BillingSol/MaintenanceListDetailsPrint.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=""

    
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

            
            return   redirect('MaintenanceList')  
        
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
                        spinsite =McustomerlistGet.slocation
                        
                        
                        TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

                        TserviceinvoicelistSave_list.customerid = customerid
                        TserviceinvoicelistSave_list.customername = customername
                        TserviceinvoicelistSave_list.saddressclient = saddressclient
                        TserviceinvoicelistSave_list.scustomerpan = scustomerpan
                        TserviceinvoicelistSave_list.scustomergst = scustomergst
                        TserviceinvoicelistSave_list.sstatecode = sstatecode
                        TserviceinvoicelistSave_list.spinsite = spinsite
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  


            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            


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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
            lLoopFinal =0
            lLoopFinal = Tserviceinvoicedetailslist_list.count()

            lLoopFinal1 =0
            lLoopFinal2 =0
            lLoopFinal3 =0
            lLoopFinal4 =0
            lLoopFinal5 =0
            lLoopFinal6 =0
            lLoopFinal7 =0
            lLoopFinal8 =0
            lLoopFinal9 =0
            lLoopFinal10 =0 

            if(lLoopFinal == 0):
                lLoopFinal10 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
                lLoopFinal5 = 1
                lLoopFinal6 = 1
                lLoopFinal7 = 1
                lLoopFinal8 = 1
                lLoopFinal9 = 1
            if(lLoopFinal == 1):
                lLoopFinal9 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
                lLoopFinal5 = 1
                lLoopFinal6 = 1
                lLoopFinal7 = 1
                lLoopFinal8 = 1
            if(lLoopFinal == 2):
                lLoopFinal8 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
                lLoopFinal5 = 1
                lLoopFinal6 = 1
                lLoopFinal7 = 1
            if(lLoopFinal == 3):
                lLoopFinal7 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
                lLoopFinal5 = 1
                lLoopFinal6 = 1
            if(lLoopFinal == 4):
                lLoopFinal6 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
                lLoopFinal5 = 1
            if(lLoopFinal == 5):
                lLoopFinal5 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
                lLoopFinal4 = 1
            if(lLoopFinal == 6):
                lLoopFinal4 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
                lLoopFinal3 = 1
            if(lLoopFinal == 7):
                lLoopFinal3 =1
                lLoopFinal1 = 1
                lLoopFinal2 = 1
            if(lLoopFinal == 8):
                lLoopFinal2 =1
                lLoopFinal1 = 1
            if(lLoopFinal == 9):
                lLoopFinal1 =1 

            iCountDetails =0
            iCountDetails = Tserviceinvoicedetailslist_list.count
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                    'lLoopFinal':lLoopFinal, 
                    'lLoopFinal1':lLoopFinal1, 
                    'lLoopFinal2':lLoopFinal2, 
                    'lLoopFinal3':lLoopFinal3, 
                    'lLoopFinal4':lLoopFinal4, 
                    'lLoopFinal5':lLoopFinal5, 
                    'lLoopFinal6':lLoopFinal6, 
                    'lLoopFinal7':lLoopFinal7, 
                    'lLoopFinal8':0, 
                    'lLoopFinal9':0, 
                    'lLoopFinal10':0,
                    'iCountDetails' : iCountDetails,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

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

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            
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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 


        if 'cmdItemSave1' in request.POST:  

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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  

            icountLoop =0
            icountLoopAll =0
            Tserviceinvoicedetailslist_listGetLoop = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tserviceinvoicedetailslist_listGetLoop.count()

            for Tserviceinvoicedetailslist_listGetLoopA in Tserviceinvoicedetailslist_listGetLoop:
                
                icountLoop=Tserviceinvoicedetailslist_listGetLoopA['salesordermultiid']
                salesordermultiid=data.get('txtItemID' + str(icountLoop))  
                sdesc=data.get('txtItemDesc1' + str(icountLoop))  
                qty=data.get('txtQuantity1' + str(icountLoop))  
                unitprice=data.get('txtRate1' + str(icountLoop))
                units=data.get('txtUnits1' + str(icountLoop))
                ddescitemtotal=data.get('txtItemAmt1' + str(icountLoop))
                shsn=data.get('txtHSNCode1' + str(icountLoop))
                dtotal=data.get('txtItemTotalAmt1' + str(icountLoop))
                ltaxrate=data.get('txtGSTRate1' + str(icountLoop))  
                ltaxrateamt=data.get('txtGSTAmt1' + str(icountLoop))  
                staxnotify=data.get('txtPOAMt1' + str(icountLoop))  
                ltaxrateamt1=0 
                ltaxrateamt2=0   


                ddescitemtotal =float(unitprice) * float(qty)
                ltaxrateamt =ddescitemtotal * float(ltaxrate)/100
                if(TserviceinvoicelistSave_list.sstatecode == TserviceinvoicelistSave_list.slocationstatecode):
                    ltaxrateamt1 =ltaxrateamt/2
                    ltaxrateamt1 =ltaxrateamt/2

                dtotal = round(ddescitemtotal + ltaxrateamt)


                Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tserviceinvoicedetailslist_AddNewOBJ.sdesc = sdesc
                Tserviceinvoicedetailslist_AddNewOBJ.unitprice = unitprice
                Tserviceinvoicedetailslist_AddNewOBJ.units = units
                Tserviceinvoicedetailslist_AddNewOBJ.qty = qty
                Tserviceinvoicedetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tserviceinvoicedetailslist_AddNewOBJ.shsn = shsn
                Tserviceinvoicedetailslist_AddNewOBJ.dtotal = dtotal
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrate = ltaxrate
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt = ltaxrateamt
                Tserviceinvoicedetailslist_AddNewOBJ.staxnotify = staxnotify
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt1 = ltaxrateamt1
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt2 = ltaxrateamt2

                #Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 
                # 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	
                # shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	
                # ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

                Tserviceinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Edited successfully!')


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

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            
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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

    









@csrf_exempt
def ProformaServiceInvoiceList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProformaServiceInvoiceListAdd')  
        
    else:
        
        Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.order_by('-invoicedate', '-salesbillno')  


        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tproformaserviceinvoicelist_list.count()
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
        paginator = Paginator(Tproformaserviceinvoicelist_list, lRecCount1)
        try:
            Tproformaserviceinvoicelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tproformaserviceinvoicelist_lists = paginator.page(1)
        except EmptyPage:
            Tproformaserviceinvoicelist_lists = paginator.page(paginator.num_pages)


        return render(request, "BillingSol/ProformaServiceInvoiceList.html",
                    {
                        'Tproformaserviceinvoicelist_list':Tproformaserviceinvoicelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def ProformaServiceInvoiceListAdd(request):

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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

            return   redirect('ProformaServiceInvoiceList') 

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

                        salesbillno=McompanylistGet.linvoice10 + 1
                        finyear=McompanylistGet.lyear
                        if(McompanylistGet.lyear < 4):
                            if(datetime.today().month >= 4):
                                finyear=datetime.today().month
                                salesbillno = 1

                        ssalesbillno = ""
                        ssalesbillno = str(salesbillno)
                        if(len(ssalesbillno) == 1):
                            ssalesbillno = "000" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 3):
                            ssalesbillno = "0" + ssalesbillno
                        sinvoicerefno=McompanylistGet.sformat10 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice10 = salesbillno
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
                        spinsite =McustomerlistGet.slocation
            
            Tproformaserviceinvoicelist_AddNewOBJ = Tproformaserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
    
            Tproformaserviceinvoicelist_AddNewOBJ.save()
            salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid

            return   redirect('ProformaServiceInvoiceListDetails', lID=salesbillid)  
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProformaServiceInvoiceListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


    
    
@csrf_exempt
def ProformaServiceInvoiceListDetailsDelete(request,lID):
    lCatID = 0
    
    lDetId =0

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tproformaserviceinvoicedetailslist_list.salesbillid
    
    # if Tproformaserviceinvoicedetailslist_list:
    #     for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
    #         lDetId = Tproformaserviceinvoicedetailslist_listQ['salesbillid']

    Tproformaserviceinvoicelist_listOBJ =  Tproformaserviceinvoicedetailslist.objects.get(salesordermultiid=lID).delete()
            


    Tproformaserviceinvoicelist_listSave = Tproformaserviceinvoicelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tproformaserviceinvoicedetailslist_listG = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lDetId).values() 



    if Tproformaserviceinvoicedetailslist_listG:
        for Tproformaserviceinvoicedetailslist_listGT in Tproformaserviceinvoicedetailslist_listG:
            dtotal =dtotal + float(Tproformaserviceinvoicedetailslist_listGT['ddescitemtotal'])
            ltaxrateamt =ltaxrateamt + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
            digst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
            dsgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt1'])
            dcgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
            dtotalfinal =dtotalfinal + float(Tproformaserviceinvoicedetailslist_listGT['dtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    Tproformaserviceinvoicelist_listSave.dtotal = dtotal
    Tproformaserviceinvoicelist_listSave.dgsttrate = ltaxrateamt

    Tproformaserviceinvoicelist_listSave.dsgst0 = 0
    Tproformaserviceinvoicelist_listSave.dcgst0 = 0 
    Tproformaserviceinvoicelist_listSave.digst0 = 0
    if(Tproformaserviceinvoicelist_listSave.sstatecode == Tproformaserviceinvoicelist_listSave.slocationstatecode):
        Tproformaserviceinvoicelist_listSave.dsgst0 = ltaxrateamt/2
        Tproformaserviceinvoicelist_listSave.dcgst0 = ltaxrateamt/2 
    else:
        Tproformaserviceinvoicelist_listSave.digst0 = ltaxrateamt

    Tproformaserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tproformaserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tproformaserviceinvoicelist_listSave.swords= swords.upper()

    
    Tproformaserviceinvoicelist_listSave.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaServiceInvoiceListDetails', lID=lDetId)  


    
@csrf_exempt
def ProformaServiceInvoiceListCopyDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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
    

    Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tproformaserviceinvoicelist_list.customerid
    customername=Tproformaserviceinvoicelist_list.customername
    saddress1=Tproformaserviceinvoicelist_list.saddress1
    saddress2=Tproformaserviceinvoicelist_list.saddress2
    saddress3=Tproformaserviceinvoicelist_list.saddress3
    spin=Tproformaserviceinvoicelist_list.spin
    scity=Tproformaserviceinvoicelist_list.scity
    sstate=Tproformaserviceinvoicelist_list.sstate
    scustomerpan=Tproformaserviceinvoicelist_list.scustomerpan
    scustomergst=Tproformaserviceinvoicelist_list.scustomergst
    customernamesite=Tproformaserviceinvoicelist_list.customernamesite
    saddress1site=Tproformaserviceinvoicelist_list.saddress1site
    saddress2site=Tproformaserviceinvoicelist_list.saddress2site
    saddress3site=Tproformaserviceinvoicelist_list.saddress3site
    spinsite=Tproformaserviceinvoicelist_list.spinsite
    scitysite=Tproformaserviceinvoicelist_list.scitysite
    sstatesite=Tproformaserviceinvoicelist_list.sstatesite
    pono=Tproformaserviceinvoicelist_list.pono
    podate=Tproformaserviceinvoicelist_list.podate
    dtotal=Tproformaserviceinvoicelist_list.dtotal
    dgsttrate=Tproformaserviceinvoicelist_list.dgsttrate
    dgst=Tproformaserviceinvoicelist_list.dgst
    dtotalfinal=Tproformaserviceinvoicelist_list.dtotalfinal
    swords=Tproformaserviceinvoicelist_list.swords
    sgstsplit=Tproformaserviceinvoicelist_list.sgstsplit
    note1=Tproformaserviceinvoicelist_list.note1
    note2=Tproformaserviceinvoicelist_list.note2
    inr=Tproformaserviceinvoicelist_list.inr
    scategoryofservice=Tproformaserviceinvoicelist_list.scategoryofservice
    username=Tproformaserviceinvoicelist_list.username
    stype1=Tproformaserviceinvoicelist_list.stype1
    sfile1=Tproformaserviceinvoicelist_list.sfile1
    sfolder1=Tproformaserviceinvoicelist_list.sfolder1
    snumber1=Tproformaserviceinvoicelist_list.snumber1
    customersiteid=Tproformaserviceinvoicelist_list.customersiteid
    sstatecode=Tproformaserviceinvoicelist_list.sstatecode
    sfromdate=Tproformaserviceinvoicelist_list.sfromdate
    stodate=Tproformaserviceinvoicelist_list.stodate
    dsgst0=Tproformaserviceinvoicelist_list.dsgst0
    dcgst0=Tproformaserviceinvoicelist_list.dcgst0
    digst0=Tproformaserviceinvoicelist_list.digst0
    lnoofedit=Tproformaserviceinvoicelist_list.lnoofedit
    ddateofedit=Tproformaserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tproformaserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tproformaserviceinvoicelist_list.sdepartmentname
    bdelete=Tproformaserviceinvoicelist_list.bdelete
    bcancelcopy=Tproformaserviceinvoicelist_list.bcancelcopy
    bapproval0=Tproformaserviceinvoicelist_list.bapproval0
    bapproval01=Tproformaserviceinvoicelist_list.bapproval01
    bapproval02=Tproformaserviceinvoicelist_list.bapproval02
    bapproval03=Tproformaserviceinvoicelist_list.bapproval03
    bapproval04=Tproformaserviceinvoicelist_list.bapproval04
    bapproval05=Tproformaserviceinvoicelist_list.bapproval05
    bapproval06=Tproformaserviceinvoicelist_list.bapproval06
    bapproval07=Tproformaserviceinvoicelist_list.bapproval07
    bapproval08=Tproformaserviceinvoicelist_list.bapproval08
    bapproval09=Tproformaserviceinvoicelist_list.bapproval09
    bapproval010=Tproformaserviceinvoicelist_list.bapproval010
    scomments=Tproformaserviceinvoicelist_list.scomments
    scommentsdelete=Tproformaserviceinvoicelist_list.scommentsdelete
    lorderid=Tproformaserviceinvoicelist_list.lorderid
    saddressclient=Tproformaserviceinvoicelist_list.saddressclient
    saddresssite=Tproformaserviceinvoicelist_list.saddresssite
    scompanyaddress=Tproformaserviceinvoicelist_list.scompanyaddress
    llocationid=Tproformaserviceinvoicelist_list.llocationid
    slocation=Tproformaserviceinvoicelist_list.slocation
    slocationstatecode=Tproformaserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tproformaserviceinvoicelist_list.slocationgstno
    slocationpanno=Tproformaserviceinvoicelist_list.slocationpanno
    slocationformat=Tproformaserviceinvoicelist_list.slocationformat
    bsitesez=Tproformaserviceinvoicelist_list.bsitesez
    sworkfrom=Tproformaserviceinvoicelist_list.sworkfrom
    sworkfto=Tproformaserviceinvoicelist_list.sworkfto
    podate1=Tproformaserviceinvoicelist_list.podate1
    bsamestate =Tproformaserviceinvoicelist_list.bsamestate 




    
    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
    if McompanylistGet:
        slocation = McompanylistGet.scompanyname  
        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
            
        slocationgstno=McompanylistGet.sgstno 
        slocationpanno=McompanylistGet.spanno
        slocationstatecode=McompanylistGet.sstatecode

        salesbillno=McompanylistGet.linvoice10 + 1
        finyear=McompanylistGet.lyear
        if(McompanylistGet.lyear < 4):
            if(datetime.today().month >= 4):
                finyear=datetime.today().month
                salesbillno = 1

        ssalesbillno = ""
        ssalesbillno = str(salesbillno)
        if(len(ssalesbillno) == 1):
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat10 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice10 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

    
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tproformaserviceinvoicelist_AddNewOBJ = Tproformaserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Tproformaserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid
    

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformaserviceinvoicedetailslist_list:
        for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
            sdesc=Tproformaserviceinvoicedetailslist_listQ['sdesc']
            partid=Tproformaserviceinvoicedetailslist_listQ['partid']
            partno=Tproformaserviceinvoicedetailslist_listQ['partno']
            qty=Tproformaserviceinvoicedetailslist_listQ['qty']
            unitprice=Tproformaserviceinvoicedetailslist_listQ['unitprice']
            units=Tproformaserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tproformaserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tproformaserviceinvoicedetailslist_listQ['shsn']
            ssac=Tproformaserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tproformaserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tproformaserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tproformaserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaServiceInvoiceListDetails', lID=salesbillid)  





@csrf_exempt
def ProformaServiceInvoiceListDetails(request,lID):
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""

    
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

            
            return   redirect('ProformaServiceInvoiceList')  
        
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
                        spinsite =McustomerlistGet.slocation
                        
                        
                        TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

                        TproformaserviceinvoicelistSave_list.customerid = customerid
                        TproformaserviceinvoicelistSave_list.customername = customername
                        TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
                        TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
                        TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
                        TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
                        TproformaserviceinvoicelistSave_list.spinsite = spinsite
                        TproformaserviceinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
                Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                            
                        #sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

                        TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
                        TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
                        TproformaserviceinvoicelistSave_list.saddresssite = saddresssite 

                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        TproformaserviceinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformaserviceinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                            'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 


            bsitesez =0
            if 'bsitesez' in request.POST: 
                bsitesez = 1


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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                            

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                            
                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                #ackdate1A = ackdate1.split("-")
                ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                #ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A =podate1 # podate1.split("-")
                podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom="" #data.get('txtFrom') 
                sfromdate=data.get('txtFrom') 
                # sworkfromA = sworkfrom.split("-")
                # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                stodate=data.get('txtTo') 
                # sworkftoA = sworkfto.split("-")
                # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                sworkfrom="" #data.get('txtFrom') 
                sworkfromA = sworkfrom # sworkfrom.split("-")
                sfromdate =sworkfrom #sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA =sworkfto # sworkfto.split("-")
                stodate =sworkfto #sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                TproformaserviceinvoicelistSave_list.bsitesez = bsitesez

                breversechargemechanism =0
                if 'breversechargemechanism' in request.POST: 
                    breversechargemechanism=1

                TproformaserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
                

                TproformaserviceinvoicelistSave_list.ackdate1 = ackdate1
                TproformaserviceinvoicelistSave_list.ackdate = ackdate
                TproformaserviceinvoicelistSave_list.ewaydate1 = ewaydate1
                TproformaserviceinvoicelistSave_list.ewaydate = ewaydate
                TproformaserviceinvoicelistSave_list.sdate1 = sdate1
                TproformaserviceinvoicelistSave_list.sdate = sdate
                TproformaserviceinvoicelistSave_list.podate1 = podate1
                TproformaserviceinvoicelistSave_list.podate = podate
                TproformaserviceinvoicelistSave_list.sworkfrom = sworkfrom
                TproformaserviceinvoicelistSave_list.sfromdate = sfromdate
                TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
                TproformaserviceinvoicelistSave_list.stodate = stodate
                TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
                TproformaserviceinvoicelistSave_list.inrno = inrno
                TproformaserviceinvoicelistSave_list.ackno = ackno
                TproformaserviceinvoicelistSave_list.ewayno = ewayno
                TproformaserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
                TproformaserviceinvoicelistSave_list.stype1 = stype1
                TproformaserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TproformaserviceinvoicelistSave_list.pono = pono
                TproformaserviceinvoicelistSave_list.note1 = note1 

                TproformaserviceinvoicelistSave_list.customerid = customerid
                TproformaserviceinvoicelistSave_list.customername = customername
                TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
                TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
                TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
                TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
                TproformaserviceinvoicelistSave_list.spinsite = spinsite
                
                TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
                TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
                TproformaserviceinvoicelistSave_list.saddresssite = saddresssite  

                TproformaserviceinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
                Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
    


            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            if(Tproformaserviceinvoicelist_list.ackno != ""):
                if(len(Tproformaserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tproformaserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                    my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            iCountDetails =0
            iCountDetails = Tproformaserviceinvoicedetailslist_list.count
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                     'iCountDetails' : iCountDetails, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProformaServiceInvoiceListDetailsPrint.html', context)
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

            TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 


            bsitesez =0
            if 'bsitesez' in request.POST: 
                bsitesez = 1


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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                            

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                            
                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

            ackdate1A =""
            ewaydate1A =""
            sdate1A =""
            podate1A =""
            sworkfromA =""
            sworkftoA =""

            ackdate1=data.get('txtAckDate') 
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            #sworkfrom="" #data.get('txtFrom') 
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
            if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                ltaxrateamt1 =ltaxrateamt/2
                ltaxrateamt1 =ltaxrateamt/2

            dtotal = round(ddescitemtotal + ltaxrateamt)


            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Added successfully!')


            Tproformaserviceinvoicedetailslist_listG = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            ltaxrateamt =0
            digst0 = 0
            dsgst0 = 0
            dcgst0 = 0
            dgsttrate = 0
            dtotalfinal = 0
            dtotal=0

                        

            if Tproformaserviceinvoicedetailslist_listG:
                for Tproformaserviceinvoicedetailslist_listGT in Tproformaserviceinvoicedetailslist_listG:
                    dtotal =dtotal + float(Tproformaserviceinvoicedetailslist_listGT['ddescitemtotal'])
                    ltaxrateamt =ltaxrateamt + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    digst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    dsgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt1'])
                    dcgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
                    dtotalfinal =dtotalfinal + float(Tproformaserviceinvoicedetailslist_listGT['dtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TproformaserviceinvoicelistSave_list.dtotal = dtotal
            TproformaserviceinvoicelistSave_list.dgsttrate = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dsgst0 = 0
            TproformaserviceinvoicelistSave_list.dcgst0 = 0 
            TproformaserviceinvoicelistSave_list.digst0 = 0 


            if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                TproformaserviceinvoicelistSave_list.dsgst0 = ltaxrateamt/2
                TproformaserviceinvoicelistSave_list.dcgst0 = ltaxrateamt/2
            else:
                TproformaserviceinvoicelistSave_list.digst0 = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.swords = swords.upper()  

            TproformaserviceinvoicelistSave_list.bsitesez = bsitesez

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TproformaserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            

            TproformaserviceinvoicelistSave_list.ackdate1 = ackdate1
            TproformaserviceinvoicelistSave_list.ackdate = ackdate
            TproformaserviceinvoicelistSave_list.ewaydate1 = ewaydate1
            TproformaserviceinvoicelistSave_list.ewaydate = ewaydate
            TproformaserviceinvoicelistSave_list.sdate1 = sdate1
            TproformaserviceinvoicelistSave_list.sdate = sdate
            TproformaserviceinvoicelistSave_list.podate1 = podate1
            TproformaserviceinvoicelistSave_list.podate = podate
            TproformaserviceinvoicelistSave_list.sworkfrom = sworkfrom
            TproformaserviceinvoicelistSave_list.sfromdate = sfromdate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.stodate = stodate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.inrno = inrno
            TproformaserviceinvoicelistSave_list.ackno = ackno
            TproformaserviceinvoicelistSave_list.ewayno = ewayno
            TproformaserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
            TproformaserviceinvoicelistSave_list.stype1 = stype1
            TproformaserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
            TproformaserviceinvoicelistSave_list.pono = pono
            TproformaserviceinvoicelistSave_list.note1 = note1 

            TproformaserviceinvoicelistSave_list.customerid = customerid
            TproformaserviceinvoicelistSave_list.customername = customername
            TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
            TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
            TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
            TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
            TproformaserviceinvoicelistSave_list.spinsite = spinsite
            
            TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
            TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
            TproformaserviceinvoicelistSave_list.saddresssite = saddresssite 
            TproformaserviceinvoicelistSave_list.swords= swords.upper()
            TproformaserviceinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

        Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
        Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformaserviceinvoicelist_list.customerid).values() 
            
        return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                            'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

    









@csrf_exempt
def MaintenanceListSEZ(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('MaintenanceListSEZAdd')  
        
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


        return render(request, "BillingSol/MaintenanceInvoiceListSEZ.html",
                    {
                        'Tserviceinvoicelist_list':Tserviceinvoicelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def MaintenanceListSEZAdd(request):

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    bsitesez=1
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=0


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

            return   redirect('MaintenanceListSEZ') 

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
                            ssalesbillno = "000" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 3):
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
                        spinsite =McustomerlistGet.slocation
            
            Tserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate, slutno=slutno, breversechargemechanism= breversechargemechanism)
 
            Tserviceinvoicelist_AddNewOBJ.save()
            salesbillid = Tserviceinvoicelist_AddNewOBJ.salesbillid

            return   redirect('MaintenanceListSEZDetails', lID=salesbillid)  
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/MaintenanceListSEZAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


    
  
@csrf_exempt
def MaintenanceListSEZDetailsDelete(request,lID):
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
    return redirect('MaintenanceListSEZDetails', lID=lDetId)  


  
@csrf_exempt
def MaintenanceListSEZCopyDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    bsitesez=1
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=0


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
 

    Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tserviceinvoicelist_list.customerid
    customername=Tserviceinvoicelist_list.customername
    saddress1=Tserviceinvoicelist_list.saddress1
    saddress2=Tserviceinvoicelist_list.saddress2
    saddress3=Tserviceinvoicelist_list.saddress3
    spin=Tserviceinvoicelist_list.spin
    scity=Tserviceinvoicelist_list.scity
    sstate=Tserviceinvoicelist_list.sstate
    scustomerpan=Tserviceinvoicelist_list.scustomerpan
    scustomergst=Tserviceinvoicelist_list.scustomergst
    customernamesite=Tserviceinvoicelist_list.customernamesite
    saddress1site=Tserviceinvoicelist_list.saddress1site
    saddress2site=Tserviceinvoicelist_list.saddress2site
    saddress3site=Tserviceinvoicelist_list.saddress3site
    spinsite=Tserviceinvoicelist_list.spinsite
    scitysite=Tserviceinvoicelist_list.scitysite
    sstatesite=Tserviceinvoicelist_list.sstatesite
    pono=Tserviceinvoicelist_list.pono
    podate=Tserviceinvoicelist_list.podate
    dtotal=Tserviceinvoicelist_list.dtotal
    dgsttrate=Tserviceinvoicelist_list.dgsttrate
    dgst=Tserviceinvoicelist_list.dgst
    dtotalfinal=Tserviceinvoicelist_list.dtotalfinal
    swords=Tserviceinvoicelist_list.swords
    sgstsplit=Tserviceinvoicelist_list.sgstsplit
    note1=Tserviceinvoicelist_list.note1
    note2=Tserviceinvoicelist_list.note2
    inr=Tserviceinvoicelist_list.inr
    scategoryofservice=Tserviceinvoicelist_list.scategoryofservice
    username=Tserviceinvoicelist_list.username
    stype1=Tserviceinvoicelist_list.stype1
    sfile1=Tserviceinvoicelist_list.sfile1
    sfolder1=Tserviceinvoicelist_list.sfolder1
    snumber1=Tserviceinvoicelist_list.snumber1
    customersiteid=Tserviceinvoicelist_list.customersiteid
    sstatecode=Tserviceinvoicelist_list.sstatecode
    sfromdate=Tserviceinvoicelist_list.sfromdate
    stodate=Tserviceinvoicelist_list.stodate
    dsgst0=Tserviceinvoicelist_list.dsgst0
    dcgst0=Tserviceinvoicelist_list.dcgst0
    digst0=Tserviceinvoicelist_list.digst0
    lnoofedit=Tserviceinvoicelist_list.lnoofedit
    ddateofedit=Tserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tserviceinvoicelist_list.sdepartmentname
    bdelete=Tserviceinvoicelist_list.bdelete
    bcancelcopy=Tserviceinvoicelist_list.bcancelcopy
    bapproval0=Tserviceinvoicelist_list.bapproval0
    bapproval01=Tserviceinvoicelist_list.bapproval01
    bapproval02=Tserviceinvoicelist_list.bapproval02
    bapproval03=Tserviceinvoicelist_list.bapproval03
    bapproval04=Tserviceinvoicelist_list.bapproval04
    bapproval05=Tserviceinvoicelist_list.bapproval05
    bapproval06=Tserviceinvoicelist_list.bapproval06
    bapproval07=Tserviceinvoicelist_list.bapproval07
    bapproval08=Tserviceinvoicelist_list.bapproval08
    bapproval09=Tserviceinvoicelist_list.bapproval09
    bapproval010=Tserviceinvoicelist_list.bapproval010
    scomments=Tserviceinvoicelist_list.scomments
    scommentsdelete=Tserviceinvoicelist_list.scommentsdelete
    lorderid=Tserviceinvoicelist_list.lorderid
    saddressclient=Tserviceinvoicelist_list.saddressclient
    saddresssite=Tserviceinvoicelist_list.saddresssite
    scompanyaddress=Tserviceinvoicelist_list.scompanyaddress
    llocationid=Tserviceinvoicelist_list.llocationid
    slocation=Tserviceinvoicelist_list.slocation
    slocationstatecode=Tserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tserviceinvoicelist_list.slocationgstno
    slocationpanno=Tserviceinvoicelist_list.slocationpanno
    slocationformat=Tserviceinvoicelist_list.slocationformat
    bsitesez=Tserviceinvoicelist_list.bsitesez
    sworkfrom=Tserviceinvoicelist_list.sworkfrom
    sworkfto=Tserviceinvoicelist_list.sworkfto
    podate1=Tserviceinvoicelist_list.podate1
    bsamestate =Tserviceinvoicelist_list.bsamestate 
    slutno =Tserviceinvoicelist_list.slutno 
    breversechargemechanism =Tserviceinvoicelist_list.breversechargemechanism 




 
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
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat1 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice1 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate, slutno=slutno, breversechargemechanism= breversechargemechanism)

    Tserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tserviceinvoicelist_AddNewOBJ.salesbillid
  

    Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tserviceinvoicedetailslist_list:
        for Tserviceinvoicedetailslist_listQ in Tserviceinvoicedetailslist_list:
            sdesc=Tserviceinvoicedetailslist_listQ['sdesc']
            partid=Tserviceinvoicedetailslist_listQ['partid']
            partno=Tserviceinvoicedetailslist_listQ['partno']
            qty=Tserviceinvoicedetailslist_listQ['qty']
            unitprice=Tserviceinvoicedetailslist_listQ['unitprice']
            units=Tserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tserviceinvoicedetailslist_listQ['shsn']
            ssac=Tserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('MaintenanceListSEZDetails', lID=salesbillid)  





@csrf_exempt
def MaintenanceListSEZDetails(request,lID):
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    bsitesez=1
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=0

    
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

            
            return   redirect('MaintenanceListSEZ')  
        
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
                        spinsite =McustomerlistGet.slocation 
                        
                        
                        TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

                        TserviceinvoicelistSave_list.customerid = customerid
                        TserviceinvoicelistSave_list.customername = customername
                        TserviceinvoicelistSave_list.saddressclient = saddressclient
                        TserviceinvoicelistSave_list.scustomerpan = scustomerpan
                        TserviceinvoicelistSave_list.scustomergst = scustomergst
                        TserviceinvoicelistSave_list.sstatecode = sstatecode
                        TserviceinvoicelistSave_list.spinsite = spinsite
                        TserviceinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
                Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/MaintenanceListSEZDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        #sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TserviceinvoicelistSave_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 

                        TserviceinvoicelistSave_list.customersiteid = customersiteid
                        TserviceinvoicelistSave_list.customernamesite = customernamesite
                        TserviceinvoicelistSave_list.saddresssite = saddresssite 
                        TserviceinvoicelistSave_list.slutno = txtslutno  

                        TserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        TserviceinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tserviceinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/MaintenanceListSEZDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  
            txtslutno=data.get('txtslutno') 

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            


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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
            TserviceinvoicelistSave_list.customersiteid = customersiteid
            TserviceinvoicelistSave_list.customernamesite = customernamesite
            TserviceinvoicelistSave_list.saddresssite = saddresssite 
            TserviceinvoicelistSave_list.slutno = txtslutno  

            TserviceinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/MaintenanceListSEZDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
                    
            iCountDetails =0
            iCountDetails = Tserviceinvoicedetailslist_list.count
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                    'iCountDetails' : iCountDetails,
                } 
            
            
            pdf = render_to_pdf('BillingSol/MaintenanceListSEZDetailsPrint.html', context)
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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  
            txtslutno=data.get('txtslutno') 


            sdesc=data.get('txtItemDesc')  
            qty=data.get('txtQuantity')  
            unitprice=data.get('txtRate')
            units=data.get('txtUnits')
            ddescitemtotal=data.get('txtItemAmt')
            shsn=data.get('txtHSNCode')
            dtotal=data.get('txtItemTotalAmt')
            ltaxrate=0 
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

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            

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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
            TserviceinvoicelistSave_list.customersiteid = customersiteid
            TserviceinvoicelistSave_list.customernamesite = customernamesite
            TserviceinvoicelistSave_list.saddresssite = saddresssite 
            TserviceinvoicelistSave_list.swords= swords.upper()
            TserviceinvoicelistSave_list.slutno = txtslutno  
            TserviceinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
            Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/MaintenanceListSEZDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                                'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 


        if 'cmdItemSave1' in request.POST:  

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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
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
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

          
            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 
          
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  

            icountLoop =0
            icountLoopAll =0
            Tserviceinvoicedetailslist_listGetLoop = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tserviceinvoicedetailslist_listGetLoop.count()

            for Tserviceinvoicedetailslist_listGetLoopA in Tserviceinvoicedetailslist_listGetLoop:
                
                icountLoop=Tserviceinvoicedetailslist_listGetLoopA['salesordermultiid']
                salesordermultiid=data.get('txtItemID' + str(icountLoop))  
                sdesc=data.get('txtItemDesc1' + str(icountLoop))  
                qty=data.get('txtQuantity1' + str(icountLoop))  
                unitprice=data.get('txtRate1' + str(icountLoop))
                units=data.get('txtUnits1' + str(icountLoop))
                ddescitemtotal=data.get('txtItemAmt1' + str(icountLoop))
                shsn=data.get('txtHSNCode1' + str(icountLoop))
                dtotal=data.get('txtItemTotalAmt1' + str(icountLoop))
                ltaxrate=0 
                ltaxrateamt=data.get('txtGSTAmt1' + str(icountLoop))  
                staxnotify=data.get('txtPOAMt1' + str(icountLoop))  
                ltaxrateamt1=0 
                ltaxrateamt2=0   


                ddescitemtotal =float(unitprice) * float(qty)
                ltaxrateamt =ddescitemtotal * float(ltaxrate)/100
                if(TserviceinvoicelistSave_list.sstatecode == TserviceinvoicelistSave_list.slocationstatecode):
                    ltaxrateamt1 =ltaxrateamt/2
                    ltaxrateamt1 =ltaxrateamt/2

                dtotal = round(ddescitemtotal + ltaxrateamt)


                Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tserviceinvoicedetailslist_AddNewOBJ.sdesc = sdesc
                Tserviceinvoicedetailslist_AddNewOBJ.unitprice = unitprice
                Tserviceinvoicedetailslist_AddNewOBJ.units = units
                Tserviceinvoicedetailslist_AddNewOBJ.qty = qty
                Tserviceinvoicedetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tserviceinvoicedetailslist_AddNewOBJ.shsn = shsn
                Tserviceinvoicedetailslist_AddNewOBJ.dtotal = dtotal
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrate = ltaxrate
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt = ltaxrateamt
                Tserviceinvoicedetailslist_AddNewOBJ.staxnotify = staxnotify
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt1 = ltaxrateamt1
                Tserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt2 = ltaxrateamt2

                #Tserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 
                # 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	
                # shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	
                # ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

                Tserviceinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Edited successfully!')


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

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            
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
            TserviceinvoicelistSave_list.spinsite = spinsite
            
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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tserviceinvoicelist_list = Tserviceinvoicelist.objects.get(salesbillid=lID) 
        Tserviceinvoicedetailslist_list = Tserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tserviceinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/MaintenanceListSEZDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

    









                        


@csrf_exempt
def ProformaServiceInvoiceList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProformaServiceInvoiceListAdd')  
        
    else:
        
        Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.order_by('-invoicedate', '-salesbillno')  


        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tproformaserviceinvoicelist_list.count()
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
        paginator = Paginator(Tproformaserviceinvoicelist_list, lRecCount1)
        try:
            Tproformaserviceinvoicelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tproformaserviceinvoicelist_lists = paginator.page(1)
        except EmptyPage:
            Tproformaserviceinvoicelist_lists = paginator.page(paginator.num_pages)


        return render(request, "BillingSol/ProformaServiceInvoiceList.html",
                    {
                        'Tproformaserviceinvoicelist_list':Tproformaserviceinvoicelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def ProformaServiceInvoiceListAdd(request):

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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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

            return   redirect('ProformaServiceInvoiceList') 

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

                        salesbillno=McompanylistGet.linvoice10 + 1
                        finyear=McompanylistGet.lyear
                        if(McompanylistGet.lyear < 4):
                            if(datetime.today().month >= 4):
                                finyear=datetime.today().month
                                salesbillno = 1

                        ssalesbillno = ""
                        ssalesbillno = str(salesbillno)
                        if(len(ssalesbillno) == 1):
                            ssalesbillno = "000" + ssalesbillno
                        elif(len(ssalesbillno) == 2):
                            ssalesbillno = "00" + ssalesbillno
                        elif(len(ssalesbillno) == 3):
                            ssalesbillno = "0" + ssalesbillno
                        sinvoicerefno=McompanylistGet.sformat10 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice10 = salesbillno
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
                        spinsite =McustomerlistGet.slocation
            
            Tproformaserviceinvoicelist_AddNewOBJ = Tproformaserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
            Tproformaserviceinvoicelist_AddNewOBJ.save()
            salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid

            return   redirect('ProformaServiceInvoiceListDetails', lID=salesbillid)  
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProformaServiceInvoiceListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


    
  
@csrf_exempt
def ProformaServiceInvoiceListDetailsDelete(request,lID):
    lCatID = 0
    
    lDetId =0

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tproformaserviceinvoicedetailslist_list.salesbillid
    
    # if Tproformaserviceinvoicedetailslist_list:
    #     for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
    #         lDetId = Tproformaserviceinvoicedetailslist_listQ['salesbillid']

    Tproformaserviceinvoicelist_listOBJ =  Tproformaserviceinvoicedetailslist.objects.get(salesordermultiid=lID).delete()
          


    Tproformaserviceinvoicelist_listSave = Tproformaserviceinvoicelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tproformaserviceinvoicedetailslist_listG = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lDetId).values() 



    if Tproformaserviceinvoicedetailslist_listG:
        for Tproformaserviceinvoicedetailslist_listGT in Tproformaserviceinvoicedetailslist_listG:
            dtotal =dtotal + float(Tproformaserviceinvoicedetailslist_listGT['ddescitemtotal'])
            ltaxrateamt =ltaxrateamt + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
            digst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
            dsgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt1'])
            dcgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
            dtotalfinal =dtotalfinal + float(Tproformaserviceinvoicedetailslist_listGT['dtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    Tproformaserviceinvoicelist_listSave.dtotal = dtotal
    Tproformaserviceinvoicelist_listSave.dgsttrate = ltaxrateamt

    Tproformaserviceinvoicelist_listSave.dsgst0 = 0
    Tproformaserviceinvoicelist_listSave.dcgst0 = 0 
    Tproformaserviceinvoicelist_listSave.digst0 = 0
    if(Tproformaserviceinvoicelist_listSave.sstatecode == Tproformaserviceinvoicelist_listSave.slocationstatecode):
        Tproformaserviceinvoicelist_listSave.dsgst0 = ltaxrateamt/2
        Tproformaserviceinvoicelist_listSave.dcgst0 = ltaxrateamt/2 
    else:
        Tproformaserviceinvoicelist_listSave.digst0 = ltaxrateamt

    Tproformaserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tproformaserviceinvoicelist_listSave.dtotalfinal = dtotalfinal
    Tproformaserviceinvoicelist_listSave.swords= swords.upper()

 
    Tproformaserviceinvoicelist_listSave.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaServiceInvoiceListDetails', lID=lDetId)  

  
@csrf_exempt
def ProformaServiceInvoiceListPrintDetails(request,lID):
   
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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
 

    Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
    if(Tproformaserviceinvoicelist_list.ackno != ""):
        if(len(Tproformaserviceinvoicelist_list.ackno) > 11):
            my_code = EAN13(Tproformaserviceinvoicelist_list.ackno, writer=ImageWriter()) 
        else:
            my_code = EAN13("34145421212121156", writer=ImageWriter())
    else:
            my_code = EAN13("34121454212121156", writer=ImageWriter())

    my_code.save("new_code")
    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    iCountDetails =0
    iCountDetails = Tproformaserviceinvoicedetailslist_list.count
    context = {
            
        'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,   
            'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
            'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list, 
            'iCountDetails' : iCountDetails,
        } 
    
    
    pdf = render_to_pdf('BillingSol/ProformaServiceInvoiceListDetailsPrint.html', context)
    return HttpResponse(pdf, content_type='application/pdf') 
    

  
@csrf_exempt
def ProformaServiceInvoiceListCopyDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""


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
 

    Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tproformaserviceinvoicelist_list.customerid
    customername=Tproformaserviceinvoicelist_list.customername
    saddress1=Tproformaserviceinvoicelist_list.saddress1
    saddress2=Tproformaserviceinvoicelist_list.saddress2
    saddress3=Tproformaserviceinvoicelist_list.saddress3
    spin=Tproformaserviceinvoicelist_list.spin
    scity=Tproformaserviceinvoicelist_list.scity
    sstate=Tproformaserviceinvoicelist_list.sstate
    scustomerpan=Tproformaserviceinvoicelist_list.scustomerpan
    scustomergst=Tproformaserviceinvoicelist_list.scustomergst
    customernamesite=Tproformaserviceinvoicelist_list.customernamesite
    saddress1site=Tproformaserviceinvoicelist_list.saddress1site
    saddress2site=Tproformaserviceinvoicelist_list.saddress2site
    saddress3site=Tproformaserviceinvoicelist_list.saddress3site
    spinsite=Tproformaserviceinvoicelist_list.spinsite
    scitysite=Tproformaserviceinvoicelist_list.scitysite
    sstatesite=Tproformaserviceinvoicelist_list.sstatesite
    pono=Tproformaserviceinvoicelist_list.pono
    podate=Tproformaserviceinvoicelist_list.podate
    dtotal=Tproformaserviceinvoicelist_list.dtotal
    dgsttrate=Tproformaserviceinvoicelist_list.dgsttrate
    dgst=Tproformaserviceinvoicelist_list.dgst
    dtotalfinal=Tproformaserviceinvoicelist_list.dtotalfinal
    swords=Tproformaserviceinvoicelist_list.swords
    sgstsplit=Tproformaserviceinvoicelist_list.sgstsplit
    note1=Tproformaserviceinvoicelist_list.note1
    note2=Tproformaserviceinvoicelist_list.note2
    inr=Tproformaserviceinvoicelist_list.inr
    scategoryofservice=Tproformaserviceinvoicelist_list.scategoryofservice
    username=Tproformaserviceinvoicelist_list.username
    stype1=Tproformaserviceinvoicelist_list.stype1
    sfile1=Tproformaserviceinvoicelist_list.sfile1
    sfolder1=Tproformaserviceinvoicelist_list.sfolder1
    snumber1=Tproformaserviceinvoicelist_list.snumber1
    customersiteid=Tproformaserviceinvoicelist_list.customersiteid
    sstatecode=Tproformaserviceinvoicelist_list.sstatecode
    sfromdate=Tproformaserviceinvoicelist_list.sfromdate
    stodate=Tproformaserviceinvoicelist_list.stodate
    dsgst0=Tproformaserviceinvoicelist_list.dsgst0
    dcgst0=Tproformaserviceinvoicelist_list.dcgst0
    digst0=Tproformaserviceinvoicelist_list.digst0
    lnoofedit=Tproformaserviceinvoicelist_list.lnoofedit
    ddateofedit=Tproformaserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tproformaserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tproformaserviceinvoicelist_list.sdepartmentname
    bdelete=Tproformaserviceinvoicelist_list.bdelete
    bcancelcopy=Tproformaserviceinvoicelist_list.bcancelcopy
    bapproval0=Tproformaserviceinvoicelist_list.bapproval0
    bapproval01=Tproformaserviceinvoicelist_list.bapproval01
    bapproval02=Tproformaserviceinvoicelist_list.bapproval02
    bapproval03=Tproformaserviceinvoicelist_list.bapproval03
    bapproval04=Tproformaserviceinvoicelist_list.bapproval04
    bapproval05=Tproformaserviceinvoicelist_list.bapproval05
    bapproval06=Tproformaserviceinvoicelist_list.bapproval06
    bapproval07=Tproformaserviceinvoicelist_list.bapproval07
    bapproval08=Tproformaserviceinvoicelist_list.bapproval08
    bapproval09=Tproformaserviceinvoicelist_list.bapproval09
    bapproval010=Tproformaserviceinvoicelist_list.bapproval010
    scomments=Tproformaserviceinvoicelist_list.scomments
    scommentsdelete=Tproformaserviceinvoicelist_list.scommentsdelete
    lorderid=Tproformaserviceinvoicelist_list.lorderid
    saddressclient=Tproformaserviceinvoicelist_list.saddressclient
    saddresssite=Tproformaserviceinvoicelist_list.saddresssite
    scompanyaddress=Tproformaserviceinvoicelist_list.scompanyaddress
    llocationid=Tproformaserviceinvoicelist_list.llocationid
    slocation=Tproformaserviceinvoicelist_list.slocation
    slocationstatecode=Tproformaserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tproformaserviceinvoicelist_list.slocationgstno
    slocationpanno=Tproformaserviceinvoicelist_list.slocationpanno
    slocationformat=Tproformaserviceinvoicelist_list.slocationformat
    bsitesez=Tproformaserviceinvoicelist_list.bsitesez
    sworkfrom=Tproformaserviceinvoicelist_list.sworkfrom
    sworkfto=Tproformaserviceinvoicelist_list.sworkfto
    podate1=Tproformaserviceinvoicelist_list.podate1
    bsamestate =Tproformaserviceinvoicelist_list.bsamestate 




 
    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
    if McompanylistGet:
        slocation = McompanylistGet.scompanyname  
        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
            
        slocationgstno=McompanylistGet.sgstno 
        slocationpanno=McompanylistGet.spanno
        slocationstatecode=McompanylistGet.sstatecode

        salesbillno=McompanylistGet.linvoice10 + 1
        finyear=McompanylistGet.lyear
        if(McompanylistGet.lyear < 4):
            if(datetime.today().month >= 4):
                finyear=datetime.today().month
                salesbillno = 1

        ssalesbillno = ""
        ssalesbillno = str(salesbillno)
        if(len(ssalesbillno) == 1):
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat10 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice10 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tproformaserviceinvoicelist_AddNewOBJ = Tproformaserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Tproformaserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid
  

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformaserviceinvoicedetailslist_list:
        for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
            sdesc=Tproformaserviceinvoicedetailslist_listQ['sdesc']
            partid=Tproformaserviceinvoicedetailslist_listQ['partid']
            partno=Tproformaserviceinvoicedetailslist_listQ['partno']
            qty=Tproformaserviceinvoicedetailslist_listQ['qty']
            unitprice=Tproformaserviceinvoicedetailslist_listQ['unitprice']
            units=Tproformaserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tproformaserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tproformaserviceinvoicedetailslist_listQ['shsn']
            ssac=Tproformaserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tproformaserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tproformaserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tproformaserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaServiceInvoiceListDetails', lID=salesbillid)  


@csrf_exempt
def ProformaServiceInvoiceListCopyCreateInvoiceDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=""


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
 



    Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tproformaserviceinvoicelist_list.customerid
    customername=Tproformaserviceinvoicelist_list.customername
    saddress1=Tproformaserviceinvoicelist_list.saddress1
    saddress2=Tproformaserviceinvoicelist_list.saddress2
    saddress3=Tproformaserviceinvoicelist_list.saddress3
    spin=Tproformaserviceinvoicelist_list.spin
    scity=Tproformaserviceinvoicelist_list.scity
    sstate=Tproformaserviceinvoicelist_list.sstate
    scustomerpan=Tproformaserviceinvoicelist_list.scustomerpan
    scustomergst=Tproformaserviceinvoicelist_list.scustomergst
    customernamesite=Tproformaserviceinvoicelist_list.customernamesite
    saddress1site=Tproformaserviceinvoicelist_list.saddress1site
    saddress2site=Tproformaserviceinvoicelist_list.saddress2site
    saddress3site=Tproformaserviceinvoicelist_list.saddress3site
    spinsite=Tproformaserviceinvoicelist_list.spinsite
    scitysite=Tproformaserviceinvoicelist_list.scitysite
    sstatesite=Tproformaserviceinvoicelist_list.sstatesite
    pono=Tproformaserviceinvoicelist_list.pono
    podate=Tproformaserviceinvoicelist_list.podate
    dtotal=Tproformaserviceinvoicelist_list.dtotal
    dgsttrate=Tproformaserviceinvoicelist_list.dgsttrate
    dgst=Tproformaserviceinvoicelist_list.dgst
    dtotalfinal=Tproformaserviceinvoicelist_list.dtotalfinal
    swords=Tproformaserviceinvoicelist_list.swords
    sgstsplit=Tproformaserviceinvoicelist_list.sgstsplit
    note1=Tproformaserviceinvoicelist_list.note1
    note2=Tproformaserviceinvoicelist_list.note2
    inr=Tproformaserviceinvoicelist_list.inr
    scategoryofservice=Tproformaserviceinvoicelist_list.scategoryofservice
    username=Tproformaserviceinvoicelist_list.username
    stype1=Tproformaserviceinvoicelist_list.stype1
    sfile1=Tproformaserviceinvoicelist_list.sfile1
    sfolder1=Tproformaserviceinvoicelist_list.sfolder1
    snumber1=Tproformaserviceinvoicelist_list.snumber1
    customersiteid=Tproformaserviceinvoicelist_list.customersiteid
    sstatecode=Tproformaserviceinvoicelist_list.sstatecode
    sfromdate=Tproformaserviceinvoicelist_list.sfromdate
    stodate=Tproformaserviceinvoicelist_list.stodate
    dsgst0=Tproformaserviceinvoicelist_list.dsgst0
    dcgst0=Tproformaserviceinvoicelist_list.dcgst0
    digst0=Tproformaserviceinvoicelist_list.digst0
    lnoofedit=Tproformaserviceinvoicelist_list.lnoofedit
    ddateofedit=Tproformaserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tproformaserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tproformaserviceinvoicelist_list.sdepartmentname
    bdelete=Tproformaserviceinvoicelist_list.bdelete
    bcancelcopy=Tproformaserviceinvoicelist_list.bcancelcopy
    bapproval0=Tproformaserviceinvoicelist_list.bapproval0
    bapproval01=Tproformaserviceinvoicelist_list.bapproval01
    bapproval02=Tproformaserviceinvoicelist_list.bapproval02
    bapproval03=Tproformaserviceinvoicelist_list.bapproval03
    bapproval04=Tproformaserviceinvoicelist_list.bapproval04
    bapproval05=Tproformaserviceinvoicelist_list.bapproval05
    bapproval06=Tproformaserviceinvoicelist_list.bapproval06
    bapproval07=Tproformaserviceinvoicelist_list.bapproval07
    bapproval08=Tproformaserviceinvoicelist_list.bapproval08
    bapproval09=Tproformaserviceinvoicelist_list.bapproval09
    bapproval010=Tproformaserviceinvoicelist_list.bapproval010
    scomments=Tproformaserviceinvoicelist_list.scomments
    scommentsdelete=Tproformaserviceinvoicelist_list.scommentsdelete
    lorderid=Tproformaserviceinvoicelist_list.lorderid
    saddressclient=Tproformaserviceinvoicelist_list.saddressclient
    saddresssite=Tproformaserviceinvoicelist_list.saddresssite
    scompanyaddress=Tproformaserviceinvoicelist_list.scompanyaddress
    llocationid=Tproformaserviceinvoicelist_list.llocationid
    slocation=Tproformaserviceinvoicelist_list.slocation
    slocationstatecode=Tproformaserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tproformaserviceinvoicelist_list.slocationgstno
    slocationpanno=Tproformaserviceinvoicelist_list.slocationpanno
    slocationformat=Tproformaserviceinvoicelist_list.slocationformat
    bsitesez=Tproformaserviceinvoicelist_list.bsitesez
    sworkfrom=Tproformaserviceinvoicelist_list.sworkfrom
    sworkfto=Tproformaserviceinvoicelist_list.sworkfto
    podate1=Tproformaserviceinvoicelist_list.podate1
    bsamestate =Tproformaserviceinvoicelist_list.bsamestate 
    slutno=Tproformaserviceinvoicelist_list.slutno
    #breversechargemechanism=Tproformaserviceinvoicelist_list.breversechargemechanism




 
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
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat1 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice1 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tproformaserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate,  slutno=slutno, breversechargemechanism=breversechargemechanism)

    Tproformaserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid
  

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformaserviceinvoicedetailslist_list:
        for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
            sdesc=Tproformaserviceinvoicedetailslist_listQ['sdesc']
            partid=Tproformaserviceinvoicedetailslist_listQ['partid']
            partno=Tproformaserviceinvoicedetailslist_listQ['partno']
            qty=Tproformaserviceinvoicedetailslist_listQ['qty']
            unitprice=Tproformaserviceinvoicedetailslist_listQ['unitprice']
            units=Tproformaserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tproformaserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tproformaserviceinvoicedetailslist_listQ['shsn']
            ssac=Tproformaserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tproformaserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tproformaserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tproformaserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete()    
    return redirect('MaintenanceListDetails', lID=salesbillid)  


@csrf_exempt
def ProformaServiceInvoiceListCopyCreateInvoiceSEZDetails(request,lID):
    
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""
    slutno=""
    breversechargemechanism=""


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
 



    Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tproformaserviceinvoicelist_list.customerid
    customername=Tproformaserviceinvoicelist_list.customername
    saddress1=Tproformaserviceinvoicelist_list.saddress1
    saddress2=Tproformaserviceinvoicelist_list.saddress2
    saddress3=Tproformaserviceinvoicelist_list.saddress3
    spin=Tproformaserviceinvoicelist_list.spin
    scity=Tproformaserviceinvoicelist_list.scity
    sstate=Tproformaserviceinvoicelist_list.sstate
    scustomerpan=Tproformaserviceinvoicelist_list.scustomerpan
    scustomergst=Tproformaserviceinvoicelist_list.scustomergst
    customernamesite=Tproformaserviceinvoicelist_list.customernamesite
    saddress1site=Tproformaserviceinvoicelist_list.saddress1site
    saddress2site=Tproformaserviceinvoicelist_list.saddress2site
    saddress3site=Tproformaserviceinvoicelist_list.saddress3site
    spinsite=Tproformaserviceinvoicelist_list.spinsite
    scitysite=Tproformaserviceinvoicelist_list.scitysite
    sstatesite=Tproformaserviceinvoicelist_list.sstatesite
    pono=Tproformaserviceinvoicelist_list.pono
    podate=Tproformaserviceinvoicelist_list.podate
    dtotal=Tproformaserviceinvoicelist_list.dtotal
    dgsttrate=Tproformaserviceinvoicelist_list.dgsttrate
    dgst=Tproformaserviceinvoicelist_list.dgst
    dtotalfinal=Tproformaserviceinvoicelist_list.dtotalfinal
    swords=Tproformaserviceinvoicelist_list.swords
    sgstsplit=Tproformaserviceinvoicelist_list.sgstsplit
    note1=Tproformaserviceinvoicelist_list.note1
    note2=Tproformaserviceinvoicelist_list.note2
    inr=Tproformaserviceinvoicelist_list.inr
    scategoryofservice=Tproformaserviceinvoicelist_list.scategoryofservice
    username=Tproformaserviceinvoicelist_list.username
    stype1=Tproformaserviceinvoicelist_list.stype1
    sfile1=Tproformaserviceinvoicelist_list.sfile1
    sfolder1=Tproformaserviceinvoicelist_list.sfolder1
    snumber1=Tproformaserviceinvoicelist_list.snumber1
    customersiteid=Tproformaserviceinvoicelist_list.customersiteid
    sstatecode=Tproformaserviceinvoicelist_list.sstatecode
    sfromdate=Tproformaserviceinvoicelist_list.sfromdate
    stodate=Tproformaserviceinvoicelist_list.stodate
    dsgst0=Tproformaserviceinvoicelist_list.dsgst0
    dcgst0=Tproformaserviceinvoicelist_list.dcgst0
    digst0=Tproformaserviceinvoicelist_list.digst0
    lnoofedit=Tproformaserviceinvoicelist_list.lnoofedit
    ddateofedit=Tproformaserviceinvoicelist_list.ddateofedit
    ldepartmentid=Tproformaserviceinvoicelist_list.ldepartmentid
    sdepartmentname=Tproformaserviceinvoicelist_list.sdepartmentname
    bdelete=Tproformaserviceinvoicelist_list.bdelete
    bcancelcopy=Tproformaserviceinvoicelist_list.bcancelcopy
    bapproval0=Tproformaserviceinvoicelist_list.bapproval0
    bapproval01=Tproformaserviceinvoicelist_list.bapproval01
    bapproval02=Tproformaserviceinvoicelist_list.bapproval02
    bapproval03=Tproformaserviceinvoicelist_list.bapproval03
    bapproval04=Tproformaserviceinvoicelist_list.bapproval04
    bapproval05=Tproformaserviceinvoicelist_list.bapproval05
    bapproval06=Tproformaserviceinvoicelist_list.bapproval06
    bapproval07=Tproformaserviceinvoicelist_list.bapproval07
    bapproval08=Tproformaserviceinvoicelist_list.bapproval08
    bapproval09=Tproformaserviceinvoicelist_list.bapproval09
    bapproval010=Tproformaserviceinvoicelist_list.bapproval010
    scomments=Tproformaserviceinvoicelist_list.scomments
    scommentsdelete=Tproformaserviceinvoicelist_list.scommentsdelete
    lorderid=Tproformaserviceinvoicelist_list.lorderid
    saddressclient=Tproformaserviceinvoicelist_list.saddressclient
    saddresssite=Tproformaserviceinvoicelist_list.saddresssite
    scompanyaddress=Tproformaserviceinvoicelist_list.scompanyaddress
    llocationid=Tproformaserviceinvoicelist_list.llocationid
    slocation=Tproformaserviceinvoicelist_list.slocation
    slocationstatecode=Tproformaserviceinvoicelist_list.slocationstatecode
    slocationgstno=Tproformaserviceinvoicelist_list.slocationgstno
    slocationpanno=Tproformaserviceinvoicelist_list.slocationpanno
    slocationformat=Tproformaserviceinvoicelist_list.slocationformat
    bsitesez=Tproformaserviceinvoicelist_list.bsitesez
    sworkfrom=Tproformaserviceinvoicelist_list.sworkfrom
    sworkfto=Tproformaserviceinvoicelist_list.sworkfto
    podate1=Tproformaserviceinvoicelist_list.podate1
    bsamestate =Tproformaserviceinvoicelist_list.bsamestate 
    slutno=Tproformaserviceinvoicelist_list.slutno
    #breversechargemechanism=Tproformaserviceinvoicelist_list.breversechargemechanism




 
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
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat1 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice1 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Tproformaserviceinvoicelist_AddNewOBJ = Tserviceinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate,  slutno=slutno, breversechargemechanism=breversechargemechanism)

    Tproformaserviceinvoicelist_AddNewOBJ.save()
    salesbillid = Tproformaserviceinvoicelist_AddNewOBJ.salesbillid
  

    Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformaserviceinvoicedetailslist_list:
        for Tproformaserviceinvoicedetailslist_listQ in Tproformaserviceinvoicedetailslist_list:
            sdesc=Tproformaserviceinvoicedetailslist_listQ['sdesc']
            partid=Tproformaserviceinvoicedetailslist_listQ['partid']
            partno=Tproformaserviceinvoicedetailslist_listQ['partno']
            qty=Tproformaserviceinvoicedetailslist_listQ['qty']
            unitprice=Tproformaserviceinvoicedetailslist_listQ['unitprice']
            units=Tproformaserviceinvoicedetailslist_listQ['units']
            ddescitemtotal=Tproformaserviceinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tproformaserviceinvoicedetailslist_listQ['shsn']
            ssac=Tproformaserviceinvoicedetailslist_listQ['ssac']
            smanrate=Tproformaserviceinvoicedetailslist_listQ['smanrate']
            staxnotify=Tproformaserviceinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Tproformaserviceinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Tproformaserviceinvoicedetailslist_listQ['ltaxrateamt2']

            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete()    
    return redirect('MaintenanceListSEZDetails', lID=salesbillid)  





@csrf_exempt
def ProformaServiceInvoiceListDetails(request,lID):
    
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
    podate=""#datetime.today().strftime('%d-%m-%Y')
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
    sworkfrom="" #datetime.today().strftime('%Y-%m-%d')
    sworkfto=""#datetime.today().strftime('%Y-%m-%d')
    ackdate=""#datetime.today().strftime('%d-%m-%Y')
    ackdate1=""#datetime.today().strftime('%Y-%m-%d')
    podate1=""#datetime.today().strftime('%Y-%m-%d')
    bsamestate =0
    sfile11=""
    sfolder11=""
    sfile12=""
    sfolder12=""
    sfile13=""
    sfolder13=""
    sfile14=""
    sfolder14=""
    sfile15=""
    sfolder15=""

    
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

            
            return   redirect('ProformaServiceInvoiceList')  
        
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
                        spinsite =McustomerlistGet.slocation
                        
                        
                        TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

                        TproformaserviceinvoicelistSave_list.customerid = customerid
                        TproformaserviceinvoicelistSave_list.customername = customername
                        TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
                        TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
                        TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
                        TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
                        TproformaserviceinvoicelistSave_list.spinsite = spinsite
                        TproformaserviceinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
                Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 
        
        if 'cmdGetSite' in request.POST:  

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        #sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 

                        TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
                        TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
                        TproformaserviceinvoicelistSave_list.saddresssite = saddresssite 

                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        TproformaserviceinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformaserviceinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                            'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 


            bsitesez =0
            if 'bsitesez' in request.POST: 
                bsitesez = 1


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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                            
                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

                ackdate1A =""
                ewaydate1A =""
                sdate1A =""
                podate1A =""
                sworkfromA =""
                sworkftoA =""

                ackdate1=data.get('txtAckDate') 
                #ackdate1A = ackdate1.split("-")
                ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

                ewaydate1=data.get('txteWayDate')
                #ewaydate1A = ewaydate1.split("-")
                ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

                sdate1=data.get('txtInvoiceDate') 
                sdate1A = sdate1.split("-")
                sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
                invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

                podate1=data.get('txtPOeDate') 
                podate1A =podate1 # podate1.split("-")
                podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

                sworkfrom="" #data.get('txtFrom') 
                sfromdate=data.get('txtFrom') 
                # sworkfromA = sworkfrom.split("-")
                # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                stodate=data.get('txtTo') 
                # sworkftoA = sworkfto.split("-")
                # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                sworkfrom="" #data.get('txtFrom') 
                sworkfromA = sworkfrom# sworkfrom.split("-")
                sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

                sworkfto=data.get('txtTo') 
                sworkftoA =sworkfto# sworkfto.split("-")
                stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                        
                inrno=data.get('txtIRNNo') 
                ackno=data.get('txtAckNo') 
                ewayno=data.get('txteWayNo')  
                scategoryofservice=data.get('txtCategory') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  


                TproformaserviceinvoicelistSave_list.bsitesez = bsitesez

                breversechargemechanism =0
                if 'breversechargemechanism' in request.POST: 
                    breversechargemechanism=1

                TproformaserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
                


                TproformaserviceinvoicelistSave_list.ackdate1 = ackdate1
                TproformaserviceinvoicelistSave_list.ackdate = ackdate
                TproformaserviceinvoicelistSave_list.ewaydate1 = ewaydate1
                TproformaserviceinvoicelistSave_list.ewaydate = ewaydate
                TproformaserviceinvoicelistSave_list.sdate1 = sdate1
                TproformaserviceinvoicelistSave_list.sdate = sdate
                TproformaserviceinvoicelistSave_list.podate1 = podate1
                TproformaserviceinvoicelistSave_list.podate = podate
                TproformaserviceinvoicelistSave_list.sworkfrom = sworkfrom
                TproformaserviceinvoicelistSave_list.sfromdate = sfromdate
                TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
                TproformaserviceinvoicelistSave_list.stodate = stodate
                TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
                TproformaserviceinvoicelistSave_list.inrno = inrno
                TproformaserviceinvoicelistSave_list.ackno = ackno
                TproformaserviceinvoicelistSave_list.ewayno = ewayno
                TproformaserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
                TproformaserviceinvoicelistSave_list.stype1 = stype1
                TproformaserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TproformaserviceinvoicelistSave_list.pono = pono
                TproformaserviceinvoicelistSave_list.note1 = note1 

                TproformaserviceinvoicelistSave_list.customerid = customerid
                TproformaserviceinvoicelistSave_list.customername = customername
                TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
                TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
                TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
                TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
                TproformaserviceinvoicelistSave_list.spinsite = spinsite
                
                TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
                TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
                TproformaserviceinvoicelistSave_list.saddresssite = saddresssite  

                TproformaserviceinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
                Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            if(Tproformaserviceinvoicelist_list.ackno != ""):
                if(len(Tproformaserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tproformaserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            iCountDetails =0
            iCountDetails = Tproformaserviceinvoicedetailslist_list.count
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                    'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list, 
                    'iCountDetails' : iCountDetails,
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProformaServiceInvoiceListDetailsPrint.html', context)
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

            TproformaserviceinvoicelistSave_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 


            bsitesez =0
            if 'bsitesez' in request.POST: 
                bsitesez = 1


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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

            ackdate1A =""
            ewaydate1A =""
            sdate1A =""
            podate1A =""
            sworkfromA =""
            sworkftoA =""

            ackdate1=data.get('txtAckDate') 
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
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
            if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                ltaxrateamt1 =ltaxrateamt/2
                ltaxrateamt1 =ltaxrateamt/2

            dtotal = round(ddescitemtotal + ltaxrateamt)


            
            Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Tproformaserviceinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Added successfully!')


            Tproformaserviceinvoicedetailslist_listG = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            ltaxrateamt =0
            digst0 = 0
            dsgst0 = 0
            dcgst0 = 0
            dgsttrate = 0
            dtotalfinal = 0
            dtotal=0

                        

            if Tproformaserviceinvoicedetailslist_listG:
                for Tproformaserviceinvoicedetailslist_listGT in Tproformaserviceinvoicedetailslist_listG:
                    dtotal =dtotal + float(Tproformaserviceinvoicedetailslist_listGT['ddescitemtotal'])
                    ltaxrateamt =ltaxrateamt + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    digst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    dsgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt1'])
                    dcgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
                    dtotalfinal =dtotalfinal + float(Tproformaserviceinvoicedetailslist_listGT['dtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TproformaserviceinvoicelistSave_list.dtotal = dtotal
            TproformaserviceinvoicelistSave_list.dgsttrate = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dsgst0 = 0
            TproformaserviceinvoicelistSave_list.dcgst0 = 0 
            TproformaserviceinvoicelistSave_list.digst0 = 0 


            if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                TproformaserviceinvoicelistSave_list.dsgst0 = ltaxrateamt/2
                TproformaserviceinvoicelistSave_list.dcgst0 = ltaxrateamt/2
            else:
                TproformaserviceinvoicelistSave_list.digst0 = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.swords = swords.upper()  

            TproformaserviceinvoicelistSave_list.bsitesez = bsitesez

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TproformaserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            

            TproformaserviceinvoicelistSave_list.ackdate1 = ackdate1
            TproformaserviceinvoicelistSave_list.ackdate = ackdate
            TproformaserviceinvoicelistSave_list.ewaydate1 = ewaydate1
            TproformaserviceinvoicelistSave_list.ewaydate = ewaydate
            TproformaserviceinvoicelistSave_list.sdate1 = sdate1
            TproformaserviceinvoicelistSave_list.sdate = sdate
            TproformaserviceinvoicelistSave_list.podate1 = podate1
            TproformaserviceinvoicelistSave_list.podate = podate
            TproformaserviceinvoicelistSave_list.sworkfrom = sworkfrom
            TproformaserviceinvoicelistSave_list.sfromdate = sfromdate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.stodate = stodate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.inrno = inrno
            TproformaserviceinvoicelistSave_list.ackno = ackno
            TproformaserviceinvoicelistSave_list.ewayno = ewayno
            TproformaserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
            TproformaserviceinvoicelistSave_list.stype1 = stype1
            TproformaserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
            TproformaserviceinvoicelistSave_list.pono = pono
            TproformaserviceinvoicelistSave_list.note1 = note1 

            TproformaserviceinvoicelistSave_list.customerid = customerid
            TproformaserviceinvoicelistSave_list.customername = customername
            TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
            TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
            TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
            TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
            TproformaserviceinvoicelistSave_list.spinsite = spinsite
            
            TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
            TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
            TproformaserviceinvoicelistSave_list.saddresssite = saddresssite 
            TproformaserviceinvoicelistSave_list.swords= swords.upper()
            TproformaserviceinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 


        if 'cmdItemSave1' in request.POST:  

            TproformaserviceinvoicelistSave_list =  Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
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
                        spinsite =McustomerlistGet.slocation
                        if (McustomerlistGet.sstatecode != ""):
                            sstatecode=McustomerlistGet.sstatecode 
                         

            customersiteid =0
            if 'cmbSite' in request.POST: 
                if(data.get('cmbSite').isnumeric()):
                    customersiteid = int(data.get('cmbSite'))
                    MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
                    if MsitelistGet:
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace # MsitelistGet.splace  # MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
                        TproformaserviceinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformaserviceinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformaserviceinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                    

            ackdate1A =""
            ewaydate1A =""
            sdate1A =""
            podate1A =""
            sworkfromA =""
            sworkftoA =""

            ackdate1=data.get('txtAckDate') 
            #ackdate1A = ackdate1.split("-")
            ackdate = ackdate1 #ackdate1A[2] + "-" + ackdate1A[1] + "-" + ackdate1A[0] 

            ewaydate1=data.get('txteWayDate')
            #ewaydate1A = ewaydate1.split("-")
            ewaydate =ewaydate1 #ewaydate1A[2] + "-" + ewaydate1A[1] + "-" + ewaydate1A[0] 

            sdate1=data.get('txtInvoiceDate') 
            sdate1A = sdate1.split("-")
            sdate =sdate1A[2] + "-" + sdate1A[1] + "-" + sdate1A[0] 
            invoicedate=datetime.strptime(sdate, '%d-%m-%Y').date()

            podate1=data.get('txtPOeDate') 
            podate1A =podate1 # podate1.split("-")
            podate =podate1 #podate1A[2] + "-" + podate1A[1] + "-" + podate1A[0] 

            sworkfrom="" #data.get('txtFrom') 
            sfromdate=data.get('txtFrom') 
            # sworkfromA = sworkfrom.split("-")
            # sfromdate =sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            stodate=data.get('txtTo') 
            # sworkftoA = sworkfto.split("-")
            # stodate =sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

            sworkfrom="" #data.get('txtFrom') 
            sworkfromA = sworkfrom# sworkfrom.split("-")
            sfromdate =sworkfrom#sworkfromA[2] + "-" + sworkfromA[1] + "-" + sworkfromA[0] 

            sworkfto=data.get('txtTo') 
            sworkftoA =sworkfto# sworkfto.split("-")
            stodate =sworkfto#sworkftoA[2] + "-" + sworkftoA[1] + "-" + sworkftoA[0] 

                    
            inrno=data.get('txtIRNNo') 
            ackno=data.get('txtAckNo') 
            ewayno=data.get('txteWayNo')  
            scategoryofservice=data.get('txtCategory') 
            stype1=data.get('txtDocType') 
            sinvoicerefno=data.get('txtInvNo') 
            pono=data.get('txtPONo') 
            note1=data.get('txtDescription')  

            icountLoop =0
            icountLoopAll =0
            Tproformaserviceinvoicedetailslist_listGetLoop = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tproformaserviceinvoicedetailslist_listGetLoop.count()

            for Tproformaserviceinvoicedetailslist_listGetLoopA in Tproformaserviceinvoicedetailslist_listGetLoop:
                
                icountLoop=Tproformaserviceinvoicedetailslist_listGetLoopA['salesordermultiid']
                salesordermultiid=data.get('txtItemID' + str(icountLoop))  
                sdesc=data.get('txtItemDesc1' + str(icountLoop))  
                qty=data.get('txtQuantity1' + str(icountLoop))  
                unitprice=data.get('txtRate1' + str(icountLoop))
                units=data.get('txtUnits1' + str(icountLoop))
                ddescitemtotal=data.get('txtItemAmt1' + str(icountLoop))
                shsn=data.get('txtHSNCode1' + str(icountLoop))
                dtotal=data.get('txtItemTotalAmt1' + str(icountLoop))
                ltaxrate=data.get('txtGSTRate1' + str(icountLoop))  
                ltaxrateamt=data.get('txtGSTAmt1' + str(icountLoop))  
                staxnotify=data.get('txtPOAMt1' + str(icountLoop))  
                ltaxrateamt1=0 
                ltaxrateamt2=0   


                ddescitemtotal =float(unitprice) * float(qty)
                ltaxrateamt =ddescitemtotal * float(ltaxrate)/100
                if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                    ltaxrateamt1 =ltaxrateamt/2
                    ltaxrateamt1 =ltaxrateamt/2

                dtotal = round(ddescitemtotal + ltaxrateamt)


                Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tproformaserviceinvoicedetailslist_AddNewOBJ.sdesc = sdesc
                Tproformaserviceinvoicedetailslist_AddNewOBJ.unitprice = unitprice
                Tproformaserviceinvoicedetailslist_AddNewOBJ.units = units
                Tproformaserviceinvoicedetailslist_AddNewOBJ.qty = qty
                Tproformaserviceinvoicedetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tproformaserviceinvoicedetailslist_AddNewOBJ.shsn = shsn
                Tproformaserviceinvoicedetailslist_AddNewOBJ.dtotal = dtotal
                Tproformaserviceinvoicedetailslist_AddNewOBJ.ltaxrate = ltaxrate
                Tproformaserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt = ltaxrateamt
                Tproformaserviceinvoicedetailslist_AddNewOBJ.staxnotify = staxnotify
                Tproformaserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt1 = ltaxrateamt1
                Tproformaserviceinvoicedetailslist_AddNewOBJ.ltaxrateamt2 = ltaxrateamt2

                #Tproformaserviceinvoicedetailslist_AddNewOBJ = Tproformaserviceinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 
                # 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	
                # shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	
                # ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

                Tproformaserviceinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Edited successfully!')


            Tproformaserviceinvoicedetailslist_listG = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            ltaxrateamt =0
            digst0 = 0
            dsgst0 = 0
            dcgst0 = 0
            dgsttrate = 0
            dtotalfinal = 0
            dtotal=0

                        

            if Tproformaserviceinvoicedetailslist_listG:
                for Tproformaserviceinvoicedetailslist_listGT in Tproformaserviceinvoicedetailslist_listG:
                    dtotal =dtotal + float(Tproformaserviceinvoicedetailslist_listGT['ddescitemtotal'])
                    ltaxrateamt =ltaxrateamt + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    digst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt'])
                    dsgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt1'])
                    dcgst0 =dgsttrate + float(Tproformaserviceinvoicedetailslist_listGT['ltaxrateamt2']) 
                    dtotalfinal =dtotalfinal + float(Tproformaserviceinvoicedetailslist_listGT['dtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TproformaserviceinvoicelistSave_list.dtotal = dtotal
            TproformaserviceinvoicelistSave_list.dgsttrate = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dsgst0 = 0
            TproformaserviceinvoicelistSave_list.dcgst0 = 0 
            TproformaserviceinvoicelistSave_list.digst0 = 0 


            if(TproformaserviceinvoicelistSave_list.sstatecode == TproformaserviceinvoicelistSave_list.slocationstatecode):
                TproformaserviceinvoicelistSave_list.dsgst0 = ltaxrateamt/2
                TproformaserviceinvoicelistSave_list.dcgst0 = ltaxrateamt/2
            else:
                TproformaserviceinvoicelistSave_list.digst0 = ltaxrateamt

            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.dtotalfinal = dtotalfinal
            TproformaserviceinvoicelistSave_list.swords = swords.upper()  

            breversechargemechanism =0
            if 'breversechargemechanism' in request.POST: 
                breversechargemechanism=1

            TproformaserviceinvoicelistSave_list.breversechargemechanism = breversechargemechanism
            
            TproformaserviceinvoicelistSave_list.ackdate1 = ackdate1
            TproformaserviceinvoicelistSave_list.ackdate = ackdate
            TproformaserviceinvoicelistSave_list.ewaydate1 = ewaydate1
            TproformaserviceinvoicelistSave_list.ewaydate = ewaydate
            TproformaserviceinvoicelistSave_list.sdate1 = sdate1
            TproformaserviceinvoicelistSave_list.sdate = sdate
            TproformaserviceinvoicelistSave_list.podate1 = podate1
            TproformaserviceinvoicelistSave_list.podate = podate
            TproformaserviceinvoicelistSave_list.sworkfrom = sworkfrom
            TproformaserviceinvoicelistSave_list.sfromdate = sfromdate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.stodate = stodate
            TproformaserviceinvoicelistSave_list.sworkfto = sworkfto
            TproformaserviceinvoicelistSave_list.inrno = inrno
            TproformaserviceinvoicelistSave_list.ackno = ackno
            TproformaserviceinvoicelistSave_list.ewayno = ewayno
            TproformaserviceinvoicelistSave_list.scategoryofservice = scategoryofservice
            TproformaserviceinvoicelistSave_list.stype1 = stype1
            TproformaserviceinvoicelistSave_list.sinvoicerefno = sinvoicerefno
            TproformaserviceinvoicelistSave_list.pono = pono
            TproformaserviceinvoicelistSave_list.note1 = note1 

            TproformaserviceinvoicelistSave_list.customerid = customerid
            TproformaserviceinvoicelistSave_list.customername = customername
            TproformaserviceinvoicelistSave_list.saddressclient = saddressclient
            TproformaserviceinvoicelistSave_list.scustomerpan = scustomerpan
            TproformaserviceinvoicelistSave_list.scustomergst = scustomergst
            TproformaserviceinvoicelistSave_list.sstatecode = sstatecode
            TproformaserviceinvoicelistSave_list.spinsite = spinsite
            
            TproformaserviceinvoicelistSave_list.customersiteid = customersiteid
            TproformaserviceinvoicelistSave_list.customernamesite = customernamesite
            TproformaserviceinvoicelistSave_list.saddresssite = saddresssite 
            TproformaserviceinvoicelistSave_list.swords= swords.upper()
            TproformaserviceinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
            Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                                'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tproformaserviceinvoicelist_list = Tproformaserviceinvoicelist.objects.get(salesbillid=lID) 
        Tproformaserviceinvoicedetailslist_list = Tproformaserviceinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformaserviceinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/ProformaServiceInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformaserviceinvoicelist_list' : Tproformaserviceinvoicelist_list,
                            'Tproformaserviceinvoicedetailslist_list' : Tproformaserviceinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 
    


    

    
