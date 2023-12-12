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
def DCList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('DCListAdd')  
        
    else:
        
        Tdclist_list = Tdclist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tdclist_list.count()
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
        paginator = Paginator(Tdclist_list, lRecCount1)
        try:
            Tdclist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tdclist_lists = paginator.page(1)
        except EmptyPage:
            Tdclist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/DCList.html",
                    {
                        'Tdclist_list':Tdclist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def DCListAdd(request):

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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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

            return   redirect('DCList') 

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

                        salesbillno=McompanylistGet.linvoice3 + 1
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
                        sinvoicerefno=McompanylistGet.sformat3 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice3 = salesbillno
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
            
            
            Tdclist_AddNewOBJ = Tdclist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15)
 
            Tdclist_AddNewOBJ.save()
            salesbillid = Tdclist_AddNewOBJ.salesbillid
   
            return   redirect('DCListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/DCListAdd.html",
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
def DCListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tdcdetailslist_list = Tdcdetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tdcdetailslist_list.salesbillid
    
    # if Tdcdetailslist_list:
    #     for Tdcdetailslist_listQ in Tdcdetailslist_list:
    #         lDetId = Tdcdetailslist_listQ['salesbillid']

    Tdclist_listOBJ =  Tdcdetailslist.objects.get(salesordermultiid=lID).delete()
          


    TdclistSave_list = Tdclist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tdcdetailslist_listG = Tdcdetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0 


                

    if Tdcdetailslist_listG:
        for Tdcdetailslist_listGT in Tdcdetailslist_listG:
            dtotal =dtotal + float(Tdcdetailslist_listGT['qty'] * Tdcdetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tdcdetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tdcdetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tdcdetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tdcdetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tdcdetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tdcdetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tdcdetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tdcdetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tdcdetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tdcdetailslist_listGT['dcgst1pt0'])
            
            dtotalfinal =dtotalfinal + float(Tdcdetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TdclistSave_list.dtotal = dtotal
    TdclistSave_list.dgsttrate = dcgst1pt0

    TdclistSave_list.dsgst0 = 0
    TdclistSave_list.dcgst0 = 0 
    TdclistSave_list.digst0 = 0 




    TdclistSave_list.dcgst01 = 0 
    TdclistSave_list.dcgst5 = 0 
    TdclistSave_list.dcgst12 = 0 
    TdclistSave_list.dcgst18 = 0 
    TdclistSave_list.dcgst28 = 0 

    TdclistSave_list.dcgst01 = 0 
    TdclistSave_list.dsgst5 = 0 
    TdclistSave_list.dsgst12 = 0 
    TdclistSave_list.dsgst18 = 0 
    TdclistSave_list.dsgst28 = 0 
 

    TdclistSave_list.dsgst01 = dsgst01 
    TdclistSave_list.dsgst5 = dsgst5 
    TdclistSave_list.dsgst12 = dsgst12 
    TdclistSave_list.dsgst18 = dsgst18 
    TdclistSave_list.dsgst28 = dsgst28  

    TdclistSave_list.dcgst01 =dcgst01 
    TdclistSave_list.dcgst5 = dcgst5 
    TdclistSave_list.dcgst12 =dcgst12
    TdclistSave_list.dcgst18 = dcgst18 
    TdclistSave_list.dcgst28 = dcgst28

    TdclistSave_list.dtotalfinal = dtotalfinal
    TdclistSave_list.dtotalfinal = dtotalfinal
    TdclistSave_list.swords = swords.upper()  


    TdclistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('DCListDetails', lID=lDetId)  


@csrf_exempt
def DCListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
                        
                        
                        TdclistSave_list = Tdclist.objects.get(salesbillid=lID) 

                        TdclistSave_list.customerid = customerid
                        TdclistSave_list.customername = customername
                        TdclistSave_list.saddressclient = saddressclient
                        TdclistSave_list.scustomerpan = scustomerpan
                        TdclistSave_list.scustomergst = scustomergst
                        TdclistSave_list.sstatecode = sstatecode
                        TdclistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdclist_list = Tdclist.objects.get(salesbillid=lID) 
                Tdcdetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DCListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tdclist_list' : Tdclist_list,
                                    'Tdcdetailslist_list' : Tdcdetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TdclistSave_list = Tdclist.objects.get(salesbillid=lID) 

                        TdclistSave_list.customersiteid = customersiteid
                        TdclistSave_list.customernamesite = customernamesite
                        TdclistSave_list.saddresssite = saddresssite 
                        

                        TdclistSave_list.spinsite = MsitelistGet.sstatecode
                        TdclistSave_list.sstatesite = MsitelistGet.stempname1
                        TdclistSave_list.scitysite = MsitelistGet.stempname2



                        TdclistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tdclist_list = Tdclist.objects.get(salesbillid=lID) 
            Tdcdetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tdclist_list.customerid).values() 
            
            return render(request, "BillingSol/DCListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tdclist_list' : Tdclist_list,
                            'Tdcdetailslist_list' : Tdcdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TdclistSave_list = Tdclist.objects.get(salesbillid=lID) 

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
                           
                        TdclistSave_list.spinsite = MsitelistGet.sstatecode
                        TdclistSave_list.sstatesite = MsitelistGet.stempname1
                        TdclistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

                sdate1=data.get('txTdcDate') 
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
                scategoryofservice=data.get('txtReturnableNon') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  
                saddress3=data.get('txtFreight') 


                TdclistSave_list.ackdate1 = ackdate1
                TdclistSave_list.ackdate = ackdate
                TdclistSave_list.ewaydate1 = ewaydate1
                TdclistSave_list.ewaydate = ewaydate
                TdclistSave_list.sdate1 = sdate1
                TdclistSave_list.sdate = sdate
                TdclistSave_list.podate1 = podate1
                TdclistSave_list.podate = podate
                TdclistSave_list.sworkfrom = sworkfrom
                TdclistSave_list.sfromdate = sfromdate
                TdclistSave_list.sworkfto = sworkfto
                TdclistSave_list.stodate = stodate
                TdclistSave_list.sworkfto = sworkfto
                TdclistSave_list.inrno = inrno
                TdclistSave_list.ackno = ackno
                TdclistSave_list.ewayno = ewayno
                TdclistSave_list.scategoryofservice = scategoryofservice
                TdclistSave_list.stype1 = stype1
                TdclistSave_list.sinvoicerefno = sinvoicerefno
                TdclistSave_list.pono = pono
                TdclistSave_list.note1 = note1 

                TdclistSave_list.customerid = customerid
                TdclistSave_list.customername = customername
                TdclistSave_list.saddressclient = saddressclient
                TdclistSave_list.scustomerpan = scustomerpan
                TdclistSave_list.scustomergst = scustomergst
                TdclistSave_list.sstatecode = sstatecode
                
                TdclistSave_list.customersiteid = customersiteid
                TdclistSave_list.customernamesite = customernamesite
                TdclistSave_list.saddresssite = saddresssite 

 
                TdclistSave_list.saddress3 = saddress3 

                TdclistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdclist_list = Tdclist.objects.get(salesbillid=lID) 
                Tdcdetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DCListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tdclist_list' : Tdclist_list,
                                    'Tdcdetailslist_list' : Tdcdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tdclist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/DCListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tdcdetailslist_listG = Tdcdetailslist.objects.filter(salesbillid=lID).values() 

            TdclistSave_list = Tdclist.objects.get(salesbillid=lID) 

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
                           
                        TdclistSave_list.spinsite = MsitelistGet.sstatecode
                        TdclistSave_list.sstatesite = MsitelistGet.stempname1
                        TdclistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

                sdate1=data.get('txTdcDate') 
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
                scategoryofservice=data.get('txtReturnableNon') 
                stype1=data.get('txtDocType') 
                sinvoicerefno=data.get('txtInvNo') 
                pono=data.get('txtPONo') 
                note1=data.get('txtDescription')  
                saddress3=data.get('txtFreight') 


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



                # dcgst1pt00 =0 #float(unitprice) * float(qty)
                # ltaxrate=0  #f0'loat(ltaxrate)
                # dsgst01=ltaxrate
                # ltaxrateamt = 0 #dcgst1pt00 * ltaxrate/100
                # dcgst1pt0 = ltaxrateamt
                # if(ltaxrate == 0):
                #     dcgst01 =0
                # elif(ltaxrate == 5):
                #     dcgst5 =ltaxrateamt 
                #     if(TdclistSave_list.sstatecode == TdclistSave_list.slocationstatecode):
                #         dsgst5 = dcgst5/2
                #     else:
                #        dcgst50  =ltaxrateamt
                # elif(ltaxrate == 12):
                #     dcgst12 =ltaxrateamt 
                #     if(TdclistSave_list.sstatecode == TdclistSave_list.slocationstatecode):
                #         dsgst12 = dcgst12/2
                #     else:
                #        dcgst120  =ltaxrateamt
                # elif(ltaxrate == 18):
                #     dcgst18 =ltaxrateamt 
                #     if(TdclistSave_list.sstatecode == TdclistSave_list.slocationstatecode):
                #         dsgst18 = dcgst18/2
                #     else:
                #        dcgst180  =ltaxrateamt
                # elif(ltaxrate == 28):
                #     dcgst28 =ltaxrateamt 
                #     if(TdclistSave_list.sstatecode == TdclistSave_list.slocationstatecode):
                #         dsgst28 = dcgst28/2
                #     else:
                #        dcgst280  =ltaxrateamt


                    

                # ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



                
                Tdcdetailslist_AddNewOBJ = Tdcdetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)
    
                Tdcdetailslist_AddNewOBJ.save()

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
                dcgst1pt0=0

                

                            

                # if Tdcdetailslist_listG:
                #     for Tdcdetailslist_listGT in Tdcdetailslist_listG:
                #         dtotal =0

                #         dcgst01 =dcgst01 + float(Tdcdetailslist_listGT['dcgst01'])
                #         dcgst5 =dcgst5 + float(Tdcdetailslist_listGT['dcgst5'])
                #         dsgst5 =dsgst5 + float(Tdcdetailslist_listGT['dsgst5'])
                #         dcgst12 =dcgst12 + float(Tdcdetailslist_listGT['dcgst12'])
                #         dsgst12 =dsgst12 + float(Tdcdetailslist_listGT['dsgst12'])
                #         dcgst18 =dcgst18 + float(Tdcdetailslist_listGT['dcgst18'])
                #         dsgst18 =dsgst18 + float(Tdcdetailslist_listGT['dsgst18'])
                #         dcgst28 =dcgst28 + float(Tdcdetailslist_listGT['dcgst28'])
                #         dsgst28 =dsgst28 + float(Tdcdetailslist_listGT['dsgst28'])
                #         dcgst1pt0=dcgst1pt0 + float(Tdcdetailslist_listGT['dcgst1pt0']) 
                        
                #         dtotalfinal =dtotalfinal + float(Tdcdetailslist_listGT['ddescitemtotal']) #Correct


                    
                # swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                # TdclistSave_list.dtotal = dtotal
                # TdclistSave_list.dgsttrate = dcgst1pt0

                TdclistSave_list.dsgst0 = 0
                TdclistSave_list.dcgst0 = 0 
                TdclistSave_list.digst0 = 0 

 


                TdclistSave_list.dcgst01 = 0 
                TdclistSave_list.dcgst5 = 0 
                TdclistSave_list.dcgst12 = 0 
                TdclistSave_list.dcgst18 = 0 
                TdclistSave_list.dcgst28 = 0 

                TdclistSave_list.dcgst01 = 0 
                TdclistSave_list.dsgst5 = 0 
                TdclistSave_list.dsgst12 = 0 
                TdclistSave_list.dsgst18 = 0 
                TdclistSave_list.dsgst28 = 0 
 

                TdclistSave_list.dsgst01 = dsgst01 
                TdclistSave_list.dsgst5 = dsgst5 
                TdclistSave_list.dsgst12 = dsgst12 
                TdclistSave_list.dsgst18 = dsgst18 
                TdclistSave_list.dsgst28 = dsgst28  

                TdclistSave_list.dcgst01 =dcgst01 
                TdclistSave_list.dcgst5 = dcgst5 
                TdclistSave_list.dcgst12 =dcgst12
                TdclistSave_list.dcgst18 = dcgst18 
                TdclistSave_list.dcgst28 = dcgst28

                TdclistSave_list.dtotalfinal = dtotalfinal
                TdclistSave_list.dtotalfinal = dtotalfinal
                TdclistSave_list.swords = swords.upper()  

                TdclistSave_list.ackdate1 = ackdate1
                TdclistSave_list.ackdate = ackdate
                TdclistSave_list.ewaydate1 = ewaydate1
                TdclistSave_list.ewaydate = ewaydate
                TdclistSave_list.sdate1 = sdate1
                TdclistSave_list.sdate = sdate
                TdclistSave_list.podate1 = podate1
                TdclistSave_list.podate = podate
                TdclistSave_list.sworkfrom = sworkfrom
                TdclistSave_list.sfromdate = sfromdate
                TdclistSave_list.sworkfto = sworkfto
                TdclistSave_list.stodate = stodate
                TdclistSave_list.sworkfto = sworkfto
                TdclistSave_list.inrno = inrno
                TdclistSave_list.ackno = ackno
                TdclistSave_list.ewayno = ewayno
                TdclistSave_list.scategoryofservice = scategoryofservice
                TdclistSave_list.stype1 = stype1
                TdclistSave_list.sinvoicerefno = sinvoicerefno
                TdclistSave_list.pono = pono
                TdclistSave_list.note1 = note1 

                TdclistSave_list.customerid = customerid
                TdclistSave_list.customername = customername
                TdclistSave_list.saddressclient = saddressclient
                TdclistSave_list.scustomerpan = scustomerpan
                TdclistSave_list.scustomergst = scustomergst
                TdclistSave_list.sstatecode = sstatecode
                
                TdclistSave_list.customersiteid = customersiteid
                TdclistSave_list.customernamesite = customernamesite
                TdclistSave_list.saddresssite = saddresssite 
                TdclistSave_list.swords= swords.upper()
                TdclistSave_list.saddress3 = saddress3
                TdclistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdclist_list = Tdclist.objects.get(salesbillid=lID) 
                Tdcdetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DCListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tdclist_list' : Tdclist_list,
                                    'Tdcdetailslist_list' : Tdcdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tdclist_list = Tdclist.objects.get(salesbillid=lID) 
        Tdcdetailslist_list = Tdcdetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tdclist_list.customerid).values() 
          
        return render(request, "BillingSol/DCListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tdclist_list' : Tdclist_list,
                            'Tdcdetailslist_list' : Tdcdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 



@csrf_exempt
def PurchaseOrderList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('PurchaseOrderListAdd')  
        
    else:
        
        Tpurchaseorderlist_list = Tpurchaseorderlist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tpurchaseorderlist_list.count()
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
        paginator = Paginator(Tpurchaseorderlist_list, lRecCount1)
        try:
            Tpurchaseorderlist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tpurchaseorderlist_lists = paginator.page(1)
        except EmptyPage:
            Tpurchaseorderlist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/PurchaseOrderList.html",
                    {
                        'Tpurchaseorderlist_list':Tpurchaseorderlist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def PurchaseOrderListAdd(request):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""

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

            return   redirect('PurchaseOrderList') 

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

                        salesbillno=McompanylistGet.linvoice5 + 1
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
                        sinvoicerefno=McompanylistGet.sformat5 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice5 = salesbillno
                        Mcompanylist_AddNewOBJ.lyear = finyear 
                        
                        Mcompanylist_AddNewOBJ.save()


            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.suppliername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode
            
            
            Tpurchaseorderlist_AddNewOBJ = Tpurchaseorderlist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15, 	stermms1=stermms1, 	stermms2=stermms2, 	stermms3=stermms3, 	stermms4=stermms4, 	stermms5=stermms5, 	stermms6=stermms6, 	stermms7=stermms7, 	stermms8=stermms8, 	stermms9=stermms9, 	stermms10=stermms10, 	sprofile1=sprofile1, 	sprofile2=sprofile2, 	sprofile3=sprofile3, 	spaymentrecddetails1=spaymentrecddetails1, 	spaymentrecddetails2=spaymentrecddetails2, 	spaymentrecddetails3=spaymentrecddetails3)
 
            Tpurchaseorderlist_AddNewOBJ.save()
            salesbillid = Tpurchaseorderlist_AddNewOBJ.salesbillid

            return   redirect('PurchaseOrderListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')                 
        return render(request, "BillingSol/PurchaseOrderListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


  
@csrf_exempt
def PurchaseOrderListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tpurchaseorderdetailslist_list.salesbillid
    
    # if Tpurchaseorderdetailslist_list:
    #     for Tpurchaseorderdetailslist_listQ in Tpurchaseorderdetailslist_list:
    #         lDetId = Tpurchaseorderdetailslist_listQ['salesbillid']

    Tpurchaseorderlist_listOBJ =  Tpurchaseorderdetailslist.objects.get(salesordermultiid=lID).delete()
          


    TpurchaseorderlistSave_list = Tpurchaseorderlist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tpurchaseorderdetailslist_listG = Tpurchaseorderdetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0


                

    if Tpurchaseorderdetailslist_listG:
        for Tpurchaseorderdetailslist_listGT in Tpurchaseorderdetailslist_listG:
            dtotal =dtotal + float(Tpurchaseorderdetailslist_listGT['qty'] * Tpurchaseorderdetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tpurchaseorderdetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tpurchaseorderdetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tpurchaseorderdetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tpurchaseorderdetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tpurchaseorderdetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tpurchaseorderdetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tpurchaseorderdetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tpurchaseorderdetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tpurchaseorderdetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
            
            
            dtotalfinal =dtotalfinal + float(Tpurchaseorderdetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TpurchaseorderlistSave_list.dtotal = dtotal
    TpurchaseorderlistSave_list.dgsttrate = dcgst1pt0

    TpurchaseorderlistSave_list.dsgst0 = 0
    TpurchaseorderlistSave_list.dcgst0 = 0 
    TpurchaseorderlistSave_list.digst0 = 0 




    TpurchaseorderlistSave_list.dcgst01 = 0 
    TpurchaseorderlistSave_list.dcgst5 = 0 
    TpurchaseorderlistSave_list.dcgst12 = 0 
    TpurchaseorderlistSave_list.dcgst18 = 0 
    TpurchaseorderlistSave_list.dcgst28 = 0 

    TpurchaseorderlistSave_list.dcgst01 = 0 
    TpurchaseorderlistSave_list.dsgst5 = 0 
    TpurchaseorderlistSave_list.dsgst12 = 0 
    TpurchaseorderlistSave_list.dsgst18 = 0 
    TpurchaseorderlistSave_list.dsgst28 = 0 
 

    TpurchaseorderlistSave_list.dsgst01 = dsgst01 
    TpurchaseorderlistSave_list.dsgst5 = dsgst5 
    TpurchaseorderlistSave_list.dsgst12 = dsgst12 
    TpurchaseorderlistSave_list.dsgst18 = dsgst18 
    TpurchaseorderlistSave_list.dsgst28 = dsgst28 

    TpurchaseorderlistSave_list.dcgst01 =dcgst01 
    TpurchaseorderlistSave_list.dcgst5 = dcgst5 
    TpurchaseorderlistSave_list.dcgst12 =dcgst12
    TpurchaseorderlistSave_list.dcgst18 = dcgst18 
    TpurchaseorderlistSave_list.dcgst28 = dcgst28

    TpurchaseorderlistSave_list.dtotalfinal = dtotalfinal
    TpurchaseorderlistSave_list.dtotalfinal = dtotalfinal
    TpurchaseorderlistSave_list.swords = swords.upper()  


    TpurchaseorderlistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('PurchaseOrderListDetails', lID=lDetId)  


@csrf_exempt
def PurchaseOrderListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""



    
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
                    McustomerlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.suppliername 
                        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
                         
                        scustomerpan=McustomerlistGet.panno
                        scustomergst=McustomerlistGet.gstno
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TpurchaseorderlistSave_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 

                        TpurchaseorderlistSave_list.customerid = customerid
                        TpurchaseorderlistSave_list.customername = customername
                        TpurchaseorderlistSave_list.saddressclient = saddressclient
                        TpurchaseorderlistSave_list.scustomerpan = scustomerpan
                        TpurchaseorderlistSave_list.scustomergst = scustomergst
                        TpurchaseorderlistSave_list.sstatecode = sstatecode
                        TpurchaseorderlistSave_list.save()


                Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')     
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace')     
        

                Tpurchaseorderlist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
                Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/PurchaseOrderListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Msupplierlist_list' : Msupplierlist_list,
                                    'Tpurchaseorderlist_list' : Tpurchaseorderlist_list,
                                    'Tpurchaseorderdetailslist_list' : Tpurchaseorderdetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TpurchaseorderlistSave_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 

                        TpurchaseorderlistSave_list.customersiteid = customersiteid
                        TpurchaseorderlistSave_list.customernamesite = customernamesite
                        TpurchaseorderlistSave_list.saddresssite = saddresssite 
                        

                        TpurchaseorderlistSave_list.spinsite = MsitelistGet.sstatecode
                        TpurchaseorderlistSave_list.sstatesite = MsitelistGet.stempname1
                        TpurchaseorderlistSave_list.scitysite = MsitelistGet.stempname2



                        TpurchaseorderlistSave_list.save()


                
            Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')       
    

            Tpurchaseorderlist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
            Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace') 
            
            return render(request, "BillingSol/PurchaseOrderListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'Tpurchaseorderlist_list' : Tpurchaseorderlist_list,
                            'Tpurchaseorderdetailslist_list' : Tpurchaseorderdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TpurchaseorderlistSave_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.suppliername 
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
                           
                        TpurchaseorderlistSave_list.spinsite = MsitelistGet.sstatecode
                        TpurchaseorderlistSave_list.sstatesite = MsitelistGet.stempname1
                        TpurchaseorderlistSave_list.scitysite = MsitelistGet.stempname2


                        
                    

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

            sdate1=data.get('txTpurchaseorderDate') 
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


            TpurchaseorderlistSave_list.ackdate1 = ackdate1
            TpurchaseorderlistSave_list.ackdate = ackdate
            TpurchaseorderlistSave_list.ewaydate1 = ewaydate1
            TpurchaseorderlistSave_list.ewaydate = ewaydate
            TpurchaseorderlistSave_list.sdate1 = sdate1
            TpurchaseorderlistSave_list.sdate = sdate
            TpurchaseorderlistSave_list.podate1 = podate1
            TpurchaseorderlistSave_list.podate = podate
            TpurchaseorderlistSave_list.sworkfrom = sworkfrom
            TpurchaseorderlistSave_list.sfromdate = sfromdate
            TpurchaseorderlistSave_list.sworkfto = sworkfto
            TpurchaseorderlistSave_list.stodate = stodate
            TpurchaseorderlistSave_list.sworkfto = sworkfto
            TpurchaseorderlistSave_list.inrno = inrno
            TpurchaseorderlistSave_list.ackno = ackno
            TpurchaseorderlistSave_list.ewayno = ewayno
            TpurchaseorderlistSave_list.scategoryofservice = scategoryofservice
            TpurchaseorderlistSave_list.stype1 = stype1
            TpurchaseorderlistSave_list.sinvoicerefno = sinvoicerefno
            TpurchaseorderlistSave_list.pono = pono
            TpurchaseorderlistSave_list.note1 = note1 

            TpurchaseorderlistSave_list.customerid = customerid
            TpurchaseorderlistSave_list.customername = customername
            TpurchaseorderlistSave_list.saddressclient = saddressclient
            TpurchaseorderlistSave_list.scustomerpan = scustomerpan
            TpurchaseorderlistSave_list.scustomergst = scustomergst
            TpurchaseorderlistSave_list.sstatecode = sstatecode
            
            TpurchaseorderlistSave_list.customersiteid = customersiteid
            TpurchaseorderlistSave_list.customernamesite = customernamesite
            TpurchaseorderlistSave_list.saddresssite = saddresssite 
            TpurchaseorderlistSave_list.save()
            

            Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')     
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace')     
    

            Tpurchaseorderlist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
            Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/PurchaseOrderListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Msupplierlist_list' : Msupplierlist_list,
                                'Tpurchaseorderlist_list' : Tpurchaseorderlist_list,
                                'Tpurchaseorderdetailslist_list' : Tpurchaseorderdetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
            
            iCountDetails =0
            iCountDetails = Tserviceinvoicedetailslist_list.count
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'iCountDetails' : iCountDetails,
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/PurchaseOrderListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tpurchaseorderdetailslist_listG = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 

            TpurchaseorderlistSave_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 


            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    McustomerlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if McustomerlistGet:
                        customername = McustomerlistGet.suppliername 
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
                           
                        TpurchaseorderlistSave_list.spinsite = MsitelistGet.sstatecode
                        TpurchaseorderlistSave_list.sstatesite = MsitelistGet.stempname1
                        TpurchaseorderlistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

            sdate1=data.get('txTpurchaseorderDate') 
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

            dcgst1pt00 =float(unitprice) * float(qty)
            ltaxrate=float(ltaxrate)
            dsgst01=ltaxrate
            ltaxrateamt =dcgst1pt00 * ltaxrate/100
            dcgst1pt0 = ltaxrateamt
            if(ltaxrate == 0):
                dcgst01 =0
            elif(ltaxrate == 5):
                dcgst5 =ltaxrateamt 
                if(TpurchaseorderlistSave_list.sstatecode == TpurchaseorderlistSave_list.slocationstatecode):
                    dsgst5 = dcgst5/2
                else:
                    dcgst50  =ltaxrateamt
            elif(ltaxrate == 12):
                dcgst12 =ltaxrateamt 
                if(TpurchaseorderlistSave_list.sstatecode == TpurchaseorderlistSave_list.slocationstatecode):
                    dsgst12 = dcgst12/2
                else:
                    dcgst120  =ltaxrateamt
            elif(ltaxrate == 18):
                dcgst18 =ltaxrateamt 
                if(TpurchaseorderlistSave_list.sstatecode == TpurchaseorderlistSave_list.slocationstatecode):
                    dsgst18 = dcgst18/2
                else:
                    dcgst180  =ltaxrateamt
            elif(ltaxrate == 28):
                dcgst28 =ltaxrateamt 
                if(TpurchaseorderlistSave_list.sstatecode == TpurchaseorderlistSave_list.slocationstatecode):
                    dsgst28 = dcgst28/2
                else:
                    dcgst280  =ltaxrateamt


                

            ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



            
            Tpurchaseorderdetailslist_AddNewOBJ = Tpurchaseorderdetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tpurchaseorderdetailslist_AddNewOBJ.save()

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
            dcgst1pt0=0
            

                        

            if Tpurchaseorderdetailslist_listG:
                for Tpurchaseorderdetailslist_listGT in Tpurchaseorderdetailslist_listG:
                    dtotal =dtotal + float(Tpurchaseorderdetailslist_listGT['qty'] * Tpurchaseorderdetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Tpurchaseorderdetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Tpurchaseorderdetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Tpurchaseorderdetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Tpurchaseorderdetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Tpurchaseorderdetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Tpurchaseorderdetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Tpurchaseorderdetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Tpurchaseorderdetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Tpurchaseorderdetailslist_listGT['dsgst28'])
                    dcgst1pt0=dcgst1pt0 + float(Tpurchaseorderdetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Tpurchaseorderdetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TpurchaseorderlistSave_list.dtotal = dtotal
            TpurchaseorderlistSave_list.dgsttrate = dcgst1pt0

            TpurchaseorderlistSave_list.dsgst0 = 0
            TpurchaseorderlistSave_list.dcgst0 = 0 
            TpurchaseorderlistSave_list.digst0 = 0 




            TpurchaseorderlistSave_list.dcgst01 = 0 
            TpurchaseorderlistSave_list.dcgst5 = 0 
            TpurchaseorderlistSave_list.dcgst12 = 0 
            TpurchaseorderlistSave_list.dcgst18 = 0 
            TpurchaseorderlistSave_list.dcgst28 = 0 

            TpurchaseorderlistSave_list.dcgst01 = 0 
            TpurchaseorderlistSave_list.dsgst5 = 0 
            TpurchaseorderlistSave_list.dsgst12 = 0 
            TpurchaseorderlistSave_list.dsgst18 = 0 
            TpurchaseorderlistSave_list.dsgst28 = 0 


            TpurchaseorderlistSave_list.dsgst01 = dsgst01 
            TpurchaseorderlistSave_list.dsgst5 = dsgst5 
            TpurchaseorderlistSave_list.dsgst12 = dsgst12 
            TpurchaseorderlistSave_list.dsgst18 = dsgst18 
            TpurchaseorderlistSave_list.dsgst28 = dsgst28 

            TpurchaseorderlistSave_list.dcgst01 =dcgst01 
            TpurchaseorderlistSave_list.dcgst5 = dcgst5 
            TpurchaseorderlistSave_list.dcgst12 =dcgst12
            TpurchaseorderlistSave_list.dcgst18 = dcgst18 
            TpurchaseorderlistSave_list.dcgst28 = dcgst28

            TpurchaseorderlistSave_list.dtotalfinal = dtotalfinal
            TpurchaseorderlistSave_list.dtotalfinal = dtotalfinal
            TpurchaseorderlistSave_list.swords = swords.upper()  

            TpurchaseorderlistSave_list.ackdate1 = ackdate1
            TpurchaseorderlistSave_list.ackdate = ackdate
            TpurchaseorderlistSave_list.ewaydate1 = ewaydate1
            TpurchaseorderlistSave_list.ewaydate = ewaydate
            TpurchaseorderlistSave_list.sdate1 = sdate1
            TpurchaseorderlistSave_list.sdate = sdate
            TpurchaseorderlistSave_list.podate1 = podate1
            TpurchaseorderlistSave_list.podate = podate
            TpurchaseorderlistSave_list.sworkfrom = sworkfrom
            TpurchaseorderlistSave_list.sfromdate = sfromdate
            TpurchaseorderlistSave_list.sworkfto = sworkfto
            TpurchaseorderlistSave_list.stodate = stodate
            TpurchaseorderlistSave_list.sworkfto = sworkfto
            TpurchaseorderlistSave_list.inrno = inrno
            TpurchaseorderlistSave_list.ackno = ackno
            TpurchaseorderlistSave_list.ewayno = ewayno
            TpurchaseorderlistSave_list.scategoryofservice = scategoryofservice
            TpurchaseorderlistSave_list.stype1 = stype1
            TpurchaseorderlistSave_list.sinvoicerefno = sinvoicerefno
            TpurchaseorderlistSave_list.pono = pono
            TpurchaseorderlistSave_list.note1 = note1 

            TpurchaseorderlistSave_list.customerid = customerid
            TpurchaseorderlistSave_list.customername = customername
            TpurchaseorderlistSave_list.saddressclient = saddressclient
            TpurchaseorderlistSave_list.scustomerpan = scustomerpan
            TpurchaseorderlistSave_list.scustomergst = scustomergst
            TpurchaseorderlistSave_list.sstatecode = sstatecode
            
            TpurchaseorderlistSave_list.customersiteid = customersiteid
            TpurchaseorderlistSave_list.customernamesite = customernamesite
            TpurchaseorderlistSave_list.saddresssite = saddresssite 
            TpurchaseorderlistSave_list.swords= swords.upper()
            TpurchaseorderlistSave_list.save()
            

            Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')     
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace')     
    

            Tpurchaseorderlist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
            Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/PurchaseOrderListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Msupplierlist_list' : Msupplierlist_list,
                                'Tpurchaseorderlist_list' : Tpurchaseorderlist_list,
                                'Tpurchaseorderdetailslist_list' : Tpurchaseorderdetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 




    else:   
        
        Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')    
  

        Tpurchaseorderlist_list = Tpurchaseorderlist.objects.get(salesbillid=lID) 
        Tpurchaseorderdetailslist_list = Tpurchaseorderdetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace') 
          
        return render(request, "BillingSol/PurchaseOrderListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'Tpurchaseorderlist_list' : Tpurchaseorderlist_list,
                            'Tpurchaseorderdetailslist_list' : Tpurchaseorderdetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 



@csrf_exempt
def OrderAcceptanceList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('OrderAcceptanceListAdd')  
        
    else:
        
        Torderacceptancelist_list = Torderacceptancelist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Torderacceptancelist_list.count()
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
        paginator = Paginator(Torderacceptancelist_list, lRecCount1)
        try:
            Torderacceptancelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Torderacceptancelist_lists = paginator.page(1)
        except EmptyPage:
            Torderacceptancelist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/OrderAcceptanceInvoiceList.html",
                    {
                        'Torderacceptancelist_list':Torderacceptancelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def OrderAcceptanceListAdd(request):

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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""


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

            return   redirect('OrderAcceptanceList') 

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

                        salesbillno=McompanylistGet.linvoice6 + 1
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
                        sinvoicerefno=McompanylistGet.sformat6 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice6 = salesbillno
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
            
            
            Torderacceptancelist_AddNewOBJ = Torderacceptancelist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15, 	stermms1=stermms1, 	stermms2=stermms2, 	stermms3=stermms3, 	stermms4=stermms4, 	stermms5=stermms5, 	stermms6=stermms6, 	stermms7=stermms7, 	stermms8=stermms8, 	stermms9=stermms9, 	stermms10=stermms10, 	sprofile1=sprofile1, 	sprofile2=sprofile2, 	sprofile3=sprofile3, 	spaymentrecddetails1=spaymentrecddetails1, 	spaymentrecddetails2=spaymentrecddetails2, 	spaymentrecddetails3=spaymentrecddetails3)
 
            Torderacceptancelist_AddNewOBJ.save()
            salesbillid = Torderacceptancelist_AddNewOBJ.salesbillid

            return   redirect('OrderAcceptanceListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/OrderAcceptanceListAdd.html",
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
def OrderAcceptanceListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Torderacceptancedetailslist_list.salesbillid
    
    # if Torderacceptancedetailslist_list:
    #     for Torderacceptancedetailslist_listQ in Torderacceptancedetailslist_list:
    #         lDetId = Torderacceptancedetailslist_listQ['salesbillid']

    Torderacceptancelist_listOBJ =  Torderacceptancedetailslist.objects.get(salesordermultiid=lID).delete()
          


    TorderacceptancelistSave_list = Torderacceptancelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Torderacceptancedetailslist_listG = Torderacceptancedetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0


                

    if Torderacceptancedetailslist_listG:
        for Torderacceptancedetailslist_listGT in Torderacceptancedetailslist_listG:
            dtotal =dtotal + float(Torderacceptancedetailslist_listGT['qty'] * Torderacceptancedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Torderacceptancedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Torderacceptancedetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Torderacceptancedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Torderacceptancedetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Torderacceptancedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Torderacceptancedetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Torderacceptancedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Torderacceptancedetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Torderacceptancedetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Torderacceptancedetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Torderacceptancedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TorderacceptancelistSave_list.dtotal = dtotal
    TorderacceptancelistSave_list.dgsttrate = dcgst1pt0

    TorderacceptancelistSave_list.dsgst0 = 0
    TorderacceptancelistSave_list.dcgst0 = 0 
    TorderacceptancelistSave_list.digst0 = 0 




    TorderacceptancelistSave_list.dcgst01 = 0 
    TorderacceptancelistSave_list.dcgst5 = 0 
    TorderacceptancelistSave_list.dcgst12 = 0 
    TorderacceptancelistSave_list.dcgst18 = 0 
    TorderacceptancelistSave_list.dcgst28 = 0 

    TorderacceptancelistSave_list.dcgst01 = 0 
    TorderacceptancelistSave_list.dsgst5 = 0 
    TorderacceptancelistSave_list.dsgst12 = 0 
    TorderacceptancelistSave_list.dsgst18 = 0 
    TorderacceptancelistSave_list.dsgst28 = 0 
 

    TorderacceptancelistSave_list.dsgst01 = dsgst01 
    TorderacceptancelistSave_list.dsgst5 = dsgst5 
    TorderacceptancelistSave_list.dsgst12 = dsgst12 
    TorderacceptancelistSave_list.dsgst18 = dsgst18 
    TorderacceptancelistSave_list.dsgst28 = dsgst28  

    TorderacceptancelistSave_list.dcgst01 =dcgst01 
    TorderacceptancelistSave_list.dcgst5 = dcgst5 
    TorderacceptancelistSave_list.dcgst12 =dcgst12
    TorderacceptancelistSave_list.dcgst18 = dcgst18 
    TorderacceptancelistSave_list.dcgst28 = dcgst28

    TorderacceptancelistSave_list.dtotalfinal = dtotalfinal
    TorderacceptancelistSave_list.dtotalfinal = dtotalfinal
    TorderacceptancelistSave_list.swords = swords.upper()  


    TorderacceptancelistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('OrderAcceptanceListDetails', lID=lDetId)  


@csrf_exempt
def OrderAcceptanceListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""

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
                        
                        
                        TorderacceptancelistSave_list = Torderacceptancelist.objects.get(salesbillid=lID) 

                        TorderacceptancelistSave_list.customerid = customerid
                        TorderacceptancelistSave_list.customername = customername
                        TorderacceptancelistSave_list.saddressclient = saddressclient
                        TorderacceptancelistSave_list.scustomerpan = scustomerpan
                        TorderacceptancelistSave_list.scustomergst = scustomergst
                        TorderacceptancelistSave_list.sstatecode = sstatecode
                        TorderacceptancelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
                Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Torderacceptancelist_list' : Torderacceptancelist_list,
                                    'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 
        
        # if 'cmdGetSite' in request.POST:  

        #     customersiteid =0
        #     if 'cmbSite' in request.POST: 
        #         if(data.get('cmbSite').isnumeric()):
        #             customersiteid = int(data.get('cmbSite'))
        #             MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
        #             if MsitelistGet:
        #                 customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
        #                 saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
        #                 sstatecode=MsitelistGet.sstatecode 
                        
                        
        #                 TorderacceptancelistSave_list = Torderacceptancelist.objects.get(salesbillid=lID) 

        #                 TorderacceptancelistSave_list.customersiteid = customersiteid
        #                 TorderacceptancelistSave_list.customernamesite = customernamesite
        #                 TorderacceptancelistSave_list.saddresssite = saddresssite 
                        

        #                 TorderacceptancelistSave_list.spinsite = MsitelistGet.sstatecode
        #                 TorderacceptancelistSave_list.sstatesite = MsitelistGet.stempname1
        #                 TorderacceptancelistSave_list.scitysite = MsitelistGet.stempname2



        #                 TorderacceptancelistSave_list.save()


                
        #     Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

        #     Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
        #     Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
        #     Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Torderacceptancelist_list.customerid).values() 
            
        #     return render(request, "BillingSol/OrderAcceptanceListDetails.html",
        #                 {
                            
        #                 'title':'User list',  
        #                     'message':'Your User list page.',
        #                     'year':datetime.now().year,  
        #                     'Msitelist_list' : Msitelist_list,
        #                     'Mcustomerlist_list' : Mcustomerlist_list,
        #                     'Torderacceptancelist_list' : Torderacceptancelist_list,
        #                     'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
        #                     'badmin':  request.session['badmin'],  
        #                     'bFinance':  request.session['bFinance'],  
        #                     'bpo':  request.session['bSupplyChain'],  
        #                     'bSales':  request.session['bSales'],  
        #                     'badmin1':  request.session['badmin1'],    
        #                 }
        #                 )  

        if 'cmbSaveAdd' in request.POST:  

            TorderacceptancelistSave_list = Torderacceptancelist.objects.get(salesbillid=lID) 

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
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TorderacceptancelistSave_list.spinsite = MsitelistGet.sstatecode
            #             TorderacceptancelistSave_list.sstatesite = MsitelistGet.stempname1
            #             TorderacceptancelistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

            sdate1=data.get('txTorderacceptanceDate') 
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
            note2=data.get('txtPayments')  


            TorderacceptancelistSave_list.ackdate1 = ackdate1
            TorderacceptancelistSave_list.ackdate = ackdate
            TorderacceptancelistSave_list.ewaydate1 = ewaydate1
            TorderacceptancelistSave_list.ewaydate = ewaydate
            TorderacceptancelistSave_list.sdate1 = sdate1
            TorderacceptancelistSave_list.sdate = sdate
            TorderacceptancelistSave_list.podate1 = podate1
            TorderacceptancelistSave_list.podate = podate
            TorderacceptancelistSave_list.sworkfrom = sworkfrom
            TorderacceptancelistSave_list.sfromdate = sfromdate
            TorderacceptancelistSave_list.sworkfto = sworkfto
            TorderacceptancelistSave_list.stodate = stodate
            TorderacceptancelistSave_list.sworkfto = sworkfto
            TorderacceptancelistSave_list.inrno = inrno
            TorderacceptancelistSave_list.ackno = ackno
            TorderacceptancelistSave_list.ewayno = ewayno
            TorderacceptancelistSave_list.scategoryofservice = scategoryofservice
            TorderacceptancelistSave_list.stype1 = stype1
            TorderacceptancelistSave_list.sinvoicerefno = sinvoicerefno
            TorderacceptancelistSave_list.pono = pono
            TorderacceptancelistSave_list.note1 = note1 
            TorderacceptancelistSave_list.note2 = note2 

            TorderacceptancelistSave_list.customerid = customerid
            TorderacceptancelistSave_list.customername = customername
            TorderacceptancelistSave_list.saddressclient = saddressclient
            TorderacceptancelistSave_list.scustomerpan = scustomerpan
            TorderacceptancelistSave_list.scustomergst = scustomergst
            TorderacceptancelistSave_list.sstatecode = sstatecode
            
            TorderacceptancelistSave_list.customersiteid = customersiteid
            TorderacceptancelistSave_list.customernamesite = customernamesite
            TorderacceptancelistSave_list.saddresssite = saddresssite 
            TorderacceptancelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
            Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Torderacceptancelist_list' : Torderacceptancelist_list,
                                'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/OrderAcceptanceListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Torderacceptancedetailslist_listG = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 

            TorderacceptancelistSave_list = Torderacceptancelist.objects.get(salesbillid=lID) 

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
                         

            # customersiteid =0
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TorderacceptancelistSave_list.spinsite = MsitelistGet.sstatecode
            #             TorderacceptancelistSave_list.sstatesite = MsitelistGet.stempname1
            #             TorderacceptancelistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

            sdate1=data.get('txTorderacceptanceDate') 
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
            note2=data.get('txtPayments')  


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


            dcgst1pt00 =float(unitprice) * float(qty)
            ltaxrate=float(ltaxrate)
            dsgst01=ltaxrate
            ltaxrateamt =dcgst1pt00 * ltaxrate/100
            dcgst1pt0 = ltaxrateamt
            if(ltaxrate == 0):
                dcgst01 =0
            elif(ltaxrate == 5):
                dcgst5 =ltaxrateamt 
                if(TorderacceptancelistSave_list.sstatecode == TorderacceptancelistSave_list.slocationstatecode):
                    dsgst5 = dcgst5/2
                else:
                    dcgst50  =ltaxrateamt
            elif(ltaxrate == 12):
                dcgst12 =ltaxrateamt 
                if(TorderacceptancelistSave_list.sstatecode == TorderacceptancelistSave_list.slocationstatecode):
                    dsgst12 = dcgst12/2
                else:
                    dcgst120  =ltaxrateamt
            elif(ltaxrate == 18):
                dcgst18 =ltaxrateamt 
                if(TorderacceptancelistSave_list.sstatecode == TorderacceptancelistSave_list.slocationstatecode):
                    dsgst18 = dcgst18/2
                else:
                    dcgst180  =ltaxrateamt
            elif(ltaxrate == 28):
                dcgst28 =ltaxrateamt 
                if(TorderacceptancelistSave_list.sstatecode == TorderacceptancelistSave_list.slocationstatecode):
                    dsgst28 = dcgst28/2
                else:
                    dcgst280  =ltaxrateamt


                

            ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



            
            Torderacceptancedetailslist_AddNewOBJ = Torderacceptancedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Torderacceptancedetailslist_AddNewOBJ.save()

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
            dcgst1pt0=0

            

                        

            if Torderacceptancedetailslist_listG:
                for Torderacceptancedetailslist_listGT in Torderacceptancedetailslist_listG:
                    dtotal =dtotal + float(Torderacceptancedetailslist_listGT['qty'] * Torderacceptancedetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Torderacceptancedetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Torderacceptancedetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Torderacceptancedetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Torderacceptancedetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Torderacceptancedetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Torderacceptancedetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Torderacceptancedetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Torderacceptancedetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Torderacceptancedetailslist_listGT['dsgst28'])
                    dcgst1pt0=dcgst1pt0 + float(Torderacceptancedetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Torderacceptancedetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TorderacceptancelistSave_list.dtotal = dtotal
            TorderacceptancelistSave_list.dgsttrate = dcgst1pt0

            TorderacceptancelistSave_list.dsgst0 = 0
            TorderacceptancelistSave_list.dcgst0 = 0 
            TorderacceptancelistSave_list.digst0 = 0 




            TorderacceptancelistSave_list.dcgst01 = 0 
            TorderacceptancelistSave_list.dcgst5 = 0 
            TorderacceptancelistSave_list.dcgst12 = 0 
            TorderacceptancelistSave_list.dcgst18 = 0 
            TorderacceptancelistSave_list.dcgst28 = 0 

            TorderacceptancelistSave_list.dcgst01 = 0 
            TorderacceptancelistSave_list.dsgst5 = 0 
            TorderacceptancelistSave_list.dsgst12 = 0 
            TorderacceptancelistSave_list.dsgst18 = 0 
            TorderacceptancelistSave_list.dsgst28 = 0 


            TorderacceptancelistSave_list.dsgst01 = dsgst01 
            TorderacceptancelistSave_list.dsgst5 = dsgst5 
            TorderacceptancelistSave_list.dsgst12 = dsgst12 
            TorderacceptancelistSave_list.dsgst18 = dsgst18 
            TorderacceptancelistSave_list.dsgst28 = dsgst28  

            TorderacceptancelistSave_list.dcgst01 =dcgst01 
            TorderacceptancelistSave_list.dcgst5 = dcgst5 
            TorderacceptancelistSave_list.dcgst12 =dcgst12
            TorderacceptancelistSave_list.dcgst18 = dcgst18 
            TorderacceptancelistSave_list.dcgst28 = dcgst28

            TorderacceptancelistSave_list.dtotalfinal = dtotalfinal
            TorderacceptancelistSave_list.dtotalfinal = dtotalfinal
            TorderacceptancelistSave_list.swords = swords.upper()  

            TorderacceptancelistSave_list.ackdate1 = ackdate1
            TorderacceptancelistSave_list.ackdate = ackdate
            TorderacceptancelistSave_list.ewaydate1 = ewaydate1
            TorderacceptancelistSave_list.ewaydate = ewaydate
            TorderacceptancelistSave_list.sdate1 = sdate1
            TorderacceptancelistSave_list.sdate = sdate
            TorderacceptancelistSave_list.podate1 = podate1
            TorderacceptancelistSave_list.podate = podate
            TorderacceptancelistSave_list.sworkfrom = sworkfrom
            TorderacceptancelistSave_list.sfromdate = sfromdate
            TorderacceptancelistSave_list.sworkfto = sworkfto
            TorderacceptancelistSave_list.stodate = stodate
            TorderacceptancelistSave_list.sworkfto = sworkfto
            TorderacceptancelistSave_list.inrno = inrno
            TorderacceptancelistSave_list.ackno = ackno
            TorderacceptancelistSave_list.ewayno = ewayno
            TorderacceptancelistSave_list.scategoryofservice = scategoryofservice
            TorderacceptancelistSave_list.stype1 = stype1
            TorderacceptancelistSave_list.sinvoicerefno = sinvoicerefno
            TorderacceptancelistSave_list.pono = pono
            TorderacceptancelistSave_list.note1 = note1 
            TorderacceptancelistSave_list.note2 = note2 

            TorderacceptancelistSave_list.customerid = customerid
            TorderacceptancelistSave_list.customername = customername
            TorderacceptancelistSave_list.saddressclient = saddressclient
            TorderacceptancelistSave_list.scustomerpan = scustomerpan
            TorderacceptancelistSave_list.scustomergst = scustomergst
            TorderacceptancelistSave_list.sstatecode = sstatecode
            
            TorderacceptancelistSave_list.customersiteid = customersiteid
            TorderacceptancelistSave_list.customernamesite = customernamesite
            TorderacceptancelistSave_list.saddresssite = saddresssite 
            TorderacceptancelistSave_list.swords= swords.upper()
            TorderacceptancelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
            Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Torderacceptancelist_list' : Torderacceptancelist_list,
                                'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 

        elif 'cmdDownloadPO' in request.POST:  
 
            sFile = ""
            TorderacceptancelistQ =  Torderacceptancelist.objects.get(salesbillid=lID) 
            if TorderacceptancelistQ:
                sFile = TorderacceptancelistQ.sfile11
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

        elif  request.method == 'POST' and request.FILES['UploadFiles']: 
                

            myfile = request.FILES['UploadFiles']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            TorderacceptancelistQ =  Torderacceptancelist.objects.get(salesbillid=lID) 
            
            TorderacceptancelistQ.sfile11 = filename
            TorderacceptancelistQ.sfolder11 =uploaded_file_url
            TorderacceptancelistQ.save()
            messages.success(request, 'P O  is Updated successfully!')

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    


            Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
            Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Torderacceptancelist_list.customerid).values() 
            
            return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Torderacceptancelist_list' : Torderacceptancelist_list,
                                'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                                'badmin':  request.session['badmin'],  
                                'bFinance':  request.session['bFinance'],  
                                'bpo':  request.session['bSupplyChain'],  
                                'bSales':  request.session['bSales'],  
                                'badmin1':  request.session['badmin1'],    
                            }
                            ) 

        else:   
            
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
            Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Torderacceptancelist_list.customerid).values() 
            
            return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Torderacceptancelist_list' : Torderacceptancelist_list,
                                'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                                'badmin':  request.session['badmin'],  
                                'bFinance':  request.session['bFinance'],  
                                'bpo':  request.session['bSupplyChain'],  
                                'bSales':  request.session['bSales'],  
                                'badmin1':  request.session['badmin1'],    
                            }
                            )

    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Torderacceptancelist_list = Torderacceptancelist.objects.get(salesbillid=lID) 
        Torderacceptancedetailslist_list = Torderacceptancedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Torderacceptancelist_list.customerid).values() 
          
        return render(request, "BillingSol/OrderAcceptanceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Torderacceptancelist_list' : Torderacceptancelist_list,
                            'Torderacceptancedetailslist_list' : Torderacceptancedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


@csrf_exempt
def ProposalList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProposalListAdd')  
        
    else:
        
        Tproposallist_list = Tproposallist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tproposallist_list.count()
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
        paginator = Paginator(Tproposallist_list, lRecCount1)
        try:
            Tproposallist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tproposallist_lists = paginator.page(1)
        except EmptyPage:
            Tproposallist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/ProposalList.html",
                    {
                        'Tproposallist_list':Tproposallist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def ProposalListAdd(request):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""

    
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

            return   redirect('ProposalList') 

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

                        salesbillno=McompanylistGet.linvoice7 + 1
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
                        sinvoicerefno=McompanylistGet.sformat7 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice7 = salesbillno
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
            
            
            Tproposallist_AddNewOBJ = Tproposallist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15, 	stermms1=stermms1, 	stermms2=stermms2, 	stermms3=stermms3, 	stermms4=stermms4, 	stermms5=stermms5, 	stermms6=stermms6, 	stermms7=stermms7, 	stermms8=stermms8, 	stermms9=stermms9, 	stermms10=stermms10, 	sprofile1=sprofile1, 	sprofile2=sprofile2, 	sprofile3=sprofile3, 	spaymentrecddetails1=spaymentrecddetails1, 	spaymentrecddetails2=spaymentrecddetails2, 	spaymentrecddetails3=spaymentrecddetails3)
 
            Tproposallist_AddNewOBJ.save()
            salesbillid = Tproposallist_AddNewOBJ.salesbillid

            return   redirect('ProposalListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProposalListAdd.html",
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
def ProposalListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tproposaldetailslist_list = Tproposaldetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tproposaldetailslist_list.salesbillid
    
    # if Tproposaldetailslist_list:
    #     for Tproposaldetailslist_listQ in Tproposaldetailslist_list:
    #         lDetId = Tproposaldetailslist_listQ['salesbillid']

    Tproposallist_listOBJ =  Tproposaldetailslist.objects.get(salesordermultiid=lID).delete()
          


    TproposallistSave_list = Tproposallist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tproposaldetailslist_listG = Tproposaldetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0

                

    if Tproposaldetailslist_listG:
        for Tproposaldetailslist_listGT in Tproposaldetailslist_listG:
            dtotal =dtotal + float(Tproposaldetailslist_listGT['qty'] * Tproposaldetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tproposaldetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tproposaldetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tproposaldetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tproposaldetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tproposaldetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tproposaldetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tproposaldetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tproposaldetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tproposaldetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tproposaldetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Tproposaldetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TproposallistSave_list.dtotal = dtotal
    TproposallistSave_list.dgsttrate = dcgst1pt0

    TproposallistSave_list.dsgst0 = 0
    TproposallistSave_list.dcgst0 = 0 
    TproposallistSave_list.digst0 = 0 




    TproposallistSave_list.dcgst01 = 0 
    TproposallistSave_list.dcgst5 = 0 
    TproposallistSave_list.dcgst12 = 0 
    TproposallistSave_list.dcgst18 = 0 
    TproposallistSave_list.dcgst28 = 0 

    TproposallistSave_list.dcgst01 = 0 
    TproposallistSave_list.dsgst5 = 0 
    TproposallistSave_list.dsgst12 = 0 
    TproposallistSave_list.dsgst18 = 0 
    TproposallistSave_list.dsgst28 = 0 
 

    TproposallistSave_list.dsgst01 = dsgst01 
    TproposallistSave_list.dsgst5 = dsgst5 
    TproposallistSave_list.dsgst12 = dsgst12 
    TproposallistSave_list.dsgst18 = dsgst18 
    TproposallistSave_list.dsgst28 = dsgst28  

    TproposallistSave_list.dcgst01 =dcgst01 
    TproposallistSave_list.dcgst5 = dcgst5 
    TproposallistSave_list.dcgst12 =dcgst12
    TproposallistSave_list.dcgst18 = dcgst18 
    TproposallistSave_list.dcgst28 = dcgst28

    TproposallistSave_list.dtotalfinal = dtotalfinal
    TproposallistSave_list.dtotalfinal = dtotalfinal
    TproposallistSave_list.swords = swords.upper()  


    TproposallistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('ProposalListDetails', lID=lDetId)  


@csrf_exempt
def ProposalListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
    stermms1=""
    stermms2=""
    stermms3=""
    stermms4=""
    stermms5=""
    stermms6=""
    stermms7=""
    stermms8=""
    stermms9=""
    stermms10=""
    sprofile1=""
    sprofile2=""
    sprofile3=""
    spaymentrecddetails1=""
    spaymentrecddetails2=""
    spaymentrecddetails3=""

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
                        
                        
                        TproposallistSave_list = Tproposallist.objects.get(salesbillid=lID) 

                        TproposallistSave_list.customerid = customerid
                        TproposallistSave_list.customername = customername
                        TproposallistSave_list.saddressclient = saddressclient
                        TproposallistSave_list.scustomerpan = scustomerpan
                        TproposallistSave_list.scustomergst = scustomergst
                        TproposallistSave_list.sstatecode = sstatecode
                        TproposallistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproposallist_list = Tproposallist.objects.get(salesbillid=lID) 
                Tproposaldetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProposalListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproposallist_list' : Tproposallist_list,
                                    'Tproposaldetailslist_list' : Tproposaldetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TproposallistSave_list = Tproposallist.objects.get(salesbillid=lID) 

                        TproposallistSave_list.customersiteid = customersiteid
                        TproposallistSave_list.customernamesite = customernamesite
                        TproposallistSave_list.saddresssite = saddresssite 
                        

                        TproposallistSave_list.spinsite = MsitelistGet.sstatecode
                        TproposallistSave_list.sstatesite = MsitelistGet.stempname1
                        TproposallistSave_list.scitysite = MsitelistGet.stempname2



                        TproposallistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tproposallist_list = Tproposallist.objects.get(salesbillid=lID) 
            Tproposaldetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproposallist_list.customerid).values() 
            
            return render(request, "BillingSol/ProposalListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproposallist_list' : Tproposallist_list,
                            'Tproposaldetailslist_list' : Tproposaldetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TproposallistSave_list = Tproposallist.objects.get(salesbillid=lID) 

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
                         

            # customersiteid =0
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TproposallistSave_list.spinsite = MsitelistGet.sstatecode
            #             TproposallistSave_list.sstatesite = MsitelistGet.stempname1
            #             TproposallistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

            sdate1=data.get('txTproposalDate') 
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

            
            sprofile1=data.get('txtProfile1')  
            sprofile2=data.get('txtProfile2')  
            saddress1site=data.get('txtQuotePresentTo')  
            saddress2site=data.get('txtQuotePresentBy')  
            stermms1=data.get('txtTerm1')  
            stermms2=data.get('txtTerm2')  
            stermms3=data.get('txtTerm3')  
            stermms4=data.get('txtTerm4')  
            stermms5=data.get('txtTerm5')  
            stermms6=data.get('txtTerm6')  
            stermms7=data.get('txtTerm7')  

            TproposallistSave_list.sprofile1 = sprofile1
            TproposallistSave_list.sprofile2 = sprofile2
            TproposallistSave_list.saddress1site = saddress1site
            TproposallistSave_list.saddress2site = saddress2site
            TproposallistSave_list.stermms1 = stermms1
            TproposallistSave_list.stermms2 = stermms2
            TproposallistSave_list.stermms3 = stermms3
            TproposallistSave_list.stermms4 = stermms4
            TproposallistSave_list.stermms5 = stermms5
            TproposallistSave_list.stermms6 = stermms6
            TproposallistSave_list.stermms7 = stermms7

            TproposallistSave_list.ackdate1 = ackdate1
            TproposallistSave_list.ackdate = ackdate
            TproposallistSave_list.ewaydate1 = ewaydate1
            TproposallistSave_list.ewaydate = ewaydate
            TproposallistSave_list.sdate1 = sdate1
            TproposallistSave_list.sdate = sdate
            TproposallistSave_list.podate1 = podate1
            TproposallistSave_list.podate = podate
            TproposallistSave_list.sworkfrom = sworkfrom
            TproposallistSave_list.sfromdate = sfromdate
            TproposallistSave_list.sworkfto = sworkfto
            TproposallistSave_list.stodate = stodate
            TproposallistSave_list.sworkfto = sworkfto
            TproposallistSave_list.inrno = inrno
            TproposallistSave_list.ackno = ackno
            TproposallistSave_list.ewayno = ewayno
            TproposallistSave_list.scategoryofservice = scategoryofservice
            TproposallistSave_list.stype1 = stype1
            TproposallistSave_list.sinvoicerefno = sinvoicerefno
            TproposallistSave_list.pono = pono
            TproposallistSave_list.note1 = note1 

            TproposallistSave_list.customerid = customerid
            TproposallistSave_list.customername = customername
            TproposallistSave_list.saddressclient = saddressclient
            TproposallistSave_list.scustomerpan = scustomerpan
            TproposallistSave_list.scustomergst = scustomergst
            TproposallistSave_list.sstatecode = sstatecode
            
            TproposallistSave_list.customersiteid = customersiteid
            TproposallistSave_list.customernamesite = customernamesite
            TproposallistSave_list.saddresssite = saddresssite 
            TproposallistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproposallist_list = Tproposallist.objects.get(salesbillid=lID) 
            Tproposaldetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProposalListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproposallist_list' : Tproposallist_list,
                                'Tproposaldetailslist_list' : Tproposaldetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tproposallist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProposalListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tproposaldetailslist_listG = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 

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
                         

            # customersiteid =0
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TproposallistSave_list.spinsite = MsitelistGet.sstatecode
            #             TproposallistSave_list.sstatesite = MsitelistGet.stempname1
            #             TproposallistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

            sdate1=data.get('txTproposalDate') 
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

            TproposallistSave_list = Tproposallist.objects.get(salesbillid=lID) 


            sprofile1=data.get('txtProfile1')  
            sprofile2=data.get('txtProfile2')  
            saddress1site=data.get('txtQuotePresentTo')  
            saddress2site=data.get('txtQuotePresentBy')  
            stermms1=data.get('txtTerm1')  
            stermms2=data.get('txtTerm2')  
            stermms3=data.get('txtTerm3')  
            stermms4=data.get('txtTerm4')  
            stermms5=data.get('txtTerm5')  
            stermms6=data.get('txtTerm6')  
            stermms7=data.get('txtTerm7')  

            TproposallistSave_list.sprofile1 = sprofile1
            TproposallistSave_list.sprofile2 = sprofile2
            TproposallistSave_list.saddress1site = saddress1site
            TproposallistSave_list.saddress2site = saddress2site
            TproposallistSave_list.stermms1 = stermms1
            TproposallistSave_list.stermms2 = stermms2
            TproposallistSave_list.stermms3 = stermms3
            TproposallistSave_list.stermms4 = stermms4
            TproposallistSave_list.stermms5 = stermms5
            TproposallistSave_list.stermms6 = stermms6
            TproposallistSave_list.stermms7 = stermms7

            dcgst1pt00 =float(unitprice) * float(qty)
            ltaxrate=float(ltaxrate)
            dsgst01=ltaxrate
            ltaxrateamt =dcgst1pt00 * ltaxrate/100
            dcgst1pt0 = ltaxrateamt
            if(ltaxrate == 0):
                dcgst01 =0
            elif(ltaxrate == 5):
                dcgst5 =ltaxrateamt 
                if(TproposallistSave_list.sstatecode == TproposallistSave_list.slocationstatecode):
                    dsgst5 = dcgst5/2
                else:
                    dcgst50  =ltaxrateamt
            elif(ltaxrate == 12):
                dcgst12 =ltaxrateamt 
                if(TproposallistSave_list.sstatecode == TproposallistSave_list.slocationstatecode):
                    dsgst12 = dcgst12/2
                else:
                    dcgst120  =ltaxrateamt
            elif(ltaxrate == 18):
                dcgst18 =ltaxrateamt 
                if(TproposallistSave_list.sstatecode == TproposallistSave_list.slocationstatecode):
                    dsgst18 = dcgst18/2
                else:
                    dcgst180  =ltaxrateamt
            elif(ltaxrate == 28):
                dcgst28 =ltaxrateamt 
                if(TproposallistSave_list.sstatecode == TproposallistSave_list.slocationstatecode):
                    dsgst28 = dcgst28/2
                else:
                    dcgst280  =ltaxrateamt


                

            ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



            
            Tproposaldetailslist_AddNewOBJ = Tproposaldetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tproposaldetailslist_AddNewOBJ.save()

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
            dcgst1pt0=0

            

                        

            if Tproposaldetailslist_listG:
                for Tproposaldetailslist_listGT in Tproposaldetailslist_listG:
                    dtotal =dtotal + float(Tproposaldetailslist_listGT['qty'] * Tproposaldetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Tproposaldetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Tproposaldetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Tproposaldetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Tproposaldetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Tproposaldetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Tproposaldetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Tproposaldetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Tproposaldetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Tproposaldetailslist_listGT['dsgst28'])
                    dcgst1pt0=dcgst1pt0 + float(Tproposaldetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Tproposaldetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TproposallistSave_list.dtotal = dtotal
            TproposallistSave_list.dgsttrate = dcgst1pt0

            TproposallistSave_list.dsgst0 = 0
            TproposallistSave_list.dcgst0 = 0 
            TproposallistSave_list.digst0 = 0 




            TproposallistSave_list.dcgst01 = 0 
            TproposallistSave_list.dcgst5 = 0 
            TproposallistSave_list.dcgst12 = 0 
            TproposallistSave_list.dcgst18 = 0 
            TproposallistSave_list.dcgst28 = 0 

            TproposallistSave_list.dcgst01 = 0 
            TproposallistSave_list.dsgst5 = 0 
            TproposallistSave_list.dsgst12 = 0 
            TproposallistSave_list.dsgst18 = 0 
            TproposallistSave_list.dsgst28 = 0 


            TproposallistSave_list.dsgst01 = dsgst01 
            TproposallistSave_list.dsgst5 = dsgst5 
            TproposallistSave_list.dsgst12 = dsgst12 
            TproposallistSave_list.dsgst18 = dsgst18 
            TproposallistSave_list.dsgst28 = dsgst28  

            TproposallistSave_list.dcgst01 =dcgst01 
            TproposallistSave_list.dcgst5 = dcgst5 
            TproposallistSave_list.dcgst12 =dcgst12
            TproposallistSave_list.dcgst18 = dcgst18 
            TproposallistSave_list.dcgst28 = dcgst28

            TproposallistSave_list.dtotalfinal = dtotalfinal
            TproposallistSave_list.dtotalfinal = dtotalfinal
            TproposallistSave_list.swords = swords.upper()  

            TproposallistSave_list.ackdate1 = ackdate1
            TproposallistSave_list.ackdate = ackdate
            TproposallistSave_list.ewaydate1 = ewaydate1
            TproposallistSave_list.ewaydate = ewaydate
            TproposallistSave_list.sdate1 = sdate1
            TproposallistSave_list.sdate = sdate
            TproposallistSave_list.podate1 = podate1
            TproposallistSave_list.podate = podate
            TproposallistSave_list.sworkfrom = sworkfrom
            TproposallistSave_list.sfromdate = sfromdate
            TproposallistSave_list.sworkfto = sworkfto
            TproposallistSave_list.stodate = stodate
            TproposallistSave_list.sworkfto = sworkfto
            TproposallistSave_list.inrno = inrno
            TproposallistSave_list.ackno = ackno
            TproposallistSave_list.ewayno = ewayno
            TproposallistSave_list.scategoryofservice = scategoryofservice
            TproposallistSave_list.stype1 = stype1
            TproposallistSave_list.sinvoicerefno = sinvoicerefno
            TproposallistSave_list.pono = pono
            TproposallistSave_list.note1 = note1 

            TproposallistSave_list.customerid = customerid
            TproposallistSave_list.customername = customername
            TproposallistSave_list.saddressclient = saddressclient
            TproposallistSave_list.scustomerpan = scustomerpan
            TproposallistSave_list.scustomergst = scustomergst
            TproposallistSave_list.sstatecode = sstatecode
            
            TproposallistSave_list.customersiteid = customersiteid
            TproposallistSave_list.customernamesite = customernamesite
            TproposallistSave_list.saddresssite = saddresssite 
            TproposallistSave_list.swords= swords.upper()
            TproposallistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproposallist_list = Tproposallist.objects.get(salesbillid=lID) 
            Tproposaldetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProposalListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproposallist_list' : Tproposallist_list,
                                'Tproposaldetailslist_list' : Tproposaldetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tproposallist_list = Tproposallist.objects.get(salesbillid=lID) 
        Tproposaldetailslist_list = Tproposaldetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproposallist_list.customerid).values() 
          
        return render(request, "BillingSol/ProposalListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproposallist_list' : Tproposallist_list,
                            'Tproposaldetailslist_list' : Tproposaldetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

@csrf_exempt
def CreditNoteList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('CreditNoteListAdd')  
        
    else:
        
        Tcreditnotelist_list = Tcreditnotelist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tcreditnotelist_list.count()
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
        paginator = Paginator(Tcreditnotelist_list, lRecCount1)
        try:
            Tcreditnotelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tcreditnotelist_lists = paginator.page(1)
        except EmptyPage:
            Tcreditnotelist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/CreditNoteList.html",
                    {
                        'Tcreditnotelist_list':Tcreditnotelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def CreditNoteListAdd(request):
    
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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

            return   redirect('CreditNoteList') 

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

                        salesbillno=McompanylistGet.linvoice8 + 1
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
                        sinvoicerefno=McompanylistGet.sformat8 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice8 = salesbillno
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
            
            
            Tcreditnotelist_AddNewOBJ = Tcreditnotelist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15)
 
            Tcreditnotelist_AddNewOBJ.save()
            salesbillid = Tcreditnotelist_AddNewOBJ.salesbillid

            return   redirect('CreditNoteListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/CreditNoteListAdd.html",
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
def CreditNoteListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tcreditnotedetailslist_list.salesbillid
    
    # if Tcreditnotedetailslist_list:
    #     for Tcreditnotedetailslist_listQ in Tcreditnotedetailslist_list:
    #         lDetId = Tcreditnotedetailslist_listQ['salesbillid']

    Tcreditnotelist_listOBJ =  Tcreditnotedetailslist.objects.get(salesordermultiid=lID).delete()
          


    TcreditnotelistSave_list = Tcreditnotelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tcreditnotedetailslist_listG = Tcreditnotedetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0


                

    if Tcreditnotedetailslist_listG:
        for Tcreditnotedetailslist_listGT in Tcreditnotedetailslist_listG:
            dtotal =dtotal + float(Tcreditnotedetailslist_listGT['qty'] * Tcreditnotedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tcreditnotedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tcreditnotedetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tcreditnotedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tcreditnotedetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tcreditnotedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tcreditnotedetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tcreditnotedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tcreditnotedetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tcreditnotedetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Tcreditnotedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TcreditnotelistSave_list.dtotal = dtotal
    TcreditnotelistSave_list.dgsttrate = dcgst1pt0

    TcreditnotelistSave_list.dsgst0 = 0
    TcreditnotelistSave_list.dcgst0 = 0 
    TcreditnotelistSave_list.digst0 = 0 




    TcreditnotelistSave_list.dcgst01 = 0 
    TcreditnotelistSave_list.dcgst5 = 0 
    TcreditnotelistSave_list.dcgst12 = 0 
    TcreditnotelistSave_list.dcgst18 = 0 
    TcreditnotelistSave_list.dcgst28 = 0 

    TcreditnotelistSave_list.dcgst01 = 0 
    TcreditnotelistSave_list.dsgst5 = 0 
    TcreditnotelistSave_list.dsgst12 = 0 
    TcreditnotelistSave_list.dsgst18 = 0 
    TcreditnotelistSave_list.dsgst28 = 0 
 

    TcreditnotelistSave_list.dsgst01 = dsgst01 
    TcreditnotelistSave_list.dsgst5 = dsgst5 
    TcreditnotelistSave_list.dsgst12 = dsgst12 
    TcreditnotelistSave_list.dsgst18 = dsgst18 
    TcreditnotelistSave_list.dsgst28 = dsgst28  

    TcreditnotelistSave_list.dcgst01 =dcgst01 
    TcreditnotelistSave_list.dcgst5 = dcgst5 
    TcreditnotelistSave_list.dcgst12 =dcgst12
    TcreditnotelistSave_list.dcgst18 = dcgst18 
    TcreditnotelistSave_list.dcgst28 = dcgst28

    TcreditnotelistSave_list.dtotalfinal = dtotalfinal
    TcreditnotelistSave_list.dtotalfinal = dtotalfinal
    TcreditnotelistSave_list.swords = swords.upper()  


    TcreditnotelistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('CreditNoteListDetails', lID=lDetId)  


@csrf_exempt
def CreditNoteListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
                        
                        
                        TcreditnotelistSave_list = Tcreditnotelist.objects.get(salesbillid=lID) 

                        TcreditnotelistSave_list.customerid = customerid
                        TcreditnotelistSave_list.customername = customername
                        TcreditnotelistSave_list.saddressclient = saddressclient
                        TcreditnotelistSave_list.scustomerpan = scustomerpan
                        TcreditnotelistSave_list.scustomergst = scustomergst
                        TcreditnotelistSave_list.sstatecode = sstatecode
                        TcreditnotelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tcreditnotelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
                Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/CreditNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tcreditnotelist_list' : Tcreditnotelist_list,
                                    'Tcreditnotedetailslist_list' : Tcreditnotedetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TcreditnotelistSave_list = Tcreditnotelist.objects.get(salesbillid=lID) 

                        TcreditnotelistSave_list.customersiteid = customersiteid
                        TcreditnotelistSave_list.customernamesite = customernamesite
                        TcreditnotelistSave_list.saddresssite = saddresssite 
                        

                        TcreditnotelistSave_list.spinsite = MsitelistGet.sstatecode
                        TcreditnotelistSave_list.sstatesite = MsitelistGet.stempname1
                        TcreditnotelistSave_list.scitysite = MsitelistGet.stempname2



                        TcreditnotelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tcreditnotelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
            Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tcreditnotelist_list.customerid).values() 
            
            return render(request, "BillingSol/CreditNoteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tcreditnotelist_list' : Tcreditnotelist_list,
                            'Tcreditnotedetailslist_list' : Tcreditnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TcreditnotelistSave_list = Tcreditnotelist.objects.get(salesbillid=lID) 

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
                           
                        TcreditnotelistSave_list.spinsite = MsitelistGet.sstatecode
                        TcreditnotelistSave_list.sstatesite = MsitelistGet.stempname1
                        TcreditnotelistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

                sdate1=data.get('txTcreditnoteDate') 
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


                TcreditnotelistSave_list.ackdate1 = ackdate1
                TcreditnotelistSave_list.ackdate = ackdate
                TcreditnotelistSave_list.ewaydate1 = ewaydate1
                TcreditnotelistSave_list.ewaydate = ewaydate
                TcreditnotelistSave_list.sdate1 = sdate1
                TcreditnotelistSave_list.sdate = sdate
                TcreditnotelistSave_list.podate1 = podate1
                TcreditnotelistSave_list.podate = podate
                TcreditnotelistSave_list.sworkfrom = sworkfrom
                TcreditnotelistSave_list.sfromdate = sfromdate
                TcreditnotelistSave_list.sworkfto = sworkfto
                TcreditnotelistSave_list.stodate = stodate
                TcreditnotelistSave_list.sworkfto = sworkfto
                TcreditnotelistSave_list.inrno = inrno
                TcreditnotelistSave_list.ackno = ackno
                TcreditnotelistSave_list.ewayno = ewayno
                TcreditnotelistSave_list.scategoryofservice = scategoryofservice
                TcreditnotelistSave_list.stype1 = stype1
                TcreditnotelistSave_list.sinvoicerefno = sinvoicerefno
                TcreditnotelistSave_list.pono = pono
                TcreditnotelistSave_list.note1 = note1 

                TcreditnotelistSave_list.customerid = customerid
                TcreditnotelistSave_list.customername = customername
                TcreditnotelistSave_list.saddressclient = saddressclient
                TcreditnotelistSave_list.scustomerpan = scustomerpan
                TcreditnotelistSave_list.scustomergst = scustomergst
                TcreditnotelistSave_list.sstatecode = sstatecode
                
                TcreditnotelistSave_list.customersiteid = customersiteid
                TcreditnotelistSave_list.customernamesite = customernamesite
                TcreditnotelistSave_list.saddresssite = saddresssite 
                TcreditnotelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tcreditnotelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
                Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/CreditNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tcreditnotelist_list' : Tcreditnotelist_list,
                                    'Tcreditnotedetailslist_list' : Tcreditnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/CreditNoteListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tcreditnotedetailslist_listG = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 

            TcreditnotelistSave_list = Tcreditnotelist.objects.get(salesbillid=lID) 

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
                           
                        TcreditnotelistSave_list.spinsite = MsitelistGet.sstatecode
                        TcreditnotelistSave_list.sstatesite = MsitelistGet.stempname1
                        TcreditnotelistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

                sdate1=data.get('txTcreditnoteDate') 
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


                dcgst1pt00 =float(unitprice) * float(qty)
                ltaxrate=float(ltaxrate)
                dsgst01=ltaxrate
                ltaxrateamt =dcgst1pt00 * ltaxrate/100
                dcgst1pt0 = ltaxrateamt
                if(ltaxrate == 0):
                    dcgst01 =0
                elif(ltaxrate == 5):
                    dcgst5 =ltaxrateamt 
                    if(TcreditnotelistSave_list.sstatecode == TcreditnotelistSave_list.slocationstatecode):
                        dsgst5 = dcgst5/2
                    else:
                       dcgst50  =ltaxrateamt
                elif(ltaxrate == 12):
                    dcgst12 =ltaxrateamt 
                    if(TcreditnotelistSave_list.sstatecode == TcreditnotelistSave_list.slocationstatecode):
                        dsgst12 = dcgst12/2
                    else:
                       dcgst120  =ltaxrateamt
                elif(ltaxrate == 18):
                    dcgst18 =ltaxrateamt 
                    if(TcreditnotelistSave_list.sstatecode == TcreditnotelistSave_list.slocationstatecode):
                        dsgst18 = dcgst18/2
                    else:
                       dcgst180  =ltaxrateamt
                elif(ltaxrate == 28):
                    dcgst28 =ltaxrateamt 
                    if(TcreditnotelistSave_list.sstatecode == TcreditnotelistSave_list.slocationstatecode):
                        dsgst28 = dcgst28/2
                    else:
                       dcgst280  =ltaxrateamt


                    

                ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



                
                Tcreditnotedetailslist_AddNewOBJ = Tcreditnotedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)
    
                Tcreditnotedetailslist_AddNewOBJ.save()

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
                dcgst1pt0=0
                

                            

                if Tcreditnotedetailslist_listG:
                    for Tcreditnotedetailslist_listGT in Tcreditnotedetailslist_listG:
                        dtotal =dtotal + float(Tcreditnotedetailslist_listGT['qty'] * Tcreditnotedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tcreditnotedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tcreditnotedetailslist_listGT['dcgst5'])
                        dsgst5 =dsgst5 + float(Tcreditnotedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tcreditnotedetailslist_listGT['dcgst12'])
                        dsgst12 =dsgst12 + float(Tcreditnotedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tcreditnotedetailslist_listGT['dcgst18'])
                        dsgst18 =dsgst18 + float(Tcreditnotedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tcreditnotedetailslist_listGT['dcgst28'])
                        dsgst28 =dsgst28 + float(Tcreditnotedetailslist_listGT['dsgst28'])
                        dcgst1pt0=dcgst1pt0 + float(Tcreditnotedetailslist_listGT['dcgst1pt0']) 
                        
                        dtotalfinal =dtotalfinal + float(Tcreditnotedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TcreditnotelistSave_list.dtotal = dtotal
                TcreditnotelistSave_list.dgsttrate = dcgst1pt0

                TcreditnotelistSave_list.dsgst0 = 0
                TcreditnotelistSave_list.dcgst0 = 0 
                TcreditnotelistSave_list.digst0 = 0 

 


                TcreditnotelistSave_list.dcgst01 = 0 
                TcreditnotelistSave_list.dcgst5 = 0 
                TcreditnotelistSave_list.dcgst12 = 0 
                TcreditnotelistSave_list.dcgst18 = 0 
                TcreditnotelistSave_list.dcgst28 = 0 

                TcreditnotelistSave_list.dcgst01 = 0 
                TcreditnotelistSave_list.dsgst5 = 0 
                TcreditnotelistSave_list.dsgst12 = 0 
                TcreditnotelistSave_list.dsgst18 = 0 
                TcreditnotelistSave_list.dsgst28 = 0 
  

                TcreditnotelistSave_list.dsgst01 = dsgst01 
                TcreditnotelistSave_list.dsgst5 = dsgst5 
                TcreditnotelistSave_list.dsgst12 = dsgst12 
                TcreditnotelistSave_list.dsgst18 = dsgst18 
                TcreditnotelistSave_list.dsgst28 = dsgst28 

                TcreditnotelistSave_list.dcgst01 =dcgst01 
                TcreditnotelistSave_list.dcgst5 = dcgst5 
                TcreditnotelistSave_list.dcgst12 =dcgst12
                TcreditnotelistSave_list.dcgst18 = dcgst18 
                TcreditnotelistSave_list.dcgst28 = dcgst28

                TcreditnotelistSave_list.dtotalfinal = dtotalfinal
                TcreditnotelistSave_list.dtotalfinal = dtotalfinal
                TcreditnotelistSave_list.swords = swords.upper()  

                TcreditnotelistSave_list.ackdate1 = ackdate1
                TcreditnotelistSave_list.ackdate = ackdate
                TcreditnotelistSave_list.ewaydate1 = ewaydate1
                TcreditnotelistSave_list.ewaydate = ewaydate
                TcreditnotelistSave_list.sdate1 = sdate1
                TcreditnotelistSave_list.sdate = sdate
                TcreditnotelistSave_list.podate1 = podate1
                TcreditnotelistSave_list.podate = podate
                TcreditnotelistSave_list.sworkfrom = sworkfrom
                TcreditnotelistSave_list.sfromdate = sfromdate
                TcreditnotelistSave_list.sworkfto = sworkfto
                TcreditnotelistSave_list.stodate = stodate
                TcreditnotelistSave_list.sworkfto = sworkfto
                TcreditnotelistSave_list.inrno = inrno
                TcreditnotelistSave_list.ackno = ackno
                TcreditnotelistSave_list.ewayno = ewayno
                TcreditnotelistSave_list.scategoryofservice = scategoryofservice
                TcreditnotelistSave_list.stype1 = stype1
                TcreditnotelistSave_list.sinvoicerefno = sinvoicerefno
                TcreditnotelistSave_list.pono = pono
                TcreditnotelistSave_list.note1 = note1 

                TcreditnotelistSave_list.customerid = customerid
                TcreditnotelistSave_list.customername = customername
                TcreditnotelistSave_list.saddressclient = saddressclient
                TcreditnotelistSave_list.scustomerpan = scustomerpan
                TcreditnotelistSave_list.scustomergst = scustomergst
                TcreditnotelistSave_list.sstatecode = sstatecode
                
                TcreditnotelistSave_list.customersiteid = customersiteid
                TcreditnotelistSave_list.customernamesite = customernamesite
                TcreditnotelistSave_list.saddresssite = saddresssite 
                TcreditnotelistSave_list.swords= swords.upper()
                TcreditnotelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tcreditnotelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
                Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/CreditNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tcreditnotelist_list' : Tcreditnotelist_list,
                                    'Tcreditnotedetailslist_list' : Tcreditnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tcreditnotelist_list = Tcreditnotelist.objects.get(salesbillid=lID) 
        Tcreditnotedetailslist_list = Tcreditnotedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tcreditnotelist_list.customerid).values() 
          
        return render(request, "BillingSol/CreditNoteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tcreditnotelist_list' : Tcreditnotelist_list,
                            'Tcreditnotedetailslist_list' : Tcreditnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

@csrf_exempt
def DebitNoteList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('DebitNoteListAdd')  
        
    else:
        
        Tdebitnotelist_list = Tdebitnotelist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tdebitnotelist_list.count()
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
        paginator = Paginator(Tdebitnotelist_list, lRecCount1)
        try:
            Tdebitnotelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tdebitnotelist_lists = paginator.page(1)
        except EmptyPage:
            Tdebitnotelist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/DebitNoteList.html",
                    {
                        'Tdebitnotelist_list':Tdebitnotelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def DebitNoteListAdd(request):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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

            return   redirect('DebitNoteList') 

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

                        salesbillno=McompanylistGet.linvoice9 + 1
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
                        sinvoicerefno=McompanylistGet.sformat9 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice9 = salesbillno
                        Mcompanylist_AddNewOBJ.lyear = finyear 
                        
                        Mcompanylist_AddNewOBJ.save()


            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    MsupplierlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if MsupplierlistGet:
                        customername = MsupplierlistGet.suppliername 
                        saddressclient = MsupplierlistGet.address1 + " " + MsupplierlistGet.address2 + " " + MsupplierlistGet.address3 + " " + MsupplierlistGet.scity + " " + MsupplierlistGet.lpin + " " + MsupplierlistGet.sstate
                         
                        scustomerpan=MsupplierlistGet.panno
                        scustomergst=MsupplierlistGet.gstno
                        sstatecode=MsupplierlistGet.sstatecode
            
            
            Tdebitnotelist_AddNewOBJ = Tdebitnotelist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15)
 
            Tdebitnotelist_AddNewOBJ.save()
            salesbillid = Tdebitnotelist_AddNewOBJ.salesbillid

            return   redirect('DebitNoteListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')              
        return render(request, "BillingSol/DebitNoteListAdd.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Mcompanylistlist_list' : Mcompanylistlist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 


  
@csrf_exempt
def DebitNoteListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tdebitnotedetailslist_list.salesbillid
    
    # if Tdebitnotedetailslist_list:
    #     for Tdebitnotedetailslist_listQ in Tdebitnotedetailslist_list:
    #         lDetId = Tdebitnotedetailslist_listQ['salesbillid']

    Tdebitnotelist_listOBJ =  Tdebitnotedetailslist.objects.get(salesordermultiid=lID).delete()
          


    TdebitnotelistSave_list = Tdebitnotelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tdebitnotedetailslist_listG = Tdebitnotedetailslist.objects.filter(salesbillid=lDetId).values() 

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
    dcgst1pt0=0

                

    if Tdebitnotedetailslist_listG:
        for Tdebitnotedetailslist_listGT in Tdebitnotedetailslist_listG:
            dtotal =dtotal + float(Tdebitnotedetailslist_listGT['qty'] * Tdebitnotedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tdebitnotedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tdebitnotedetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tdebitnotedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tdebitnotedetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tdebitnotedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tdebitnotedetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tdebitnotedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tdebitnotedetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tdebitnotedetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tdebitnotedetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Tdebitnotedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TdebitnotelistSave_list.dtotal = dtotal
    TdebitnotelistSave_list.dgsttrate = dcgst1pt0

    TdebitnotelistSave_list.dsgst0 = 0
    TdebitnotelistSave_list.dcgst0 = 0 
    TdebitnotelistSave_list.digst0 = 0 




    TdebitnotelistSave_list.dcgst01 = 0 
    TdebitnotelistSave_list.dcgst5 = 0 
    TdebitnotelistSave_list.dcgst12 = 0 
    TdebitnotelistSave_list.dcgst18 = 0 
    TdebitnotelistSave_list.dcgst28 = 0 

    TdebitnotelistSave_list.dcgst01 = 0 
    TdebitnotelistSave_list.dsgst5 = 0 
    TdebitnotelistSave_list.dsgst12 = 0 
    TdebitnotelistSave_list.dsgst18 = 0 
    TdebitnotelistSave_list.dsgst28 = 0 
 

    TdebitnotelistSave_list.dsgst01 = dsgst01 
    TdebitnotelistSave_list.dsgst5 = dsgst5 
    TdebitnotelistSave_list.dsgst12 = dsgst12 
    TdebitnotelistSave_list.dsgst18 = dsgst18 
    TdebitnotelistSave_list.dsgst28 = dsgst28  

    TdebitnotelistSave_list.dcgst01 =dcgst01 
    TdebitnotelistSave_list.dcgst5 = dcgst5 
    TdebitnotelistSave_list.dcgst12 =dcgst12
    TdebitnotelistSave_list.dcgst18 = dcgst18 
    TdebitnotelistSave_list.dcgst28 = dcgst28

    TdebitnotelistSave_list.dtotalfinal = dtotalfinal
    TdebitnotelistSave_list.dtotalfinal = dtotalfinal
    TdebitnotelistSave_list.swords = swords.upper()  


    TdebitnotelistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('DebitNoteListDetails', lID=lDetId)  


@csrf_exempt
def DebitNoteListDetails(request,lID):
    
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
    scategoryofservice=""
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
    ddateofedit=datetime.today().strftime('%d-%m-%Y')
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
    saddressclient1=""
    saddresssite1=""
    scompanyaddress1=""
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
    sworkfrom=datetime.today().strftime('%Y-%m-%d')
    sworkfto=datetime.today().strftime('%Y-%m-%d')
    bsitesez=0
    ackdate=datetime.today().strftime('%d-%m-%Y')
    ackdate1=datetime.today().strftime('%Y-%m-%d')
    podate1=datetime.today().strftime('%Y-%m-%d')
    bsamestate=0
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
                    MsupplierlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if MsupplierlistGet:
                        customername = MsupplierlistGet.suppliername 
                        saddressclient = MsupplierlistGet.address1 + " " + MsupplierlistGet.address2 + " " + MsupplierlistGet.address3 + " " + MsupplierlistGet.scity + " " + MsupplierlistGet.lpin + " " + MsupplierlistGet.sstate
                         
                        scustomerpan=MsupplierlistGet.panno
                        scustomergst=MsupplierlistGet.gstno
                        sstatecode=MsupplierlistGet.sstatecode
            
 
                        
                        
                        TdebitnotelistSave_list = Tdebitnotelist.objects.get(salesbillid=lID) 

                        TdebitnotelistSave_list.customerid = customerid
                        TdebitnotelistSave_list.customername = customername
                        TdebitnotelistSave_list.saddressclient = saddressclient
                        TdebitnotelistSave_list.scustomerpan = scustomerpan
                        TdebitnotelistSave_list.scustomergst = scustomergst
                        TdebitnotelistSave_list.sstatecode = sstatecode
                        TdebitnotelistSave_list.save()


                Msupplierlist_list = Msupplierlist.objects.order_by('suppliername') 
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdebitnotelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
                Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DebitNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Msupplierlist_list' : Msupplierlist_list,
                                    'Tdebitnotelist_list' : Tdebitnotelist_list,
                                    'Tdebitnotedetailslist_list' : Tdebitnotedetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TdebitnotelistSave_list = Tdebitnotelist.objects.get(salesbillid=lID) 

                        TdebitnotelistSave_list.customersiteid = customersiteid
                        TdebitnotelistSave_list.customernamesite = customernamesite
                        TdebitnotelistSave_list.saddresssite = saddresssite 
                        

                        TdebitnotelistSave_list.spinsite = MsitelistGet.sstatecode
                        TdebitnotelistSave_list.sstatesite = MsitelistGet.stempname1
                        TdebitnotelistSave_list.scitysite = MsitelistGet.stempname2



                        TdebitnotelistSave_list.save()


                
            Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')   
    

            Tdebitnotelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
            Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tdebitnotelist_list.customerid).values() 
            
            return render(request, "BillingSol/DebitNoteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'Tdebitnotelist_list' : Tdebitnotelist_list,
                            'Tdebitnotedetailslist_list' : Tdebitnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TdebitnotelistSave_list = Tdebitnotelist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    MsupplierlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if MsupplierlistGet:
                        customername = MsupplierlistGet.suppliername 
                        saddressclient = MsupplierlistGet.address1 + " " + MsupplierlistGet.address2 + " " + MsupplierlistGet.address3 + " " + MsupplierlistGet.scity + " " + MsupplierlistGet.lpin + " " + MsupplierlistGet.sstate
                         
                        scustomerpan=MsupplierlistGet.panno
                        scustomergst=MsupplierlistGet.gstno
                        sstatecode=MsupplierlistGet.sstatecode
            
 
                         

            # customersiteid =0
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TdebitnotelistSave_list.spinsite = MsitelistGet.sstatecode
            #             TdebitnotelistSave_list.sstatesite = MsitelistGet.stempname1
            #             TdebitnotelistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

                sdate1=data.get('txTdebitnoteDate') 
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


                TdebitnotelistSave_list.ackdate1 = ackdate1
                TdebitnotelistSave_list.ackdate = ackdate
                TdebitnotelistSave_list.ewaydate1 = ewaydate1
                TdebitnotelistSave_list.ewaydate = ewaydate
                TdebitnotelistSave_list.sdate1 = sdate1
                TdebitnotelistSave_list.sdate = sdate
                TdebitnotelistSave_list.podate1 = podate1
                TdebitnotelistSave_list.podate = podate
                TdebitnotelistSave_list.sworkfrom = sworkfrom
                TdebitnotelistSave_list.sfromdate = sfromdate
                TdebitnotelistSave_list.sworkfto = sworkfto
                TdebitnotelistSave_list.stodate = stodate
                TdebitnotelistSave_list.sworkfto = sworkfto
                TdebitnotelistSave_list.inrno = inrno
                TdebitnotelistSave_list.ackno = ackno
                TdebitnotelistSave_list.ewayno = ewayno
                TdebitnotelistSave_list.scategoryofservice = scategoryofservice
                TdebitnotelistSave_list.stype1 = stype1
                TdebitnotelistSave_list.sinvoicerefno = sinvoicerefno
                TdebitnotelistSave_list.pono = pono
                TdebitnotelistSave_list.note1 = note1 

                TdebitnotelistSave_list.customerid = customerid
                TdebitnotelistSave_list.customername = customername
                TdebitnotelistSave_list.saddressclient = saddressclient
                TdebitnotelistSave_list.scustomerpan = scustomerpan
                TdebitnotelistSave_list.scustomergst = scustomergst
                TdebitnotelistSave_list.sstatecode = sstatecode
                
                TdebitnotelistSave_list.customersiteid = customersiteid
                TdebitnotelistSave_list.customernamesite = customernamesite
                TdebitnotelistSave_list.saddresssite = saddresssite 
                TdebitnotelistSave_list.save()
                

                Msupplierlist_list = Msupplierlist.objects.order_by('suppliername') 
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdebitnotelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
                Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DebitNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Msupplierlist_list' : Msupplierlist_list,
                                    'Tdebitnotelist_list' : Tdebitnotelist_list,
                                    'Tdebitnotedetailslist_list' : Tdebitnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/DebitNoteListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tdebitnotedetailslist_listG = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 

            TdebitnotelistSave_list = Tdebitnotelist.objects.get(salesbillid=lID) 

            customerid =0
            if 'cmbClient' in request.POST: 
                if(data.get('cmbClient').isnumeric()):
                    customerid = int(data.get('cmbClient'))
                    MsupplierlistGet = Msupplierlist.objects.get(supplierid=customerid) 
                    if MsupplierlistGet:
                        customername = MsupplierlistGet.suppliername 
                        saddressclient = MsupplierlistGet.address1 + " " + MsupplierlistGet.address2 + " " + MsupplierlistGet.address3 + " " + MsupplierlistGet.scity + " " + MsupplierlistGet.lpin + " " + MsupplierlistGet.sstate
                         
                        scustomerpan=MsupplierlistGet.panno
                        scustomergst=MsupplierlistGet.gstno
                        sstatecode=MsupplierlistGet.sstatecode
            
 
                         

            # customersiteid =0
            # if 'cmbSite' in request.POST: 
            #     if(data.get('cmbSite').isnumeric()):
            #         customersiteid = int(data.get('cmbSite'))
            #         MsitelistGet = Msitelist.objects.get(lcontactdetailnoid=customersiteid) 
            #         if MsitelistGet:
            #             customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
            #             saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                           
            #             TdebitnotelistSave_list.spinsite = MsitelistGet.sstatecode
            #             TdebitnotelistSave_list.sstatesite = MsitelistGet.stempname1
            #             TdebitnotelistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

                sdate1=data.get('txTdebitnoteDate') 
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


                dcgst1pt00 =float(unitprice) * float(qty)
                ltaxrate=float(ltaxrate)
                dsgst01=ltaxrate
                ltaxrateamt =dcgst1pt00 * ltaxrate/100
                dcgst1pt0 = ltaxrateamt
                if(ltaxrate == 0):
                    dcgst01 =0
                elif(ltaxrate == 5):
                    dcgst5 =ltaxrateamt 
                    if(TdebitnotelistSave_list.sstatecode == TdebitnotelistSave_list.slocationstatecode):
                        dsgst5 = dcgst5/2
                    else:
                       dcgst50  =ltaxrateamt
                elif(ltaxrate == 12):
                    dcgst12 =ltaxrateamt 
                    if(TdebitnotelistSave_list.sstatecode == TdebitnotelistSave_list.slocationstatecode):
                        dsgst12 = dcgst12/2
                    else:
                       dcgst120  =ltaxrateamt
                elif(ltaxrate == 18):
                    dcgst18 =ltaxrateamt 
                    if(TdebitnotelistSave_list.sstatecode == TdebitnotelistSave_list.slocationstatecode):
                        dsgst18 = dcgst18/2
                    else:
                       dcgst180  =ltaxrateamt
                elif(ltaxrate == 28):
                    dcgst28 =ltaxrateamt 
                    if(TdebitnotelistSave_list.sstatecode == TdebitnotelistSave_list.slocationstatecode):
                        dsgst28 = dcgst28/2
                    else:
                       dcgst280  =ltaxrateamt


                    

                ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



                
                Tdebitnotedetailslist_AddNewOBJ = Tdebitnotedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)
    
                Tdebitnotedetailslist_AddNewOBJ.save()

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
                dcgst1pt0=0
                

                            

                if Tdebitnotedetailslist_listG:
                    for Tdebitnotedetailslist_listGT in Tdebitnotedetailslist_listG:
                        dtotal =dtotal + float(Tdebitnotedetailslist_listGT['qty'] * Tdebitnotedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tdebitnotedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tdebitnotedetailslist_listGT['dcgst5'])
                        dsgst5 =dsgst5 + float(Tdebitnotedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tdebitnotedetailslist_listGT['dcgst12'])
                        dsgst12 =dsgst12 + float(Tdebitnotedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tdebitnotedetailslist_listGT['dcgst18'])
                        dsgst18 =dsgst18 + float(Tdebitnotedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tdebitnotedetailslist_listGT['dcgst28'])
                        dsgst28 =dsgst28 + float(Tdebitnotedetailslist_listGT['dsgst28'])
                        dcgst1pt0=dcgst1pt0 + float(Tdebitnotedetailslist_listGT['dcgst1pt0']) 
                        
                        dtotalfinal =dtotalfinal + float(Tdebitnotedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TdebitnotelistSave_list.dtotal = dtotal
                TdebitnotelistSave_list.dgsttrate = dcgst1pt0

                TdebitnotelistSave_list.dsgst0 = 0
                TdebitnotelistSave_list.dcgst0 = 0 
                TdebitnotelistSave_list.digst0 = 0 

 


                TdebitnotelistSave_list.dcgst01 = 0 
                TdebitnotelistSave_list.dcgst5 = 0 
                TdebitnotelistSave_list.dcgst12 = 0 
                TdebitnotelistSave_list.dcgst18 = 0 
                TdebitnotelistSave_list.dcgst28 = 0 

                TdebitnotelistSave_list.dcgst01 = 0 
                TdebitnotelistSave_list.dsgst5 = 0 
                TdebitnotelistSave_list.dsgst12 = 0 
                TdebitnotelistSave_list.dsgst18 = 0 
                TdebitnotelistSave_list.dsgst28 = 0 
 

                TdebitnotelistSave_list.dsgst01 = dsgst01 
                TdebitnotelistSave_list.dsgst5 = dsgst5 
                TdebitnotelistSave_list.dsgst12 = dsgst12 
                TdebitnotelistSave_list.dsgst18 = dsgst18 
                TdebitnotelistSave_list.dsgst28 = dsgst28  

                TdebitnotelistSave_list.dcgst01 =dcgst01 
                TdebitnotelistSave_list.dcgst5 = dcgst5 
                TdebitnotelistSave_list.dcgst12 =dcgst12
                TdebitnotelistSave_list.dcgst18 = dcgst18 
                TdebitnotelistSave_list.dcgst28 = dcgst28

                TdebitnotelistSave_list.dtotalfinal = dtotalfinal
                TdebitnotelistSave_list.dtotalfinal = dtotalfinal
                TdebitnotelistSave_list.swords = swords.upper()  

                TdebitnotelistSave_list.ackdate1 = ackdate1
                TdebitnotelistSave_list.ackdate = ackdate
                TdebitnotelistSave_list.ewaydate1 = ewaydate1
                TdebitnotelistSave_list.ewaydate = ewaydate
                TdebitnotelistSave_list.sdate1 = sdate1
                TdebitnotelistSave_list.sdate = sdate
                TdebitnotelistSave_list.podate1 = podate1
                TdebitnotelistSave_list.podate = podate
                TdebitnotelistSave_list.sworkfrom = sworkfrom
                TdebitnotelistSave_list.sfromdate = sfromdate
                TdebitnotelistSave_list.sworkfto = sworkfto
                TdebitnotelistSave_list.stodate = stodate
                TdebitnotelistSave_list.sworkfto = sworkfto
                TdebitnotelistSave_list.inrno = inrno
                TdebitnotelistSave_list.ackno = ackno
                TdebitnotelistSave_list.ewayno = ewayno
                TdebitnotelistSave_list.scategoryofservice = scategoryofservice
                TdebitnotelistSave_list.stype1 = stype1
                TdebitnotelistSave_list.sinvoicerefno = sinvoicerefno
                TdebitnotelistSave_list.pono = pono
                TdebitnotelistSave_list.note1 = note1 

                TdebitnotelistSave_list.customerid = customerid
                TdebitnotelistSave_list.customername = customername
                TdebitnotelistSave_list.saddressclient = saddressclient
                TdebitnotelistSave_list.scustomerpan = scustomerpan
                TdebitnotelistSave_list.scustomergst = scustomergst
                TdebitnotelistSave_list.sstatecode = sstatecode
                
                TdebitnotelistSave_list.customersiteid = customersiteid
                TdebitnotelistSave_list.customernamesite = customernamesite
                TdebitnotelistSave_list.saddresssite = saddresssite 
                TdebitnotelistSave_list.swords= swords.upper()
                TdebitnotelistSave_list.save()
                

                Msupplierlist_list = Msupplierlist.objects.order_by('suppliername') 
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tdebitnotelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
                Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/DebitNoteListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Msupplierlist_list' : Msupplierlist_list,
                                    'Tdebitnotelist_list' : Tdebitnotelist_list,
                                    'Tdebitnotedetailslist_list' : Tdebitnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 




    else:   
        
        Msupplierlist_list = Msupplierlist.objects.order_by('suppliername')   
  

        Tdebitnotelist_list = Tdebitnotelist.objects.get(salesbillid=lID) 
        Tdebitnotedetailslist_list = Tdebitnotedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tdebitnotelist_list.customerid).values() 
          
        return render(request, "BillingSol/DebitNoteListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Msupplierlist_list' : Msupplierlist_list,
                            'Tdebitnotelist_list' : Tdebitnotelist_list,
                            'Tdebitnotedetailslist_list' : Tdebitnotedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 









    
@csrf_exempt
def RentInvoiceList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('RentInvoiceListAdd')  
        
    else:
        
        Trentinvoicelist_list = Trentinvoicelist.objects.order_by('-invoicedate', '-salesbillno')  


        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Trentinvoicelist_list.count()
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
        paginator = Paginator(Trentinvoicelist_list, lRecCount1)
        try:
            Trentinvoicelist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Trentinvoicelist_lists = paginator.page(1)
        except EmptyPage:
            Trentinvoicelist_lists = paginator.page(paginator.num_pages)


        return render(request, "BillingSol/RentInvoiceList.html",
                    {
                        'Trentinvoicelist_list':Trentinvoicelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def RentInvoiceListAdd(request):

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

            return   redirect('RentInvoiceList') 

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
                        sinvoicerefno=McompanylistGet.sformat11 + ssalesbillno + McompanylistGet.sformat 



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
            
            Trentinvoicelist_AddNewOBJ = Trentinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
            Trentinvoicelist_AddNewOBJ.save()
            salesbillid = Trentinvoicelist_AddNewOBJ.salesbillid

            return   redirect('RentInvoiceListDetails', lID=salesbillid)  
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/RentInvoiceListAdd.html",
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
def RentInvoiceListDetailsDelete(request,lID):
    lCatID = 0
    
    lDetId =0

    Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Trentinvoicedetailslist_list.salesbillid
    
    # if Trentinvoicedetailslist_list:
    #     for Trentinvoicedetailslist_listQ in Trentinvoicedetailslist_list:
    #         lDetId = Trentinvoicedetailslist_listQ['salesbillid']

    Trentinvoicelist_listOBJ =  Trentinvoicedetailslist.objects.get(salesordermultiid=lID).delete()
          


    Trentinvoicelist_listSave = Trentinvoicelist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Trentinvoicedetailslist_listG = Trentinvoicedetailslist.objects.filter(salesbillid=lDetId).values() 



    if Trentinvoicedetailslist_listG:
        for Trentinvoicedetailslist_listGT in Trentinvoicedetailslist_listG:
            dtotal =dtotal + float(Trentinvoicedetailslist_listGT['ddescitemtotal'])
            ltaxrateamt =ltaxrateamt + float(Trentinvoicedetailslist_listGT['ltaxrateamt'])
            digst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt'])
            dsgst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt1'])
            dcgst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt2']) 
            dtotalfinal =dtotalfinal + float(Trentinvoicedetailslist_listGT['dtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    Trentinvoicelist_listSave.dtotal = dtotal
    Trentinvoicelist_listSave.dgsttrate = ltaxrateamt

    Trentinvoicelist_listSave.dsgst0 = 0
    Trentinvoicelist_listSave.dcgst0 = 0 
    Trentinvoicelist_listSave.digst0 = 0
    if(Trentinvoicelist_listSave.sstatecode == Trentinvoicelist_listSave.slocationstatecode):
        Trentinvoicelist_listSave.dsgst0 = ltaxrateamt/2
        Trentinvoicelist_listSave.dcgst0 = ltaxrateamt/2 
    else:
        Trentinvoicelist_listSave.digst0 = ltaxrateamt

    Trentinvoicelist_listSave.dtotalfinal = dtotalfinal
    Trentinvoicelist_listSave.dtotalfinal = dtotalfinal
    Trentinvoicelist_listSave.swords= swords.upper()

 
    Trentinvoicelist_listSave.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('RentInvoiceListDetails', lID=lDetId)  


  
@csrf_exempt
def RentInvoiceListCopyDetails(request,lID):
    
    
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
 

    Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 

    customerid=Trentinvoicelist_list.customerid
    customername=Trentinvoicelist_list.customername
    saddress1=Trentinvoicelist_list.saddress1
    saddress2=Trentinvoicelist_list.saddress2
    saddress3=Trentinvoicelist_list.saddress3
    spin=Trentinvoicelist_list.spin
    scity=Trentinvoicelist_list.scity
    sstate=Trentinvoicelist_list.sstate
    scustomerpan=Trentinvoicelist_list.scustomerpan
    scustomergst=Trentinvoicelist_list.scustomergst
    customernamesite=Trentinvoicelist_list.customernamesite
    saddress1site=Trentinvoicelist_list.saddress1site
    saddress2site=Trentinvoicelist_list.saddress2site
    saddress3site=Trentinvoicelist_list.saddress3site
    spinsite=Trentinvoicelist_list.spinsite
    scitysite=Trentinvoicelist_list.scitysite
    sstatesite=Trentinvoicelist_list.sstatesite
    pono=Trentinvoicelist_list.pono
    podate=Trentinvoicelist_list.podate
    dtotal=Trentinvoicelist_list.dtotal
    dgsttrate=Trentinvoicelist_list.dgsttrate
    dgst=Trentinvoicelist_list.dgst
    dtotalfinal=Trentinvoicelist_list.dtotalfinal
    swords=Trentinvoicelist_list.swords
    sgstsplit=Trentinvoicelist_list.sgstsplit
    note1=Trentinvoicelist_list.note1
    note2=Trentinvoicelist_list.note2
    inr=Trentinvoicelist_list.inr
    scategoryofservice=Trentinvoicelist_list.scategoryofservice
    username=Trentinvoicelist_list.username
    stype1=Trentinvoicelist_list.stype1
    sfile1=Trentinvoicelist_list.sfile1
    sfolder1=Trentinvoicelist_list.sfolder1
    snumber1=Trentinvoicelist_list.snumber1
    customersiteid=Trentinvoicelist_list.customersiteid
    sstatecode=Trentinvoicelist_list.sstatecode
    sfromdate=Trentinvoicelist_list.sfromdate
    stodate=Trentinvoicelist_list.stodate
    dsgst0=Trentinvoicelist_list.dsgst0
    dcgst0=Trentinvoicelist_list.dcgst0
    digst0=Trentinvoicelist_list.digst0
    lnoofedit=Trentinvoicelist_list.lnoofedit
    ddateofedit=Trentinvoicelist_list.ddateofedit
    ldepartmentid=Trentinvoicelist_list.ldepartmentid
    sdepartmentname=Trentinvoicelist_list.sdepartmentname
    bdelete=Trentinvoicelist_list.bdelete
    bcancelcopy=Trentinvoicelist_list.bcancelcopy
    bapproval0=Trentinvoicelist_list.bapproval0
    bapproval01=Trentinvoicelist_list.bapproval01
    bapproval02=Trentinvoicelist_list.bapproval02
    bapproval03=Trentinvoicelist_list.bapproval03
    bapproval04=Trentinvoicelist_list.bapproval04
    bapproval05=Trentinvoicelist_list.bapproval05
    bapproval06=Trentinvoicelist_list.bapproval06
    bapproval07=Trentinvoicelist_list.bapproval07
    bapproval08=Trentinvoicelist_list.bapproval08
    bapproval09=Trentinvoicelist_list.bapproval09
    bapproval010=Trentinvoicelist_list.bapproval010
    scomments=Trentinvoicelist_list.scomments
    scommentsdelete=Trentinvoicelist_list.scommentsdelete
    lorderid=Trentinvoicelist_list.lorderid
    saddressclient=Trentinvoicelist_list.saddressclient
    saddresssite=Trentinvoicelist_list.saddresssite
    scompanyaddress=Trentinvoicelist_list.scompanyaddress
    llocationid=Trentinvoicelist_list.llocationid
    slocation=Trentinvoicelist_list.slocation
    slocationstatecode=Trentinvoicelist_list.slocationstatecode
    slocationgstno=Trentinvoicelist_list.slocationgstno
    slocationpanno=Trentinvoicelist_list.slocationpanno
    slocationformat=Trentinvoicelist_list.slocationformat
    bsitesez=Trentinvoicelist_list.bsitesez
    sworkfrom=Trentinvoicelist_list.sworkfrom
    sworkfto=Trentinvoicelist_list.sworkfto
    podate1=Trentinvoicelist_list.podate1
    bsamestate =Trentinvoicelist_list.bsamestate 




 
    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
    if McompanylistGet:
        slocation = McompanylistGet.scompanyname  
        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
            
        slocationgstno=McompanylistGet.sgstno 
        slocationpanno=McompanylistGet.spanno
        slocationstatecode=McompanylistGet.sstatecode

        salesbillno=McompanylistGet.linvoice11 + 1
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
        sinvoicerefno=McompanylistGet.sformat11 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice11 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            

    
    Trentinvoicelist_AddNewOBJ = Trentinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Trentinvoicelist_AddNewOBJ.save()
    salesbillid = Trentinvoicelist_AddNewOBJ.salesbillid
  

    Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Trentinvoicedetailslist_list:
        for Trentinvoicedetailslist_listQ in Trentinvoicedetailslist_list:
            sdesc=Trentinvoicedetailslist_listQ['sdesc']
            partid=Trentinvoicedetailslist_listQ['partid']
            partno=Trentinvoicedetailslist_listQ['partno']
            qty=Trentinvoicedetailslist_listQ['qty']
            unitprice=Trentinvoicedetailslist_listQ['unitprice']
            units=Trentinvoicedetailslist_listQ['units']
            ddescitemtotal=Trentinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Trentinvoicedetailslist_listQ['shsn']
            ssac=Trentinvoicedetailslist_listQ['ssac']
            smanrate=Trentinvoicedetailslist_listQ['smanrate']
            staxnotify=Trentinvoicedetailslist_listQ['staxnotify']
            ltaxrate=0	
            ltaxrateamt=0 	
            ltaxrateamt1=0	
            ltaxrateamt2=0
            ltaxrate=Trentinvoicedetailslist_listQ['ltaxrate']
            ltaxrateamt=Trentinvoicedetailslist_listQ['ltaxrateamt'] 	
            ltaxrateamt1=Trentinvoicedetailslist_listQ['ltaxrateamt1']	
            ltaxrateamt2=Trentinvoicedetailslist_listQ['ltaxrateamt2']

            
            Trentinvoicedetailslist_AddNewOBJ = Trentinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Trentinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('RentInvoiceListDetails', lID=salesbillid)  





@csrf_exempt
def RentInvoiceListDetails(request,lID):
    
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

            
            return   redirect('RentInvoiceList')  
        
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
                        
                        
                        TrentinvoicelistSave_list = Trentinvoicelist.objects.get(salesbillid=lID) 

                        TrentinvoicelistSave_list.customerid = customerid
                        TrentinvoicelistSave_list.customername = customername
                        TrentinvoicelistSave_list.saddressclient = saddressclient
                        TrentinvoicelistSave_list.scustomerpan = scustomerpan
                        TrentinvoicelistSave_list.scustomergst = scustomergst
                        TrentinvoicelistSave_list.sstatecode = sstatecode
                        TrentinvoicelistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
                Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/RentInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Trentinvoicelist_list' : Trentinvoicelist_list,
                                    'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list,
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
                        customernamesite = MsitelistGet.slocation  + " "  + MsitelistGet.splace 
                        saddresssite = MsitelistGet.address1 + " " + MsitelistGet.address2 + " " + MsitelistGet.address3 + " " + MsitelistGet.scity + " " + MsitelistGet.lpin + " " + MsitelistGet.sstate
                          
                        #sstatecode=MsitelistGet.sstatecode 
                        
                        
                        TrentinvoicelistSave_list = Trentinvoicelist.objects.get(salesbillid=lID) 

                        TrentinvoicelistSave_list.customersiteid = customersiteid
                        TrentinvoicelistSave_list.customernamesite = customernamesite
                        TrentinvoicelistSave_list.saddresssite = saddresssite 

                        TrentinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TrentinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TrentinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        TrentinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
            Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Trentinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/RentInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Trentinvoicelist_list' : Trentinvoicelist_list,
                            'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TrentinvoicelistSave_list = Trentinvoicelist.objects.get(salesbillid=lID) 

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
                            
                        TrentinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TrentinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TrentinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

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



                TrentinvoicelistSave_list.ackdate1 = ackdate1
                TrentinvoicelistSave_list.ackdate = ackdate
                TrentinvoicelistSave_list.ewaydate1 = ewaydate1
                TrentinvoicelistSave_list.ewaydate = ewaydate
                TrentinvoicelistSave_list.sdate1 = sdate1
                TrentinvoicelistSave_list.sdate = sdate
                TrentinvoicelistSave_list.podate1 = podate1
                TrentinvoicelistSave_list.podate = podate
                TrentinvoicelistSave_list.sworkfrom = sworkfrom
                TrentinvoicelistSave_list.sfromdate = sfromdate
                TrentinvoicelistSave_list.sworkfto = sworkfto
                TrentinvoicelistSave_list.stodate = stodate
                TrentinvoicelistSave_list.sworkfto = sworkfto
                TrentinvoicelistSave_list.inrno = inrno
                TrentinvoicelistSave_list.ackno = ackno
                TrentinvoicelistSave_list.ewayno = ewayno
                TrentinvoicelistSave_list.scategoryofservice = scategoryofservice
                TrentinvoicelistSave_list.stype1 = stype1
                TrentinvoicelistSave_list.sinvoicerefno = sinvoicerefno
                TrentinvoicelistSave_list.pono = pono
                TrentinvoicelistSave_list.note1 = note1 

                TrentinvoicelistSave_list.customerid = customerid
                TrentinvoicelistSave_list.customername = customername
                TrentinvoicelistSave_list.saddressclient = saddressclient
                TrentinvoicelistSave_list.scustomerpan = scustomerpan
                TrentinvoicelistSave_list.scustomergst = scustomergst
                TrentinvoicelistSave_list.sstatecode = sstatecode
                
                TrentinvoicelistSave_list.customersiteid = customersiteid
                TrentinvoicelistSave_list.customernamesite = customernamesite
                TrentinvoicelistSave_list.saddresssite = saddresssite  

                TrentinvoicelistSave_list.save()
                

                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
                Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/RentInvoiceListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Trentinvoicelist_list' : Trentinvoicelist_list,
                                    'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                                }
                                ) 



        if 'cmdPrint' in request.POST: 
 


            Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
            if(Trentinvoicelist_list.ackno != ""):
                if(len(Trentinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Trentinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Trentinvoicelist_list' : Trentinvoicelist_list,
                    'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/RentInvoiceListDetailsPrint.html', context)
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

            TrentinvoicelistSave_list = Trentinvoicelist.objects.get(salesbillid=lID) 
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
                           
                        TrentinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TrentinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TrentinvoicelistSave_list.scitysite = MsitelistGet.stempname2

                        
                        

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
            if(TrentinvoicelistSave_list.sstatecode == TrentinvoicelistSave_list.slocationstatecode):
                ltaxrateamt1 =ltaxrateamt/2
                ltaxrateamt1 =ltaxrateamt/2

            dtotal = round(ddescitemtotal + ltaxrateamt)


            
            Trentinvoicedetailslist_AddNewOBJ = Trentinvoicedetailslist(salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dtotal=dtotal, 	ltaxrate=ltaxrate, 	ltaxrateamt=ltaxrateamt, 	ltaxrateamt1=ltaxrateamt1, 	ltaxrateamt2=ltaxrateamt2)

            Trentinvoicedetailslist_AddNewOBJ.save()

            messages.success(request, 'Item is Added successfully!')


            Trentinvoicedetailslist_listG = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 

            ltaxrateamt =0
            digst0 = 0
            dsgst0 = 0
            dcgst0 = 0
            dgsttrate = 0
            dtotalfinal = 0
            dtotal=0

                        

            if Trentinvoicedetailslist_listG:
                for Trentinvoicedetailslist_listGT in Trentinvoicedetailslist_listG:
                    dtotal =dtotal + float(Trentinvoicedetailslist_listGT['ddescitemtotal'])
                    ltaxrateamt =ltaxrateamt + float(Trentinvoicedetailslist_listGT['ltaxrateamt'])
                    digst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt'])
                    dsgst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt1'])
                    dcgst0 =dgsttrate + float(Trentinvoicedetailslist_listGT['ltaxrateamt2']) 
                    dtotalfinal =dtotalfinal + float(Trentinvoicedetailslist_listGT['dtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TrentinvoicelistSave_list.dtotal = dtotal
            TrentinvoicelistSave_list.dgsttrate = ltaxrateamt

            TrentinvoicelistSave_list.dsgst0 = 0
            TrentinvoicelistSave_list.dcgst0 = 0 
            TrentinvoicelistSave_list.digst0 = 0 


            if(TrentinvoicelistSave_list.sstatecode == TrentinvoicelistSave_list.slocationstatecode):
                TrentinvoicelistSave_list.dsgst0 = ltaxrateamt/2
                TrentinvoicelistSave_list.dcgst0 = ltaxrateamt/2
            else:
                TrentinvoicelistSave_list.digst0 = ltaxrateamt

            TrentinvoicelistSave_list.dtotalfinal = dtotalfinal
            TrentinvoicelistSave_list.dtotalfinal = dtotalfinal
            TrentinvoicelistSave_list.swords = swords.upper()  

            TrentinvoicelistSave_list.ackdate1 = ackdate1
            TrentinvoicelistSave_list.ackdate = ackdate
            TrentinvoicelistSave_list.ewaydate1 = ewaydate1
            TrentinvoicelistSave_list.ewaydate = ewaydate
            TrentinvoicelistSave_list.sdate1 = sdate1
            TrentinvoicelistSave_list.sdate = sdate
            TrentinvoicelistSave_list.podate1 = podate1
            TrentinvoicelistSave_list.podate = podate
            TrentinvoicelistSave_list.sworkfrom = sworkfrom
            TrentinvoicelistSave_list.sfromdate = sfromdate
            TrentinvoicelistSave_list.sworkfto = sworkfto
            TrentinvoicelistSave_list.stodate = stodate
            TrentinvoicelistSave_list.sworkfto = sworkfto
            TrentinvoicelistSave_list.inrno = inrno
            TrentinvoicelistSave_list.ackno = ackno
            TrentinvoicelistSave_list.ewayno = ewayno
            TrentinvoicelistSave_list.scategoryofservice = scategoryofservice
            TrentinvoicelistSave_list.stype1 = stype1
            TrentinvoicelistSave_list.sinvoicerefno = sinvoicerefno
            TrentinvoicelistSave_list.pono = pono
            TrentinvoicelistSave_list.note1 = note1 

            TrentinvoicelistSave_list.customerid = customerid
            TrentinvoicelistSave_list.customername = customername
            TrentinvoicelistSave_list.saddressclient = saddressclient
            TrentinvoicelistSave_list.scustomerpan = scustomerpan
            TrentinvoicelistSave_list.scustomergst = scustomergst
            TrentinvoicelistSave_list.sstatecode = sstatecode
            
            TrentinvoicelistSave_list.customersiteid = customersiteid
            TrentinvoicelistSave_list.customernamesite = customernamesite
            TrentinvoicelistSave_list.saddresssite = saddresssite 
            TrentinvoicelistSave_list.swords= swords.upper()
            TrentinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
            Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/RentInvoiceListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Trentinvoicelist_list' : Trentinvoicelist_list,
                                'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 




    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Trentinvoicelist_list = Trentinvoicelist.objects.get(salesbillid=lID) 
        Trentinvoicedetailslist_list = Trentinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Trentinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/RentInvoiceListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Trentinvoicelist_list' : Trentinvoicelist_list,
                            'Trentinvoicedetailslist_list' : Trentinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 

    



@csrf_exempt
def ProformaListCopyDetails(request,lID):
    
    
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
 

    Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 

    customerid=Tinvoicelist_list.customerid
    customername=Tinvoicelist_list.customername
    saddress1=Tinvoicelist_list.saddress1
    saddress2=Tinvoicelist_list.saddress2
    saddress3=Tinvoicelist_list.saddress3
    spin=Tinvoicelist_list.spin
    scity=Tinvoicelist_list.scity
    sstate=Tinvoicelist_list.sstate
    scustomerpan=Tinvoicelist_list.scustomerpan
    scustomergst=Tinvoicelist_list.scustomergst
    customernamesite=Tinvoicelist_list.customernamesite
    saddress1site=Tinvoicelist_list.saddress1site
    saddress2site=Tinvoicelist_list.saddress2site
    saddress3site=Tinvoicelist_list.saddress3site
    spinsite=Tinvoicelist_list.spinsite
    scitysite=Tinvoicelist_list.scitysite
    sstatesite=Tinvoicelist_list.sstatesite
    pono=Tinvoicelist_list.pono
    podate=Tinvoicelist_list.podate
    dtotal=Tinvoicelist_list.dtotal
    dgsttrate=Tinvoicelist_list.dgsttrate
    dgst=Tinvoicelist_list.dgst
    dtotalfinal=Tinvoicelist_list.dtotalfinal
    swords=Tinvoicelist_list.swords
    sgstsplit=Tinvoicelist_list.sgstsplit
    note1=Tinvoicelist_list.note1
    note2=Tinvoicelist_list.note2
    inr=Tinvoicelist_list.inr
    scategoryofservice=Tinvoicelist_list.scategoryofservice
    username=Tinvoicelist_list.username
    stype1=Tinvoicelist_list.stype1
    sfile1=Tinvoicelist_list.sfile1
    sfolder1=Tinvoicelist_list.sfolder1
    snumber1=Tinvoicelist_list.snumber1
    customersiteid=Tinvoicelist_list.customersiteid
    sstatecode=Tinvoicelist_list.sstatecode
    sfromdate=Tinvoicelist_list.sfromdate
    stodate=Tinvoicelist_list.stodate
    dsgst0=Tinvoicelist_list.dsgst0
    dcgst0=Tinvoicelist_list.dcgst0
    digst0=Tinvoicelist_list.digst0
    lnoofedit=Tinvoicelist_list.lnoofedit
    ddateofedit=Tinvoicelist_list.ddateofedit
    ldepartmentid=Tinvoicelist_list.ldepartmentid
    sdepartmentname=Tinvoicelist_list.sdepartmentname
    bdelete=Tinvoicelist_list.bdelete
    bcancelcopy=Tinvoicelist_list.bcancelcopy
    bapproval0=Tinvoicelist_list.bapproval0
    bapproval01=Tinvoicelist_list.bapproval01
    bapproval02=Tinvoicelist_list.bapproval02
    bapproval03=Tinvoicelist_list.bapproval03
    bapproval04=Tinvoicelist_list.bapproval04
    bapproval05=Tinvoicelist_list.bapproval05
    bapproval06=Tinvoicelist_list.bapproval06
    bapproval07=Tinvoicelist_list.bapproval07
    bapproval08=Tinvoicelist_list.bapproval08
    bapproval09=Tinvoicelist_list.bapproval09
    bapproval010=Tinvoicelist_list.bapproval010
    scomments=Tinvoicelist_list.scomments
    scommentsdelete=Tinvoicelist_list.scommentsdelete
    lorderid=Tinvoicelist_list.lorderid
    dsgst01=Tinvoicelist_list.dsgst01
    dcgst01=Tinvoicelist_list.dcgst01
    dcgst00=Tinvoicelist_list.dcgst00
    dsgst5=Tinvoicelist_list.dsgst5
    dcgst5=Tinvoicelist_list.dcgst5
    dcgst50=Tinvoicelist_list.dcgst50
    dsgst12=Tinvoicelist_list.dsgst12
    dcgst12=Tinvoicelist_list.dcgst12
    dcgst120=Tinvoicelist_list.dcgst120
    dsgst18=Tinvoicelist_list.dsgst18
    dcgst18=Tinvoicelist_list.dcgst18
    dcgst180=Tinvoicelist_list.dcgst180
    dsgst28=Tinvoicelist_list.dsgst28
    dcgst28=Tinvoicelist_list.dcgst28
    dcgst280=Tinvoicelist_list.dcgst280
    dgst28cess=Tinvoicelist_list.dgst28cess
    dsgst0pt5=Tinvoicelist_list.dsgst0pt5
    dcgst0pt5=Tinvoicelist_list.dcgst0pt5
    dcgst0pt50=Tinvoicelist_list.dcgst0pt50
    dsgst2pt0=Tinvoicelist_list.dsgst2pt0
    dcgst2pt0=Tinvoicelist_list.dcgst2pt0
    dcgst2pt00=Tinvoicelist_list.dcgst2pt00
    dsgst2pt5=Tinvoicelist_list.dsgst2pt5
    dcgst2pt5=Tinvoicelist_list.dcgst2pt5
    dcgst2pt50=Tinvoicelist_list.dcgst2pt50
    dsgst1p0=Tinvoicelist_list.dsgst1p0
    dcgst1pt0=Tinvoicelist_list.dcgst1pt0
    dcgst1pt00=Tinvoicelist_list.dcgst1pt00
    saddressclient=Tinvoicelist_list.saddressclient
    saddresssite=Tinvoicelist_list.saddresssite
    scompanyaddress=Tinvoicelist_list.scompanyaddress
    sdate=Tinvoicelist_list.sdate
    sdate1=Tinvoicelist_list.sdate1
    llocationid=Tinvoicelist_list.llocationid
    slocation=Tinvoicelist_list.slocation
    slocationstatecode=Tinvoicelist_list.slocationstatecode
    slocationgstno=Tinvoicelist_list.slocationgstno
    slocationpanno=Tinvoicelist_list.slocationpanno
    slocationformat=Tinvoicelist_list.slocationformat
    bsitesez=Tinvoicelist_list.bsitesez
    sworkfrom=Tinvoicelist_list.sworkfrom
    sworkfto=Tinvoicelist_list.sworkfto
    podate1=Tinvoicelist_list.podate1
    bsamestate =Tinvoicelist_list.bsamestate 
    sfile11=Tinvoicelist_list.sfile11
    sfolder11=Tinvoicelist_list.sfolder11
    sfile12=Tinvoicelist_list.sfile12
    sfolder12=Tinvoicelist_list.sfolder12
    sfile13=Tinvoicelist_list.sfile13
    sfolder13=Tinvoicelist_list.sfolder13
    sfile14=Tinvoicelist_list.sfile14
    sfolder14=Tinvoicelist_list.sfolder14
    sfile15=Tinvoicelist_list.sfile15
    sfolder15=Tinvoicelist_list.sfolder15
 




 
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
            ssalesbillno = "000" + ssalesbillno
        elif(len(ssalesbillno) == 2):
            ssalesbillno = "00" + ssalesbillno
        elif(len(ssalesbillno) == 3):
            ssalesbillno = "0" + ssalesbillno
        sinvoicerefno=McompanylistGet.sformat2 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice2 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            


    Tinvoicelist_AddNewOBJ = Tinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Tinvoicelist_AddNewOBJ.save()
    salesbillid = Tinvoicelist_AddNewOBJ.salesbillid
  

    Tproformalist_list = Tproformalist.objects.filter(salesbillid=lID).values() 
    
    if Tproformalist_list:
        for Tproformalist_listQ in Tproformalist_list:
            sdesc=Tproformalist_listQ['sdesc']
            partid=Tproformalist_listQ['partid']
            partno=Tproformalist_listQ['partno']
            qty=Tproformalist_listQ['qty']
            unitprice=Tproformalist_listQ['unitprice']
            units=Tproformalist_listQ['units']
            ddescitemtotal=Tproformalist_listQ['ddescitemtotal']
            shsn=Tproformalist_listQ['shsn']
            ssac=Tproformalist_listQ['ssac']
            smanrate=Tproformalist_listQ['smanrate']
            staxnotify=Tproformalist_listQ['staxnotify']
            dsgst01=Tproformalist_listQ['dsgst01']
            dcgst01=Tproformalist_listQ['dcgst01']
            dcgst00=Tproformalist_listQ['dcgst00']
            dsgst5=Tproformalist_listQ['dsgst5']
            dcgst5=Tproformalist_listQ['dcgst5']
            dcgst50=Tproformalist_listQ['dcgst50']
            dsgst12=Tproformalist_listQ['dsgst12']
            dcgst12=Tproformalist_listQ['dcgst12']
            dcgst120=Tproformalist_listQ['dcgst120']
            dsgst18=Tproformalist_listQ['dsgst18']
            dcgst18=Tproformalist_listQ['dcgst18']
            dcgst180=Tproformalist_listQ['dcgst180']
            dsgst28=Tproformalist_listQ['dsgst28']
            dcgst28=Tproformalist_listQ['dcgst28']
            dcgst280=Tproformalist_listQ['dcgst280']
            dgst28cess=Tproformalist_listQ['dgst28cess']
            dsgst0pt5=Tproformalist_listQ['dsgst0pt5']
            dcgst0pt5=Tproformalist_listQ['dcgst0pt5']
            dcgst0pt50=Tproformalist_listQ['dcgst0pt50']
            dsgst2pt0=Tproformalist_listQ['dsgst2pt0']
            dcgst2pt0=Tproformalist_listQ['dcgst2pt0']
            dcgst2pt00=Tproformalist_listQ['dcgst2pt00']
            dsgst2pt5=Tproformalist_listQ['dsgst2pt5']
            dcgst2pt5=Tproformalist_listQ['dcgst2pt5']
            dcgst2pt50=Tproformalist_listQ['dcgst2pt50']
            dsgst1p0=Tproformalist_listQ['dsgst1p0']
            dcgst1pt0=Tproformalist_listQ['dcgst1pt0']
            dcgst1pt00=Tproformalist_listQ['dcgst1pt00']


            
            Tproformalist_AddNewOBJ = Tproformalist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tproformalist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaListDetails', lID=salesbillid)  


    




 




