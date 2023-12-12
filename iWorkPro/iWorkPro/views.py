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
from django.core import mail

from django.core.files.storage import FileSystemStorage
from os import urandom

import random
import array

from django.core.mail import send_mail

import iWorkPro_project.settings
#import textutils.settings


import threading as th
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from iWorkPro.models import Aemployeelist, Aemployeedoclist, Aprojectcategorylist, Adepartmentlist
from iWorkPro.models import Acustomerlst, Acustomercontactlist, Adesignationlist, Aprojectcategorysublist, Aprojectcategorysubtasklist
from iWorkPro.models import Projectdoclist , Projecttasklist, Projectsublist, Projectmainlist, Projecttaskdetailslist 


@csrf_exempt
def Logout(request):

    request.session['lLoginID']  =0
    request.session['username']  =""
    request.session['sname']  =""
    request.session['badmin']  =0
    request.session['bEmployee']  =0
    request.session['bCustomer']  =0
    request.session['bEmployeePM']  =0
    request.session['bEmployeeManagement']  =0
    request.session['bothers']  =0
    request.session['btester']  =0
    request.session['bdeveloper']  =0
    request.session['bpm']  =0
  

    badmin  =0
    bEmployee  =0
    bCustomer  =0
    bEmployeePM  =0
    bEmployeeManagement  =0
    bothers  =0
    btester  =0
    bdeveloper  =0
    bpm  =0
  



    u1_username=""
    u1_password=""
    radEmployee=0
    radiCustomer=0

 
    return redirect("home")  






@csrf_exempt
def home(request):
    # print(request.POST)

    request.session['lcustomerid']  =0


    if request.method == "POST":
        data = request.POST  


        if 'cmdForgotPassword' in request.POST:  
            u1_username=data.get("typeEmailX")  
            if(u1_username==""):
                
                messages.error(request, 'Login ID is not entered.Please enter and try!')
                return render(request, "iWorkPro/home.html", 
                    {
                                        'title':'Login list', 
                                        'message':'Your Login list page.',
                                        'bHome':1,
                                        'year':datetime.now().year,  
                                        'sName':request.session['sname'] , 
                                        'Menu1':'', 
                                        'Menu2':'', 
                                        'Menu3':'', 
                                        'Menu4':'', 
                                        'Menu5':'',   
                                        'MenuName1':'', 
                                        'MenuName2':'', 
                                        'MenuName3':'', 
                                        'MenuName4':'', 
                                        'MenuName5':'',   
                    }
                                        )
            else:

                chars = ""
                chars = "ABCDEFGHJKLMNPQRSTUVWXYZ123456789"
                chars1 = ""
                chars1 = "9@#*123456789@#*abcdefghijklmnopqrstuvwxyz9@#*" 
                chars2 = ""
                chars2 = "9@#*abcdefghijklmnopqrstuvwxyz@#*123456789" 
                length=0
                length=4

                sPassword1 = ""
                sPassword1 = "".join(chars[c % len(chars)] for c in urandom(length))

                length=4

                sPassword2 = ""
                sPassword2 = "".join(chars1[c % len(chars1)] for c in urandom(length))
                length=4

                sPassword3 = ""
                sPassword3 = "".join(chars2[c % len(chars2)] for c in urandom(length))

                sPassword = ""
                sPassword = sPassword3 + sPassword1 + sPassword2

                lUserId =0
                sEmail = ""
                UserlistPWDAdmin = Aemployeelist.objects.filter(sempid=u1_username).values()
                if UserlistPWDAdmin:
                    for UserlistPWDAdminA in UserlistPWDAdmin.all():   
                        if( UserlistPWDAdminA['bactive'] == 1):
                            lUserId = UserlistPWDAdminA['lid']
                            sEmail = UserlistPWDAdminA['sempemailid']
                            connection = mail.get_connection()
                            email1 = mail.EmailMessage(
                                    "iWorkPro Password Change Information",
                                "Hi, \n Information from www.Dhruthi.org:8004 - iWorkPro \n For your ID : " + u1_username + " \n Your new Password : " + sPassword + "\n\n\n This is notification Mail. Please Don't Reply",
                                "iworkproalerts@dhruthi.org",
                                [sEmail],
                                connection=connection,
                            )
                            email1.send()

                            UserlistPWDAdminSave = Aemployeelist.objects.get(lid=lUserId)
                            UserlistPWDAdminSave.spassword = sPassword
                            UserlistPWDAdminSave.save()
                            messages.success(request, 'Password is mailed to your Registered eMail Address!')
                            return render(request, "iWorkPro/home.html", 
                                        {
                                                            'title':'Login list', 
                                                            'message':'Your Login list page.',
                                                            'bHome':1,
                                                            'year':datetime.now().year,  
                                                            'sName':request.session['sname'] , 
                                                            'Menu1':'', 
                                                            'Menu2':'', 
                                                            'Menu3':'', 
                                                            'Menu4':'', 
                                                            'Menu5':'',   
                                                            'MenuName1':'', 
                                                            'MenuName2':'', 
                                                            'MenuName3':'', 
                                                            'MenuName4':'', 
                                                            'MenuName5':'',   
                                        }
                                                            )
                else:

                    lUserId =0
                    sEmail = ""
                    UserlistPWDAdmin = Acustomercontactlist.objects.filter(suserid=u1_username).values()
                    if UserlistPWDAdmin:
                        for UserlistPWDAdminA in UserlistPWDAdmin.all():   
                            if( UserlistPWDAdminA['bactive'] == 1):
                                lUserId = UserlistPWDAdminA['lid']
                                sEmail = UserlistPWDAdminA['lcustomercontactid']
                                connection = mail.get_connection()
                                email1 = mail.EmailMessage(
                                    "iWorkPro Password Change Information",
                                    "Hi, \n Information from www.Dhruthi.org:8004 - iWorkPro \n For your ID : " + u1_username + " \n Your new Password : " + sPassword + "\n\n\n This is notification Mail. Please Don't Reply",
                                    "iworkproalerts@dhruthi.org",
                                    [sEmail],
                                    connection=connection,
                                )
                                email1.send()

                                UserlistPWDAdminSave = Acustomercontactlist.objects.get(lcustomercontactid=lUserId)
                                UserlistPWDAdminSave.spassword = sPassword
                                UserlistPWDAdminSave.save()
                                messages.success(request, 'Password is mailed to your Registered eMail Address!')
                                return render(request, "iWorkPro/home.html", 
                                            {
                                                                'title':'Login list', 
                                                                'message':'Your Login list page.',
                                                                'bHome':1,
                                                                'year':datetime.now().year,  
                                                                'sName':request.session['sname'] , 
                                                                'Menu1':'', 
                                                                'Menu2':'', 
                                                                'Menu3':'', 
                                                                'Menu4':'', 
                                                                'Menu5':'',   
                                                                'MenuName1':'', 
                                                                'MenuName2':'', 
                                                                'MenuName3':'', 
                                                                'MenuName4':'', 
                                                                'MenuName5':'',   
                                            }
                                                                )
                
        if 'btnGo' in request.POST:  
            u1_username=data.get("typeEmailX")    
            u1_password=data.get("typePasswordX")    

                               
            radType=data.get('radType') 

            if(radType == 'Employee'):
                radEmployee = 1
                radiCustomer = 0 
            else:
                radiCustomer = 1   
                radEmployee = 0   

            request.session['bEmployee']  =radEmployee
            request.session['bCustomer']  =radiCustomer  

            if(radEmployee==1):
            
                UserlistPWDAdmin = Aemployeelist.objects.filter(sempid=u1_username, spassword=u1_password).values()
                if UserlistPWDAdmin:
                    for UserlistPWDAdminA in UserlistPWDAdmin.all():   
                        if( UserlistPWDAdminA['bactive'] == 1):
                            request.session['lLoginID']  =UserlistPWDAdminA['lid']
                            request.session['username']  =UserlistPWDAdminA['sempid']
                            request.session['sname']  =UserlistPWDAdminA['susername']
                            request.session['badmin']  =UserlistPWDAdminA['badmin'] 
                            request.session['bEmployeePM']  =UserlistPWDAdminA['bprojectmanager']
                            request.session['bEmployeeManagement']  =UserlistPWDAdminA['bmanagement']
                            request.session['bothers']  =UserlistPWDAdminA['bothers']
                            request.session['btester']  =UserlistPWDAdminA['btester']
                            request.session['bdeveloper']   =UserlistPWDAdminA['bdeveloper']
                            request.session['bpm']  =UserlistPWDAdminA['bpm']
                            badmin  =UserlistPWDAdminA['badmin']  
                            bEmployeePM  =UserlistPWDAdminA['bprojectmanager']
                            bEmployeeManagement  =UserlistPWDAdminA['bmanagement']
                            bothers  =UserlistPWDAdminA['bothers']
                            btester  =UserlistPWDAdminA['btester']
                            bdeveloper  =UserlistPWDAdminA['bdeveloper']
                            bpm  =UserlistPWDAdminA['bpm']

                            return redirect("Dashboard")  
            else:
                UserlistPWDAdmin = Acustomercontactlist.objects.filter(suserid=u1_username, spassword=u1_password).values()
                if UserlistPWDAdmin:
                    for UserlistPWDAdminA in UserlistPWDAdmin.all():   
                        if( UserlistPWDAdminA['bactive'] == 1):
                            request.session['lLoginID']  =UserlistPWDAdminA['lid']
                            request.session['lcustomerid']  =UserlistPWDAdminA['lcustomerid']
                            request.session['username']  =UserlistPWDAdminA['scustomercontactname']
                            request.session['sname']  =UserlistPWDAdminA['suserid'] 
                            return redirect("DashboardCustomer")  




        return render(request, "iWorkPro/home.html", 
                    {
                                        'title':'Login list', 
                                        'message':'Your Login list page.',
                                        'bHome':1,
                                        'year':datetime.now().year,  
                                        'sName':request.session['sname'] , 
                                        'Menu1':'', 
                                        'Menu2':'', 
                                        'Menu3':'', 
                                        'Menu4':'', 
                                        'Menu5':'',   
                                        'MenuName1':'', 
                                        'MenuName2':'', 
                                        'MenuName3':'', 
                                        'MenuName4':'', 
                                        'MenuName5':'',   
                    }
                                        )

    else:
         
        request.session['lLoginID']  =0
        request.session['username']  =""
        request.session['sname']  =""
        request.session['badmin']  =0
        request.session['bEmployee']  =0
        request.session['bCustomer']  =0
        request.session['bEmployeePM']  =0
        request.session['bEmployeeManagement']  =0
        request.session['bothers']  =0
        request.session['btester']  =0
        request.session['bdeveloper']  =0
        request.session['bpm']  =0
    

        badmin  =0
        bEmployee  =0
        bCustomer  =0
        bEmployeePM  =0
        bEmployeeManagement  =0
        bothers  =0
        btester  =0
        bdeveloper  =0
        bpm  =0
    



        u1_username=""
        u1_password=""
        radEmployee=0
        radiCustomer=0
        return render(request, "iWorkPro/home.html", 
                    {
                                        'title':'Login list', 
                                        'message':'Your Login list page.',
                                        'year':datetime.now().year,    
                                        'bHome':1,
                                        
                                        'sName':request.session['sname'] , 
                                        'Menu1':'',  
                                        'Menu2':'', 
                                        'Menu3':'', 
                                        'Menu4':'', 
                                        'Menu5':'', 
                                        'MenuName1':'', 
                                        'MenuName2':'', 
                                        'MenuName3':'', 
                                        'MenuName4':'', 
                                        'MenuName5':'',   
                    }
                                        )



@csrf_exempt
def Dashboard(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    lLoginID =0
    lLoginID = int(request.session['lLoginID'])
 
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Projectmainlist_list = Projectmainlist.objects.filter(sprojectname__contains = txtSearch) | Projectmainlist.objects.filter(scustomername__contains = txtSearch).order_by('-lid').values() 
            
         
            return render(request, "iWorkPro/dashboard.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 1 ,  
                        'bCustomer': 0 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Projectmainlist_list = Projectmainlist.objects.order_by('-lid') 
         
            return render(request, "iWorkPro/dashboard.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] , 
                        'bEmployee': 1 ,  
                        'bCustomer': 0 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
            }
                        )
    else:  


        Projectmainlist_list = Projectmainlist.objects.order_by('-lid') 
         
        return render(request, "iWorkPro/dashboard.html", 
        {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,  
                        'bEmployee': 1 ,  
                        'bCustomer': 0 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
        }
                    )



@csrf_exempt
def CreateProject(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtName=""

    lprojectno = 0
    lprojectsubnocount = 0
    lcustomerid = 0
    lprojectownerid = 0
    ltotalsubproject = 0
    ltotalsubprojectopen = 0
    ltotalsubprojectclosed = 0
    ltotalsubprojecttask = 0
    ltotalsubprojectopentask = 0
    ltotalsubprojectclosedtask = 0
    bclosed = 0
    bcompleted = 0
    bdiscarded = 0
    bstoppedtemporary = 0
    lplannedtotalhours = 0
    lactualtotalhours = 0
    dtcreatedon = datetime.today().strftime('%Y-%m-%d')
    dtclosedon = datetime.today().strftime('%Y-%m-%d')
    dtplannedstarton = datetime.today().strftime('%Y-%m-%d')
    dtplannedendon = datetime.today().strftime('%Y-%m-%d')
    sprojectno = ""
    sprojectname = ""
    scustomername = ""
    screatedon = datetime.today().strftime('%d-%m-%Y')
    scompletedon = ""
    splannedstarton = datetime.today().strftime('%d-%m-%Y')
    splannedendon = ""
    sprojectowner = ""
    bcustomervisible = 0
    lcustomerpriority = ""
    lcategoryid=0
    scategory=""

    lprojectid = 0
    lprojectsubno = 0
    lprojectsubtasknocount = 0
    lcategoryid = 0
    lcustomerid = 0
    lprojectownerid = 0
    lprojectownerid1 = 0
    lprojectownerid2 = 0
    lprojectownerid3 = 0
    fplannedcost = 0
    factualcost = 0
    brequirementreceived = 0
    bproposalgiven = 0
    bclosed = 0
    bcompleted = 0
    bdiscarded = 0
    bstoppedtemporary = 0
    bporecd = 0
    badvancerecd = 0
    bpaymentrecd = 0
    bdesigncompleted = 0
    bdevcompleted = 0
    bqualitycompleted = 0
    bimplementcompleted = 0
    busertestcompleted = 0
    blive = 0
    bbillable = 0
    lplannedtotaltime = 0
    lactualtotaltime = 0
    ltotalsubprojecttask = 0
    ltotalsubprojectopentask = 0
    ltotalsubprojectclosedtask = 0
    dtprojectstartdate = datetime.today().strftime('%Y-%m-%d')
    dtprojectenddate= datetime.today().strftime('%Y-%m-%d')
    dtreqrecddate = datetime.today().strftime('%Y-%m-%d')
    dtproposaldate = datetime.today().strftime('%Y-%m-%d')
    dtporecddate = datetime.today().strftime('%Y-%m-%d')
    badvancerecdon = datetime.today().strftime('%Y-%m-%d')
    dtpaymentrecdon = datetime.today().strftime('%Y-%m-%d')
    dtdesigncompletedon = datetime.today().strftime('%Y-%m-%d')
    dtdevcompletedon = datetime.today().strftime('%Y-%m-%d')
    dtqualitycompletedon =datetime.today().strftime('%Y-%m-%d')
    dtimplementcompletedon =datetime.today().strftime('%Y-%m-%d')
    dtusertestcompletedon =datetime.today().strftime('%Y-%m-%d')
    bliveon =datetime.today().strftime('%Y-%m-%d')
    sprojectsubno = 0
    ssubprojectname = 0
    sprojectname = 0
    scategoryname = 0
    scustomername = 0
    sprojectowner = 0
    sprojectowner1 = 0
    sprojectowner2 = 0
    sprojectowner3 = 0

    ssubprojecttemplate1 = ""
    ssubprojecttemplate2 = ""
    ssubprojecttemplate3 = ""
    ssubprojecttemplate4 = ""
    ssubprojecttemplate5 = ""
    ssubprojecttemplate6 = ""
    ssubprojecttemplate7 = ""
    ssubprojecttemplate8 = ""
    ssubprojecttemplate9 = ""
    ssubprojecttemplate10 = ""
    ssubprojecttemplate11 = ""
    ssubprojecttemplate12 = ""
    ssubprojecttemplate13 = ""
    ssubprojecttemplate14 = ""
    ssubprojecttemplate15 = ""
    ssubprojecttemplate16 = ""
    ssubprojecttemplate17 = ""
    ssubprojecttemplate18 = ""
    ssubprojecttemplate19 = ""
    ssubprojecttemplate20 = ""
 
    ltaskno = 0
    lsubprojectid = 0
    lfollowupeduptaskid = 0
    lasignedid = 0 
    dtplannedstarttime = datetime.today().strftime('%Y-%m-%d')
    dtplannedendtime = datetime.today().strftime('%Y-%m-%d')
    dtactualstarttime = datetime.today().strftime('%Y-%m-%d')
    dtactualendtime = datetime.today().strftime('%Y-%m-%d')
    dtteststarttime = datetime.today().strftime('%Y-%m-%d')
    dttestendtime = datetime.today().strftime('%Y-%m-%d')
    dtcustomertestendtime = datetime.today().strftime('%Y-%m-%d')
    bclosed = 0
    bcompleted = 0
    bdiscarded = 0
    bstoppedtemporary = 0
    btested = 0
    btestok = 0
    bcustomertested = 0
    bcustomertestok = 0
    bfollowuptask = 0
    bbillable = 0
    bdirectmanreqd = 0
    bteamreqd = 0
    bmaterialreqd = 0
    bmachinereqd = 0
    bindirectmanreqd = 0
    btravelreqd = 0
    botherindirectcostreqd = 0
    bapprovalreqd = 0
    bapproved1 = 0
    bapproved2 = 0
    lapprovalid2 = 0
    bapproved3 = 0
    bapproved4 = 0
    bapproved5 = 0
    brecalled = 0
    btask = 0
    bactionitem = 0
    bmeetingpoint = 0
    bfollowup = 0
    breminder = 0
    lpriority = 0
    lsequence = 0
    lsequencefollowup = 0
    lplannedperiod = 0
    lactualperiod = 0
    lplannedtotaltime = 0
    lactualtotaltime = 0
    lapprovallevel = 0
    lapprovalid1 = 0
    lapprovalid3 = 0
    lapprovalid4 = 0
    lapprovalid5 = 0
    lteammemberid1 = 0
    lteammemberid2 = 0
    lteammemberid3 = 0
    lteammemberid4 = 0
    lteammemberid5 = 0
    fplannedcost = 0
    factualcost = 0
    fcostperhourplanned = 0
    staskno =  ""
    staskname =  ""
    scomment =  ""
    scommentcustomer =  ""
    scommenttestteam =  ""
    scommentpm =  ""
    sasignedto =  ""
    sapprovalname1 =  ""
    sapprovalname2 =  ""
    sapprovalname3 =  ""
    sapprovalname4 =  ""
    sapprovalname5 =  ""
    steammembername1 =  ""
    steammembername2 =  ""
    steammembername3 =  ""
    steammembername4 =  ""
    steammembername5 =  ""
    srecallreason =  ""
    sdiscarded =  ""
    sprojectowner =  ""
    sprojectowner1 =  ""
    sprojectowner2 =  ""
    sprojectowner3 =  ""
    lcustomerpriority = 0
    bcustomervisible = 0



    if request.method == "POST":
        data = request.POST
        
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 

        if(txtName==""): 
            messages.error(request, 'Designation is not entered. Please enter and then try to save')
            Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
            return render(request, "iWorkPro/PCreateProject.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                    'Acustomerlst_list':Acustomerlst_list,
                    'Aprojectcategorylist_list':Aprojectcategorylist_list,  
                    'AemployeelistRepManager_list':AemployeelistRepManager_list, 
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                    'Menu2':'Create Project', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Create Project', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )
        


        if 'CustomerListDD' in request.POST:
            lcustomerid=int(request.POST['CustomerListDD']) #('Machine')
            if(lcustomerid==0):
              
                messages.error(request, 'Customer is not selected. Please Select and then try!')

                Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
                return render(request, "iWorkPro/PCreateProject.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            'Acustomerlst_list':Acustomerlst_list,
                            'Aprojectcategorylist_list':Aprojectcategorylist_list,  
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,  
                            
                            'Menu2':'Create Project', 
                            'Menu3':'', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Create Project', 
                                'MenuName3':'', 
                                'MenuName4':'', 
                                'MenuName5':'',   
                }
                            )

            else:
                AcustomerlstGet = Acustomerlst.objects.get(lid=lcustomerid)
                scustomername = AcustomerlstGet.scustomername

                if(AcustomerlstGet.bprioritya==1):                    
                    lcustomerpriority="A"
                elif(AcustomerlstGet.bpriorityb==1):                    
                    lcustomerpriority="B"
                elif(AcustomerlstGet.bpriorityc==1):                    
                    lcustomerpriority="C"
                elif(AcustomerlstGet.bpriorityd==1):                    
                    lcustomerpriority="D"


                lprojectno = AcustomerlstGet.lprojecctnocount
                lprojectno = lprojectno + 1

                sprojectno = AcustomerlstGet.scustomerabv + "-00" + str(lprojectno)
                AcustomerlstGet.lprojecctnocount =lprojectno
                AcustomerlstGet.save()


        if 'OwnerListDD' in request.POST:
            lprojectownerid=int(request.POST['OwnerListDD']) #('Machine')
            if(lprojectownerid==0):
              
                messages.error(request, 'Owner of Project is not selected. Please Select and then try!')

                Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
                return render(request, "iWorkPro/PCreateProject.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            'Acustomerlst_list':Acustomerlst_list,
                            'Aprojectcategorylist_list':Aprojectcategorylist_list,  
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,  
                            
                            'Menu2':'Create Project', 
                            'Menu3':'', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Create Project', 
                                'MenuName3':'', 
                                'MenuName4':'', 
                                'MenuName5':'',   
                }
                            )

            else:
                AemployeelistGet = Aemployeelist.objects.get(lid=lprojectownerid)
                sprojectowner = AemployeelistGet.susername 
 
        if 'ProjectCategoryListDD' in request.POST:
            lcategoryid=int(request.POST['ProjectCategoryListDD']) #('Machine')
            if(lcategoryid==0):
              
                messages.error(request, 'Project Category is not selected. Please Select and then try!')

                Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
                return render(request, "iWorkPro/PCreateProject.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            'Acustomerlst_list':Acustomerlst_list,
                            'Aprojectcategorylist_list':Aprojectcategorylist_list,  
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,  
                            
                            'Menu2':'Create Project', 
                            'Menu3':'', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Create Project', 
                                'MenuName3':'', 
                                'MenuName4':'', 
                                'MenuName5':'',   
                }
                            )

            else:
                AprojectcategorylistGet = Aprojectcategorylist.objects.get(lid=lcategoryid)
                scategory = AprojectcategorylistGet.scategoryname 
                scategoryname = AprojectcategorylistGet.scategoryname 

                lprojectsubnocount = AprojectcategorylistGet.ltotalsubcount

                bcustomervisible = AprojectcategorylistGet.bcustomervisible
                ssubprojecttemplate1 = AprojectcategorylistGet.ssubprojecttemplate1 
                ssubprojecttemplate2 = AprojectcategorylistGet.ssubprojecttemplate2
                ssubprojecttemplate3 = AprojectcategorylistGet.ssubprojecttemplate3
                ssubprojecttemplate4 = AprojectcategorylistGet.ssubprojecttemplate4
                ssubprojecttemplate5 = AprojectcategorylistGet.ssubprojecttemplate5
                ssubprojecttemplate6 = AprojectcategorylistGet.ssubprojecttemplate6
                ssubprojecttemplate7 = AprojectcategorylistGet.ssubprojecttemplate7
                ssubprojecttemplate8 = AprojectcategorylistGet.ssubprojecttemplate8
                ssubprojecttemplate9 = AprojectcategorylistGet.ssubprojecttemplate9
                ssubprojecttemplate10 = AprojectcategorylistGet.ssubprojecttemplate10
                ssubprojecttemplate11 = AprojectcategorylistGet.ssubprojecttemplate11
                ssubprojecttemplate12 = AprojectcategorylistGet.ssubprojecttemplate12
                ssubprojecttemplate13 = AprojectcategorylistGet.ssubprojecttemplate13
                ssubprojecttemplate14 = AprojectcategorylistGet.ssubprojecttemplate14
                ssubprojecttemplate15 = AprojectcategorylistGet.ssubprojecttemplate15
                ssubprojecttemplate16 = AprojectcategorylistGet.ssubprojecttemplate16
                ssubprojecttemplate17 = AprojectcategorylistGet.ssubprojecttemplate17
                ssubprojecttemplate18 = AprojectcategorylistGet.ssubprojecttemplate18
                ssubprojecttemplate19 = AprojectcategorylistGet.ssubprojecttemplate19
                ssubprojecttemplate20 = AprojectcategorylistGet.ssubprojecttemplate20

 


        sprojectname = txtName 
 
        # sdesignation=""
        # sdesignation=txtName
        ProjectmainlistSave = Projectmainlist(lprojectno = lprojectno, 	lprojectsubnocount = lprojectsubnocount, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	ltotalsubproject = ltotalsubproject, 	ltotalsubprojectopen = ltotalsubprojectopen, 	ltotalsubprojectclosed = ltotalsubprojectclosed, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	lplannedtotalhours = lplannedtotalhours, 	lactualtotalhours = lactualtotalhours, 	dtcreatedon = dtcreatedon, 	dtclosedon = dtclosedon, 	dtplannedstarton = dtplannedstarton, 	dtplannedendon = dtplannedendon, 	sprojectno = sprojectno, 	sprojectname = sprojectname, 	scustomername = scustomername, 	screatedon = screatedon, 	scompletedon = scompletedon, 	splannedstarton = splannedstarton, 	splannedendon = splannedendon, 	sprojectowner = sprojectowner, 	bcustomervisible = bcustomervisible, 	lcustomerpriority = lcustomerpriority, 	lcategoryid = lcategoryid, 	scategory = scategory,btaststarted=0)
        ProjectmainlistSave.save()
        lprojectid=ProjectmainlistSave.lid


        lCategorySubID =0
        lProjectSubID =0
        AprojectcategorysublistGet = Aprojectcategorysublist.objects.filter(lprojectcategoryid=lcategoryid).order_by('lid').values()
        if(AprojectcategorysublistGet):
            for AprojectcategorysublistGetOBJ in AprojectcategorysublistGet: 

                lCategorySubID =AprojectcategorysublistGetOBJ['lid']
                lprojectsubno=lprojectsubno + 1
                sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
                ssubprojectname=AprojectcategorysublistGetOBJ['ssubname']
                ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="",btaststarted=0)
                ProjectsublistSave.save()
                lsubprojectid = ProjectsublistSave.lid
                ltaskno =0

                AprojectcategorysubtasklistGet = Aprojectcategorysubtasklist.objects.filter(lprojectcategorysubid=lCategorySubID).order_by('lid').values()
                if(AprojectcategorysubtasklistGet):
                    for AprojectcategorysubtasklistGetOBJ in AprojectcategorysubtasklistGet: 

                        ltaskno=ltaskno + 1
                        staskno =sprojectsubno + "/0" + str(ltaskno)
                        staskname=AprojectcategorysubtasklistGetOBJ['ssubname']

                        ProjecttasklistSave = Projecttasklist(lprojectid = lprojectid, 	ltaskno = ltaskno, 	lsubprojectid = lsubprojectid, 	lfollowupeduptaskid = lfollowupeduptaskid, 	lasignedid = lasignedid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	dtplannedstarttime = dtplannedstarttime, 	dtplannedendtime = dtplannedendtime, 	dtactualstarttime = dtactualstarttime, 	dtactualendtime = dtactualendtime, 	dtteststarttime = dtteststarttime, 	dttestendtime = dttestendtime, 	dtcustomertestendtime = dtcustomertestendtime, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	btested = btested, 	btestok = btestok, 	bcustomertested = bcustomertested, 	bcustomertestok = bcustomertestok, 	bfollowuptask = bfollowuptask, 	bbillable = bbillable, 	bdirectmanreqd = bdirectmanreqd, 	bteamreqd = bteamreqd, 	bmaterialreqd = bmaterialreqd, 	bmachinereqd = bmachinereqd, 	bindirectmanreqd = bindirectmanreqd, 	btravelreqd = btravelreqd, 	botherindirectcostreqd = botherindirectcostreqd, 	bapprovalreqd = bapprovalreqd, 	bapproved1 = bapproved1, 	bapproved2 = bapproved2, 	lapprovalid2 = lapprovalid2, 	bapproved3 = bapproved3, 	bapproved4 = bapproved4, 	bapproved5 = bapproved5, 	brecalled = brecalled, 	btask = btask, 	bactionitem = bactionitem, 	bmeetingpoint = bmeetingpoint, 	bfollowup = bfollowup, 	breminder = breminder, 	lpriority = lpriority, 	lsequence = lsequence, 	lsequencefollowup = lsequencefollowup, 	lplannedperiod = lplannedperiod, 	lactualperiod = lactualperiod, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	lapprovallevel = lapprovallevel, 	lapprovalid1 = lapprovalid1, 	lapprovalid3 = lapprovalid3, 	lapprovalid4 = lapprovalid4, 	lapprovalid5 = lapprovalid5, 	lteammemberid1 = lteammemberid1, 	lteammemberid2 = lteammemberid2, 	lteammemberid3 = lteammemberid3, 	lteammemberid4 = lteammemberid4, 	lteammemberid5 = lteammemberid5, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	fcostperhourplanned = fcostperhourplanned, 	staskno = staskno, 	staskname = staskname, 	scomment = scomment, 	scommentcustomer = scommentcustomer, 	scommenttestteam = scommenttestteam, 	scommentpm = scommentpm, 	sasignedto = sasignedto, 	sapprovalname1 = sapprovalname1, 	sapprovalname2 = sapprovalname2, 	sapprovalname3 = sapprovalname3, 	sapprovalname4 = sapprovalname4, 	sapprovalname5 = sapprovalname5, 	steammembername1 = steammembername1, 	steammembername2 = steammembername2, 	steammembername3 = steammembername3, 	steammembername4 = steammembername4, 	steammembername5 = steammembername5, 	srecallreason = srecallreason, 	sdiscarded = sdiscarded, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, 	lcustomerpriority = lcustomerpriority, 	bcustomervisible = bcustomervisible,btaststarted=0)
                        ProjecttasklistSave.save()


                ProjectsublistEditSave = Projectsublist.objects.get(lid=lsubprojectid)
                ProjectsublistEditSave.lprojectsubtasknocount = ltaskno
                ProjectsublistEditSave.save()

        


        # if( ssubprojecttemplate1 != ""):
        #     ProjectsublistSave = Projectsublist()

        # if( ssubprojecttemplate2 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate2
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()

        # if( ssubprojecttemplate3 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate3
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            
        # if( ssubprojecttemplate4 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate4
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            
        # if( ssubprojecttemplate5 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate5
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate6 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate6
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate7 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate7
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate8 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate8
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate9 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate9
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate10 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate10
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate11 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate11
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate12 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate12
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate13 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate13
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate14 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate14
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate15 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate15
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate16 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate16
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate17 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate17
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate18 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate18
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate19 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate19
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            

        # if( ssubprojecttemplate20 != ""):
        #     ProjectsublistSave = Projectsublist()
        #     lprojectsubno=lprojectsubno + 1
        #     sprojectsubno =sprojectno + " 0" + str(lprojectsubno)
        #     ssubprojectname=ssubprojecttemplate20
            
        #     ProjectsublistSave = Projectsublist(lprojectid = lprojectid, 	lprojectsubno = lprojectsubno, 	lprojectsubtasknocount = lprojectsubtasknocount, 	lcategoryid = lcategoryid, 	lcustomerid = lcustomerid, 	lprojectownerid = lprojectownerid, 	lprojectownerid1 = lprojectownerid1, 	lprojectownerid2 = lprojectownerid2, 	lprojectownerid3 = lprojectownerid3, 	fplannedcost = fplannedcost, 	factualcost = factualcost, 	brequirementreceived = brequirementreceived, 	bproposalgiven = bproposalgiven, 	bclosed = bclosed, 	bcompleted = bcompleted, 	bdiscarded = bdiscarded, 	bstoppedtemporary = bstoppedtemporary, 	bporecd = bporecd, 	badvancerecd = badvancerecd, 	bpaymentrecd = bpaymentrecd, 	bdesigncompleted = bdesigncompleted, 	bdevcompleted = bdevcompleted, 	bqualitycompleted = bqualitycompleted, 	bimplementcompleted = bimplementcompleted, 	busertestcompleted = busertestcompleted, 	blive = blive, 	bbillable = bbillable, 	lplannedtotaltime = lplannedtotaltime, 	lactualtotaltime = lactualtotaltime, 	ltotalsubprojecttask = ltotalsubprojecttask, 	ltotalsubprojectopentask = ltotalsubprojectopentask, 	ltotalsubprojectclosedtask = ltotalsubprojectclosedtask, 	dtprojectstartdate = dtprojectstartdate, 	dtprojectenddate = dtprojectenddate, 	dtreqrecddate = dtreqrecddate, 	dtproposaldate = dtproposaldate, 	dtporecddate = dtporecddate, 	badvancerecdon = badvancerecdon, 	dtpaymentrecdon = dtpaymentrecdon, 	dtdesigncompletedon = dtdesigncompletedon, 	dtdevcompletedon = dtdevcompletedon, 	dtqualitycompletedon = dtqualitycompletedon, 	dtimplementcompletedon = dtimplementcompletedon, 	dtusertestcompletedon = dtusertestcompletedon, 	bliveon = bliveon, 	sprojectsubno = sprojectsubno, 	ssubprojectname = ssubprojectname, 	sprojectname = sprojectname, 	scategoryname = scategoryname, 	scustomername = scustomername, 	sprojectowner = sprojectowner, 	sprojectowner1 = sprojectowner1, 	sprojectowner2 = sprojectowner2, 	sprojectowner3 = sprojectowner3, lcustomerpriority="")
        #     ProjectsublistSave.save()
            


        return redirect("EditProject", lID=lprojectid)  


    else:  
        
        Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
        Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
        return render(request, "iWorkPro/PCreateProject.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Acustomerlst_list':Acustomerlst_list,
                    'Aprojectcategorylist_list':Aprojectcategorylist_list,  
                    'AemployeelistRepManager_list':AemployeelistRepManager_list,  
                     
                    'Menu2':'Create Project', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Create Project', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )


@csrf_exempt
def EditProject(request, lID):

    if(request.session['username']  == ""): 
        return redirect("Logout")  

    if request.method == "POST":
        data = request.POST

    else:
          
        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
        Projectmainlist_list = Projectmainlist.objects.get(lid=lID) 

        Projectsublist_list = Projectsublist.objects.filter(lprojectid=lID).order_by('lid') 


        return render(request, "iWorkPro/PEditProject.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Projectmainlist_list':Projectmainlist_list,
                    'Projectsublist_list':Projectsublist_list,  
                    'AemployeelistRepManager_list':AemployeelistRepManager_list,  
                     
                    'Menu2':'View / Edit Project Details', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'View / Edit Project Details', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )

@csrf_exempt
def ProjectSubList(request, lID):

    if(request.session['username']  == ""): 
        return redirect("Logout")  

    if request.method == "POST":
        data = request.POST

    else:
           
        Projectmainlist_list = Projectmainlist.objects.get(lid=lID) 

        Projectsublist_list = Projectsublist.objects.filter(lprojectid=lID).order_by('lid') 


        return render(request, "iWorkPro/PViewProject.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Projectmainlist_list':Projectmainlist_list,
                    'Projectsublist_list':Projectsublist_list,   
                     
                    'Menu2':'View / Edit Project Details', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'View / Edit Project Details', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )
    





@csrf_exempt
def EditSubProject(request, lID):

    if(request.session['username']  == ""): 
        return redirect("Logout")  

    if request.method == "POST":
        data = request.POST

    else:
          
        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
        Projectsublist_list = Projectsublist.objects.get(lid=lID) 
        Projectmainlist_list = Projectmainlist.objects.get(lid=Projectsublist_list.lprojectid) 



        Projecttasklist_list = Projecttasklist.objects.filter(lsubprojectid=lID).order_by('lid') 

        return render(request, "iWorkPro/EditSubProject.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Projectmainlist_list':Projectmainlist_list,
                    'Projectsublist_list':Projectsublist_list,  
                    'Projecttasklist_list':Projecttasklist_list,  
                     
                    'Menu2':'View / Edit Project Details', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'View / Edit Project Details', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )

@csrf_exempt
def SubpojectSubList(request, lID):

    if(request.session['username']  == ""): 
        return redirect("Logout")  

    if request.method == "POST":
        data = request.POST

    else:
           
        Projectsublist_list = Projectsublist.objects.get(lid=lID) 
        Projectmainlist_list = Projectmainlist.objects.get(lid=Projectsublist_list.lprojectid) 



        Projecttasklist_list = Projecttasklist.objects.filter(lsubprojectid=lID).order_by('lid') 


        return render(request, "iWorkPro/SubpojectSubList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Projectmainlist_list':Projectmainlist_list,
                    'Projectsublist_list':Projectsublist_list,   
                    'Projecttasklist_list':Projecttasklist_list,  
                     
                    'Menu2':'View / Edit Project Details', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'View / Edit Project Details', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )
    





    
@csrf_exempt
def DashboardCustomer(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    lLoginID =0
    lLoginID = int(request.session['lLoginID'])
    lcustomerid= int(request.session['lcustomerid'])
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Projectmainlist_list = Projectmainlist.objects.filter(sprojectname__contains = txtSearch, lcustomerid=lcustomerid).order_by('lid').values() 
            
         
            return render(request, "iWorkPro/dashboardCustomer.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Projectmainlist_list = Projectmainlist.objects.filter(lcustomerid=lcustomerid).order_by('lid') 
         
            return render(request, "iWorkPro/dashboardCustomer.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
            }
                        )
    else:  


        Projectmainlist_list = Projectmainlist.objects.filter(lcustomerid=lcustomerid).order_by('lid') 
         
        return render(request, "iWorkPro/dashboardCustomer.html", 
        {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Projectmainlist_list':Projectmainlist_list
        }
                    )
    
 
@csrf_exempt
def ProjectSubCustomerList(request, lID):

    if(request.session['username']  == ""): 
        return redirect("Logout")  

    if request.method == "POST":
        data = request.POST

    else:
           
        Projectmainlist_list = Projectmainlist.objects.get(lid=lID) 

        Projectsublist_list = Projectsublist.objects.filter(lprojectid=lID).order_by('lid') 


        return render(request, "iWorkPro/PViewProjectCustomer.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                    'Projectmainlist_list':Projectmainlist_list,
                    'Projectsublist_list':Projectsublist_list,   
                     
                    'Menu2':'View / Edit Project Details', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'View / Edit Project Details', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )


      
@csrf_exempt
def EmployeeList(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Aemployeelist_list = Aemployeelist.objects.filter(Employee__contains = txtSearch).order_by('lid').values() 
            return render(request, "iWorkPro/Employeelist.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'sSearch':txtSearch,
                        'Aemployeelist_list':Aemployeelist_list, 
                        'MenuName1':'Home', 
                        'MenuName2':'Employee', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Aemployeelist_list = Aemployeelist.objects .order_by('lid') 
            return render(request, "iWorkPro/Employeelist.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Employee', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Aemployeelist_list':Aemployeelist_list
            }
                        )
    else:  


        Aemployeelist_list = Aemployeelist.objects.order_by('lid') 
        return render(request, "iWorkPro/Employeelist.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'EmployeeList', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Employee', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                    'sSearch':'',
                    'Aemployeelist_list':Aemployeelist_list
        }
                    )
    

    
@csrf_exempt
def EmployeeListAdd(request):

    lDepartmentID =0
    ReportingManagerID =0
    lDesignationID =0
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtName=""

    if request.method == "POST":
        data = request.POST
        
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 

        if(txtName==""): 
            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
            Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            messages.error(request, 'Employee is not entered. Please enter and then try to save')
            return render(request, "iWorkPro/EmployeelistAdd.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'Adesignationlist_list':Adesignationlist_list,
                        'AemployeelistRepManager_list':AemployeelistRepManager_list,
                        'ReportingManagerID':ReportingManagerID,
                        'lDepartmentID':lDepartmentID,
                        'lDesignationID':lDesignationID,
                            
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'New Employee', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Employee', 
                            'MenuName3':'Create New', 
                            'MenuName4':'', 
                            'MenuName5':'',   
            }
                        )
        else:
            Employee=""
            Employee=txtName
            AemployeelistSave = Aemployeelist(Employee=Employee)
            AemployeelistSave.save()
            return redirect("EmployeeList")  


    else:  


        susername = ""
        sempid = ""
        spassword = ""
        sempemailid = ""
        smobile = ""
        sdeptname = ""
        sreportmanager = ""
        sdesignation = ""
        dtdateofjleft = ""
        sdateofjoin =  datetime.today().strftime('%d-%m-%Y')
        spfno = ""
        sesino = ""
        sadharno = ""
        spanno = ""
        sbloodgroup = ""
        saddress = ""
        sspousename = ""
        sscontact = ""
        sfathername = ""
        sfathercontact = ""
        smothername = ""
        schildrenname1 = ""
        schildrenname2 = ""
        schildrenname3 = ""
        schildrenname4 = ""
        schildrenname5 = ""
        sdateofbirth = ""
        sphotofile = ""
        sinsurancedetails = ""
        sbankname = ""
        sifsccode = ""
        bankaccountno = ""
        dtdateofjoin = datetime.today().strftime('%Y-%m-%d')
        ldeptid = 0
        lreportmanagerid = 0
        ldesignationid = 0
        lage = 0
        badmin = 0
        bpm = 0
        bprojectmanager = 0
        bdeveloper = 0
        btester = 0
        bothers = 0
        bactive = 0
        bactive = 1
        bmanagement = 0
        bit = 0
        binsurance = 0
        bta = 0
        bmedicalallow = 0
        bda = 0
        bpf = 0
        besi = 0
        fcosttocompanyperhour = 0
        fcosttocompany1 = 0
        fcosttocompany2 = 0
        fcosttocompany3 = 0
        fcosttocompany4 = 0
        fcosttocompany5 = 0
        fcosttocompany6 = 0
        fcosttocompany7 = 0
        fcosttocompany8 = 0
        fcosttocompany9 = 0
        fcosttocompany10 = 0
        fcosttocompany11 = 0
        fcosttocompany12 = 0
        fcosttocompany13 = 0
        fcosttocompany14 = 0
        fcosttocompany15 = 0
        fcosttocompany16 = 0
        fcosttocompany17 = 0
        fcosttocompany18 = 0
        fcosttocompany19 = 0
        fcosttocompany20 = 0


        AemployeelistNewSave = Aemployeelist(susername =  susername, 	sempid =  sempid, 	spassword =  spassword, 	sempemailid =  sempemailid, 	smobile =  smobile, 	sdeptname =  sdeptname, 	sreportmanager =  sreportmanager, 	sdesignation =  sdesignation, 	dtdateofjleft =  dtdateofjleft, 	sdateofjoin =  sdateofjoin, 	spfno =  spfno, 	sesino =  sesino, 	sadharno =  sadharno, 	spanno =  spanno, 	sbloodgroup =  sbloodgroup, 	saddress =  saddress, 	sspousename =  sspousename, 	sscontact =  sscontact, 	sfathername =  sfathername, 	sfathercontact =  sfathercontact, 	smothername =  smothername, 	schildrenname1 =  schildrenname1, 	schildrenname2 =  schildrenname2, 	schildrenname3 =  schildrenname3, 	schildrenname4 =  schildrenname4, 	schildrenname5 =  schildrenname5, 	sdateofbirth =  sdateofbirth, 	sphotofile =  sphotofile, 	sinsurancedetails =  sinsurancedetails, 	sbankname =  sbankname, 	sifsccode =  sifsccode, 	bankaccountno =  bankaccountno, 	dtdateofjoin =  dtdateofjoin, 	ldeptid =  ldeptid, 	lreportmanagerid =  lreportmanagerid, 	ldesignationid =  ldesignationid, 	lage =  lage, 	badmin =  badmin, 	bpm =  bpm, 	bprojectmanager =  bprojectmanager, 	bdeveloper =  bdeveloper, 	btester =  btester, 	bothers =  bothers, 	bactive =  bactive, 	bmanagement =  bmanagement, 	bit =  bit, 	binsurance =  binsurance, 	bta =  bta, 	bmedicalallow =  bmedicalallow, 	bda =  bda, 	bpf =  bpf, 	besi =  besi, 	fcosttocompanyperhour =  fcosttocompanyperhour, 	fcosttocompany1 =  fcosttocompany1, 	fcosttocompany2 =  fcosttocompany2, 	fcosttocompany3 =  fcosttocompany3, 	fcosttocompany4 =  fcosttocompany4, 	fcosttocompany5 =  fcosttocompany5, 	fcosttocompany6 =  fcosttocompany6, 	fcosttocompany7 =  fcosttocompany7, 	fcosttocompany8 =  fcosttocompany8, 	fcosttocompany9 =  fcosttocompany9, 	fcosttocompany10 =  fcosttocompany10, 	fcosttocompany11 =  fcosttocompany11, 	fcosttocompany12 =  fcosttocompany12, 	fcosttocompany13 =  fcosttocompany13, 	fcosttocompany14 =  fcosttocompany14, 	fcosttocompany15 =  fcosttocompany15, 	fcosttocompany16 =  fcosttocompany16, 	fcosttocompany17 =  fcosttocompany17, 	fcosttocompany18 =  fcosttocompany18, 	fcosttocompany19 =  fcosttocompany19, 	fcosttocompany20 =  fcosttocompany20)
        AemployeelistNewSave.save()
        

        # Aemployeelist_list = Aemployeelist.objects.order_by('-lid').values()
        

        lNewID =0
        lNewID =AemployeelistNewSave.lid

        lNewUserID = 10000 + lNewID
        AemployeelistEditSave = Aemployeelist.objects.get(lid=lNewID)
        
        AemployeelistEditSave.sempid = str(lNewUserID)
        AemployeelistEditSave.save()
        # if Aemployeelist_list:
        #     for Aemployeelist_listOBJ in Aemployeelist_list:
        #         if(lNewID==0):
        #             lNewID = Aemployeelist_listOBJ['lid']
        #             lNewUserID = 10000 + lNewID
        #             AemployeelistEditSave = Aemployeelist.objects.get(lid=lNewID)
                    
        #             AemployeelistEditSave.sempid = str(lNewUserID)
        #             AemployeelistEditSave.save()


        return redirect("EmployeeListEdit", lID=lNewID)   
        
         
    
@csrf_exempt
def EmployeeListEdit(request,lID):

    lDepartmentID =0
    ReportingManagerID =0
    lDesignationID =0
    ReportingManagerID=0
    txtName=""
    EmployeeName=""
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


        sempid=""
        susername = "" 
        spassword = ""
        sempemailid = ""
        smobile = ""
        sdeptname = ""
        sreportmanager = ""
        sdesignation = ""
        dtdateofjleft = "" 
        spfno = ""
        sesino = ""
        sadharno = ""
        spanno = ""
        sbloodgroup = ""
        saddress = ""
        sspousename = ""
        sscontact = ""
        sfathername = ""
        sfathercontact = ""
        smothername = ""
        schildrenname1 = ""
        schildrenname2 = ""
        schildrenname3 = ""
        schildrenname4 = ""
        schildrenname5 = ""
        sdateofbirth = ""
        sphotofile = ""
        sinsurancedetails = ""
        sbankname = ""
        sifsccode = ""
        bankaccountno = "" 
        ldeptid = 0
        lreportmanagerid = 0
        ldesignationid = 0
        lage = 0
        badmin = 0
        bpm = 0
        bprojectmanager = 0
        bdeveloper = 0
        btester = 0
        bothers = 0
        bactive = 0
        bactive = 1
        bmanagement = 0
        bit = 0
        binsurance = 0
        bta = 0
        bmedicalallow = 0
        bda = 0
        bpf = 0
        besi = 0
        fcosttocompanyperhour = 0
        fcosttocompany1 = 0
        fcosttocompany2 = 0
        fcosttocompany3 = 0
        fcosttocompany4 = 0
        fcosttocompany5 = 0
        fcosttocompany6 = 0
        fcosttocompany7 = 0
        fcosttocompany8 = 0
        fcosttocompany9 = 0
        fcosttocompany10 = 0
        fcosttocompany11 = 0
        fcosttocompany12 = 0
        fcosttocompany13 = 0
        fcosttocompany14 = 0
        fcosttocompany15 = 0
        fcosttocompany16 = 0
        fcosttocompany17 = 0
        fcosttocompany18 = 0
        fcosttocompany19 = 0
        fcosttocompany20 = 0

        txtPassword = ""
        if 'txtPassword' in request.POST: 
            txtPassword=data.get("txtPassword") 

        if 'txtEmpNo' in request.POST: 
            sempid=data.get("txtEmpNo") 

        if(txtPassword == ""):
            chars = ""
            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ123456789"
            chars1 = ""
            chars1 = "9@#*123456789@#*abcdefghijklmnopqrstuvwxyz9@#*" 
            chars2 = ""
            chars2 = "9@#*abcdefghijklmnopqrstuvwxyz@#*123456789" 
            length=0
            length=4

            sPassword1 = ""
            sPassword1 = "".join(chars[c % len(chars)] for c in urandom(length))

            length=4

            sPassword2 = ""
            sPassword2 = "".join(chars1[c % len(chars1)] for c in urandom(length))
            length=4

            sPassword3 = ""
            sPassword3 = "".join(chars2[c % len(chars2)] for c in urandom(length))

            spassword = ""
            spassword = sPassword3 + sPassword1 + sPassword2

            if 'txtEMailAddress' in request.POST: 
                sempemailid=data.get("txtEMailAddress") 


            lUserId =0
            sEmail = ""  
            sEmail = sempemailid
            connection = mail.get_connection()
            email1 = mail.EmailMessage(
                    "iWorkPro - New Employee Created",
                "Hi, \n Information from www.Dhruthi.org:8004 - iWorkPro \n For your ID : " + sempid + " \n Your new Password : " + spassword + "\n\n\n This is notification Mail. Please Don't Reply",
                "iworkproalerts@dhruthi.org",
                [sEmail],
                bcc = ['sanjay@dhruthi.org', 'sanjaybk@dhruthitech.onmicrosoft.com'],
                connection=connection,
            )
            email1.send()



        if 'txtEmpNo' in request.POST: 
            sempid=data.get("txtEmpNo") 
        if 'txtName' in request.POST: 
            susername=data.get("txtName") 


        bactive = 0
        if 'bactive' in request.POST:
            bactive =1 
 

        badmin = 0
        if 'chkAdmin' in request.POST:
            badmin =1 
 
        bpm = 0
        if 'chkApprover' in request.POST:
            bpm =1 
 
        if 'DepartmentManager' in request.POST:
            ldeptid=int(request.POST['DepartmentManager']) #('Machine')
            if(ldeptid==0):
              
                messages.error(request, 'Department is not selected. Please Select and then try!')

                Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
                Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
                return render(request, "iWorkPro/EmployeelistEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                            'Adepartmentlist_list':Adepartmentlist_list,
                            'Adesignationlist_list':Adesignationlist_list,
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,
                            'ReportingManagerID':ReportingManagerID,
                            'lDepartmentID':lDepartmentID,
                            'lDesignationID':lDesignationID,

                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'EmployeeList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Employee', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'EmployeeName':EmployeeName,
                }
                        )
            else:
                AdepartmentlistGet = Adepartmentlist.objects.get(lid=ldeptid)
                sdeptname = AdepartmentlistGet.sdeptname
        else:              
            messages.error(request, 'Department is not selected. Please Select and then try!')

            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
            Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
            Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
            return render(request, "iWorkPro/EmployeelistEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'Adesignationlist_list':Adesignationlist_list,
                        'AemployeelistRepManager_list':AemployeelistRepManager_list,
                        'ReportingManagerID':ReportingManagerID,
                        'lDepartmentID':lDepartmentID,
                        'lDesignationID':lDesignationID,

                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Employee', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'EmployeeName':EmployeeName,
            }
                    )
        

        if 'DesignationManager' in request.POST:
            ldesignationid=int(request.POST['DesignationManager']) #('Machine')
            if(ldesignationid==0):
                         
                messages.error(request, 'Designation is not selected. Please Select and then try!')

                Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aemployeelist_list = Aemployeelist.objects.get(lid=lID) 
                Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values() 
                return render(request, "iWorkPro/EmployeelistEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                            'Adepartmentlist_list':Adepartmentlist_list,
                            'Adesignationlist_list':Adesignationlist_list,
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,
                            'ReportingManagerID':ReportingManagerID,
                            'lDepartmentID':lDepartmentID,
                            'lDesignationID':lDesignationID,

                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'EmployeeList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Employee', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'EmployeeName':EmployeeName,
                }
                        )
            else:
                AdesignationlistGet = Adesignationlist.objects.get(lid=ldesignationid)
                sdesignation = AdesignationlistGet.sdesignation
        else:              
            messages.error(request, 'Designation is not selected. Please Select and then try!')

            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
            Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
            Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
            return render(request, "iWorkPro/EmployeelistEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'Adesignationlist_list':Adesignationlist_list,
                        'AemployeelistRepManager_list':AemployeelistRepManager_list,
                        'ReportingManagerID':ReportingManagerID,
                        'lDepartmentID':lDepartmentID,
                        'lDesignationID':lDesignationID,

                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Employee', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'EmployeeName':EmployeeName,
            }
                    )


        if 'ReportingManager' in request.POST:
            lreportmanagerid=int(request.POST['ReportingManager']) #('Machine')
            if(lreportmanagerid==0):
                                   
                messages.error(request, 'Reporting Manager is not selected. Please Select and then try!')

                Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
                Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
                return render(request, "iWorkPro/EmployeelistEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                            'Adepartmentlist_list':Adepartmentlist_list,
                            'Adesignationlist_list':Adesignationlist_list,
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,
                            'ReportingManagerID':ReportingManagerID,
                            'lDepartmentID':lDepartmentID,
                            'lDesignationID':lDesignationID,

                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'EmployeeList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Employee', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'EmployeeName':EmployeeName,
                }
                        )
            else:

                AemployeelistGet = Aemployeelist.objects.get(lid=lreportmanagerid)
                sreportmanager = AemployeelistGet.susername
        else:              
            messages.error(request, 'Reporting Manager is not selected. Please Select and then try!')

            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
            Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
            Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
            return render(request, "iWorkPro/EmployeelistEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'Adesignationlist_list':Adesignationlist_list,
                        'AemployeelistRepManager_list':AemployeelistRepManager_list,
                        'ReportingManagerID':ReportingManagerID,
                        'lDepartmentID':lDepartmentID,
                        'lDesignationID':lDesignationID,

                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Employee', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'EmployeeName':EmployeeName,
            }
                    )

        if 'txtAddress' in request.POST: 
            saddress=data.get("txtAddress") 
        if 'txtDateofBirth' in request.POST: 
            sdateofbirth=data.get("txtDateofBirth") 
        if 'txtContactNo' in request.POST: 
            smobile=data.get("txtContactNo") 
        if 'txtFatherSpouseName' in request.POST: 
            sspousename=data.get("txtFatherSpouseName") 
        if 'txtEmergencyContact' in request.POST: 
            sscontact=data.get("txtEmergencyContact") 
        if 'txtAAdharNo' in request.POST: 
            sadharno=data.get("txtAAdharNo") 
        if 'txtPANNo' in request.POST: 
            spanno=data.get("txtPANNo") 
        if 'txtBloodGroup' in request.POST: 
            sbloodgroup=data.get("txtBloodGroup") 
        if 'txtPFNo' in request.POST: 
            spfno=data.get("txtPFNo") 
        if 'txtInsuranceDetails' in request.POST: 
            sinsurancedetails=data.get("txtInsuranceDetails") 
        if 'txtSalary' in request.POST: 
            fcosttocompany1=data.get("txtSalary") 
        if 'txtBankName' in request.POST: 
            sbankname=data.get("txtBankName") 
        if 'txtIFSCDetails' in request.POST: 
            sifsccode=data.get("txtIFSCDetails") 
        if 'txtBankAccountNo' in request.POST: 
            bankaccountno=data.get("txtBankAccountNo") 
 
        if 'cmdSave' in request.POST:
            
            Employee=""
            Employee=txtName
            AemployeelistSave = Aemployeelist.objects.get(lid=lID) 
            AemployeelistSave.susername=susername 
            if(txtPassword == ""):
                AemployeelistSave.spassword=spassword
            AemployeelistSave.sempemailid=sempemailid
            AemployeelistSave.smobile=smobile
            AemployeelistSave.sdeptname=sdeptname
            AemployeelistSave.sreportmanager=sreportmanager
            AemployeelistSave.sdesignation=sdesignation
            AemployeelistSave.dtdateofjleft=dtdateofjleft 
            AemployeelistSave.spfno=spfno
            AemployeelistSave.sesino=sesino
            AemployeelistSave.sadharno=sadharno
            AemployeelistSave.spanno=spanno
            AemployeelistSave.sbloodgroup=sbloodgroup
            AemployeelistSave.saddress=saddress
            AemployeelistSave.sspousename=sspousename
            AemployeelistSave.sscontact=sscontact
            AemployeelistSave.sfathername=sfathername
            AemployeelistSave.sfathercontact=sfathercontact
            AemployeelistSave.smothername=smothername
            AemployeelistSave.schildrenname1=schildrenname1
            AemployeelistSave.schildrenname2=schildrenname2
            AemployeelistSave.schildrenname3=schildrenname3
            AemployeelistSave.schildrenname4=schildrenname4
            AemployeelistSave.schildrenname5=schildrenname5
            AemployeelistSave.sdateofbirth=sdateofbirth 
            AemployeelistSave.sinsurancedetails=sinsurancedetails
            AemployeelistSave.sbankname=sbankname
            AemployeelistSave.sifsccode=sifsccode
            AemployeelistSave.bankaccountno=bankaccountno 
            AemployeelistSave.ldeptid=ldeptid
            AemployeelistSave.lreportmanagerid=lreportmanagerid
            AemployeelistSave.ldesignationid=ldesignationid
            AemployeelistSave.lage=lage
            AemployeelistSave.badmin=badmin
            AemployeelistSave.bpm=bpm
            AemployeelistSave.bprojectmanager=bprojectmanager
            AemployeelistSave.bdeveloper=bdeveloper
            AemployeelistSave.btester=btester
            AemployeelistSave.bothers=bothers
            AemployeelistSave.bactive=bactive
            AemployeelistSave.bmanagement=bmanagement
            AemployeelistSave.bit=bit
            AemployeelistSave.binsurance=binsurance
            AemployeelistSave.bta=bta
            AemployeelistSave.bmedicalallow=bmedicalallow
            AemployeelistSave.bda=bda
            AemployeelistSave.bpf=bpf
            AemployeelistSave.besi=besi
            AemployeelistSave.fcosttocompanyperhour=fcosttocompanyperhour
            AemployeelistSave.fcosttocompany1=fcosttocompany1
            AemployeelistSave.fcosttocompany2=fcosttocompany2
            AemployeelistSave.fcosttocompany3=fcosttocompany3
            AemployeelistSave.fcosttocompany4=fcosttocompany4
            AemployeelistSave.fcosttocompany5=fcosttocompany5
            AemployeelistSave.fcosttocompany6=fcosttocompany6
            AemployeelistSave.fcosttocompany7=fcosttocompany7
            AemployeelistSave.fcosttocompany8=fcosttocompany8
            AemployeelistSave.fcosttocompany9=fcosttocompany9
            AemployeelistSave.fcosttocompany10=fcosttocompany10
            AemployeelistSave.fcosttocompany11=fcosttocompany11
            AemployeelistSave.fcosttocompany12=fcosttocompany12
            AemployeelistSave.fcosttocompany13=fcosttocompany13
            AemployeelistSave.fcosttocompany14=fcosttocompany14
            AemployeelistSave.fcosttocompany15=fcosttocompany15
            AemployeelistSave.fcosttocompany16=fcosttocompany16
            AemployeelistSave.fcosttocompany17=fcosttocompany17
            AemployeelistSave.fcosttocompany18=fcosttocompany18
            AemployeelistSave.fcosttocompany19=fcosttocompany19
            AemployeelistSave.fcosttocompany20=fcosttocompany20

            
            AemployeelistSave.save()
            messages.success(request, 'Record is saved.')
            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
            Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
            AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
            Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
            Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
            return render(request, "iWorkPro/EmployeelistEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'Adesignationlist_list':Adesignationlist_list,
                        'AemployeelistRepManager_list':AemployeelistRepManager_list,
                        'ReportingManagerID':ReportingManagerID,
                        'lDepartmentID':lDepartmentID,
                        'lDesignationID':lDesignationID,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'EmployeeList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Employee', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'EmployeeName':EmployeeName,
            }
                        ) 

        if 'UploadFilePhoto' in request.FILES:
            if  request.method == 'POST' and request.FILES['UploadFilePhoto']: 
                    

                #request.session['lhistorymainid'] = lID
                myfile = request.FILES['UploadFilePhoto']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                uploaded_file_url = fs.url(filename)
                filenamePath = "/media/" + filename
                #filepath =  BASE_DIR + filenamePath
                AemployeelistSave = Aemployeelist.objects.get(lid=lID) 
                AemployeelistSave.sphotofile=filenamePath
                AemployeelistSave.susername=susername 
                if(txtPassword == ""):
                    AemployeelistSave.spassword=spassword
                AemployeelistSave.sempemailid=sempemailid
                AemployeelistSave.smobile=smobile
                AemployeelistSave.sdeptname=sdeptname
                AemployeelistSave.sreportmanager=sreportmanager
                AemployeelistSave.sdesignation=sdesignation
                AemployeelistSave.dtdateofjleft=dtdateofjleft 
                AemployeelistSave.spfno=spfno
                AemployeelistSave.sesino=sesino
                AemployeelistSave.sadharno=sadharno
                AemployeelistSave.spanno=spanno
                AemployeelistSave.sbloodgroup=sbloodgroup
                AemployeelistSave.saddress=saddress
                AemployeelistSave.sspousename=sspousename
                AemployeelistSave.sscontact=sscontact
                AemployeelistSave.sfathername=sfathername
                AemployeelistSave.sfathercontact=sfathercontact
                AemployeelistSave.smothername=smothername
                AemployeelistSave.schildrenname1=schildrenname1
                AemployeelistSave.schildrenname2=schildrenname2
                AemployeelistSave.schildrenname3=schildrenname3
                AemployeelistSave.schildrenname4=schildrenname4
                AemployeelistSave.schildrenname5=schildrenname5
                AemployeelistSave.sdateofbirth=sdateofbirth 
                AemployeelistSave.sinsurancedetails=sinsurancedetails
                AemployeelistSave.sbankname=sbankname
                AemployeelistSave.sifsccode=sifsccode
                AemployeelistSave.bankaccountno=bankaccountno 
                AemployeelistSave.ldeptid=ldeptid
                AemployeelistSave.lreportmanagerid=lreportmanagerid
                AemployeelistSave.ldesignationid=ldesignationid
                AemployeelistSave.lage=lage
                AemployeelistSave.badmin=badmin
                AemployeelistSave.bpm=bpm
                AemployeelistSave.bprojectmanager=bprojectmanager
                AemployeelistSave.bdeveloper=bdeveloper
                AemployeelistSave.btester=btester
                AemployeelistSave.bothers=bothers
                AemployeelistSave.bactive=bactive
                AemployeelistSave.bmanagement=bmanagement
                AemployeelistSave.bit=bit
                AemployeelistSave.binsurance=binsurance
                AemployeelistSave.bta=bta
                AemployeelistSave.bmedicalallow=bmedicalallow
                AemployeelistSave.bda=bda
                AemployeelistSave.bpf=bpf
                AemployeelistSave.besi=besi
                AemployeelistSave.fcosttocompanyperhour=fcosttocompanyperhour
                AemployeelistSave.fcosttocompany1=fcosttocompany1
                AemployeelistSave.fcosttocompany2=fcosttocompany2
                AemployeelistSave.fcosttocompany3=fcosttocompany3
                AemployeelistSave.fcosttocompany4=fcosttocompany4
                AemployeelistSave.fcosttocompany5=fcosttocompany5
                AemployeelistSave.fcosttocompany6=fcosttocompany6
                AemployeelistSave.fcosttocompany7=fcosttocompany7
                AemployeelistSave.fcosttocompany8=fcosttocompany8
                AemployeelistSave.fcosttocompany9=fcosttocompany9
                AemployeelistSave.fcosttocompany10=fcosttocompany10
                AemployeelistSave.fcosttocompany11=fcosttocompany11
                AemployeelistSave.fcosttocompany12=fcosttocompany12
                AemployeelistSave.fcosttocompany13=fcosttocompany13
                AemployeelistSave.fcosttocompany14=fcosttocompany14
                AemployeelistSave.fcosttocompany15=fcosttocompany15
                AemployeelistSave.fcosttocompany16=fcosttocompany16
                AemployeelistSave.fcosttocompany17=fcosttocompany17
                AemployeelistSave.fcosttocompany18=fcosttocompany18
                AemployeelistSave.fcosttocompany19=fcosttocompany19
                AemployeelistSave.fcosttocompany20=fcosttocompany20

                
                AemployeelistSave.save()
                # return redirect("EmployeeList")  

                messages.success(request, 'Record is saved.')
                Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
                Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
                return render(request, "iWorkPro/EmployeelistEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                            'Adepartmentlist_list':Adepartmentlist_list,
                            'Adesignationlist_list':Adesignationlist_list,
                            'AemployeelistRepManager_list':AemployeelistRepManager_list,
                            'ReportingManagerID':ReportingManagerID,
                            'lDepartmentID':lDepartmentID,
                            'lDesignationID':lDesignationID,

                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'EmployeeList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Employee', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'EmployeeName':EmployeeName,
                }
                        )



        if 'UploadFilePDocument' in request.FILES:
            if  request.method == 'POST' and request.FILES['UploadFilePDocument']: 
            
                sDocVal = ""
                if 'DocumentType' in request.POST:
                    sDocVal=request.POST['DocumentType'] #('Machine')
                    if(sDocVal=="0") or (sDocVal==""):
                    
                        messages.error(request, 'Document Type is not selected. Please Select and then try!')

                        Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                        Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                        Aemployeelist_list = Aemployeelist.objects.get(lid=lID)  
                        Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
                        return render(request, "iWorkPro/EmployeelistEdit.html", 
                        {
                                    'title':'Login list', 
                                    'message':'Your Login list page.',
                                    'year':datetime.now().year,
                                    'badmin': request.session['badmin'] ,  
                                    'bEmployeePM': request.session['bEmployeePM'] ,  
                                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                                    'bothers': request.session['bothers'] ,  
                                    'btester': request.session['btester'] ,  
                                    'bdeveloper': request.session['bdeveloper'] ,  
                                    'bpm': request.session['bpm'] ,   
                                    'bEmployee': 0 ,  
                                    'bCustomer': 1 ,    
                                    'bHome':0,
                                    
                                    'Aemployeelist_list':Aemployeelist_list,
                                    'Aemployeedoclist_list':Aemployeedoclist_list,
                                    'Adepartmentlist_list':Adepartmentlist_list,
                                    'Adesignationlist_list':Adesignationlist_list,
                                    'AemployeelistRepManager_list':AemployeelistRepManager_list,
                                    'ReportingManagerID':ReportingManagerID,
                                    'lDepartmentID':lDepartmentID,
                                    'lDesignationID':lDesignationID,

                                    'sName':request.session['sname'] , 
                                    'Menu1':'Dashboard',  
                                    
                                    'Menu2':'EmployeeList', 
                                    'Menu3':'View & Edit', 
                                    'Menu4':'', 
                                    'Menu5':'',
                                        'MenuName1':'Home', 
                                        'MenuName2':'Employee', 
                                        'MenuName3':'View & Edit', 
                                        'MenuName4':'', 
                                        'MenuName5':'',  
                                        'EmployeeName':EmployeeName,
                        }
                                )
                    else:
                    

                        #request.session['lhistorymainid'] = lID
                        myfile = request.FILES['UploadFilePDocument']
                        fs = FileSystemStorage()
                        filename = fs.save(myfile.name, myfile)
                        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        uploaded_file_url = fs.url(filename)
                        filenamePath = "/media/" + filename
                        #filepath =  BASE_DIR + filenamePath 

                        AemployeelistDocSave = Aemployeedoclist(lemployeeid=lID, sfiledesc=sDocVal, sfilename= filenamePath)
                        AemployeelistDocSave.save()

                        messages.success(request, 'Document is Uploaded.')
                        Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
                        Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
                        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
                        Aemployeelist_list = Aemployeelist.objects.get(lid=lID) 
                        Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
                        EmployeeName=Aemployeelist_list.susername
                        return render(request, "iWorkPro/EmployeelistEdit.html", 
                        {
                                    'title':'Login list', 
                                    'message':'Your Login list page.',
                                    'year':datetime.now().year,
                                    'badmin': request.session['badmin'] ,  
                                    'bEmployeePM': request.session['bEmployeePM'] ,  
                                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                                    'bothers': request.session['bothers'] ,  
                                    'btester': request.session['btester'] ,  
                                    'bdeveloper': request.session['bdeveloper'] ,  
                                    'bpm': request.session['bpm'] ,   
                                    'bEmployee': 0 ,  
                                    'bCustomer': 1 ,    
                                    'bHome':0,
                                    'Aemployeelist_list':Aemployeelist_list,
                                    'Aemployeedoclist_list':Aemployeedoclist_list,
                                    'Adepartmentlist_list':Adepartmentlist_list,
                                    'Adesignationlist_list':Adesignationlist_list,
                                    'AemployeelistRepManager_list':AemployeelistRepManager_list,
                                    'ReportingManagerID':ReportingManagerID,
                                    'lDepartmentID':lDepartmentID,
                                    'lDesignationID':lDesignationID,
                                    
                                    'sName':request.session['sname'] , 
                                    'Menu1':'Dashboard',  
                                    
                                    'Menu2':'EmployeeList', 
                                    'Menu3':'View & Edit', 
                                    'Menu4':'', 
                                    'Menu5':'',
                                        'MenuName1':'Home', 
                                        'MenuName2':'Employee', 
                                        'MenuName3':'View & Edit', 
                                        'MenuName4':'', 
                                        'MenuName5':'',  
                                        'EmployeeName':EmployeeName,
                        }
                                    )

    else:  
        
        Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
        Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
        AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
        Aemployeelist_list = Aemployeelist.objects.get(lid=lID) 
        Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
        EmployeeName=Aemployeelist_list.susername
        return render(request, "iWorkPro/EmployeelistEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    'Aemployeelist_list':Aemployeelist_list,
                            'Aemployeedoclist_list':Aemployeedoclist_list,
                    'Adepartmentlist_list':Adepartmentlist_list,
                    'Adesignationlist_list':Adesignationlist_list,
                    'AemployeelistRepManager_list':AemployeelistRepManager_list,
                    'ReportingManagerID':ReportingManagerID,
                    'lDepartmentID':lDepartmentID,
                    'lDesignationID':lDesignationID,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'EmployeeList', 
                    'Menu3':'View & Edit', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Employee', 
                        'MenuName3':'View & Edit', 
                        'MenuName4':'', 
                        'MenuName5':'',  
                        'EmployeeName':EmployeeName,
        }
                    )


    
    
@csrf_exempt
def EmployeelistDetails(request):


    lDepartmentID =0
    ReportingManagerID =0
    lDesignationID =0
    ReportingManagerID=0
    txtName=""
    EmployeeName=""
    if(request.session['username']  == ""): 
        return redirect("Logout")  
  
    lID =0
    lID = int(request.session['lLoginID'])

    Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname').values() 
    Adesignationlist_list = Adesignationlist.objects.order_by('sdesignation').values() 
    AemployeelistRepManager_list = Aemployeelist.objects.order_by('susername') 
    Aemployeelist_list = Aemployeelist.objects.get(lid=lID) 
    Aemployeedoclist_list = Aemployeedoclist.objects.filter(lemployeeid=lID).order_by('-lid').values()
    EmployeeName=Aemployeelist_list.susername
    return render(request, "iWorkPro/EmployeelistDetails.html", 
    {
                'title':'Login list', 
                'message':'Your Login list page.',
                'year':datetime.now().year,
                'badmin': request.session['badmin'] ,  
                'bEmployeePM': request.session['bEmployeePM'] ,  
                'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                'bothers': request.session['bothers'] ,  
                'btester': request.session['btester'] ,  
                'bdeveloper': request.session['bdeveloper'] ,  
                'bpm': request.session['bpm'] ,   
                'bEmployee': 0 ,  
                'bCustomer': 1 ,    
                'bHome':0,
                'Aemployeelist_list':Aemployeelist_list,
                        'Aemployeedoclist_list':Aemployeedoclist_list,
                'Adepartmentlist_list':Adepartmentlist_list,
                'Adesignationlist_list':Adesignationlist_list,
                'AemployeelistRepManager_list':AemployeelistRepManager_list,
                'ReportingManagerID':ReportingManagerID,
                'lDepartmentID':lDepartmentID,
                'lDesignationID':lDesignationID,
                
                'sName':request.session['sname'] , 
                'Menu1':'Dashboard',  
                    
                'Menu2':'My Details', 
                'Menu3':'', 
                'Menu4':'', 
                'Menu5':'',
                    'MenuName1':'Home', 
                    'MenuName2':'Employee', 
                    'MenuName3':'View & Edit', 
                    'MenuName4':'', 
                    'MenuName5':'',  
                    'EmployeeName':EmployeeName,
    }
                )



    
@csrf_exempt
def DepartmentList(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Adepartmentlist_list = Adepartmentlist.objects.filter(sdeptname__contains = txtSearch).order_by('sdeptname').values() 
            return render(request, "iWorkPro/DepartmentList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DepartmentList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'sSearch':txtSearch,
                        'Adepartmentlist_list':Adepartmentlist_list,
                        'MenuName1':'Home', 
                        'MenuName2':'Department', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname') 
            return render(request, "iWorkPro/DepartmentList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DepartmentList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Department', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Adepartmentlist_list':Adepartmentlist_list
            }
                        )
    else:  


        Adepartmentlist_list = Adepartmentlist.objects.order_by('sdeptname') 
        return render(request, "iWorkPro/DepartmentList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DepartmentList', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Department', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                    'sSearch':'',
                    'Adepartmentlist_list':Adepartmentlist_list
        }
                    )
    

    
@csrf_exempt
def DepartmentListAdd(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtName=""

    if request.method == "POST":
        data = request.POST
        
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 

        if(txtName==""): 
            messages.error(request, 'Department is not entered. Please enter and then try to save')
            return render(request, "iWorkPro/DepartmentListAdd.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DepartmentList', 
                        'Menu3':'New Department', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Department', 
                            'MenuName3':'Create New', 
                            'MenuName4':'', 
                            'MenuName5':'',   
            }
                        )
        else:
            sdeptname=""
            sdeptname=txtName
            AdepartmentlistSave = Adepartmentlist(sdeptname=sdeptname)
            AdepartmentlistSave.save()
            return redirect("DepartmentList")  


    else:  
        return render(request, "iWorkPro/DepartmentListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DepartmentList', 
                    'Menu3':'New Department', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Department', 
                        'MenuName3':'Create New', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )
    
    
@csrf_exempt
def DepartmentListEdit(request,lID):

    txtName=""
    DepartmentName=""
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 
 

        if(txtName==""): 
            messages.error(request, 'Department is not entered. Please enter and then try to save')
            return render(request, "iWorkPro/DepartmentListEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DepartmentList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Department', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'DepartmentName':DepartmentName,
            }
                        )
        else:
            sdeptname=""
            sdeptname=txtName
            AdepartmentlistSave = Adepartmentlist.objects.get(lid=lID) 
            AdepartmentlistSave.sdeptname=sdeptname
            AdepartmentlistSave.save()
            return redirect("DepartmentList")  


    else:  
        
        Adepartmentlist_list = Adepartmentlist.objects.get(lid=lID) 
        DepartmentName=Adepartmentlist_list.sdeptname
        return render(request, "iWorkPro/DepartmentListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DepartmentList', 
                    'Menu3':'View & Edit', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Department', 
                        'MenuName3':'View & Edit', 
                        'MenuName4':'', 
                        'MenuName5':'',  
                        'DepartmentName':DepartmentName,
        }
                    )



    
@csrf_exempt
def DesignationList(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            ADesignationlist_list = Adesignationlist.objects.filter(sdesignation__contains = txtSearch).order_by('sdesignation').values() 
            return render(request, "iWorkPro/DesignationList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DesignationList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'sSearch':txtSearch,
                        'ADesignationlist_list':ADesignationlist_list,
                        'MenuName1':'Home', 
                        'MenuName2':'Designation', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            ADesignationlist_list = Adesignationlist.objects.order_by('sdesignation') 
            return render(request, "iWorkPro/DesignationList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DesignationList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Designation', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'ADesignationlist_list':ADesignationlist_list
            }
                        )
    else:  


        ADesignationlist_list = Adesignationlist.objects.order_by('sdesignation') 
        return render(request, "iWorkPro/DesignationList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DesignationList', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Designation', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                    'sSearch':'',
                    'ADesignationlist_list':ADesignationlist_list
        }
                    )
    

    
@csrf_exempt
def DesignationListAdd(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtName=""

    if request.method == "POST":
        data = request.POST
        
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 

        if(txtName==""): 
            messages.error(request, 'Designation is not entered. Please enter and then try to save')
            return render(request, "iWorkPro/DesignationListAdd.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DesignationList', 
                        'Menu3':'New Designation', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Designation', 
                            'MenuName3':'Create New', 
                            'MenuName4':'', 
                            'MenuName5':'',   
            }
                        )
        else:
            sdesignation=""
            sdesignation=txtName
            ADesignationlistSave = Adesignationlist(sdesignation=sdesignation)
            ADesignationlistSave.save()
            return redirect("DesignationList")  


    else:  
        return render(request, "iWorkPro/DesignationListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DesignationList', 
                    'Menu3':'New Designation', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Designation', 
                        'MenuName3':'Create New', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )
    
    
@csrf_exempt
def DesignationListEdit(request,lID):

    txtName=""
    DesignationName=""
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 
 

        if(txtName==""): 
            messages.error(request, 'Designation is not entered. Please enter and then try to save')
            ADesignationlist_list = Adesignationlist.objects.get(lid=lID) 
            DesignationName=ADesignationlist_list.sdesignation
            return render(request, "iWorkPro/DesignationListEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'DesignationList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Designation', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'DesignationName':DesignationName,
            }
                        )
        else:
            sdesignation=""
            sdesignation=txtName
            ADesignationlistSave = Adesignationlist.objects.get(lid=lID) 
            ADesignationlistSave.sdesignation=sdesignation
            ADesignationlistSave.save()
            return redirect("DesignationList")  


    else:  
        
        ADesignationlist_list = Adesignationlist.objects.get(lid=lID) 
        DesignationName=ADesignationlist_list.sdesignation
        return render(request, "iWorkPro/DesignationListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'DesignationList', 
                    'Menu3':'View & Edit', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Designation', 
                        'MenuName3':'View & Edit', 
                        'MenuName4':'', 
                        'MenuName5':'',  
                        'DesignationName':DesignationName,
        }
                    )



    
@csrf_exempt
def CategoryList(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtSearch=""
    if request.method == "POST":
        data = request.POST
    
        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Aprojectcategorylist_list = Aprojectcategorylist.objects.filter(scategoryname__contains = txtSearch).order_by('scategoryname').values() 
            return render(request, "iWorkPro/CategoryList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CategoryList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'sSearch':txtSearch,
                        'Aprojectcategorylist_list':Aprojectcategorylist_list,
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
            return render(request, "iWorkPro/CategoryList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CategoryList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Aprojectcategorylist_list':Aprojectcategorylist_list
            }
                        )
    else:  


        Aprojectcategorylist_list = Aprojectcategorylist.objects.order_by('scategoryname') 
        return render(request, "iWorkPro/CategoryList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'CategoryList', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                    'sSearch':'',
                    'Aprojectcategorylist_list':Aprojectcategorylist_list
        }
                    )
    

    
@csrf_exempt
def CategoryListAdd(request):

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    txtName=""

    if request.method == "POST":
        data = request.POST
        
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 

        if(txtName==""): 
            messages.error(request, 'Category is not entered. Please enter and then try to save')
            return render(request, "iWorkPro/CategoryListAdd.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CategoryList', 
                        'Menu3':'New Category', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Category', 
                            'MenuName3':'Create New', 
                            'MenuName4':'', 
                            'MenuName5':'',   
            }
                        )
        else:
            scategoryname=""
            scategoryname=txtName
            AprojectcategorylistSave = Aprojectcategorylist(scategoryname=scategoryname)
            AprojectcategorylistSave.save()
            return redirect("CategoryList")  


    else:  
        return render(request, "iWorkPro/CategoryListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'CategoryList', 
                    'Menu3':'New Category', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'Create New', 
                        'MenuName4':'', 
                        'MenuName5':'',   
        }
                    )
    
    
@csrf_exempt
def CategoryListEdit(request,lID):

    txtName=""
    CategoryName=""
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST
        if 'txtName' in request.POST: 
            txtName=data.get("txtName") 
 

        if(txtName==""): 
            messages.error(request, 'Category is not entered. Please enter and then try to save')
            Aprojectcategorylist_list = Aprojectcategorylist.objects.get(lid=lID) 
            CategoryName=Aprojectcategorylist_list.scategoryname
            return render(request, "iWorkPro/CategoryListEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CategoryList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Category', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'CategoryName':CategoryName,
            }
                        )
        else:
            scategoryname=""
            scategoryname=txtName
            AprojectcategorylistSave = Aprojectcategorylist.objects.get(lid=lID) 
            AprojectcategorylistSave.scategoryname=scategoryname
            AprojectcategorylistSave.save()
            return redirect("CategoryList")  


    else:  
        
        Aprojectcategorylist_list = Aprojectcategorylist.objects.get(lid=lID) 
        CategoryName=Aprojectcategorylist_list.scategoryname
        return render(request, "iWorkPro/CategoryListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'CategoryList', 
                    'Menu3':'View & Edit', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'View & Edit', 
                        'MenuName4':'', 
                        'MenuName5':'',  
                        'CategoryName':CategoryName,
        }
                    )



 



    
@csrf_exempt
def CustomerList(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


        if 'cmdSearch' in request.POST:  

            txtSearch=data.get("txtSearch") 

            Acustomerlst_list = Acustomerlst.objects.filter(scustomername__contains = txtSearch).order_by('scustomername').values() 
            return render(request, "iWorkPro/CustomerList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CustomerList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'sSearch':txtSearch,
                        'Acustomerlst_list':Acustomerlst_list,
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
            }
                        )





            
        if 'cmdRefresh' in request.POST:  

            Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
            return render(request, "iWorkPro/CustomerList.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CustomerList', 
                        'Menu3':'', 
                        'Menu4':'', 
                        'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                        'sSearch':'',
                        'Acustomerlst_list':Acustomerlst_list
            }
                        )
    else:  


        Acustomerlst_list = Acustomerlst.objects.order_by('scustomername') 
        return render(request, "iWorkPro/CustomerList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'CustomerList', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Category', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',   
                    'sSearch':'',
                    'Acustomerlst_list':Acustomerlst_list
        }
                    )
    

    
    

    
@csrf_exempt
def CustomerListAdd(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  

        scustomername = ""
        slocation=""
        bdomestric =1
        binternational=0
        bprioritya=1
        bpriorityb=0
        bpriorityc=0
        bpriorityd=0
        lprojecctnocount=0
        scustomerabv = ""

        AcustomerlstNewSave = Acustomerlst(scustomername =  scustomername, 	slocation =  slocation, 	bdomestric =  bdomestric, 	binternational =  binternational, 	bprioritya=bprioritya, bpriorityb=bpriorityb, bpriorityc=bpriorityc, bpriorityd=bpriorityd, lprojecctnocount=lprojecctnocount,scustomerabv=scustomerabv)
        AcustomerlstNewSave.save()
        



        lNewID =0
        lNewID =AcustomerlstNewSave.lid


        


        return redirect("CustomerListEdit", lID=lNewID)   
        

 
    
    
@csrf_exempt
def CustomerListEdit(request,lID):

    scustomername = ""
    slocation=""
    bdomestric =1
    binternational=0
    bprioritya=0
    bpriorityb=0
    bpriorityc=0
    bpriorityd=0

    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST

        
        if 'cmdContactSave' in request.POST:

            txtContactContactName=""
            if 'txtContactContactName' in request.POST: 
                txtContactContactName=data.get("txtContactContactName") 

            txtContactUserID=""
            if 'txtContactUserID' in request.POST: 
                txtContactUserID=data.get("txtContactUserID") 

            txtContactEmailAddress=""
            if 'txtContactEmailAddress' in request.POST: 
                txtContactEmailAddress=data.get("txtContactEmailAddress") 

            txtContactContactNo=""
            if 'txtContactContactNo' in request.POST: 
                txtContactContactNo=data.get("txtContactContactNo") 


            if(txtContactContactName==""): 
                messages.error(request, 'Customer Contact Name is not entered. Please enter and then try to save')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )
            
            if(txtContactUserID==""): 
                messages.error(request, 'Customer Contact Login ID is not entered. Please enter and then try to save')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )


            if(txtContactEmailAddress==""): 
                messages.error(request, 'Customer Contact EMail Address is not entered. Please enter and then try to save')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )

            if(txtContactContactNo==""): 
                messages.error(request, 'Customer Contact No. is not entered. Please enter and then try to save')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )
            
            if 'txtName' in request.POST: 
                txtName=data.get("txtName") 


            chars = ""
            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ123456789"
            chars1 = ""
            chars1 = "9@#*123456789@#*abcdefghijklmnopqrstuvwxyz9@#*" 
            chars2 = ""
            chars2 = "9@#*abcdefghijklmnopqrstuvwxyz@#*123456789" 
            length=0
            length=4

            sPassword1 = ""
            sPassword1 = "".join(chars[c % len(chars)] for c in urandom(length))

            length=4

            sPassword2 = ""
            sPassword2 = "".join(chars1[c % len(chars1)] for c in urandom(length))
            length=4

            sPassword3 = ""
            sPassword3 = "".join(chars2[c % len(chars2)] for c in urandom(length))

            spassword = ""
            spassword = sPassword3 + sPassword1 + sPassword2
 

            scustomercontactname= txtContactContactName
            suserid= txtContactUserID
            spassword= spassword
            bactive= 1
            sempemailid= txtContactEmailAddress
            smobile= txtContactContactNo
            lcustomerid= lID
            scustomername= txtName

                 
            AcustomercontactlistNewSave = Acustomercontactlist(scustomercontactname =  scustomercontactname, 	suserid =  suserid, 	spassword =  spassword, 	bactive =  bactive, 	sempemailid=sempemailid, smobile=smobile, lcustomerid=lcustomerid, scustomername=scustomername)
            AcustomercontactlistNewSave.save()
            


            lUserId =0
            sEmail = ""  
            sEmail = txtContactEmailAddress
            connection = mail.get_connection()
            email1 = mail.EmailMessage(
                    "iWorkPro - New Employee Created",
                "Hi, \n Information from www.Dhruthi.org:8004 - iWorkPro \n For your LoginID : " + txtContactUserID + " \n Your new Password : " + spassword + "\n\n\n This is notification Mail. Please Don't Reply",
                "iworkproalerts@dhruthi.org",
                [sEmail],
                bcc = ['sanjay@dhruthi.org', 'sanjaybk@dhruthitech.onmicrosoft.com'],
                connection=connection,
            )
            email1.send()


            messages.success(request, 'Customer Contact is saved')
            Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
            Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
            
            CustomerName=Acustomerlst_list.scustomername
            return render(request, "iWorkPro/CustomerListEdit.html", 
            {
                        'title':'Login list', 
                        'message':'Your Login list page.',
                        'year':datetime.now().year,
                        'badmin': request.session['badmin'] ,  
                        'bEmployeePM': request.session['bEmployeePM'] ,  
                        'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                        'bothers': request.session['bothers'] ,  
                        'btester': request.session['btester'] ,  
                        'bdeveloper': request.session['bdeveloper'] ,  
                        'bpm': request.session['bpm'] ,   
                        'bEmployee': 0 ,  
                        'bCustomer': 1 ,    
                        'bHome':0,
                        
                        'Acustomercontactlist_list':Acustomercontactlist_list,
                        'Acustomerlst_list':Acustomerlst_list,
                        'sName':request.session['sname'] , 
                        'Menu1':'Dashboard',  
                        
                        'Menu2':'CustomerList', 
                        'Menu3':'View & Edit', 
                        'Menu4':'', 
                        'Menu5':'',
                            'MenuName1':'Home', 
                            'MenuName2':'Customer', 
                            'MenuName3':'View & Edit', 
                            'MenuName4':'', 
                            'MenuName5':'',  
                            'CustomerName':CustomerName,
            }
                        )


        if 'cmdSave' in request.POST:  
            if 'txtName' in request.POST: 
                txtName=data.get("txtName") 

            if 'txtNameAbv' in request.POST: 
                txtNameAbv=data.get("txtNameAbv") 
    

            if(txtName==""): 
                messages.error(request, 'Customer is not entered. Please enter and then try to save')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )
            else:
                scustomername=""
                scustomername=txtName



                rad_TypeofCustomer = ""
                if 'rad_TypeofCustomer' in request.POST:
                    rad_TypeofCustomer =data.get("rad_TypeofCustomer")  

                if(rad_TypeofCustomer == ""):
                    bdomestric =1
                elif(rad_TypeofCustomer == "Domestic"):
                    bdomestric =1
                else:
                    bdomestric =0
                    binternational=1


                bprioritya =0
                bpriorityb =0
                bpriorityc =0
                bpriorityd =0
                rad_Priority = ""
                if 'rad_Priority' in request.POST:
                    rad_Priority =data.get("rad_Priority")  

                if(rad_Priority == ""):
                    bprioritya =1
                elif(rad_Priority == "PriorityA"):
                    bprioritya =1
                elif(rad_Priority == "PriorityB"):
                    bpriorityb =1
                elif(rad_Priority == "PriorityC"):
                    bpriorityc =1
                else: 
                    bpriorityd=1


                AcustomerlstSave = Acustomerlst.objects.get(lid=lID) 
                AcustomerlstSave.scustomername=scustomername
                AcustomerlstSave.bdomestric=bdomestric
                AcustomerlstSave.binternational=binternational
                AcustomerlstSave.bprioritya=bprioritya
                AcustomerlstSave.bpriorityb=bpriorityb
                AcustomerlstSave.bpriorityc=bpriorityc
                AcustomerlstSave.bpriorityd=bpriorityd
                AcustomerlstSave.scustomerabv=txtNameAbv



                AcustomerlstSave.save()
                messages.success(request, 'Customer is saved')
                Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
                Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values() 
                CustomerName=Acustomerlst_list.scustomername
                return render(request, "iWorkPro/CustomerListEdit.html", 
                {
                            'title':'Login list', 
                            'message':'Your Login list page.',
                            'year':datetime.now().year,
                            'badmin': request.session['badmin'] ,  
                            'bEmployeePM': request.session['bEmployeePM'] ,  
                            'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                            'bothers': request.session['bothers'] ,  
                            'btester': request.session['btester'] ,  
                            'bdeveloper': request.session['bdeveloper'] ,  
                            'bpm': request.session['bpm'] ,   
                            'bEmployee': 0 ,  
                            'bCustomer': 1 ,    
                            'bHome':0,
                            
                            'Acustomercontactlist_list':Acustomercontactlist_list,
                            'Acustomerlst_list':Acustomerlst_list,
                            'sName':request.session['sname'] , 
                            'Menu1':'Dashboard',  
                            
                            'Menu2':'CustomerList', 
                            'Menu3':'View & Edit', 
                            'Menu4':'', 
                            'Menu5':'',
                                'MenuName1':'Home', 
                                'MenuName2':'Customer', 
                                'MenuName3':'View & Edit', 
                                'MenuName4':'', 
                                'MenuName5':'',  
                                'CustomerName':CustomerName,
                }
                            )


    else:  
        
        Acustomerlst_list = Acustomerlst.objects.get(lid=lID) 
        Acustomercontactlist_list = Acustomercontactlist.objects.filter(lcustomerid=lID).order_by('scustomercontactname').values()
        CustomerName=Acustomerlst_list.scustomername
        return render(request, "iWorkPro/CustomerListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    'Acustomercontactlist_list':Acustomercontactlist_list,
                    'Acustomerlst_list':Acustomerlst_list,
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'CustomerList', 
                    'Menu3':'View & Edit', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'Customer', 
                        'MenuName3':'View & Edit', 
                        'MenuName4':'', 
                        'MenuName5':'',  
                        'CustomerName':CustomerName,
        }
                    )





    
@csrf_exempt
def CustomerContactList(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/CustomerContactList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    

    
@csrf_exempt
def CustomerContactListAdd(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/CustomerContactListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    
    
@csrf_exempt
def CustomerContactListEdit(request,lID):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/CustomerContactListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    


 



    
@csrf_exempt
def ProjectList(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    

    
@csrf_exempt
def ProjectListAdd(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    
    
@csrf_exempt
def ProjectListEdit(request,lID):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    


 



    
@csrf_exempt
def ProjectSubList(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectSubList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    

    
@csrf_exempt
def ProjectSubListAdd(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectSubListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    
    
@csrf_exempt
def ProjectSubListEdit(request,lID):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/ProjectSubListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    


 



    
@csrf_exempt
def TaskList(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/TaskList.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    

    
@csrf_exempt
def TaskListAdd(request):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/TaskListAdd.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    
    
@csrf_exempt
def TaskListEdit(request,lID):

   
    if(request.session['username']  == ""): 
        return redirect("Logout")  
    
    if request.method == "POST":
        data = request.POST


    else:  
        return render(request, "iWorkPro/TaskListEdit.html", 
        {
                    'title':'Login list', 
                    'message':'Your Login list page.',
                    'year':datetime.now().year,
                    'badmin': request.session['badmin'] ,  
                    'bEmployeePM': request.session['bEmployeePM'] ,  
                    'bEmployeeManagement': request.session['bEmployeeManagement'] ,  
                    'bothers': request.session['bothers'] ,  
                    'btester': request.session['btester'] ,  
                    'bdeveloper': request.session['bdeveloper'] ,  
                    'bpm': request.session['bpm'] ,   
                    'bEmployee': 0 ,  
                    'bCustomer': 1 ,    
                    'bHome':0,
                    
                    'sName':request.session['sname'] , 
                    'Menu1':'Dashboard',  
                     
                    'Menu2':'', 
                    'Menu3':'', 
                    'Menu4':'', 
                    'Menu5':'',
                        'MenuName1':'Home', 
                        'MenuName2':'', 
                        'MenuName3':'', 
                        'MenuName4':'', 
                        'MenuName5':'',  
        }
                    )
    


 

 


 
    
 














