from django.urls import path
from CloudCaliber import views, viewsamasterListdetails, viewsbmasterListdetails
from CloudCaliber import viewscategorycreation, viewsidcreate, views8d, viewscalibrations, viewscalibrations
from CloudCaliber import viewscategorycreation, viewsdamaged, viewsduecalendar, viewsduelist, viewsgaugeusagewise
from CloudCaliber import viewsissuereturn, viewsmasterlist, viewsmasterlistdetails, viewsmsastudy, viewsuserlist
from CloudCaliber import viewsvalidations, viewsahistory, viewsamasterListdetails, viewsbmasterListdetails, viewsMasters, viewsMasters1

from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path("", views.home, name="home"),

 

    path('export/excel', viewsmasterlist.export_Masterlist_xls, name='export_excel'),
    path("export/excel1", viewsduelist.export_Duelist_xls, name="export_excel1"),
    path("export/excel2", viewsduelist.export_OverDuelist_xls, name="export_excel2"),

    path("GaugeMasterlistCreateOLDID/<int:lID>", viewsidcreate.GaugeMasterlistCreateOLDID, name="GaugeMasterlistCreateOLDID"),
    path("GaugeMasterlistCreateOLDUserID/<int:lID>", viewsidcreate.GaugeMasterlistCreateOLDUserID, name="GaugeMasterlistCreateOLDUserID"),

    path("GaugeMasterlistCreateID", viewsidcreate.GaugeMasterlistCreateID, name="GaugeMasterlistCreateID"),

    path('load_Categories/', viewsidcreate.load_Categories, name='ajax_load_Categories'),
    path('load_Classification_Details/', viewsidcreate.load_Classification_Details, name='ajax_load_Classification'),
    path('load_Code_ForAsset/', viewsidcreate.load_Code_ForAsset, name='ajax_loadCode_ForAsset'),

    path('load_Code_FlowLabel1/', viewsidcreate.load_Code_FlowLabel1, name='ajax_loadCode_FlowLabel1'),
    path('load_Code_Flow1/', viewsidcreate.load_Code_Flow1, name='ajax_loadCode_Flow1'), 
    path('load_Code_FlowLabel2/', viewsidcreate.load_Code_FlowLabel2, name='ajax_loadCode_FlowLabel2'),
    path('load_Code_Flow2/', viewsidcreate.load_Code_Flow2, name='ajax_loadCode_Flow2'), 
    path('load_Code_FlowLabel3/', viewsidcreate.load_Code_FlowLabel3, name='ajax_loadCode_FlowLabel3'),
    path('load_Code_Flow3/', viewsidcreate.load_Code_Flow3, name='ajax_loadCode_Flow3'), 
    path('load_Code_FlowLabel4/', viewsidcreate.load_Code_FlowLabel4, name='ajax_loadCode_FlowLabel4'),
    path('load_Code_Flow4/', viewsidcreate.load_Code_Flow4, name='ajax_loadCode_Flow4'), 
    path('load_Code_FlowLabel5/', viewsidcreate.load_Code_FlowLabel5, name='ajax_loadCode_FlowLabel5'),
    path('load_Code_Flow5/', viewsidcreate.load_Code_Flow5, name='ajax_loadCode_Flow5'), 

    path('load_Code_FlowValue1/', viewsidcreate.load_Code_FlowValue1, name='ajax_loadCode_FlowValue1'), 
    path('load_Code_FlowValue2/', viewsidcreate.load_Code_FlowValue2, name='ajax_loadCode_FlowValue2'),
    path('load_Code_FlowValue3/', viewsidcreate.load_Code_FlowValue3, name='ajax_loadCode_FlowValue3'),
    path('load_Code_FlowValue4/', viewsidcreate.load_Code_FlowValue4, name='ajax_loadCode_FlowValue4'),
    path('load_Code_FlowValue5/', viewsidcreate.load_Code_FlowValue5, name='ajax_loadCode_FlowValue5'),
    path('load_loadCodeIDNewChecked_ForAsset/', viewsidcreate.load_loadCodeIDNewChecked_ForAsset, name='ajax_loadCodeIDNewChecked_ForAsset'),

 





    # path('load_CategoriesDue/', viewsduelist.load_CategoriesDue, name='ajax_load_CategoriesDue'),
    # path('load_Classification_DetailsDue/', viewsduelist.load_Classification_DetailsDue, name='ajax_load_ClassificationDue'),
     
    # path('load_Code_FlowLabel1Due/', viewsduelist.load_Code_FlowLabel1Due, name='ajax_loadCode_FlowLabel1Due'),  
    # path('load_Code_Flow1Due/', viewsduelist.load_Code_Flow1Due, name='ajax_loadCode_Flow1Due'), 
    # path('load_Code_FlowLabel2Due/', viewsduelist.load_Code_FlowLabel2Due, name='ajax_loadCode_FlowLabel2Due'),
    # path('load_Code_Flow2Due/', viewsduelist.load_Code_Flow2Due, name='ajax_loadCode_Flow2Due'), 
    # path('load_Code_FlowLabel3Due/', viewsduelist.load_Code_FlowLabel3Due, name='ajax_loadCode_FlowLabel3Due'),
    # path('load_Code_Flow3Due/', viewsduelist.load_Code_Flow3Due, name='ajax_loadCode_Flow3Due'), 
    # path('load_Code_FlowLabel4Due/', viewsduelist.load_Code_FlowLabel4Due, name='ajax_loadCode_FlowLabel4Due'),
    # path('load_Code_Flow4Due/', viewsduelist.load_Code_Flow4Due, name='ajax_loadCode_Flow4Due'), 
    # path('load_Code_FlowLabel5Due/', viewsduelist.load_Code_FlowLabel5Due, name='ajax_loadCode_FlowLabel5Due'),
    # path('load_Code_Flow5Due/', viewsduelist.load_Code_Flow5Due, name='ajax_loadCode_Flow5Due'), 


    path("GaugeMasterlistUnderPurchase/", viewsmasterlist.GaugeMasterlistUnderPurchase, name="GaugeMasterlistUnderPurchase"),


    path("GaugeMasterlistIdle/", viewsmasterlist.GaugeMasterlistIdle, name="GaugeMasterlistIdle"), 
    path("GaugeMasterlistSpare/", viewsmasterlist.GaugeMasterlistSpare, name="GaugeMasterlistSpare"), 
    path("GaugeMasterlistIssueIdle/", viewsmasterlist.GaugeMasterlistIssueIdle, name="GaugeMasterlistIssueIdle"),
    path("GaugeMasterlistIssueSpare/", viewsmasterlist.GaugeMasterlistIssueSpare, name="GaugeMasterlistIssueSpare"),
    path("GaugeIssueReturn/", viewsmasterlist.GaugeIssueReturn, name="GaugeIssueReturn"),
    path("GaugeIssuelist/", viewsmasterlist.GaugeIssuelist, name="GaugeIssuelist"),

    path("GaugeMasterlistIssued/", viewsmasterlist.GaugeMasterlistIssued, name="GaugeMasterlistIssued"), 
    path("GaugeMasterlistDamaged/", viewsmasterlist.GaugeMasterlistDamaged, name="GaugeMasterlistDamaged"), 
    path("GaugeMasterlistMissing/", viewsmasterlist.GaugeMasterlistMissing, name="GaugeMasterlistMissing"), 
    path("GaugeMasterlistLimitedUsage/", viewsmasterlist.GaugeMasterlistLimitedUsage, name="GaugeMasterlistLimitedUsage"), 
    path("GaugeMasterlistOutofCalibration/", viewsmasterlist.GaugeMasterlistOutofCalibration, name="GaugeMasterlistOutofCalibration"), 
    path("GaugeMasterlistScraped/", viewsmasterlist.GaugeMasterlistScraped, name="GaugeMasterlistScraped"), 
    path("GaugeUnderCalibration/", viewsmasterlist.GaugeUnderCalibration, name="GaugeUnderCalibration"),


    path("GaugeMasterListListDetails/", viewsmasterlist.GaugeMasterListListDetails, name="GaugeMasterListListDetails"),
    path("GaugeMasterListListCalibrationDetails/", viewsmasterlist.GaugeMasterListListCalibrationDetails, name="GaugeMasterListListCalibrationDetails"),

    path("PlantAssetViewDashboard/", views.PlantAssetViewDashboard, name="PlantAssetViewDashboard"),
    path("AdminMasterlistDashboard/", views.AdminMasterlistDashboard, name="AdminMasterlistDashboard"),
    path("AdministratorDashboard/", views.AdministratorDashboard, name="AdministratorDashboard"),
    path("AdministratorDashboardA/", views.AdministratorDashboardA, name="AdministratorDashboardA"),

    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"), 
    path("Dashboard/", views.Dashboard, name="Dashboard"), 
    path("SignINClicked/", views.SignINClicked, name="SignINClicked"), 
    path("GaugeScheduler/", views.GaugeScheduler, name="GaugeScheduler"),


    path("GaugeIssue/<int:lID>", viewsissuereturn.GaugeIssue, name="GaugeIssue"),
    path("GaugeReturn/<int:lID>", viewsissuereturn.GaugeReturn, name="GaugeReturn"),


    path("GaugeMSA/", views.GaugeMSA, name="GaugeMSA"),
    path("GaugeUtility/", views.GaugeUtility, name="GaugeUtility"),
    path("GaugeMasters/", views.GaugeMasters, name="GaugeMasters"), 
    path("GaugeAdministrator/", views.GaugeAdministrator, name="GaugeAdministrator"),
    path("GaugeCalibration30DaysDue/", viewsduelist.GaugeCalibration30DaysDue, name="GaugeCalibration30DaysDue"), 
    path("GaugeMasterDueList/", viewsduelist.GaugeMasterDueList, name="GaugeMasterDueList"),
    path("GaugeMasterOverDueList/", viewsduelist.GaugeMasterOverDueList, name="GaugeMasterOverDueList"),
    path("GaugeMSADue1Year/", viewsduelist.GaugeMSADue1Year, name="GaugeMSADue1Year"),
    path("GaugeMSAHistory/", viewsduelist.GaugeMSAHistory, name="GaugeMSAHistory"),
    path("Gauge8DHistory/", viewsduelist.Gauge8DHistory, name="Gauge8DHistory"),   
    path("GaugeMSADue/", viewsduelist.GaugeMSADue, name="GaugeMSADue"), 
    path("GaugeMSAUnder/", viewsmsastudy.GaugeMSAUnder, name="GaugeMSAUnder"),


    path("GaugeVerifications/", viewsduelist.GaugeVerifications, name="GaugeVerifications"),
    path("GaugeVerificationDue/", viewsduelist.GaugeVerificationDue, name="GaugeVerificationDue"), 
    path("GaugeVerificationUnderProcess/", viewsduelist.GaugeVerificationUnderProcess, name="GaugeVerificationUnderProcess"), 
    path("GaugeVerificationHistory/", viewsduelist.GaugeVerificationHistory, name="GaugeVerificationHistory"), 



    path("GaugeMasterlist/", viewsmasterlist.GaugeMasterlist, name="GaugeMasterlist"), 

    path("GaugePrepone/<int:lID>", viewsissuereturn.GaugePrepone, name="GaugePrepone"),
    path("GaugePostpone/<int:lID>", viewsissuereturn.GaugePostpone, name="GaugePostpone"),
    path("GaugeMissingScrap/<int:lID>", viewsissuereturn.GaugeMissingScrap, name="GaugeMissingScrap"),
    path("GaugeMissingRecover/<int:lID>", viewsissuereturn.GaugeMissingRecover, name="GaugeMissingRecover"),
    path("GaugeServiceRepair/<int:lID>", viewsdamaged.GaugeServiceRepair, name="GaugeMissingRecover"),



    path("GaugeUserList/", views.GaugeUserList, name="GaugeUserList"), 
    path("UserListAdd/", views.UserListAdd, name="UserListAdd"), 
    path("UserListDetails/<int:lID>", views.UserListDetails, name="UserListDetails"), 

    path("AdminUnitList/", viewsMasters.AdminUnitList, name="AdminUnitList"), 
    path("AdminUnitAdd/", viewsMasters.AdminUnitAdd, name="AdminUnitAdd"),  
    path("AdminUnitDetails/<int:lID>", viewsMasters.AdminUnitDetails, name="AdminUnitDetails"), 

    path("AdminAreaofUseList/", viewsMasters.AdminAreaofUseList, name="AdminAreaofUseList"), 
    path("AdminAreaofUseAdd/", viewsMasters.AdminAreaofUseAdd, name="AdminAreaofUseAdd"),  
    path("AdminAreaofUseDetails/<int:lID>", viewsMasters.AdminAreaofUseDetails, name="AdminAreaofUseDetails"), 
    path("AdminUOMList/", viewsMasters.AdminUOMList, name="AdminUOMList"), 
    path("AdminUOMAdd/", viewsMasters.AdminUOMAdd, name="AdminUOMAdd"),  
    path("AdminUOMDetails/<int:lID>", viewsMasters.AdminUOMDetails, name="AdminUOMDetails"), 


    path("AdminAdmintoleranceclasslist/", viewsMasters1.AdminAdmintoleranceclasslist, name="AdminAdmintoleranceclasslist"), 
    path("AdmintoleranceclasslistAdd/", viewsMasters1.AdmintoleranceclasslistAdd, name="AdmintoleranceclasslistAdd"),  
    path("AdmintoleranceclasslistDetails/<int:lID>", viewsMasters1.AdmintoleranceclasslistDetails, name="AdmintoleranceclasslistDetails"), 
    path("adminToleranceISManufacturingStdChartList/", viewsMasters1.adminToleranceISManufacturingStdChartList, name="adminToleranceISManufacturingStdChartList"), 
    path("adminToleranceDialGaugeList/", viewsMasters1.adminToleranceDialGaugeList, name="adminToleranceDialGaugeList"), 
    path("adminTolerancePressureGaugeList/", viewsMasters1.adminTolerancePressureGaugeList, name="adminTolerancePressureGaugeList"), 
    path("adminToleranceRadiusGaugeList/", viewsMasters1.adminToleranceRadiusGaugeList, name="adminToleranceRadiusGaugeList"), 
    path("adminToleranceSettingRingList/", viewsMasters1.adminToleranceSettingRingList, name="adminToleranceSettingRingList"), 
    path("adminToleranceSlipGaugeList/", viewsMasters1.adminToleranceSlipGaugeList, name="adminToleranceSlipGaugeList"), 
    path("adminCalibConditionsList/", viewsMasters1.adminCalibConditionsList, name="adminCalibConditionsList"), 

    path("adminExternalAgencyList/", viewsMasters.adminExternalAgencyList, name="adminExternalAgencyList"), 
    path("adminExternalAgencyListAdd/", viewsMasters.adminExternalAgencyListAdd, name="adminExternalAgencyListAdd"),  
    path("adminExternalAgencyListDetails/<int:lID>", viewsMasters.adminExternalAgencyListDetails, name="adminExternalAgencyListDetails"),

    path("adminOperatorList/", viewsMasters.adminOperatorList, name="adminOperatorList"), 
    path("adminOperatorListAdd/", viewsMasters.adminOperatorListAdd, name="adminOperatorListAdd"),  
    path("adminOperatorListDetails/<int:lID>", viewsMasters.adminOperatorListDetails, name="adminOperatorListDetails"), 

    path("adminSparepartsList/", viewsMasters.adminSparepartsList, name="adminSparepartsList"), 
    path("adminSparepartsListAdd/", viewsMasters.adminSparepartsListAdd, name="adminSparepartsListAdd"),  
    path("adminSparepartsListDetails/<int:lID>", viewsMasters.adminSparepartsListDetails, name="adminSparepartsListDetails"),   
    
    path("adminMakeList/", viewsMasters.adminMakeList, name="adminMakeList"), 
    path("adminMakeListAdd/", viewsMasters.adminMakeListAdd, name="adminMakeListAdd"),  
    path("adminMakeListDetails/<int:lID>", viewsMasters.adminMakeListDetails, name="adminMakeListDetails"), 
    path("adminMakeListDelete/<int:lID>", viewsMasters.adminMakeListDelete, name="adminMakeListDelete"),  
 

    path("adminStorageLocationList/", viewsMasters.adminStorageLocationList, name="adminStorageLocationList"), 
    
    path("adminStorageLocationListAdd/", viewsMasters.adminStorageLocationListAdd, name="adminStorageLocationListAdd"),  
    path("adminStorageLocationListDetails/<int:lID>", viewsMasters.adminStorageLocationListDetails, name="adminStorageLocationListDetails"), 
    
    path("adminStorageLocationListDelete/<int:lID>", viewsMasters.adminStorageLocationListDelete, name="adminStorageLocationListDelete"),  

    path("adminLocationListDelete/<int:lID>", viewsMasters.adminLocationListDelete, name="adminLocationListDelete"),  


    path("adminPartDetailsListList/", viewsMasters.adminPartDetailsListList, name="adminPartDetailsListList"), 
    path("adminPartDetailsListListAdd/", viewsMasters.adminPartDetailsListListAdd, name="adminPartDetailsListListAdd"),  
    path("adminPartDetailsListListDetails/<int:lID>", viewsMasters.adminPartDetailsListListDetails, name="adminPartDetailsListListDetails"), 
 
    path("adminCustomerList/", views.adminCustomerList, name="adminCustomerList"), 
    path("adminCustomerListAdd/", views.adminCustomerListAdd, name="adminCustomerListAdd"),  
    path("adminCustomerListDetails/<int:lID>", views.adminCustomerListDetails, name="adminCustomerListDetails"), 
 

    path("adminInstrumentOperationList/", viewsMasters.adminInstrumentOperationList, name="adminInstrumentOperationList"), 
    path("adminInstrumentOperationListAdd/", viewsMasters.adminInstrumentOperationListAdd, name="adminInstrumentOperationListAdd"),  
    path("adminInstrumentOperationListDetails/<int:lID>", viewsMasters.adminInstrumentOperationListDetails, name="adminInstrumentOperationListDetails"), 
 
    
    path("adminInstrumentMaterialList/", viewsMasters.adminInstrumentMaterialList, name="adminInstrumentMaterialList"), 
    path("adminInstrumentMaterialListAdd/", viewsMasters.adminInstrumentMaterialListAdd, name="adminInstrumentMaterialListAdd"),  
    path("adminInstrumentMaterialListDetails/<int:lID>", viewsMasters.adminInstrumentMaterialListDetails, name="adminInstrumentMaterialListDetails"), 
 
    path("adminAssetTypeList/", viewsMasters.adminAssetTypeList, name="adminAssetTypeList"), 
    path("adminAssetTypeListAdd/", viewsMasters.adminAssetTypeListAdd, name="adminAssetTypeListAdd"),  
    path("adminAssetTypeListDetails/<int:lID>", viewsMasters.adminAssetTypeListDetails, name="adminAssetTypeListDetails"), 
 
    path("adminAssetCategoryList/", viewscategorycreation.adminAssetCategoryList, name="adminAssetCategoryList"), 
    path("adminAssetCategoryListAdd/", viewscategorycreation.adminAssetCategoryListAdd, name="adminAssetCategoryListAdd"),  
    path("adminAssetCategoryListDetails/<int:lID>", viewscategorycreation.adminAssetCategoryListDetails, name="adminAssetCategoryListDetails"),
    path("adminAssetCategoryListAddDelete/<int:lID>", viewscategorycreation.adminAssetCategoryListAddDelete, name="adminAssetCategoryListAddDelete"), 
    path("adminAssetCategoryListDetailsDelete/<int:lID>", viewscategorycreation.adminAssetCategoryListDetailsDelete, name="adminAssetCategoryListDetailsDelete"),  
 


    path("MasterInstrumentsList/", viewsMasters.MasterInstrumentsList, name="MasterInstrumentsList"), 
    path("MasterInstrumentsListAdd/", viewsMasters.MasterInstrumentsListAdd, name="MasterInstrumentsListAdd"),  
    path("MasterInstrumentsListDetails/<int:lID>", viewsMasters.MasterInstrumentsListDetails, name="MasterInstrumentsListDetails"), 
 
    path("AdminInstrumentTypeList/", viewsMasters.AdminInstrumentTypeList, name="AdminInstrumentTypeList"), 
    path("AdminInstrumentTypeListAdd/", viewsMasters.AdminInstrumentTypeListAdd, name="AdminInstrumentTypeListAdd"),  
    path("AdminInstrumentTypeListDetails/<int:lID>", viewsMasters.AdminInstrumentTypeListDetails, name="AdminInstrumentTypeListDetails"), 
 
    path("AdminEquipmentList/", viewsMasters.AdminEquipmentList, name="AdminEquipmentList"), 
    path("AdminEquipmentListAdd/", viewsMasters.AdminEquipmentListAdd, name="AdminEquipmentListAdd"),  
    path("AdminEquipmentListDetails/<int:lID>", viewsMasters.AdminEquipmentListDetails, name="AdminEquipmentListDetails"), 
    path("AdminEquipmentLisDelete/<int:lID>", viewsMasters.AdminEquipmentLisDelete, name="AdminEquipmentLisDelete"), 

    path("AdminRangeList/", viewsMasters.AdminRangeList, name="AdminRangeList"), 
    path("AdminRangeListAdd/", viewsMasters.AdminRangeListAdd, name="AdminRangeListAdd"),  
    path("AdminRangeListDetails/<int:lID>", viewsMasters.AdminRangeListDetails, name="AdminRangeListDetails"),
 
    path("MasterList/", views.MasterList, name="MasterList"), 
    path("DueScheduleList/", views.DueScheduleList, name="DueScheduleList"), 
    path("DueCalendarList/", views.DueCalendarList, name="DueCalendarList"), 
    path("DuePeriodicList/", views.DuePeriodicList, name="DuePeriodicList"), 
    path("MasterList/", views.MasterList, name="MasterList"), 
    path("StartCalibrationList/", views.StartCalibrationList, name="StartCalibrationList"), 
    path("PostponeCalibrationList/", views.PostponeCalibrationList, name="PostponeCalibrationList"), 
    path("PreponeCalibrationList/", views.PreponeCalibrationList, name="PreponeCalibrationList"),  

    path("CalibrationApprovalDetailsGet/<int:lHistoryID>", viewscalibrations.CalibrationApprovalDetailsGet, name="CalibrationApprovalDetailsGet"), 
    path("CalibrationPendingDetailsGet/<int:lHistoryID>", viewscalibrations.CalibrationPendingDetailsGet, name="CalibrationPendingDetailsGet"), 
    
    path("CalibrationPendingDetails/", viewscalibrations.CalibrationPendingDetails, name="CalibrationPendingDetails"), 
    path("CalibrationApprovalDetails/", viewscalibrations.CalibrationApprovalDetails, name="CalibrationApprovalDetails"), 

    path("CalibrationStart/<int:lID>", viewscalibrations.CalibrationStart, name="CalibrationStart"), 

    path("CalibrationApprovalDetails/", views.CalibrationApprovalDetails, name="CalibrationApprovalDetails"), 
    path("CalibrationHistoryDetails/", views.CalibrationHistoryDetails, name="CalibrationHistoryDetails"), 
 


path('GaugeMasterlistDetails/<int:lID>', viewsmasterlist.GaugeMasterlistDetails, name='GaugeMasterlistDetails'),
    

    path('GaugeMasterlistUnderPurchaseDetails/<int:lID>', viewsmasterlist.GaugeMasterlistUnderPurchaseDetails, name='GaugeMasterlistUnderPurchaseDetails'),
    path('DetailsMasterListPurchase/', viewsmasterlist.DetailsMasterListPurchase, name='DetailsMasterListPurchase'),

    path("MasterDetailsList/<int:lID>", viewsamasterListdetails.MasterDetailsList, name="MasterDetailsList"), 
    path("MasterDetailsListAdmin/<int:lID>", viewsamasterListdetails.MasterDetailsListAdmin, name="MasterDetailsListAdmin"), 
    path("MasterDetailsListAllPlant/<int:lID>", viewsamasterListdetails.MasterDetailsListAllPlant, name="MasterDetailsListAllPlant"), 
    path("MasterDetailsListDisabled/<int:lID>", viewsbmasterListdetails.MasterDetailsListDisabled, name="MasterDetailsListDisabled"), 

    path("MasterHistoryDetailsList/<int:lID>", viewsamasterListdetails.MasterHistoryDetailsList, name="MasterHistoryDetailsList"), 
    path("MasterHistoryDetailsListAdmin/<int:lID>", viewsamasterListdetails.MasterHistoryDetailsListAdmin, name="MasterHistoryDetailsListAdmin"), 
    path("MasterHistoryDetailsListAllPlant/<int:lID>", viewsamasterListdetails.MasterHistoryDetailsListAllPlant, name="MasterHistoryDetailsListAllPlant"),
    path("MasterHistoryDetailsListDisabled/<int:lID>", viewsbmasterListdetails.MasterHistoryDetailsListDisabled, name="MasterHistoryDetailsListDisabled"),  

    path("MasterHistoryList/<int:lID>", viewsahistory.MasterHistoryList, name="MasterHistoryList"), 
    path("MasterHistoryListAdmin/<int:lID>", viewsahistory.MasterHistoryListAdmin, name="MasterHistoryListAdmin"), 
    path("MasterHistoryListAllPlant/<int:lID>", viewsahistory.MasterHistoryListAllPlant, name="MasterHistoryListAllPlant"),
    path("MasterHistoryListDisabled/<int:lID>", viewsahistory.MasterHistoryListDisabled, name="MasterHistoryListDisabled"),  
              
    path("MasterListDetails/<int:lID>", viewsamasterListdetails.MasterListDetails, name="MasterListDetails"),  
    path("MasterListDetailsDisabled/<int:lID>", viewsbmasterListdetails.MasterListDetailsDisabled, name="MasterListDetailsDisabled"),  
    path("MasterListCalibrationDetails/<int:lID>", viewsamasterListdetails.MasterListCalibrationDetails, name="MasterListCalibrationDetails"),  
    path("MasterListCalibrationDetailsDisabled/<int:lID>", viewsbmasterListdetails.MasterListCalibrationDetailsDisabled, name="MasterListCalibrationDetailsDisabled"),  


    path("GaugeCalibrationHistory/", viewsduelist.GaugeCalibrationHistory, name="GaugeCalibrationHistory"),


    path("GaugeCalibrationHistoryA/<int:lHistoryID>", viewscalibrations.GaugeCalibrationHistoryA, name="GaugeCalibrationHistoryA"),

    path("GaugeCalibrationPending/<int:lHistoryID>", viewscalibrations.GaugeCalibrationPending, name="GaugeCalibrationPending"),

    path("GaugeStartCalibration/<int:linstrumentid>", viewscalibrations.GaugeStartCalibration, name="GaugeStartCalibration"),

    path("GaugeCalibrationHistoryDetails/<int:lHistoryID>", viewscalibrations.GaugeCalibrationHistoryDetails, name="GaugeCalibrationHistoryDetails"),


    path('AdminuserlistApi',views.AdminuserlistApi, name="AdminuserlistApi"),

    path("GaugeRepairDetails/<int:lID>", viewsdamaged.GaugeRepairDetails, name="GaugeRepairDetails"),
    path("GaugeRepairHistoryDetails/<int:lID>", viewsdamaged.GaugeRepairHistoryDetails, name="GaugeRepairHistoryDetails"),


]