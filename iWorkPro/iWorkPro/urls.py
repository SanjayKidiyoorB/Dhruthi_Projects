from django.urls import path
from iWorkPro import views

from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static


urlpatterns = [
    
    path("", views.home, name="home"),
    path("Dashboard/", views.Dashboard, name="Dashboard"),
    path("DashboardCustomer/", views.DashboardCustomer, name="DashboardCustomer"),
    path("Logout/", views.Logout, name="Logout"),


    path("CreateProject/", views.CreateProject, name="CreateProject"),
    path("EditProject/<int:lID>", views.EditProject, name="EditProject"),
    path("ProjectSubList/<int:lID>", views.ProjectSubList, name="ProjectSubList"),
    path("ProjectSubCustomerList/<int:lID>", views.ProjectSubCustomerList, name="ProjectSubCustomerList"),
    path("EditSubProject/<int:lID>", views.EditSubProject, name="EditSubProject"),
    path("SubpojectSubList/<int:lID>", views.SubpojectSubList, name="SubpojectSubList"),


    path("EmployeeList/", views.EmployeeList, name="EmployeeList"),
    path("EmployeeListAdd/", views.EmployeeListAdd, name="EmployeeListAdd"),
    path("EmployeeListEdit/<int:lID>", views.EmployeeListEdit, name="EmployeeListEdit"),
    path("EmployeelistDetails/", views.EmployeelistDetails, name="EmployeelistDetails"), 

    path("DepartmentList/", views.DepartmentList, name="DepartmentList"),
    path("DepartmentListAdd/", views.DepartmentListAdd, name="DepartmentListAdd"),
    path("DepartmentListEdit/<int:lID>", views.DepartmentListEdit, name="DepartmentListEdit"),

    path("DesignationList/", views.DesignationList, name="DesignationList"),
    path("DesignationListAdd/", views.DesignationListAdd, name="DesignationListAdd"),
    path("DesignationListEdit/<int:lID>", views.DesignationListEdit, name="DesignationListEdit"),

    path("CategoryList/", views.CategoryList, name="CategoryList"),
    path("CategoryListAdd/", views.CategoryListAdd, name="CategoryListAdd"),
    path("CategoryListEdit/<int:lID>", views.CategoryListEdit, name="CategoryListEdit"),

    path("CustomerList/", views.CustomerList, name="CustomerList"),
    path("CustomerListAdd/", views.CustomerListAdd, name="CustomerListAdd"),
    path("CustomerListEdit/<int:lID>", views.CustomerListEdit, name="CustomerListEdit"),

    path("CustomerContactList/", views.CustomerContactList, name="CustomerContactList"),
    path("CustomerContactListAdd/", views.CustomerContactListAdd, name="CustomerContactListAdd"),
    path("CustomerContactListEdit/<int:lID>", views.CustomerContactListEdit, name="CustomerContactListEdit"),

    path("ProjectList/", views.ProjectList, name="ProjectList"),
    path("ProjectListAdd/", views.ProjectListAdd, name="ProjectListAdd"),
    path("ProjectListEdit/<int:lID>", views.ProjectListEdit, name="ProjectListEdit"),

    path("ProjectSubList/", views.ProjectSubList, name="ProjectSubList"),
    path("ProjectSubListAdd/", views.ProjectSubListAdd, name="ProjectSubListAdd"),
    path("ProjectSubListEdit/<int:lID>", views.ProjectSubListEdit, name="ProjectSubListEdit"),

    path("TaskList/", views.TaskList, name="TaskList"),
    path("TaskListAdd/", views.TaskListAdd, name="TaskListAdd"),
    path("TaskListEdit/<int:lID>", views.TaskListEdit, name="TaskListEdit"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 