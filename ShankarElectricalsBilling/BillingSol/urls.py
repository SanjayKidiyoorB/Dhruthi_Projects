from django.urls import path
from BillingSol import views, viewsmaster, viewstransaction, viewstransactionMaintenance, viewstransactionProject
 
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
 
 
    path("MaintenanceList/", viewstransactionMaintenance.MaintenanceList, name="MaintenanceList"),
    path("MaintenanceListAdd/", viewstransactionMaintenance.MaintenanceListAdd, name="MaintenanceListAdd"),
    path("MaintenanceListDetails/<int:lID>", viewstransactionMaintenance.MaintenanceListDetails, name="MaintenanceListDetails"),
    path("MaintenanceListDetailsDelete/<int:lID>", viewstransactionMaintenance.MaintenanceListDetailsDelete, name="MaintenanceListDetailsDelete"),

    path("MaintenanceListCopyDetails/<int:lID>", viewstransactionMaintenance.MaintenanceListCopyDetails, name="MaintenanceListCopyDetails"),

    path("MaintenanceListDetailsPrint/<int:lID>", viewstransactionMaintenance.MaintenanceListDetailsPrint, name="MaintenanceListDetailsPrint"),

    path("ProjectList/", viewstransactionProject.ProjectList, name="ProjectList"),
    path("ProjectListAdd/", viewstransactionProject.ProjectListAdd, name="ProjectListAdd"),
    path("ProjectListDetails/<int:lID>", viewstransactionProject.ProjectListDetails, name="ProjectListDetails"),
    path("ProjectListDetailsDelete/<int:lID>", viewstransactionProject.ProjectListDetailsDelete, name="ProjectListDetailsDelete"),

    path("ProjectListCopyDetails/<int:lID>", viewstransactionProject.ProjectListCopyDetails, name="ProjectListCopyDetails"),
    path("ProjectListDetailsPrint/<int:lID>", viewstransactionProject.ProjectListDetailsPrint, name="ProjectListDetailsPrint"),

    path("DCList/", viewstransaction.DCList, name="DCList"),
    path("DCListAdd/", viewstransaction.DCListAdd, name="DCListAdd"),
    path("DCListDetails/<int:lID>", viewstransaction.DCListDetails, name="DCListDetails"),
    path("DCListDetailsDelete/<int:lID>", viewstransaction.DCListDetailsDelete, name="DCListDetailsDelete"),

    path("ProformaList/", viewstransactionProject.ProformaList, name="ProformaList"),
    path("ProformaListAdd/", viewstransactionProject.ProformaListAdd, name="ProformaListAdd"),
    path("ProformaListDetails/<int:lID>", viewstransactionProject.ProformaListDetails, name="ProformaListDetails"),
    path("ProformaListDetailsDelete/<int:lID>", viewstransactionProject.ProformaListDetailsDelete, name="ProformaListDetailsDelete"),
    path("ProformaListPrintDetails/<int:lID>", viewstransactionProject.ProformaListPrintDetails, name="ProformaListPrintDetails"),
    
    path("ProformaListCopyDetails/<int:lID>", viewstransactionProject.ProformaListCopyDetails, name="ProformaListCopyDetails"),


    path("ProformaListCopyInvoiceCreateDetails/<int:lID>", viewstransactionProject.ProformaListCopyInvoiceCreateDetails, name="ProformaListCopyInvoiceCreateDetails"),
    path("ProformaListCopyInvoiceSEZCreateDetails/<int:lID>", viewstransactionProject.ProformaListCopyInvoiceSEZCreateDetails, name="ProformaListCopyInvoiceSEZCreateDetails"),



    path("PurchaseOrderList/", viewstransaction.PurchaseOrderList, name="PurchaseOrderList"),
    path("PurchaseOrderListAdd/", viewstransaction.PurchaseOrderListAdd, name="PurchaseOrderListAdd"),
    path("PurchaseOrderListDetails/<int:lID>", viewstransaction.PurchaseOrderListDetails, name="PurchaseOrderListDetails"),
    path("PurchaseOrderListDetailsDelete/<int:lID>", viewstransaction.PurchaseOrderListDetailsDelete, name="PurchaseOrderListDetailsDelete"),

    path("OrderAcceptanceList/", viewstransaction.OrderAcceptanceList, name="OrderAcceptanceList"),
    path("OrderAcceptanceListAdd/", viewstransaction.OrderAcceptanceListAdd, name="OrderAcceptanceListAdd"),
    path("OrderAcceptanceListDetails/<int:lID>", viewstransaction.OrderAcceptanceListDetails, name="OrderAcceptanceListDetails"),
    path("OrderAcceptanceListDetailsDelete/<int:lID>", viewstransaction.OrderAcceptanceListDetailsDelete, name="OrderAcceptanceListDetailsDelete"),

    path("ProposalList/", viewstransaction.ProposalList, name="ProposalList"),
    path("ProposalListAdd/", viewstransaction.ProposalListAdd, name="ProposalListAdd"),
    path("ProposalListDetails/<int:lID>", viewstransaction.ProposalListDetails, name="ProposalListDetails"),
    path("ProposalListDetailsDelete/<int:lID>", viewstransaction.ProposalListDetailsDelete, name="ProposalListDetailsDelete"),

    path("CreditNoteList/", viewstransaction.CreditNoteList, name="CreditNoteList"),
    path("CreditNoteListAdd/", viewstransaction.CreditNoteListAdd, name="CreditNoteListAdd"),
    path("CreditNoteListDetails/<int:lID>", viewstransaction.CreditNoteListDetails, name="CreditNoteListDetails"),
    path("CreditNoteListDetailsDelete/<int:lID>", viewstransaction.CreditNoteListDetailsDelete, name="CreditNoteListDetailsDelete"),

    path("DebitNoteList/", viewstransaction.DebitNoteList, name="DebitNoteList"),
    path("DebitNoteListAdd/", viewstransaction.DebitNoteListAdd, name="DebitNoteListAdd"),
    path("DebitNoteListDetails/<int:lID>", viewstransaction.DebitNoteListDetails, name="DebitNoteListDetails"),
    path("DebitNoteListDetailsDelete/<int:lID>", viewstransaction.DebitNoteListDetailsDelete, name="DebitNoteListDetailsDelete"),
 
    path("ProformaServiceInvoiceList/", viewstransactionMaintenance.ProformaServiceInvoiceList, name="ProformaServiceInvoiceList"),
    path("ProformaServiceInvoiceListAdd/", viewstransactionMaintenance.ProformaServiceInvoiceListAdd, name="ProformaServiceInvoiceListAdd"),
    path("ProformaServiceInvoiceListDetails/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListDetails, name="ProformaServiceInvoiceListDetails"),
    path("ProformaServiceInvoiceListDetailsDelete/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListDetailsDelete, name="ProformaServiceInvoiceListDetailsDelete"),
 
    path("ProformaServiceInvoiceListCopyDetails/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListCopyDetails, name="ProformaServiceInvoiceListCopyDetails"),

    path("ProformaServiceInvoiceListPrintDetails/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListPrintDetails, name="ProformaServiceInvoiceListPrintDetails"),

    path("ProformaServiceInvoiceListCopyCreateInvoiceDetails/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListCopyCreateInvoiceDetails, name="ProformaServiceInvoiceListCopyCreateInvoiceDetails"),

    path("ProformaServiceInvoiceListCopyCreateInvoiceSEZDetails/<int:lID>", viewstransactionMaintenance.ProformaServiceInvoiceListCopyCreateInvoiceSEZDetails, name="ProformaServiceInvoiceListCopyCreateInvoiceSEZDetails"),


    path("RentInvoiceList/", viewstransaction.RentInvoiceList, name="RentInvoiceList"),
    path("RentInvoiceListAdd/", viewstransaction.RentInvoiceListAdd, name="RentInvoiceListAdd"),
    path("RentInvoiceListDetails/<int:lID>", viewstransaction.RentInvoiceListDetails, name="RentInvoiceListDetails"),
    path("RentInvoiceListDetailsDelete/<int:lID>", viewstransaction.RentInvoiceListDetailsDelete, name="RentInvoiceListDetailsDelete"),
 

  
 
    path("MaintenanceListSEZ/", viewstransactionMaintenance.MaintenanceListSEZ, name="MaintenanceListSEZ"),
    path("MaintenanceListSEZAdd/", viewstransactionMaintenance.MaintenanceListSEZAdd, name="MaintenanceListSEZAdd"),
    path("MaintenanceListSEZDetails/<int:lID>", viewstransactionMaintenance.MaintenanceListSEZDetails, name="MaintenanceListSEZDetails"),
    path("MaintenanceListSEZDetailsDelete/<int:lID>", viewstransactionMaintenance.MaintenanceListSEZDetailsDelete, name="MaintenanceListSEZDetailsDelete"),

    path("MaintenanceListSEZCopyDetails/<int:lID>", viewstransactionMaintenance.MaintenanceListSEZCopyDetails, name="MaintenanceListSEZCopyDetails"),

    path("ProjectListSEZ/", viewstransactionProject.ProjectListSEZ, name="ProjectListSEZ"),
    path("ProjectListSEZAdd/", viewstransactionProject.ProjectListSEZAdd, name="ProjectListSEZAdd"),
    path("ProjectListSEZDetails/<int:lID>", viewstransactionProject.ProjectListSEZDetails, name="ProjectListSEZDetails"),
    path("ProjectListSEZDetailsDelete/<int:lID>", viewstransactionProject.ProjectListSEZDetailsDelete, name="ProjectListSEZDetailsDelete"),

    path("ProjectListSEZCopyDetails/<int:lID>", viewstransactionProject.ProjectListSEZCopyDetails, name="ProjectListSEZCopyDetails"),

    path("ProjectListDetailsPrint/<int:lID>", viewstransactionProject.ProjectListDetailsPrint, name="ProjectListDetailsPrint"),






]