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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })

@csrf_exempt
def ProjectListCopyDetails(request,lID):
    
    
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
  

    Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tinvoicedetailslist_list:
        for Tinvoicedetailslist_listQ in Tinvoicedetailslist_list:
            sdesc=Tinvoicedetailslist_listQ['sdesc']
            partid=Tinvoicedetailslist_listQ['partid']
            partno=Tinvoicedetailslist_listQ['partno']
            qty=Tinvoicedetailslist_listQ['qty']
            unitprice=Tinvoicedetailslist_listQ['unitprice']
            units=Tinvoicedetailslist_listQ['units']
            ddescitemtotal=Tinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tinvoicedetailslist_listQ['shsn']
            ssac=Tinvoicedetailslist_listQ['ssac']
            smanrate=Tinvoicedetailslist_listQ['smanrate']
            staxnotify=Tinvoicedetailslist_listQ['staxnotify']
            dsgst01=Tinvoicedetailslist_listQ['dsgst01']
            dcgst01=Tinvoicedetailslist_listQ['dcgst01']
            dcgst00=Tinvoicedetailslist_listQ['dcgst00']
            dsgst5=Tinvoicedetailslist_listQ['dsgst5']
            dcgst5=Tinvoicedetailslist_listQ['dcgst5']
            dcgst50=Tinvoicedetailslist_listQ['dcgst50']
            dsgst12=Tinvoicedetailslist_listQ['dsgst12']
            dcgst12=Tinvoicedetailslist_listQ['dcgst12']
            dcgst120=Tinvoicedetailslist_listQ['dcgst120']
            dsgst18=Tinvoicedetailslist_listQ['dsgst18']
            dcgst18=Tinvoicedetailslist_listQ['dcgst18']
            dcgst180=Tinvoicedetailslist_listQ['dcgst180']
            dsgst28=Tinvoicedetailslist_listQ['dsgst28']
            dcgst28=Tinvoicedetailslist_listQ['dcgst28']
            dcgst280=Tinvoicedetailslist_listQ['dcgst280']
            dgst28cess=Tinvoicedetailslist_listQ['dgst28cess']
            dsgst0pt5=Tinvoicedetailslist_listQ['dsgst0pt5']
            dcgst0pt5=Tinvoicedetailslist_listQ['dcgst0pt5']
            dcgst0pt50=Tinvoicedetailslist_listQ['dcgst0pt50']
            dsgst2pt0=Tinvoicedetailslist_listQ['dsgst2pt0']
            dcgst2pt0=Tinvoicedetailslist_listQ['dcgst2pt0']
            dcgst2pt00=Tinvoicedetailslist_listQ['dcgst2pt00']
            dsgst2pt5=Tinvoicedetailslist_listQ['dsgst2pt5']
            dcgst2pt5=Tinvoicedetailslist_listQ['dcgst2pt5']
            dcgst2pt50=Tinvoicedetailslist_listQ['dcgst2pt50']
            dsgst1p0=Tinvoicedetailslist_listQ['dsgst1p0']
            dcgst1pt0=Tinvoicedetailslist_listQ['dcgst1pt0']
            dcgst1pt00=Tinvoicedetailslist_listQ['dcgst1pt00']


            
            Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProjectListDetails', lID=salesbillid)  



    
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
            
            
            Tinvoicelist_AddNewOBJ = Tinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)
 
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
    dcgst1pt0=0


                

    if Tinvoicedetailslist_listG:
        for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
            dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TinvoicelistSave_list.dtotal = dtotal
    TinvoicelistSave_list.dgsttrate = dcgst1pt0

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
  

    TinvoicelistSave_list.dsgst01 = dsgst01 
    TinvoicelistSave_list.dsgst5 = dsgst5 
    TinvoicelistSave_list.dsgst12 = dsgst12 
    TinvoicelistSave_list.dsgst18 = dsgst18 
    TinvoicelistSave_list.dsgst28 = dsgst28  

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
def ProjectListDetailsPrint(request,lID):

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

            
            return   redirect('ProjectList')  
        
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
            dcgst1pt0=0
            

                        

            if Tinvoicedetailslist_listG:
                for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                    dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                    dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TinvoicelistSave_list.dtotal = dtotal
            TinvoicelistSave_list.dgsttrate = dcgst1pt0

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


            TinvoicelistSave_list.dsgst01 = dsgst01 
            TinvoicelistSave_list.dsgst5 = dsgst5 
            TinvoicelistSave_list.dsgst12 = dsgst12 
            TinvoicelistSave_list.dsgst18 = dsgst18 
            TinvoicelistSave_list.dsgst28 = dsgst28  

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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 


        if 'cmdItemSave1' in request.POST:  

            Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

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

            icountLoop =0
            icountLoopAll =0
            Tinvoicedetailslist_listGetLoop = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tinvoicedetailslist_listGetLoop.count()

            for Tinvoicedetailslist_listGetLoopA in Tinvoicedetailslist_listGetLoop:
                      
                icountLoop=Tinvoicedetailslist_listGetLoopA['salesordermultiid']  


                sdesc=data.get('txtItemDesc' + str(icountLoop))   
                qty=data.get('txtQuantity' + str(icountLoop))   
                unitprice=data.get('txtRate' + str(icountLoop)) 
                units=data.get('txtUnits' + str(icountLoop)) 
                ddescitemtotal=data.get('txtItemAmt' + str(icountLoop)) 
                shsn=data.get('txtHSNCode' + str(icountLoop)) 
                dtotal=data.get('txtItemTotalAmt' + str(icountLoop)) 
                ltaxrate=data.get('txtGSTRate' + str(icountLoop))   
                ltaxrateamt=data.get('txtGSTAmt' + str(icountLoop))   
                staxnotify=data.get('txtPOAMt' + str(icountLoop))   
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


                Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tinvoicedetailslist_AddNewOBJ.sdesc = sdesc
                Tinvoicedetailslist_AddNewOBJ.qty = qty
                Tinvoicedetailslist_AddNewOBJ.unitprice = unitprice
                Tinvoicedetailslist_AddNewOBJ.units = units
                Tinvoicedetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tinvoicedetailslist_AddNewOBJ.shsn = shsn
                Tinvoicedetailslist_AddNewOBJ.ssac = ssac
                Tinvoicedetailslist_AddNewOBJ.smanrate = smanrate
                Tinvoicedetailslist_AddNewOBJ.staxnotify = staxnotify
                Tinvoicedetailslist_AddNewOBJ.dsgst01 = dsgst01
                Tinvoicedetailslist_AddNewOBJ.dcgst01 = dcgst01
                Tinvoicedetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tinvoicedetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tinvoicedetailslist_AddNewOBJ.dsgst5 = dsgst5
                Tinvoicedetailslist_AddNewOBJ.dcgst5 = dcgst5 
                
               
                Tinvoicedetailslist_AddNewOBJ.dcgst50=dcgst50
                Tinvoicedetailslist_AddNewOBJ.dsgst12=dsgst12
                Tinvoicedetailslist_AddNewOBJ.dcgst12=dcgst12
                Tinvoicedetailslist_AddNewOBJ.dcgst120=dcgst120
                Tinvoicedetailslist_AddNewOBJ.dsgst18=dsgst18
                Tinvoicedetailslist_AddNewOBJ.dcgst18=dcgst18
                Tinvoicedetailslist_AddNewOBJ.dcgst180=dcgst180
                Tinvoicedetailslist_AddNewOBJ.dsgst28=dsgst28
                Tinvoicedetailslist_AddNewOBJ.dcgst28=dcgst28
                Tinvoicedetailslist_AddNewOBJ.dcgst280=dcgst280
                Tinvoicedetailslist_AddNewOBJ.dgst28cess=dgst28cess 
                Tinvoicedetailslist_AddNewOBJ.dsgst0pt5=dsgst0pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst0pt5=dcgst0pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst0pt50=dcgst0pt50
                Tinvoicedetailslist_AddNewOBJ.dsgst2pt0=dsgst2pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt0=dcgst2pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt00=dcgst2pt00
                Tinvoicedetailslist_AddNewOBJ.dsgst2pt5=dsgst2pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt5=dcgst2pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt50=dcgst2pt50
                Tinvoicedetailslist_AddNewOBJ.dsgst1p0=dsgst1p0,
                Tinvoicedetailslist_AddNewOBJ.dcgst1pt0=dcgst1pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst1pt00=dcgst1pt00

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
                dcgst1pt0=0
                

                            

                if Tinvoicedetailslist_listG:
                    for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                        dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
                        dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
                        dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
                        dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
                        dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                        dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
                        
                        dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TinvoicelistSave_list.dtotal = dtotal
                TinvoicelistSave_list.dgsttrate = dcgst1pt0

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


                TinvoicelistSave_list.dsgst01 = dsgst01 
                TinvoicelistSave_list.dsgst5 = dsgst5 
                TinvoicelistSave_list.dsgst12 = dsgst12 
                TinvoicelistSave_list.dsgst18 = dsgst18 
                TinvoicelistSave_list.dsgst28 = dsgst28  

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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 









@csrf_exempt
def ProjectListSEZ(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProjectListSEZAdd')  
        
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
        


        return render(request, "BillingSol/ProjectInvoiceListSEZ.html",
                    {
                        'Tinvoicelist_list':Tinvoicelist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })

@csrf_exempt
def ProjectListDetailsPrint(request,lID):
    
    
    salesbillid=0


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
    iCountDetails =0
    iCountDetails = Tserviceinvoicedetailslist_list.count
    context = {
            
        'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,   
            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
        } 
    
    
    pdf = render_to_pdf('BillingSol/ProjectListSEZDetailsPrint.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


@csrf_exempt
def ProjectListSEZCopyDetails(request,lID):
    
    
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
    bsitesez=1
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
  

    Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tinvoicedetailslist_list:
        for Tinvoicedetailslist_listQ in Tinvoicedetailslist_list:
            sdesc=Tinvoicedetailslist_listQ['sdesc']
            partid=Tinvoicedetailslist_listQ['partid']
            partno=Tinvoicedetailslist_listQ['partno']
            qty=Tinvoicedetailslist_listQ['qty']
            unitprice=Tinvoicedetailslist_listQ['unitprice']
            units=Tinvoicedetailslist_listQ['units']
            ddescitemtotal=Tinvoicedetailslist_listQ['ddescitemtotal']
            shsn=Tinvoicedetailslist_listQ['shsn']
            ssac=Tinvoicedetailslist_listQ['ssac']
            smanrate=Tinvoicedetailslist_listQ['smanrate']
            staxnotify=Tinvoicedetailslist_listQ['staxnotify']
            dsgst01=Tinvoicedetailslist_listQ['dsgst01']
            dcgst01=Tinvoicedetailslist_listQ['dcgst01']
            dcgst00=Tinvoicedetailslist_listQ['dcgst00']
            dsgst5=Tinvoicedetailslist_listQ['dsgst5']
            dcgst5=Tinvoicedetailslist_listQ['dcgst5']
            dcgst50=Tinvoicedetailslist_listQ['dcgst50']
            dsgst12=Tinvoicedetailslist_listQ['dsgst12']
            dcgst12=Tinvoicedetailslist_listQ['dcgst12']
            dcgst120=Tinvoicedetailslist_listQ['dcgst120']
            dsgst18=Tinvoicedetailslist_listQ['dsgst18']
            dcgst18=Tinvoicedetailslist_listQ['dcgst18']
            dcgst180=Tinvoicedetailslist_listQ['dcgst180']
            dsgst28=Tinvoicedetailslist_listQ['dsgst28']
            dcgst28=Tinvoicedetailslist_listQ['dcgst28']
            dcgst280=Tinvoicedetailslist_listQ['dcgst280']
            dgst28cess=Tinvoicedetailslist_listQ['dgst28cess']
            dsgst0pt5=Tinvoicedetailslist_listQ['dsgst0pt5']
            dcgst0pt5=Tinvoicedetailslist_listQ['dcgst0pt5']
            dcgst0pt50=Tinvoicedetailslist_listQ['dcgst0pt50']
            dsgst2pt0=Tinvoicedetailslist_listQ['dsgst2pt0']
            dcgst2pt0=Tinvoicedetailslist_listQ['dcgst2pt0']
            dcgst2pt00=Tinvoicedetailslist_listQ['dcgst2pt00']
            dsgst2pt5=Tinvoicedetailslist_listQ['dsgst2pt5']
            dcgst2pt5=Tinvoicedetailslist_listQ['dcgst2pt5']
            dcgst2pt50=Tinvoicedetailslist_listQ['dcgst2pt50']
            dsgst1p0=Tinvoicedetailslist_listQ['dsgst1p0']
            dcgst1pt0=Tinvoicedetailslist_listQ['dcgst1pt0']
            dcgst1pt00=Tinvoicedetailslist_listQ['dcgst1pt00']


            
            Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProjectListSEZDetails', lID=salesbillid)  



    
@csrf_exempt
def ProjectListSEZAdd(request):
    
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
    bsitesez=1
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
    slutno=""
    breversechargemechanism=0

    if request.method == "POST":

        data = request.POST
        if 'cmbCloseAdd' in request.POST:  

            return   redirect('ProjectListSEZ') 

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
            
            
            Tinvoicelist_AddNewOBJ = Tinvoicelist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate, slutno=slutno, breversechargemechanism= breversechargemechanism)
 
            Tinvoicelist_AddNewOBJ.save()
            salesbillid = Tinvoicelist_AddNewOBJ.salesbillid

            return   redirect('ProjectListSEZDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProjectListSEZAdd.html",
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
def ProjectListSEZDetailsDelete(request,lID):
    
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
    dcgst1pt0=0


                

    if Tinvoicedetailslist_listG:
        for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
            dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
            
            dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TinvoicelistSave_list.dtotal = dtotal
    TinvoicelistSave_list.dgsttrate = dcgst1pt0

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
  

    TinvoicelistSave_list.dsgst01 = dsgst01 
    TinvoicelistSave_list.dsgst5 = dsgst5 
    TinvoicelistSave_list.dsgst12 = dsgst12 
    TinvoicelistSave_list.dsgst18 = dsgst18 
    TinvoicelistSave_list.dsgst28 = dsgst28  

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
    return redirect('ProjectListSEZDetails', lID=lDetId)  


@csrf_exempt
def ProjectListSEZDetails(request,lID):
    
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
    bsitesez=1
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


    slutno=""
    breversechargemechanism=0

    
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

            
            return   redirect('ProjectListSEZ')  
        
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
                
                return render(request, "BillingSol/ProjectListSEZDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tinvoicelist_list' : Tinvoicelist_list,
                                    'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
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
                        
                        
                        TinvoicelistSave_list = Tinvoicelist.objects.get(salesbillid=lID) 

                        TinvoicelistSave_list.customersiteid = customersiteid
                        TinvoicelistSave_list.customernamesite = customernamesite
                        TinvoicelistSave_list.saddresssite = saddresssite 
                        TinvoicelistSave_list.slutno = txtslutno 
                        

                        TinvoicelistSave_list.spinsite = MsitelistGet.sstatecode
                        TinvoicelistSave_list.sstatesite = MsitelistGet.stempname1
                        TinvoicelistSave_list.scitysite = MsitelistGet.stempname2



                        TinvoicelistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
            
            return render(request, "BillingSol/ProjectListSEZDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
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
            txtslutno=data.get('txtslutno') 


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
            TinvoicelistSave_list.slutno = txtslutno 


            TinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProjectListSEZDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tinvoicelist_list' : Tinvoicelist_list,
                                'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
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
            
            
            pdf = render_to_pdf('BillingSol/ProjectListSEZDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

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
            txtslutno=data.get('txtslutno') 


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
            dcgst1pt0=0
            

                        

            if Tinvoicedetailslist_listG:
                for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                    dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                    dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TinvoicelistSave_list.dtotal = dtotal
            TinvoicelistSave_list.dgsttrate = dcgst1pt0

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


            TinvoicelistSave_list.dsgst01 = dsgst01 
            TinvoicelistSave_list.dsgst5 = dsgst5 
            TinvoicelistSave_list.dsgst12 = dsgst12 
            TinvoicelistSave_list.dsgst18 = dsgst18 
            TinvoicelistSave_list.dsgst28 = dsgst28  

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
            TinvoicelistSave_list.slutno = txtslutno 
            TinvoicelistSave_list.swords= swords.upper()
            TinvoicelistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
            Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProjectListSEZDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tinvoicelist_list' : Tinvoicelist_list,
                                'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 

        if 'cmdItemSave1' in request.POST:  

            Tinvoicedetailslist_listG = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 

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

            icountLoop =0
            icountLoopAll =0
            Tinvoicedetailslist_listGetLoop = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tinvoicedetailslist_listGetLoop.count()

            for Tinvoicedetailslist_listGetLoopA in Tinvoicedetailslist_listGetLoop:
                      
                icountLoop=Tinvoicedetailslist_listGetLoopA['salesordermultiid']  


                sdesc=data.get('txtItemDesc' + str(icountLoop))   
                qty=data.get('txtQuantity' + str(icountLoop))   
                unitprice=data.get('txtRate' + str(icountLoop)) 
                units=data.get('txtUnits' + str(icountLoop)) 
                ddescitemtotal=data.get('txtItemAmt' + str(icountLoop)) 
                shsn=data.get('txtHSNCode' + str(icountLoop)) 
                dtotal=data.get('txtItemTotalAmt' + str(icountLoop)) 
                ltaxrate=data.get('txtGSTRate' + str(icountLoop))   
                ltaxrateamt=data.get('txtGSTAmt' + str(icountLoop))   
                staxnotify=data.get('txtPOAMt' + str(icountLoop))   
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


                Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tinvoicedetailslist_AddNewOBJ.sdesc = sdesc
                Tinvoicedetailslist_AddNewOBJ.qty = qty
                Tinvoicedetailslist_AddNewOBJ.unitprice = unitprice
                Tinvoicedetailslist_AddNewOBJ.units = units
                Tinvoicedetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tinvoicedetailslist_AddNewOBJ.shsn = shsn
                Tinvoicedetailslist_AddNewOBJ.ssac = ssac
                Tinvoicedetailslist_AddNewOBJ.smanrate = smanrate
                Tinvoicedetailslist_AddNewOBJ.staxnotify = staxnotify
                Tinvoicedetailslist_AddNewOBJ.dsgst01 = dsgst01
                Tinvoicedetailslist_AddNewOBJ.dcgst01 = dcgst01
                Tinvoicedetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tinvoicedetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tinvoicedetailslist_AddNewOBJ.dsgst5 = dsgst5
                Tinvoicedetailslist_AddNewOBJ.dcgst5 = dcgst5 
                
               
                Tinvoicedetailslist_AddNewOBJ.dcgst50=dcgst50
                Tinvoicedetailslist_AddNewOBJ.dsgst12=dsgst12
                Tinvoicedetailslist_AddNewOBJ.dcgst12=dcgst12
                Tinvoicedetailslist_AddNewOBJ.dcgst120=dcgst120
                Tinvoicedetailslist_AddNewOBJ.dsgst18=dsgst18
                Tinvoicedetailslist_AddNewOBJ.dcgst18=dcgst18
                Tinvoicedetailslist_AddNewOBJ.dcgst180=dcgst180
                Tinvoicedetailslist_AddNewOBJ.dsgst28=dsgst28
                Tinvoicedetailslist_AddNewOBJ.dcgst28=dcgst28
                Tinvoicedetailslist_AddNewOBJ.dcgst280=dcgst280
                Tinvoicedetailslist_AddNewOBJ.dgst28cess=dgst28cess 
                Tinvoicedetailslist_AddNewOBJ.dsgst0pt5=dsgst0pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst0pt5=dcgst0pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst0pt50=dcgst0pt50
                Tinvoicedetailslist_AddNewOBJ.dsgst2pt0=dsgst2pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt0=dcgst2pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt00=dcgst2pt00
                Tinvoicedetailslist_AddNewOBJ.dsgst2pt5=dsgst2pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt5=dcgst2pt5
                Tinvoicedetailslist_AddNewOBJ.dcgst2pt50=dcgst2pt50
                Tinvoicedetailslist_AddNewOBJ.dsgst1p0=dsgst1p0,
                Tinvoicedetailslist_AddNewOBJ.dcgst1pt0=dcgst1pt0
                Tinvoicedetailslist_AddNewOBJ.dcgst1pt00=dcgst1pt00

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
                dcgst1pt0=0
                

                            

                if Tinvoicedetailslist_listG:
                    for Tinvoicedetailslist_listGT in Tinvoicedetailslist_listG:
                        dtotal =dtotal + float(Tinvoicedetailslist_listGT['qty'] * Tinvoicedetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tinvoicedetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tinvoicedetailslist_listGT['dcgst5'])
                        dsgst5 =dsgst5 + float(Tinvoicedetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tinvoicedetailslist_listGT['dcgst12'])
                        dsgst12 =dsgst12 + float(Tinvoicedetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tinvoicedetailslist_listGT['dcgst18'])
                        dsgst18 =dsgst18 + float(Tinvoicedetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tinvoicedetailslist_listGT['dcgst28'])
                        dsgst28 =dsgst28 + float(Tinvoicedetailslist_listGT['dsgst28'])
                        dcgst1pt0=dcgst1pt0 + float(Tinvoicedetailslist_listGT['dcgst1pt0']) 
                        
                        dtotalfinal =dtotalfinal + float(Tinvoicedetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TinvoicelistSave_list.dtotal = dtotal
                TinvoicelistSave_list.dgsttrate = dcgst1pt0

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


                TinvoicelistSave_list.dsgst01 = dsgst01 
                TinvoicelistSave_list.dsgst5 = dsgst5 
                TinvoicelistSave_list.dsgst12 = dsgst12 
                TinvoicelistSave_list.dsgst18 = dsgst18 
                TinvoicelistSave_list.dsgst28 = dsgst28  

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
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 






    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tinvoicelist_list = Tinvoicelist.objects.get(salesbillid=lID) 
        Tinvoicedetailslist_list = Tinvoicedetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tinvoicelist_list.customerid).values() 
          
        return render(request, "BillingSol/ProjectListSEZDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tinvoicelist_list' : Tinvoicelist_list,
                            'Tinvoicedetailslist_list' : Tinvoicedetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        ) 





















 
@csrf_exempt
def ProformaList(request):
    if request.method == "POST":
        data = request.POST 

        if 'cmbAdd' in request.POST:  
            
            return   redirect('ProformaListAdd')  
        
    else:
        
        Tproformalist_list = Tproformalist.objects.order_by('-invoicedate', '-salesbillno') 

        
        page_number  = request.GET.get('page')

        lRecCount =0 
        lRecCount = Tproformalist_list.count()
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
        paginator = Paginator(Tproformalist_list, lRecCount1)
        try:
            Tproformalist_lists = paginator.get_page(page_number )
        except PageNotAnInteger:
            Tproformalist_lists = paginator.page(1)
        except EmptyPage:
            Tproformalist_lists = paginator.page(paginator.num_pages)
        


        return render(request, "BillingSol/ProformaInvoiceList.html",
                    {
                        'Tproformalist_list':Tproformalist_lists,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    

                    })


    
@csrf_exempt
def ProformaListAdd(request):
    
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

            return   redirect('ProformaList') 

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

                        salesbillno=McompanylistGet.linvoice4 + 1
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
                        sinvoicerefno=McompanylistGet.sformat4 + ssalesbillno + McompanylistGet.sformat 



                        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
                        
                        Mcompanylist_AddNewOBJ.linvoice4 = salesbillno
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
            
            
            Tproformalist_AddNewOBJ = Tproformalist(salesbillno=salesbillno, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	saddressclient1=saddressclient1, 	saddresssite1=saddresssite1, 	scompanyaddress1=scompanyaddress1, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, 	bsitesez=bsitesez, 	ackdate=ackdate, 	ackdate1=ackdate1, 	podate1=podate1, 	bsamestate=bsamestate, 	sfile11=sfile11, 	sfolder11=sfolder11, 	sfile12=sfile12, 	sfolder12=sfolder12, 	sfile13=sfile13, 	sfolder13=sfolder13, 	sfile14=sfile14, 	sfolder14=sfolder14, 	sfile15=sfile15, 	sfolder15=sfolder15)
 
            Tproformalist_AddNewOBJ.save()
            salesbillid = Tproformalist_AddNewOBJ.salesbillid

            return   redirect('ProformaListDetails', lID=salesbillid) 
    else:   
        Mcompanylistlist_list = Mcompanylist.objects.order_by('scompanyname')  
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')              
        return render(request, "BillingSol/ProformaListAdd.html",
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
def ProformaListDetailsDelete(request,lID):
    
    lCatID = 0
     
    
    lDetId =0

    Tproformadetailslist_list = Tproformadetailslist.objects.get(salesordermultiid=lID)
    
    lDetId = Tproformadetailslist_list.salesbillid
    
    # if Tproformadetailslist_list:
    #     for Tproformadetailslist_listQ in Tproformadetailslist_list:
    #         lDetId = Tproformadetailslist_listQ['salesbillid']

    Tproformalist_listOBJ =  Tproformadetailslist.objects.get(salesordermultiid=lID).delete()
          


    TproformalistSave_list = Tproformalist.objects.get(salesbillid=lDetId) 


    ltaxrateamt =0
    digst0 = 0
    dsgst0 = 0
    dcgst0 = 0
    dgsttrate = 0
    dtotalfinal = 0
    dtotal =0
    swords=""

    Tproformadetailslist_listG = Tproformadetailslist.objects.filter(salesbillid=lDetId).values() 

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


                

    if Tproformadetailslist_listG:
        for Tproformadetailslist_listGT in Tproformadetailslist_listG:
            dtotal =dtotal + float(Tproformadetailslist_listGT['qty'] * Tproformadetailslist_listGT['unitprice'])

            dcgst01 =dcgst01 + float(Tproformadetailslist_listGT['dcgst01'])
            dcgst5 =dcgst5 + float(Tproformadetailslist_listGT['dcgst5'])
            dsgst5 =dsgst5 + float(Tproformadetailslist_listGT['dsgst5'])
            dcgst12 =dcgst12 + float(Tproformadetailslist_listGT['dcgst12'])
            dsgst12 =dsgst12 + float(Tproformadetailslist_listGT['dsgst12'])
            dcgst18 =dcgst18 + float(Tproformadetailslist_listGT['dcgst18'])
            dsgst18 =dsgst18 + float(Tproformadetailslist_listGT['dsgst18'])
            dcgst28 =dcgst28 + float(Tproformadetailslist_listGT['dcgst28'])
            dsgst28 =dsgst28 + float(Tproformadetailslist_listGT['dsgst28'])
            dcgst1pt0=dcgst1pt0 + float(Tproformadetailslist_listGT['dcgst1pt0']) 
            
            
            dtotalfinal =dtotalfinal + float(Tproformadetailslist_listGT['ddescitemtotal']) #Correct


        
    swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

    TproformalistSave_list.dtotal = dtotal
    TproformalistSave_list.dgsttrate = dcgst1pt0

    TproformalistSave_list.dsgst0 = 0
    TproformalistSave_list.dcgst0 = 0 
    TproformalistSave_list.digst0 = 0 




    TproformalistSave_list.dcgst01 = 0 
    TproformalistSave_list.dcgst5 = 0 
    TproformalistSave_list.dcgst12 = 0 
    TproformalistSave_list.dcgst18 = 0 
    TproformalistSave_list.dcgst28 = 0 

    TproformalistSave_list.dcgst01 = 0 
    TproformalistSave_list.dsgst5 = 0 
    TproformalistSave_list.dsgst12 = 0 
    TproformalistSave_list.dsgst18 = 0 
    TproformalistSave_list.dsgst28 = 0 
 

    TproformalistSave_list.dsgst01 = dsgst01 
    TproformalistSave_list.dsgst5 = dsgst5 
    TproformalistSave_list.dsgst12 = dsgst12 
    TproformalistSave_list.dsgst18 = dsgst18 
    TproformalistSave_list.dsgst28 = dsgst28  
    TproformalistSave_list.dcgst01 =dcgst01 
    TproformalistSave_list.dcgst5 = dcgst5 
    TproformalistSave_list.dcgst12 =dcgst12
    TproformalistSave_list.dcgst18 = dcgst18 
    TproformalistSave_list.dcgst28 = dcgst28

    TproformalistSave_list.dtotalfinal = dtotalfinal
    TproformalistSave_list.dtotalfinal = dtotalfinal
    TproformalistSave_list.swords = swords.upper()  


    TproformalistSave_list.save()




    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaListDetails', lID=lDetId)  


@csrf_exempt
def ProformaListDetails(request,lID):
    
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

            
            return   redirect('ProformaList')  
        
        if 'cmdGetClient' in request.POST:  

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
                        sstatecode=McustomerlistGet.sstatecode 
                        
                        
                        TproformalistSave_list = Tproformalist.objects.get(salesbillid=lID) 

                        TproformalistSave_list.customerid = customerid
                        TproformalistSave_list.customername = customername
                        TproformalistSave_list.saddressclient = saddressclient
                        TproformalistSave_list.scustomerpan = scustomerpan
                        TproformalistSave_list.scustomergst = scustomergst
                        TproformalistSave_list.sstatecode = sstatecode
                        TproformalistSave_list.save()


                Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
                
                Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
        

                Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
                Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
                
                return render(request, "BillingSol/ProformaListDetails.html",
                                {
                                    
                                'title':'User list',  
                                    'message':'Your User list page.',
                                    'year':datetime.now().year,  
                                    'Msitelist_list' : Msitelist_list,
                                    'Mcustomerlist_list' : Mcustomerlist_list,
                                    'Tproformalist_list' : Tproformalist_list,
                                    'Tproformadetailslist_list' : Tproformadetailslist_list,
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
                        
                        
                        TproformalistSave_list = Tproformalist.objects.get(salesbillid=lID) 

                        TproformalistSave_list.customersiteid = customersiteid
                        TproformalistSave_list.customernamesite = customernamesite
                        TproformalistSave_list.saddresssite = saddresssite 
                        

                        TproformalistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformalistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformalistSave_list.scitysite = MsitelistGet.stempname2



                        TproformalistSave_list.save()


                
            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
    

            Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
            Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformalist_list.customerid).values() 
            
            return render(request, "BillingSol/ProformaListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformalist_list' : Tproformalist_list,
                            'Tproformadetailslist_list' : Tproformadetailslist_list,
                            'badmin':  request.session['badmin'],  
                            'bFinance':  request.session['bFinance'],  
                            'bpo':  request.session['bSupplyChain'],  
                            'bSales':  request.session['bSales'],  
                            'badmin1':  request.session['badmin1'],    
                        }
                        )  

        if 'cmbSaveAdd' in request.POST:  

            TproformalistSave_list = Tproformalist.objects.get(salesbillid=lID) 

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
                           
                        TproformalistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformalistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformalistSave_list.scitysite = MsitelistGet.stempname2


                        
                        

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

 

            TproformalistSave_list.bsitesez = bsitesez


            TproformalistSave_list.ackdate1 = ackdate1
            TproformalistSave_list.ackdate = ackdate
            TproformalistSave_list.ewaydate1 = ewaydate1
            TproformalistSave_list.ewaydate = ewaydate
            TproformalistSave_list.sdate1 = sdate1
            TproformalistSave_list.sdate = sdate
            TproformalistSave_list.podate1 = podate1
            TproformalistSave_list.podate = podate
            TproformalistSave_list.sworkfrom = sworkfrom
            TproformalistSave_list.sfromdate = sfromdate
            TproformalistSave_list.sworkfto = sworkfto
            TproformalistSave_list.stodate = stodate
            TproformalistSave_list.sworkfto = sworkfto
            TproformalistSave_list.inrno = inrno
            TproformalistSave_list.ackno = ackno
            TproformalistSave_list.ewayno = ewayno
            TproformalistSave_list.scategoryofservice = scategoryofservice
            TproformalistSave_list.stype1 = stype1
            TproformalistSave_list.sinvoicerefno = sinvoicerefno
            TproformalistSave_list.pono = pono
            TproformalistSave_list.note1 = note1 

            TproformalistSave_list.customerid = customerid
            TproformalistSave_list.customername = customername
            TproformalistSave_list.saddressclient = saddressclient
            TproformalistSave_list.scustomerpan = scustomerpan
            TproformalistSave_list.scustomergst = scustomergst
            TproformalistSave_list.sstatecode = sstatecode
            
            TproformalistSave_list.customersiteid = customersiteid
            TproformalistSave_list.customernamesite = customernamesite
            TproformalistSave_list.saddresssite = saddresssite 
            TproformalistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
            Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProformaListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformalist_list' : Tproformalist_list,
                                'Tproformadetailslist_list' : Tproformadetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 



        if 'cmdPrint' in request.POST: 
 


            Tserviceinvoicelist_list = Tproformalist.objects.get(salesbillid=lID) 
            if(Tserviceinvoicelist_list.ackno != ""):
                if(len(Tserviceinvoicelist_list.ackno) > 11):
                    my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
                else:
                    my_code = EAN13("34145421212121156", writer=ImageWriter())
            else:
                 my_code = EAN13("34121454212121156", writer=ImageWriter())

            my_code.save("new_code")
            Tserviceinvoicedetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            
            context = {
                    
                'title':'User list',  
                    'message':'Your User list page.',
                    'year':datetime.now().year,   
                    'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
                    'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
                } 
            
            
            pdf = render_to_pdf('BillingSol/ProformaListDetailsPrint.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        if 'cmdItemSave' in request.POST:  

            Tproformadetailslist_listG = Tproformadetailslist.objects.filter(salesbillid=lID).values() 

            TproformalistSave_list = Tproformalist.objects.get(salesbillid=lID) 

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
                           
                        TproformalistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformalistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformalistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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
                if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                    dsgst5 = dcgst5/2
                else:
                    dcgst50  =ltaxrateamt
            elif(ltaxrate == 12):
                dcgst12 =ltaxrateamt 
                if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                    dsgst12 = dcgst12/2
                else:
                    dcgst120  =ltaxrateamt
            elif(ltaxrate == 18):
                dcgst18 =ltaxrateamt 
                if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                    dsgst18 = dcgst18/2
                else:
                    dcgst180  =ltaxrateamt
            elif(ltaxrate == 28):
                dcgst28 =ltaxrateamt 
                if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                    dsgst28 = dcgst28/2
                else:
                    dcgst280  =ltaxrateamt


                

            ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)



            
            Tproformadetailslist_AddNewOBJ = Tproformadetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tproformadetailslist_AddNewOBJ.save()

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
            dcgst1pt0=0

                        

            if Tproformadetailslist_listG:
                for Tproformadetailslist_listGT in Tproformadetailslist_listG:
                    dtotal =dtotal + float(Tproformadetailslist_listGT['qty'] * Tproformadetailslist_listGT['unitprice'])

                    dcgst01 =dcgst01 + float(Tproformadetailslist_listGT['dcgst01'])
                    dcgst5 =dcgst5 + float(Tproformadetailslist_listGT['dcgst5'])
                    dsgst5 =dsgst5 + float(Tproformadetailslist_listGT['dsgst5'])
                    dcgst12 =dcgst12 + float(Tproformadetailslist_listGT['dcgst12'])
                    dsgst12 =dsgst12 + float(Tproformadetailslist_listGT['dsgst12'])
                    dcgst18 =dcgst18 + float(Tproformadetailslist_listGT['dcgst18'])
                    dsgst18 =dsgst18 + float(Tproformadetailslist_listGT['dsgst18'])
                    dcgst28 =dcgst28 + float(Tproformadetailslist_listGT['dcgst28'])
                    dsgst28 =dsgst28 + float(Tproformadetailslist_listGT['dsgst28']) 
                    dcgst1pt0=dcgst1pt0 + float(Tproformadetailslist_listGT['dcgst1pt0']) 
                    dcgst1pt0=dcgst1pt0 + float(Tproformadetailslist_listGT['dcgst1pt0']) 
                    
                    dtotalfinal =dtotalfinal + float(Tproformadetailslist_listGT['ddescitemtotal']) #Correct


                
            swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

            TproformalistSave_list.dtotal = dtotal
            TproformalistSave_list.dgsttrate = dcgst1pt0

            TproformalistSave_list.dsgst0 = 0
            TproformalistSave_list.dcgst0 = 0 
            TproformalistSave_list.digst0 = 0 




            TproformalistSave_list.dcgst01 = 0 
            TproformalistSave_list.dcgst5 = 0 
            TproformalistSave_list.dcgst12 = 0 
            TproformalistSave_list.dcgst18 = 0 
            TproformalistSave_list.dcgst28 = 0 

            TproformalistSave_list.dcgst01 = 0 
            TproformalistSave_list.dsgst5 = 0 
            TproformalistSave_list.dsgst12 = 0 
            TproformalistSave_list.dsgst18 = 0 
            TproformalistSave_list.dsgst28 = 0 


            TproformalistSave_list.dsgst01 = dsgst01 
            TproformalistSave_list.dsgst5 = dsgst5 
            TproformalistSave_list.dsgst12 = dsgst12 
            TproformalistSave_list.dsgst18 = dsgst18 
            TproformalistSave_list.dsgst28 = dsgst28  

            TproformalistSave_list.dcgst01 =dcgst01 
            TproformalistSave_list.dcgst5 = dcgst5 
            TproformalistSave_list.dcgst12 =dcgst12
            TproformalistSave_list.dcgst18 = dcgst18 
            TproformalistSave_list.dcgst28 = dcgst28

            TproformalistSave_list.dtotalfinal = dtotalfinal
            TproformalistSave_list.dtotalfinal = dtotalfinal
            TproformalistSave_list.swords = swords.upper()  

            TproformalistSave_list.bsitesez = bsitesez

            TproformalistSave_list.ackdate1 = ackdate1
            TproformalistSave_list.ackdate = ackdate
            TproformalistSave_list.ewaydate1 = ewaydate1
            TproformalistSave_list.ewaydate = ewaydate
            TproformalistSave_list.sdate1 = sdate1
            TproformalistSave_list.sdate = sdate
            TproformalistSave_list.podate1 = podate1
            TproformalistSave_list.podate = podate
            TproformalistSave_list.sworkfrom = sworkfrom
            TproformalistSave_list.sfromdate = sfromdate
            TproformalistSave_list.sworkfto = sworkfto
            TproformalistSave_list.stodate = stodate
            TproformalistSave_list.sworkfto = sworkfto
            TproformalistSave_list.inrno = inrno
            TproformalistSave_list.ackno = ackno
            TproformalistSave_list.ewayno = ewayno
            TproformalistSave_list.scategoryofservice = scategoryofservice
            TproformalistSave_list.stype1 = stype1
            TproformalistSave_list.sinvoicerefno = sinvoicerefno
            TproformalistSave_list.pono = pono
            TproformalistSave_list.note1 = note1 

            TproformalistSave_list.customerid = customerid
            TproformalistSave_list.customername = customername
            TproformalistSave_list.saddressclient = saddressclient
            TproformalistSave_list.scustomerpan = scustomerpan
            TproformalistSave_list.scustomergst = scustomergst
            TproformalistSave_list.sstatecode = sstatecode
            
            TproformalistSave_list.customersiteid = customersiteid
            TproformalistSave_list.customernamesite = customernamesite
            TproformalistSave_list.saddresssite = saddresssite 
            TproformalistSave_list.swords= swords.upper()
            TproformalistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
            Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProformaListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformalist_list' : Tproformalist_list,
                                'Tproformadetailslist_list' : Tproformadetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 

        if 'cmdItemSave1' in request.POST:  

            Tproformadetailslist_listG = Tproformadetailslist.objects.filter(salesbillid=lID).values() 

            TproformalistSave_list = Tproformalist.objects.get(salesbillid=lID) 
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
                           
                        TproformalistSave_list.spinsite = MsitelistGet.sstatecode
                        TproformalistSave_list.sstatesite = MsitelistGet.stempname1
                        TproformalistSave_list.scitysite = MsitelistGet.stempname2
                        
                        

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

            icountLoop =0
            icountLoopAll =0
            Tproformadetailslist_listGetLoop = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            icountLoopAll = Tproformadetailslist_listGetLoop.count()

            for Tproformadetailslist_listGetLoopA in Tproformadetailslist_listGetLoop:
                      
                icountLoop=Tproformadetailslist_listGetLoopA['salesordermultiid']  


                sdesc=data.get('txtItemDesc' + str(icountLoop))   
                qty=data.get('txtQuantity' + str(icountLoop))   
                unitprice=data.get('txtRate' + str(icountLoop)) 
                units=data.get('txtUnits' + str(icountLoop)) 
                ddescitemtotal=data.get('txtItemAmt' + str(icountLoop)) 
                shsn=data.get('txtHSNCode' + str(icountLoop)) 
                dtotal=data.get('txtItemTotalAmt' + str(icountLoop)) 
                ltaxrate=data.get('txtGSTRate' + str(icountLoop))   
                ltaxrateamt=data.get('txtGSTAmt' + str(icountLoop))   
                staxnotify=data.get('txtPOAMt' + str(icountLoop))   
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
                    if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                        dsgst5 = dcgst5/2
                    else:
                        dcgst50  =ltaxrateamt
                elif(ltaxrate == 12):
                    dcgst12 =ltaxrateamt 
                    if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                        dsgst12 = dcgst12/2
                    else:
                        dcgst120  =ltaxrateamt
                elif(ltaxrate == 18):
                    dcgst18 =ltaxrateamt 
                    if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                        dsgst18 = dcgst18/2
                    else:
                        dcgst180  =ltaxrateamt
                elif(ltaxrate == 28):
                    dcgst28 =ltaxrateamt 
                    if(TproformalistSave_list.sstatecode == TproformalistSave_list.slocationstatecode):
                        dsgst28 = dcgst28/2
                    else:
                        dcgst280  =ltaxrateamt


                    

                ddescitemtotal = round(dcgst1pt00 + ltaxrateamt)


                Tproformadetailslist_AddNewOBJ = Tproformadetailslist.objects.get(salesordermultiid=salesordermultiid) 
                
                Tproformadetailslist_AddNewOBJ.sdesc = sdesc
                Tproformadetailslist_AddNewOBJ.qty = qty
                Tproformadetailslist_AddNewOBJ.unitprice = unitprice
                Tproformadetailslist_AddNewOBJ.units = units
                Tproformadetailslist_AddNewOBJ.ddescitemtotal = ddescitemtotal
                Tproformadetailslist_AddNewOBJ.shsn = shsn
                Tproformadetailslist_AddNewOBJ.ssac = ssac
                Tproformadetailslist_AddNewOBJ.smanrate = smanrate
                Tproformadetailslist_AddNewOBJ.staxnotify = staxnotify
                Tproformadetailslist_AddNewOBJ.dsgst01 = dsgst01
                Tproformadetailslist_AddNewOBJ.dcgst01 = dcgst01
                Tproformadetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tproformadetailslist_AddNewOBJ.dcgst00 = dcgst00
                Tproformadetailslist_AddNewOBJ.dsgst5 = dsgst5
                Tproformadetailslist_AddNewOBJ.dcgst5 = dcgst5 
                
               
                Tproformadetailslist_AddNewOBJ.dcgst50=dcgst50
                Tproformadetailslist_AddNewOBJ.dsgst12=dsgst12
                Tproformadetailslist_AddNewOBJ.dcgst12=dcgst12
                Tproformadetailslist_AddNewOBJ.dcgst120=dcgst120
                Tproformadetailslist_AddNewOBJ.dsgst18=dsgst18
                Tproformadetailslist_AddNewOBJ.dcgst18=dcgst18
                Tproformadetailslist_AddNewOBJ.dcgst180=dcgst180
                Tproformadetailslist_AddNewOBJ.dsgst28=dsgst28
                Tproformadetailslist_AddNewOBJ.dcgst28=dcgst28
                Tproformadetailslist_AddNewOBJ.dcgst280=dcgst280
                Tproformadetailslist_AddNewOBJ.dgst28cess=dgst28cess 
                Tproformadetailslist_AddNewOBJ.dsgst0pt5=dsgst0pt5
                Tproformadetailslist_AddNewOBJ.dcgst0pt5=dcgst0pt5
                Tproformadetailslist_AddNewOBJ.dcgst0pt50=dcgst0pt50
                Tproformadetailslist_AddNewOBJ.dsgst2pt0=dsgst2pt0
                Tproformadetailslist_AddNewOBJ.dcgst2pt0=dcgst2pt0
                Tproformadetailslist_AddNewOBJ.dcgst2pt00=dcgst2pt00
                Tproformadetailslist_AddNewOBJ.dsgst2pt5=dsgst2pt5
                Tproformadetailslist_AddNewOBJ.dcgst2pt5=dcgst2pt5
                Tproformadetailslist_AddNewOBJ.dcgst2pt50=dcgst2pt50
                Tproformadetailslist_AddNewOBJ.dsgst1p0=dsgst1p0,
                Tproformadetailslist_AddNewOBJ.dcgst1pt0=dcgst1pt0
                Tproformadetailslist_AddNewOBJ.dcgst1pt00=dcgst1pt00

                Tproformadetailslist_AddNewOBJ.save()

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
                

                            

                if Tproformadetailslist_listG:
                    for Tproformadetailslist_listGT in Tproformadetailslist_listG:
                        dtotal =dtotal + float(Tproformadetailslist_listGT['qty'] * Tproformadetailslist_listGT['unitprice'])

                        dcgst01 =dcgst01 + float(Tproformadetailslist_listGT['dcgst01'])
                        dcgst5 =dcgst5 + float(Tproformadetailslist_listGT['dcgst5'])
                        dsgst5 =dsgst5 + float(Tproformadetailslist_listGT['dsgst5'])
                        dcgst12 =dcgst12 + float(Tproformadetailslist_listGT['dcgst12'])
                        dsgst12 =dsgst12 + float(Tproformadetailslist_listGT['dsgst12'])
                        dcgst18 =dcgst18 + float(Tproformadetailslist_listGT['dcgst18'])
                        dsgst18 =dsgst18 + float(Tproformadetailslist_listGT['dsgst18'])
                        dcgst28 =dcgst28 + float(Tproformadetailslist_listGT['dcgst28'])
                        dsgst28 =dsgst28 + float(Tproformadetailslist_listGT['dsgst28'])
                        dcgst1pt0=dcgst1pt0 + float(Tproformadetailslist_listGT['dcgst1pt0']) 
                        
                        dtotalfinal =dtotalfinal + float(Tproformadetailslist_listGT['ddescitemtotal']) #Correct


                    
                swords = "Rupees " + num2words(int(dtotalfinal), lang='en_IN')

                TproformalistSave_list.dtotal = dtotal
                TproformalistSave_list.dgsttrate = dcgst1pt0

                TproformalistSave_list.dsgst0 = 0
                TproformalistSave_list.dcgst0 = 0 
                TproformalistSave_list.digst0 = 0 




                TproformalistSave_list.dcgst01 = 0 
                TproformalistSave_list.dcgst5 = 0 
                TproformalistSave_list.dcgst12 = 0 
                TproformalistSave_list.dcgst18 = 0 
                TproformalistSave_list.dcgst28 = 0 

                TproformalistSave_list.dcgst01 = 0 
                TproformalistSave_list.dsgst5 = 0 
                TproformalistSave_list.dsgst12 = 0 
                TproformalistSave_list.dsgst18 = 0 
                TproformalistSave_list.dsgst28 = 0 


                TproformalistSave_list.dsgst01 = dsgst01 
                TproformalistSave_list.dsgst5 = dsgst5 
                TproformalistSave_list.dsgst12 = dsgst12 
                TproformalistSave_list.dsgst18 = dsgst18 
                TproformalistSave_list.dsgst28 = dsgst28  

                TproformalistSave_list.dcgst01 =dcgst01 
                TproformalistSave_list.dcgst5 = dcgst5 
                TproformalistSave_list.dcgst12 =dcgst12
                TproformalistSave_list.dcgst18 = dcgst18 
                TproformalistSave_list.dcgst28 = dcgst28

                TproformalistSave_list.dtotalfinal = dtotalfinal
                TproformalistSave_list.dtotalfinal = dtotalfinal
                TproformalistSave_list.swords = swords.upper()  

                TproformalistSave_list.ackdate1 = ackdate1
                TproformalistSave_list.ackdate = ackdate
                TproformalistSave_list.ewaydate1 = ewaydate1
                TproformalistSave_list.ewaydate = ewaydate
                TproformalistSave_list.sdate1 = sdate1
                TproformalistSave_list.sdate = sdate
                TproformalistSave_list.podate1 = podate1
                TproformalistSave_list.podate = podate
                TproformalistSave_list.sworkfrom = sworkfrom
                TproformalistSave_list.sfromdate = sfromdate
                TproformalistSave_list.sworkfto = sworkfto
                TproformalistSave_list.stodate = stodate
                TproformalistSave_list.sworkfto = sworkfto
                TproformalistSave_list.inrno = inrno
                TproformalistSave_list.ackno = ackno
                TproformalistSave_list.ewayno = ewayno
                TproformalistSave_list.scategoryofservice = scategoryofservice
                TproformalistSave_list.stype1 = stype1
                TproformalistSave_list.sinvoicerefno = sinvoicerefno
                TproformalistSave_list.pono = pono
                TproformalistSave_list.note1 = note1 

                TproformalistSave_list.customerid = customerid
                TproformalistSave_list.customername = customername
                TproformalistSave_list.saddressclient = saddressclient
                TproformalistSave_list.scustomerpan = scustomerpan
                TproformalistSave_list.scustomergst = scustomergst
                TproformalistSave_list.sstatecode = sstatecode
                
                TproformalistSave_list.customersiteid = customersiteid
                TproformalistSave_list.customernamesite = customernamesite
                TproformalistSave_list.saddresssite = saddresssite 
                TproformalistSave_list.swords= swords.upper()
                TproformalistSave_list.save()
            

            Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')  
            
            Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=customerid).values()     
    

            Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
            Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
            
            return render(request, "BillingSol/ProjectListDetails.html",
                            {
                                
                            'title':'User list',  
                                'message':'Your User list page.',
                                'year':datetime.now().year,  
                                'Msitelist_list' : Msitelist_list,
                                'Mcustomerlist_list' : Mcustomerlist_list,
                                'Tproformalist_list' : Tproformalist_list,
                                'Tproformadetailslist_list' : Tproformadetailslist_list,
                        'badmin':  request.session['badmin'],  
                        'bFinance':  request.session['bFinance'],  
                        'bpo':  request.session['bSupplyChain'],  
                        'bSales':  request.session['bSales'],  
                        'badmin1':  request.session['badmin1'],    
                            }
                            ) 






    else:   
        
        Mcustomerlist_list = Mcustomerlist.objects.order_by('customername')    
  

        Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 
        Tproformadetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
        Msitelist_list = Msitelist.objects.order_by('slocation', 'splace').filter(customerid=Tproformalist_list.customerid).values() 
          
        return render(request, "BillingSol/ProformaListDetails.html",
                        {
                            
                        'title':'User list',  
                            'message':'Your User list page.',
                            'year':datetime.now().year,  
                            'Msitelist_list' : Msitelist_list,
                            'Mcustomerlist_list' : Mcustomerlist_list,
                            'Tproformalist_list' : Tproformalist_list,
                            'Tproformadetailslist_list' : Tproformadetailslist_list,
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
 

    Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 

    customerid=Tproformalist_list.customerid
    customername=Tproformalist_list.customername
    saddress1=Tproformalist_list.saddress1
    saddress2=Tproformalist_list.saddress2
    saddress3=Tproformalist_list.saddress3
    spin=Tproformalist_list.spin
    scity=Tproformalist_list.scity
    sstate=Tproformalist_list.sstate
    scustomerpan=Tproformalist_list.scustomerpan
    scustomergst=Tproformalist_list.scustomergst
    customernamesite=Tproformalist_list.customernamesite
    saddress1site=Tproformalist_list.saddress1site
    saddress2site=Tproformalist_list.saddress2site
    saddress3site=Tproformalist_list.saddress3site
    spinsite=Tproformalist_list.spinsite
    scitysite=Tproformalist_list.scitysite
    sstatesite=Tproformalist_list.sstatesite
    pono=Tproformalist_list.pono
    podate=Tproformalist_list.podate
    dtotal=Tproformalist_list.dtotal
    dgsttrate=Tproformalist_list.dgsttrate
    dgst=Tproformalist_list.dgst
    dtotalfinal=Tproformalist_list.dtotalfinal
    swords=Tproformalist_list.swords
    sgstsplit=Tproformalist_list.sgstsplit
    note1=Tproformalist_list.note1
    note2=Tproformalist_list.note2
    inr=Tproformalist_list.inr
    scategoryofservice=Tproformalist_list.scategoryofservice
    username=Tproformalist_list.username
    stype1=Tproformalist_list.stype1
    sfile1=Tproformalist_list.sfile1
    sfolder1=Tproformalist_list.sfolder1
    snumber1=Tproformalist_list.snumber1
    customersiteid=Tproformalist_list.customersiteid
    sstatecode=Tproformalist_list.sstatecode
    sfromdate=Tproformalist_list.sfromdate
    stodate=Tproformalist_list.stodate
    dsgst0=Tproformalist_list.dsgst0
    dcgst0=Tproformalist_list.dcgst0
    digst0=Tproformalist_list.digst0
    lnoofedit=Tproformalist_list.lnoofedit
    ddateofedit=Tproformalist_list.ddateofedit
    ldepartmentid=Tproformalist_list.ldepartmentid
    sdepartmentname=Tproformalist_list.sdepartmentname
    bdelete=Tproformalist_list.bdelete
    bcancelcopy=Tproformalist_list.bcancelcopy
    bapproval0=Tproformalist_list.bapproval0
    bapproval01=Tproformalist_list.bapproval01
    bapproval02=Tproformalist_list.bapproval02
    bapproval03=Tproformalist_list.bapproval03
    bapproval04=Tproformalist_list.bapproval04
    bapproval05=Tproformalist_list.bapproval05
    bapproval06=Tproformalist_list.bapproval06
    bapproval07=Tproformalist_list.bapproval07
    bapproval08=Tproformalist_list.bapproval08
    bapproval09=Tproformalist_list.bapproval09
    bapproval010=Tproformalist_list.bapproval010
    scomments=Tproformalist_list.scomments
    scommentsdelete=Tproformalist_list.scommentsdelete
    lorderid=Tproformalist_list.lorderid
    dsgst01=Tproformalist_list.dsgst01
    dcgst01=Tproformalist_list.dcgst01
    dcgst00=Tproformalist_list.dcgst00
    dsgst5=Tproformalist_list.dsgst5
    dcgst5=Tproformalist_list.dcgst5
    dcgst50=Tproformalist_list.dcgst50
    dsgst12=Tproformalist_list.dsgst12
    dcgst12=Tproformalist_list.dcgst12
    dcgst120=Tproformalist_list.dcgst120
    dsgst18=Tproformalist_list.dsgst18
    dcgst18=Tproformalist_list.dcgst18
    dcgst180=Tproformalist_list.dcgst180
    dsgst28=Tproformalist_list.dsgst28
    dcgst28=Tproformalist_list.dcgst28
    dcgst280=Tproformalist_list.dcgst280
    dgst28cess=Tproformalist_list.dgst28cess
    dsgst0pt5=Tproformalist_list.dsgst0pt5
    dcgst0pt5=Tproformalist_list.dcgst0pt5
    dcgst0pt50=Tproformalist_list.dcgst0pt50
    dsgst2pt0=Tproformalist_list.dsgst2pt0
    dcgst2pt0=Tproformalist_list.dcgst2pt0
    dcgst2pt00=Tproformalist_list.dcgst2pt00
    dsgst2pt5=Tproformalist_list.dsgst2pt5
    dcgst2pt5=Tproformalist_list.dcgst2pt5
    dcgst2pt50=Tproformalist_list.dcgst2pt50
    dsgst1p0=Tproformalist_list.dsgst1p0
    dcgst1pt0=Tproformalist_list.dcgst1pt0
    dcgst1pt00=Tproformalist_list.dcgst1pt00
    saddressclient=Tproformalist_list.saddressclient
    saddresssite=Tproformalist_list.saddresssite
    scompanyaddress=Tproformalist_list.scompanyaddress
    sdate=Tproformalist_list.sdate
    sdate1=Tproformalist_list.sdate1
    llocationid=Tproformalist_list.llocationid
    slocation=Tproformalist_list.slocation
    slocationstatecode=Tproformalist_list.slocationstatecode
    slocationgstno=Tproformalist_list.slocationgstno
    slocationpanno=Tproformalist_list.slocationpanno
    slocationformat=Tproformalist_list.slocationformat
    bsitesez=Tproformalist_list.bsitesez
    sworkfrom=Tproformalist_list.sworkfrom
    sworkfto=Tproformalist_list.sworkfto
    podate1=Tproformalist_list.podate1
    bsamestate =Tproformalist_list.bsamestate 
    sfile11=Tproformalist_list.sfile11
    sfolder11=Tproformalist_list.sfolder11
    sfile12=Tproformalist_list.sfile12
    sfolder12=Tproformalist_list.sfolder12
    sfile13=Tproformalist_list.sfile13
    sfolder13=Tproformalist_list.sfolder13
    sfile14=Tproformalist_list.sfile14
    sfolder14=Tproformalist_list.sfolder14
    sfile15=Tproformalist_list.sfile15
    sfolder15=Tproformalist_list.sfolder15
 




 
    McompanylistGet = Mcompanylist.objects.get(locationid=llocationid) 
    if McompanylistGet:
        slocation = McompanylistGet.scompanyname  
        scompanyaddress = McompanylistGet.address1 + " " + McompanylistGet.address2 + " " + McompanylistGet.address3 + " " + McompanylistGet.scity + " " + McompanylistGet.lpin + " " + McompanylistGet.sstate
            
        slocationgstno=McompanylistGet.sgstno 
        slocationpanno=McompanylistGet.spanno
        slocationstatecode=McompanylistGet.sstatecode

        salesbillno=McompanylistGet.linvoice4 + 1
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
        sinvoicerefno=McompanylistGet.sformat4 + ssalesbillno + McompanylistGet.sformat 



        Mcompanylist_AddNewOBJ = Mcompanylist.objects.get(locationid=llocationid) 
        
        Mcompanylist_AddNewOBJ.linvoice4 = salesbillno
        Mcompanylist_AddNewOBJ.lyear = finyear 
        
        Mcompanylist_AddNewOBJ.save()

  
    McustomerlistGet = Mcustomerlist.objects.get(customerid=customerid) 
    if McustomerlistGet:
        customername = McustomerlistGet.customername 
        saddressclient = McustomerlistGet.address1 + " " + McustomerlistGet.address2 + " " + McustomerlistGet.address3 + " " + McustomerlistGet.scity + " " + McustomerlistGet.lpin + " " + McustomerlistGet.sstate
            
        scustomerpan=McustomerlistGet.panno
        scustomergst=McustomerlistGet.gstno
        sstatecode=McustomerlistGet.sstatecode
            


    Tproformalist_AddNewOBJ = Tproformalist(salesbillno=salesbillno , sfile11=sfile11, sfolder11=sfolder11 , sfile12=sfile12, sfolder12=sfolder12 , sfile13=sfile13, sfolder13=sfolder13 , sfile14=sfile14, sfolder14=sfolder14 , sfile15=sfile15, sfolder15=sfolder15, 	finyear=finyear, 	sinvoicerefno=sinvoicerefno, 	invoicedate=invoicedate, 	customerid=customerid, 	customername=customername, 	saddress1=saddress1, 	saddress2=saddress2, 	saddress3=saddress3, 	spin=spin, 	scity=scity, 	sstate=sstate, 	scustomerpan=scustomerpan, 	scustomergst=scustomergst, 	customernamesite=customernamesite, 	saddress1site=saddress1site, 	saddress2site=saddress2site, 	saddress3site=saddress3site, 	spinsite=spinsite, 	scitysite=scitysite, 	sstatesite=sstatesite, 	pono=pono, 	podate=podate, 	dtotal=dtotal, 	dgsttrate=dgsttrate, 	dgst=dgst, 	dtotalfinal=dtotalfinal, 	swords=swords, 	sgstsplit=sgstsplit, 	note1=note1, 	note2=note2, 	inr=inr, 	scategoryofservice=scategoryofservice, 	username=username, 	stype1=stype1, 	sfile1=sfile1, 	sfolder1=sfolder1, 	snumber1=snumber1, 	customersiteid=customersiteid, 	sstatecode=sstatecode, 	sfromdate=sfromdate, 	stodate=stodate, 	dsgst0=dsgst0, 	dcgst0=dcgst0, 	digst0=digst0, 	lnoofedit=lnoofedit, 	ddateofedit=ddateofedit, 	ldepartmentid=ldepartmentid, 	sdepartmentname=sdepartmentname, 	bdelete=bdelete, 	bcancelcopy=bcancelcopy, 	bapproval0=bapproval0, 	bapproval01=bapproval01, 	bapproval02=bapproval02, 	bapproval03=bapproval03, 	bapproval04=bapproval04, 	bapproval05=bapproval05, 	bapproval06=bapproval06, 	bapproval07=bapproval07, 	bapproval08=bapproval08, 	bapproval09=bapproval09, 	bapproval010=bapproval010, 	scomments=scomments, 	scommentsdelete=scommentsdelete, 	lorderid=lorderid, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00, 	saddressclient=saddressclient, 	saddresssite=saddresssite, 	scompanyaddress=scompanyaddress, 	inrno=inrno, 	ackno=ackno, 	ewayno=ewayno, 	ewaydate=ewaydate, 	ewaydate1=ewaydate1, 	sdate=sdate, 	sdate1=sdate1, 	llocationid=llocationid, 	slocation=slocation, 	slocationstatecode=slocationstatecode, 	slocationgstno=slocationgstno, 	slocationpanno=slocationpanno, 	slocationformat=slocationformat, 	bsitesez=bsitesez, 	sworkfrom=sworkfrom, 	sworkfto=sworkfto, ackdate=ackdate, ackdate1=ackdate1, podate1=podate1, bsamestate=bsamestate)

    Tproformalist_AddNewOBJ.save()
    salesbillid = Tproformalist_AddNewOBJ.salesbillid
  

    Tproformadetailslist_List = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformadetailslist:
        for TproformadetailslistQ in Tproformadetailslist_List:
            sdesc=TproformadetailslistQ['sdesc']
            partid=TproformadetailslistQ['partid']
            partno=TproformadetailslistQ['partno']
            qty=TproformadetailslistQ['qty']
            unitprice=TproformadetailslistQ['unitprice']
            units=TproformadetailslistQ['units']
            ddescitemtotal=TproformadetailslistQ['ddescitemtotal']
            shsn=TproformadetailslistQ['shsn']
            ssac=TproformadetailslistQ['ssac']
            smanrate=TproformadetailslistQ['smanrate']
            staxnotify=TproformadetailslistQ['staxnotify']
            dsgst01=TproformadetailslistQ['dsgst01']
            dcgst01=TproformadetailslistQ['dcgst01']
            dcgst00=TproformadetailslistQ['dcgst00']
            dsgst5=TproformadetailslistQ['dsgst5']
            dcgst5=TproformadetailslistQ['dcgst5']
            dcgst50=TproformadetailslistQ['dcgst50']
            dsgst12=TproformadetailslistQ['dsgst12']
            dcgst12=TproformadetailslistQ['dcgst12']
            dcgst120=TproformadetailslistQ['dcgst120']
            dsgst18=TproformadetailslistQ['dsgst18']
            dcgst18=TproformadetailslistQ['dcgst18']
            dcgst180=TproformadetailslistQ['dcgst180']
            dsgst28=TproformadetailslistQ['dsgst28']
            dcgst28=TproformadetailslistQ['dcgst28']
            dcgst280=TproformadetailslistQ['dcgst280']
            dgst28cess=TproformadetailslistQ['dgst28cess']
            dsgst0pt5=TproformadetailslistQ['dsgst0pt5']
            dcgst0pt5=TproformadetailslistQ['dcgst0pt5']
            dcgst0pt50=TproformadetailslistQ['dcgst0pt50']
            dsgst2pt0=TproformadetailslistQ['dsgst2pt0']
            dcgst2pt0=TproformadetailslistQ['dcgst2pt0']
            dcgst2pt00=TproformadetailslistQ['dcgst2pt00']
            dsgst2pt5=TproformadetailslistQ['dsgst2pt5']
            dcgst2pt5=TproformadetailslistQ['dcgst2pt5']
            dcgst2pt50=TproformadetailslistQ['dcgst2pt50']
            dsgst1p0=TproformadetailslistQ['dsgst1p0']
            dcgst1pt0=TproformadetailslistQ['dcgst1pt0']
            dcgst1pt00=TproformadetailslistQ['dcgst1pt00']


            
            Tproformadetailslist_AddNewOBJ = Tproformadetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tproformadetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProformaListDetails', lID=salesbillid)  


                        

@csrf_exempt
def ProformaListCopyInvoiceCreateDetails(request,lID):
    
    
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
 

    Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 

    customerid=Tproformalist_list.customerid
    customername=Tproformalist_list.customername
    saddress1=Tproformalist_list.saddress1
    saddress2=Tproformalist_list.saddress2
    saddress3=Tproformalist_list.saddress3
    spin=Tproformalist_list.spin
    scity=Tproformalist_list.scity
    sstate=Tproformalist_list.sstate
    scustomerpan=Tproformalist_list.scustomerpan
    scustomergst=Tproformalist_list.scustomergst
    customernamesite=Tproformalist_list.customernamesite
    saddress1site=Tproformalist_list.saddress1site
    saddress2site=Tproformalist_list.saddress2site
    saddress3site=Tproformalist_list.saddress3site
    spinsite=Tproformalist_list.spinsite
    scitysite=Tproformalist_list.scitysite
    sstatesite=Tproformalist_list.sstatesite
    pono=Tproformalist_list.pono
    podate=Tproformalist_list.podate
    dtotal=Tproformalist_list.dtotal
    dgsttrate=Tproformalist_list.dgsttrate
    dgst=Tproformalist_list.dgst
    dtotalfinal=Tproformalist_list.dtotalfinal
    swords=Tproformalist_list.swords
    sgstsplit=Tproformalist_list.sgstsplit
    note1=Tproformalist_list.note1
    note2=Tproformalist_list.note2
    inr=Tproformalist_list.inr
    scategoryofservice=Tproformalist_list.scategoryofservice
    username=Tproformalist_list.username
    stype1=Tproformalist_list.stype1
    sfile1=Tproformalist_list.sfile1
    sfolder1=Tproformalist_list.sfolder1
    snumber1=Tproformalist_list.snumber1
    customersiteid=Tproformalist_list.customersiteid
    sstatecode=Tproformalist_list.sstatecode
    sfromdate=Tproformalist_list.sfromdate
    stodate=Tproformalist_list.stodate
    dsgst0=Tproformalist_list.dsgst0
    dcgst0=Tproformalist_list.dcgst0
    digst0=Tproformalist_list.digst0
    lnoofedit=Tproformalist_list.lnoofedit
    ddateofedit=Tproformalist_list.ddateofedit
    ldepartmentid=Tproformalist_list.ldepartmentid
    sdepartmentname=Tproformalist_list.sdepartmentname
    bdelete=Tproformalist_list.bdelete
    bcancelcopy=Tproformalist_list.bcancelcopy
    bapproval0=Tproformalist_list.bapproval0
    bapproval01=Tproformalist_list.bapproval01
    bapproval02=Tproformalist_list.bapproval02
    bapproval03=Tproformalist_list.bapproval03
    bapproval04=Tproformalist_list.bapproval04
    bapproval05=Tproformalist_list.bapproval05
    bapproval06=Tproformalist_list.bapproval06
    bapproval07=Tproformalist_list.bapproval07
    bapproval08=Tproformalist_list.bapproval08
    bapproval09=Tproformalist_list.bapproval09
    bapproval010=Tproformalist_list.bapproval010
    scomments=Tproformalist_list.scomments
    scommentsdelete=Tproformalist_list.scommentsdelete
    lorderid=Tproformalist_list.lorderid
    dsgst01=Tproformalist_list.dsgst01
    dcgst01=Tproformalist_list.dcgst01
    dcgst00=Tproformalist_list.dcgst00
    dsgst5=Tproformalist_list.dsgst5
    dcgst5=Tproformalist_list.dcgst5
    dcgst50=Tproformalist_list.dcgst50
    dsgst12=Tproformalist_list.dsgst12
    dcgst12=Tproformalist_list.dcgst12
    dcgst120=Tproformalist_list.dcgst120
    dsgst18=Tproformalist_list.dsgst18
    dcgst18=Tproformalist_list.dcgst18
    dcgst180=Tproformalist_list.dcgst180
    dsgst28=Tproformalist_list.dsgst28
    dcgst28=Tproformalist_list.dcgst28
    dcgst280=Tproformalist_list.dcgst280
    dgst28cess=Tproformalist_list.dgst28cess
    dsgst0pt5=Tproformalist_list.dsgst0pt5
    dcgst0pt5=Tproformalist_list.dcgst0pt5
    dcgst0pt50=Tproformalist_list.dcgst0pt50
    dsgst2pt0=Tproformalist_list.dsgst2pt0
    dcgst2pt0=Tproformalist_list.dcgst2pt0
    dcgst2pt00=Tproformalist_list.dcgst2pt00
    dsgst2pt5=Tproformalist_list.dsgst2pt5
    dcgst2pt5=Tproformalist_list.dcgst2pt5
    dcgst2pt50=Tproformalist_list.dcgst2pt50
    dsgst1p0=Tproformalist_list.dsgst1p0
    dcgst1pt0=Tproformalist_list.dcgst1pt0
    dcgst1pt00=Tproformalist_list.dcgst1pt00
    saddressclient=Tproformalist_list.saddressclient
    saddresssite=Tproformalist_list.saddresssite
    scompanyaddress=Tproformalist_list.scompanyaddress
    sdate=Tproformalist_list.sdate
    sdate1=Tproformalist_list.sdate1
    llocationid=Tproformalist_list.llocationid
    slocation=Tproformalist_list.slocation
    slocationstatecode=Tproformalist_list.slocationstatecode
    slocationgstno=Tproformalist_list.slocationgstno
    slocationpanno=Tproformalist_list.slocationpanno
    slocationformat=Tproformalist_list.slocationformat
    bsitesez=Tproformalist_list.bsitesez
    sworkfrom=Tproformalist_list.sworkfrom
    sworkfto=Tproformalist_list.sworkfto
    podate1=Tproformalist_list.podate1
    bsamestate =Tproformalist_list.bsamestate 
    sfile11=Tproformalist_list.sfile11
    sfolder11=Tproformalist_list.sfolder11
    sfile12=Tproformalist_list.sfile12
    sfolder12=Tproformalist_list.sfolder12
    sfile13=Tproformalist_list.sfile13
    sfolder13=Tproformalist_list.sfolder13
    sfile14=Tproformalist_list.sfile14
    sfolder14=Tproformalist_list.sfolder14
    sfile15=Tproformalist_list.sfile15
    sfolder15=Tproformalist_list.sfolder15
 




 
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
  

    Tproformadetailslist_List = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformadetailslist:
        for TproformadetailslistQ in Tproformadetailslist_List:
            sdesc=TproformadetailslistQ['sdesc']
            partid=TproformadetailslistQ['partid']
            partno=TproformadetailslistQ['partno']
            qty=TproformadetailslistQ['qty']
            unitprice=TproformadetailslistQ['unitprice']
            units=TproformadetailslistQ['units']
            ddescitemtotal=TproformadetailslistQ['ddescitemtotal']
            shsn=TproformadetailslistQ['shsn']
            ssac=TproformadetailslistQ['ssac']
            smanrate=TproformadetailslistQ['smanrate']
            staxnotify=TproformadetailslistQ['staxnotify']
            dsgst01=TproformadetailslistQ['dsgst01']
            dcgst01=TproformadetailslistQ['dcgst01']
            dcgst00=TproformadetailslistQ['dcgst00']
            dsgst5=TproformadetailslistQ['dsgst5']
            dcgst5=TproformadetailslistQ['dcgst5']
            dcgst50=TproformadetailslistQ['dcgst50']
            dsgst12=TproformadetailslistQ['dsgst12']
            dcgst12=TproformadetailslistQ['dcgst12']
            dcgst120=TproformadetailslistQ['dcgst120']
            dsgst18=TproformadetailslistQ['dsgst18']
            dcgst18=TproformadetailslistQ['dcgst18']
            dcgst180=TproformadetailslistQ['dcgst180']
            dsgst28=TproformadetailslistQ['dsgst28']
            dcgst28=TproformadetailslistQ['dcgst28']
            dcgst280=TproformadetailslistQ['dcgst280']
            dgst28cess=TproformadetailslistQ['dgst28cess']
            dsgst0pt5=TproformadetailslistQ['dsgst0pt5']
            dcgst0pt5=TproformadetailslistQ['dcgst0pt5']
            dcgst0pt50=TproformadetailslistQ['dcgst0pt50']
            dsgst2pt0=TproformadetailslistQ['dsgst2pt0']
            dcgst2pt0=TproformadetailslistQ['dcgst2pt0']
            dcgst2pt00=TproformadetailslistQ['dcgst2pt00']
            dsgst2pt5=TproformadetailslistQ['dsgst2pt5']
            dcgst2pt5=TproformadetailslistQ['dcgst2pt5']
            dcgst2pt50=TproformadetailslistQ['dcgst2pt50']
            dsgst1p0=TproformadetailslistQ['dsgst1p0']
            dcgst1pt0=TproformadetailslistQ['dcgst1pt0']
            dcgst1pt00=TproformadetailslistQ['dcgst1pt00']


            
            Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tinvoicedetailslist_AddNewOBJ.save()
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProjectListDetails', lID=salesbillid)  




           

@csrf_exempt
def ProformaListCopyInvoiceSEZCreateDetails(request,lID):
    
    
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
    bsitesez=1
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
 

    Tproformalist_list = Tproformalist.objects.get(salesbillid=lID) 

    customerid=Tproformalist_list.customerid
    customername=Tproformalist_list.customername
    saddress1=Tproformalist_list.saddress1
    saddress2=Tproformalist_list.saddress2
    saddress3=Tproformalist_list.saddress3
    spin=Tproformalist_list.spin
    scity=Tproformalist_list.scity
    sstate=Tproformalist_list.sstate
    scustomerpan=Tproformalist_list.scustomerpan
    scustomergst=Tproformalist_list.scustomergst
    customernamesite=Tproformalist_list.customernamesite
    saddress1site=Tproformalist_list.saddress1site
    saddress2site=Tproformalist_list.saddress2site
    saddress3site=Tproformalist_list.saddress3site
    spinsite=Tproformalist_list.spinsite
    scitysite=Tproformalist_list.scitysite
    sstatesite=Tproformalist_list.sstatesite
    pono=Tproformalist_list.pono
    podate=Tproformalist_list.podate
    dtotal=Tproformalist_list.dtotal
    dgsttrate=Tproformalist_list.dgsttrate
    dgst=Tproformalist_list.dgst
    dtotalfinal=Tproformalist_list.dtotalfinal
    swords=Tproformalist_list.swords
    sgstsplit=Tproformalist_list.sgstsplit
    note1=Tproformalist_list.note1
    note2=Tproformalist_list.note2
    inr=Tproformalist_list.inr
    scategoryofservice=Tproformalist_list.scategoryofservice
    username=Tproformalist_list.username
    stype1=Tproformalist_list.stype1
    sfile1=Tproformalist_list.sfile1
    sfolder1=Tproformalist_list.sfolder1
    snumber1=Tproformalist_list.snumber1
    customersiteid=Tproformalist_list.customersiteid
    sstatecode=Tproformalist_list.sstatecode
    sfromdate=Tproformalist_list.sfromdate
    stodate=Tproformalist_list.stodate
    dsgst0=Tproformalist_list.dsgst0
    dcgst0=Tproformalist_list.dcgst0
    digst0=Tproformalist_list.digst0
    lnoofedit=Tproformalist_list.lnoofedit
    ddateofedit=Tproformalist_list.ddateofedit
    ldepartmentid=Tproformalist_list.ldepartmentid
    sdepartmentname=Tproformalist_list.sdepartmentname
    bdelete=Tproformalist_list.bdelete
    bcancelcopy=Tproformalist_list.bcancelcopy
    bapproval0=Tproformalist_list.bapproval0
    bapproval01=Tproformalist_list.bapproval01
    bapproval02=Tproformalist_list.bapproval02
    bapproval03=Tproformalist_list.bapproval03
    bapproval04=Tproformalist_list.bapproval04
    bapproval05=Tproformalist_list.bapproval05
    bapproval06=Tproformalist_list.bapproval06
    bapproval07=Tproformalist_list.bapproval07
    bapproval08=Tproformalist_list.bapproval08
    bapproval09=Tproformalist_list.bapproval09
    bapproval010=Tproformalist_list.bapproval010
    scomments=Tproformalist_list.scomments
    scommentsdelete=Tproformalist_list.scommentsdelete
    lorderid=Tproformalist_list.lorderid
    dsgst01=Tproformalist_list.dsgst01
    dcgst01=Tproformalist_list.dcgst01
    dcgst00=Tproformalist_list.dcgst00
    dsgst5=Tproformalist_list.dsgst5
    dcgst5=Tproformalist_list.dcgst5
    dcgst50=Tproformalist_list.dcgst50
    dsgst12=Tproformalist_list.dsgst12
    dcgst12=Tproformalist_list.dcgst12
    dcgst120=Tproformalist_list.dcgst120
    dsgst18=Tproformalist_list.dsgst18
    dcgst18=Tproformalist_list.dcgst18
    dcgst180=Tproformalist_list.dcgst180
    dsgst28=Tproformalist_list.dsgst28
    dcgst28=Tproformalist_list.dcgst28
    dcgst280=Tproformalist_list.dcgst280
    dgst28cess=Tproformalist_list.dgst28cess
    dsgst0pt5=Tproformalist_list.dsgst0pt5
    dcgst0pt5=Tproformalist_list.dcgst0pt5
    dcgst0pt50=Tproformalist_list.dcgst0pt50
    dsgst2pt0=Tproformalist_list.dsgst2pt0
    dcgst2pt0=Tproformalist_list.dcgst2pt0
    dcgst2pt00=Tproformalist_list.dcgst2pt00
    dsgst2pt5=Tproformalist_list.dsgst2pt5
    dcgst2pt5=Tproformalist_list.dcgst2pt5
    dcgst2pt50=Tproformalist_list.dcgst2pt50
    dsgst1p0=Tproformalist_list.dsgst1p0
    dcgst1pt0=Tproformalist_list.dcgst1pt0
    dcgst1pt00=Tproformalist_list.dcgst1pt00
    saddressclient=Tproformalist_list.saddressclient
    saddresssite=Tproformalist_list.saddresssite
    scompanyaddress=Tproformalist_list.scompanyaddress
    sdate=Tproformalist_list.sdate
    sdate1=Tproformalist_list.sdate1
    llocationid=Tproformalist_list.llocationid
    slocation=Tproformalist_list.slocation
    slocationstatecode=Tproformalist_list.slocationstatecode
    slocationgstno=Tproformalist_list.slocationgstno
    slocationpanno=Tproformalist_list.slocationpanno
    slocationformat=Tproformalist_list.slocationformat
    bsitesez=Tproformalist_list.bsitesez
    sworkfrom=Tproformalist_list.sworkfrom
    sworkfto=Tproformalist_list.sworkfto
    podate1=Tproformalist_list.podate1
    bsamestate =Tproformalist_list.bsamestate 
    sfile11=Tproformalist_list.sfile11
    sfolder11=Tproformalist_list.sfolder11
    sfile12=Tproformalist_list.sfile12
    sfolder12=Tproformalist_list.sfolder12
    sfile13=Tproformalist_list.sfile13
    sfolder13=Tproformalist_list.sfolder13
    sfile14=Tproformalist_list.sfile14
    sfolder14=Tproformalist_list.sfolder14
    sfile15=Tproformalist_list.sfile15
    sfolder15=Tproformalist_list.sfolder15
 




 
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
  

    Tproformadetailslist_List = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
    
    if Tproformadetailslist:
        for TproformadetailslistQ in Tproformadetailslist_List:
            sdesc=TproformadetailslistQ['sdesc']
            partid=TproformadetailslistQ['partid']
            partno=TproformadetailslistQ['partno']
            qty=TproformadetailslistQ['qty']
            unitprice=TproformadetailslistQ['unitprice']
            units=TproformadetailslistQ['units']
            ddescitemtotal=TproformadetailslistQ['ddescitemtotal']
            shsn=TproformadetailslistQ['shsn']
            ssac=TproformadetailslistQ['ssac']
            smanrate=TproformadetailslistQ['smanrate']
            staxnotify=TproformadetailslistQ['staxnotify']
            dsgst01=TproformadetailslistQ['dsgst01']
            dcgst01=TproformadetailslistQ['dcgst01']
            dcgst00=TproformadetailslistQ['dcgst00']
            dsgst5=TproformadetailslistQ['dsgst5']
            dcgst5=TproformadetailslistQ['dcgst5']
            dcgst50=TproformadetailslistQ['dcgst50']
            dsgst12=TproformadetailslistQ['dsgst12']
            dcgst12=TproformadetailslistQ['dcgst12']
            dcgst120=TproformadetailslistQ['dcgst120']
            dsgst18=TproformadetailslistQ['dsgst18']
            dcgst18=TproformadetailslistQ['dcgst18']
            dcgst180=TproformadetailslistQ['dcgst180']
            dsgst28=TproformadetailslistQ['dsgst28']
            dcgst28=TproformadetailslistQ['dcgst28']
            dcgst280=TproformadetailslistQ['dcgst280']
            dgst28cess=TproformadetailslistQ['dgst28cess']
            dsgst0pt5=TproformadetailslistQ['dsgst0pt5']
            dcgst0pt5=TproformadetailslistQ['dcgst0pt5']
            dcgst0pt50=TproformadetailslistQ['dcgst0pt50']
            dsgst2pt0=TproformadetailslistQ['dsgst2pt0']
            dcgst2pt0=TproformadetailslistQ['dcgst2pt0']
            dcgst2pt00=TproformadetailslistQ['dcgst2pt00']
            dsgst2pt5=TproformadetailslistQ['dsgst2pt5']
            dcgst2pt5=TproformadetailslistQ['dcgst2pt5']
            dcgst2pt50=TproformadetailslistQ['dcgst2pt50']
            dsgst1p0=TproformadetailslistQ['dsgst1p0']
            dcgst1pt0=TproformadetailslistQ['dcgst1pt0']
            dcgst1pt00=TproformadetailslistQ['dcgst1pt00']


            
            Tinvoicedetailslist_AddNewOBJ = Tinvoicedetailslist( 	salesbillid=salesbillid, 	sdesc=sdesc, 	partid=partid, 	partno=partno, 	qty=qty, 	unitprice=unitprice, 	units=units, 	ddescitemtotal=ddescitemtotal, 	shsn=shsn, 	ssac=ssac, 	smanrate=smanrate, 	staxnotify=staxnotify, 	dsgst01=dsgst01, 	dcgst01=dcgst01, 	dcgst00=dcgst00, 	dsgst5=dsgst5, 	dcgst5=dcgst5, 	dcgst50=dcgst50, 	dsgst12=dsgst12, 	dcgst12=dcgst12, 	dcgst120=dcgst120, 	dsgst18=dsgst18, 	dcgst18=dcgst18, 	dcgst180=dcgst180, 	dsgst28=dsgst28, 	dcgst28=dcgst28, 	dcgst280=dcgst280, 	dgst28cess=dgst28cess, 	dsgst0pt5=dsgst0pt5, 	dcgst0pt5=dcgst0pt5, 	dcgst0pt50=dcgst0pt50, 	dsgst2pt0=dsgst2pt0, 	dcgst2pt0=dcgst2pt0, 	dcgst2pt00=dcgst2pt00, 	dsgst2pt5=dsgst2pt5, 	dcgst2pt5=dcgst2pt5, 	dcgst2pt50=dcgst2pt50, 	dsgst1p0=dsgst1p0, 	dcgst1pt0=dcgst1pt0, 	dcgst1pt00=dcgst1pt00)

            Tinvoicedetailslist_AddNewOBJ.save()
            
            
        
            
            
        


    # Details.objects.filter(id=pk).delete() 
    return redirect('ProjectListSEZDetails', lID=salesbillid)  







@csrf_exempt
def ProformaListPrintDetails(request,lID):
    
    
    salesbillid=0
       


    Tserviceinvoicelist_list = Tproformalist.objects.get(salesbillid=lID) 
    if(Tserviceinvoicelist_list.ackno != ""):
        if(len(Tserviceinvoicelist_list.ackno) > 11):
            my_code = EAN13(Tserviceinvoicelist_list.ackno, writer=ImageWriter()) 
        else:
            my_code = EAN13("34145421212121156", writer=ImageWriter())
    else:
            my_code = EAN13("34121454212121156", writer=ImageWriter())

    my_code.save("new_code")
    Tserviceinvoicedetailslist_list = Tproformadetailslist.objects.filter(salesbillid=lID).values() 
    
    context = {
            
        'title':'User list',  
            'message':'Your User list page.',
            'year':datetime.now().year,   
            'Tserviceinvoicelist_list' : Tserviceinvoicelist_list,
            'Tserviceinvoicedetailslist_list' : Tserviceinvoicedetailslist_list, 
        } 
    
    
    pdf = render_to_pdf('BillingSol/ProformaListDetailsPrint.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

    