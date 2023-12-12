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
def home(request):
    request.session['username']  =""
    request.session['sname']  =""
    request.session['sadmin']  =False
    if request.method == "POST":


        data = request.POST 
        if 'btnGo' in request.POST:  
            
            UserlistPWDAdmin = Userlist.objects.filter(u1_username=data.get("txtEmployeeID"), u1_password=data.get("txtPassword")).values()
            if UserlistPWDAdmin:
                for UserlistPWDAdminA in UserlistPWDAdmin.all():   
                    if( UserlistPWDAdminA['bblock'] == False):
                        lUnitId = 0
                        request.session['username']  =UserlistPWDAdminA['u1_username']
                        request.session['sname']  =UserlistPWDAdminA['sname']
                        if(UserlistPWDAdminA['sadmin'] == True):
                            request.session['sadmin']  =True
                        return redirect("Dashboard")  
                return render(request, "BillingSol/home.html")
            else:
                return render(request, "BillingSol/home.html")

    else:
        return render(request, "BillingSol/home.html")
    

    
@csrf_exempt
def Dashboard(request):
    if request.method == "POST":
        data = request.POST 

    else:
        return render(request, "BillingSol/Dashboard.html")
