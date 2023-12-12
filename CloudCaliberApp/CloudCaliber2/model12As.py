# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Masterinstrumentattachmentslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stypeoffile = models.CharField(db_column='sTypeofFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfile = models.CharField(db_column='sFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentAttachmentsList'


class Masterinstrumentcalibrationmasterslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lcalibrationmasterid = models.IntegerField(db_column='lCalibrationMasterId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentCalibrationMastersList'


class Masterinstrumentcalibrationsettingslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    sparameter = models.CharField(db_column='sParameter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luomid = models.IntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    dmax = models.FloatField(db_column='dMax', blank=True, null=True)  # Field name made lowercase.
    dmin = models.FloatField(db_column='dMin', blank=True, null=True)  # Field name made lowercase.
    sappliedvalue = models.CharField(db_column='sAppliedValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fappliedvalue = models.FloatField(db_column='fAppliedValue', blank=True, null=True)  # Field name made lowercase.
    derrorallowed = models.FloatField(db_column='dErrorAllowed', blank=True, null=True)  # Field name made lowercase.
    bsubinstruments = models.BooleanField(db_column='bsubInstruments', blank=True, null=True)  # Field name made lowercase.
    ssubdescription = models.CharField(db_column='ssubDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dleastcount = models.FloatField(db_column='dLeastCount', blank=True, null=True)  # Field name made lowercase.
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    stestmeterreading = models.CharField(db_column='sTestMeterReading', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dducreading = models.FloatField(db_column='dDUCReading', blank=True, null=True)  # Field name made lowercase.
    dstd1 = models.FloatField(db_column='dSTD1', blank=True, null=True)  # Field name made lowercase.
    dstd2 = models.FloatField(db_column='dSTD2', blank=True, null=True)  # Field name made lowercase.
    dstd3 = models.FloatField(db_column='dSTD3', blank=True, null=True)  # Field name made lowercase.
    dstd4 = models.FloatField(db_column='dSTD4', blank=True, null=True)  # Field name made lowercase.
    dstd5 = models.FloatField(db_column='dSTD5', blank=True, null=True)  # Field name made lowercase.
    daverage = models.FloatField(db_column='dAverage', blank=True, null=True)  # Field name made lowercase.
    derror = models.FloatField(db_column='dError', blank=True, null=True)  # Field name made lowercase.
    dstd6 = models.FloatField(db_column='dSTD6', blank=True, null=True)  # Field name made lowercase.
    dstd7 = models.FloatField(db_column='dSTD7', blank=True, null=True)  # Field name made lowercase.
    dstd8 = models.FloatField(db_column='dSTD8', blank=True, null=True)  # Field name made lowercase.
    dstd9 = models.FloatField(db_column='dSTD9', blank=True, null=True)  # Field name made lowercase.
    dstd10 = models.FloatField(db_column='dSTD10', blank=True, null=True)  # Field name made lowercase.
    dstd11 = models.FloatField(db_column='dSTD11', blank=True, null=True)  # Field name made lowercase.
    dstd12 = models.FloatField(db_column='dSTD12', blank=True, null=True)  # Field name made lowercase.
    dstd13 = models.FloatField(db_column='dSTD13', blank=True, null=True)  # Field name made lowercase.
    dstd14 = models.FloatField(db_column='dSTD14', blank=True, null=True)  # Field name made lowercase.
    dstd15 = models.FloatField(db_column='dSTD15', blank=True, null=True)  # Field name made lowercase.
    dstd16 = models.FloatField(db_column='dSTD16', blank=True, null=True)  # Field name made lowercase.
    dstd17 = models.FloatField(db_column='dSTD17', blank=True, null=True)  # Field name made lowercase.
    dstd18 = models.FloatField(db_column='dSTD18', blank=True, null=True)  # Field name made lowercase.
    dstd19 = models.FloatField(db_column='dSTD19', blank=True, null=True)  # Field name made lowercase.
    dstd20 = models.FloatField(db_column='dSTD20', blank=True, null=True)  # Field name made lowercase.
    dtoleranceno = models.FloatField(db_column='dToleranceNo', blank=True, null=True)  # Field name made lowercase.
    stolclass = models.CharField(db_column='sTolClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtearp = models.FloatField(db_column='dTearP', blank=True, null=True)  # Field name made lowercase.
    dtearn = models.FloatField(db_column='dTearN', blank=True, null=True)  # Field name made lowercase.
    btoleranceclass = models.BooleanField(db_column='bToleranceClass', blank=True, null=True)  # Field name made lowercase.
    btoleranceisstd = models.BooleanField(db_column='bToleranceISStd', blank=True, null=True)  # Field name made lowercase.
    ltoleranceisstd = models.IntegerField(db_column='lToleranceISStd', blank=True, null=True)  # Field name made lowercase.
    dfromdia = models.FloatField(db_column='dFromDia', blank=True, null=True)  # Field name made lowercase.
    dtodia = models.FloatField(db_column='dToDia', blank=True, null=True)  # Field name made lowercase.
    dtolupto = models.FloatField(db_column='dTolUpto', blank=True, null=True)  # Field name made lowercase.
    dhby2 = models.FloatField(db_column='dHBY2', blank=True, null=True)  # Field name made lowercase.
    dy = models.FloatField(db_column='dY', blank=True, null=True)  # Field name made lowercase.
    dz = models.FloatField(db_column='dZ', blank=True, null=True)  # Field name made lowercase.
    da = models.FloatField(db_column='dA', blank=True, null=True)  # Field name made lowercase.
    dh1by2 = models.FloatField(db_column='dH1BY2', blank=True, null=True)  # Field name made lowercase.
    dy1 = models.FloatField(db_column='dY1', blank=True, null=True)  # Field name made lowercase.
    dz1 = models.FloatField(db_column='dZ1', blank=True, null=True)  # Field name made lowercase.
    da1 = models.FloatField(db_column='dA1', blank=True, null=True)  # Field name made lowercase.
    bmanufacturingstd = models.BooleanField(db_column='bManufacturingStd', blank=True, null=True)  # Field name made lowercase.
    ldegree1 = models.IntegerField(db_column='lDegree1', blank=True, null=True)  # Field name made lowercase.
    lmin1 = models.IntegerField(db_column='lMin1', blank=True, null=True)  # Field name made lowercase.
    lsec1 = models.IntegerField(db_column='lSec1', blank=True, null=True)  # Field name made lowercase.
    ldegree2 = models.IntegerField(db_column='lDegree2', blank=True, null=True)  # Field name made lowercase.
    lmin2 = models.IntegerField(db_column='lMin2', blank=True, null=True)  # Field name made lowercase.
    lsec2 = models.IntegerField(db_column='lSec2', blank=True, null=True)  # Field name made lowercase.
    bimage = models.BooleanField(db_column='bImage', blank=True, null=True)  # Field name made lowercase.
    bdegree = models.BooleanField(db_column='bDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentCalibrationSettingsList'


class Masterinstrumentenvironmentconditionlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scondition1 = models.CharField(db_column='sCondition1', max_length=180, blank=True, null=True)  # Field name made lowercase.
    scondition2 = models.CharField(db_column='sCondition2', max_length=180, blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentEnvironmentConditionList'


class Masterinstrumentpartprojectslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lpartdetailsid = models.IntegerField(db_column='lPartDetailsId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPartProjectsList'


class Masterinstrumentpreventivemaintenancelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    smaintenancetype = models.CharField(db_column='sMaintenanceType', max_length=480, blank=True, null=True)  # Field name made lowercase.
    linterval = models.IntegerField(db_column='lInterval', blank=True, null=True)  # Field name made lowercase.
    sintervalperiod = models.CharField(db_column='sIntervalPeriod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dtlastmaintenance = models.DateTimeField(db_column='dtLastMaintenance', blank=True, null=True)  # Field name made lowercase.
    dtnextmaintenance = models.DateTimeField(db_column='dtNextMaintenance', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.IntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtservicedisplaydate = models.DateTimeField(db_column='dtServiceDisplayDate', blank=True, null=True)  # Field name made lowercase.
    bverification = models.BooleanField(db_column='bVerification', blank=True, null=True)  # Field name made lowercase.
    bpreventivemaintenance = models.BooleanField(db_column='bPreventiveMaintenance', blank=True, null=True)  # Field name made lowercase.
    bconditionbasedmaintenance = models.BooleanField(db_column='bConditionbasedMaintenance', blank=True, null=True)  # Field name made lowercase.
    bsystematicmaintenance = models.BooleanField(db_column='bsystematicMaintenance', blank=True, null=True)  # Field name made lowercase.
    bpredictivemaintenance = models.BooleanField(db_column='bPredictiveMaintenance', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantID', blank=True, null=True)  # Field name made lowercase.
    ssopfile = models.CharField(db_column='sSOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.IntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.IntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.IntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    sagencycalib = models.CharField(db_column='sAgencyCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lvendorid = models.IntegerField(db_column='lVendorID', blank=True, null=True)  # Field name made lowercase.
    dnextdisplay = models.DateTimeField(db_column='dNextDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextalert = models.DateTimeField(db_column='dNextAlert', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPreventiveMaintenanceList'


class Masterinstrumentpurchasechecklist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lpurchasechecklistid = models.IntegerField(db_column='lPurchaseChecklistID', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=480, blank=True, null=True)  # Field name made lowercase.
    sspecification = models.CharField(db_column='sSpecification', max_length=480, blank=True, null=True)  # Field name made lowercase.
    bok = models.BooleanField(db_column='bOK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPurchaseCheckList'


class Masterinstrumentsparepartslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lsparepartdetailsid = models.IntegerField(db_column='lSparePartDetailsId', blank=True, null=True)  # Field name made lowercase.
    bstockreqd = models.BooleanField(db_column='bStockReqd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentSparePartsList'


class Masterinstrumentslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=180, blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=480, blank=True, null=True)  # Field name made lowercase.
    sassettype = models.CharField(db_column='sAssetType', max_length=180, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantID', blank=True, null=True)  # Field name made lowercase.
    splanttype = models.CharField(db_column='sPlantType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    splanttypecode = models.CharField(db_column='sPlantTypeCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategoryid = models.IntegerField(db_column='lCategoryID', blank=True, null=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='CategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lassetid = models.IntegerField(db_column='lAssetID', blank=True, null=True)  # Field name made lowercase.
    btyperef = models.BooleanField(db_column='bTypeRef', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scodea = models.CharField(db_column='sCodeA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    btyperef1 = models.BooleanField(db_column='bTypeRef1', blank=True, null=True)  # Field name made lowercase.
    scategorytype1 = models.CharField(db_column='sCategoryType1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype11 = models.IntegerField(db_column='lCategoryType11', blank=True, null=True)  # Field name made lowercase.
    lcategorytype21 = models.IntegerField(db_column='lCategoryType21', blank=True, null=True)  # Field name made lowercase.
    scode1 = models.CharField(db_column='sCode1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode11 = models.IntegerField(db_column='lCode11', blank=True, null=True)  # Field name made lowercase.
    lcode21 = models.IntegerField(db_column='lCode21', blank=True, null=True)  # Field name made lowercase.
    styperefname1 = models.CharField(db_column='sTypeRefName1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring1 = models.BooleanField(db_column='bTypeRefasString1', blank=True, null=True)  # Field name made lowercase.
    btyperefasint1 = models.BooleanField(db_column='bTypeRefasInt1', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e1 = models.BooleanField(db_column='bTypeRefasRang1e1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa1 = models.BooleanField(db_column='bTypeRefasContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob1 = models.BooleanField(db_column='bTypeRefasContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa1 = models.IntegerField(db_column='lContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob1 = models.IntegerField(db_column='lContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    btyperef2 = models.BooleanField(db_column='bTypeRef2', blank=True, null=True)  # Field name made lowercase.
    scategorytype2 = models.CharField(db_column='sCategoryType2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype12 = models.IntegerField(db_column='lCategoryType12', blank=True, null=True)  # Field name made lowercase.
    lcategorytype22 = models.IntegerField(db_column='lCategoryType22', blank=True, null=True)  # Field name made lowercase.
    scode2 = models.CharField(db_column='sCode2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode12 = models.IntegerField(db_column='lCode12', blank=True, null=True)  # Field name made lowercase.
    lcode22 = models.IntegerField(db_column='lCode22', blank=True, null=True)  # Field name made lowercase.
    styperefname2 = models.CharField(db_column='sTypeRefName2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring2 = models.BooleanField(db_column='bTypeRefasString2', blank=True, null=True)  # Field name made lowercase.
    btyperefasint2 = models.BooleanField(db_column='bTypeRefasInt2', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e2 = models.BooleanField(db_column='bTypeRefasRang1e2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa2 = models.BooleanField(db_column='bTypeRefasContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob2 = models.BooleanField(db_column='bTypeRefasContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa2 = models.IntegerField(db_column='lContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob2 = models.IntegerField(db_column='lContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    btyperef3 = models.BooleanField(db_column='bTypeRef3', blank=True, null=True)  # Field name made lowercase.
    scategorytype3 = models.CharField(db_column='sCategoryType3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype13 = models.IntegerField(db_column='lCategoryType13', blank=True, null=True)  # Field name made lowercase.
    lcategorytype23 = models.IntegerField(db_column='lCategoryType23', blank=True, null=True)  # Field name made lowercase.
    scode3 = models.CharField(db_column='sCode3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode13 = models.IntegerField(db_column='lCode13', blank=True, null=True)  # Field name made lowercase.
    lcode23 = models.IntegerField(db_column='lCode23', blank=True, null=True)  # Field name made lowercase.
    styperefname3 = models.CharField(db_column='sTypeRefName3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring3 = models.BooleanField(db_column='bTypeRefasString3', blank=True, null=True)  # Field name made lowercase.
    btyperefasint3 = models.BooleanField(db_column='bTypeRefasInt3', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e3 = models.BooleanField(db_column='bTypeRefasRang1e3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa3 = models.BooleanField(db_column='bTypeRefasContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob3 = models.BooleanField(db_column='bTypeRefasContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa3 = models.IntegerField(db_column='lContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob3 = models.IntegerField(db_column='lContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    btyperef4 = models.BooleanField(db_column='bTypeRef4', blank=True, null=True)  # Field name made lowercase.
    scategorytype4 = models.CharField(db_column='sCategoryType4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype14 = models.IntegerField(db_column='lCategoryType14', blank=True, null=True)  # Field name made lowercase.
    lcategorytype24 = models.IntegerField(db_column='lCategoryType24', blank=True, null=True)  # Field name made lowercase.
    scode4 = models.CharField(db_column='sCode4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode14 = models.IntegerField(db_column='lCode14', blank=True, null=True)  # Field name made lowercase.
    lcode24 = models.IntegerField(db_column='lCode24', blank=True, null=True)  # Field name made lowercase.
    styperefname4 = models.CharField(db_column='sTypeRefName4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring4 = models.BooleanField(db_column='bTypeRefasString4', blank=True, null=True)  # Field name made lowercase.
    btyperefasint4 = models.BooleanField(db_column='bTypeRefasInt4', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e4 = models.BooleanField(db_column='bTypeRefasRang1e4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa4 = models.BooleanField(db_column='bTypeRefasContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob4 = models.BooleanField(db_column='bTypeRefasContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa4 = models.IntegerField(db_column='lContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob4 = models.IntegerField(db_column='lContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    btyperef5 = models.BooleanField(db_column='bTypeRef5', blank=True, null=True)  # Field name made lowercase.
    scategorytype5 = models.CharField(db_column='sCategoryType5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype15 = models.IntegerField(db_column='lCategoryType15', blank=True, null=True)  # Field name made lowercase.
    lcategorytype25 = models.IntegerField(db_column='lCategoryType25', blank=True, null=True)  # Field name made lowercase.
    scode5 = models.CharField(db_column='sCode5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode15 = models.IntegerField(db_column='lCode15', blank=True, null=True)  # Field name made lowercase.
    lcode25 = models.IntegerField(db_column='lCode25', blank=True, null=True)  # Field name made lowercase.
    styperefname5 = models.CharField(db_column='sTypeRefName5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring5 = models.BooleanField(db_column='bTypeRefasString5', blank=True, null=True)  # Field name made lowercase.
    btyperefasint5 = models.BooleanField(db_column='bTypeRefasInt5', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e5 = models.BooleanField(db_column='bTypeRefasRang1e5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa5 = models.BooleanField(db_column='bTypeRefasContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob5 = models.BooleanField(db_column='bTypeRefasContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa5 = models.IntegerField(db_column='lContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob5 = models.IntegerField(db_column='lContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    btyperef6 = models.BooleanField(db_column='bTypeRef6', blank=True, null=True)  # Field name made lowercase.
    scategorytype6 = models.CharField(db_column='sCategoryType6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype16 = models.IntegerField(db_column='lCategoryType16', blank=True, null=True)  # Field name made lowercase.
    lcategorytype26 = models.IntegerField(db_column='lCategoryType26', blank=True, null=True)  # Field name made lowercase.
    scode6 = models.CharField(db_column='sCode6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode16 = models.IntegerField(db_column='lCode16', blank=True, null=True)  # Field name made lowercase.
    lcode26 = models.IntegerField(db_column='lCode26', blank=True, null=True)  # Field name made lowercase.
    styperefname6 = models.CharField(db_column='sTypeRefName6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring6 = models.BooleanField(db_column='bTypeRefasString6', blank=True, null=True)  # Field name made lowercase.
    btyperefasint6 = models.BooleanField(db_column='bTypeRefasInt6', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e6 = models.BooleanField(db_column='bTypeRefasRang1e6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa6 = models.BooleanField(db_column='bTypeRefasContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob6 = models.BooleanField(db_column='bTypeRefasContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa6 = models.IntegerField(db_column='lContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob6 = models.IntegerField(db_column='lContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    btyperef7 = models.BooleanField(db_column='bTypeRef7', blank=True, null=True)  # Field name made lowercase.
    scategorytype7 = models.CharField(db_column='sCategoryType7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype17 = models.IntegerField(db_column='lCategoryType17', blank=True, null=True)  # Field name made lowercase.
    lcategorytype27 = models.IntegerField(db_column='lCategoryType27', blank=True, null=True)  # Field name made lowercase.
    scode7 = models.CharField(db_column='sCode7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode17 = models.IntegerField(db_column='lCode17', blank=True, null=True)  # Field name made lowercase.
    lcode27 = models.IntegerField(db_column='lCode27', blank=True, null=True)  # Field name made lowercase.
    styperefname7 = models.CharField(db_column='sTypeRefName7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring7 = models.BooleanField(db_column='bTypeRefasString7', blank=True, null=True)  # Field name made lowercase.
    btyperefasint7 = models.BooleanField(db_column='bTypeRefasInt7', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e7 = models.BooleanField(db_column='bTypeRefasRang1e7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa7 = models.BooleanField(db_column='bTypeRefasContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob7 = models.BooleanField(db_column='bTypeRefasContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa7 = models.IntegerField(db_column='lContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob7 = models.IntegerField(db_column='lContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    btyperef8 = models.BooleanField(db_column='bTypeRef8', blank=True, null=True)  # Field name made lowercase.
    scategorytype8 = models.CharField(db_column='sCategoryType8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype18 = models.IntegerField(db_column='lCategoryType18', blank=True, null=True)  # Field name made lowercase.
    lcategorytype28 = models.IntegerField(db_column='lCategoryType28', blank=True, null=True)  # Field name made lowercase.
    scode8 = models.CharField(db_column='sCode8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode18 = models.IntegerField(db_column='lCode18', blank=True, null=True)  # Field name made lowercase.
    lcode28 = models.IntegerField(db_column='lCode28', blank=True, null=True)  # Field name made lowercase.
    styperefname8 = models.CharField(db_column='sTypeRefName8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring8 = models.BooleanField(db_column='bTypeRefasString8', blank=True, null=True)  # Field name made lowercase.
    btyperefasint8 = models.BooleanField(db_column='bTypeRefasInt8', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e8 = models.BooleanField(db_column='bTypeRefasRang1e8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa8 = models.BooleanField(db_column='bTypeRefasContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob8 = models.BooleanField(db_column='bTypeRefasContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa8 = models.IntegerField(db_column='lContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob8 = models.IntegerField(db_column='lContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    btyperef9 = models.BooleanField(db_column='bTypeRef9', blank=True, null=True)  # Field name made lowercase.
    scategorytype9 = models.CharField(db_column='sCategoryType9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype19 = models.IntegerField(db_column='lCategoryType19', blank=True, null=True)  # Field name made lowercase.
    lcategorytype29 = models.IntegerField(db_column='lCategoryType29', blank=True, null=True)  # Field name made lowercase.
    scode9 = models.CharField(db_column='sCode9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode19 = models.IntegerField(db_column='lCode19', blank=True, null=True)  # Field name made lowercase.
    lcode29 = models.IntegerField(db_column='lCode29', blank=True, null=True)  # Field name made lowercase.
    styperefname9 = models.CharField(db_column='sTypeRefName9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring9 = models.BooleanField(db_column='bTypeRefasString9', blank=True, null=True)  # Field name made lowercase.
    btyperefasint9 = models.BooleanField(db_column='bTypeRefasInt9', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e9 = models.BooleanField(db_column='bTypeRefasRang1e9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa9 = models.BooleanField(db_column='bTypeRefasContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob9 = models.BooleanField(db_column='bTypeRefasContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa9 = models.IntegerField(db_column='lContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob9 = models.IntegerField(db_column='lContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    btyperef10 = models.BooleanField(db_column='bTypeRef10', blank=True, null=True)  # Field name made lowercase.
    scategorytype10 = models.CharField(db_column='sCategoryType10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype110 = models.IntegerField(db_column='lCategoryType110', blank=True, null=True)  # Field name made lowercase.
    lcategorytype210 = models.IntegerField(db_column='lCategoryType210', blank=True, null=True)  # Field name made lowercase.
    scode10 = models.CharField(db_column='sCode10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode110 = models.IntegerField(db_column='lCode110', blank=True, null=True)  # Field name made lowercase.
    lcode210 = models.IntegerField(db_column='lCode210', blank=True, null=True)  # Field name made lowercase.
    styperefname10 = models.CharField(db_column='sTypeRefName10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring10 = models.BooleanField(db_column='bTypeRefasString10', blank=True, null=True)  # Field name made lowercase.
    btyperefasint10 = models.BooleanField(db_column='bTypeRefasInt10', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e10 = models.BooleanField(db_column='bTypeRefasRang1e10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa10 = models.BooleanField(db_column='bTypeRefasContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob10 = models.BooleanField(db_column='bTypeRefasContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa10 = models.IntegerField(db_column='lContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob10 = models.IntegerField(db_column='lContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    btyperef11 = models.BooleanField(db_column='bTypeRef11', blank=True, null=True)  # Field name made lowercase.
    scategorytype11 = models.CharField(db_column='sCategoryType11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype111 = models.IntegerField(db_column='lCategoryType111', blank=True, null=True)  # Field name made lowercase.
    lcategorytype211 = models.IntegerField(db_column='lCategoryType211', blank=True, null=True)  # Field name made lowercase.
    scode11 = models.CharField(db_column='sCode11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode111 = models.IntegerField(db_column='lCode111', blank=True, null=True)  # Field name made lowercase.
    lcode211 = models.IntegerField(db_column='lCode211', blank=True, null=True)  # Field name made lowercase.
    styperefname11 = models.CharField(db_column='sTypeRefName11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring11 = models.BooleanField(db_column='bTypeRefasString11', blank=True, null=True)  # Field name made lowercase.
    btyperefasint11 = models.BooleanField(db_column='bTypeRefasInt11', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e11 = models.BooleanField(db_column='bTypeRefasRang1e11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa11 = models.BooleanField(db_column='bTypeRefasContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob11 = models.BooleanField(db_column='bTypeRefasContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa11 = models.IntegerField(db_column='lContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob11 = models.IntegerField(db_column='lContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    btyperef12 = models.BooleanField(db_column='bTypeRef12', blank=True, null=True)  # Field name made lowercase.
    scategorytype12 = models.CharField(db_column='sCategoryType12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype112 = models.IntegerField(db_column='lCategoryType112', blank=True, null=True)  # Field name made lowercase.
    lcategorytype212 = models.IntegerField(db_column='lCategoryType212', blank=True, null=True)  # Field name made lowercase.
    scode12 = models.CharField(db_column='sCode12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode112 = models.IntegerField(db_column='lCode112', blank=True, null=True)  # Field name made lowercase.
    lcode212 = models.IntegerField(db_column='lCode212', blank=True, null=True)  # Field name made lowercase.
    styperefname12 = models.CharField(db_column='sTypeRefName12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring12 = models.BooleanField(db_column='bTypeRefasString12', blank=True, null=True)  # Field name made lowercase.
    btyperefasint12 = models.BooleanField(db_column='bTypeRefasInt12', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e12 = models.BooleanField(db_column='bTypeRefasRang1e12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa12 = models.BooleanField(db_column='bTypeRefasContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob12 = models.BooleanField(db_column='bTypeRefasContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa12 = models.IntegerField(db_column='lContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob12 = models.IntegerField(db_column='lContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    btyperef13 = models.BooleanField(db_column='bTypeRef13', blank=True, null=True)  # Field name made lowercase.
    scategorytype13 = models.CharField(db_column='sCategoryType13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype113 = models.IntegerField(db_column='lCategoryType113', blank=True, null=True)  # Field name made lowercase.
    lcategorytype213 = models.IntegerField(db_column='lCategoryType213', blank=True, null=True)  # Field name made lowercase.
    scode13 = models.CharField(db_column='sCode13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode113 = models.IntegerField(db_column='lCode113', blank=True, null=True)  # Field name made lowercase.
    lcode213 = models.IntegerField(db_column='lCode213', blank=True, null=True)  # Field name made lowercase.
    styperefname13 = models.CharField(db_column='sTypeRefName13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring13 = models.BooleanField(db_column='bTypeRefasString13', blank=True, null=True)  # Field name made lowercase.
    btyperefasint13 = models.BooleanField(db_column='bTypeRefasInt13', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e13 = models.BooleanField(db_column='bTypeRefasRang1e13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa13 = models.BooleanField(db_column='bTypeRefasContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob13 = models.BooleanField(db_column='bTypeRefasContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa13 = models.IntegerField(db_column='lContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob13 = models.IntegerField(db_column='lContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    btyperef14 = models.BooleanField(db_column='bTypeRef14', blank=True, null=True)  # Field name made lowercase.
    scategorytype14 = models.CharField(db_column='sCategoryType14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype114 = models.IntegerField(db_column='lCategoryType114', blank=True, null=True)  # Field name made lowercase.
    lcategorytype214 = models.IntegerField(db_column='lCategoryType214', blank=True, null=True)  # Field name made lowercase.
    scode14 = models.CharField(db_column='sCode14', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode114 = models.IntegerField(db_column='lCode114', blank=True, null=True)  # Field name made lowercase.
    lcode214 = models.IntegerField(db_column='lCode214', blank=True, null=True)  # Field name made lowercase.
    styperefname14 = models.CharField(db_column='sTypeRefName14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring14 = models.BooleanField(db_column='bTypeRefasString14', blank=True, null=True)  # Field name made lowercase.
    btyperefasint14 = models.BooleanField(db_column='bTypeRefasInt14', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e14 = models.BooleanField(db_column='bTypeRefasRang1e14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa14 = models.BooleanField(db_column='bTypeRefasContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob14 = models.BooleanField(db_column='bTypeRefasContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa14 = models.IntegerField(db_column='lContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob14 = models.IntegerField(db_column='lContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    btyperef15 = models.BooleanField(db_column='bTypeRef15', blank=True, null=True)  # Field name made lowercase.
    scategorytype15 = models.CharField(db_column='sCategoryType15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype115 = models.IntegerField(db_column='lCategoryType115', blank=True, null=True)  # Field name made lowercase.
    lcategorytype215 = models.IntegerField(db_column='lCategoryType215', blank=True, null=True)  # Field name made lowercase.
    scode15 = models.CharField(db_column='sCode15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode115 = models.IntegerField(db_column='lCode115', blank=True, null=True)  # Field name made lowercase.
    lcode215 = models.IntegerField(db_column='lCode215', blank=True, null=True)  # Field name made lowercase.
    styperefname15 = models.CharField(db_column='sTypeRefName15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring15 = models.BooleanField(db_column='bTypeRefasString15', blank=True, null=True)  # Field name made lowercase.
    btyperefasint15 = models.BooleanField(db_column='bTypeRefasInt15', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e15 = models.BooleanField(db_column='bTypeRefasRang1e15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa15 = models.BooleanField(db_column='bTypeRefasContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob15 = models.BooleanField(db_column='bTypeRefasContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa15 = models.IntegerField(db_column='lContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob15 = models.IntegerField(db_column='lContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    btyperef16 = models.BooleanField(db_column='bTypeRef16', blank=True, null=True)  # Field name made lowercase.
    scategorytype16 = models.CharField(db_column='sCategoryType16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype116 = models.IntegerField(db_column='lCategoryType116', blank=True, null=True)  # Field name made lowercase.
    lcategorytype216 = models.IntegerField(db_column='lCategoryType216', blank=True, null=True)  # Field name made lowercase.
    scode16 = models.CharField(db_column='sCode16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode116 = models.IntegerField(db_column='lCode116', blank=True, null=True)  # Field name made lowercase.
    lcode216 = models.IntegerField(db_column='lCode216', blank=True, null=True)  # Field name made lowercase.
    styperefname16 = models.CharField(db_column='sTypeRefName16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring16 = models.BooleanField(db_column='bTypeRefasString16', blank=True, null=True)  # Field name made lowercase.
    btyperefasint16 = models.BooleanField(db_column='bTypeRefasInt16', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e16 = models.BooleanField(db_column='bTypeRefasRang1e16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa16 = models.BooleanField(db_column='bTypeRefasContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob16 = models.BooleanField(db_column='bTypeRefasContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa16 = models.IntegerField(db_column='lContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob16 = models.IntegerField(db_column='lContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    btyperef17 = models.BooleanField(db_column='bTypeRef17', blank=True, null=True)  # Field name made lowercase.
    scategorytype17 = models.CharField(db_column='sCategoryType17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype117 = models.IntegerField(db_column='lCategoryType117', blank=True, null=True)  # Field name made lowercase.
    lcategorytype217 = models.IntegerField(db_column='lCategoryType217', blank=True, null=True)  # Field name made lowercase.
    scode17 = models.CharField(db_column='sCode17', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode117 = models.IntegerField(db_column='lCode117', blank=True, null=True)  # Field name made lowercase.
    lcode217 = models.IntegerField(db_column='lCode217', blank=True, null=True)  # Field name made lowercase.
    styperefname17 = models.CharField(db_column='sTypeRefName17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring17 = models.BooleanField(db_column='bTypeRefasString17', blank=True, null=True)  # Field name made lowercase.
    btyperefasint17 = models.BooleanField(db_column='bTypeRefasInt17', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e17 = models.BooleanField(db_column='bTypeRefasRang1e17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa17 = models.BooleanField(db_column='bTypeRefasContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob17 = models.BooleanField(db_column='bTypeRefasContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa17 = models.IntegerField(db_column='lContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob17 = models.IntegerField(db_column='lContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    btyperef18 = models.BooleanField(db_column='bTypeRef18', blank=True, null=True)  # Field name made lowercase.
    scategorytype18 = models.CharField(db_column='sCategoryType18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype118 = models.IntegerField(db_column='lCategoryType118', blank=True, null=True)  # Field name made lowercase.
    lcategorytype218 = models.IntegerField(db_column='lCategoryType218', blank=True, null=True)  # Field name made lowercase.
    scode18 = models.CharField(db_column='sCode18', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode118 = models.IntegerField(db_column='lCode118', blank=True, null=True)  # Field name made lowercase.
    lcode218 = models.IntegerField(db_column='lCode218', blank=True, null=True)  # Field name made lowercase.
    styperefname18 = models.CharField(db_column='sTypeRefName18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring18 = models.BooleanField(db_column='bTypeRefasString18', blank=True, null=True)  # Field name made lowercase.
    btyperefasint18 = models.BooleanField(db_column='bTypeRefasInt18', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e18 = models.BooleanField(db_column='bTypeRefasRang1e18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa18 = models.BooleanField(db_column='bTypeRefasContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob18 = models.BooleanField(db_column='bTypeRefasContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa18 = models.IntegerField(db_column='lContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob18 = models.IntegerField(db_column='lContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    btyperef19 = models.BooleanField(db_column='bTypeRef19', blank=True, null=True)  # Field name made lowercase.
    scategorytype19 = models.CharField(db_column='sCategoryType19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype119 = models.IntegerField(db_column='lCategoryType119', blank=True, null=True)  # Field name made lowercase.
    lcategorytype219 = models.IntegerField(db_column='lCategoryType219', blank=True, null=True)  # Field name made lowercase.
    scode19 = models.CharField(db_column='sCode19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode119 = models.IntegerField(db_column='lCode119', blank=True, null=True)  # Field name made lowercase.
    lcode219 = models.IntegerField(db_column='lCode219', blank=True, null=True)  # Field name made lowercase.
    styperefname19 = models.CharField(db_column='sTypeRefName19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring19 = models.BooleanField(db_column='bTypeRefasString19', blank=True, null=True)  # Field name made lowercase.
    btyperefasint19 = models.BooleanField(db_column='bTypeRefasInt19', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e19 = models.BooleanField(db_column='bTypeRefasRang1e19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa19 = models.BooleanField(db_column='bTypeRefasContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob19 = models.BooleanField(db_column='bTypeRefasContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa19 = models.IntegerField(db_column='lContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob19 = models.IntegerField(db_column='lContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    btyperef20 = models.BooleanField(db_column='bTypeRef20', blank=True, null=True)  # Field name made lowercase.
    scategorytype20 = models.CharField(db_column='sCategoryType20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype120 = models.IntegerField(db_column='lCategoryType120', blank=True, null=True)  # Field name made lowercase.
    lcategorytype220 = models.IntegerField(db_column='lCategoryType220', blank=True, null=True)  # Field name made lowercase.
    scode20 = models.CharField(db_column='sCode20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode120 = models.IntegerField(db_column='lCode120', blank=True, null=True)  # Field name made lowercase.
    lcode220 = models.IntegerField(db_column='lCode220', blank=True, null=True)  # Field name made lowercase.
    styperefname20 = models.CharField(db_column='sTypeRefName20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring20 = models.BooleanField(db_column='bTypeRefasString20', blank=True, null=True)  # Field name made lowercase.
    btyperefasint20 = models.BooleanField(db_column='bTypeRefasInt20', blank=True, null=True)  # Field name made lowercase.
    btyperefasrang1e20 = models.BooleanField(db_column='bTypeRefasRang1e20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa20 = models.BooleanField(db_column='bTypeRefasContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob20 = models.BooleanField(db_column='bTypeRefasContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa20 = models.IntegerField(db_column='lContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob20 = models.IntegerField(db_column='lContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
    ssize = models.CharField(db_column='sSize', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smake = models.CharField(db_column='sMake', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcurrentlocationid = models.IntegerField(db_column='lCurrentLocationId', blank=True, null=True)  # Field name made lowercase.
    ldefaultlocationid = models.IntegerField(db_column='lDefaultLocationId', blank=True, null=True)  # Field name made lowercase.
    sstoragerack = models.CharField(db_column='sStorageRack', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingno = models.CharField(db_column='sDrawingNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingrevno = models.CharField(db_column='sDrawingRevNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingfile = models.CharField(db_column='sDrawingFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sunitofmeasure = models.CharField(db_column='sUnitofMeasure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    srevisionno = models.CharField(db_column='sRevisionNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sproperty = models.CharField(db_column='sProperty', max_length=1, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentstatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ssstatus = models.CharField(db_column='sSstatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scatalogueno = models.CharField(db_column='sCatalogueNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    frangefrom = models.FloatField(db_column='fRangeFrom', blank=True, null=True)  # Field name made lowercase.
    frangeto = models.FloatField(db_column='fRangeTo', blank=True, null=True)  # Field name made lowercase.
    fleastcount = models.FloatField(db_column='fLeastCount', blank=True, null=True)  # Field name made lowercase.
    scheckmethod = models.CharField(db_column='sCheckMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bcalib = models.BooleanField(db_column='bCalib', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lintervalcalib = models.IntegerField(db_column='lIntervalCalib', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodcalib = models.CharField(db_column='sIntervalPeriodCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lintervalservice = models.IntegerField(db_column='lIntervalService', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodservice = models.CharField(db_column='sIntervalPeriodService', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.IntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smanualduecalib = models.CharField(db_column='sManualDueCalib', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ldayremaincalib = models.IntegerField(db_column='lDayRemainCalib', blank=True, null=True)  # Field name made lowercase.
    dtlastcalib = models.DateTimeField(db_column='dtLastCalib', blank=True, null=True)  # Field name made lowercase.
    dtnextcalib = models.DateTimeField(db_column='dtNextCalib', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.IntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtcalibdisplaydate = models.DateTimeField(db_column='dtCalibDisplayDate', blank=True, null=True)  # Field name made lowercase.
    ldueday = models.IntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.IntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.IntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    busagewise = models.BooleanField(db_column='bUsageWise', blank=True, null=True)  # Field name made lowercase.
    lusageinterval = models.IntegerField(db_column='lUsageInterval', blank=True, null=True)  # Field name made lowercase.
    lusageintervaldisplay = models.IntegerField(db_column='lUsageIntervalDisplay', blank=True, null=True)  # Field name made lowercase.
    lusagecurrent = models.IntegerField(db_column='lUsageCurrent', blank=True, null=True)  # Field name made lowercase.
    dlastservice = models.DateTimeField(db_column='dLastService', blank=True, null=True)  # Field name made lowercase.
    dnextservice = models.DateTimeField(db_column='dNextService', blank=True, null=True)  # Field name made lowercase.
    smanualduernr = models.CharField(db_column='sManualDueRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ldayremainrnr = models.IntegerField(db_column='lDayRemainRnR', blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frange3 = models.FloatField(db_column='fRange3', blank=True, null=True)  # Field name made lowercase.
    lpurchasevendorid = models.IntegerField(db_column='lPurchaseVendorId', blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.IntegerField(db_column='lServiceVendorId', blank=True, null=True)  # Field name made lowercase.
    lcalibrationvendorid = models.IntegerField(db_column='lCalibrationVendorID', blank=True, null=True)  # Field name made lowercase.
    sagencycalib = models.CharField(db_column='sAgencyCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smanufacturer = models.CharField(db_column='sManufacturer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddateofprocure = models.DateTimeField(db_column='dDateofProcure', blank=True, null=True)  # Field name made lowercase.
    smodelno = models.CharField(db_column='sModelNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sserialno = models.CharField(db_column='sSerialNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcalibrationcost = models.FloatField(db_column='dCalibrationCost', blank=True, null=True)  # Field name made lowercase.
    dpurchaseprice = models.FloatField(db_column='dPurchasePrice', blank=True, null=True)  # Field name made lowercase.
    saccuracy = models.CharField(db_column='sAccuracy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bcheckin = models.BooleanField(db_column='bCheckin', blank=True, null=True)  # Field name made lowercase.
    ssize1 = models.CharField(db_column='sSize1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    llusagedefault = models.IntegerField(db_column='llUsageDefault', blank=True, null=True)  # Field name made lowercase.
    llusagecount = models.IntegerField(db_column='llUsageCount', blank=True, null=True)  # Field name made lowercase.
    soperation = models.CharField(db_column='sOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bcustomer = models.BooleanField(db_column='bCustomer', blank=True, null=True)  # Field name made lowercase.
    busage = models.BooleanField(db_column='bUsage', blank=True, null=True)  # Field name made lowercase.
    lcalibalert = models.IntegerField(db_column='lCalibAlert', blank=True, null=True)  # Field name made lowercase.
    lservicealert = models.IntegerField(db_column='lServiceAlert', blank=True, null=True)  # Field name made lowercase.
    lrnralert = models.IntegerField(db_column='lRnRAlert', blank=True, null=True)  # Field name made lowercase.
    blimitedusage = models.BooleanField(db_column='bLimitedUsage', blank=True, null=True)  # Field name made lowercase.
    bdamaged = models.BooleanField(db_column='bDamaged', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    smounted = models.CharField(db_column='sMounted', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fproducttolerance = models.FloatField(db_column='fProductTolerance', blank=True, null=True)  # Field name made lowercase.
    sproducttolerance = models.CharField(db_column='sProductTolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facconstant = models.FloatField(db_column='fACConstant', blank=True, null=True)  # Field name made lowercase.
    lintervalserv3 = models.IntegerField(db_column='lIntervalServ3', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodserv3 = models.CharField(db_column='sIntervalPeriodServ3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smanualdueserv3 = models.CharField(db_column='sManualDueServ3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ldayremainserv3 = models.IntegerField(db_column='lDayRemainServ3', blank=True, null=True)  # Field name made lowercase.
    dlastserv3 = models.DateTimeField(db_column='dLastServ3', blank=True, null=True)  # Field name made lowercase.
    dnextserv3 = models.DateTimeField(db_column='dNextServ3', blank=True, null=True)  # Field name made lowercase.
    lserv3alert = models.IntegerField(db_column='lServ3Alert', blank=True, null=True)  # Field name made lowercase.
    bserv3 = models.BooleanField(db_column='bServ3', blank=True, null=True)  # Field name made lowercase.
    sagencyservice = models.CharField(db_column='sAgencyService', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtype = models.CharField(db_column='sFreqType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bpressuregauge = models.BooleanField(db_column='bPressureGauge', blank=True, null=True)  # Field name made lowercase.
    btimer = models.BooleanField(db_column='bTimer', blank=True, null=True)  # Field name made lowercase.
    bpowersupply = models.BooleanField(db_column='bPowerSupply', blank=True, null=True)  # Field name made lowercase.
    bgeneral = models.BooleanField(db_column='bGeneral', blank=True, null=True)  # Field name made lowercase.
    bvernier = models.BooleanField(db_column='bVernier', blank=True, null=True)  # Field name made lowercase.
    bboregaugewithdial = models.BooleanField(db_column='bBoreGaugewithDial', blank=True, null=True)  # Field name made lowercase.
    bboregauge = models.BooleanField(db_column='bBoreGauge', blank=True, null=True)  # Field name made lowercase.
    bdialindicator = models.BooleanField(db_column='bDialIndicator', blank=True, null=True)  # Field name made lowercase.
    bheightgauge = models.BooleanField(db_column='bHeightGauge', blank=True, null=True)  # Field name made lowercase.
    bmicrometer = models.BooleanField(db_column='bMicrometer', blank=True, null=True)  # Field name made lowercase.
    ferrorallowed = models.FloatField(db_column='fErrorAllowed', blank=True, null=True)  # Field name made lowercase.
    splanned = models.CharField(db_column='sPlanned', max_length=255, blank=True, null=True)  # Field name made lowercase.
    splanneddate = models.CharField(db_column='sPlannedDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sprocuredate = models.CharField(db_column='sProcureDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brejected = models.BooleanField(db_column='bRejected', blank=True, null=True)  # Field name made lowercase.
    srejecteddate = models.CharField(db_column='sRejectedDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    breplaced = models.BooleanField(db_column='bReplaced', blank=True, null=True)  # Field name made lowercase.
    lreplacedinstrumentid = models.IntegerField(db_column='lReplacedInstrumentId', blank=True, null=True)  # Field name made lowercase.
    bfreezecalib = models.BooleanField(db_column='bFreezeCalib', blank=True, null=True)  # Field name made lowercase.
    b1 = models.BooleanField(blank=True, null=True)
    b2 = models.BooleanField(blank=True, null=True)
    b3 = models.BooleanField(blank=True, null=True)
    b4 = models.BooleanField(blank=True, null=True)
    b5 = models.BooleanField(blank=True, null=True)
    b6 = models.BooleanField(blank=True, null=True)
    b7 = models.BooleanField(blank=True, null=True)
    b8 = models.BooleanField(blank=True, null=True)
    b9 = models.BooleanField(blank=True, null=True)
    b10 = models.BooleanField(blank=True, null=True)
    brnra = models.BooleanField(db_column='bRnRA', blank=True, null=True)  # Field name made lowercase.
    lrnr = models.IntegerField(db_column='lRnR', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lattribute = models.IntegerField(db_column='lAttribute', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lstability = models.IntegerField(db_column='lStability', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lbias = models.IntegerField(db_column='lBias', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    llinearity = models.IntegerField(db_column='lLinearity', blank=True, null=True)  # Field name made lowercase.
    bduechanged = models.BooleanField(db_column='bDueChanged', blank=True, null=True)  # Field name made lowercase.
    dtduechangdate = models.DateTimeField(db_column='dtDueChangDate', blank=True, null=True)  # Field name made lowercase.
    serpcode = models.CharField(db_column='sERPCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lanova = models.IntegerField(db_column='lAnova', blank=True, null=True)  # Field name made lowercase.
    blanova = models.BooleanField(db_column='blAnova', blank=True, null=True)  # Field name made lowercase.
    srevno = models.CharField(db_column='sRevNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scommentchangecalibstd = models.TextField(db_column='sCommentChangeCalibStd', blank=True, null=True)  # Field name made lowercase.
    dtvalidationdate = models.DateTimeField(db_column='dtValidationDate', blank=True, null=True)  # Field name made lowercase.
    bvalidation = models.BooleanField(db_column='bValidation', blank=True, null=True)  # Field name made lowercase.
    bverifyforpurchase = models.BooleanField(db_column='bVerifyForPurchase', blank=True, null=True)  # Field name made lowercase.
    dtsendforverificationforpurchaseon = models.DateTimeField(db_column='dtSendForVerificationForPurchaseOn', blank=True, null=True)  # Field name made lowercase.
    bverifiedforpurchase = models.BooleanField(db_column='bVerifiedForPurchase', blank=True, null=True)  # Field name made lowercase.
    dtverifiedforpurchaseon = models.DateTimeField(db_column='dtVerifiedForPurchaseOn', blank=True, null=True)  # Field name made lowercase.
    brejectedforpurchase = models.BooleanField(db_column='bRejectedForPurchase', blank=True, null=True)  # Field name made lowercase.
    dtrejectedforpurchaseon = models.DateTimeField(db_column='dtRejectedForPurchaseOn', blank=True, null=True)  # Field name made lowercase.
    scommentrejectedforpurchase = models.TextField(db_column='sCommentRejectedForPurchase', blank=True, null=True)  # Field name made lowercase.
    splannedby = models.CharField(db_column='sPlannedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    splancheckedby = models.CharField(db_column='sPlanCheckedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    svalidationby = models.CharField(db_column='sValidationBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bsentforcalibration = models.BooleanField(db_column='bSentForCalibration', blank=True, null=True)  # Field name made lowercase.
    oldinstrument_id = models.CharField(db_column='OLDInstrument_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schangeoldid = models.TextField(db_column='sChangeOLDID', blank=True, null=True)  # Field name made lowercase.
    bidchanged = models.BooleanField(db_column='bIDChanged', blank=True, null=True)  # Field name made lowercase.
    sfreqtyperange = models.CharField(db_column='sFreqTypeRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtypeanova = models.CharField(db_column='sFreqTypeAnova', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtypeattribute = models.CharField(db_column='sFreqTypeAttribute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtypebias = models.CharField(db_column='sFreqTypeBias', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtypestability = models.CharField(db_column='sFreqTypeStability', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfreqtypelinearity = models.CharField(db_column='sFreqTypeLinearity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    banova = models.BooleanField(db_column='bAnova', blank=True, null=True)  # Field name made lowercase.
    lintervalstability = models.IntegerField(db_column='lIntervalStability', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodstability = models.CharField(db_column='sIntervalPeriodStability', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lalertstability = models.IntegerField(db_column='lAlertStability', blank=True, null=True)  # Field name made lowercase.
    dlaststability = models.DateTimeField(db_column='dLastStability', blank=True, null=True)  # Field name made lowercase.
    dnextstability = models.DateTimeField(db_column='dNextStability', blank=True, null=True)  # Field name made lowercase.
    lintervalbias = models.IntegerField(db_column='lIntervalBias', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodbias = models.CharField(db_column='sIntervalPeriodBias', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lalertbias = models.IntegerField(db_column='lAlertBias', blank=True, null=True)  # Field name made lowercase.
    dlastbias = models.DateTimeField(db_column='dLastBias', blank=True, null=True)  # Field name made lowercase.
    dnextbias = models.DateTimeField(db_column='dNextBias', blank=True, null=True)  # Field name made lowercase.
    lintervallinearity = models.IntegerField(db_column='lIntervalLinearity', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodlinearity = models.CharField(db_column='sIntervalPeriodLinearity', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lalertlinearity = models.IntegerField(db_column='lAlertLinearity', blank=True, null=True)  # Field name made lowercase.
    dlastlinearity = models.DateTimeField(db_column='dLastLinearity', blank=True, null=True)  # Field name made lowercase.
    dnextlinearity = models.DateTimeField(db_column='dNextLinearity', blank=True, null=True)  # Field name made lowercase.
    llusagecountalerts = models.IntegerField(db_column='llUsageCountAlerts', blank=True, null=True)  # Field name made lowercase.
    scommentchangepm = models.TextField(db_column='sCommentChangePM', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spreferredvendor = models.CharField(db_column='sPreferredVendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bpurchaseclosed = models.BooleanField(db_column='bPurchaseClosed', blank=True, null=True)  # Field name made lowercase.
    bbonded = models.BooleanField(db_column='bBonded', blank=True, null=True)  # Field name made lowercase.
    sbondnumber = models.CharField(db_column='sBondNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lhistorycard = models.IntegerField(db_column='lHistoryCard', blank=True, null=True)  # Field name made lowercase.
    bidlecalibration = models.BooleanField(db_column='bIdleCalibration', blank=True, null=True)  # Field name made lowercase.
    lidlecalibfrequency = models.IntegerField(db_column='lIdleCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    sidlecalibfreq = models.CharField(db_column='sIdleCalibFreq', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bnextidlecalibration = models.DateTimeField(db_column='bNextIdleCalibration', blank=True, null=True)  # Field name made lowercase.
    didleon = models.DateTimeField(db_column='dIdleOn', blank=True, null=True)  # Field name made lowercase.
    b1monthvalidation = models.BooleanField(db_column='b1MonthValidation', blank=True, null=True)  # Field name made lowercase.
    bnextvalidation = models.DateTimeField(db_column='bNextValidation', blank=True, null=True)  # Field name made lowercase.
    dlastvalidation = models.DateTimeField(db_column='dlastValidation', blank=True, null=True)  # Field name made lowercase.
    bsamplepartusage = models.BooleanField(db_column='bSamplePartusage', blank=True, null=True)  # Field name made lowercase.
    bregularpartusage = models.BooleanField(db_column='bRegularPartUsage', blank=True, null=True)  # Field name made lowercase.
    bcalibstandards = models.BooleanField(db_column='bCalibStandards', blank=True, null=True)  # Field name made lowercase.
    dgo = models.FloatField(db_column='dGO', blank=True, null=True)  # Field name made lowercase.
    dnogo = models.FloatField(db_column='dNOGO', blank=True, null=True)  # Field name made lowercase.
    dtoldiff = models.FloatField(db_column='dTolDiff', blank=True, null=True)  # Field name made lowercase.
    dtolallowed = models.FloatField(db_column='dTolAllowed', blank=True, null=True)  # Field name made lowercase.
    bmanufacturingstd = models.BooleanField(db_column='bManufacturingSTD', blank=True, null=True)  # Field name made lowercase.
    dplusofminus = models.FloatField(db_column='dPlusofminus', blank=True, null=True)  # Field name made lowercase.
    dz = models.FloatField(db_column='dZ', blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnextdisplay = models.DateTimeField(db_column='dNextDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextalert = models.DateTimeField(db_column='dNextAlert', blank=True, null=True)  # Field name made lowercase.
    dnextdisplay1 = models.DateTimeField(db_column='dNextDisplay1', blank=True, null=True)  # Field name made lowercase.
    dnextalert1 = models.DateTimeField(db_column='dNextAlert1', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.
    bdontblockcalibidle = models.BooleanField(db_column='bDontBlockCalibIdle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentsList'


class Thistorytransactions(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    lhistorymainid = models.IntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    shistorytype = models.CharField(db_column='sHistoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendor = models.CharField(db_column='sCalibrationVendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendorid = models.CharField(db_column='sCalibrationVendorID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationresult = models.CharField(db_column='sCalibrationResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtcalibrationdate = models.DateTimeField(db_column='dtCalibrationDate', blank=True, null=True)  # Field name made lowercase.
    fcalibcost = models.FloatField(db_column='fCalibCost', blank=True, null=True)  # Field name made lowercase.
    llplantid = models.IntegerField(db_column='llPlantId', blank=True, null=True)  # Field name made lowercase.
    ssplantname = models.CharField(db_column='ssPlantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slplantcode = models.CharField(db_column='slPlantCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryTransactions'


class Admin1Atrack(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.IntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.
    dtdateoftransaction = models.DateTimeField(db_column='dtDateofTransaction', blank=True, null=True)  # Field name made lowercase.
    stimeoftrans = models.CharField(db_column='sTimeofTrans', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepage = models.CharField(db_column='sUsedTypePage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework = models.CharField(db_column='sUsedTypePageWork', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework1 = models.CharField(db_column='sUsedTypePageWork1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework2 = models.CharField(db_column='sUsedTypePageWork2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedby = models.CharField(db_column='sUsedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin1ATrack'


class Admin1Companyinfo(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=655, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=155, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=155, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scontact_no = models.CharField(db_column='sContact_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slogofile = models.CharField(db_column='sLogoFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slicence = models.CharField(db_column='sLicence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sproduct = models.CharField(max_length=255, blank=True, null=True)
    bdemo = models.BooleanField(blank=True, null=True)
    dtstartdate = models.DateTimeField(db_column='dtStartDate', blank=True, null=True)  # Field name made lowercase.
    ldays = models.IntegerField(db_column='lDays', blank=True, null=True)  # Field name made lowercase.
    dtcurrentdate = models.DateTimeField(db_column='dtCurrentDate', blank=True, null=True)  # Field name made lowercase.
    sdivision = models.CharField(db_column='sDivision', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtreminderdate = models.DateTimeField(db_column='dtReminderDate', blank=True, null=True)  # Field name made lowercase.
    semailsendfrom = models.CharField(db_column='sEmailSendFrom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semailsmtpno = models.CharField(db_column='sEmailSMTPNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lremotesocket = models.IntegerField(db_column='lRemoteSocket', blank=True, null=True)  # Field name made lowercase.
    sremotehost = models.CharField(db_column='sRemoteHost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail1 = models.CharField(db_column='sEmail1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail2 = models.CharField(db_column='sEmail2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail3 = models.CharField(db_column='sEmail3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail4 = models.CharField(db_column='sEmail4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail5 = models.CharField(db_column='sEmail5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail6 = models.CharField(db_column='sEmail6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail7 = models.CharField(db_column='sEmail7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail8 = models.CharField(db_column='sEmail8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail9 = models.CharField(db_column='sEmail9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail10 = models.CharField(db_column='sEmail10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail11 = models.CharField(db_column='sEmail11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail12 = models.CharField(db_column='sEmail12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail13 = models.CharField(db_column='sEmail13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail14 = models.CharField(db_column='sEmail14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail15 = models.CharField(db_column='sEmail15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail16 = models.CharField(db_column='sEmail16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail17 = models.CharField(db_column='sEmail17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail18 = models.CharField(db_column='sEmail18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail19 = models.CharField(db_column='sEmail19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semail20 = models.CharField(db_column='sEmail20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ldcno = models.IntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    lmonth = models.IntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.IntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    ldcno1 = models.IntegerField(db_column='lDCNo1', blank=True, null=True)  # Field name made lowercase.
    ldcno2 = models.IntegerField(db_column='lDCNo2', blank=True, null=True)  # Field name made lowercase.
    ldcno3 = models.IntegerField(db_column='lDCNo3', blank=True, null=True)  # Field name made lowercase.
    ldcno4 = models.IntegerField(db_column='lDCNo4', blank=True, null=True)  # Field name made lowercase.
    ldcno5 = models.IntegerField(db_column='lDCNo5', blank=True, null=True)  # Field name made lowercase.
    ldcno6 = models.IntegerField(db_column='lDCNo6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin1CompanyInfo'


class Adminassetcategorylist(models.Model):
    lcategoryid = models.AutoField(db_column='lCategoryID', primary_key=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='CategoryType', max_length=255)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lassetid = models.IntegerField(db_column='lAssetID', blank=True, null=True)  # Field name made lowercase.
    btyperef = models.BooleanField(db_column='bTypeRef', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    btyperef1 = models.BooleanField(db_column='bTypeRef1', blank=True, null=True)  # Field name made lowercase.
    styperefname1 = models.CharField(db_column='sTypeRefName1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring1 = models.BooleanField(db_column='bTypeRefasString1', blank=True, null=True)  # Field name made lowercase.
    btyperefasint1 = models.BooleanField(db_column='bTypeRefasInt1', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange1 = models.BooleanField(db_column='bTypeRefasRange1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa1 = models.BooleanField(db_column='bTypeRefasContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob1 = models.BooleanField(db_column='bTypeRefasContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa1 = models.IntegerField(db_column='lContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob1 = models.IntegerField(db_column='lContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    btyperef2 = models.BooleanField(db_column='bTypeRef2', blank=True, null=True)  # Field name made lowercase.
    styperefname2 = models.CharField(db_column='sTypeRefName2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring2 = models.BooleanField(db_column='bTypeRefasString2', blank=True, null=True)  # Field name made lowercase.
    btyperefasint2 = models.BooleanField(db_column='bTypeRefasInt2', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange2 = models.BooleanField(db_column='bTypeRefasRange2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa2 = models.BooleanField(db_column='bTypeRefasContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob2 = models.BooleanField(db_column='bTypeRefasContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa2 = models.IntegerField(db_column='lContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob2 = models.IntegerField(db_column='lContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    btyperef3 = models.BooleanField(db_column='bTypeRef3', blank=True, null=True)  # Field name made lowercase.
    styperefname3 = models.CharField(db_column='sTypeRefName3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring3 = models.BooleanField(db_column='bTypeRefasString3', blank=True, null=True)  # Field name made lowercase.
    btyperefasint3 = models.BooleanField(db_column='bTypeRefasInt3', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange3 = models.BooleanField(db_column='bTypeRefasRange3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa3 = models.BooleanField(db_column='bTypeRefasContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob3 = models.BooleanField(db_column='bTypeRefasContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa3 = models.IntegerField(db_column='lContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob3 = models.IntegerField(db_column='lContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    btyperef4 = models.BooleanField(db_column='bTypeRef4', blank=True, null=True)  # Field name made lowercase.
    styperefname4 = models.CharField(db_column='sTypeRefName4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring4 = models.BooleanField(db_column='bTypeRefasString4', blank=True, null=True)  # Field name made lowercase.
    btyperefasint4 = models.BooleanField(db_column='bTypeRefasInt4', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange4 = models.BooleanField(db_column='bTypeRefasRange4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa4 = models.BooleanField(db_column='bTypeRefasContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob4 = models.BooleanField(db_column='bTypeRefasContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa4 = models.IntegerField(db_column='lContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob4 = models.IntegerField(db_column='lContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    btyperef5 = models.BooleanField(db_column='bTypeRef5', blank=True, null=True)  # Field name made lowercase.
    styperefname5 = models.CharField(db_column='sTypeRefName5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring5 = models.BooleanField(db_column='bTypeRefasString5', blank=True, null=True)  # Field name made lowercase.
    btyperefasint5 = models.BooleanField(db_column='bTypeRefasInt5', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange5 = models.BooleanField(db_column='bTypeRefasRange5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa5 = models.BooleanField(db_column='bTypeRefasContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob5 = models.BooleanField(db_column='bTypeRefasContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa5 = models.IntegerField(db_column='lContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob5 = models.IntegerField(db_column='lContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    btyperef6 = models.BooleanField(db_column='bTypeRef6', blank=True, null=True)  # Field name made lowercase.
    styperefname6 = models.CharField(db_column='sTypeRefName6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring6 = models.BooleanField(db_column='bTypeRefasString6', blank=True, null=True)  # Field name made lowercase.
    btyperefasint6 = models.BooleanField(db_column='bTypeRefasInt6', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange6 = models.BooleanField(db_column='bTypeRefasRange6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa6 = models.BooleanField(db_column='bTypeRefasContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob6 = models.BooleanField(db_column='bTypeRefasContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa6 = models.IntegerField(db_column='lContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob6 = models.IntegerField(db_column='lContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    btyperef7 = models.BooleanField(db_column='bTypeRef7', blank=True, null=True)  # Field name made lowercase.
    styperefname7 = models.CharField(db_column='sTypeRefName7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring7 = models.BooleanField(db_column='bTypeRefasString7', blank=True, null=True)  # Field name made lowercase.
    btyperefasint7 = models.BooleanField(db_column='bTypeRefasInt7', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange7 = models.BooleanField(db_column='bTypeRefasRange7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa7 = models.BooleanField(db_column='bTypeRefasContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob7 = models.BooleanField(db_column='bTypeRefasContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa7 = models.IntegerField(db_column='lContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob7 = models.IntegerField(db_column='lContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    btyperef8 = models.BooleanField(db_column='bTypeRef8', blank=True, null=True)  # Field name made lowercase.
    styperefname8 = models.CharField(db_column='sTypeRefName8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring8 = models.BooleanField(db_column='bTypeRefasString8', blank=True, null=True)  # Field name made lowercase.
    btyperefasint8 = models.BooleanField(db_column='bTypeRefasInt8', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange8 = models.BooleanField(db_column='bTypeRefasRange8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa8 = models.BooleanField(db_column='bTypeRefasContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob8 = models.BooleanField(db_column='bTypeRefasContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa8 = models.IntegerField(db_column='lContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob8 = models.IntegerField(db_column='lContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    btyperef9 = models.BooleanField(db_column='bTypeRef9', blank=True, null=True)  # Field name made lowercase.
    styperefname9 = models.CharField(db_column='sTypeRefName9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring9 = models.BooleanField(db_column='bTypeRefasString9', blank=True, null=True)  # Field name made lowercase.
    btyperefasint9 = models.BooleanField(db_column='bTypeRefasInt9', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange9 = models.BooleanField(db_column='bTypeRefasRange9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa9 = models.BooleanField(db_column='bTypeRefasContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob9 = models.BooleanField(db_column='bTypeRefasContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa9 = models.IntegerField(db_column='lContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob9 = models.IntegerField(db_column='lContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    btyperef10 = models.BooleanField(db_column='bTypeRef10', blank=True, null=True)  # Field name made lowercase.
    styperefname10 = models.CharField(db_column='sTypeRefName10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring10 = models.BooleanField(db_column='bTypeRefasString10', blank=True, null=True)  # Field name made lowercase.
    btyperefasint10 = models.BooleanField(db_column='bTypeRefasInt10', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange10 = models.BooleanField(db_column='bTypeRefasRange10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa10 = models.BooleanField(db_column='bTypeRefasContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob10 = models.BooleanField(db_column='bTypeRefasContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa10 = models.IntegerField(db_column='lContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob10 = models.IntegerField(db_column='lContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    btyperef11 = models.BooleanField(db_column='bTypeRef11', blank=True, null=True)  # Field name made lowercase.
    styperefname11 = models.CharField(db_column='sTypeRefName11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring11 = models.BooleanField(db_column='bTypeRefasString11', blank=True, null=True)  # Field name made lowercase.
    btyperefasint11 = models.BooleanField(db_column='bTypeRefasInt11', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange11 = models.BooleanField(db_column='bTypeRefasRange11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa11 = models.BooleanField(db_column='bTypeRefasContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob11 = models.BooleanField(db_column='bTypeRefasContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa11 = models.IntegerField(db_column='lContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob11 = models.IntegerField(db_column='lContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    btyperef12 = models.BooleanField(db_column='bTypeRef12', blank=True, null=True)  # Field name made lowercase.
    styperefname12 = models.CharField(db_column='sTypeRefName12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring12 = models.BooleanField(db_column='bTypeRefasString12', blank=True, null=True)  # Field name made lowercase.
    btyperefasint12 = models.BooleanField(db_column='bTypeRefasInt12', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange12 = models.BooleanField(db_column='bTypeRefasRange12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa12 = models.BooleanField(db_column='bTypeRefasContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob12 = models.BooleanField(db_column='bTypeRefasContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa12 = models.IntegerField(db_column='lContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob12 = models.IntegerField(db_column='lContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    btyperef13 = models.BooleanField(db_column='bTypeRef13', blank=True, null=True)  # Field name made lowercase.
    styperefname13 = models.CharField(db_column='sTypeRefName13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring13 = models.BooleanField(db_column='bTypeRefasString13', blank=True, null=True)  # Field name made lowercase.
    btyperefasint13 = models.BooleanField(db_column='bTypeRefasInt13', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange13 = models.BooleanField(db_column='bTypeRefasRange13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa13 = models.BooleanField(db_column='bTypeRefasContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob13 = models.BooleanField(db_column='bTypeRefasContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa13 = models.IntegerField(db_column='lContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob13 = models.IntegerField(db_column='lContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    btyperef14 = models.BooleanField(db_column='bTypeRef14', blank=True, null=True)  # Field name made lowercase.
    styperefname14 = models.CharField(db_column='sTypeRefName14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring14 = models.BooleanField(db_column='bTypeRefasString14', blank=True, null=True)  # Field name made lowercase.
    btyperefasint14 = models.BooleanField(db_column='bTypeRefasInt14', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange14 = models.BooleanField(db_column='bTypeRefasRange14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa14 = models.BooleanField(db_column='bTypeRefasContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob14 = models.BooleanField(db_column='bTypeRefasContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa14 = models.IntegerField(db_column='lContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob14 = models.IntegerField(db_column='lContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    btyperef15 = models.BooleanField(db_column='bTypeRef15', blank=True, null=True)  # Field name made lowercase.
    styperefname15 = models.CharField(db_column='sTypeRefName15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring15 = models.BooleanField(db_column='bTypeRefasString15', blank=True, null=True)  # Field name made lowercase.
    btyperefasint15 = models.BooleanField(db_column='bTypeRefasInt15', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange15 = models.BooleanField(db_column='bTypeRefasRange15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa15 = models.BooleanField(db_column='bTypeRefasContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob15 = models.BooleanField(db_column='bTypeRefasContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa15 = models.IntegerField(db_column='lContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob15 = models.IntegerField(db_column='lContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    btyperef16 = models.BooleanField(db_column='bTypeRef16', blank=True, null=True)  # Field name made lowercase.
    styperefname16 = models.CharField(db_column='sTypeRefName16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring16 = models.BooleanField(db_column='bTypeRefasString16', blank=True, null=True)  # Field name made lowercase.
    btyperefasint16 = models.BooleanField(db_column='bTypeRefasInt16', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange16 = models.BooleanField(db_column='bTypeRefasRange16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa16 = models.BooleanField(db_column='bTypeRefasContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob16 = models.BooleanField(db_column='bTypeRefasContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa16 = models.IntegerField(db_column='lContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob16 = models.IntegerField(db_column='lContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    btyperef17 = models.BooleanField(db_column='bTypeRef17', blank=True, null=True)  # Field name made lowercase.
    styperefname17 = models.CharField(db_column='sTypeRefName17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring17 = models.BooleanField(db_column='bTypeRefasString17', blank=True, null=True)  # Field name made lowercase.
    btyperefasint17 = models.BooleanField(db_column='bTypeRefasInt17', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange17 = models.BooleanField(db_column='bTypeRefasRange17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa17 = models.BooleanField(db_column='bTypeRefasContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob17 = models.BooleanField(db_column='bTypeRefasContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa17 = models.IntegerField(db_column='lContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob17 = models.IntegerField(db_column='lContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    btyperef18 = models.BooleanField(db_column='bTypeRef18', blank=True, null=True)  # Field name made lowercase.
    styperefname18 = models.CharField(db_column='sTypeRefName18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring18 = models.BooleanField(db_column='bTypeRefasString18', blank=True, null=True)  # Field name made lowercase.
    btyperefasint18 = models.BooleanField(db_column='bTypeRefasInt18', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange18 = models.BooleanField(db_column='bTypeRefasRange18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa18 = models.BooleanField(db_column='bTypeRefasContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob18 = models.BooleanField(db_column='bTypeRefasContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa18 = models.IntegerField(db_column='lContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob18 = models.IntegerField(db_column='lContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    btyperef19 = models.BooleanField(db_column='bTypeRef19', blank=True, null=True)  # Field name made lowercase.
    styperefname19 = models.CharField(db_column='sTypeRefName19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring19 = models.BooleanField(db_column='bTypeRefasString19', blank=True, null=True)  # Field name made lowercase.
    btyperefasint19 = models.BooleanField(db_column='bTypeRefasInt19', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange19 = models.BooleanField(db_column='bTypeRefasRange19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa19 = models.BooleanField(db_column='bTypeRefasContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob19 = models.BooleanField(db_column='bTypeRefasContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa19 = models.IntegerField(db_column='lContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob19 = models.IntegerField(db_column='lContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    btyperef20 = models.BooleanField(db_column='bTypeRef20', blank=True, null=True)  # Field name made lowercase.
    styperefname20 = models.CharField(db_column='sTypeRefName20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring20 = models.BooleanField(db_column='bTypeRefasString20', blank=True, null=True)  # Field name made lowercase.
    btyperefasint20 = models.BooleanField(db_column='bTypeRefasInt20', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange20 = models.BooleanField(db_column='bTypeRefasRange20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa20 = models.BooleanField(db_column='bTypeRefasContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob20 = models.BooleanField(db_column='bTypeRefasContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa20 = models.IntegerField(db_column='lContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob20 = models.IntegerField(db_column='lContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
    b1 = models.BooleanField(blank=True, null=True)
    b2 = models.BooleanField(blank=True, null=True)
    b3 = models.BooleanField(blank=True, null=True)
    b4 = models.BooleanField(blank=True, null=True)
    b5 = models.BooleanField(blank=True, null=True)
    b6 = models.BooleanField(blank=True, null=True)
    b7 = models.BooleanField(blank=True, null=True)
    b8 = models.BooleanField(blank=True, null=True)
    b9 = models.BooleanField(blank=True, null=True)
    b10 = models.BooleanField(blank=True, null=True)
    bpressuregauge = models.BooleanField(db_column='bPressureGauge', blank=True, null=True)  # Field name made lowercase.
    btimer = models.BooleanField(db_column='bTimer', blank=True, null=True)  # Field name made lowercase.
    bpowersupply = models.BooleanField(db_column='bPowerSupply', blank=True, null=True)  # Field name made lowercase.
    bgeneral = models.BooleanField(db_column='bGeneral', blank=True, null=True)  # Field name made lowercase.
    bvernier = models.BooleanField(db_column='bVernier', blank=True, null=True)  # Field name made lowercase.
    bboregaugewithdial = models.BooleanField(db_column='bBoreGaugewithDial', blank=True, null=True)  # Field name made lowercase.
    bboregauge = models.BooleanField(db_column='bBoreGauge', blank=True, null=True)  # Field name made lowercase.
    bdialindicator = models.BooleanField(db_column='bDialIndicator', blank=True, null=True)  # Field name made lowercase.
    bheightgauge = models.BooleanField(db_column='bHeightGauge', blank=True, null=True)  # Field name made lowercase.
    bmicrometer = models.BooleanField(db_column='bMicrometer', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.IntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.IntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lrnr = models.IntegerField(db_column='lRnR', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lattribute = models.IntegerField(db_column='lAttribute', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lstability = models.IntegerField(db_column='lStability', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lbias = models.IntegerField(db_column='lBias', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    llinearity = models.IntegerField(db_column='lLinearity', blank=True, null=True)  # Field name made lowercase.
    bmsablock = models.BooleanField(db_column='bMSABlock', blank=True, null=True)  # Field name made lowercase.
    lminqty = models.IntegerField(db_column='lMinQty', blank=True, null=True)  # Field name made lowercase.
    lmaxqty = models.IntegerField(db_column='lMaxQty', blank=True, null=True)  # Field name made lowercase.
    lavailableqty = models.IntegerField(db_column='lAvailableQty', blank=True, null=True)  # Field name made lowercase.
    bnotrequired = models.BooleanField(db_column='bNotRequired', blank=True, null=True)  # Field name made lowercase.
    bmanufacturingstd = models.BooleanField(db_column='bManufacturingStd', blank=True, null=True)  # Field name made lowercase.
    bppg = models.BooleanField(db_column='bPPG', blank=True, null=True)  # Field name made lowercase.
    bradiusgauge = models.BooleanField(db_column='bRadiusGauge', blank=True, null=True)  # Field name made lowercase.
    bsettingring = models.BooleanField(db_column='bSettingRing', blank=True, null=True)  # Field name made lowercase.
    bthreadpluggauge = models.BooleanField(db_column='bThreadPlugGauge', blank=True, null=True)  # Field name made lowercase.
    bthreadringgauge = models.BooleanField(db_column='bThreadRingGauge', blank=True, null=True)  # Field name made lowercase.
    bdialgauge = models.BooleanField(db_column='bDialGauge', blank=True, null=True)  # Field name made lowercase.
    bslipgauge = models.BooleanField(db_column='bSlipGauge', blank=True, null=True)  # Field name made lowercase.
    bprg = models.BooleanField(db_column='bPRG', blank=True, null=True)  # Field name made lowercase.
    smsasopfile = models.CharField(db_column='sMSASOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.IntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.IntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.IntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryList'


class Adminassetcategorytypelist(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList'


class Adminassetcategorytypelist1(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList1'


class Adminassetcategorytypelist10(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList10'


class Adminassetcategorytypelist11(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList11'


class Adminassetcategorytypelist12(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList12'


class Adminassetcategorytypelist13(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList13'


class Adminassetcategorytypelist14(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList14'


class Adminassetcategorytypelist15(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList15'


class Adminassetcategorytypelist16(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList16'


class Adminassetcategorytypelist17(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList17'


class Adminassetcategorytypelist18(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList18'


class Adminassetcategorytypelist19(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList19'


class Adminassetcategorytypelist2(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList2'


class Adminassetcategorytypelist20(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList20'


class Adminassetcategorytypelist3(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList3'


class Adminassetcategorytypelist4(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList4'


class Adminassetcategorytypelist5(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList5'


class Adminassetcategorytypelist6(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList6'


class Adminassetcategorytypelist7(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList7'


class Adminassetcategorytypelist8(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList8'


class Adminassetcategorytypelist9(models.Model):
    lcategorytypeid = models.AutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.IntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.IntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.IntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.IntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasInt', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.IntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.IntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList9'


class Adminassetclassificationlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sclassification = models.CharField(db_column='sClassification', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetClassificationList'


class Adminassetcontinuousformatlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scontinuousformat = models.CharField(db_column='sContinuousFormat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcontinuousformat = models.IntegerField(db_column='lContinuousFormat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetContinuousFormatList'


class Adminassetserialformatlist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lserialno = models.IntegerField(db_column='lSerialNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetSerialFormatList'


class Adminassetsparepartslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srevetails = models.CharField(db_column='sRevetails', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bstock = models.BooleanField(db_column='bStock', blank=True, null=True)  # Field name made lowercase.
    drate = models.FloatField(db_column='dRate', blank=True, null=True)  # Field name made lowercase.
    lopenbal = models.IntegerField(db_column='lOpenBal', blank=True, null=True)  # Field name made lowercase.
    linward = models.IntegerField(db_column='lInward', blank=True, null=True)  # Field name made lowercase.
    loutward = models.IntegerField(db_column='lOutward', blank=True, null=True)  # Field name made lowercase.
    ltotqty = models.IntegerField(db_column='lTotQty', blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.
    lcode = models.IntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.IntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.IntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.IntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetSparePartsList'


class Adminassettypelist(models.Model):
    lassetid = models.AutoField(db_column='lAssetID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetTypeList'


class Adminassettypesublist(models.Model):
    lassetid = models.AutoField(db_column='lAssetID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lassettypeid = models.IntegerField(db_column='lAssetTypeID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    bequipment = models.BooleanField(db_column='bEquipment', blank=True, null=True)  # Field name made lowercase.
    bmachine = models.BooleanField(db_column='bMachine', blank=True, null=True)  # Field name made lowercase.
    brange2variable = models.BooleanField(db_column='bRange2Variable', blank=True, null=True)  # Field name made lowercase.
    brange3variable = models.BooleanField(db_column='bRange3Variable', blank=True, null=True)  # Field name made lowercase.
    bmaterial = models.BooleanField(db_column='bMaterial', blank=True, null=True)  # Field name made lowercase.
    boperation = models.BooleanField(db_column='bOperation', blank=True, null=True)  # Field name made lowercase.
    bcontinuousno = models.BooleanField(db_column='bContinuousNo', blank=True, null=True)  # Field name made lowercase.
    btype = models.BooleanField(db_column='bType', blank=True, null=True)  # Field name made lowercase.
    btype1 = models.BooleanField(db_column='bType1', blank=True, null=True)  # Field name made lowercase.
    btype2 = models.BooleanField(db_column='bType2', blank=True, null=True)  # Field name made lowercase.
    btype3 = models.BooleanField(db_column='bType3', blank=True, null=True)  # Field name made lowercase.
    btype4 = models.BooleanField(db_column='bType4', blank=True, null=True)  # Field name made lowercase.
    btype5 = models.BooleanField(db_column='bType5', blank=True, null=True)  # Field name made lowercase.
    btype6 = models.BooleanField(db_column='bType6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetTypeSubList'


class Admincalibconditionslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stemperature = models.CharField(db_column='sTemperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shumidity = models.CharField(db_column='sHumidity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCalibConditionsList'


class Admincategoryidcontinuousnolist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lserialno = models.IntegerField(db_column='lSerialNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCategoryIDContinuousNoList'


class Admincustomerlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCustomerList'


class Adminequipmentlist(models.Model):
    lid = models.AutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    sequipmentname = models.CharField(db_column='sEquipmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminEquipmentList'


class Adminexternalagencylist(models.Model):
    lagencyid = models.AutoField(db_column='lAgencyId', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scontact_no = models.CharField(db_column='sContact_No', max_length=350, blank=True, null=True)  # Field name made lowercase.
    semail = models.CharField(db_column='sEmail', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scontact_person = models.CharField(db_column='sContact_Person', max_length=350, blank=True, null=True)  # Field name made lowercase.
    s_o_calib = models.CharField(db_column='S_O_Calib', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sbasisofaffiliation = models.CharField(db_column='sBasisofAffiliation', max_length=350, blank=True, null=True)  # Field name made lowercase.
    svendorid = models.CharField(db_column='sVendorID', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bmaker = models.BooleanField(db_column='bMaker', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    bcalib = models.BooleanField(db_column='bCalib', blank=True, null=True)  # Field name made lowercase.
    bcustomers = models.BooleanField(db_column='bCustomers', blank=True, null=True)  # Field name made lowercase.
    bmeasurement = models.BooleanField(db_column='bMeasurement', blank=True, null=True)  # Field name made lowercase.
    bcmm = models.BooleanField(db_column='bCMM', blank=True, null=True)  # Field name made lowercase.
    calib_rate = models.FloatField(db_column='Calib_Rate', blank=True, null=True)  # Field name made lowercase.
    dconfidencelevel = models.FloatField(db_column='dConfidenceLevel', blank=True, null=True)  # Field name made lowercase.
    sconfidencelevel = models.CharField(db_column='sConfidenceLevel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtnablcertificatevalidity = models.DateTimeField(db_column='dtNABLCertificateValidity', blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatedate = models.CharField(db_column='sNABLCertificateDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatefile = models.CharField(db_column='sNABLCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatepath = models.CharField(db_column='sNABLCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationID', blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    span = models.CharField(db_column='sPAN', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminExternalAgencyList'


class Adminexternalagencytraceabilitylist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatedate = models.CharField(db_column='sNABLCertificateDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatefile = models.CharField(db_column='sNABLCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatepath = models.CharField(db_column='sNABLCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lagencyid = models.IntegerField(db_column='lAgencyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminExternalAgencyTraceabilityList'


class Admingradelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sgradename = models.CharField(db_column='sGradeName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminGradeList'


class Admininstrumentcattypelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scattype = models.CharField(db_column='sCatType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentCatTypeList'


class Admininstrumentcatsubtypelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scattype = models.CharField(db_column='sCatType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcattypeid = models.IntegerField(db_column='lCatTypeId', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentCatsubTypeList'


class Admininstrumentequipmentlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sequipment = models.CharField(db_column='sEquipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentEquipmentList'


class Admininstrumentmateriallist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smaterial = models.CharField(db_column='sMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentMaterialList'


class Admininstrumentoperationlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    soperation = models.CharField(db_column='sOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentOperationList'


class Admininstrumentrangelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentRangeList'


class Admininstrumenttypelist(models.Model):
    lid = models.AutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    sinstrumenttype = models.CharField(db_column='sInstrumentType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentTypeList'


class Adminlocationlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    slocationname = models.CharField(db_column='sLocationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scontactperson = models.CharField(db_column='sContactPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scontactemailid = models.CharField(db_column='sContactEMailId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminLocationList'


class Adminmakelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smake = models.CharField(db_column='sMake', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminMakeList'


class Adminmateriallist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smaterial = models.CharField(db_column='sMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminMaterialList'


class Adminoperatorlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    soperator = models.CharField(db_column='sOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminOperatorList'


class Adminpartdetailslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spartname = models.CharField(db_column='sPartName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.IntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lpantid = models.IntegerField(db_column='lPantId', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.IntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.IntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    smsasopfile = models.CharField(db_column='sMSASOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.IntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.IntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.IntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    ldueday1 = models.IntegerField(db_column='lDueDay1', blank=True, null=True)  # Field name made lowercase.
    lduemonth1 = models.IntegerField(db_column='lDueMonth1', blank=True, null=True)  # Field name made lowercase.
    ldueyear1 = models.IntegerField(db_column='lDueYear1', blank=True, null=True)  # Field name made lowercase.
    ldueday2 = models.IntegerField(db_column='lDueDay2', blank=True, null=True)  # Field name made lowercase.
    lduemonth2 = models.IntegerField(db_column='lDueMonth2', blank=True, null=True)  # Field name made lowercase.
    ldueyear2 = models.IntegerField(db_column='lDueYear2', blank=True, null=True)  # Field name made lowercase.
    ldueday3 = models.IntegerField(db_column='lDueDay3', blank=True, null=True)  # Field name made lowercase.
    lduemonth3 = models.IntegerField(db_column='lDueMonth3', blank=True, null=True)  # Field name made lowercase.
    ldueyear3 = models.IntegerField(db_column='lDueYear3', blank=True, null=True)  # Field name made lowercase.
    ldueday4 = models.IntegerField(db_column='lDueDay4', blank=True, null=True)  # Field name made lowercase.
    lduemonth4 = models.IntegerField(db_column='lDueMonth4', blank=True, null=True)  # Field name made lowercase.
    ldueyear4 = models.IntegerField(db_column='lDueYear4', blank=True, null=True)  # Field name made lowercase.
    ldueday5 = models.IntegerField(db_column='lDueDay5', blank=True, null=True)  # Field name made lowercase.
    lduemonth5 = models.IntegerField(db_column='lDueMonth5', blank=True, null=True)  # Field name made lowercase.
    ldueyear5 = models.IntegerField(db_column='lDueYear5', blank=True, null=True)  # Field name made lowercase.
    ldueday6 = models.IntegerField(db_column='lDueDay6', blank=True, null=True)  # Field name made lowercase.
    lduemonth6 = models.IntegerField(db_column='lDueMonth6', blank=True, null=True)  # Field name made lowercase.
    ldueyear6 = models.IntegerField(db_column='lDueYear6', blank=True, null=True)  # Field name made lowercase.
    bvisualinspection = models.BooleanField(db_column='bVisualInspection', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr1 = models.IntegerField(db_column='lIntervalRnR1', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr1 = models.CharField(db_column='sIntervalPeriodRnR1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr1 = models.DateTimeField(db_column='dLastRnR1', blank=True, null=True)  # Field name made lowercase.
    dnextrnr1 = models.DateTimeField(db_column='dNextRnR1', blank=True, null=True)  # Field name made lowercase.
    lalertinterval1 = models.IntegerField(db_column='lAlertInterval1', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate1 = models.DateTimeField(db_column='dtRnRDisplayDate1', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr2 = models.IntegerField(db_column='lIntervalRnR2', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr2 = models.CharField(db_column='sIntervalPeriodRnR2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr2 = models.DateTimeField(db_column='dLastRnR2', blank=True, null=True)  # Field name made lowercase.
    dnextrnr2 = models.DateTimeField(db_column='dNextRnR2', blank=True, null=True)  # Field name made lowercase.
    lalertinterval2 = models.IntegerField(db_column='lAlertInterval2', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate2 = models.DateTimeField(db_column='dtRnRDisplayDate2', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr3 = models.IntegerField(db_column='lIntervalRnR3', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr3 = models.CharField(db_column='sIntervalPeriodRnR3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr3 = models.DateTimeField(db_column='dLastRnR3', blank=True, null=True)  # Field name made lowercase.
    dnextrnr3 = models.DateTimeField(db_column='dNextRnR3', blank=True, null=True)  # Field name made lowercase.
    lalertinterval3 = models.IntegerField(db_column='lAlertInterval3', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate3 = models.DateTimeField(db_column='dtRnRDisplayDate3', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr4 = models.IntegerField(db_column='lIntervalRnR4', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr4 = models.CharField(db_column='sIntervalPeriodRnR4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr4 = models.DateTimeField(db_column='dLastRnR4', blank=True, null=True)  # Field name made lowercase.
    dnextrnr4 = models.DateTimeField(db_column='dNextRnR4', blank=True, null=True)  # Field name made lowercase.
    lalertinterval4 = models.IntegerField(db_column='lAlertInterval4', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate4 = models.DateTimeField(db_column='dtRnRDisplayDate4', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr5 = models.IntegerField(db_column='lIntervalRnR5', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr5 = models.CharField(db_column='sIntervalPeriodRnR5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr5 = models.DateTimeField(db_column='dLastRnR5', blank=True, null=True)  # Field name made lowercase.
    dnextrnr5 = models.DateTimeField(db_column='dNextRnR5', blank=True, null=True)  # Field name made lowercase.
    lalertinterval5 = models.IntegerField(db_column='lAlertInterval5', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate5 = models.DateTimeField(db_column='dtRnRDisplayDate5', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsList'


class AdminpartdetailslistBackup(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spartname = models.CharField(db_column='sPartName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.IntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lpantid = models.IntegerField(db_column='lPantId', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.IntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.IntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    smsasopfile = models.CharField(db_column='sMSASOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.IntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.IntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.IntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    ldueday1 = models.IntegerField(db_column='lDueDay1', blank=True, null=True)  # Field name made lowercase.
    lduemonth1 = models.IntegerField(db_column='lDueMonth1', blank=True, null=True)  # Field name made lowercase.
    ldueyear1 = models.IntegerField(db_column='lDueYear1', blank=True, null=True)  # Field name made lowercase.
    ldueday2 = models.IntegerField(db_column='lDueDay2', blank=True, null=True)  # Field name made lowercase.
    lduemonth2 = models.IntegerField(db_column='lDueMonth2', blank=True, null=True)  # Field name made lowercase.
    ldueyear2 = models.IntegerField(db_column='lDueYear2', blank=True, null=True)  # Field name made lowercase.
    ldueday3 = models.IntegerField(db_column='lDueDay3', blank=True, null=True)  # Field name made lowercase.
    lduemonth3 = models.IntegerField(db_column='lDueMonth3', blank=True, null=True)  # Field name made lowercase.
    ldueyear3 = models.IntegerField(db_column='lDueYear3', blank=True, null=True)  # Field name made lowercase.
    ldueday4 = models.IntegerField(db_column='lDueDay4', blank=True, null=True)  # Field name made lowercase.
    lduemonth4 = models.IntegerField(db_column='lDueMonth4', blank=True, null=True)  # Field name made lowercase.
    ldueyear4 = models.IntegerField(db_column='lDueYear4', blank=True, null=True)  # Field name made lowercase.
    ldueday5 = models.IntegerField(db_column='lDueDay5', blank=True, null=True)  # Field name made lowercase.
    lduemonth5 = models.IntegerField(db_column='lDueMonth5', blank=True, null=True)  # Field name made lowercase.
    ldueyear5 = models.IntegerField(db_column='lDueYear5', blank=True, null=True)  # Field name made lowercase.
    ldueday6 = models.IntegerField(db_column='lDueDay6', blank=True, null=True)  # Field name made lowercase.
    lduemonth6 = models.IntegerField(db_column='lDueMonth6', blank=True, null=True)  # Field name made lowercase.
    ldueyear6 = models.IntegerField(db_column='lDueYear6', blank=True, null=True)  # Field name made lowercase.
    bvisualinspection = models.BooleanField(db_column='bVisualInspection', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr1 = models.IntegerField(db_column='lIntervalRnR1', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr1 = models.CharField(db_column='sIntervalPeriodRnR1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr1 = models.DateTimeField(db_column='dLastRnR1', blank=True, null=True)  # Field name made lowercase.
    dnextrnr1 = models.DateTimeField(db_column='dNextRnR1', blank=True, null=True)  # Field name made lowercase.
    lalertinterval1 = models.IntegerField(db_column='lAlertInterval1', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate1 = models.DateTimeField(db_column='dtRnRDisplayDate1', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr2 = models.IntegerField(db_column='lIntervalRnR2', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr2 = models.CharField(db_column='sIntervalPeriodRnR2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr2 = models.DateTimeField(db_column='dLastRnR2', blank=True, null=True)  # Field name made lowercase.
    dnextrnr2 = models.DateTimeField(db_column='dNextRnR2', blank=True, null=True)  # Field name made lowercase.
    lalertinterval2 = models.IntegerField(db_column='lAlertInterval2', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate2 = models.DateTimeField(db_column='dtRnRDisplayDate2', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr3 = models.IntegerField(db_column='lIntervalRnR3', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr3 = models.CharField(db_column='sIntervalPeriodRnR3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr3 = models.DateTimeField(db_column='dLastRnR3', blank=True, null=True)  # Field name made lowercase.
    dnextrnr3 = models.DateTimeField(db_column='dNextRnR3', blank=True, null=True)  # Field name made lowercase.
    lalertinterval3 = models.IntegerField(db_column='lAlertInterval3', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate3 = models.DateTimeField(db_column='dtRnRDisplayDate3', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr4 = models.IntegerField(db_column='lIntervalRnR4', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr4 = models.CharField(db_column='sIntervalPeriodRnR4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr4 = models.DateTimeField(db_column='dLastRnR4', blank=True, null=True)  # Field name made lowercase.
    dnextrnr4 = models.DateTimeField(db_column='dNextRnR4', blank=True, null=True)  # Field name made lowercase.
    lalertinterval4 = models.IntegerField(db_column='lAlertInterval4', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate4 = models.DateTimeField(db_column='dtRnRDisplayDate4', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr5 = models.IntegerField(db_column='lIntervalRnR5', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr5 = models.CharField(db_column='sIntervalPeriodRnR5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr5 = models.DateTimeField(db_column='dLastRnR5', blank=True, null=True)  # Field name made lowercase.
    dnextrnr5 = models.DateTimeField(db_column='dNextRnR5', blank=True, null=True)  # Field name made lowercase.
    lalertinterval5 = models.IntegerField(db_column='lAlertInterval5', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate5 = models.DateTimeField(db_column='dtRnRDisplayDate5', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsList_Backup'


class Adminpartdetailsforinstrumentlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lpartnoid = models.IntegerField(db_column='lPartNoID', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.IntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    sinstrumentno = models.CharField(db_column='sInstrumentNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsforInstrumentList'


class Adminpurchasechecklist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=480, blank=True, null=True)  # Field name made lowercase.
    sspecification = models.CharField(db_column='sSpecification', max_length=480, blank=True, null=True)  # Field name made lowercase.
    bok = models.BooleanField(db_column='bOK', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPurchaseCheckList'


class Adminrangelist(models.Model):
    lid = models.AutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminRangeList'


class Adminrolelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    srolename = models.CharField(db_column='sRoleName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminRoleList'


class Adminstoragelocationlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sstoragelocation = models.CharField(db_column='sStorageLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.IntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminStorageLocationList'


class Admintoleranceclasschartlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    ltoneranceclassid = models.IntegerField(db_column='lToneranceClassID', blank=True, null=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbasicsizemin = models.FloatField(db_column='dBasicSizemin', blank=True, null=True)  # Field name made lowercase.
    dbasicsizemax = models.FloatField(db_column='dBasicSizemax', blank=True, null=True)  # Field name made lowercase.
    dtolmax = models.FloatField(db_column='dTolMax', blank=True, null=True)  # Field name made lowercase.
    dtolmin = models.FloatField(db_column='dTolMin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceClassChartList'


class Admintoleranceclasslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceClassList'


class Admintolerancedialgaugelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dtolerance1 = models.FloatField(db_column='dTolerance1', blank=True, null=True)  # Field name made lowercase.
    dtolerance2 = models.FloatField(db_column='dTolerance2', blank=True, null=True)  # Field name made lowercase.
    dtolerance3 = models.FloatField(db_column='dTolerance3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceDialGaugeList'


class Admintoleranceismanufacturingstdchartlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfromdia = models.FloatField(db_column='dFromDia', blank=True, null=True)  # Field name made lowercase.
    dtodia = models.FloatField(db_column='dToDia', blank=True, null=True)  # Field name made lowercase.
    dtolupto = models.FloatField(db_column='dTolUpto', blank=True, null=True)  # Field name made lowercase.
    dhby2 = models.FloatField(db_column='dHBY2', blank=True, null=True)  # Field name made lowercase.
    dy = models.FloatField(db_column='dY', blank=True, null=True)  # Field name made lowercase.
    dz = models.FloatField(db_column='dZ', blank=True, null=True)  # Field name made lowercase.
    da = models.FloatField(db_column='dA', blank=True, null=True)  # Field name made lowercase.
    dh1by2 = models.FloatField(db_column='dH1BY2', blank=True, null=True)  # Field name made lowercase.
    dy1 = models.FloatField(db_column='dY1', blank=True, null=True)  # Field name made lowercase.
    dz1 = models.FloatField(db_column='dZ1', blank=True, null=True)  # Field name made lowercase.
    da1 = models.FloatField(db_column='dA1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceISManufacturingStdChartList'


class Admintolerancepressuregaugelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dtolerance1 = models.FloatField(db_column='dTolerance1', blank=True, null=True)  # Field name made lowercase.
    dtolerance2 = models.FloatField(db_column='dTolerance2', blank=True, null=True)  # Field name made lowercase.
    dtolerance3 = models.FloatField(db_column='dTolerance3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminTolerancePressureGaugeList'


class Admintoleranceradiusgaugelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dtolerance1 = models.FloatField(db_column='dTolerance1', blank=True, null=True)  # Field name made lowercase.
    dtolerance2 = models.FloatField(db_column='dTolerance2', blank=True, null=True)  # Field name made lowercase.
    dtolerance3 = models.FloatField(db_column='dTolerance3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceRadiusGaugeList'


class Admintolerancesettingringlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dtolerance1 = models.FloatField(db_column='dTolerance1', blank=True, null=True)  # Field name made lowercase.
    dtolerance2 = models.FloatField(db_column='dTolerance2', blank=True, null=True)  # Field name made lowercase.
    dtolerance3 = models.FloatField(db_column='dTolerance3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceSettingRingList'


class Admintoleranceslipgaugelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drangefrom = models.FloatField(db_column='dRangeFrom', blank=True, null=True)  # Field name made lowercase.
    drangeto = models.FloatField(db_column='dRangeTo', blank=True, null=True)  # Field name made lowercase.
    dtolerance1 = models.FloatField(db_column='dTolerance1', blank=True, null=True)  # Field name made lowercase.
    dtolerance2 = models.FloatField(db_column='dTolerance2', blank=True, null=True)  # Field name made lowercase.
    dtolerance3 = models.FloatField(db_column='dTolerance3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceSlipGaugeList'


class Adminunitlist(models.Model):
    lplantid = models.AutoField(db_column='lPlantId', primary_key=True)  # Field name made lowercase.
    splantno = models.CharField(db_column='sPlantNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUnitList'


class Adminunitofmeasurelist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sunitofmeasure = models.CharField(db_column='sUnitofMeasure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sshort = models.CharField(db_column='sShort', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUnitofMeasureList'


class Adminuseraccesslist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    luserid = models.IntegerField(db_column='lUserId', blank=True, null=True)  # Field name made lowercase.
    semployeename = models.CharField(db_column='sEmployeeName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    semployeeno = models.CharField(db_column='sEmployeeNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lunitid = models.IntegerField(db_column='lUnitId', blank=True, null=True)  # Field name made lowercase.
    sunitno = models.CharField(db_column='sUnitNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sunitname = models.CharField(db_column='sUnitName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    badmin = models.BooleanField(db_column='bAdmin', blank=True, null=True)  # Field name made lowercase.
    bstores = models.BooleanField(db_column='bStores', blank=True, null=True)  # Field name made lowercase.
    bcalibration = models.BooleanField(db_column='bCalibration', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    bmsa = models.BooleanField(db_column='bMSA', blank=True, null=True)  # Field name made lowercase.
    boperator = models.BooleanField(db_column='bOperator', blank=True, null=True)  # Field name made lowercase.
    breadwrite = models.BooleanField(db_column='bReadWrite', blank=True, null=True)  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly', blank=True, null=True)  # Field name made lowercase.
    bmasterlistonlyallplant = models.BooleanField(db_column='bMasterListOnlyAllPlant', blank=True, null=True)  # Field name made lowercase.
    ballfeatures = models.BooleanField(db_column='bAllFeatures', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUserAccessList'


class Adminuserlist(models.Model):
    luserid = models.AutoField(db_column='lUserId', primary_key=True)  # Field name made lowercase.
    semployeename = models.CharField(db_column='sEmployeeName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    semployeeno = models.CharField(db_column='sEmployeeNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    badmin = models.BooleanField(db_column='bAdmin', blank=True, null=True)  # Field name made lowercase.
    boperator = models.BooleanField(db_column='bOperator', blank=True, null=True)  # Field name made lowercase.
    bmasterlistonlyallplant = models.BooleanField(db_column='bMasterListOnlyAllPlant', blank=True, null=True)  # Field name made lowercase.
    bchangepassword = models.BooleanField(db_column='bChangePassword', blank=True, null=True)  # Field name made lowercase.
    lunitid = models.IntegerField(db_column='lUnitId', blank=True, null=True)  # Field name made lowercase.
    sunitno = models.CharField(db_column='sUnitNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sunitname = models.CharField(db_column='sUnitName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lroleid = models.IntegerField(db_column='lRoleId', blank=True, null=True)  # Field name made lowercase.
    srolename = models.CharField(db_column='sRoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lgradeid = models.IntegerField(db_column='lGradeId', blank=True, null=True)  # Field name made lowercase.
    sgradename = models.CharField(db_column='sGradeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.IntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompanyname = models.CharField(db_column='sCompanyName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    semailaddress = models.CharField(db_column='sEmailAddress', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bmatrix = models.BooleanField(db_column='bMatrix', blank=True, null=True)  # Field name made lowercase.
    lplant1 = models.IntegerField(db_column='lPlant1', blank=True, null=True)  # Field name made lowercase.
    bstores = models.BooleanField(db_column='bStores', blank=True, null=True)  # Field name made lowercase.
    bcalibration = models.BooleanField(db_column='bCalibration', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    bmsa = models.BooleanField(db_column='bMSA', blank=True, null=True)  # Field name made lowercase.
    breadwrite = models.BooleanField(db_column='bReadWrite', blank=True, null=True)  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly', blank=True, null=True)  # Field name made lowercase.
    ballfeatures = models.BooleanField(db_column='bAllFeatures', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.
    lplant11 = models.IntegerField(db_column='lPlant11', blank=True, null=True)  # Field name made lowercase.
    bstores1 = models.BooleanField(db_column='bStores1', blank=True, null=True)  # Field name made lowercase.
    bcalibration1 = models.BooleanField(db_column='bCalibration1', blank=True, null=True)  # Field name made lowercase.
    bservice1 = models.BooleanField(db_column='bService1', blank=True, null=True)  # Field name made lowercase.
    bmsa1 = models.BooleanField(db_column='bMSA1', blank=True, null=True)  # Field name made lowercase.
    breadwrite1 = models.BooleanField(db_column='bReadWrite1', blank=True, null=True)  # Field name made lowercase.
    breadonly1 = models.BooleanField(db_column='bReadOnly1', blank=True, null=True)  # Field name made lowercase.
    ballfeatures1 = models.BooleanField(db_column='bAllFeatures1', blank=True, null=True)  # Field name made lowercase.
    bactive1 = models.BooleanField(db_column='bActive1', blank=True, null=True)  # Field name made lowercase.
    lplant12 = models.IntegerField(db_column='lPlant12', blank=True, null=True)  # Field name made lowercase.
    bstores2 = models.BooleanField(db_column='bStores2', blank=True, null=True)  # Field name made lowercase.
    bcalibration2 = models.BooleanField(db_column='bCalibration2', blank=True, null=True)  # Field name made lowercase.
    bservice2 = models.BooleanField(db_column='bService2', blank=True, null=True)  # Field name made lowercase.
    bmsa2 = models.BooleanField(db_column='bMSA2', blank=True, null=True)  # Field name made lowercase.
    breadwrite2 = models.BooleanField(db_column='bReadWrite2', blank=True, null=True)  # Field name made lowercase.
    breadonly2 = models.BooleanField(db_column='bReadOnly2', blank=True, null=True)  # Field name made lowercase.
    ballfeatures2 = models.BooleanField(db_column='bAllFeatures2', blank=True, null=True)  # Field name made lowercase.
    bactive2 = models.BooleanField(db_column='bActive2', blank=True, null=True)  # Field name made lowercase.
    lplant13 = models.IntegerField(db_column='lPlant13', blank=True, null=True)  # Field name made lowercase.
    bstores3 = models.BooleanField(db_column='bStores3', blank=True, null=True)  # Field name made lowercase.
    bcalibration3 = models.BooleanField(db_column='bCalibration3', blank=True, null=True)  # Field name made lowercase.
    bservice3 = models.BooleanField(db_column='bService3', blank=True, null=True)  # Field name made lowercase.
    bmsa3 = models.BooleanField(db_column='bMSA3', blank=True, null=True)  # Field name made lowercase.
    breadwrite3 = models.BooleanField(db_column='bReadWrite3', blank=True, null=True)  # Field name made lowercase.
    breadonly3 = models.BooleanField(db_column='bReadOnly3', blank=True, null=True)  # Field name made lowercase.
    ballfeatures3 = models.BooleanField(db_column='bAllFeatures3', blank=True, null=True)  # Field name made lowercase.
    bactive3 = models.BooleanField(db_column='bActive3', blank=True, null=True)  # Field name made lowercase.
    lplant14 = models.IntegerField(db_column='lPlant14', blank=True, null=True)  # Field name made lowercase.
    bstores4 = models.BooleanField(db_column='bStores4', blank=True, null=True)  # Field name made lowercase.
    bcalibration4 = models.BooleanField(db_column='bCalibration4', blank=True, null=True)  # Field name made lowercase.
    bservice4 = models.BooleanField(db_column='bService4', blank=True, null=True)  # Field name made lowercase.
    bmsa4 = models.BooleanField(db_column='bMSA4', blank=True, null=True)  # Field name made lowercase.
    breadwrite4 = models.BooleanField(db_column='bReadWrite4', blank=True, null=True)  # Field name made lowercase.
    breadonly4 = models.BooleanField(db_column='bReadOnly4', blank=True, null=True)  # Field name made lowercase.
    ballfeatures4 = models.BooleanField(db_column='bAllFeatures4', blank=True, null=True)  # Field name made lowercase.
    bactive4 = models.BooleanField(db_column='bActive4', blank=True, null=True)  # Field name made lowercase.
    lplant15 = models.IntegerField(db_column='lPlant15', blank=True, null=True)  # Field name made lowercase.
    bstores5 = models.BooleanField(db_column='bStores5', blank=True, null=True)  # Field name made lowercase.
    bcalibration5 = models.BooleanField(db_column='bCalibration5', blank=True, null=True)  # Field name made lowercase.
    bservice5 = models.BooleanField(db_column='bService5', blank=True, null=True)  # Field name made lowercase.
    bmsa5 = models.BooleanField(db_column='bMSA5', blank=True, null=True)  # Field name made lowercase.
    breadwrite5 = models.BooleanField(db_column='bReadWrite5', blank=True, null=True)  # Field name made lowercase.
    breadonly5 = models.BooleanField(db_column='bReadOnly5', blank=True, null=True)  # Field name made lowercase.
    ballfeatures5 = models.BooleanField(db_column='bAllFeatures5', blank=True, null=True)  # Field name made lowercase.
    bactive5 = models.BooleanField(db_column='bActive5', blank=True, null=True)  # Field name made lowercase.
    lplant16 = models.IntegerField(db_column='lPlant16', blank=True, null=True)  # Field name made lowercase.
    bstores6 = models.BooleanField(db_column='bStores6', blank=True, null=True)  # Field name made lowercase.
    bcalibration6 = models.BooleanField(db_column='bCalibration6', blank=True, null=True)  # Field name made lowercase.
    bservice6 = models.BooleanField(db_column='bService6', blank=True, null=True)  # Field name made lowercase.
    bmsa6 = models.BooleanField(db_column='bMSA6', blank=True, null=True)  # Field name made lowercase.
    breadwrite6 = models.BooleanField(db_column='bReadWrite6', blank=True, null=True)  # Field name made lowercase.
    breadonly6 = models.BooleanField(db_column='bReadOnly6', blank=True, null=True)  # Field name made lowercase.
    ballfeatures6 = models.BooleanField(db_column='bAllFeatures6', blank=True, null=True)  # Field name made lowercase.
    bactive6 = models.BooleanField(db_column='bActive6', blank=True, null=True)  # Field name made lowercase.
    lplant17 = models.IntegerField(db_column='lPlant17', blank=True, null=True)  # Field name made lowercase.
    bstores7 = models.BooleanField(db_column='bStores7', blank=True, null=True)  # Field name made lowercase.
    bcalibration7 = models.BooleanField(db_column='bCalibration7', blank=True, null=True)  # Field name made lowercase.
    bservice7 = models.BooleanField(db_column='bService7', blank=True, null=True)  # Field name made lowercase.
    bmsa7 = models.BooleanField(db_column='bMSA7', blank=True, null=True)  # Field name made lowercase.
    breadwrite7 = models.BooleanField(db_column='bReadWrite7', blank=True, null=True)  # Field name made lowercase.
    breadonly7 = models.BooleanField(db_column='bReadOnly7', blank=True, null=True)  # Field name made lowercase.
    ballfeatures7 = models.BooleanField(db_column='bAllFeatures7', blank=True, null=True)  # Field name made lowercase.
    bactive7 = models.BooleanField(db_column='bActive7', blank=True, null=True)  # Field name made lowercase.
    lplant18 = models.IntegerField(db_column='lPlant18', blank=True, null=True)  # Field name made lowercase.
    bstores8 = models.BooleanField(db_column='bStores8', blank=True, null=True)  # Field name made lowercase.
    bcalibration8 = models.BooleanField(db_column='bCalibration8', blank=True, null=True)  # Field name made lowercase.
    bservice8 = models.BooleanField(db_column='bService8', blank=True, null=True)  # Field name made lowercase.
    bmsa8 = models.BooleanField(db_column='bMSA8', blank=True, null=True)  # Field name made lowercase.
    breadwrite8 = models.BooleanField(db_column='bReadWrite8', blank=True, null=True)  # Field name made lowercase.
    breadonly8 = models.BooleanField(db_column='bReadOnly8', blank=True, null=True)  # Field name made lowercase.
    ballfeatures8 = models.BooleanField(db_column='bAllFeatures8', blank=True, null=True)  # Field name made lowercase.
    bactive8 = models.BooleanField(db_column='bActive8', blank=True, null=True)  # Field name made lowercase.
    lplant19 = models.IntegerField(db_column='lPlant19', blank=True, null=True)  # Field name made lowercase.
    bstores9 = models.BooleanField(db_column='bStores9', blank=True, null=True)  # Field name made lowercase.
    bcalibration9 = models.BooleanField(db_column='bCalibration9', blank=True, null=True)  # Field name made lowercase.
    bservice9 = models.BooleanField(db_column='bService9', blank=True, null=True)  # Field name made lowercase.
    bmsa9 = models.BooleanField(db_column='bMSA9', blank=True, null=True)  # Field name made lowercase.
    breadwrite9 = models.BooleanField(db_column='bReadWrite9', blank=True, null=True)  # Field name made lowercase.
    breadonly9 = models.BooleanField(db_column='bReadOnly9', blank=True, null=True)  # Field name made lowercase.
    ballfeatures9 = models.BooleanField(db_column='bAllFeatures9', blank=True, null=True)  # Field name made lowercase.
    bactive9 = models.BooleanField(db_column='bActive9', blank=True, null=True)  # Field name made lowercase.
    lplant110 = models.IntegerField(db_column='lPlant110', blank=True, null=True)  # Field name made lowercase.
    bstores10 = models.BooleanField(db_column='bStores10', blank=True, null=True)  # Field name made lowercase.
    bcalibration10 = models.BooleanField(db_column='bCalibration10', blank=True, null=True)  # Field name made lowercase.
    bservice10 = models.BooleanField(db_column='bService10', blank=True, null=True)  # Field name made lowercase.
    bmsa10 = models.BooleanField(db_column='bMSA10', blank=True, null=True)  # Field name made lowercase.
    breadwrite10 = models.BooleanField(db_column='bReadWrite10', blank=True, null=True)  # Field name made lowercase.
    breadonly10 = models.BooleanField(db_column='bReadOnly10', blank=True, null=True)  # Field name made lowercase.
    ballfeatures10 = models.BooleanField(db_column='bAllFeatures10', blank=True, null=True)  # Field name made lowercase.
    bactive10 = models.BooleanField(db_column='bActive10', blank=True, null=True)  # Field name made lowercase.
    lplant111 = models.IntegerField(db_column='lPlant111', blank=True, null=True)  # Field name made lowercase.
    bstores11 = models.BooleanField(db_column='bStores11', blank=True, null=True)  # Field name made lowercase.
    bcalibration11 = models.BooleanField(db_column='bCalibration11', blank=True, null=True)  # Field name made lowercase.
    bservice11 = models.BooleanField(db_column='bService11', blank=True, null=True)  # Field name made lowercase.
    bmsa11 = models.BooleanField(db_column='bMSA11', blank=True, null=True)  # Field name made lowercase.
    breadwrite11 = models.BooleanField(db_column='bReadWrite11', blank=True, null=True)  # Field name made lowercase.
    breadonly11 = models.BooleanField(db_column='bReadOnly11', blank=True, null=True)  # Field name made lowercase.
    ballfeatures11 = models.BooleanField(db_column='bAllFeatures11', blank=True, null=True)  # Field name made lowercase.
    bactive11 = models.BooleanField(db_column='bActive11', blank=True, null=True)  # Field name made lowercase.
    lplant112 = models.IntegerField(db_column='lPlant112', blank=True, null=True)  # Field name made lowercase.
    bstores12 = models.BooleanField(db_column='bStores12', blank=True, null=True)  # Field name made lowercase.
    bcalibration12 = models.BooleanField(db_column='bCalibration12', blank=True, null=True)  # Field name made lowercase.
    bservice12 = models.BooleanField(db_column='bService12', blank=True, null=True)  # Field name made lowercase.
    bmsa12 = models.BooleanField(db_column='bMSA12', blank=True, null=True)  # Field name made lowercase.
    breadwrite12 = models.BooleanField(db_column='bReadWrite12', blank=True, null=True)  # Field name made lowercase.
    breadonly12 = models.BooleanField(db_column='bReadOnly12', blank=True, null=True)  # Field name made lowercase.
    ballfeatures12 = models.BooleanField(db_column='bAllFeatures12', blank=True, null=True)  # Field name made lowercase.
    bactive12 = models.BooleanField(db_column='bActive12', blank=True, null=True)  # Field name made lowercase.
    lplant113 = models.IntegerField(db_column='lPlant113', blank=True, null=True)  # Field name made lowercase.
    bstores13 = models.BooleanField(db_column='bStores13', blank=True, null=True)  # Field name made lowercase.
    bcalibration13 = models.BooleanField(db_column='bCalibration13', blank=True, null=True)  # Field name made lowercase.
    bservice13 = models.BooleanField(db_column='bService13', blank=True, null=True)  # Field name made lowercase.
    bmsa13 = models.BooleanField(db_column='bMSA13', blank=True, null=True)  # Field name made lowercase.
    breadwrite13 = models.BooleanField(db_column='bReadWrite13', blank=True, null=True)  # Field name made lowercase.
    breadonly13 = models.BooleanField(db_column='bReadOnly13', blank=True, null=True)  # Field name made lowercase.
    ballfeatures13 = models.BooleanField(db_column='bAllFeatures13', blank=True, null=True)  # Field name made lowercase.
    bactive13 = models.BooleanField(db_column='bActive13', blank=True, null=True)  # Field name made lowercase.
    lplant114 = models.IntegerField(db_column='lPlant114', blank=True, null=True)  # Field name made lowercase.
    bstores14 = models.BooleanField(db_column='bStores14', blank=True, null=True)  # Field name made lowercase.
    bcalibration14 = models.BooleanField(db_column='bCalibration14', blank=True, null=True)  # Field name made lowercase.
    bservice14 = models.BooleanField(db_column='bService14', blank=True, null=True)  # Field name made lowercase.
    bmsa14 = models.BooleanField(db_column='bMSA14', blank=True, null=True)  # Field name made lowercase.
    breadwrite14 = models.BooleanField(db_column='bReadWrite14', blank=True, null=True)  # Field name made lowercase.
    breadonly14 = models.BooleanField(db_column='bReadOnly14', blank=True, null=True)  # Field name made lowercase.
    ballfeatures14 = models.BooleanField(db_column='bAllFeatures14', blank=True, null=True)  # Field name made lowercase.
    bactive14 = models.BooleanField(db_column='bActive14', blank=True, null=True)  # Field name made lowercase.
    lplant115 = models.IntegerField(db_column='lPlant115', blank=True, null=True)  # Field name made lowercase.
    bstores15 = models.BooleanField(db_column='bStores15', blank=True, null=True)  # Field name made lowercase.
    bcalibration15 = models.BooleanField(db_column='bCalibration15', blank=True, null=True)  # Field name made lowercase.
    bservice15 = models.BooleanField(db_column='bService15', blank=True, null=True)  # Field name made lowercase.
    bmsa15 = models.BooleanField(db_column='bMSA15', blank=True, null=True)  # Field name made lowercase.
    breadwrite15 = models.BooleanField(db_column='bReadWrite15', blank=True, null=True)  # Field name made lowercase.
    breadonly15 = models.BooleanField(db_column='bReadOnly15', blank=True, null=True)  # Field name made lowercase.
    ballfeatures15 = models.BooleanField(db_column='bAllFeatures15', blank=True, null=True)  # Field name made lowercase.
    bactive15 = models.BooleanField(db_column='bActive15', blank=True, null=True)  # Field name made lowercase.
    lplant116 = models.IntegerField(db_column='lPlant116', blank=True, null=True)  # Field name made lowercase.
    bstores16 = models.BooleanField(db_column='bStores16', blank=True, null=True)  # Field name made lowercase.
    bcalibration16 = models.BooleanField(db_column='bCalibration16', blank=True, null=True)  # Field name made lowercase.
    bservice16 = models.BooleanField(db_column='bService16', blank=True, null=True)  # Field name made lowercase.
    bmsa16 = models.BooleanField(db_column='bMSA16', blank=True, null=True)  # Field name made lowercase.
    breadwrite16 = models.BooleanField(db_column='bReadWrite16', blank=True, null=True)  # Field name made lowercase.
    breadonly16 = models.BooleanField(db_column='bReadOnly16', blank=True, null=True)  # Field name made lowercase.
    ballfeatures16 = models.BooleanField(db_column='bAllFeatures16', blank=True, null=True)  # Field name made lowercase.
    bactive16 = models.BooleanField(db_column='bActive16', blank=True, null=True)  # Field name made lowercase.
    lplant117 = models.IntegerField(db_column='lPlant117', blank=True, null=True)  # Field name made lowercase.
    bstores17 = models.BooleanField(db_column='bStores17', blank=True, null=True)  # Field name made lowercase.
    bcalibration17 = models.BooleanField(db_column='bCalibration17', blank=True, null=True)  # Field name made lowercase.
    bservice17 = models.BooleanField(db_column='bService17', blank=True, null=True)  # Field name made lowercase.
    bmsa17 = models.BooleanField(db_column='bMSA17', blank=True, null=True)  # Field name made lowercase.
    breadwrite17 = models.BooleanField(db_column='bReadWrite17', blank=True, null=True)  # Field name made lowercase.
    breadonly17 = models.BooleanField(db_column='bReadOnly17', blank=True, null=True)  # Field name made lowercase.
    ballfeatures17 = models.BooleanField(db_column='bAllFeatures17', blank=True, null=True)  # Field name made lowercase.
    bactive17 = models.BooleanField(db_column='bActive17', blank=True, null=True)  # Field name made lowercase.
    lplant118 = models.IntegerField(db_column='lPlant118', blank=True, null=True)  # Field name made lowercase.
    bstores18 = models.BooleanField(db_column='bStores18', blank=True, null=True)  # Field name made lowercase.
    bcalibration18 = models.BooleanField(db_column='bCalibration18', blank=True, null=True)  # Field name made lowercase.
    bservice18 = models.BooleanField(db_column='bService18', blank=True, null=True)  # Field name made lowercase.
    bmsa18 = models.BooleanField(db_column='bMSA18', blank=True, null=True)  # Field name made lowercase.
    breadwrite18 = models.BooleanField(db_column='bReadWrite18', blank=True, null=True)  # Field name made lowercase.
    breadonly18 = models.BooleanField(db_column='bReadOnly18', blank=True, null=True)  # Field name made lowercase.
    ballfeatures18 = models.BooleanField(db_column='bAllFeatures18', blank=True, null=True)  # Field name made lowercase.
    bactive18 = models.BooleanField(db_column='bActive18', blank=True, null=True)  # Field name made lowercase.
    lplant119 = models.IntegerField(db_column='lPlant119', blank=True, null=True)  # Field name made lowercase.
    bstores19 = models.BooleanField(db_column='bStores19', blank=True, null=True)  # Field name made lowercase.
    bcalibration19 = models.BooleanField(db_column='bCalibration19', blank=True, null=True)  # Field name made lowercase.
    bservice19 = models.BooleanField(db_column='bService19', blank=True, null=True)  # Field name made lowercase.
    bmsa19 = models.BooleanField(db_column='bMSA19', blank=True, null=True)  # Field name made lowercase.
    breadwrite19 = models.BooleanField(db_column='bReadWrite19', blank=True, null=True)  # Field name made lowercase.
    breadonly19 = models.BooleanField(db_column='bReadOnly19', blank=True, null=True)  # Field name made lowercase.
    ballfeatures19 = models.BooleanField(db_column='bAllFeatures19', blank=True, null=True)  # Field name made lowercase.
    bactive19 = models.BooleanField(db_column='bActive19', blank=True, null=True)  # Field name made lowercase.
    lplant120 = models.IntegerField(db_column='lPlant120', blank=True, null=True)  # Field name made lowercase.
    bstores20 = models.BooleanField(db_column='bStores20', blank=True, null=True)  # Field name made lowercase.
    bcalibration20 = models.BooleanField(db_column='bCalibration20', blank=True, null=True)  # Field name made lowercase.
    bservice20 = models.BooleanField(db_column='bService20', blank=True, null=True)  # Field name made lowercase.
    bmsa20 = models.BooleanField(db_column='bMSA20', blank=True, null=True)  # Field name made lowercase.
    breadwrite20 = models.BooleanField(db_column='bReadWrite20', blank=True, null=True)  # Field name made lowercase.
    breadonly20 = models.BooleanField(db_column='bReadOnly20', blank=True, null=True)  # Field name made lowercase.
    ballfeatures20 = models.BooleanField(db_column='bAllFeatures20', blank=True, null=True)  # Field name made lowercase.
    bactive20 = models.BooleanField(db_column='bActive20', blank=True, null=True)  # Field name made lowercase.
    lplant121 = models.IntegerField(db_column='lPlant121', blank=True, null=True)  # Field name made lowercase.
    bstores21 = models.BooleanField(db_column='bStores21', blank=True, null=True)  # Field name made lowercase.
    bcalibration21 = models.BooleanField(db_column='bCalibration21', blank=True, null=True)  # Field name made lowercase.
    bservice21 = models.BooleanField(db_column='bService21', blank=True, null=True)  # Field name made lowercase.
    bmsa21 = models.BooleanField(db_column='bMSA21', blank=True, null=True)  # Field name made lowercase.
    breadwrite21 = models.BooleanField(db_column='bReadWrite21', blank=True, null=True)  # Field name made lowercase.
    breadonly21 = models.BooleanField(db_column='bReadOnly21', blank=True, null=True)  # Field name made lowercase.
    ballfeatures21 = models.BooleanField(db_column='bAllFeatures21', blank=True, null=True)  # Field name made lowercase.
    bactive21 = models.BooleanField(db_column='bActive21', blank=True, null=True)  # Field name made lowercase.
    lplant122 = models.IntegerField(db_column='lPlant122', blank=True, null=True)  # Field name made lowercase.
    bstores22 = models.BooleanField(db_column='bStores22', blank=True, null=True)  # Field name made lowercase.
    bcalibration22 = models.BooleanField(db_column='bCalibration22', blank=True, null=True)  # Field name made lowercase.
    bservice22 = models.BooleanField(db_column='bService22', blank=True, null=True)  # Field name made lowercase.
    bmsa22 = models.BooleanField(db_column='bMSA22', blank=True, null=True)  # Field name made lowercase.
    breadwrite22 = models.BooleanField(db_column='bReadWrite22', blank=True, null=True)  # Field name made lowercase.
    breadonly22 = models.BooleanField(db_column='bReadOnly22', blank=True, null=True)  # Field name made lowercase.
    ballfeatures22 = models.BooleanField(db_column='bAllFeatures22', blank=True, null=True)  # Field name made lowercase.
    bactive22 = models.BooleanField(db_column='bActive22', blank=True, null=True)  # Field name made lowercase.
    lplant123 = models.IntegerField(db_column='lPlant123', blank=True, null=True)  # Field name made lowercase.
    bstores23 = models.BooleanField(db_column='bStores23', blank=True, null=True)  # Field name made lowercase.
    bcalibration23 = models.BooleanField(db_column='bCalibration23', blank=True, null=True)  # Field name made lowercase.
    bservice23 = models.BooleanField(db_column='bService23', blank=True, null=True)  # Field name made lowercase.
    bmsa23 = models.BooleanField(db_column='bMSA23', blank=True, null=True)  # Field name made lowercase.
    breadwrite23 = models.BooleanField(db_column='bReadWrite23', blank=True, null=True)  # Field name made lowercase.
    breadonly23 = models.BooleanField(db_column='bReadOnly23', blank=True, null=True)  # Field name made lowercase.
    ballfeatures23 = models.BooleanField(db_column='bAllFeatures23', blank=True, null=True)  # Field name made lowercase.
    bactive23 = models.BooleanField(db_column='bActive23', blank=True, null=True)  # Field name made lowercase.
    lplant124 = models.IntegerField(db_column='lPlant124', blank=True, null=True)  # Field name made lowercase.
    bstores24 = models.BooleanField(db_column='bStores24', blank=True, null=True)  # Field name made lowercase.
    bcalibration24 = models.BooleanField(db_column='bCalibration24', blank=True, null=True)  # Field name made lowercase.
    bservice24 = models.BooleanField(db_column='bService24', blank=True, null=True)  # Field name made lowercase.
    bmsa24 = models.BooleanField(db_column='bMSA24', blank=True, null=True)  # Field name made lowercase.
    breadwrite24 = models.BooleanField(db_column='bReadWrite24', blank=True, null=True)  # Field name made lowercase.
    breadonly24 = models.BooleanField(db_column='bReadOnly24', blank=True, null=True)  # Field name made lowercase.
    ballfeatures24 = models.BooleanField(db_column='bAllFeatures24', blank=True, null=True)  # Field name made lowercase.
    bactive24 = models.BooleanField(db_column='bActive24', blank=True, null=True)  # Field name made lowercase.
    lplant125 = models.IntegerField(db_column='lPlant125', blank=True, null=True)  # Field name made lowercase.
    bstores25 = models.BooleanField(db_column='bStores25', blank=True, null=True)  # Field name made lowercase.
    bcalibration25 = models.BooleanField(db_column='bCalibration25', blank=True, null=True)  # Field name made lowercase.
    bservice25 = models.BooleanField(db_column='bService25', blank=True, null=True)  # Field name made lowercase.
    bmsa25 = models.BooleanField(db_column='bMSA25', blank=True, null=True)  # Field name made lowercase.
    breadwrite25 = models.BooleanField(db_column='bReadWrite25', blank=True, null=True)  # Field name made lowercase.
    breadonly25 = models.BooleanField(db_column='bReadOnly25', blank=True, null=True)  # Field name made lowercase.
    ballfeatures25 = models.BooleanField(db_column='bAllFeatures25', blank=True, null=True)  # Field name made lowercase.
    bactive25 = models.BooleanField(db_column='bActive25', blank=True, null=True)  # Field name made lowercase.
    lplant126 = models.IntegerField(db_column='lPlant126', blank=True, null=True)  # Field name made lowercase.
    bstores26 = models.BooleanField(db_column='bStores26', blank=True, null=True)  # Field name made lowercase.
    bcalibration26 = models.BooleanField(db_column='bCalibration26', blank=True, null=True)  # Field name made lowercase.
    bservice26 = models.BooleanField(db_column='bService26', blank=True, null=True)  # Field name made lowercase.
    bmsa26 = models.BooleanField(db_column='bMSA26', blank=True, null=True)  # Field name made lowercase.
    breadwrite26 = models.BooleanField(db_column='bReadWrite26', blank=True, null=True)  # Field name made lowercase.
    breadonly26 = models.BooleanField(db_column='bReadOnly26', blank=True, null=True)  # Field name made lowercase.
    ballfeatures26 = models.BooleanField(db_column='bAllFeatures26', blank=True, null=True)  # Field name made lowercase.
    bactive26 = models.BooleanField(db_column='bActive26', blank=True, null=True)  # Field name made lowercase.
    lplant127 = models.IntegerField(db_column='lPlant127', blank=True, null=True)  # Field name made lowercase.
    bstores27 = models.BooleanField(db_column='bStores27', blank=True, null=True)  # Field name made lowercase.
    bcalibration27 = models.BooleanField(db_column='bCalibration27', blank=True, null=True)  # Field name made lowercase.
    bservice27 = models.BooleanField(db_column='bService27', blank=True, null=True)  # Field name made lowercase.
    bmsa27 = models.BooleanField(db_column='bMSA27', blank=True, null=True)  # Field name made lowercase.
    breadwrite27 = models.BooleanField(db_column='bReadWrite27', blank=True, null=True)  # Field name made lowercase.
    breadonly27 = models.BooleanField(db_column='bReadOnly27', blank=True, null=True)  # Field name made lowercase.
    ballfeatures27 = models.BooleanField(db_column='bAllFeatures27', blank=True, null=True)  # Field name made lowercase.
    bactive27 = models.BooleanField(db_column='bActive27', blank=True, null=True)  # Field name made lowercase.
    lplant128 = models.IntegerField(db_column='lPlant128', blank=True, null=True)  # Field name made lowercase.
    bstores28 = models.BooleanField(db_column='bStores28', blank=True, null=True)  # Field name made lowercase.
    bcalibration28 = models.BooleanField(db_column='bCalibration28', blank=True, null=True)  # Field name made lowercase.
    bservice28 = models.BooleanField(db_column='bService28', blank=True, null=True)  # Field name made lowercase.
    bmsa28 = models.BooleanField(db_column='bMSA28', blank=True, null=True)  # Field name made lowercase.
    breadwrite28 = models.BooleanField(db_column='bReadWrite28', blank=True, null=True)  # Field name made lowercase.
    breadonly28 = models.BooleanField(db_column='bReadOnly28', blank=True, null=True)  # Field name made lowercase.
    ballfeatures28 = models.BooleanField(db_column='bAllFeatures28', blank=True, null=True)  # Field name made lowercase.
    bactive28 = models.BooleanField(db_column='bActive28', blank=True, null=True)  # Field name made lowercase.
    lplant129 = models.IntegerField(db_column='lPlant129', blank=True, null=True)  # Field name made lowercase.
    bstores29 = models.BooleanField(db_column='bStores29', blank=True, null=True)  # Field name made lowercase.
    bcalibration29 = models.BooleanField(db_column='bCalibration29', blank=True, null=True)  # Field name made lowercase.
    bservice29 = models.BooleanField(db_column='bService29', blank=True, null=True)  # Field name made lowercase.
    bmsa29 = models.BooleanField(db_column='bMSA29', blank=True, null=True)  # Field name made lowercase.
    breadwrite29 = models.BooleanField(db_column='bReadWrite29', blank=True, null=True)  # Field name made lowercase.
    breadonly29 = models.BooleanField(db_column='bReadOnly29', blank=True, null=True)  # Field name made lowercase.
    ballfeatures29 = models.BooleanField(db_column='bAllFeatures29', blank=True, null=True)  # Field name made lowercase.
    bactive29 = models.BooleanField(db_column='bActive29', blank=True, null=True)  # Field name made lowercase.
    lplant130 = models.IntegerField(db_column='lPlant130', blank=True, null=True)  # Field name made lowercase.
    bstores30 = models.BooleanField(db_column='bStores30', blank=True, null=True)  # Field name made lowercase.
    bcalibration30 = models.BooleanField(db_column='bCalibration30', blank=True, null=True)  # Field name made lowercase.
    bservice30 = models.BooleanField(db_column='bService30', blank=True, null=True)  # Field name made lowercase.
    bmsa30 = models.BooleanField(db_column='bMSA30', blank=True, null=True)  # Field name made lowercase.
    breadwrite30 = models.BooleanField(db_column='bReadWrite30', blank=True, null=True)  # Field name made lowercase.
    breadonly30 = models.BooleanField(db_column='bReadOnly30', blank=True, null=True)  # Field name made lowercase.
    ballfeatures30 = models.BooleanField(db_column='bAllFeatures30', blank=True, null=True)  # Field name made lowercase.
    bactive30 = models.BooleanField(db_column='bActive30', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUserList'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
