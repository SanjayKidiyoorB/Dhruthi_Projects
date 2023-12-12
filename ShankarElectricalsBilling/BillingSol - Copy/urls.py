from django.urls import path
from BillingSol import views, viewsmaster, viewstransaction
 
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path("", views.home, name="home"),
    path("Dashboard/", views.Dashboard, name="Dashboard"),



    path("CompanyList/", viewsmaster.CompanyList, name="CompanyList"),
    path("CompanyListAdd/", viewsmaster.CompanyListAdd, name="CompanyListAdd"),
    path("CompanyListDetails/<int:lID>", viewsmaster.CompanyListDetails, name="CompanyListDetails"),

    path("ClientList/", viewsmaster.ClientList, name="ClientList"),
    path("ClientListAdd/", viewsmaster.ClientListAdd, name="ClientListAdd"),
    path("ClientListDetails/<int:lID>", viewsmaster.ClientListDetails, name="ClientListDetails"),

    path("SiteList/", viewsmaster.SiteList, name="SiteList"),
    path("SiteListAdd/", viewsmaster.SiteListAdd, name="SiteListAdd"),
    path("SiteListDetails/<int:lID>", viewsmaster.SiteListDetails, name="SiteListDetails"),

    path("SupplierList/", viewsmaster.SupplierList, name="SupplierList"),
    path("SupplierListAdd/", viewsmaster.SupplierListAdd, name="SupplierListAdd"),
    path("SupplierListDetails/<int:lID>", viewsmaster.SupplierListDetails, name="SupplierListDetails"),

    path("UserList/", viewsmaster.UserList, name="UserList"),
    path("UserListAdd/", viewsmaster.UserListAdd, name="UserListAdd"),
    path("UserListDetails/<int:lID>", viewsmaster.UserListDetails, name="UserListDetails"),
 

    path("POList/", viewstransaction.POList, name="POList"),
    path("POListAdd/", viewstransaction.POListAdd, name="POListAdd"),
    path("POListDetails/<int:lID>", viewstransaction.POListDetails, name="POListDetails"),

    path("MaintenanceList/", viewstransaction.MaintenanceList, name="MaintenanceList"),
    path("MaintenanceListAdd/", viewstransaction.MaintenanceListAdd, name="MaintenanceListAdd"),
    path("MaintenanceListDetails/<int:lID>", viewstransaction.MaintenanceListDetails, name="MaintenanceListDetails"),
    path("MaintenanceListDetailsDelete/<int:lID>", viewstransaction.MaintenanceListDetailsDelete, name="MaintenanceListDetailsDelete"),

    path("ProjectList/", viewstransaction.ProjectList, name="ProjectList"),
    path("ProjectListAdd/", viewstransaction.ProjectListAdd, name="ProjectListAdd"),
    path("ProjectListDetails/<int:lID>", viewstransaction.ProjectListDetails, name="ProjectListDetails"),
    path("ProjectListDetailsDelete/<int:lID>", viewstransaction.ProjectListDetailsDelete, name="ProjectListDetailsDelete"),

]