# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Masterinstrumentattachmentslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stypeoffile = models.CharField(db_column='sTypeofFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfile = models.CharField(db_column='sFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentAttachmentsList'


class Masterinstrumentcalibrationmasterslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lcalibrationmasterid = models.BigIntegerField(db_column='lCalibrationMasterId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentCalibrationMastersList'


class Masterinstrumentcalibrationsettingslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    sparameter = models.CharField(db_column='sParameter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
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
    scomment = models.CharField(db_column='sComment', max_length=700, blank=True, null=True)  # Field name made lowercase.
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
    ltoleranceisstd = models.BigIntegerField(db_column='lToleranceISStd', blank=True, null=True)  # Field name made lowercase.
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
    ldegree1 = models.BigIntegerField(db_column='lDegree1', blank=True, null=True)  # Field name made lowercase.
    lmin1 = models.BigIntegerField(db_column='lMin1', blank=True, null=True)  # Field name made lowercase.
    lsec1 = models.BigIntegerField(db_column='lSec1', blank=True, null=True)  # Field name made lowercase.
    ldegree2 = models.BigIntegerField(db_column='lDegree2', blank=True, null=True)  # Field name made lowercase.
    lmin2 = models.BigIntegerField(db_column='lMin2', blank=True, null=True)  # Field name made lowercase.
    lsec2 = models.BigIntegerField(db_column='lSec2', blank=True, null=True)  # Field name made lowercase.
    bimage = models.BooleanField(db_column='bImage', blank=True, null=True)  # Field name made lowercase.
    bdegree = models.BooleanField(db_column='bDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentCalibrationSettingsList'


class Masterinstrumentenvironmentconditionlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scondition1 = models.CharField(db_column='sCondition1', max_length=180, blank=True, null=True)  # Field name made lowercase.
    scondition2 = models.CharField(db_column='sCondition2', max_length=180, blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentEnvironmentConditionList'


class Masterinstrumentpartprojectslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lpartdetailsid = models.BigIntegerField(db_column='lPartDetailsId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPartProjectsList'


class Masterinstrumentpreventivemabigintenancelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    smabigintenancetype = models.CharField(db_column='sMabigintenanceType', max_length=480, blank=True, null=True)  # Field name made lowercase.
    linterval = models.BigIntegerField(db_column='lInterval', blank=True, null=True)  # Field name made lowercase.
    sintervalperiod = models.CharField(db_column='sIntervalPeriod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dtlastmabigintenance = models.DateTimeField(db_column='dtLastMabigintenance', blank=True, null=True)  # Field name made lowercase.
    dtnextmabigintenance = models.DateTimeField(db_column='dtNextMabigintenance', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.BigIntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtservicedisplaydate = models.DateTimeField(db_column='dtServiceDisplayDate', blank=True, null=True)  # Field name made lowercase.
    bverification = models.BooleanField(db_column='bVerification', blank=True, null=True)  # Field name made lowercase.
    bpreventivemabigintenance = models.BooleanField(db_column='bPreventiveMabigintenance', blank=True, null=True)  # Field name made lowercase.
    bconditionbasedmabigintenance = models.BooleanField(db_column='bConditionbasedMabigintenance', blank=True, null=True)  # Field name made lowercase.
    bsystematicmabigintenance = models.BooleanField(db_column='bsystematicMabigintenance', blank=True, null=True)  # Field name made lowercase.
    bpredictivemabigintenance = models.BooleanField(db_column='bPredictiveMabigintenance', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantID', blank=True, null=True)  # Field name made lowercase.
    ssopfile = models.CharField(db_column='sSOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.BigIntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.BigIntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.BigIntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    sagencycalib = models.CharField(db_column='sAgencyCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lvendorid = models.BigIntegerField(db_column='lVendorID', blank=True, null=True)  # Field name made lowercase.
    dnextdisplay = models.DateTimeField(db_column='dNextDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextalert = models.DateTimeField(db_column='dNextAlert', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPreventiveMabigintenanceList'


class Masterinstrumentpurchasechecklist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lpurchasechecklistid = models.BigIntegerField(db_column='lPurchaseChecklistID', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=480, blank=True, null=True)  # Field name made lowercase.
    sspecification = models.CharField(db_column='sSpecification', max_length=480, blank=True, null=True)  # Field name made lowercase.
    bok = models.BooleanField(db_column='bOK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentPurchaseCheckList'


class Masterinstrumentsparepartslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lsparepartdetailsid = models.BigIntegerField(db_column='lSparePartDetailsId', blank=True, null=True)  # Field name made lowercase.
    bstockreqd = models.BooleanField(db_column='bStockReqd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentSparePartsList'


class Masterinstrumentslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=320, blank=True, null=True)  # Field name made lowercase.
    sassettype = models.CharField(db_column='sAssetType', max_length=130, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantID', blank=True, null=True)  # Field name made lowercase.
    splanttype = models.CharField(db_column='sPlantType', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lcategoryid = models.BigIntegerField(db_column='lCategoryID', blank=True, null=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='CategoryType', max_length=120, blank=True, null=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lassetid = models.BigIntegerField(db_column='lAssetID', blank=True, null=True)  # Field name made lowercase.
    btyperef1 = models.BooleanField(db_column='bTypeRef1', blank=True, null=True)  # Field name made lowercase.
    scategorytype1 = models.CharField(db_column='sCategoryType1', max_length=160, blank=True, null=True)  # Field name made lowercase.
    styperefname1 = models.CharField(db_column='sTypeRefName1', max_length=160, blank=True, null=True)  # Field name made lowercase.
    btyperef2 = models.BooleanField(db_column='bTypeRef2', blank=True, null=True)  # Field name made lowercase.
    scategorytype2 = models.CharField(db_column='sCategoryType2', max_length=160, blank=True, null=True)  # Field name made lowercase.
    styperefname2 = models.CharField(db_column='sTypeRefName2', max_length=160, blank=True, null=True)  # Field name made lowercase.
    btyperef3 = models.BooleanField(db_column='bTypeRef3', blank=True, null=True)  # Field name made lowercase.
    scategorytype3 = models.CharField(db_column='sCategoryType3', max_length=160, blank=True, null=True)  # Field name made lowercase.
    styperefname3 = models.CharField(db_column='sTypeRefName3', max_length=160, blank=True, null=True)  # Field name made lowercase.
    btyperef4 = models.BooleanField(db_column='bTypeRef4', blank=True, null=True)  # Field name made lowercase.
    scategorytype4 = models.CharField(db_column='sCategoryType4', max_length=160, blank=True, null=True)  # Field name made lowercase.
    styperefname4 = models.CharField(db_column='sTypeRefName4', max_length=160, blank=True, null=True)  # Field name made lowercase.
    btyperef5 = models.BooleanField(db_column='bTypeRef5', blank=True, null=True)  # Field name made lowercase.
    scategorytype5 = models.CharField(db_column='sCategoryType5', max_length=160, blank=True, null=True)  # Field name made lowercase.
    styperefname5 = models.CharField(db_column='sTypeRefName5', max_length=160, blank=True, null=True)  # Field name made lowercase.
    smake = models.CharField(db_column='sMake', max_length=160, blank=True, null=True)  # Field name made lowercase.
    ldefaultlocationid = models.BigIntegerField(db_column='lDefaultLocationId', blank=True, null=True)  # Field name made lowercase.
    slocationname = models.CharField(db_column='sLocationName', max_length=190, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentstatus', max_length=120, blank=True, null=True)  # Field name made lowercase.
    bcalib = models.BooleanField(db_column='bCalib', blank=True, null=True)  # Field name made lowercase.
    dtlastcalib = models.DateTimeField(db_column='dtLastCalib', blank=True, null=True)  # Field name made lowercase.
    dtnextcalib = models.DateTimeField(db_column='dtNextCalib', blank=True, null=True)  # Field name made lowercase.
    slastcalibdate = models.CharField(db_column='sLastCalibDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibdate = models.CharField(db_column='sNextCalibDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dtcalibdisplaydate = models.DateTimeField(db_column='dtCalibDisplayDate', blank=True, null=True)  # Field name made lowercase.
    ldueday = models.BigIntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.BigIntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.BigIntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    sfreqtype = models.CharField(db_column='sFreqType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busagewise = models.BooleanField(db_column='bUsageWise', blank=True, null=True)  # Field name made lowercase.
    lcalibrationvendorid = models.BigIntegerField(db_column='lCalibrationVendorID', blank=True, null=True)  # Field name made lowercase.
    scalibvendor = models.CharField(db_column='sCalibVendor', max_length=210, blank=True, null=True)  # Field name made lowercase.
    bcheckin = models.BooleanField(db_column='bCheckin', blank=True, null=True)  # Field name made lowercase.
    busage = models.BooleanField(db_column='bUsage', blank=True, null=True)  # Field name made lowercase.
    blimitedusage = models.BooleanField(db_column='bLimitedUsage', blank=True, null=True)  # Field name made lowercase.
    bdamaged = models.BooleanField(db_column='bDamaged', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    bfreezecalib = models.BooleanField(db_column='bFreezeCalib', blank=True, null=True)  # Field name made lowercase.
    bvalidation = models.BooleanField(db_column='bValidation', blank=True, null=True)  # Field name made lowercase.
    bsentforcalibration = models.BooleanField(db_column='bSentForCalibration', blank=True, null=True)  # Field name made lowercase.
    oldinstrument_id = models.CharField(db_column='OLDInstrument_Id', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bpurchaseclosed = models.BooleanField(db_column='bPurchaseClosed', blank=True, null=True)  # Field name made lowercase.
    bidlecalibration = models.BooleanField(db_column='bIdleCalibration', blank=True, null=True)  # Field name made lowercase.
    bsamplepartusage = models.BooleanField(db_column='bSamplePartusage', blank=True, null=True)  # Field name made lowercase.
    bregularpartusage = models.BooleanField(db_column='bRegularPartUsage', blank=True, null=True)  # Field name made lowercase.
    bcalibstandards = models.BooleanField(db_column='bCalibStandards', blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    bplanned = models.BooleanField(db_column='bPlanned', blank=True, null=True)  # Field name made lowercase.
    serpcode = models.CharField(db_column='sERPCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lhistorycard = models.BigIntegerField(db_column='lHistoryCard', blank=True, null=True)  # Field name made lowercase.
    lfolowid1 = models.BigIntegerField(db_column='lFolowID1', blank=True, null=True)  # Field name made lowercase.
    lfolowid2 = models.BigIntegerField(db_column='lFolowID2', blank=True, null=True)  # Field name made lowercase.
    lfolowid3 = models.BigIntegerField(db_column='lFolowID3', blank=True, null=True)  # Field name made lowercase.
    lfolowid4 = models.BigIntegerField(db_column='lFolowID4', blank=True, null=True)  # Field name made lowercase.
    lfolowid5 = models.BigIntegerField(db_column='lFolowID5', blank=True, null=True)  # Field name made lowercase.
    ltolid = models.BigIntegerField(db_column='lTolID', blank=True, null=True)  # Field name made lowercase.
    sissueddate = models.CharField(db_column='sIssuedDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sreturneddate = models.CharField(db_column='sReturnedDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bsapcodegenerate = models.BooleanField(db_column='bSAPCodeGenerate', blank=True, null=True)  # Field name made lowercase.
    bcalibrateidle = models.BooleanField(db_column='bCalibrateIdle', blank=True, null=True)  # Field name made lowercase.
    scalibrationstartdate = models.CharField(db_column='sCalibrationStartDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smsastartdate = models.CharField(db_column='sMSAStartDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    svalidationstartdate = models.CharField(db_column='sValidationStartDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bshowlistascalibrate = models.BooleanField(db_column='bShowListasCalibrate', blank=True, null=True)  # Field name made lowercase.
    sdamagedon = models.CharField(db_column='sDamagedON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smissingon = models.CharField(db_column='sMissingON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sinitiatedon = models.TextField(db_column='sInitiatedOn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spurchaseon = models.TextField(db_column='sPurchaseOn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    breferencegauge = models.IntegerField(db_column='bReferenceGauge', blank=True, null=True)  # Field name made lowercase.
    slimitedcomment = models.TextField(db_column='sLimitedComment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ssize = models.TextField(db_column='sSize', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size = models.TextField(blank=True, null=True)  # This field type is a guess.
    ssizea = models.CharField(db_column='sSizeA', max_length=120, blank=True, null=True)  # Field name made lowercase.
    sissuedto = models.CharField(db_column='sIssuedTo', max_length=140, blank=True, null=True)  # Field name made lowercase.
    sissuedmachineto = models.CharField(db_column='sIssuedMachineTo', max_length=140, blank=True, null=True)  # Field name made lowercase.
    sissuedpartno = models.CharField(db_column='sIssuedPartNo', max_length=140, blank=True, null=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=300, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    scalibcertificatfile = models.CharField(db_column='sCalibCertificatFile', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lhistoryid = models.IntegerField(db_column='lHistoryID', blank=True, null=True)  # Field name made lowercase.
    sstoragelocation = models.CharField(db_column='sStorageLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lrepairid = models.BigIntegerField(db_column='lRepairID', blank=True, null=True)  # Field name made lowercase.
    bunderrepair = models.BooleanField(db_column='bUnderRepair', blank=True, null=True)  # Field name made lowercase.
    lvalibationid = models.BigIntegerField(db_column='lValibationID', blank=True, null=True)  # Field name made lowercase.
    bundervalidation = models.BooleanField(db_column='bUnderValidation', blank=True, null=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    bunder8d = models.BooleanField(db_column='bUnder8D', blank=True, null=True)  # Field name made lowercase.
    lmsarnrid = models.BigIntegerField(db_column='lMSARnRID', blank=True, null=True)  # Field name made lowercase.
    bunderrnr = models.BooleanField(db_column='bUnderRnR', blank=True, null=True)  # Field name made lowercase.
    bunderattribute = models.BooleanField(db_column='bUnderAttribute', blank=True, null=True)  # Field name made lowercase.
    lstabilityid = models.BigIntegerField(db_column='lStabilityID', blank=True, null=True)  # Field name made lowercase.
    bunderstability = models.BooleanField(db_column='bUnderStability', blank=True, null=True)  # Field name made lowercase.
    lbiasid = models.BigIntegerField(db_column='lBiasID', blank=True, null=True)  # Field name made lowercase.
    bunderbias = models.BooleanField(db_column='bUnderBias', blank=True, null=True)  # Field name made lowercase.
    llinearityid = models.BigIntegerField(db_column='lLinearityID', blank=True, null=True)  # Field name made lowercase.
    bunderlinearity = models.BooleanField(db_column='bUnderLinearity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentsList'


class Masterinstrumentslistpart2(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    sstoragerack = models.CharField(db_column='sStorageRack', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingno = models.CharField(db_column='sDrawingNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingrevno = models.CharField(db_column='sDrawingRevNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdrawingfile = models.CharField(db_column='sDrawingFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sunitofmeasure = models.CharField(db_column='sUnitofMeasure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    srevisionno = models.CharField(db_column='sRevisionNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sproperty = models.CharField(db_column='sProperty', max_length=1, blank=True, null=True)  # Field name made lowercase.
    scatalogueno = models.CharField(db_column='sCatalogueNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frangefrom = models.FloatField(db_column='fRangeFrom', blank=True, null=True)  # Field name made lowercase.
    frangeto = models.FloatField(db_column='fRangeTo', blank=True, null=True)  # Field name made lowercase.
    fleastcount = models.FloatField(db_column='fLeastCount', blank=True, null=True)  # Field name made lowercase.
    scheckmethod = models.CharField(db_column='sCheckMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtlastservice = models.DateTimeField(db_column='dtLastService', blank=True, null=True)  # Field name made lowercase.
    dtnextservice = models.DateTimeField(db_column='dtNextService', blank=True, null=True)  # Field name made lowercase.
    slastservicedate = models.CharField(db_column='sLastServiceDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextservicedate = models.CharField(db_column='sNextServiceDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    smanualduernr = models.CharField(db_column='sManualDueRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ldayremainrnr = models.BigIntegerField(db_column='lDayRemainRnR', blank=True, null=True)  # Field name made lowercase.
    dtlastrnr = models.DateTimeField(db_column='dtLastRnR', blank=True, null=True)  # Field name made lowercase.
    dtnextrnr = models.DateTimeField(db_column='dtNextRnR', blank=True, null=True)  # Field name made lowercase.
    slastrnrdate = models.CharField(db_column='sLastRnRDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextrnrdate = models.CharField(db_column='sNextRnRDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frange3 = models.FloatField(db_column='fRange3', blank=True, null=True)  # Field name made lowercase.
    dcalibrationcost = models.FloatField(db_column='dCalibrationCost', blank=True, null=True)  # Field name made lowercase.
    dpurchaseprice = models.FloatField(db_column='dPurchasePrice', blank=True, null=True)  # Field name made lowercase.
    smodelno = models.CharField(db_column='sModelNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sserialno = models.CharField(db_column='sSerialNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saccuracy = models.CharField(db_column='sAccuracy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ssize1 = models.CharField(db_column='sSize1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    llusagedefault = models.BigIntegerField(db_column='llUsageDefault', blank=True, null=True)  # Field name made lowercase.
    llusagecount = models.BigIntegerField(db_column='llUsageCount', blank=True, null=True)  # Field name made lowercase.
    smounted = models.CharField(db_column='sMounted', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fproducttolerance = models.FloatField(db_column='fProductTolerance', blank=True, null=True)  # Field name made lowercase.
    sproducttolerance = models.CharField(db_column='sProductTolerance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facconstant = models.FloatField(db_column='fACConstant', blank=True, null=True)  # Field name made lowercase.
    sagencyservice = models.CharField(db_column='sAgencyService', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sprocuredate = models.CharField(db_column='sProcureDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brejected = models.BooleanField(db_column='bRejected', blank=True, null=True)  # Field name made lowercase.
    srejecteddate = models.CharField(db_column='sRejectedDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    breplaced = models.BooleanField(db_column='bReplaced', blank=True, null=True)  # Field name made lowercase.
    lreplacedinstrumentid = models.BigIntegerField(db_column='lReplacedInstrumentId', blank=True, null=True)  # Field name made lowercase.
    bduechanged = models.BooleanField(db_column='bDueChanged', blank=True, null=True)  # Field name made lowercase.
    dtduechangedate = models.DateTimeField(db_column='dtDueChangeDate', blank=True, null=True)  # Field name made lowercase.
    slastchangedate = models.CharField(db_column='sLastChangeDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    blanova = models.BooleanField(db_column='blAnova', blank=True, null=True)  # Field name made lowercase.
    srevno = models.CharField(db_column='sRevNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scommentchangecalibstd = models.CharField(db_column='sCommentChangeCalibStd', max_length=700, blank=True, null=True)  # Field name made lowercase.
    bverifyforpurchase = models.BooleanField(db_column='bVerifyForPurchase', blank=True, null=True)  # Field name made lowercase.
    dtsendforverificationforpurchaseon = models.DateTimeField(db_column='dtSendForVerificationForPurchaseOn', blank=True, null=True)  # Field name made lowercase.
    dtverifiedforpurchaseon = models.DateTimeField(db_column='dtVerifiedForPurchaseOn', blank=True, null=True)  # Field name made lowercase.
    ssendforverificationforpurchaseon = models.CharField(db_column='sSendForVerificationForPurchaseOn', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sverifiedforpurchaseon = models.CharField(db_column='sVerifiedForPurchaseOn', max_length=25, blank=True, null=True)  # Field name made lowercase.
    spreferredvendor = models.CharField(db_column='sPreferredVendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sbondnumber = models.CharField(db_column='sBondNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dgo = models.FloatField(db_column='dGO', blank=True, null=True)  # Field name made lowercase.
    dnogo = models.FloatField(db_column='dNOGO', blank=True, null=True)  # Field name made lowercase.
    dtoldiff = models.FloatField(db_column='dTolDiff', blank=True, null=True)  # Field name made lowercase.
    dtolallowed = models.FloatField(db_column='dTolAllowed', blank=True, null=True)  # Field name made lowercase.
    bmanufacturingstd = models.BooleanField(db_column='bManufacturingSTD', blank=True, null=True)  # Field name made lowercase.
    dplusofminus = models.FloatField(db_column='dPlusofminus', blank=True, null=True)  # Field name made lowercase.
    dz = models.FloatField(db_column='dZ', blank=True, null=True)  # Field name made lowercase.
    bpartno = models.BooleanField(db_column='bPartNo', blank=True, null=True)  # Field name made lowercase.
    gageserialno = models.CharField(db_column='GageSerialNo', max_length=320, blank=True, null=True)  # Field name made lowercase.
    sdrawingno2 = models.CharField(db_column='sDrawingNo2', max_length=320, blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa2 = models.BigIntegerField(db_column='lContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob2 = models.BigIntegerField(db_column='lContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.BigIntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.BigIntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    bcustomer = models.BooleanField(db_column='bCustomer', blank=True, null=True)  # Field name made lowercase.
    lservicealert = models.BigIntegerField(db_column='lServiceAlert', blank=True, null=True)  # Field name made lowercase.
    ferrorallowed = models.FloatField(db_column='fErrorAllowed', blank=True, null=True)  # Field name made lowercase.
    splannedby = models.CharField(db_column='sPlannedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bidchanged = models.BooleanField(db_column='bIDChanged', blank=True, null=True)  # Field name made lowercase.
    scode1 = models.CharField(db_column='sCode1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode2 = models.CharField(db_column='sCode2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode3 = models.CharField(db_column='sCode3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode4 = models.CharField(db_column='sCode4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode5 = models.CharField(db_column='sCode5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ssstatus = models.CharField(db_column='sSstatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ssize = models.CharField(db_column='sSize', max_length=160, blank=True, null=True)  # Field name made lowercase.
    lintervalservice = models.BigIntegerField(db_column='lIntervalService', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodservice = models.CharField(db_column='sIntervalPeriodService', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smanufacturer = models.CharField(db_column='sManufacturer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddateofprocure = models.DateTimeField(db_column='dDateofProcure', blank=True, null=True)  # Field name made lowercase.
    sdateofprocure = models.CharField(db_column='sDateofProcure', max_length=25, blank=True, null=True)  # Field name made lowercase.
    soperation = models.CharField(db_column='sOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=320, blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa1 = models.BigIntegerField(db_column='lContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob1 = models.BigIntegerField(db_column='lContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.BigIntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.BigIntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    btyperef = models.BooleanField(db_column='bTypeRef', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=700, blank=True, null=True)  # Field name made lowercase.
    lpurchasevendorid = models.BigIntegerField(db_column='lPurchaseVendorId', blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.BigIntegerField(db_column='lServiceVendorId', blank=True, null=True)  # Field name made lowercase.
    sagencycalib = models.CharField(db_column='sAgencyCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcurrentlocationid = models.BigIntegerField(db_column='lCurrentLocationId', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    lcalibalert = models.BigIntegerField(db_column='lCalibAlert', blank=True, null=True)  # Field name made lowercase.
    lintervalcalib = models.BigIntegerField(db_column='lIntervalCalib', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodcalib = models.CharField(db_column='sIntervalPeriodCalib', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.BigIntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    ldayremaincalib = models.BigIntegerField(db_column='lDayRemainCalib', blank=True, null=True)  # Field name made lowercase.
    lusageinterval = models.BigIntegerField(db_column='lUsageInterval', blank=True, null=True)  # Field name made lowercase.
    lusageintervaldisplay = models.BigIntegerField(db_column='lUsageIntervalDisplay', blank=True, null=True)  # Field name made lowercase.
    lusagecurrent = models.BigIntegerField(db_column='lUsageCurrent', blank=True, null=True)  # Field name made lowercase.
    lidlecalibfrequency = models.BigIntegerField(db_column='LIdleCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    dtplanneddate = models.DateTimeField(db_column='dtPlannedDate', blank=True, null=True)  # Field name made lowercase.
    splanneddate = models.CharField(db_column='sPlannedDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dtvalidationlastdate = models.DateTimeField(db_column='dtValidationLastDate', blank=True, null=True)  # Field name made lowercase.
    svalidationlastdate = models.CharField(db_column='sValidationLastDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dtvalidationnextdate = models.DateTimeField(db_column='dtValidationNextDate', blank=True, null=True)  # Field name made lowercase.
    svalidationnextdate = models.CharField(db_column='sValidationNextDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    schangeoldid = models.CharField(db_column='sChangeOLDID', max_length=340, blank=True, null=True)  # Field name made lowercase.
    llusagecountalerts = models.BigIntegerField(db_column='llUsageCountAlerts', blank=True, null=True)  # Field name made lowercase.
    btnextidlecalibration = models.DateTimeField(db_column='btNextIdleCalibration', blank=True, null=True)  # Field name made lowercase.
    snextidlecalibration = models.CharField(db_column='sNextIdleCalibration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dtidleon = models.DateTimeField(db_column='dtIdleOn', blank=True, null=True)  # Field name made lowercase.
    sidleon = models.CharField(db_column='sIdleOn', max_length=25, blank=True, null=True)  # Field name made lowercase.
    b1monthvalidation = models.BooleanField(db_column='b1MonthValidation', blank=True, null=True)  # Field name made lowercase.
    dtnextvalidation = models.DateTimeField(db_column='dtNextValidation', blank=True, null=True)  # Field name made lowercase.
    snextvalidation = models.CharField(db_column='sNextValidation', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dtlastvalidation = models.DateTimeField(db_column='dtlastValidation', blank=True, null=True)  # Field name made lowercase.
    slastvalidation = models.CharField(db_column='slastValidation', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentsListPart2'


class Masterinstrumentslistpart3(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid1 = models.BigIntegerField(db_column='lMasterInstrumentID1', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid1 = models.TextField(db_column='sMasterInstrumentId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription1 = models.TextField(db_column='sMasterDescription1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate1 = models.CharField(db_column='sLastCalibrationDate1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate1 = models.CharField(db_column='sNextCalibrationDate1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid2 = models.BigIntegerField(db_column='lMasterInstrumentID2', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid2 = models.TextField(db_column='sMasterInstrumentId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription2 = models.TextField(db_column='sMasterDescription2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate2 = models.CharField(db_column='sLastCalibrationDate2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate2 = models.CharField(db_column='sNextCalibrationDate2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid3 = models.BigIntegerField(db_column='lMasterInstrumentID3', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid3 = models.TextField(db_column='sMasterInstrumentId3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription3 = models.TextField(db_column='sMasterDescription3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate3 = models.CharField(db_column='sLastCalibrationDate3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate3 = models.CharField(db_column='sNextCalibrationDate3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid4 = models.BigIntegerField(db_column='lMasterInstrumentID4', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid4 = models.TextField(db_column='sMasterInstrumentId4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription4 = models.TextField(db_column='sMasterDescription4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate4 = models.CharField(db_column='sLastCalibrationDate4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate4 = models.CharField(db_column='sNextCalibrationDate4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid5 = models.BigIntegerField(db_column='lMasterInstrumentID5', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid5 = models.TextField(db_column='sMasterInstrumentId5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription5 = models.TextField(db_column='sMasterDescription5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate5 = models.CharField(db_column='sLastCalibrationDate5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate5 = models.CharField(db_column='sNextCalibrationDate5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    stypeoffile1 = models.TextField(db_column='sTypeofFile1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile1 = models.TextField(db_column='sFile1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile2 = models.TextField(db_column='sTypeofFile2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile2 = models.TextField(db_column='sFile2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile3 = models.TextField(db_column='sTypeofFile3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile3 = models.TextField(db_column='sFile3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile4 = models.TextField(db_column='sTypeofFile4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile4 = models.TextField(db_column='sFile4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile5 = models.TextField(db_column='sTypeofFile5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile5 = models.TextField(db_column='sFile5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    suom1 = models.TextField(db_column='sUOM1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue1 = models.TextField(db_column='sAppliedValue1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea1 = models.FloatField(db_column='fAppliedValueA1', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb1 = models.FloatField(db_column='fAppliedValueB1', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec1 = models.FloatField(db_column='fAppliedValueC1', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued1 = models.FloatField(db_column='fAppliedValueD1', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee1 = models.FloatField(db_column='fAppliedValueE1', blank=True, null=True)  # Field name made lowercase.
    derrorallowed1 = models.FloatField(db_column='dErrorAllowed1', blank=True, null=True)  # Field name made lowercase.
    dmax1 = models.FloatField(db_column='dMax1', blank=True, null=True)  # Field name made lowercase.
    dmin1 = models.FloatField(db_column='dMin1', blank=True, null=True)  # Field name made lowercase.
    suom2 = models.TextField(db_column='sUOM2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue2 = models.TextField(db_column='sAppliedValue2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea2 = models.FloatField(db_column='fAppliedValueA2', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb2 = models.FloatField(db_column='fAppliedValueB2', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec2 = models.FloatField(db_column='fAppliedValueC2', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued2 = models.FloatField(db_column='fAppliedValueD2', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee2 = models.FloatField(db_column='fAppliedValueE2', blank=True, null=True)  # Field name made lowercase.
    derrorallowed2 = models.FloatField(db_column='dErrorAllowed2', blank=True, null=True)  # Field name made lowercase.
    dmax2 = models.FloatField(db_column='dMax2', blank=True, null=True)  # Field name made lowercase.
    dmin2 = models.FloatField(db_column='dMin2', blank=True, null=True)  # Field name made lowercase.
    suom3 = models.TextField(db_column='sUOM3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue3 = models.TextField(db_column='sAppliedValue3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea3 = models.FloatField(db_column='fAppliedValueA3', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb3 = models.FloatField(db_column='fAppliedValueB3', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec3 = models.FloatField(db_column='fAppliedValueC3', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued3 = models.FloatField(db_column='fAppliedValueD3', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee3 = models.FloatField(db_column='fAppliedValueE3', blank=True, null=True)  # Field name made lowercase.
    derrorallowed3 = models.FloatField(db_column='dErrorAllowed3', blank=True, null=True)  # Field name made lowercase.
    dmax3 = models.FloatField(db_column='dMax3', blank=True, null=True)  # Field name made lowercase.
    dmin3 = models.FloatField(db_column='dMin3', blank=True, null=True)  # Field name made lowercase.
    suom4 = models.TextField(db_column='sUOM4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue4 = models.TextField(db_column='sAppliedValue4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea4 = models.FloatField(db_column='fAppliedValueA4', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb4 = models.FloatField(db_column='fAppliedValueB4', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec4 = models.FloatField(db_column='fAppliedValueC4', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued4 = models.FloatField(db_column='fAppliedValueD4', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee4 = models.FloatField(db_column='fAppliedValueE4', blank=True, null=True)  # Field name made lowercase.
    derrorallowed4 = models.FloatField(db_column='dErrorAllowed4', blank=True, null=True)  # Field name made lowercase.
    dmax4 = models.FloatField(db_column='dMax4', blank=True, null=True)  # Field name made lowercase.
    dmin4 = models.FloatField(db_column='dMin4', blank=True, null=True)  # Field name made lowercase.
    suom5 = models.TextField(db_column='sUOM5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue5 = models.TextField(db_column='sAppliedValue5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea5 = models.FloatField(db_column='fAppliedValueA5', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb5 = models.FloatField(db_column='fAppliedValueB5', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec5 = models.FloatField(db_column='fAppliedValueC5', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued5 = models.FloatField(db_column='fAppliedValueD5', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee5 = models.FloatField(db_column='fAppliedValueE5', blank=True, null=True)  # Field name made lowercase.
    derrorallowed5 = models.FloatField(db_column='dErrorAllowed5', blank=True, null=True)  # Field name made lowercase.
    dmax5 = models.FloatField(db_column='dMax5', blank=True, null=True)  # Field name made lowercase.
    dmin5 = models.FloatField(db_column='dMin5', blank=True, null=True)  # Field name made lowercase.
    suom6 = models.TextField(db_column='sUOM6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue6 = models.TextField(db_column='sAppliedValue6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea6 = models.FloatField(db_column='fAppliedValueA6', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb6 = models.FloatField(db_column='fAppliedValueB6', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec6 = models.FloatField(db_column='fAppliedValueC6', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued6 = models.FloatField(db_column='fAppliedValueD6', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee6 = models.FloatField(db_column='fAppliedValueE6', blank=True, null=True)  # Field name made lowercase.
    derrorallowed6 = models.FloatField(db_column='dErrorAllowed6', blank=True, null=True)  # Field name made lowercase.
    dmax6 = models.FloatField(db_column='dMax6', blank=True, null=True)  # Field name made lowercase.
    dmin6 = models.FloatField(db_column='dMin6', blank=True, null=True)  # Field name made lowercase.
    suom7 = models.TextField(db_column='sUOM7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue7 = models.TextField(db_column='sAppliedValue7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea7 = models.FloatField(db_column='fAppliedValueA7', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb7 = models.FloatField(db_column='fAppliedValueB7', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec7 = models.FloatField(db_column='fAppliedValueC7', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued7 = models.FloatField(db_column='fAppliedValueD7', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee7 = models.FloatField(db_column='fAppliedValueE7', blank=True, null=True)  # Field name made lowercase.
    derrorallowed7 = models.FloatField(db_column='dErrorAllowed7', blank=True, null=True)  # Field name made lowercase.
    dmax7 = models.FloatField(db_column='dMax7', blank=True, null=True)  # Field name made lowercase.
    dmin7 = models.FloatField(db_column='dMin7', blank=True, null=True)  # Field name made lowercase.
    suom8 = models.TextField(db_column='sUOM8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue8 = models.TextField(db_column='sAppliedValue8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea8 = models.FloatField(db_column='fAppliedValueA8', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb8 = models.FloatField(db_column='fAppliedValueB8', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec8 = models.FloatField(db_column='fAppliedValueC8', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued8 = models.FloatField(db_column='fAppliedValueD8', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee8 = models.FloatField(db_column='fAppliedValueE8', blank=True, null=True)  # Field name made lowercase.
    derrorallowed8 = models.FloatField(db_column='dErrorAllowed8', blank=True, null=True)  # Field name made lowercase.
    dmax8 = models.FloatField(db_column='dMax8', blank=True, null=True)  # Field name made lowercase.
    dmin8 = models.FloatField(db_column='dMin8', blank=True, null=True)  # Field name made lowercase.
    suom9 = models.TextField(db_column='sUOM9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue9 = models.TextField(db_column='sAppliedValue9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea9 = models.FloatField(db_column='fAppliedValueA9', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb9 = models.FloatField(db_column='fAppliedValueB9', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec9 = models.FloatField(db_column='fAppliedValueC9', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued9 = models.FloatField(db_column='fAppliedValueD9', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee9 = models.FloatField(db_column='fAppliedValueE9', blank=True, null=True)  # Field name made lowercase.
    derrorallowed9 = models.FloatField(db_column='dErrorAllowed9', blank=True, null=True)  # Field name made lowercase.
    dmax9 = models.FloatField(db_column='dMax9', blank=True, null=True)  # Field name made lowercase.
    dmin9 = models.FloatField(db_column='dMin9', blank=True, null=True)  # Field name made lowercase.
    suom10 = models.TextField(db_column='sUOM10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue10 = models.TextField(db_column='sAppliedValue10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea10 = models.FloatField(db_column='fAppliedValueA10', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb10 = models.FloatField(db_column='fAppliedValueB10', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec10 = models.FloatField(db_column='fAppliedValueC10', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued10 = models.FloatField(db_column='fAppliedValueD10', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee10 = models.FloatField(db_column='fAppliedValueE10', blank=True, null=True)  # Field name made lowercase.
    derrorallowed10 = models.FloatField(db_column='dErrorAllowed10', blank=True, null=True)  # Field name made lowercase.
    dmax10 = models.FloatField(db_column='dMax10', blank=True, null=True)  # Field name made lowercase.
    dmin10 = models.FloatField(db_column='dMin10', blank=True, null=True)  # Field name made lowercase.
    suom11 = models.TextField(db_column='sUOM11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue11 = models.TextField(db_column='sAppliedValue11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea11 = models.FloatField(db_column='fAppliedValueA11', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb11 = models.FloatField(db_column='fAppliedValueB11', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec11 = models.FloatField(db_column='fAppliedValueC11', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued11 = models.FloatField(db_column='fAppliedValueD11', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee11 = models.FloatField(db_column='fAppliedValueE11', blank=True, null=True)  # Field name made lowercase.
    derrorallowed11 = models.FloatField(db_column='dErrorAllowed11', blank=True, null=True)  # Field name made lowercase.
    dmax11 = models.FloatField(db_column='dMax11', blank=True, null=True)  # Field name made lowercase.
    dmin11 = models.FloatField(db_column='dMin11', blank=True, null=True)  # Field name made lowercase.
    suom12 = models.TextField(db_column='sUOM12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue12 = models.TextField(db_column='sAppliedValue12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea12 = models.FloatField(db_column='fAppliedValueA12', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb12 = models.FloatField(db_column='fAppliedValueB12', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec12 = models.FloatField(db_column='fAppliedValueC12', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued12 = models.FloatField(db_column='fAppliedValueD12', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee12 = models.FloatField(db_column='fAppliedValueE12', blank=True, null=True)  # Field name made lowercase.
    derrorallowed12 = models.FloatField(db_column='dErrorAllowed12', blank=True, null=True)  # Field name made lowercase.
    dmax12 = models.FloatField(db_column='dMax12', blank=True, null=True)  # Field name made lowercase.
    dmin12 = models.FloatField(db_column='dMin12', blank=True, null=True)  # Field name made lowercase.
    suom13 = models.TextField(db_column='sUOM13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue13 = models.TextField(db_column='sAppliedValue13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea13 = models.FloatField(db_column='fAppliedValueA13', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb13 = models.FloatField(db_column='fAppliedValueB13', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec13 = models.FloatField(db_column='fAppliedValueC13', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued13 = models.FloatField(db_column='fAppliedValueD13', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee13 = models.FloatField(db_column='fAppliedValueE13', blank=True, null=True)  # Field name made lowercase.
    derrorallowed13 = models.FloatField(db_column='dErrorAllowed13', blank=True, null=True)  # Field name made lowercase.
    dmax13 = models.FloatField(db_column='dMax13', blank=True, null=True)  # Field name made lowercase.
    dmin13 = models.FloatField(db_column='dMin13', blank=True, null=True)  # Field name made lowercase.
    suom14 = models.TextField(db_column='sUOM14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue14 = models.TextField(db_column='sAppliedValue14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea14 = models.FloatField(db_column='fAppliedValueA14', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb14 = models.FloatField(db_column='fAppliedValueB14', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec14 = models.FloatField(db_column='fAppliedValueC14', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued14 = models.FloatField(db_column='fAppliedValueD14', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee14 = models.FloatField(db_column='fAppliedValueE14', blank=True, null=True)  # Field name made lowercase.
    derrorallowed14 = models.FloatField(db_column='dErrorAllowed14', blank=True, null=True)  # Field name made lowercase.
    dmax14 = models.FloatField(db_column='dMax14', blank=True, null=True)  # Field name made lowercase.
    dmin14 = models.FloatField(db_column='dMin14', blank=True, null=True)  # Field name made lowercase.
    suom15 = models.TextField(db_column='sUOM15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue15 = models.TextField(db_column='sAppliedValue15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea15 = models.FloatField(db_column='fAppliedValueA15', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb15 = models.FloatField(db_column='fAppliedValueB15', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec15 = models.FloatField(db_column='fAppliedValueC15', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued15 = models.FloatField(db_column='fAppliedValueD15', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee15 = models.FloatField(db_column='fAppliedValueE15', blank=True, null=True)  # Field name made lowercase.
    derrorallowed15 = models.FloatField(db_column='dErrorAllowed15', blank=True, null=True)  # Field name made lowercase.
    dmax15 = models.FloatField(db_column='dMax15', blank=True, null=True)  # Field name made lowercase.
    dmin15 = models.FloatField(db_column='dMin15', blank=True, null=True)  # Field name made lowercase.
    suom16 = models.TextField(db_column='sUOM16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue16 = models.TextField(db_column='sAppliedValue16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea16 = models.FloatField(db_column='fAppliedValueA16', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb16 = models.FloatField(db_column='fAppliedValueB16', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec16 = models.FloatField(db_column='fAppliedValueC16', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued16 = models.FloatField(db_column='fAppliedValueD16', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee16 = models.FloatField(db_column='fAppliedValueE16', blank=True, null=True)  # Field name made lowercase.
    derrorallowed16 = models.FloatField(db_column='dErrorAllowed16', blank=True, null=True)  # Field name made lowercase.
    dmax16 = models.FloatField(db_column='dMax16', blank=True, null=True)  # Field name made lowercase.
    dmin16 = models.FloatField(db_column='dMin16', blank=True, null=True)  # Field name made lowercase.
    suom17 = models.TextField(db_column='sUOM17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue17 = models.TextField(db_column='sAppliedValue17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea17 = models.FloatField(db_column='fAppliedValueA17', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb17 = models.FloatField(db_column='fAppliedValueB17', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec17 = models.FloatField(db_column='fAppliedValueC17', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued17 = models.FloatField(db_column='fAppliedValueD17', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee17 = models.FloatField(db_column='fAppliedValueE17', blank=True, null=True)  # Field name made lowercase.
    derrorallowed17 = models.FloatField(db_column='dErrorAllowed17', blank=True, null=True)  # Field name made lowercase.
    dmax17 = models.FloatField(db_column='dMax17', blank=True, null=True)  # Field name made lowercase.
    dmin17 = models.FloatField(db_column='dMin17', blank=True, null=True)  # Field name made lowercase.
    suom18 = models.TextField(db_column='sUOM18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue18 = models.TextField(db_column='sAppliedValue18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea18 = models.FloatField(db_column='fAppliedValueA18', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb18 = models.FloatField(db_column='fAppliedValueB18', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec18 = models.FloatField(db_column='fAppliedValueC18', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued18 = models.FloatField(db_column='fAppliedValueD18', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee18 = models.FloatField(db_column='fAppliedValueE18', blank=True, null=True)  # Field name made lowercase.
    derrorallowed18 = models.FloatField(db_column='dErrorAllowed18', blank=True, null=True)  # Field name made lowercase.
    dmax18 = models.FloatField(db_column='dMax18', blank=True, null=True)  # Field name made lowercase.
    dmin18 = models.FloatField(db_column='dMin18', blank=True, null=True)  # Field name made lowercase.
    suom19 = models.TextField(db_column='sUOM19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue19 = models.TextField(db_column='sAppliedValue19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea19 = models.FloatField(db_column='fAppliedValueA19', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb19 = models.FloatField(db_column='fAppliedValueB19', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec19 = models.FloatField(db_column='fAppliedValueC19', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued19 = models.FloatField(db_column='fAppliedValueD19', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee19 = models.FloatField(db_column='fAppliedValueE19', blank=True, null=True)  # Field name made lowercase.
    derrorallowed19 = models.FloatField(db_column='dErrorAllowed19', blank=True, null=True)  # Field name made lowercase.
    dmax19 = models.FloatField(db_column='dMax19', blank=True, null=True)  # Field name made lowercase.
    dmin19 = models.FloatField(db_column='dMin19', blank=True, null=True)  # Field name made lowercase.
    suom20 = models.TextField(db_column='sUOM20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue20 = models.TextField(db_column='sAppliedValue20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea20 = models.FloatField(db_column='fAppliedValueA20', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb20 = models.FloatField(db_column='fAppliedValueB20', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec20 = models.FloatField(db_column='fAppliedValueC20', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued20 = models.FloatField(db_column='fAppliedValueD20', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee20 = models.FloatField(db_column='fAppliedValueE20', blank=True, null=True)  # Field name made lowercase.
    derrorallowed20 = models.FloatField(db_column='dErrorAllowed20', blank=True, null=True)  # Field name made lowercase.
    dmax20 = models.FloatField(db_column='dMax20', blank=True, null=True)  # Field name made lowercase.
    dmin20 = models.FloatField(db_column='dMin20', blank=True, null=True)  # Field name made lowercase.
    suom21 = models.TextField(db_column='sUOM21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue21 = models.TextField(db_column='sAppliedValue21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea21 = models.FloatField(db_column='fAppliedValueA21', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb21 = models.FloatField(db_column='fAppliedValueB21', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec21 = models.FloatField(db_column='fAppliedValueC21', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued21 = models.FloatField(db_column='fAppliedValueD21', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee21 = models.FloatField(db_column='fAppliedValueE21', blank=True, null=True)  # Field name made lowercase.
    derrorallowed21 = models.FloatField(db_column='dErrorAllowed21', blank=True, null=True)  # Field name made lowercase.
    dmax21 = models.FloatField(db_column='dMax21', blank=True, null=True)  # Field name made lowercase.
    dmin21 = models.FloatField(db_column='dMin21', blank=True, null=True)  # Field name made lowercase.
    suom22 = models.TextField(db_column='sUOM22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue22 = models.TextField(db_column='sAppliedValue22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea22 = models.FloatField(db_column='fAppliedValueA22', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb22 = models.FloatField(db_column='fAppliedValueB22', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec22 = models.FloatField(db_column='fAppliedValueC22', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued22 = models.FloatField(db_column='fAppliedValueD22', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee22 = models.FloatField(db_column='fAppliedValueE22', blank=True, null=True)  # Field name made lowercase.
    derrorallowed22 = models.FloatField(db_column='dErrorAllowed22', blank=True, null=True)  # Field name made lowercase.
    dmax22 = models.FloatField(db_column='dMax22', blank=True, null=True)  # Field name made lowercase.
    dmin22 = models.FloatField(db_column='dMin22', blank=True, null=True)  # Field name made lowercase.
    suom23 = models.TextField(db_column='sUOM23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue23 = models.TextField(db_column='sAppliedValue23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea23 = models.FloatField(db_column='fAppliedValueA23', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb23 = models.FloatField(db_column='fAppliedValueB23', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec23 = models.FloatField(db_column='fAppliedValueC23', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued23 = models.FloatField(db_column='fAppliedValueD23', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee23 = models.FloatField(db_column='fAppliedValueE23', blank=True, null=True)  # Field name made lowercase.
    derrorallowed23 = models.FloatField(db_column='dErrorAllowed23', blank=True, null=True)  # Field name made lowercase.
    dmax23 = models.FloatField(db_column='dMax23', blank=True, null=True)  # Field name made lowercase.
    dmin23 = models.FloatField(db_column='dMin23', blank=True, null=True)  # Field name made lowercase.
    suom24 = models.TextField(db_column='sUOM24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue24 = models.TextField(db_column='sAppliedValue24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea24 = models.FloatField(db_column='fAppliedValueA24', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb24 = models.FloatField(db_column='fAppliedValueB24', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec24 = models.FloatField(db_column='fAppliedValueC24', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued24 = models.FloatField(db_column='fAppliedValueD24', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee24 = models.FloatField(db_column='fAppliedValueE24', blank=True, null=True)  # Field name made lowercase.
    derrorallowed24 = models.FloatField(db_column='dErrorAllowed24', blank=True, null=True)  # Field name made lowercase.
    dmax24 = models.FloatField(db_column='dMax24', blank=True, null=True)  # Field name made lowercase.
    dmin24 = models.FloatField(db_column='dMin24', blank=True, null=True)  # Field name made lowercase.
    suom25 = models.TextField(db_column='sUOM25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue25 = models.TextField(db_column='sAppliedValue25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea25 = models.FloatField(db_column='fAppliedValueA25', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb25 = models.FloatField(db_column='fAppliedValueB25', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec25 = models.FloatField(db_column='fAppliedValueC25', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued25 = models.FloatField(db_column='fAppliedValueD25', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee25 = models.FloatField(db_column='fAppliedValueE25', blank=True, null=True)  # Field name made lowercase.
    derrorallowed25 = models.FloatField(db_column='dErrorAllowed25', blank=True, null=True)  # Field name made lowercase.
    dmax25 = models.FloatField(db_column='dMax25', blank=True, null=True)  # Field name made lowercase.
    dmin25 = models.FloatField(db_column='dMin25', blank=True, null=True)  # Field name made lowercase.
    suom26 = models.TextField(db_column='sUOM26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue26 = models.TextField(db_column='sAppliedValue26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea26 = models.FloatField(db_column='fAppliedValueA26', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb26 = models.FloatField(db_column='fAppliedValueB26', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec26 = models.FloatField(db_column='fAppliedValueC26', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued26 = models.FloatField(db_column='fAppliedValueD26', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee26 = models.FloatField(db_column='fAppliedValueE26', blank=True, null=True)  # Field name made lowercase.
    derrorallowed26 = models.FloatField(db_column='dErrorAllowed26', blank=True, null=True)  # Field name made lowercase.
    dmax26 = models.FloatField(db_column='dMax26', blank=True, null=True)  # Field name made lowercase.
    dmin26 = models.FloatField(db_column='dMin26', blank=True, null=True)  # Field name made lowercase.
    suom27 = models.TextField(db_column='sUOM27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue27 = models.TextField(db_column='sAppliedValue27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea27 = models.FloatField(db_column='fAppliedValueA27', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb27 = models.FloatField(db_column='fAppliedValueB27', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec27 = models.FloatField(db_column='fAppliedValueC27', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued27 = models.FloatField(db_column='fAppliedValueD27', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee27 = models.FloatField(db_column='fAppliedValueE27', blank=True, null=True)  # Field name made lowercase.
    derrorallowed27 = models.FloatField(db_column='dErrorAllowed27', blank=True, null=True)  # Field name made lowercase.
    dmax27 = models.FloatField(db_column='dMax27', blank=True, null=True)  # Field name made lowercase.
    dmin27 = models.FloatField(db_column='dMin27', blank=True, null=True)  # Field name made lowercase.
    suom28 = models.TextField(db_column='sUOM28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue28 = models.TextField(db_column='sAppliedValue28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea28 = models.FloatField(db_column='fAppliedValueA28', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb28 = models.FloatField(db_column='fAppliedValueB28', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec28 = models.FloatField(db_column='fAppliedValueC28', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued28 = models.FloatField(db_column='fAppliedValueD28', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee28 = models.FloatField(db_column='fAppliedValueE28', blank=True, null=True)  # Field name made lowercase.
    derrorallowed28 = models.FloatField(db_column='dErrorAllowed28', blank=True, null=True)  # Field name made lowercase.
    dmax28 = models.FloatField(db_column='dMax28', blank=True, null=True)  # Field name made lowercase.
    dmin28 = models.FloatField(db_column='dMin28', blank=True, null=True)  # Field name made lowercase.
    suom29 = models.TextField(db_column='sUOM29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue29 = models.TextField(db_column='sAppliedValue29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea29 = models.FloatField(db_column='fAppliedValueA29', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb29 = models.FloatField(db_column='fAppliedValueB29', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec29 = models.FloatField(db_column='fAppliedValueC29', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued29 = models.FloatField(db_column='fAppliedValueD29', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee29 = models.FloatField(db_column='fAppliedValueE29', blank=True, null=True)  # Field name made lowercase.
    derrorallowed29 = models.FloatField(db_column='dErrorAllowed29', blank=True, null=True)  # Field name made lowercase.
    dmax29 = models.FloatField(db_column='dMax29', blank=True, null=True)  # Field name made lowercase.
    dmin29 = models.FloatField(db_column='dMin29', blank=True, null=True)  # Field name made lowercase.
    suom30 = models.TextField(db_column='sUOM30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue30 = models.TextField(db_column='sAppliedValue30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea30 = models.FloatField(db_column='fAppliedValueA30', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb30 = models.FloatField(db_column='fAppliedValueB30', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec30 = models.FloatField(db_column='fAppliedValueC30', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued30 = models.FloatField(db_column='fAppliedValueD30', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee30 = models.FloatField(db_column='fAppliedValueE30', blank=True, null=True)  # Field name made lowercase.
    derrorallowed30 = models.FloatField(db_column='dErrorAllowed30', blank=True, null=True)  # Field name made lowercase.
    dmax30 = models.FloatField(db_column='dMax30', blank=True, null=True)  # Field name made lowercase.
    dmin30 = models.FloatField(db_column='dMin30', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentsListPart3'


class Masterinstrumentslistpart4(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lpartid1 = models.BigIntegerField(db_column='lPartID1', blank=True, null=True)  # Field name made lowercase.
    spartno1 = models.TextField(db_column='sPartNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc1 = models.TextField(db_column='sPartDesc1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision1 = models.TextField(db_column='sPartRivision1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid2 = models.BigIntegerField(db_column='lPartID2', blank=True, null=True)  # Field name made lowercase.
    spartno2 = models.TextField(db_column='sPartNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc2 = models.TextField(db_column='sPartDesc2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision2 = models.TextField(db_column='sPartRivision2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid3 = models.BigIntegerField(db_column='lPartID3', blank=True, null=True)  # Field name made lowercase.
    spartno3 = models.TextField(db_column='sPartNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc3 = models.TextField(db_column='sPartDesc3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision3 = models.TextField(db_column='sPartRivision3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid4 = models.BigIntegerField(db_column='lPartID4', blank=True, null=True)  # Field name made lowercase.
    spartno4 = models.TextField(db_column='sPartNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc4 = models.TextField(db_column='sPartDesc4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision4 = models.TextField(db_column='sPartRivision4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid5 = models.BigIntegerField(db_column='lPartID5', blank=True, null=True)  # Field name made lowercase.
    spartno5 = models.TextField(db_column='sPartNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc5 = models.TextField(db_column='sPartDesc5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision5 = models.TextField(db_column='sPartRivision5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid6 = models.BigIntegerField(db_column='lPartID6', blank=True, null=True)  # Field name made lowercase.
    spartno6 = models.TextField(db_column='sPartNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc6 = models.TextField(db_column='sPartDesc6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision6 = models.TextField(db_column='sPartRivision6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid7 = models.BigIntegerField(db_column='lPartID7', blank=True, null=True)  # Field name made lowercase.
    spartno7 = models.TextField(db_column='sPartNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc7 = models.TextField(db_column='sPartDesc7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision7 = models.TextField(db_column='sPartRivision7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid8 = models.BigIntegerField(db_column='lPartID8', blank=True, null=True)  # Field name made lowercase.
    spartno8 = models.TextField(db_column='sPartNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc8 = models.TextField(db_column='sPartDesc8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision8 = models.TextField(db_column='sPartRivision8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid9 = models.BigIntegerField(db_column='lPartID9', blank=True, null=True)  # Field name made lowercase.
    spartno9 = models.TextField(db_column='sPartNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc9 = models.TextField(db_column='sPartDesc9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision9 = models.TextField(db_column='sPartRivision9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lpartid10 = models.BigIntegerField(db_column='lPartID10', blank=True, null=True)  # Field name made lowercase.
    spartno10 = models.TextField(db_column='sPartNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartdesc10 = models.TextField(db_column='sPartDesc10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spartrivision10 = models.TextField(db_column='sPartRivision10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MasterInstrumentsListPart4'


class T8D(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8dno = models.BigIntegerField(db_column='l8DNo', blank=True, null=True)  # Field name made lowercase.
    s8dno = models.CharField(db_column='s8DNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ddateofreport = models.DateTimeField(db_column='dDateofReport', blank=True, null=True)  # Field name made lowercase.
    ssourceofcomplabigint = models.CharField(db_column='sSourceofComplabigint', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ssourcename = models.CharField(db_column='sSourceName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    soperationno = models.CharField(db_column='sOperationNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    d0closuredate = models.DateTimeField(db_column='D0ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d0checkdate = models.DateTimeField(db_column='D0CheckDate', blank=True, null=True)  # Field name made lowercase.
    d1closuredate = models.DateTimeField(db_column='D1ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d1checkdate = models.DateTimeField(db_column='D1CheckDate', blank=True, null=True)  # Field name made lowercase.
    d2closuredate = models.DateTimeField(db_column='D2ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d2checkdate = models.DateTimeField(db_column='D2CheckDate', blank=True, null=True)  # Field name made lowercase.
    d3closuredate = models.DateTimeField(db_column='D3ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d3checkdate = models.DateTimeField(db_column='D3CheckDate', blank=True, null=True)  # Field name made lowercase.
    d4closuredate = models.DateTimeField(db_column='D4ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d4checkdate = models.DateTimeField(db_column='D4CheckDate', blank=True, null=True)  # Field name made lowercase.
    d5closuredate = models.DateTimeField(db_column='D5ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d5checkdate = models.DateTimeField(db_column='D5CheckDate', blank=True, null=True)  # Field name made lowercase.
    d6closuredate = models.DateTimeField(db_column='D6ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d6checkdate = models.DateTimeField(db_column='D6CheckDate', blank=True, null=True)  # Field name made lowercase.
    d7closuredate = models.DateTimeField(db_column='D7ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d7checkdate = models.DateTimeField(db_column='D7CheckDate', blank=True, null=True)  # Field name made lowercase.
    d8closuredate = models.DateTimeField(db_column='D8ClosureDate', blank=True, null=True)  # Field name made lowercase.
    d8checkdate = models.DateTimeField(db_column='D8CheckDate', blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    spartdesc = models.CharField(db_column='sPartDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sworkorderno = models.CharField(db_column='sWorkOrderNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    spono = models.CharField(db_column='sPONo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    scustomercontact = models.CharField(db_column='sCustomerContact', max_length=250, blank=True, null=True)  # Field name made lowercase.
    switnessby = models.CharField(db_column='sWitnessBy', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sdefecttype = models.CharField(db_column='sDefectType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    scustomerrefno = models.CharField(db_column='sCustomerRefNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    semergresactions = models.CharField(db_column='sEmergResActions', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bdeliveryaffected = models.BooleanField(db_column='bDeliveryaffected', blank=True, null=True)  # Field name made lowercase.
    bsusprootcauseidentified = models.BooleanField(db_column='bSusprootcauseidentified', blank=True, null=True)  # Field name made lowercase.
    brootcauseverified = models.BooleanField(db_column='bRootcauseverified', blank=True, null=True)  # Field name made lowercase.
    bemerresponseaction = models.BooleanField(db_column='bEmerResponseAction', blank=True, null=True)  # Field name made lowercase.
    brecurringproblem = models.BooleanField(db_column='bRecurringproblem', blank=True, null=True)  # Field name made lowercase.
    srecurringprobfile = models.CharField(db_column='sRecurringProbFile', max_length=250, blank=True, null=True)  # Field name made lowercase.
    srecurringprobfolder = models.CharField(db_column='sRecurringProbFolder', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sproblemdesc = models.CharField(db_column='sProblemDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sspecrequired = models.CharField(db_column='sSpecRequired', max_length=250, blank=True, null=True)  # Field name made lowercase.
    swhatspec = models.CharField(db_column='sWhatSpec', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lpartproduced = models.BigIntegerField(db_column='lPartProduced', blank=True, null=True)  # Field name made lowercase.
    lpartaffected = models.BigIntegerField(db_column='lPartAffected', blank=True, null=True)  # Field name made lowercase.
    lpartpercent = models.BigIntegerField(db_column='lPartPercent', blank=True, null=True)  # Field name made lowercase.
    sissueimagefile = models.CharField(db_column='sIssueImageFile', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sissueimagefolder = models.CharField(db_column='sIssueImageFolder', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bbiginternal = models.BooleanField(blank=True, null=True)
    sbiginternal = models.BooleanField(blank=True, null=True)
    bsupplier = models.BooleanField(db_column='bSupplier', blank=True, null=True)  # Field name made lowercase.
    ssupplier = models.BooleanField(db_column='sSupplier', blank=True, null=True)  # Field name made lowercase.
    bcustomer = models.BooleanField(db_column='bCustomer', blank=True, null=True)  # Field name made lowercase.
    scustomer = models.CharField(db_column='sCustomer', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dtprobpartoccurdate = models.DateTimeField(db_column='dtProbpartoccurdate', blank=True, null=True)  # Field name made lowercase.
    dtprobpartawarenessdate = models.DateTimeField(db_column='dtProbpartawarenessdate', blank=True, null=True)  # Field name made lowercase.
    dtprobpartshipmentdate = models.DateTimeField(db_column='dtProbpartshipmentdate', blank=True, null=True)  # Field name made lowercase.
    sverifiedby = models.CharField(db_column='sVerifiedBy', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sverifiedtitle = models.CharField(db_column='sVerifiedTitle', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dtverifieddate = models.DateTimeField(db_column='dtVerifiedDate', blank=True, null=True)  # Field name made lowercase.
    dtwhendate = models.DateTimeField(db_column='dtWhenDate', blank=True, null=True)  # Field name made lowercase.
    dtwheredate = models.DateTimeField(db_column='dtWhereDate', blank=True, null=True)  # Field name made lowercase.
    dthowdate = models.DateTimeField(db_column='dtHowDate', blank=True, null=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sdateofreport = models.CharField(db_column='sDateofReport', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sclosuredate = models.CharField(db_column='sClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s0checkdate = models.CharField(db_column='s0CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s1closuredate = models.CharField(db_column='s1ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s1checkdate = models.CharField(db_column='s1CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s2closuredate = models.CharField(db_column='s2ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s2checkdate = models.CharField(db_column='s2CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s3closuredate = models.CharField(db_column='s3ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s3checkdate = models.CharField(db_column='s3CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s4closuredate = models.CharField(db_column='s4ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s4checkdate = models.CharField(db_column='s4CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s5closuredate = models.CharField(db_column='s5ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s5checkdate = models.CharField(db_column='s5CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s6closuredate = models.CharField(db_column='s6ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s6checkdate = models.CharField(db_column='s6CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s7closuredate = models.CharField(db_column='s7ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s7checkdate = models.CharField(db_column='s7CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s8closuredate = models.CharField(db_column='s8ClosureDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s8checkdate = models.CharField(db_column='s8CheckDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stprobpartoccurdate = models.CharField(db_column='stProbpartoccurdate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stprobpartawarenessdate = models.CharField(db_column='stProbpartawarenessdate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stprobpartshipmentdate = models.CharField(db_column='stProbpartshipmentdate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stverifieddate = models.CharField(db_column='stVerifiedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stwhendate = models.CharField(db_column='stWhenDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stwheredate = models.CharField(db_column='stWhereDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sthowdate = models.CharField(db_column='stHowDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D'


class T8D0Emergencyaction(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    semergencyaction = models.CharField(db_column='sEmergencyAction', max_length=250, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dtdate = models.DateTimeField(db_column='dtDate', blank=True, null=True)  # Field name made lowercase.
    dtfinisheddate = models.DateTimeField(db_column='dtFinishedDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=250, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    s5ms = models.CharField(db_column='s5Ms', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bverified = models.BooleanField(db_column='bVerified', blank=True, null=True)  # Field name made lowercase.
    sverifiedmethod = models.CharField(db_column='sVerifiedMethod', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dtstartdate = models.DateTimeField(db_column='dtStartDate', blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sfinisheddate = models.CharField(db_column='sFinishedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D0EmergencyAction'


class T8D1Documents(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    sdocumenttype = models.CharField(db_column='sDocumentType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sfilename = models.CharField(db_column='sFileName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sfilefolder = models.CharField(db_column='sFileFolder', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sversionno = models.CharField(db_column='sVersionNo', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D1Documents'


class T8D1Teamd(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    sdepartment = models.CharField(db_column='sDepartment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scontactno = models.CharField(db_column='sContactNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    semail = models.CharField(db_column='sEmail', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D1TeamD'


class T8D3Containmentaction(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    scontainmentaction = models.CharField(db_column='sContainmentAction', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dttargetdate = models.DateTimeField(db_column='dtTargetDate', blank=True, null=True)  # Field name made lowercase.
    dtfinisheddate = models.DateTimeField(db_column='dtFinishedDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    s5ms = models.CharField(db_column='s5Ms', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bverified = models.BooleanField(db_column='bVerified', blank=True, null=True)  # Field name made lowercase.
    sverifiedmethod = models.CharField(db_column='sVerifiedMethod', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtstartdate = models.DateTimeField(db_column='dtStartDate', blank=True, null=True)  # Field name made lowercase.
    stargetdate = models.CharField(db_column='sTargetDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sfinisheddate = models.CharField(db_column='sFinishedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D3ContainmentAction'


class T8D4Rootcause(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    srootcause = models.CharField(db_column='sRootCause', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dttargetdate = models.DateTimeField(db_column='dtTargetDate', blank=True, null=True)  # Field name made lowercase.
    dtverifieddate = models.DateTimeField(db_column='dtVerifiedDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    s5ms = models.CharField(db_column='s5Ms', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bverified = models.BooleanField(db_column='bVerified', blank=True, null=True)  # Field name made lowercase.
    sverifiedmethod = models.CharField(db_column='sVerifiedMethod', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D4RootCause'


class T8D5Correctiveaction(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    spercorraction = models.CharField(db_column='sPerCorrAction', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dttargetdate = models.DateTimeField(db_column='dtTargetDate', blank=True, null=True)  # Field name made lowercase.
    dtverifieddate = models.DateTimeField(db_column='dtVerifiedDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    s5ms = models.CharField(db_column='s5Ms', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bverified = models.BooleanField(db_column='bVerified', blank=True, null=True)  # Field name made lowercase.
    sverifiedmethod = models.CharField(db_column='sVerifiedMethod', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stargetdate = models.CharField(db_column='sTargetDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sverifieddate = models.CharField(db_column='sVerifiedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D5CorrectiveAction'


class T8D6Implcorrectiveaction(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    spercorraction = models.CharField(db_column='sPerCorrAction', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dttargetdate = models.DateTimeField(db_column='dtTargetDate', blank=True, null=True)  # Field name made lowercase.
    dtimplementationdate = models.DateTimeField(db_column='dtImplementationDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    bcustomerconcurrence = models.BooleanField(db_column='bCustomerConcurrence', blank=True, null=True)  # Field name made lowercase.
    stargetdate = models.CharField(db_column='sTargetDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sverifieddate = models.CharField(db_column='sVerifiedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D6ImplCorrectiveAction'


class T8D6Implpreventiveaction(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    spa = models.CharField(db_column='sPA', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spcaimplementationplan = models.CharField(db_column='sPCAImplementationPlan', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dttargetdate = models.DateTimeField(db_column='dtTargetDate', blank=True, null=True)  # Field name made lowercase.
    dtimplementationdate = models.DateTimeField(db_column='dtImplementationDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    bcustomerconcurrence = models.BooleanField(db_column='bCustomerConcurrence', blank=True, null=True)  # Field name made lowercase.
    stargetdate = models.CharField(db_column='sTargetDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D6ImplPreventiveAction'


class T8D7Creview(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    srevieweddocument = models.CharField(db_column='sRevieweddocument', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srevisionstatus = models.CharField(db_column='sRevisionStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sresp = models.CharField(db_column='sResp', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtplanneddate = models.DateTimeField(db_column='dtPlannedDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    bcustomerconcurrence = models.BooleanField(db_column='bCustomerConcurrence', blank=True, null=True)  # Field name made lowercase.
    splanneddate = models.CharField(db_column='sPlannedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D7CReview'


class T8D8Followupmeetings(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    l8did = models.BigIntegerField(db_column='l8DID', blank=True, null=True)  # Field name made lowercase.
    dtplanneddate = models.DateTimeField(db_column='dtPlannedDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=750, blank=True, null=True)  # Field name made lowercase.
    bcustomerconcurrence = models.BooleanField(db_column='bCustomerConcurrence', blank=True, null=True)  # Field name made lowercase.
    splanneddate = models.CharField(db_column='sPlannedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sstartdate = models.CharField(db_column='sStartDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T8D8FollowupMeetings'


class Tagencyinstrument(models.Model):
    agencyinstrumentid = models.BigAutoField(db_column='AgencyInstrumentId', primary_key=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    agencyid = models.BigIntegerField(db_column='AgencyId', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=750, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAgencyInstrument'


class Tcheckin(models.Model):
    historycheckinid = models.BigAutoField(db_column='HistoryCheckinId', primary_key=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    currentlocationid = models.BigIntegerField(db_column='CurrentLocationId', blank=True, null=True)  # Field name made lowercase.
    scurrentlocation = models.CharField(db_column='sCurrentLocation', max_length=350, blank=True, null=True)  # Field name made lowercase.
    igtype = models.CharField(db_column='IGType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    checkindate = models.DateTimeField(db_column='CheckinDate', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvaldate = models.DateTimeField(db_column='ApprovalDate', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    newlocationid = models.BigIntegerField(db_column='NewLocationId', blank=True, null=True)  # Field name made lowercase.
    snewlocation = models.CharField(db_column='sNewLocation', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scheckout = models.CharField(db_column='sCheckOut', max_length=350, blank=True, null=True)  # Field name made lowercase.
    machinetype = models.CharField(db_column='MachineType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibration = models.CharField(db_column='sCalibration', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcalibrationdate = models.DateTimeField(db_column='dCalibrationDate', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    checoutdate = models.DateTimeField(db_column='ChecoutDate', blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken = models.CharField(db_column='srecdTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    breturned = models.BooleanField(db_column='bReturned', blank=True, null=True)  # Field name made lowercase.
    loriginalissuedtoid = models.BigIntegerField(db_column='lOriginalIssuedToId', blank=True, null=True)  # Field name made lowercase.
    soriginalusername = models.DateTimeField(db_column='sOriginalUserName', blank=True, null=True)  # Field name made lowercase.
    btransferred = models.BooleanField(db_column='bTransferred', blank=True, null=True)  # Field name made lowercase.
    ltransferredfromissuedtoid = models.BigIntegerField(db_column='lTransferredfromIssuedToId', blank=True, null=True)  # Field name made lowercase.
    stransferredfromrname = models.CharField(db_column='sTransferredfromrName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ltransferredtoissuedtoid = models.BigIntegerField(db_column='lTransferredToIssuedToId', blank=True, null=True)  # Field name made lowercase.
    stransferredtorname = models.CharField(db_column='sTransferredTorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lreturnedfromtoid = models.BigIntegerField(db_column='lReturnedfromToId', blank=True, null=True)  # Field name made lowercase.
    sreturnedfromname = models.CharField(db_column='sReturnedfromName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lreturnedtotoid = models.BigIntegerField(db_column='lReturnedToToId', blank=True, null=True)  # Field name made lowercase.
    sreturnedtoname = models.CharField(db_column='sReturnedToName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lnooftransfers = models.BigIntegerField(db_column='lNoofTransfers', blank=True, null=True)  # Field name made lowercase.
    lasttransferredondate = models.DateTimeField(db_column='LastTransferredonDate', blank=True, null=True)  # Field name made lowercase.
    previoustransferredondate = models.DateTimeField(db_column='PreviousTransferredonDate', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken1 = models.CharField(db_column='srecdTimeTaken1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken2 = models.CharField(db_column='srecdTimeTaken2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken3 = models.CharField(db_column='srecdTimeTaken3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken4 = models.CharField(db_column='srecdTimeTaken4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srecdtimetaken5 = models.CharField(db_column='srecdTimeTaken5', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstno = models.CharField(db_column='sInstNo', max_length=400, blank=True, null=True)  # Field name made lowercase.
    sinstdesc = models.CharField(db_column='sInstDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    scheckindate = models.CharField(db_column='SCheckinDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scalibrationdate = models.CharField(db_column='sCalibrationDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    schecoutdate = models.CharField(db_column='sChecoutDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    saoriginalusername = models.CharField(db_column='saOriginalUserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slasttransferredondate = models.CharField(db_column='sLastTransferredonDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sprevioustransferredondate = models.CharField(db_column='sPreviousTransferredonDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    brequest = models.IntegerField(db_column='bRequest', blank=True, null=True)  # Field name made lowercase.
    lrequestbyid = models.BigIntegerField(db_column='lRequestbyId', blank=True, null=True)  # Field name made lowercase.
    srequestbyname = models.CharField(db_column='sRequestbyName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    srequeston = models.CharField(db_column='sRequestOn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    srequestcomment = models.CharField(db_column='sRequestComment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brequestcancel = models.IntegerField(db_column='bRequestCancel', blank=True, null=True)  # Field name made lowercase.
    brequestaccept = models.IntegerField(db_column='bRequestAccept', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCheckIN'


class Tdccmm(models.Model):
    ldcin = models.BigAutoField(db_column='lDCIN', primary_key=True)  # Field name made lowercase.
    sdcno = models.CharField(db_column='sDCNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcdate = models.DateTimeField(db_column='dcDate', blank=True, null=True)  # Field name made lowercase.
    iyear = models.BigIntegerField(db_column='iYear', blank=True, null=True)  # Field name made lowercase.
    ldcno = models.BigIntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress1 = models.CharField(db_column='sToAddress1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress2 = models.CharField(db_column='sToAddress2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress3 = models.CharField(db_column='sToAddress3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shandedto = models.CharField(db_column='sHandedTO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdeliverybyhand = models.BooleanField(db_column='bDeliveryByHand', blank=True, null=True)  # Field name made lowercase.
    bdeliverybydoor = models.BooleanField(db_column='bDeliveryByDoor', blank=True, null=True)  # Field name made lowercase.
    bdeliverybyoffice = models.BooleanField(db_column='bDeliveryByOffice', blank=True, null=True)  # Field name made lowercase.
    bdeliverybycollsupplier = models.BooleanField(db_column='bDeliveryByCollSupplier', blank=True, null=True)  # Field name made lowercase.
    lnoofcasesitems = models.BigIntegerField(db_column='lNoofCasesItems', blank=True, null=True)  # Field name made lowercase.
    ltotalweight = models.BigIntegerField(db_column='lTotalWeight', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopay = models.BooleanField(db_column='bFrieghtToPay', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopaid = models.BooleanField(db_column='bFrieghtToPaid', blank=True, null=True)  # Field name made lowercase.
    bfrieghttona = models.BooleanField(db_column='bFrieghtToNA', blank=True, null=True)  # Field name made lowercase.
    frieghtcharges = models.FloatField(db_column='FrieghtCharges', blank=True, null=True)  # Field name made lowercase.
    bmaterialchargeable = models.BooleanField(db_column='bMaterialChargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnochargeable = models.BooleanField(db_column='bMaterialNochargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialreturnable = models.BooleanField(db_column='bMaterialReturnable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnonreturnable = models.BooleanField(db_column='bMaterialNonReturnable', blank=True, null=True)  # Field name made lowercase.
    soriginatingdepartment = models.CharField(db_column='sOriginatingDepartment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    schallanno = models.CharField(db_column='sChallanNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lmonth = models.BigIntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.BigIntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    breceivedbackall = models.BooleanField(db_column='bReceivedBackAll', blank=True, null=True)  # Field name made lowercase.
    bbiginternalmeasurement = models.BooleanField(db_column='bbiginternalMeasurement', blank=True, null=True)  # Field name made lowercase.
    sthrough = models.CharField(db_column='sThrough', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bfrieghtpaidonline = models.BooleanField(db_column='bFrieghtPaidOnline', blank=True, null=True)  # Field name made lowercase.
    bfrieghttpaidcheque = models.BooleanField(db_column='bFrieghtTPaidCheque', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.BigIntegerField(db_column='lPlantCode', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate2 = models.CharField(db_column='sDate2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate3 = models.CharField(db_column='sDate3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate4 = models.CharField(db_column='sDate4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scdate = models.CharField(db_column='scDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapproveddate = models.CharField(db_column='sApprovedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCCMM'


class Tdccmmmulti(models.Model):
    ldcmultiin = models.BigAutoField(db_column='lDCMultiIN', primary_key=True)  # Field name made lowercase.
    ldcid = models.BigIntegerField(db_column='lDCID', blank=True, null=True)  # Field name made lowercase.
    thistorymainid = models.BigIntegerField(db_column='THistoryMainID', blank=True, null=True)  # Field name made lowercase.
    iinstid = models.BigIntegerField(db_column='IInstID', blank=True, null=True)  # Field name made lowercase.
    tinstdeschistorymainid = models.BigIntegerField(db_column='TInstDescHistoryMainID', blank=True, null=True)  # Field name made lowercase.
    sdescmaterial = models.CharField(db_column='sDescMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    spurpose = models.CharField(db_column='sPurpose', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sspecialinst = models.CharField(db_column='sSpecialInst', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcatid = models.BigIntegerField(db_column='lCatId', blank=True, null=True)  # Field name made lowercase.
    sinstdesc = models.CharField(db_column='sInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    dateofrecd = models.DateTimeField(db_column='DateofRecd', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ltransid = models.BigIntegerField(db_column='lTransID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCCMMMulti'


class Tdccalibration(models.Model):
    ldcin = models.BigAutoField(db_column='lDCIN', primary_key=True)  # Field name made lowercase.
    sdcno = models.CharField(db_column='sDCNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcdate = models.DateTimeField(db_column='dcDate', blank=True, null=True)  # Field name made lowercase.
    iyear = models.BigIntegerField(db_column='iYear', blank=True, null=True)  # Field name made lowercase.
    ldcno = models.BigIntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress1 = models.CharField(db_column='sToAddress1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress2 = models.CharField(db_column='sToAddress2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress3 = models.CharField(db_column='sToAddress3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shandedto = models.CharField(db_column='sHandedTO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdeliverybyhand = models.BooleanField(db_column='bDeliveryByHand', blank=True, null=True)  # Field name made lowercase.
    bdeliverybydoor = models.BooleanField(db_column='bDeliveryByDoor', blank=True, null=True)  # Field name made lowercase.
    bdeliverybyoffice = models.BooleanField(db_column='bDeliveryByOffice', blank=True, null=True)  # Field name made lowercase.
    bdeliverybycollsupplier = models.BooleanField(db_column='bDeliveryByCollSupplier', blank=True, null=True)  # Field name made lowercase.
    lnoofcasesitems = models.BigIntegerField(db_column='lNoofCasesItems', blank=True, null=True)  # Field name made lowercase.
    ltotalweight = models.BigIntegerField(db_column='lTotalWeight', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopay = models.BooleanField(db_column='bFrieghtToPay', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopaid = models.BooleanField(db_column='bFrieghtToPaid', blank=True, null=True)  # Field name made lowercase.
    bfrieghttona = models.BooleanField(db_column='bFrieghtToNA', blank=True, null=True)  # Field name made lowercase.
    frieghtcharges = models.FloatField(db_column='FrieghtCharges', blank=True, null=True)  # Field name made lowercase.
    bmaterialchargeable = models.BooleanField(db_column='bMaterialChargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnochargeable = models.BooleanField(db_column='bMaterialNochargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialreturnable = models.BooleanField(db_column='bMaterialReturnable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnonreturnable = models.BooleanField(db_column='bMaterialNonReturnable', blank=True, null=True)  # Field name made lowercase.
    soriginatingdepartment = models.CharField(db_column='sOriginatingDepartment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    schallanno = models.CharField(db_column='sChallanNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lmonth = models.BigIntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.BigIntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    breceivedbackall = models.BooleanField(db_column='bReceivedBackAll', blank=True, null=True)  # Field name made lowercase.
    bbiginternalmeasurement = models.BooleanField(db_column='bbiginternalMeasurement', blank=True, null=True)  # Field name made lowercase.
    sthrough = models.CharField(db_column='sThrough', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bfrieghtpaidonline = models.BooleanField(db_column='bFrieghtPaidOnline', blank=True, null=True)  # Field name made lowercase.
    bfrieghttpaidcheque = models.BooleanField(db_column='bFrieghtTPaidCheque', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.BigIntegerField(db_column='lPlantCode', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate2 = models.CharField(db_column='sDate2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate3 = models.CharField(db_column='sDate3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate4 = models.CharField(db_column='sDate4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scdate = models.CharField(db_column='scDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapproveddate = models.CharField(db_column='sApprovedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCCalibration'


class Tdccalibrationmulti(models.Model):
    ldcmultiin = models.BigAutoField(db_column='lDCMultiIN', primary_key=True)  # Field name made lowercase.
    ldcid = models.BigIntegerField(db_column='lDCID', blank=True, null=True)  # Field name made lowercase.
    thistorymainid = models.BigIntegerField(db_column='THistoryMainID', blank=True, null=True)  # Field name made lowercase.
    iinstid = models.BigIntegerField(db_column='IInstID', blank=True, null=True)  # Field name made lowercase.
    tinstdeschistorymainid = models.BigIntegerField(db_column='TInstDescHistoryMainID', blank=True, null=True)  # Field name made lowercase.
    sdescmaterial = models.CharField(db_column='sDescMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    spurpose = models.CharField(db_column='sPurpose', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sspecialinst = models.CharField(db_column='sSpecialInst', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcatid = models.BigIntegerField(db_column='lCatId', blank=True, null=True)  # Field name made lowercase.
    sinstdesc = models.CharField(db_column='sInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    dateofrecd = models.DateTimeField(db_column='DateofRecd', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ltransid = models.BigIntegerField(db_column='lTransID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCCalibrationMulti'


class Tdcmeasurement(models.Model):
    ldcin = models.BigAutoField(db_column='lDCIN', primary_key=True)  # Field name made lowercase.
    sdcno = models.CharField(db_column='sDCNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcdate = models.DateTimeField(db_column='dcDate', blank=True, null=True)  # Field name made lowercase.
    iyear = models.BigIntegerField(db_column='iYear', blank=True, null=True)  # Field name made lowercase.
    ldcno = models.BigIntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress1 = models.CharField(db_column='sToAddress1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress2 = models.CharField(db_column='sToAddress2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress3 = models.CharField(db_column='sToAddress3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shandedto = models.CharField(db_column='sHandedTO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdeliverybyhand = models.BooleanField(db_column='bDeliveryByHand', blank=True, null=True)  # Field name made lowercase.
    bdeliverybydoor = models.BooleanField(db_column='bDeliveryByDoor', blank=True, null=True)  # Field name made lowercase.
    bdeliverybyoffice = models.BooleanField(db_column='bDeliveryByOffice', blank=True, null=True)  # Field name made lowercase.
    bdeliverybycollsupplier = models.BooleanField(db_column='bDeliveryByCollSupplier', blank=True, null=True)  # Field name made lowercase.
    lnoofcasesitems = models.BigIntegerField(db_column='lNoofCasesItems', blank=True, null=True)  # Field name made lowercase.
    ltotalweight = models.BigIntegerField(db_column='lTotalWeight', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopay = models.BooleanField(db_column='bFrieghtToPay', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopaid = models.BooleanField(db_column='bFrieghtToPaid', blank=True, null=True)  # Field name made lowercase.
    bfrieghttona = models.BooleanField(db_column='bFrieghtToNA', blank=True, null=True)  # Field name made lowercase.
    frieghtcharges = models.FloatField(db_column='FrieghtCharges', blank=True, null=True)  # Field name made lowercase.
    bmaterialchargeable = models.BooleanField(db_column='bMaterialChargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnochargeable = models.BooleanField(db_column='bMaterialNochargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialreturnable = models.BooleanField(db_column='bMaterialReturnable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnonreturnable = models.BooleanField(db_column='bMaterialNonReturnable', blank=True, null=True)  # Field name made lowercase.
    soriginatingdepartment = models.CharField(db_column='sOriginatingDepartment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    schallanno = models.CharField(db_column='sChallanNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lmonth = models.BigIntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.BigIntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    breceivedbackall = models.BooleanField(db_column='bReceivedBackAll', blank=True, null=True)  # Field name made lowercase.
    bbiginternalmeasurement = models.BooleanField(db_column='bbiginternalMeasurement', blank=True, null=True)  # Field name made lowercase.
    sthrough = models.CharField(db_column='sThrough', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bfrieghtpaidonline = models.BooleanField(db_column='bFrieghtPaidOnline', blank=True, null=True)  # Field name made lowercase.
    bfrieghttpaidcheque = models.BooleanField(db_column='bFrieghtTPaidCheque', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.BigIntegerField(db_column='lPlantCode', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate2 = models.CharField(db_column='sDate2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate3 = models.CharField(db_column='sDate3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate4 = models.CharField(db_column='sDate4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scdate = models.CharField(db_column='scDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapproveddate = models.CharField(db_column='sApprovedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCMeasurement'


class Tdcmeasurementmmulti(models.Model):
    ldcmultiin = models.BigAutoField(db_column='lDCMultiIN', primary_key=True)  # Field name made lowercase.
    ldcid = models.BigIntegerField(db_column='lDCID', blank=True, null=True)  # Field name made lowercase.
    thistorymainid = models.BigIntegerField(db_column='THistoryMainID', blank=True, null=True)  # Field name made lowercase.
    iinstid = models.BigIntegerField(db_column='IInstID', blank=True, null=True)  # Field name made lowercase.
    tinstdeschistorymainid = models.BigIntegerField(db_column='TInstDescHistoryMainID', blank=True, null=True)  # Field name made lowercase.
    sdescmaterial = models.CharField(db_column='sDescMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    spurpose = models.CharField(db_column='sPurpose', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sspecialinst = models.CharField(db_column='sSpecialInst', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcatid = models.BigIntegerField(db_column='lCatId', blank=True, null=True)  # Field name made lowercase.
    sinstdesc = models.CharField(db_column='sInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    dateofrecd = models.DateTimeField(db_column='DateofRecd', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ltransid = models.BigIntegerField(db_column='lTransID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCMeasurementMMulti'


class Tdcservice(models.Model):
    ldcin = models.BigAutoField(db_column='lDCIN', primary_key=True)  # Field name made lowercase.
    sdcno = models.CharField(db_column='sDCNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcdate = models.DateTimeField(db_column='dcDate', blank=True, null=True)  # Field name made lowercase.
    iyear = models.BigIntegerField(db_column='iYear', blank=True, null=True)  # Field name made lowercase.
    ldcno = models.BigIntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress1 = models.CharField(db_column='sToAddress1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress2 = models.CharField(db_column='sToAddress2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stoaddress3 = models.CharField(db_column='sToAddress3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shandedto = models.CharField(db_column='sHandedTO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdeliverybyhand = models.BooleanField(db_column='bDeliveryByHand', blank=True, null=True)  # Field name made lowercase.
    bdeliverybydoor = models.BooleanField(db_column='bDeliveryByDoor', blank=True, null=True)  # Field name made lowercase.
    bdeliverybyoffice = models.BooleanField(db_column='bDeliveryByOffice', blank=True, null=True)  # Field name made lowercase.
    bdeliverybycollsupplier = models.BooleanField(db_column='bDeliveryByCollSupplier', blank=True, null=True)  # Field name made lowercase.
    lnoofcasesitems = models.BigIntegerField(db_column='lNoofCasesItems', blank=True, null=True)  # Field name made lowercase.
    ltotalweight = models.BigIntegerField(db_column='lTotalWeight', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopay = models.BooleanField(db_column='bFrieghtToPay', blank=True, null=True)  # Field name made lowercase.
    bfrieghttopaid = models.BooleanField(db_column='bFrieghtToPaid', blank=True, null=True)  # Field name made lowercase.
    bfrieghttona = models.BooleanField(db_column='bFrieghtToNA', blank=True, null=True)  # Field name made lowercase.
    frieghtcharges = models.FloatField(db_column='FrieghtCharges', blank=True, null=True)  # Field name made lowercase.
    bmaterialchargeable = models.BooleanField(db_column='bMaterialChargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnochargeable = models.BooleanField(db_column='bMaterialNochargeable', blank=True, null=True)  # Field name made lowercase.
    bmaterialreturnable = models.BooleanField(db_column='bMaterialReturnable', blank=True, null=True)  # Field name made lowercase.
    bmaterialnonreturnable = models.BooleanField(db_column='bMaterialNonReturnable', blank=True, null=True)  # Field name made lowercase.
    soriginatingdepartment = models.CharField(db_column='sOriginatingDepartment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    schallanno = models.CharField(db_column='sChallanNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lmonth = models.BigIntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.BigIntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    breceivedbackall = models.BooleanField(db_column='bReceivedBackAll', blank=True, null=True)  # Field name made lowercase.
    bbiginternalmeasurement = models.BooleanField(db_column='bbiginternalMeasurement', blank=True, null=True)  # Field name made lowercase.
    sthrough = models.CharField(db_column='sThrough', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bfrieghtpaidonline = models.BooleanField(db_column='bFrieghtPaidOnline', blank=True, null=True)  # Field name made lowercase.
    bfrieghttpaidcheque = models.BooleanField(db_column='bFrieghtTPaidCheque', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.BigIntegerField(db_column='lPlantCode', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate2 = models.CharField(db_column='sDate2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate3 = models.CharField(db_column='sDate3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdate4 = models.CharField(db_column='sDate4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scdate = models.CharField(db_column='scDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapproveddate = models.CharField(db_column='sApprovedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCService'


class Tdcservicemmulti(models.Model):
    ldcmultiin = models.BigAutoField(db_column='lDCMultiIN', primary_key=True)  # Field name made lowercase.
    ldcid = models.BigIntegerField(db_column='lDCID', blank=True, null=True)  # Field name made lowercase.
    thistorymainid = models.BigIntegerField(db_column='THistoryMainID', blank=True, null=True)  # Field name made lowercase.
    iinstid = models.BigIntegerField(db_column='IInstID', blank=True, null=True)  # Field name made lowercase.
    tinstdeschistorymainid = models.BigIntegerField(db_column='TInstDescHistoryMainID', blank=True, null=True)  # Field name made lowercase.
    sdescmaterial = models.CharField(db_column='sDescMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    spurpose = models.CharField(db_column='sPurpose', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sspecialinst = models.CharField(db_column='sSpecialInst', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcatid = models.BigIntegerField(db_column='lCatId', blank=True, null=True)  # Field name made lowercase.
    sinstdesc = models.CharField(db_column='sInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brecdback = models.BooleanField(db_column='bRecdBack', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    bcalibrationexternal = models.BooleanField(db_column='bCalibrationExternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementinternal = models.BooleanField(db_column='bMeasurementInternal', blank=True, null=True)  # Field name made lowercase.
    bmeasurementbiginternal = models.BooleanField(db_column='bMeasurementbiginternal', blank=True, null=True)  # Field name made lowercase.
    dateofrecd = models.DateTimeField(db_column='DateofRecd', blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ltransid = models.BigIntegerField(db_column='lTransID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDCServiceMMulti'


class Thistory(models.Model):
    lid = models.CharField(db_column='lId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.CharField(db_column='lHistoryMainId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.CharField(db_column='lInstrumentId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shistorytype = models.CharField(db_column='sHistoryType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendor = models.CharField(db_column='sCalibrationVendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendorid = models.CharField(db_column='sCalibrationVendorID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scalibrationresult = models.CharField(db_column='sCalibrationResult', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtcalibrationdate = models.CharField(db_column='dtCalibrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fcalibcost = models.CharField(db_column='fCalibCost', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llplantid = models.CharField(db_column='llPlantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssplantname = models.CharField(db_column='ssPlantName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    slplantcode = models.CharField(db_column='slPlantCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.CharField(db_column='lCompanyId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtreturneddate = models.CharField(db_column='dtReturnedDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sfrom = models.CharField(db_column='sFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dthistorydate = models.CharField(db_column='dtHistoryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shistorydate = models.CharField(db_column='sHistoryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sreturneddate = models.CharField(db_column='sReturnedDate', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistory'


class Thistorymain(models.Model):
    lhistorymainid = models.BigAutoField(db_column='lHistoryMainId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationresult = models.CharField(db_column='sCalibrationResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtcalibrationdate = models.DateTimeField(db_column='dtCalibrationDate', blank=True, null=True)  # Field name made lowercase.
    scalibrationdate = models.CharField(db_column='sCalibrationDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcalibcost = models.FloatField(db_column='fCalibCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemperature = models.CharField(db_column='sTemperature', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shumidity = models.CharField(db_column='sHumidity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredbyid = models.BigIntegerField(db_column='lEnteredById', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedbyid = models.BigIntegerField(db_column='lApprovedById', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovaldate = models.CharField(db_column='sApprovalDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendor = models.CharField(db_column='sCalibrationVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibrationvendorid = models.BigIntegerField(db_column='lCalibrationVendorID', blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    sdispatchdate = models.CharField(db_column='sDispatchDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lcalibratedbyid = models.BigIntegerField(db_column='lCalibratedByID', blank=True, null=True)  # Field name made lowercase.
    scalibratedby = models.CharField(db_column='sCalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificateno = models.CharField(db_column='sCalibrationCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcertificate = models.BooleanField(db_column='bCertificate', blank=True, null=True)  # Field name made lowercase.
    ftotalerror = models.FloatField(db_column='fTotalError', blank=True, null=True)  # Field name made lowercase.
    facconstant = models.FloatField(db_column='fACConstant', blank=True, null=True)  # Field name made lowercase.
    flc = models.FloatField(db_column='fLC', blank=True, null=True)  # Field name made lowercase.
    fproducttolerance = models.FloatField(db_column='fProductTolerance', blank=True, null=True)  # Field name made lowercase.
    facceptancecriteria = models.FloatField(db_column='fAcceptanceCriteria', blank=True, null=True)  # Field name made lowercase.
    dtindentdate = models.DateTimeField(db_column='dtIndentDate', blank=True, null=True)  # Field name made lowercase.
    sndentdate = models.CharField(db_column='sndentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dgtreturneddate = models.DateTimeField(db_column='dgtReturnedDate', blank=True, null=True)  # Field name made lowercase.
    sreturneddate = models.CharField(db_column='sReturnedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtissuedate = models.DateTimeField(db_column='dtIssueDate', blank=True, null=True)  # Field name made lowercase.
    sissuedate = models.CharField(db_column='sIssueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
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
    ferrormax = models.FloatField(db_column='fErrorMax', blank=True, null=True)  # Field name made lowercase.
    ferrormin = models.FloatField(db_column='fErrorMin', blank=True, null=True)  # Field name made lowercase.
    ftotalerror1 = models.FloatField(db_column='fTotalError1', blank=True, null=True)  # Field name made lowercase.
    dtrecddate = models.DateTimeField(db_column='dtRecdDate', blank=True, null=True)  # Field name made lowercase.
    srecddate = models.CharField(db_column='sRecdDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtissueddate = models.DateTimeField(db_column='dtIssuedDate', blank=True, null=True)  # Field name made lowercase.
    sissueddate = models.CharField(db_column='sIssuedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scategory = models.CharField(db_column='sCategory', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseordernosinstdesc = models.CharField(db_column='sPurchaseOrderNosInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp1 = models.CharField(db_column='sTemp1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp2 = models.CharField(db_column='sTemp2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp3 = models.CharField(db_column='sTemp3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp4 = models.CharField(db_column='sTemp4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp5 = models.CharField(db_column='sTemp5', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp6 = models.CharField(db_column='sTemp6', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp7 = models.CharField(db_column='sTemp7', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp8 = models.CharField(db_column='sTemp8', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp9 = models.CharField(db_column='sTemp9', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp10 = models.CharField(db_column='sTemp10', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile1 = models.CharField(db_column='sTraceabilityFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath1 = models.CharField(db_column='sTraceabilitypath1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile2 = models.CharField(db_column='sTraceabilityFile2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath2 = models.CharField(db_column='sTraceabilitypath2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile3 = models.CharField(db_column='sTraceabilityFile3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath3 = models.CharField(db_column='sTraceabilitypath3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdcdone = models.BooleanField(db_column='bDCDone', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    spodate = models.CharField(db_column='sPODate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    binternal = models.IntegerField(db_column='bInternal', blank=True, null=True)  # Field name made lowercase.
    bexternal = models.IntegerField(db_column='bExternal', blank=True, null=True)  # Field name made lowercase.
    snablexpirydate = models.CharField(db_column='sNablExpiryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sexternalnablcertificate = models.CharField(db_column='sExternalNABLCertificate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bissued = models.IntegerField(db_column='bIssued', blank=True, null=True)  # Field name made lowercase.
    bapprove = models.IntegerField(db_column='bApprove', blank=True, null=True)  # Field name made lowercase.
    breturned = models.IntegerField(db_column='bReturned', blank=True, null=True)  # Field name made lowercase.
    llastlocationid = models.IntegerField(db_column='lLastLocationID', blank=True, null=True)  # Field name made lowercase.
    lrepairid = models.IntegerField(db_column='lRepairId', blank=True, null=True)  # Field name made lowercase.
    lrecalibrationid = models.IntegerField(db_column='lReCalibrationID', blank=True, null=True)  # Field name made lowercase.
    slaststatus = models.CharField(db_column='sLastStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slastlocation = models.CharField(db_column='sLastLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slastissuedto = models.CharField(db_column='sLastIssuedTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slastmachineto = models.CharField(db_column='sLastMachineTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slastpartnoto = models.CharField(db_column='sLastPartNoTO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMain'


class Thistorymainpart1(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lhistoryid = models.BigIntegerField(db_column='lHistoryID', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid1 = models.BigIntegerField(db_column='lMasterInstrumentID1', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid1 = models.TextField(db_column='sMasterInstrumentId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription1 = models.TextField(db_column='sMasterDescription1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate1 = models.CharField(db_column='sLastCalibrationDate1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate1 = models.CharField(db_column='sNextCalibrationDate1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid2 = models.BigIntegerField(db_column='lMasterInstrumentID2', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid2 = models.TextField(db_column='sMasterInstrumentId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription2 = models.TextField(db_column='sMasterDescription2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate2 = models.CharField(db_column='sLastCalibrationDate2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate2 = models.CharField(db_column='sNextCalibrationDate2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid3 = models.BigIntegerField(db_column='lMasterInstrumentID3', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid3 = models.TextField(db_column='sMasterInstrumentId3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription3 = models.TextField(db_column='sMasterDescription3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate3 = models.CharField(db_column='sLastCalibrationDate3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate3 = models.CharField(db_column='sNextCalibrationDate3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid4 = models.BigIntegerField(db_column='lMasterInstrumentID4', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid4 = models.TextField(db_column='sMasterInstrumentId4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription4 = models.TextField(db_column='sMasterDescription4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate4 = models.CharField(db_column='sLastCalibrationDate4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate4 = models.CharField(db_column='sNextCalibrationDate4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmasterinstrumentid5 = models.BigIntegerField(db_column='lMasterInstrumentID5', blank=True, null=True)  # Field name made lowercase.
    smasterinstrumentid5 = models.TextField(db_column='sMasterInstrumentId5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    smasterdescription5 = models.TextField(db_column='sMasterDescription5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slastcalibrationdate5 = models.CharField(db_column='sLastCalibrationDate5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    snextcalibrationdate5 = models.CharField(db_column='sNextCalibrationDate5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    stypeoffile1 = models.TextField(db_column='sTypeofFile1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile1 = models.TextField(db_column='sFile1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile2 = models.TextField(db_column='sTypeofFile2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile2 = models.TextField(db_column='sFile2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile3 = models.TextField(db_column='sTypeofFile3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile3 = models.TextField(db_column='sFile3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile4 = models.TextField(db_column='sTypeofFile4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile4 = models.TextField(db_column='sFile4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stypeoffile5 = models.TextField(db_column='sTypeofFile5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sfile5 = models.TextField(db_column='sFile5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    suom1 = models.TextField(db_column='sUOM1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue1 = models.TextField(db_column='sAppliedValue1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea1 = models.FloatField(db_column='fAppliedValueA1', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb1 = models.FloatField(db_column='fAppliedValueB1', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec1 = models.FloatField(db_column='fAppliedValueC1', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued1 = models.FloatField(db_column='fAppliedValueD1', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee1 = models.FloatField(db_column='fAppliedValueE1', blank=True, null=True)  # Field name made lowercase.
    derrorallowed1 = models.FloatField(db_column='dErrorAllowed1', blank=True, null=True)  # Field name made lowercase.
    dmax1 = models.FloatField(db_column='dMax1', blank=True, null=True)  # Field name made lowercase.
    dmin1 = models.FloatField(db_column='dMin1', blank=True, null=True)  # Field name made lowercase.
    suom2 = models.TextField(db_column='sUOM2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue2 = models.TextField(db_column='sAppliedValue2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea2 = models.FloatField(db_column='fAppliedValueA2', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb2 = models.FloatField(db_column='fAppliedValueB2', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec2 = models.FloatField(db_column='fAppliedValueC2', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued2 = models.FloatField(db_column='fAppliedValueD2', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee2 = models.FloatField(db_column='fAppliedValueE2', blank=True, null=True)  # Field name made lowercase.
    derrorallowed2 = models.FloatField(db_column='dErrorAllowed2', blank=True, null=True)  # Field name made lowercase.
    dmax2 = models.FloatField(db_column='dMax2', blank=True, null=True)  # Field name made lowercase.
    dmin2 = models.FloatField(db_column='dMin2', blank=True, null=True)  # Field name made lowercase.
    suom3 = models.TextField(db_column='sUOM3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue3 = models.TextField(db_column='sAppliedValue3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea3 = models.FloatField(db_column='fAppliedValueA3', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb3 = models.FloatField(db_column='fAppliedValueB3', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec3 = models.FloatField(db_column='fAppliedValueC3', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued3 = models.FloatField(db_column='fAppliedValueD3', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee3 = models.FloatField(db_column='fAppliedValueE3', blank=True, null=True)  # Field name made lowercase.
    derrorallowed3 = models.FloatField(db_column='dErrorAllowed3', blank=True, null=True)  # Field name made lowercase.
    dmax3 = models.FloatField(db_column='dMax3', blank=True, null=True)  # Field name made lowercase.
    dmin3 = models.FloatField(db_column='dMin3', blank=True, null=True)  # Field name made lowercase.
    suom4 = models.TextField(db_column='sUOM4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue4 = models.TextField(db_column='sAppliedValue4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea4 = models.FloatField(db_column='fAppliedValueA4', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb4 = models.FloatField(db_column='fAppliedValueB4', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec4 = models.FloatField(db_column='fAppliedValueC4', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued4 = models.FloatField(db_column='fAppliedValueD4', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee4 = models.FloatField(db_column='fAppliedValueE4', blank=True, null=True)  # Field name made lowercase.
    derrorallowed4 = models.FloatField(db_column='dErrorAllowed4', blank=True, null=True)  # Field name made lowercase.
    dmax4 = models.FloatField(db_column='dMax4', blank=True, null=True)  # Field name made lowercase.
    dmin4 = models.FloatField(db_column='dMin4', blank=True, null=True)  # Field name made lowercase.
    suom5 = models.TextField(db_column='sUOM5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue5 = models.TextField(db_column='sAppliedValue5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea5 = models.FloatField(db_column='fAppliedValueA5', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb5 = models.FloatField(db_column='fAppliedValueB5', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec5 = models.FloatField(db_column='fAppliedValueC5', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued5 = models.FloatField(db_column='fAppliedValueD5', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee5 = models.FloatField(db_column='fAppliedValueE5', blank=True, null=True)  # Field name made lowercase.
    derrorallowed5 = models.FloatField(db_column='dErrorAllowed5', blank=True, null=True)  # Field name made lowercase.
    dmax5 = models.FloatField(db_column='dMax5', blank=True, null=True)  # Field name made lowercase.
    dmin5 = models.FloatField(db_column='dMin5', blank=True, null=True)  # Field name made lowercase.
    suom6 = models.TextField(db_column='sUOM6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue6 = models.TextField(db_column='sAppliedValue6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea6 = models.FloatField(db_column='fAppliedValueA6', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb6 = models.FloatField(db_column='fAppliedValueB6', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec6 = models.FloatField(db_column='fAppliedValueC6', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued6 = models.FloatField(db_column='fAppliedValueD6', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee6 = models.FloatField(db_column='fAppliedValueE6', blank=True, null=True)  # Field name made lowercase.
    derrorallowed6 = models.FloatField(db_column='dErrorAllowed6', blank=True, null=True)  # Field name made lowercase.
    dmax6 = models.FloatField(db_column='dMax6', blank=True, null=True)  # Field name made lowercase.
    dmin6 = models.FloatField(db_column='dMin6', blank=True, null=True)  # Field name made lowercase.
    suom7 = models.TextField(db_column='sUOM7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue7 = models.TextField(db_column='sAppliedValue7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea7 = models.FloatField(db_column='fAppliedValueA7', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb7 = models.FloatField(db_column='fAppliedValueB7', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec7 = models.FloatField(db_column='fAppliedValueC7', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued7 = models.FloatField(db_column='fAppliedValueD7', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee7 = models.FloatField(db_column='fAppliedValueE7', blank=True, null=True)  # Field name made lowercase.
    derrorallowed7 = models.FloatField(db_column='dErrorAllowed7', blank=True, null=True)  # Field name made lowercase.
    dmax7 = models.FloatField(db_column='dMax7', blank=True, null=True)  # Field name made lowercase.
    dmin7 = models.FloatField(db_column='dMin7', blank=True, null=True)  # Field name made lowercase.
    suom8 = models.TextField(db_column='sUOM8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue8 = models.TextField(db_column='sAppliedValue8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea8 = models.FloatField(db_column='fAppliedValueA8', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb8 = models.FloatField(db_column='fAppliedValueB8', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec8 = models.FloatField(db_column='fAppliedValueC8', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued8 = models.FloatField(db_column='fAppliedValueD8', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee8 = models.FloatField(db_column='fAppliedValueE8', blank=True, null=True)  # Field name made lowercase.
    derrorallowed8 = models.FloatField(db_column='dErrorAllowed8', blank=True, null=True)  # Field name made lowercase.
    dmax8 = models.FloatField(db_column='dMax8', blank=True, null=True)  # Field name made lowercase.
    dmin8 = models.FloatField(db_column='dMin8', blank=True, null=True)  # Field name made lowercase.
    suom9 = models.TextField(db_column='sUOM9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue9 = models.TextField(db_column='sAppliedValue9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea9 = models.FloatField(db_column='fAppliedValueA9', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb9 = models.FloatField(db_column='fAppliedValueB9', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec9 = models.FloatField(db_column='fAppliedValueC9', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued9 = models.FloatField(db_column='fAppliedValueD9', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee9 = models.FloatField(db_column='fAppliedValueE9', blank=True, null=True)  # Field name made lowercase.
    derrorallowed9 = models.FloatField(db_column='dErrorAllowed9', blank=True, null=True)  # Field name made lowercase.
    dmax9 = models.FloatField(db_column='dMax9', blank=True, null=True)  # Field name made lowercase.
    dmin9 = models.FloatField(db_column='dMin9', blank=True, null=True)  # Field name made lowercase.
    suom10 = models.TextField(db_column='sUOM10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue10 = models.TextField(db_column='sAppliedValue10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea10 = models.FloatField(db_column='fAppliedValueA10', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb10 = models.FloatField(db_column='fAppliedValueB10', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec10 = models.FloatField(db_column='fAppliedValueC10', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued10 = models.FloatField(db_column='fAppliedValueD10', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee10 = models.FloatField(db_column='fAppliedValueE10', blank=True, null=True)  # Field name made lowercase.
    derrorallowed10 = models.FloatField(db_column='dErrorAllowed10', blank=True, null=True)  # Field name made lowercase.
    dmax10 = models.FloatField(db_column='dMax10', blank=True, null=True)  # Field name made lowercase.
    dmin10 = models.FloatField(db_column='dMin10', blank=True, null=True)  # Field name made lowercase.
    suom11 = models.TextField(db_column='sUOM11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue11 = models.TextField(db_column='sAppliedValue11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea11 = models.FloatField(db_column='fAppliedValueA11', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb11 = models.FloatField(db_column='fAppliedValueB11', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec11 = models.FloatField(db_column='fAppliedValueC11', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued11 = models.FloatField(db_column='fAppliedValueD11', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee11 = models.FloatField(db_column='fAppliedValueE11', blank=True, null=True)  # Field name made lowercase.
    derrorallowed11 = models.FloatField(db_column='dErrorAllowed11', blank=True, null=True)  # Field name made lowercase.
    dmax11 = models.FloatField(db_column='dMax11', blank=True, null=True)  # Field name made lowercase.
    dmin11 = models.FloatField(db_column='dMin11', blank=True, null=True)  # Field name made lowercase.
    suom12 = models.TextField(db_column='sUOM12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue12 = models.TextField(db_column='sAppliedValue12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea12 = models.FloatField(db_column='fAppliedValueA12', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb12 = models.FloatField(db_column='fAppliedValueB12', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec12 = models.FloatField(db_column='fAppliedValueC12', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued12 = models.FloatField(db_column='fAppliedValueD12', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee12 = models.FloatField(db_column='fAppliedValueE12', blank=True, null=True)  # Field name made lowercase.
    derrorallowed12 = models.FloatField(db_column='dErrorAllowed12', blank=True, null=True)  # Field name made lowercase.
    dmax12 = models.FloatField(db_column='dMax12', blank=True, null=True)  # Field name made lowercase.
    dmin12 = models.FloatField(db_column='dMin12', blank=True, null=True)  # Field name made lowercase.
    suom13 = models.TextField(db_column='sUOM13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue13 = models.TextField(db_column='sAppliedValue13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea13 = models.FloatField(db_column='fAppliedValueA13', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb13 = models.FloatField(db_column='fAppliedValueB13', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec13 = models.FloatField(db_column='fAppliedValueC13', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued13 = models.FloatField(db_column='fAppliedValueD13', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee13 = models.FloatField(db_column='fAppliedValueE13', blank=True, null=True)  # Field name made lowercase.
    derrorallowed13 = models.FloatField(db_column='dErrorAllowed13', blank=True, null=True)  # Field name made lowercase.
    dmax13 = models.FloatField(db_column='dMax13', blank=True, null=True)  # Field name made lowercase.
    dmin13 = models.FloatField(db_column='dMin13', blank=True, null=True)  # Field name made lowercase.
    suom14 = models.TextField(db_column='sUOM14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue14 = models.TextField(db_column='sAppliedValue14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea14 = models.FloatField(db_column='fAppliedValueA14', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb14 = models.FloatField(db_column='fAppliedValueB14', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec14 = models.FloatField(db_column='fAppliedValueC14', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued14 = models.FloatField(db_column='fAppliedValueD14', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee14 = models.FloatField(db_column='fAppliedValueE14', blank=True, null=True)  # Field name made lowercase.
    derrorallowed14 = models.FloatField(db_column='dErrorAllowed14', blank=True, null=True)  # Field name made lowercase.
    dmax14 = models.FloatField(db_column='dMax14', blank=True, null=True)  # Field name made lowercase.
    dmin14 = models.FloatField(db_column='dMin14', blank=True, null=True)  # Field name made lowercase.
    suom15 = models.TextField(db_column='sUOM15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue15 = models.TextField(db_column='sAppliedValue15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea15 = models.FloatField(db_column='fAppliedValueA15', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb15 = models.FloatField(db_column='fAppliedValueB15', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec15 = models.FloatField(db_column='fAppliedValueC15', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued15 = models.FloatField(db_column='fAppliedValueD15', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee15 = models.FloatField(db_column='fAppliedValueE15', blank=True, null=True)  # Field name made lowercase.
    derrorallowed15 = models.FloatField(db_column='dErrorAllowed15', blank=True, null=True)  # Field name made lowercase.
    dmax15 = models.FloatField(db_column='dMax15', blank=True, null=True)  # Field name made lowercase.
    dmin15 = models.FloatField(db_column='dMin15', blank=True, null=True)  # Field name made lowercase.
    suom16 = models.TextField(db_column='sUOM16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue16 = models.TextField(db_column='sAppliedValue16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea16 = models.FloatField(db_column='fAppliedValueA16', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb16 = models.FloatField(db_column='fAppliedValueB16', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec16 = models.FloatField(db_column='fAppliedValueC16', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued16 = models.FloatField(db_column='fAppliedValueD16', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee16 = models.FloatField(db_column='fAppliedValueE16', blank=True, null=True)  # Field name made lowercase.
    derrorallowed16 = models.FloatField(db_column='dErrorAllowed16', blank=True, null=True)  # Field name made lowercase.
    dmax16 = models.FloatField(db_column='dMax16', blank=True, null=True)  # Field name made lowercase.
    dmin16 = models.FloatField(db_column='dMin16', blank=True, null=True)  # Field name made lowercase.
    suom17 = models.TextField(db_column='sUOM17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue17 = models.TextField(db_column='sAppliedValue17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea17 = models.FloatField(db_column='fAppliedValueA17', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb17 = models.FloatField(db_column='fAppliedValueB17', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec17 = models.FloatField(db_column='fAppliedValueC17', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued17 = models.FloatField(db_column='fAppliedValueD17', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee17 = models.FloatField(db_column='fAppliedValueE17', blank=True, null=True)  # Field name made lowercase.
    derrorallowed17 = models.FloatField(db_column='dErrorAllowed17', blank=True, null=True)  # Field name made lowercase.
    dmax17 = models.FloatField(db_column='dMax17', blank=True, null=True)  # Field name made lowercase.
    dmin17 = models.FloatField(db_column='dMin17', blank=True, null=True)  # Field name made lowercase.
    suom18 = models.TextField(db_column='sUOM18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue18 = models.TextField(db_column='sAppliedValue18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea18 = models.FloatField(db_column='fAppliedValueA18', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb18 = models.FloatField(db_column='fAppliedValueB18', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec18 = models.FloatField(db_column='fAppliedValueC18', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued18 = models.FloatField(db_column='fAppliedValueD18', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee18 = models.FloatField(db_column='fAppliedValueE18', blank=True, null=True)  # Field name made lowercase.
    derrorallowed18 = models.FloatField(db_column='dErrorAllowed18', blank=True, null=True)  # Field name made lowercase.
    dmax18 = models.FloatField(db_column='dMax18', blank=True, null=True)  # Field name made lowercase.
    dmin18 = models.FloatField(db_column='dMin18', blank=True, null=True)  # Field name made lowercase.
    suom19 = models.TextField(db_column='sUOM19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue19 = models.TextField(db_column='sAppliedValue19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea19 = models.FloatField(db_column='fAppliedValueA19', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb19 = models.FloatField(db_column='fAppliedValueB19', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec19 = models.FloatField(db_column='fAppliedValueC19', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued19 = models.FloatField(db_column='fAppliedValueD19', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee19 = models.FloatField(db_column='fAppliedValueE19', blank=True, null=True)  # Field name made lowercase.
    derrorallowed19 = models.FloatField(db_column='dErrorAllowed19', blank=True, null=True)  # Field name made lowercase.
    dmax19 = models.FloatField(db_column='dMax19', blank=True, null=True)  # Field name made lowercase.
    dmin19 = models.FloatField(db_column='dMin19', blank=True, null=True)  # Field name made lowercase.
    suom20 = models.TextField(db_column='sUOM20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue20 = models.TextField(db_column='sAppliedValue20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea20 = models.FloatField(db_column='fAppliedValueA20', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb20 = models.FloatField(db_column='fAppliedValueB20', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec20 = models.FloatField(db_column='fAppliedValueC20', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued20 = models.FloatField(db_column='fAppliedValueD20', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee20 = models.FloatField(db_column='fAppliedValueE20', blank=True, null=True)  # Field name made lowercase.
    derrorallowed20 = models.FloatField(db_column='dErrorAllowed20', blank=True, null=True)  # Field name made lowercase.
    dmax20 = models.FloatField(db_column='dMax20', blank=True, null=True)  # Field name made lowercase.
    dmin20 = models.FloatField(db_column='dMin20', blank=True, null=True)  # Field name made lowercase.
    suom21 = models.TextField(db_column='sUOM21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue21 = models.TextField(db_column='sAppliedValue21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea21 = models.FloatField(db_column='fAppliedValueA21', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb21 = models.FloatField(db_column='fAppliedValueB21', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec21 = models.FloatField(db_column='fAppliedValueC21', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued21 = models.FloatField(db_column='fAppliedValueD21', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee21 = models.FloatField(db_column='fAppliedValueE21', blank=True, null=True)  # Field name made lowercase.
    derrorallowed21 = models.FloatField(db_column='dErrorAllowed21', blank=True, null=True)  # Field name made lowercase.
    dmax21 = models.FloatField(db_column='dMax21', blank=True, null=True)  # Field name made lowercase.
    dmin21 = models.FloatField(db_column='dMin21', blank=True, null=True)  # Field name made lowercase.
    suom22 = models.TextField(db_column='sUOM22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue22 = models.TextField(db_column='sAppliedValue22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea22 = models.FloatField(db_column='fAppliedValueA22', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb22 = models.FloatField(db_column='fAppliedValueB22', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec22 = models.FloatField(db_column='fAppliedValueC22', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued22 = models.FloatField(db_column='fAppliedValueD22', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee22 = models.FloatField(db_column='fAppliedValueE22', blank=True, null=True)  # Field name made lowercase.
    derrorallowed22 = models.FloatField(db_column='dErrorAllowed22', blank=True, null=True)  # Field name made lowercase.
    dmax22 = models.FloatField(db_column='dMax22', blank=True, null=True)  # Field name made lowercase.
    dmin22 = models.FloatField(db_column='dMin22', blank=True, null=True)  # Field name made lowercase.
    suom23 = models.TextField(db_column='sUOM23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue23 = models.TextField(db_column='sAppliedValue23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea23 = models.FloatField(db_column='fAppliedValueA23', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb23 = models.FloatField(db_column='fAppliedValueB23', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec23 = models.FloatField(db_column='fAppliedValueC23', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued23 = models.FloatField(db_column='fAppliedValueD23', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee23 = models.FloatField(db_column='fAppliedValueE23', blank=True, null=True)  # Field name made lowercase.
    derrorallowed23 = models.FloatField(db_column='dErrorAllowed23', blank=True, null=True)  # Field name made lowercase.
    dmax23 = models.FloatField(db_column='dMax23', blank=True, null=True)  # Field name made lowercase.
    dmin23 = models.FloatField(db_column='dMin23', blank=True, null=True)  # Field name made lowercase.
    suom24 = models.TextField(db_column='sUOM24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue24 = models.TextField(db_column='sAppliedValue24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea24 = models.FloatField(db_column='fAppliedValueA24', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb24 = models.FloatField(db_column='fAppliedValueB24', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec24 = models.FloatField(db_column='fAppliedValueC24', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued24 = models.FloatField(db_column='fAppliedValueD24', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee24 = models.FloatField(db_column='fAppliedValueE24', blank=True, null=True)  # Field name made lowercase.
    derrorallowed24 = models.FloatField(db_column='dErrorAllowed24', blank=True, null=True)  # Field name made lowercase.
    dmax24 = models.FloatField(db_column='dMax24', blank=True, null=True)  # Field name made lowercase.
    dmin24 = models.FloatField(db_column='dMin24', blank=True, null=True)  # Field name made lowercase.
    suom25 = models.TextField(db_column='sUOM25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue25 = models.TextField(db_column='sAppliedValue25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea25 = models.FloatField(db_column='fAppliedValueA25', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb25 = models.FloatField(db_column='fAppliedValueB25', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec25 = models.FloatField(db_column='fAppliedValueC25', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued25 = models.FloatField(db_column='fAppliedValueD25', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee25 = models.FloatField(db_column='fAppliedValueE25', blank=True, null=True)  # Field name made lowercase.
    derrorallowed25 = models.FloatField(db_column='dErrorAllowed25', blank=True, null=True)  # Field name made lowercase.
    dmax25 = models.FloatField(db_column='dMax25', blank=True, null=True)  # Field name made lowercase.
    dmin25 = models.FloatField(db_column='dMin25', blank=True, null=True)  # Field name made lowercase.
    suom26 = models.TextField(db_column='sUOM26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue26 = models.TextField(db_column='sAppliedValue26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea26 = models.FloatField(db_column='fAppliedValueA26', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb26 = models.FloatField(db_column='fAppliedValueB26', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec26 = models.FloatField(db_column='fAppliedValueC26', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued26 = models.FloatField(db_column='fAppliedValueD26', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee26 = models.FloatField(db_column='fAppliedValueE26', blank=True, null=True)  # Field name made lowercase.
    derrorallowed26 = models.FloatField(db_column='dErrorAllowed26', blank=True, null=True)  # Field name made lowercase.
    dmax26 = models.FloatField(db_column='dMax26', blank=True, null=True)  # Field name made lowercase.
    dmin26 = models.FloatField(db_column='dMin26', blank=True, null=True)  # Field name made lowercase.
    suom27 = models.TextField(db_column='sUOM27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue27 = models.TextField(db_column='sAppliedValue27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea27 = models.FloatField(db_column='fAppliedValueA27', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb27 = models.FloatField(db_column='fAppliedValueB27', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec27 = models.FloatField(db_column='fAppliedValueC27', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued27 = models.FloatField(db_column='fAppliedValueD27', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee27 = models.FloatField(db_column='fAppliedValueE27', blank=True, null=True)  # Field name made lowercase.
    derrorallowed27 = models.FloatField(db_column='dErrorAllowed27', blank=True, null=True)  # Field name made lowercase.
    dmax27 = models.FloatField(db_column='dMax27', blank=True, null=True)  # Field name made lowercase.
    dmin27 = models.FloatField(db_column='dMin27', blank=True, null=True)  # Field name made lowercase.
    suom28 = models.TextField(db_column='sUOM28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue28 = models.TextField(db_column='sAppliedValue28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea28 = models.FloatField(db_column='fAppliedValueA28', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb28 = models.FloatField(db_column='fAppliedValueB28', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec28 = models.FloatField(db_column='fAppliedValueC28', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued28 = models.FloatField(db_column='fAppliedValueD28', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee28 = models.FloatField(db_column='fAppliedValueE28', blank=True, null=True)  # Field name made lowercase.
    derrorallowed28 = models.FloatField(db_column='dErrorAllowed28', blank=True, null=True)  # Field name made lowercase.
    dmax28 = models.FloatField(db_column='dMax28', blank=True, null=True)  # Field name made lowercase.
    dmin28 = models.FloatField(db_column='dMin28', blank=True, null=True)  # Field name made lowercase.
    suom29 = models.TextField(db_column='sUOM29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue29 = models.TextField(db_column='sAppliedValue29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea29 = models.FloatField(db_column='fAppliedValueA29', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb29 = models.FloatField(db_column='fAppliedValueB29', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec29 = models.FloatField(db_column='fAppliedValueC29', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued29 = models.FloatField(db_column='fAppliedValueD29', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee29 = models.FloatField(db_column='fAppliedValueE29', blank=True, null=True)  # Field name made lowercase.
    derrorallowed29 = models.FloatField(db_column='dErrorAllowed29', blank=True, null=True)  # Field name made lowercase.
    dmax29 = models.FloatField(db_column='dMax29', blank=True, null=True)  # Field name made lowercase.
    dmin29 = models.FloatField(db_column='dMin29', blank=True, null=True)  # Field name made lowercase.
    suom30 = models.TextField(db_column='sUOM30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sappliedvalue30 = models.TextField(db_column='sAppliedValue30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fappliedvaluea30 = models.FloatField(db_column='fAppliedValueA30', blank=True, null=True)  # Field name made lowercase.
    fappliedvalueb30 = models.FloatField(db_column='fAppliedValueB30', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluec30 = models.FloatField(db_column='fAppliedValueC30', blank=True, null=True)  # Field name made lowercase.
    fappliedvalued30 = models.FloatField(db_column='fAppliedValueD30', blank=True, null=True)  # Field name made lowercase.
    fappliedvaluee30 = models.FloatField(db_column='fAppliedValueE30', blank=True, null=True)  # Field name made lowercase.
    derrorallowed30 = models.FloatField(db_column='dErrorAllowed30', blank=True, null=True)  # Field name made lowercase.
    dmax30 = models.FloatField(db_column='dMax30', blank=True, null=True)  # Field name made lowercase.
    dmin30 = models.FloatField(db_column='dMin30', blank=True, null=True)  # Field name made lowercase.
    lhistorytraceid1 = models.IntegerField(db_column='lHistoryTraceID1', blank=True, null=True)  # Field name made lowercase.
    lhistorytraceid2 = models.IntegerField(db_column='lHistoryTraceID2', blank=True, null=True)  # Field name made lowercase.
    lhistorytraceid3 = models.IntegerField(db_column='lHistoryTraceID3', blank=True, null=True)  # Field name made lowercase.
    lhistorytraceid4 = models.IntegerField(db_column='lHistoryTraceID4', blank=True, null=True)  # Field name made lowercase.
    lhistorytraceid5 = models.IntegerField(db_column='lHistoryTraceID5', blank=True, null=True)  # Field name made lowercase.
    shistorytraceid1 = models.CharField(db_column='sHistoryTraceID1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shistorytraceid2 = models.CharField(db_column='sHistoryTraceID2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shistorytraceid3 = models.CharField(db_column='sHistoryTraceID3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shistorytraceid4 = models.CharField(db_column='sHistoryTraceID4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shistorytraceid5 = models.CharField(db_column='sHistoryTraceID5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMainPart1'


class Thistorymainpart2(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lhistoryid = models.BigIntegerField(db_column='lHistoryID', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    factualvaluea1 = models.FloatField(db_column='fActualValueA1', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa1 = models.FloatField(db_column='fActualValueAA1', blank=True, null=True)  # Field name made lowercase.
    factualvalueb1 = models.FloatField(db_column='fActualValueB1', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb1 = models.FloatField(db_column='fActualValueBB1', blank=True, null=True)  # Field name made lowercase.
    factualvaluec1 = models.FloatField(db_column='fActualValueC1', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc1 = models.FloatField(db_column='fActualValueCC1', blank=True, null=True)  # Field name made lowercase.
    factualvalued1 = models.FloatField(db_column='fActualValueD1', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd1 = models.FloatField(db_column='fActualValueDD1', blank=True, null=True)  # Field name made lowercase.
    factualvaluee1 = models.FloatField(db_column='fActualValueE1', blank=True, null=True)  # Field name made lowercase.
    factualvalueee1 = models.FloatField(db_column='fActualValueEE1', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult1 = models.TextField(db_column='sBeforeResult1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok1 = models.IntegerField(db_column='bBeforeOK1', blank=True, null=True)  # Field name made lowercase.
    safterresult1 = models.TextField(db_column='sAfterResult1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok1 = models.IntegerField(db_column='bAfterOK1', blank=True, null=True)  # Field name made lowercase.
    factualberror1 = models.FloatField(db_column='fActualBError1', blank=True, null=True)  # Field name made lowercase.
    factualaerror1 = models.FloatField(db_column='fActualAError1', blank=True, null=True)  # Field name made lowercase.
    factualvaluea2 = models.FloatField(db_column='fActualValueA2', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa2 = models.FloatField(db_column='fActualValueAA2', blank=True, null=True)  # Field name made lowercase.
    factualvalueb2 = models.FloatField(db_column='fActualValueB2', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb2 = models.FloatField(db_column='fActualValueBB2', blank=True, null=True)  # Field name made lowercase.
    factualvaluec2 = models.FloatField(db_column='fActualValueC2', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc2 = models.FloatField(db_column='fActualValueCC2', blank=True, null=True)  # Field name made lowercase.
    factualvalued2 = models.FloatField(db_column='fActualValueD2', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd2 = models.FloatField(db_column='fActualValueDD2', blank=True, null=True)  # Field name made lowercase.
    factualvaluee2 = models.FloatField(db_column='fActualValueE2', blank=True, null=True)  # Field name made lowercase.
    factualvalueee2 = models.FloatField(db_column='fActualValueEE2', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult2 = models.TextField(db_column='sBeforeResult2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok2 = models.IntegerField(db_column='bBeforeOK2', blank=True, null=True)  # Field name made lowercase.
    safterresult2 = models.TextField(db_column='sAfterResult2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok2 = models.IntegerField(db_column='bAfterOK2', blank=True, null=True)  # Field name made lowercase.
    factualberror2 = models.FloatField(db_column='fActualBError2', blank=True, null=True)  # Field name made lowercase.
    factualaerror2 = models.FloatField(db_column='fActualAError2', blank=True, null=True)  # Field name made lowercase.
    factualvaluea3 = models.FloatField(db_column='fActualValueA3', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa3 = models.FloatField(db_column='fActualValueAA3', blank=True, null=True)  # Field name made lowercase.
    factualvalueb3 = models.FloatField(db_column='fActualValueB3', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb3 = models.FloatField(db_column='fActualValueBB3', blank=True, null=True)  # Field name made lowercase.
    factualvaluec3 = models.FloatField(db_column='fActualValueC3', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc3 = models.FloatField(db_column='fActualValueCC3', blank=True, null=True)  # Field name made lowercase.
    factualvalued3 = models.FloatField(db_column='fActualValueD3', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd3 = models.FloatField(db_column='fActualValueDD3', blank=True, null=True)  # Field name made lowercase.
    factualvaluee3 = models.FloatField(db_column='fActualValueE3', blank=True, null=True)  # Field name made lowercase.
    factualvalueee3 = models.FloatField(db_column='fActualValueEE3', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult3 = models.TextField(db_column='sBeforeResult3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok3 = models.IntegerField(db_column='bBeforeOK3', blank=True, null=True)  # Field name made lowercase.
    safterresult3 = models.TextField(db_column='sAfterResult3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok3 = models.IntegerField(db_column='bAfterOK3', blank=True, null=True)  # Field name made lowercase.
    factualberror3 = models.FloatField(db_column='fActualBError3', blank=True, null=True)  # Field name made lowercase.
    factualaerror3 = models.FloatField(db_column='fActualAError3', blank=True, null=True)  # Field name made lowercase.
    factualvaluea4 = models.FloatField(db_column='fActualValueA4', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa4 = models.FloatField(db_column='fActualValueAA4', blank=True, null=True)  # Field name made lowercase.
    factualvalueb4 = models.FloatField(db_column='fActualValueB4', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb4 = models.FloatField(db_column='fActualValueBB4', blank=True, null=True)  # Field name made lowercase.
    factualvaluec4 = models.FloatField(db_column='fActualValueC4', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc4 = models.FloatField(db_column='fActualValueCC4', blank=True, null=True)  # Field name made lowercase.
    factualvalued4 = models.FloatField(db_column='fActualValueD4', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd4 = models.FloatField(db_column='fActualValueDD4', blank=True, null=True)  # Field name made lowercase.
    factualvaluee4 = models.FloatField(db_column='fActualValueE4', blank=True, null=True)  # Field name made lowercase.
    factualvalueee4 = models.FloatField(db_column='fActualValueEE4', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult4 = models.TextField(db_column='sBeforeResult4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok4 = models.IntegerField(db_column='bBeforeOK4', blank=True, null=True)  # Field name made lowercase.
    safterresult4 = models.TextField(db_column='sAfterResult4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok4 = models.IntegerField(db_column='bAfterOK4', blank=True, null=True)  # Field name made lowercase.
    factualberror4 = models.FloatField(db_column='fActualBError4', blank=True, null=True)  # Field name made lowercase.
    factualaerror4 = models.FloatField(db_column='fActualAError4', blank=True, null=True)  # Field name made lowercase.
    factualvaluea5 = models.FloatField(db_column='fActualValueA5', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa5 = models.FloatField(db_column='fActualValueAA5', blank=True, null=True)  # Field name made lowercase.
    factualvalueb5 = models.FloatField(db_column='fActualValueB5', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb5 = models.FloatField(db_column='fActualValueBB5', blank=True, null=True)  # Field name made lowercase.
    factualvaluec5 = models.FloatField(db_column='fActualValueC5', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc5 = models.FloatField(db_column='fActualValueCC5', blank=True, null=True)  # Field name made lowercase.
    factualvalued5 = models.FloatField(db_column='fActualValueD5', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd5 = models.FloatField(db_column='fActualValueDD5', blank=True, null=True)  # Field name made lowercase.
    factualvaluee5 = models.FloatField(db_column='fActualValueE5', blank=True, null=True)  # Field name made lowercase.
    factualvalueee5 = models.FloatField(db_column='fActualValueEE5', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult5 = models.TextField(db_column='sBeforeResult5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok5 = models.IntegerField(db_column='bBeforeOK5', blank=True, null=True)  # Field name made lowercase.
    safterresult5 = models.TextField(db_column='sAfterResult5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok5 = models.IntegerField(db_column='bAfterOK5', blank=True, null=True)  # Field name made lowercase.
    factualberror5 = models.FloatField(db_column='fActualBError5', blank=True, null=True)  # Field name made lowercase.
    factualaerror5 = models.FloatField(db_column='fActualAError5', blank=True, null=True)  # Field name made lowercase.
    factualvaluea6 = models.FloatField(db_column='fActualValueA6', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa6 = models.FloatField(db_column='fActualValueAA6', blank=True, null=True)  # Field name made lowercase.
    factualvalueb6 = models.FloatField(db_column='fActualValueB6', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb6 = models.FloatField(db_column='fActualValueBB6', blank=True, null=True)  # Field name made lowercase.
    factualvaluec6 = models.FloatField(db_column='fActualValueC6', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc6 = models.FloatField(db_column='fActualValueCC6', blank=True, null=True)  # Field name made lowercase.
    factualvalued6 = models.FloatField(db_column='fActualValueD6', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd6 = models.FloatField(db_column='fActualValueDD6', blank=True, null=True)  # Field name made lowercase.
    factualvaluee6 = models.FloatField(db_column='fActualValueE6', blank=True, null=True)  # Field name made lowercase.
    factualvalueee6 = models.FloatField(db_column='fActualValueEE6', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult6 = models.TextField(db_column='sBeforeResult6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok6 = models.IntegerField(db_column='bBeforeOK6', blank=True, null=True)  # Field name made lowercase.
    safterresult6 = models.TextField(db_column='sAfterResult6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok6 = models.IntegerField(db_column='bAfterOK6', blank=True, null=True)  # Field name made lowercase.
    factualberror6 = models.FloatField(db_column='fActualBError6', blank=True, null=True)  # Field name made lowercase.
    factualaerror6 = models.FloatField(db_column='fActualAError6', blank=True, null=True)  # Field name made lowercase.
    factualvaluea7 = models.FloatField(db_column='fActualValueA7', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa7 = models.FloatField(db_column='fActualValueAA7', blank=True, null=True)  # Field name made lowercase.
    factualvalueb7 = models.FloatField(db_column='fActualValueB7', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb7 = models.FloatField(db_column='fActualValueBB7', blank=True, null=True)  # Field name made lowercase.
    factualvaluec7 = models.FloatField(db_column='fActualValueC7', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc7 = models.FloatField(db_column='fActualValueCC7', blank=True, null=True)  # Field name made lowercase.
    factualvalued7 = models.FloatField(db_column='fActualValueD7', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd7 = models.FloatField(db_column='fActualValueDD7', blank=True, null=True)  # Field name made lowercase.
    factualvaluee7 = models.FloatField(db_column='fActualValueE7', blank=True, null=True)  # Field name made lowercase.
    factualvalueee7 = models.FloatField(db_column='fActualValueEE7', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult7 = models.TextField(db_column='sBeforeResult7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok7 = models.IntegerField(db_column='bBeforeOK7', blank=True, null=True)  # Field name made lowercase.
    safterresult7 = models.TextField(db_column='sAfterResult7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok7 = models.IntegerField(db_column='bAfterOK7', blank=True, null=True)  # Field name made lowercase.
    factualberror7 = models.FloatField(db_column='fActualBError7', blank=True, null=True)  # Field name made lowercase.
    factualaerror7 = models.FloatField(db_column='fActualAError7', blank=True, null=True)  # Field name made lowercase.
    factualvaluea8 = models.FloatField(db_column='fActualValueA8', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa8 = models.FloatField(db_column='fActualValueAA8', blank=True, null=True)  # Field name made lowercase.
    factualvalueb8 = models.FloatField(db_column='fActualValueB8', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb8 = models.FloatField(db_column='fActualValueBB8', blank=True, null=True)  # Field name made lowercase.
    factualvaluec8 = models.FloatField(db_column='fActualValueC8', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc8 = models.FloatField(db_column='fActualValueCC8', blank=True, null=True)  # Field name made lowercase.
    factualvalued8 = models.FloatField(db_column='fActualValueD8', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd8 = models.FloatField(db_column='fActualValueDD8', blank=True, null=True)  # Field name made lowercase.
    factualvaluee8 = models.FloatField(db_column='fActualValueE8', blank=True, null=True)  # Field name made lowercase.
    factualvalueee8 = models.FloatField(db_column='fActualValueEE8', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult8 = models.TextField(db_column='sBeforeResult8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok8 = models.IntegerField(db_column='bBeforeOK8', blank=True, null=True)  # Field name made lowercase.
    safterresult8 = models.TextField(db_column='sAfterResult8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok8 = models.IntegerField(db_column='bAfterOK8', blank=True, null=True)  # Field name made lowercase.
    factualberror8 = models.FloatField(db_column='fActualBError8', blank=True, null=True)  # Field name made lowercase.
    factualaerror8 = models.FloatField(db_column='fActualAError8', blank=True, null=True)  # Field name made lowercase.
    factualvaluea9 = models.FloatField(db_column='fActualValueA9', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa9 = models.FloatField(db_column='fActualValueAA9', blank=True, null=True)  # Field name made lowercase.
    factualvalueb9 = models.FloatField(db_column='fActualValueB9', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb9 = models.FloatField(db_column='fActualValueBB9', blank=True, null=True)  # Field name made lowercase.
    factualvaluec9 = models.FloatField(db_column='fActualValueC9', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc9 = models.FloatField(db_column='fActualValueCC9', blank=True, null=True)  # Field name made lowercase.
    factualvalued9 = models.FloatField(db_column='fActualValueD9', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd9 = models.FloatField(db_column='fActualValueDD9', blank=True, null=True)  # Field name made lowercase.
    factualvaluee9 = models.FloatField(db_column='fActualValueE9', blank=True, null=True)  # Field name made lowercase.
    factualvalueee9 = models.FloatField(db_column='fActualValueEE9', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult9 = models.TextField(db_column='sBeforeResult9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok9 = models.IntegerField(db_column='bBeforeOK9', blank=True, null=True)  # Field name made lowercase.
    safterresult9 = models.TextField(db_column='sAfterResult9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok9 = models.IntegerField(db_column='bAfterOK9', blank=True, null=True)  # Field name made lowercase.
    factualberror9 = models.FloatField(db_column='fActualBError9', blank=True, null=True)  # Field name made lowercase.
    factualaerror9 = models.FloatField(db_column='fActualAError9', blank=True, null=True)  # Field name made lowercase.
    factualvaluea10 = models.FloatField(db_column='fActualValueA10', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa10 = models.FloatField(db_column='fActualValueAA10', blank=True, null=True)  # Field name made lowercase.
    factualvalueb10 = models.FloatField(db_column='fActualValueB10', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb10 = models.FloatField(db_column='fActualValueBB10', blank=True, null=True)  # Field name made lowercase.
    factualvaluec10 = models.FloatField(db_column='fActualValueC10', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc10 = models.FloatField(db_column='fActualValueCC10', blank=True, null=True)  # Field name made lowercase.
    factualvalued10 = models.FloatField(db_column='fActualValueD10', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd10 = models.FloatField(db_column='fActualValueDD10', blank=True, null=True)  # Field name made lowercase.
    factualvaluee10 = models.FloatField(db_column='fActualValueE10', blank=True, null=True)  # Field name made lowercase.
    factualvalueee10 = models.FloatField(db_column='fActualValueEE10', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult10 = models.TextField(db_column='sBeforeResult10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok10 = models.IntegerField(db_column='bBeforeOK10', blank=True, null=True)  # Field name made lowercase.
    safterresult10 = models.TextField(db_column='sAfterResult10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok10 = models.IntegerField(db_column='bAfterOK10', blank=True, null=True)  # Field name made lowercase.
    factualberror10 = models.FloatField(db_column='fActualBError10', blank=True, null=True)  # Field name made lowercase.
    factualaerror10 = models.FloatField(db_column='fActualAError10', blank=True, null=True)  # Field name made lowercase.
    factualvaluea11 = models.FloatField(db_column='fActualValueA11', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa11 = models.FloatField(db_column='fActualValueAA11', blank=True, null=True)  # Field name made lowercase.
    factualvalueb11 = models.FloatField(db_column='fActualValueB11', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb11 = models.FloatField(db_column='fActualValueBB11', blank=True, null=True)  # Field name made lowercase.
    factualvaluec11 = models.FloatField(db_column='fActualValueC11', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc11 = models.FloatField(db_column='fActualValueCC11', blank=True, null=True)  # Field name made lowercase.
    factualvalued11 = models.FloatField(db_column='fActualValueD11', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd11 = models.FloatField(db_column='fActualValueDD11', blank=True, null=True)  # Field name made lowercase.
    factualvaluee11 = models.FloatField(db_column='fActualValueE11', blank=True, null=True)  # Field name made lowercase.
    factualvalueee11 = models.FloatField(db_column='fActualValueEE11', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult11 = models.TextField(db_column='sBeforeResult11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok11 = models.IntegerField(db_column='bBeforeOK11', blank=True, null=True)  # Field name made lowercase.
    safterresult11 = models.TextField(db_column='sAfterResult11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok11 = models.IntegerField(db_column='bAfterOK11', blank=True, null=True)  # Field name made lowercase.
    factualberror11 = models.FloatField(db_column='fActualBError11', blank=True, null=True)  # Field name made lowercase.
    factualaerror11 = models.FloatField(db_column='fActualAError11', blank=True, null=True)  # Field name made lowercase.
    factualvaluea12 = models.FloatField(db_column='fActualValueA12', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa12 = models.FloatField(db_column='fActualValueAA12', blank=True, null=True)  # Field name made lowercase.
    factualvalueb12 = models.FloatField(db_column='fActualValueB12', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb12 = models.FloatField(db_column='fActualValueBB12', blank=True, null=True)  # Field name made lowercase.
    factualvaluec12 = models.FloatField(db_column='fActualValueC12', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc12 = models.FloatField(db_column='fActualValueCC12', blank=True, null=True)  # Field name made lowercase.
    factualvalued12 = models.FloatField(db_column='fActualValueD12', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd12 = models.FloatField(db_column='fActualValueDD12', blank=True, null=True)  # Field name made lowercase.
    factualvaluee12 = models.FloatField(db_column='fActualValueE12', blank=True, null=True)  # Field name made lowercase.
    factualvalueee12 = models.FloatField(db_column='fActualValueEE12', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult12 = models.TextField(db_column='sBeforeResult12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok12 = models.IntegerField(db_column='bBeforeOK12', blank=True, null=True)  # Field name made lowercase.
    safterresult12 = models.TextField(db_column='sAfterResult12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok12 = models.IntegerField(db_column='bAfterOK12', blank=True, null=True)  # Field name made lowercase.
    factualberror12 = models.FloatField(db_column='fActualBError12', blank=True, null=True)  # Field name made lowercase.
    factualaerror12 = models.FloatField(db_column='fActualAError12', blank=True, null=True)  # Field name made lowercase.
    factualvaluea13 = models.FloatField(db_column='fActualValueA13', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa13 = models.FloatField(db_column='fActualValueAA13', blank=True, null=True)  # Field name made lowercase.
    factualvalueb13 = models.FloatField(db_column='fActualValueB13', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb13 = models.FloatField(db_column='fActualValueBB13', blank=True, null=True)  # Field name made lowercase.
    factualvaluec13 = models.FloatField(db_column='fActualValueC13', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc13 = models.FloatField(db_column='fActualValueCC13', blank=True, null=True)  # Field name made lowercase.
    factualvalued13 = models.FloatField(db_column='fActualValueD13', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd13 = models.FloatField(db_column='fActualValueDD13', blank=True, null=True)  # Field name made lowercase.
    factualvaluee13 = models.FloatField(db_column='fActualValueE13', blank=True, null=True)  # Field name made lowercase.
    factualvalueee13 = models.FloatField(db_column='fActualValueEE13', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult13 = models.TextField(db_column='sBeforeResult13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok13 = models.IntegerField(db_column='bBeforeOK13', blank=True, null=True)  # Field name made lowercase.
    safterresult13 = models.TextField(db_column='sAfterResult13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok13 = models.IntegerField(db_column='bAfterOK13', blank=True, null=True)  # Field name made lowercase.
    factualberror13 = models.FloatField(db_column='fActualBError13', blank=True, null=True)  # Field name made lowercase.
    factualaerror13 = models.FloatField(db_column='fActualAError13', blank=True, null=True)  # Field name made lowercase.
    factualvaluea14 = models.FloatField(db_column='fActualValueA14', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa14 = models.FloatField(db_column='fActualValueAA14', blank=True, null=True)  # Field name made lowercase.
    factualvalueb14 = models.FloatField(db_column='fActualValueB14', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb14 = models.FloatField(db_column='fActualValueBB14', blank=True, null=True)  # Field name made lowercase.
    factualvaluec14 = models.FloatField(db_column='fActualValueC14', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc14 = models.FloatField(db_column='fActualValueCC14', blank=True, null=True)  # Field name made lowercase.
    factualvalued14 = models.FloatField(db_column='fActualValueD14', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd14 = models.FloatField(db_column='fActualValueDD14', blank=True, null=True)  # Field name made lowercase.
    factualvaluee14 = models.FloatField(db_column='fActualValueE14', blank=True, null=True)  # Field name made lowercase.
    factualvalueee14 = models.FloatField(db_column='fActualValueEE14', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult14 = models.TextField(db_column='sBeforeResult14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok14 = models.IntegerField(db_column='bBeforeOK14', blank=True, null=True)  # Field name made lowercase.
    safterresult14 = models.TextField(db_column='sAfterResult14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok14 = models.IntegerField(db_column='bAfterOK14', blank=True, null=True)  # Field name made lowercase.
    factualberror14 = models.FloatField(db_column='fActualBError14', blank=True, null=True)  # Field name made lowercase.
    factualaerror14 = models.FloatField(db_column='fActualAError14', blank=True, null=True)  # Field name made lowercase.
    factualvaluea15 = models.FloatField(db_column='fActualValueA15', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa15 = models.FloatField(db_column='fActualValueAA15', blank=True, null=True)  # Field name made lowercase.
    factualvalueb15 = models.FloatField(db_column='fActualValueB15', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb15 = models.FloatField(db_column='fActualValueBB15', blank=True, null=True)  # Field name made lowercase.
    factualvaluec15 = models.FloatField(db_column='fActualValueC15', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc15 = models.FloatField(db_column='fActualValueCC15', blank=True, null=True)  # Field name made lowercase.
    factualvalued15 = models.FloatField(db_column='fActualValueD15', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd15 = models.FloatField(db_column='fActualValueDD15', blank=True, null=True)  # Field name made lowercase.
    factualvaluee15 = models.FloatField(db_column='fActualValueE15', blank=True, null=True)  # Field name made lowercase.
    factualvalueee15 = models.FloatField(db_column='fActualValueEE15', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult15 = models.TextField(db_column='sBeforeResult15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok15 = models.IntegerField(db_column='bBeforeOK15', blank=True, null=True)  # Field name made lowercase.
    safterresult15 = models.TextField(db_column='sAfterResult15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok15 = models.IntegerField(db_column='bAfterOK15', blank=True, null=True)  # Field name made lowercase.
    factualberror15 = models.FloatField(db_column='fActualBError15', blank=True, null=True)  # Field name made lowercase.
    factualaerror15 = models.FloatField(db_column='fActualAError15', blank=True, null=True)  # Field name made lowercase.
    factualvaluea16 = models.FloatField(db_column='fActualValueA16', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa16 = models.FloatField(db_column='fActualValueAA16', blank=True, null=True)  # Field name made lowercase.
    factualvalueb16 = models.FloatField(db_column='fActualValueB16', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb16 = models.FloatField(db_column='fActualValueBB16', blank=True, null=True)  # Field name made lowercase.
    factualvaluec16 = models.FloatField(db_column='fActualValueC16', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc16 = models.FloatField(db_column='fActualValueCC16', blank=True, null=True)  # Field name made lowercase.
    factualvalued16 = models.FloatField(db_column='fActualValueD16', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd16 = models.FloatField(db_column='fActualValueDD16', blank=True, null=True)  # Field name made lowercase.
    factualvaluee16 = models.FloatField(db_column='fActualValueE16', blank=True, null=True)  # Field name made lowercase.
    factualvalueee16 = models.FloatField(db_column='fActualValueEE16', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult16 = models.TextField(db_column='sBeforeResult16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok16 = models.IntegerField(db_column='bBeforeOK16', blank=True, null=True)  # Field name made lowercase.
    safterresult16 = models.TextField(db_column='sAfterResult16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok16 = models.IntegerField(db_column='bAfterOK16', blank=True, null=True)  # Field name made lowercase.
    factualberror16 = models.FloatField(db_column='fActualBError16', blank=True, null=True)  # Field name made lowercase.
    factualaerror16 = models.FloatField(db_column='fActualAError16', blank=True, null=True)  # Field name made lowercase.
    factualvaluea17 = models.FloatField(db_column='fActualValueA17', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa17 = models.FloatField(db_column='fActualValueAA17', blank=True, null=True)  # Field name made lowercase.
    factualvalueb17 = models.FloatField(db_column='fActualValueB17', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb17 = models.FloatField(db_column='fActualValueBB17', blank=True, null=True)  # Field name made lowercase.
    factualvaluec17 = models.FloatField(db_column='fActualValueC17', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc17 = models.FloatField(db_column='fActualValueCC17', blank=True, null=True)  # Field name made lowercase.
    factualvalued17 = models.FloatField(db_column='fActualValueD17', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd17 = models.FloatField(db_column='fActualValueDD17', blank=True, null=True)  # Field name made lowercase.
    factualvaluee17 = models.FloatField(db_column='fActualValueE17', blank=True, null=True)  # Field name made lowercase.
    factualvalueee17 = models.FloatField(db_column='fActualValueEE17', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult17 = models.TextField(db_column='sBeforeResult17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok17 = models.IntegerField(db_column='bBeforeOK17', blank=True, null=True)  # Field name made lowercase.
    safterresult17 = models.TextField(db_column='sAfterResult17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok17 = models.IntegerField(db_column='bAfterOK17', blank=True, null=True)  # Field name made lowercase.
    factualberror17 = models.FloatField(db_column='fActualBError17', blank=True, null=True)  # Field name made lowercase.
    factualaerror17 = models.FloatField(db_column='fActualAError17', blank=True, null=True)  # Field name made lowercase.
    factualvaluea18 = models.FloatField(db_column='fActualValueA18', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa18 = models.FloatField(db_column='fActualValueAA18', blank=True, null=True)  # Field name made lowercase.
    factualvalueb18 = models.FloatField(db_column='fActualValueB18', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb18 = models.FloatField(db_column='fActualValueBB18', blank=True, null=True)  # Field name made lowercase.
    factualvaluec18 = models.FloatField(db_column='fActualValueC18', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc18 = models.FloatField(db_column='fActualValueCC18', blank=True, null=True)  # Field name made lowercase.
    factualvalued18 = models.FloatField(db_column='fActualValueD18', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd18 = models.FloatField(db_column='fActualValueDD18', blank=True, null=True)  # Field name made lowercase.
    factualvaluee18 = models.FloatField(db_column='fActualValueE18', blank=True, null=True)  # Field name made lowercase.
    factualvalueee18 = models.FloatField(db_column='fActualValueEE18', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult18 = models.TextField(db_column='sBeforeResult18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok18 = models.IntegerField(db_column='bBeforeOK18', blank=True, null=True)  # Field name made lowercase.
    safterresult18 = models.TextField(db_column='sAfterResult18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok18 = models.IntegerField(db_column='bAfterOK18', blank=True, null=True)  # Field name made lowercase.
    factualberror18 = models.FloatField(db_column='fActualBError18', blank=True, null=True)  # Field name made lowercase.
    factualaerror18 = models.FloatField(db_column='fActualAError18', blank=True, null=True)  # Field name made lowercase.
    factualvaluea19 = models.FloatField(db_column='fActualValueA19', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa19 = models.FloatField(db_column='fActualValueAA19', blank=True, null=True)  # Field name made lowercase.
    factualvalueb19 = models.FloatField(db_column='fActualValueB19', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb19 = models.FloatField(db_column='fActualValueBB19', blank=True, null=True)  # Field name made lowercase.
    factualvaluec19 = models.FloatField(db_column='fActualValueC19', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc19 = models.FloatField(db_column='fActualValueCC19', blank=True, null=True)  # Field name made lowercase.
    factualvalued19 = models.FloatField(db_column='fActualValueD19', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd19 = models.FloatField(db_column='fActualValueDD19', blank=True, null=True)  # Field name made lowercase.
    factualvaluee19 = models.FloatField(db_column='fActualValueE19', blank=True, null=True)  # Field name made lowercase.
    factualvalueee19 = models.FloatField(db_column='fActualValueEE19', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult19 = models.TextField(db_column='sBeforeResult19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok19 = models.IntegerField(db_column='bBeforeOK19', blank=True, null=True)  # Field name made lowercase.
    safterresult19 = models.TextField(db_column='sAfterResult19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok19 = models.IntegerField(db_column='bAfterOK19', blank=True, null=True)  # Field name made lowercase.
    factualberror19 = models.FloatField(db_column='fActualBError19', blank=True, null=True)  # Field name made lowercase.
    factualaerror19 = models.FloatField(db_column='fActualAError19', blank=True, null=True)  # Field name made lowercase.
    factualvaluea20 = models.FloatField(db_column='fActualValueA20', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa20 = models.FloatField(db_column='fActualValueAA20', blank=True, null=True)  # Field name made lowercase.
    factualvalueb20 = models.FloatField(db_column='fActualValueB20', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb20 = models.FloatField(db_column='fActualValueBB20', blank=True, null=True)  # Field name made lowercase.
    factualvaluec20 = models.FloatField(db_column='fActualValueC20', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc20 = models.FloatField(db_column='fActualValueCC20', blank=True, null=True)  # Field name made lowercase.
    factualvalued20 = models.FloatField(db_column='fActualValueD20', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd20 = models.FloatField(db_column='fActualValueDD20', blank=True, null=True)  # Field name made lowercase.
    factualvaluee20 = models.FloatField(db_column='fActualValueE20', blank=True, null=True)  # Field name made lowercase.
    factualvalueee20 = models.FloatField(db_column='fActualValueEE20', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult20 = models.TextField(db_column='sBeforeResult20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok20 = models.IntegerField(db_column='bBeforeOK20', blank=True, null=True)  # Field name made lowercase.
    safterresult20 = models.TextField(db_column='sAfterResult20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok20 = models.IntegerField(db_column='bAfterOK20', blank=True, null=True)  # Field name made lowercase.
    factualberror20 = models.FloatField(db_column='fActualBError20', blank=True, null=True)  # Field name made lowercase.
    factualaerror20 = models.FloatField(db_column='fActualAError20', blank=True, null=True)  # Field name made lowercase.
    factualvaluea21 = models.FloatField(db_column='fActualValueA21', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa21 = models.FloatField(db_column='fActualValueAA21', blank=True, null=True)  # Field name made lowercase.
    factualvalueb21 = models.FloatField(db_column='fActualValueB21', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb21 = models.FloatField(db_column='fActualValueBB21', blank=True, null=True)  # Field name made lowercase.
    factualvaluec21 = models.FloatField(db_column='fActualValueC21', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc21 = models.FloatField(db_column='fActualValueCC21', blank=True, null=True)  # Field name made lowercase.
    factualvalued21 = models.FloatField(db_column='fActualValueD21', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd21 = models.FloatField(db_column='fActualValueDD21', blank=True, null=True)  # Field name made lowercase.
    factualvaluee21 = models.FloatField(db_column='fActualValueE21', blank=True, null=True)  # Field name made lowercase.
    factualvalueee21 = models.FloatField(db_column='fActualValueEE21', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult21 = models.TextField(db_column='sBeforeResult21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok21 = models.IntegerField(db_column='bBeforeOK21', blank=True, null=True)  # Field name made lowercase.
    safterresult21 = models.TextField(db_column='sAfterResult21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok21 = models.IntegerField(db_column='bAfterOK21', blank=True, null=True)  # Field name made lowercase.
    factualberror21 = models.FloatField(db_column='fActualBError21', blank=True, null=True)  # Field name made lowercase.
    factualaerror21 = models.FloatField(db_column='fActualAError21', blank=True, null=True)  # Field name made lowercase.
    factualvaluea22 = models.FloatField(db_column='fActualValueA22', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa22 = models.FloatField(db_column='fActualValueAA22', blank=True, null=True)  # Field name made lowercase.
    factualvalueb22 = models.FloatField(db_column='fActualValueB22', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb22 = models.FloatField(db_column='fActualValueBB22', blank=True, null=True)  # Field name made lowercase.
    factualvaluec22 = models.FloatField(db_column='fActualValueC22', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc22 = models.FloatField(db_column='fActualValueCC22', blank=True, null=True)  # Field name made lowercase.
    factualvalued22 = models.FloatField(db_column='fActualValueD22', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd22 = models.FloatField(db_column='fActualValueDD22', blank=True, null=True)  # Field name made lowercase.
    factualvaluee22 = models.FloatField(db_column='fActualValueE22', blank=True, null=True)  # Field name made lowercase.
    factualvalueee22 = models.FloatField(db_column='fActualValueEE22', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult22 = models.TextField(db_column='sBeforeResult22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok22 = models.IntegerField(db_column='bBeforeOK22', blank=True, null=True)  # Field name made lowercase.
    safterresult22 = models.TextField(db_column='sAfterResult22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok22 = models.IntegerField(db_column='bAfterOK22', blank=True, null=True)  # Field name made lowercase.
    factualberror22 = models.FloatField(db_column='fActualBError22', blank=True, null=True)  # Field name made lowercase.
    factualaerror22 = models.FloatField(db_column='fActualAError22', blank=True, null=True)  # Field name made lowercase.
    factualvaluea23 = models.FloatField(db_column='fActualValueA23', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa23 = models.FloatField(db_column='fActualValueAA23', blank=True, null=True)  # Field name made lowercase.
    factualvalueb23 = models.FloatField(db_column='fActualValueB23', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb23 = models.FloatField(db_column='fActualValueBB23', blank=True, null=True)  # Field name made lowercase.
    factualvaluec23 = models.FloatField(db_column='fActualValueC23', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc23 = models.FloatField(db_column='fActualValueCC23', blank=True, null=True)  # Field name made lowercase.
    factualvalued23 = models.FloatField(db_column='fActualValueD23', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd23 = models.FloatField(db_column='fActualValueDD23', blank=True, null=True)  # Field name made lowercase.
    factualvaluee23 = models.FloatField(db_column='fActualValueE23', blank=True, null=True)  # Field name made lowercase.
    factualvalueee23 = models.FloatField(db_column='fActualValueEE23', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult23 = models.TextField(db_column='sBeforeResult23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok23 = models.IntegerField(db_column='bBeforeOK23', blank=True, null=True)  # Field name made lowercase.
    safterresult23 = models.TextField(db_column='sAfterResult23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok23 = models.IntegerField(db_column='bAfterOK23', blank=True, null=True)  # Field name made lowercase.
    factualberror23 = models.FloatField(db_column='fActualBError23', blank=True, null=True)  # Field name made lowercase.
    factualaerror23 = models.FloatField(db_column='fActualAError23', blank=True, null=True)  # Field name made lowercase.
    factualvaluea24 = models.FloatField(db_column='fActualValueA24', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa24 = models.FloatField(db_column='fActualValueAA24', blank=True, null=True)  # Field name made lowercase.
    factualvalueb24 = models.FloatField(db_column='fActualValueB24', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb24 = models.FloatField(db_column='fActualValueBB24', blank=True, null=True)  # Field name made lowercase.
    factualvaluec24 = models.FloatField(db_column='fActualValueC24', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc24 = models.FloatField(db_column='fActualValueCC24', blank=True, null=True)  # Field name made lowercase.
    factualvalued24 = models.FloatField(db_column='fActualValueD24', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd24 = models.FloatField(db_column='fActualValueDD24', blank=True, null=True)  # Field name made lowercase.
    factualvaluee24 = models.FloatField(db_column='fActualValueE24', blank=True, null=True)  # Field name made lowercase.
    factualvalueee24 = models.FloatField(db_column='fActualValueEE24', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult24 = models.TextField(db_column='sBeforeResult24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok24 = models.IntegerField(db_column='bBeforeOK24', blank=True, null=True)  # Field name made lowercase.
    safterresult24 = models.TextField(db_column='sAfterResult24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok24 = models.IntegerField(db_column='bAfterOK24', blank=True, null=True)  # Field name made lowercase.
    factualberror24 = models.FloatField(db_column='fActualBError24', blank=True, null=True)  # Field name made lowercase.
    factualaerror24 = models.FloatField(db_column='fActualAError24', blank=True, null=True)  # Field name made lowercase.
    factualvaluea25 = models.FloatField(db_column='fActualValueA25', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa25 = models.FloatField(db_column='fActualValueAA25', blank=True, null=True)  # Field name made lowercase.
    factualvalueb25 = models.FloatField(db_column='fActualValueB25', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb25 = models.FloatField(db_column='fActualValueBB25', blank=True, null=True)  # Field name made lowercase.
    factualvaluec25 = models.FloatField(db_column='fActualValueC25', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc25 = models.FloatField(db_column='fActualValueCC25', blank=True, null=True)  # Field name made lowercase.
    factualvalued25 = models.FloatField(db_column='fActualValueD25', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd25 = models.FloatField(db_column='fActualValueDD25', blank=True, null=True)  # Field name made lowercase.
    factualvaluee25 = models.FloatField(db_column='fActualValueE25', blank=True, null=True)  # Field name made lowercase.
    factualvalueee25 = models.FloatField(db_column='fActualValueEE25', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult25 = models.TextField(db_column='sBeforeResult25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok25 = models.IntegerField(db_column='bBeforeOK25', blank=True, null=True)  # Field name made lowercase.
    safterresult25 = models.TextField(db_column='sAfterResult25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok25 = models.IntegerField(db_column='bAfterOK25', blank=True, null=True)  # Field name made lowercase.
    factualberror25 = models.FloatField(db_column='fActualBError25', blank=True, null=True)  # Field name made lowercase.
    factualaerror25 = models.FloatField(db_column='fActualAError25', blank=True, null=True)  # Field name made lowercase.
    factualvaluea26 = models.FloatField(db_column='fActualValueA26', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa26 = models.FloatField(db_column='fActualValueAA26', blank=True, null=True)  # Field name made lowercase.
    factualvalueb26 = models.FloatField(db_column='fActualValueB26', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb26 = models.FloatField(db_column='fActualValueBB26', blank=True, null=True)  # Field name made lowercase.
    factualvaluec26 = models.FloatField(db_column='fActualValueC26', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc26 = models.FloatField(db_column='fActualValueCC26', blank=True, null=True)  # Field name made lowercase.
    factualvalued26 = models.FloatField(db_column='fActualValueD26', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd26 = models.FloatField(db_column='fActualValueDD26', blank=True, null=True)  # Field name made lowercase.
    factualvaluee26 = models.FloatField(db_column='fActualValueE26', blank=True, null=True)  # Field name made lowercase.
    factualvalueee26 = models.FloatField(db_column='fActualValueEE26', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult26 = models.TextField(db_column='sBeforeResult26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok26 = models.IntegerField(db_column='bBeforeOK26', blank=True, null=True)  # Field name made lowercase.
    safterresult26 = models.TextField(db_column='sAfterResult26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok26 = models.IntegerField(db_column='bAfterOK26', blank=True, null=True)  # Field name made lowercase.
    factualberror26 = models.FloatField(db_column='fActualBError26', blank=True, null=True)  # Field name made lowercase.
    factualaerror26 = models.FloatField(db_column='fActualAError26', blank=True, null=True)  # Field name made lowercase.
    factualvaluea27 = models.FloatField(db_column='fActualValueA27', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa27 = models.FloatField(db_column='fActualValueAA27', blank=True, null=True)  # Field name made lowercase.
    factualvalueb27 = models.FloatField(db_column='fActualValueB27', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb27 = models.FloatField(db_column='fActualValueBB27', blank=True, null=True)  # Field name made lowercase.
    factualvaluec27 = models.FloatField(db_column='fActualValueC27', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc27 = models.FloatField(db_column='fActualValueCC27', blank=True, null=True)  # Field name made lowercase.
    factualvalued27 = models.FloatField(db_column='fActualValueD27', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd27 = models.FloatField(db_column='fActualValueDD27', blank=True, null=True)  # Field name made lowercase.
    factualvaluee27 = models.FloatField(db_column='fActualValueE27', blank=True, null=True)  # Field name made lowercase.
    factualvalueee27 = models.FloatField(db_column='fActualValueEE27', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult27 = models.TextField(db_column='sBeforeResult27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok27 = models.IntegerField(db_column='bBeforeOK27', blank=True, null=True)  # Field name made lowercase.
    safterresult27 = models.TextField(db_column='sAfterResult27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok27 = models.IntegerField(db_column='bAfterOK27', blank=True, null=True)  # Field name made lowercase.
    factualberror27 = models.FloatField(db_column='fActualBError27', blank=True, null=True)  # Field name made lowercase.
    factualaerror27 = models.FloatField(db_column='fActualAError27', blank=True, null=True)  # Field name made lowercase.
    factualvaluea28 = models.FloatField(db_column='fActualValueA28', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa28 = models.FloatField(db_column='fActualValueAA28', blank=True, null=True)  # Field name made lowercase.
    factualvalueb28 = models.FloatField(db_column='fActualValueB28', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb28 = models.FloatField(db_column='fActualValueBB28', blank=True, null=True)  # Field name made lowercase.
    factualvaluec28 = models.FloatField(db_column='fActualValueC28', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc28 = models.FloatField(db_column='fActualValueCC28', blank=True, null=True)  # Field name made lowercase.
    factualvalued28 = models.FloatField(db_column='fActualValueD28', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd28 = models.FloatField(db_column='fActualValueDD28', blank=True, null=True)  # Field name made lowercase.
    factualvaluee28 = models.FloatField(db_column='fActualValueE28', blank=True, null=True)  # Field name made lowercase.
    factualvalueee28 = models.FloatField(db_column='fActualValueEE28', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult28 = models.TextField(db_column='sBeforeResult28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok28 = models.IntegerField(db_column='bBeforeOK28', blank=True, null=True)  # Field name made lowercase.
    safterresult28 = models.TextField(db_column='sAfterResult28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok28 = models.IntegerField(db_column='bAfterOK28', blank=True, null=True)  # Field name made lowercase.
    factualberror28 = models.FloatField(db_column='fActualBError28', blank=True, null=True)  # Field name made lowercase.
    factualaerror28 = models.FloatField(db_column='fActualAError28', blank=True, null=True)  # Field name made lowercase.
    factualvaluea29 = models.FloatField(db_column='fActualValueA29', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa29 = models.FloatField(db_column='fActualValueAA29', blank=True, null=True)  # Field name made lowercase.
    factualvalueb29 = models.FloatField(db_column='fActualValueB29', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb29 = models.FloatField(db_column='fActualValueBB29', blank=True, null=True)  # Field name made lowercase.
    factualvaluec29 = models.FloatField(db_column='fActualValueC29', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc29 = models.FloatField(db_column='fActualValueCC29', blank=True, null=True)  # Field name made lowercase.
    factualvalued29 = models.FloatField(db_column='fActualValueD29', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd29 = models.FloatField(db_column='fActualValueDD29', blank=True, null=True)  # Field name made lowercase.
    factualvaluee29 = models.FloatField(db_column='fActualValueE29', blank=True, null=True)  # Field name made lowercase.
    factualvalueee29 = models.FloatField(db_column='fActualValueEE29', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult29 = models.TextField(db_column='sBeforeResult29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok29 = models.IntegerField(db_column='bBeforeOK29', blank=True, null=True)  # Field name made lowercase.
    safterresult29 = models.TextField(db_column='sAfterResult29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok29 = models.IntegerField(db_column='bAfterOK29', blank=True, null=True)  # Field name made lowercase.
    factualberror29 = models.FloatField(db_column='fActualBError29', blank=True, null=True)  # Field name made lowercase.
    factualaerror29 = models.FloatField(db_column='fActualAError29', blank=True, null=True)  # Field name made lowercase.
    factualvaluea30 = models.FloatField(db_column='fActualValueA30', blank=True, null=True)  # Field name made lowercase.
    factualvalueaa30 = models.FloatField(db_column='fActualValueAA30', blank=True, null=True)  # Field name made lowercase.
    factualvalueb30 = models.FloatField(db_column='fActualValueB30', blank=True, null=True)  # Field name made lowercase.
    factualvaluebb30 = models.FloatField(db_column='fActualValueBB30', blank=True, null=True)  # Field name made lowercase.
    factualvaluec30 = models.FloatField(db_column='fActualValueC30', blank=True, null=True)  # Field name made lowercase.
    factualvaluecc30 = models.FloatField(db_column='fActualValueCC30', blank=True, null=True)  # Field name made lowercase.
    factualvalued30 = models.FloatField(db_column='fActualValueD30', blank=True, null=True)  # Field name made lowercase.
    factualvaluedd30 = models.FloatField(db_column='fActualValueDD30', blank=True, null=True)  # Field name made lowercase.
    factualvaluee30 = models.FloatField(db_column='fActualValueE30', blank=True, null=True)  # Field name made lowercase.
    factualvalueee30 = models.FloatField(db_column='fActualValueEE30', blank=True, null=True)  # Field name made lowercase.
    sbeforeresult30 = models.TextField(db_column='sBeforeResult30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bbeforeok30 = models.IntegerField(db_column='bBeforeOK30', blank=True, null=True)  # Field name made lowercase.
    safterresult30 = models.TextField(db_column='sAfterResult30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bafterok30 = models.IntegerField(db_column='bAfterOK30', blank=True, null=True)  # Field name made lowercase.
    factualberror30 = models.FloatField(db_column='fActualBError30', blank=True, null=True)  # Field name made lowercase.
    factualaerror30 = models.FloatField(db_column='fActualAError30', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMainPart2'


class Thistorymulti(models.Model):
    historymultiid = models.BigAutoField(db_column='HistoryMultiId', primary_key=True)  # Field name made lowercase.
    historymainid = models.BigIntegerField(db_column='HistoryMainId', blank=True, null=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcalibsetid = models.BigIntegerField(db_column='sInstrumentCalibSetID', blank=True, null=True)  # Field name made lowercase.
    calibrationresultvalue = models.CharField(db_column='CalibrationResultValue', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calibrationresult = models.CharField(db_column='CalibrationResult', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calibrationresultvalueadjusted = models.CharField(db_column='CalibrationResultValueAdjusted', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calibrationresultadjusted = models.CharField(db_column='CalibrationResultAdjusted', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    ducreading = models.CharField(db_column='DUCReading', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deviationfound = models.CharField(db_column='DeviationFound', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dmax = models.FloatField(db_column='dMax', blank=True, null=True)  # Field name made lowercase.
    dmin = models.FloatField(db_column='dMin', blank=True, null=True)  # Field name made lowercase.
    sappliedvalue = models.CharField(db_column='sAppliedValue', max_length=20, blank=True, null=True)  # Field name made lowercase.
    derrorallowed = models.FloatField(db_column='dErrorAllowed', blank=True, null=True)  # Field name made lowercase.
    testmeterreading = models.FloatField(db_column='TestMeterReading', blank=True, null=True)  # Field name made lowercase.
    ducreadinfstd = models.CharField(db_column='DUCReadinfSTD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    std1 = models.FloatField(db_column='STD1', blank=True, null=True)  # Field name made lowercase.
    std2 = models.FloatField(db_column='STD2', blank=True, null=True)  # Field name made lowercase.
    std3 = models.FloatField(db_column='STD3', blank=True, null=True)  # Field name made lowercase.
    std4 = models.FloatField(db_column='STD4', blank=True, null=True)  # Field name made lowercase.
    std5 = models.FloatField(db_column='STD5', blank=True, null=True)  # Field name made lowercase.
    std6 = models.FloatField(db_column='STD6', blank=True, null=True)  # Field name made lowercase.
    std7 = models.FloatField(db_column='STD7', blank=True, null=True)  # Field name made lowercase.
    std8 = models.FloatField(db_column='STD8', blank=True, null=True)  # Field name made lowercase.
    std9 = models.FloatField(db_column='STD9', blank=True, null=True)  # Field name made lowercase.
    std10 = models.FloatField(db_column='STD10', blank=True, null=True)  # Field name made lowercase.
    std11 = models.FloatField(db_column='STD11', blank=True, null=True)  # Field name made lowercase.
    std12 = models.FloatField(db_column='STD12', blank=True, null=True)  # Field name made lowercase.
    std13 = models.FloatField(db_column='STD13', blank=True, null=True)  # Field name made lowercase.
    std14 = models.FloatField(db_column='STD14', blank=True, null=True)  # Field name made lowercase.
    std15 = models.FloatField(db_column='STD15', blank=True, null=True)  # Field name made lowercase.
    std16 = models.FloatField(db_column='STD16', blank=True, null=True)  # Field name made lowercase.
    std17 = models.FloatField(db_column='STD17', blank=True, null=True)  # Field name made lowercase.
    std18 = models.FloatField(db_column='STD18', blank=True, null=True)  # Field name made lowercase.
    std19 = models.FloatField(db_column='STD19', blank=True, null=True)  # Field name made lowercase.
    std20 = models.FloatField(db_column='STD20', blank=True, null=True)  # Field name made lowercase.
    testmeterreading1 = models.FloatField(db_column='TestMeterReading1', blank=True, null=True)  # Field name made lowercase.
    testmeterreading2 = models.FloatField(db_column='TestMeterReading2', blank=True, null=True)  # Field name made lowercase.
    svaltoview = models.CharField(db_column='sValtoView', max_length=350, blank=True, null=True)  # Field name made lowercase.
    slno = models.BigIntegerField(db_column='slNo', blank=True, null=True)  # Field name made lowercase.
    ldegree1 = models.BigIntegerField(db_column='lDegree1', blank=True, null=True)  # Field name made lowercase.
    lmin1 = models.BigIntegerField(db_column='lMin1', blank=True, null=True)  # Field name made lowercase.
    lsec1 = models.BigIntegerField(db_column='lSec1', blank=True, null=True)  # Field name made lowercase.
    ldegree2 = models.BigIntegerField(db_column='lDegree2', blank=True, null=True)  # Field name made lowercase.
    lmin2 = models.BigIntegerField(db_column='lMin2', blank=True, null=True)  # Field name made lowercase.
    lsec2 = models.BigIntegerField(db_column='lSec2', blank=True, null=True)  # Field name made lowercase.
    bimage = models.BooleanField(db_column='bImage', blank=True, null=True)  # Field name made lowercase.
    bdegree = models.BooleanField(db_column='bDegree', blank=True, null=True)  # Field name made lowercase.
    ldegreeactual = models.BigIntegerField(db_column='lDegreeActual', blank=True, null=True)  # Field name made lowercase.
    lminactual = models.BigIntegerField(db_column='lMinActual', blank=True, null=True)  # Field name made lowercase.
    lsecactual = models.BigIntegerField(db_column='lSecActual', blank=True, null=True)  # Field name made lowercase.
    daverage = models.FloatField(db_column='dAverage', blank=True, null=True)  # Field name made lowercase.
    derror = models.FloatField(db_column='dError', blank=True, null=True)  # Field name made lowercase.
    ddeviationfound = models.FloatField(db_column='dDeviationFound', blank=True, null=True)  # Field name made lowercase.
    std110 = models.FloatField(db_column='STD110', blank=True, null=True)  # Field name made lowercase.
    std21 = models.FloatField(db_column='STD21', blank=True, null=True)  # Field name made lowercase.
    std31 = models.FloatField(db_column='STD31', blank=True, null=True)  # Field name made lowercase.
    std41 = models.FloatField(db_column='STD41', blank=True, null=True)  # Field name made lowercase.
    std51 = models.FloatField(db_column='STD51', blank=True, null=True)  # Field name made lowercase.
    std61 = models.FloatField(db_column='STD61', blank=True, null=True)  # Field name made lowercase.
    std71 = models.FloatField(db_column='STD71', blank=True, null=True)  # Field name made lowercase.
    std81 = models.FloatField(db_column='STD81', blank=True, null=True)  # Field name made lowercase.
    std91 = models.FloatField(db_column='STD91', blank=True, null=True)  # Field name made lowercase.
    std101 = models.FloatField(db_column='STD101', blank=True, null=True)  # Field name made lowercase.
    std111 = models.FloatField(db_column='STD111', blank=True, null=True)  # Field name made lowercase.
    std121 = models.FloatField(db_column='STD121', blank=True, null=True)  # Field name made lowercase.
    std131 = models.FloatField(db_column='STD131', blank=True, null=True)  # Field name made lowercase.
    std141 = models.FloatField(db_column='STD141', blank=True, null=True)  # Field name made lowercase.
    std151 = models.FloatField(db_column='STD151', blank=True, null=True)  # Field name made lowercase.
    std161 = models.FloatField(db_column='STD161', blank=True, null=True)  # Field name made lowercase.
    std171 = models.FloatField(db_column='STD171', blank=True, null=True)  # Field name made lowercase.
    std181 = models.FloatField(db_column='STD181', blank=True, null=True)  # Field name made lowercase.
    std191 = models.FloatField(db_column='STD191', blank=True, null=True)  # Field name made lowercase.
    std201 = models.FloatField(db_column='STD201', blank=True, null=True)  # Field name made lowercase.
    std112 = models.FloatField(db_column='STD112', blank=True, null=True)  # Field name made lowercase.
    std22 = models.FloatField(db_column='STD22', blank=True, null=True)  # Field name made lowercase.
    std32 = models.FloatField(db_column='STD32', blank=True, null=True)  # Field name made lowercase.
    std42 = models.FloatField(db_column='STD42', blank=True, null=True)  # Field name made lowercase.
    std52 = models.FloatField(db_column='STD52', blank=True, null=True)  # Field name made lowercase.
    std62 = models.FloatField(db_column='STD62', blank=True, null=True)  # Field name made lowercase.
    std72 = models.FloatField(db_column='STD72', blank=True, null=True)  # Field name made lowercase.
    std82 = models.FloatField(db_column='STD82', blank=True, null=True)  # Field name made lowercase.
    std92 = models.FloatField(db_column='STD92', blank=True, null=True)  # Field name made lowercase.
    std102 = models.FloatField(db_column='STD102', blank=True, null=True)  # Field name made lowercase.
    std113 = models.FloatField(db_column='STD113', blank=True, null=True)  # Field name made lowercase.
    std122 = models.FloatField(db_column='STD122', blank=True, null=True)  # Field name made lowercase.
    std132 = models.FloatField(db_column='STD132', blank=True, null=True)  # Field name made lowercase.
    std142 = models.FloatField(db_column='STD142', blank=True, null=True)  # Field name made lowercase.
    std152 = models.FloatField(db_column='STD152', blank=True, null=True)  # Field name made lowercase.
    std162 = models.FloatField(db_column='STD162', blank=True, null=True)  # Field name made lowercase.
    std172 = models.FloatField(db_column='STD172', blank=True, null=True)  # Field name made lowercase.
    std182 = models.FloatField(db_column='STD182', blank=True, null=True)  # Field name made lowercase.
    std192 = models.FloatField(db_column='STD192', blank=True, null=True)  # Field name made lowercase.
    std202 = models.FloatField(db_column='STD202', blank=True, null=True)  # Field name made lowercase.
    std114 = models.FloatField(db_column='STD114', blank=True, null=True)  # Field name made lowercase.
    std23 = models.FloatField(db_column='STD23', blank=True, null=True)  # Field name made lowercase.
    std33 = models.FloatField(db_column='STD33', blank=True, null=True)  # Field name made lowercase.
    std43 = models.FloatField(db_column='STD43', blank=True, null=True)  # Field name made lowercase.
    std53 = models.FloatField(db_column='STD53', blank=True, null=True)  # Field name made lowercase.
    std63 = models.FloatField(db_column='STD63', blank=True, null=True)  # Field name made lowercase.
    std73 = models.FloatField(db_column='STD73', blank=True, null=True)  # Field name made lowercase.
    std83 = models.FloatField(db_column='STD83', blank=True, null=True)  # Field name made lowercase.
    std93 = models.FloatField(db_column='STD93', blank=True, null=True)  # Field name made lowercase.
    std103 = models.FloatField(db_column='STD103', blank=True, null=True)  # Field name made lowercase.
    std115 = models.FloatField(db_column='STD115', blank=True, null=True)  # Field name made lowercase.
    std123 = models.FloatField(db_column='STD123', blank=True, null=True)  # Field name made lowercase.
    std133 = models.FloatField(db_column='STD133', blank=True, null=True)  # Field name made lowercase.
    std143 = models.FloatField(db_column='STD143', blank=True, null=True)  # Field name made lowercase.
    std153 = models.FloatField(db_column='STD153', blank=True, null=True)  # Field name made lowercase.
    std163 = models.FloatField(db_column='STD163', blank=True, null=True)  # Field name made lowercase.
    std173 = models.FloatField(db_column='STD173', blank=True, null=True)  # Field name made lowercase.
    std183 = models.FloatField(db_column='STD183', blank=True, null=True)  # Field name made lowercase.
    std193 = models.FloatField(db_column='STD193', blank=True, null=True)  # Field name made lowercase.
    std203 = models.FloatField(db_column='STD203', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMulti'


class Thistorymultiestd(models.Model):
    sinstrumentcalibsetid = models.BigAutoField(db_column='sInstrumentCalibSetID', primary_key=True)  # Field name made lowercase.
    historymainid = models.BigIntegerField(db_column='HistoryMainId', blank=True, null=True)  # Field name made lowercase.
    ecinstrumentid = models.BigIntegerField(db_column='ECInstrumentId', blank=True, null=True)  # Field name made lowercase.
    bselect = models.BooleanField(db_column='bSelect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMultiESTD'


class Thistorymultisetting(models.Model):
    sinstrumentcalibsetid = models.BigAutoField(db_column='sInstrumentCalibSetID', primary_key=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    sparameter = models.CharField(db_column='sParameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    uomid = models.BigIntegerField(db_column='UOMID', blank=True, null=True)  # Field name made lowercase.
    dmax = models.FloatField(db_column='dMax', blank=True, null=True)  # Field name made lowercase.
    dmin = models.FloatField(db_column='dMin', blank=True, null=True)  # Field name made lowercase.
    sappliedvalue = models.CharField(db_column='sAppliedValue', max_length=20, blank=True, null=True)  # Field name made lowercase.
    derrorallowed = models.FloatField(db_column='dErrorAllowed', blank=True, null=True)  # Field name made lowercase.
    lsubinstruments = models.BigIntegerField(db_column='lsubInstruments', blank=True, null=True)  # Field name made lowercase.
    bsubdescription = models.BooleanField(db_column='bsubDescription', blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    scomment = models.FloatField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    testmeterreading = models.FloatField(db_column='TestMeterReading', blank=True, null=True)  # Field name made lowercase.
    ducreading = models.FloatField(db_column='DUCReading', blank=True, null=True)  # Field name made lowercase.
    std1 = models.FloatField(db_column='STD1', blank=True, null=True)  # Field name made lowercase.
    std2 = models.FloatField(db_column='STD2', blank=True, null=True)  # Field name made lowercase.
    std3 = models.FloatField(db_column='STD3', blank=True, null=True)  # Field name made lowercase.
    std4 = models.FloatField(db_column='STD4', blank=True, null=True)  # Field name made lowercase.
    std5 = models.FloatField(db_column='STD5', blank=True, null=True)  # Field name made lowercase.
    daverage = models.FloatField(db_column='dAverage', blank=True, null=True)  # Field name made lowercase.
    derror = models.FloatField(db_column='dError', blank=True, null=True)  # Field name made lowercase.
    std6 = models.FloatField(db_column='STD6', blank=True, null=True)  # Field name made lowercase.
    std7 = models.FloatField(db_column='STD7', blank=True, null=True)  # Field name made lowercase.
    std8 = models.FloatField(db_column='STD8', blank=True, null=True)  # Field name made lowercase.
    std9 = models.FloatField(db_column='STD9', blank=True, null=True)  # Field name made lowercase.
    std10 = models.FloatField(db_column='STD10', blank=True, null=True)  # Field name made lowercase.
    std11 = models.FloatField(db_column='STD11', blank=True, null=True)  # Field name made lowercase.
    std12 = models.FloatField(db_column='STD12', blank=True, null=True)  # Field name made lowercase.
    std13 = models.FloatField(db_column='STD13', blank=True, null=True)  # Field name made lowercase.
    std14 = models.FloatField(db_column='STD14', blank=True, null=True)  # Field name made lowercase.
    std15 = models.FloatField(db_column='STD15', blank=True, null=True)  # Field name made lowercase.
    std16 = models.FloatField(db_column='STD16', blank=True, null=True)  # Field name made lowercase.
    std17 = models.FloatField(db_column='STD17', blank=True, null=True)  # Field name made lowercase.
    std18 = models.FloatField(db_column='STD18', blank=True, null=True)  # Field name made lowercase.
    std19 = models.FloatField(db_column='STD19', blank=True, null=True)  # Field name made lowercase.
    std20 = models.FloatField(db_column='STD20', blank=True, null=True)  # Field name made lowercase.
    historymainid = models.BigIntegerField(db_column='HistoryMainId', blank=True, null=True)  # Field name made lowercase.
    ldegree1 = models.BigIntegerField(db_column='lDegree1', blank=True, null=True)  # Field name made lowercase.
    lmin1 = models.BigIntegerField(db_column='lMin1', blank=True, null=True)  # Field name made lowercase.
    lsec1 = models.BigIntegerField(db_column='lSec1', blank=True, null=True)  # Field name made lowercase.
    ldegree2 = models.BigIntegerField(db_column='lDegree2', blank=True, null=True)  # Field name made lowercase.
    lmin2 = models.BigIntegerField(db_column='lMin2', blank=True, null=True)  # Field name made lowercase.
    lsec2 = models.BigIntegerField(db_column='lSec2', blank=True, null=True)  # Field name made lowercase.
    bimage = models.BooleanField(db_column='bImage', blank=True, null=True)  # Field name made lowercase.
    bdegree = models.BooleanField(db_column='bDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryMultiSetting'


class Thistoryreviewchecklist(models.Model):
    historyreviewid = models.BigAutoField(db_column='HistoryReviewId', primary_key=True)  # Field name made lowercase.
    historymainid = models.BigIntegerField(db_column='HistoryMainId', blank=True, null=True)  # Field name made lowercase.
    binstrumentcode1 = models.BooleanField(db_column='bInstrumentCode1', blank=True, null=True)  # Field name made lowercase.
    brange1 = models.BooleanField(db_column='bRange1', blank=True, null=True)  # Field name made lowercase.
    btraceability1 = models.BooleanField(db_column='bTraceability1', blank=True, null=True)  # Field name made lowercase.
    bcalibdate1 = models.BooleanField(db_column='bCalibDate1', blank=True, null=True)  # Field name made lowercase.
    bcalibsticker1 = models.BooleanField(db_column='bCalibSticker1', blank=True, null=True)  # Field name made lowercase.
    bstdused1 = models.BooleanField(db_column='bStdUsed1', blank=True, null=True)  # Field name made lowercase.
    binstrumentcode2 = models.BooleanField(db_column='bInstrumentCode2', blank=True, null=True)  # Field name made lowercase.
    brange2 = models.BooleanField(db_column='bRange2', blank=True, null=True)  # Field name made lowercase.
    btraceability2 = models.BooleanField(db_column='bTraceability2', blank=True, null=True)  # Field name made lowercase.
    bcalibdate2 = models.BooleanField(db_column='bCalibDate2', blank=True, null=True)  # Field name made lowercase.
    bcalibsticker2 = models.BooleanField(db_column='bCalibSticker2', blank=True, null=True)  # Field name made lowercase.
    bstdused2 = models.BooleanField(db_column='bStdUsed2', blank=True, null=True)  # Field name made lowercase.
    bvaluescorrect = models.BooleanField(db_column='bValuesCorrect', blank=True, null=True)  # Field name made lowercase.
    bstatuscorrect = models.BooleanField(db_column='bStatusCorrect', blank=True, null=True)  # Field name made lowercase.
    bcertificateattacjhed = models.BooleanField(db_column='bCertificateAttacjhed', blank=True, null=True)  # Field name made lowercase.
    bwithinnablexpirydate = models.BooleanField(db_column='bWithinNABLExpiryDate', blank=True, null=True)  # Field name made lowercase.
    bacceptancecriteriacorrect = models.BooleanField(db_column='bAcceptanceCriteriaCorrect', blank=True, null=True)  # Field name made lowercase.
    bschedulecorrect = models.BooleanField(db_column='bScheduleCorrect', blank=True, null=True)  # Field name made lowercase.
    bscheduleneedschanged = models.BooleanField(db_column='bScheduleneedschanged', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryReviewCheckList'


class Thistorytransactionmsa(models.Model):
    lhistorytranid = models.BigAutoField(db_column='lHistoryTranID', primary_key=True)  # Field name made lowercase.
    historymainid = models.BigIntegerField(db_column='HistoryMainId', blank=True, null=True)  # Field name made lowercase.
    instrumentid = models.BigIntegerField(db_column='InstrumentId', blank=True, null=True)  # Field name made lowercase.
    historytype = models.CharField(db_column='HistoryType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibrationvendor = models.CharField(db_column='CalibrationVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibrationvendorid = models.BigIntegerField(db_column='CalibrationVendorID', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibrationresult = models.CharField(db_column='CalibrationResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibrationdate = models.DateTimeField(db_column='CalibrationDate', blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    br = models.BooleanField(db_column='bR', blank=True, null=True)  # Field name made lowercase.
    ba = models.BooleanField(db_column='bA', blank=True, null=True)  # Field name made lowercase.
    bs = models.BooleanField(db_column='bS', blank=True, null=True)  # Field name made lowercase.
    bb = models.BooleanField(db_column='bB', blank=True, null=True)  # Field name made lowercase.
    bl = models.BooleanField(db_column='bL', blank=True, null=True)  # Field name made lowercase.
    brresult = models.BooleanField(db_column='bRResult', blank=True, null=True)  # Field name made lowercase.
    baresult = models.BooleanField(db_column='bAResult', blank=True, null=True)  # Field name made lowercase.
    bsresult = models.BooleanField(db_column='bSResult', blank=True, null=True)  # Field name made lowercase.
    bbresult = models.BooleanField(db_column='bBResult', blank=True, null=True)  # Field name made lowercase.
    blresult = models.BooleanField(db_column='bLResult', blank=True, null=True)  # Field name made lowercase.
    lr = models.BigIntegerField(db_column='lR', blank=True, null=True)  # Field name made lowercase.
    la = models.BigIntegerField(db_column='lA', blank=True, null=True)  # Field name made lowercase.
    ls = models.BigIntegerField(db_column='lS', blank=True, null=True)  # Field name made lowercase.
    lb = models.BigIntegerField(db_column='lB', blank=True, null=True)  # Field name made lowercase.
    ll = models.BigIntegerField(db_column='lL', blank=True, null=True)  # Field name made lowercase.
    historymainidr = models.BigIntegerField(db_column='HistoryMainIdR', blank=True, null=True)  # Field name made lowercase.
    historymainida = models.BigIntegerField(db_column='HistoryMainIdA', blank=True, null=True)  # Field name made lowercase.
    historymainids = models.BigIntegerField(db_column='HistoryMainIdS', blank=True, null=True)  # Field name made lowercase.
    historymainidb = models.BigIntegerField(db_column='HistoryMainIdB', blank=True, null=True)  # Field name made lowercase.
    historymainidl = models.BigIntegerField(db_column='HistoryMainIdL', blank=True, null=True)  # Field name made lowercase.
    lanova = models.BigIntegerField(db_column='lAnova', blank=True, null=True)  # Field name made lowercase.
    blanova = models.BigIntegerField(db_column='blAnova', blank=True, null=True)  # Field name made lowercase.
    danova = models.BigIntegerField(db_column='dAnova', blank=True, null=True)  # Field name made lowercase.
    historymainidanova = models.BigIntegerField(db_column='HistoryMainIdAnova', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scalibrationdate = models.CharField(db_column='sCalibrationDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dthistorydate = models.DateTimeField(db_column='dtHistoryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryTransactionMSA'


class Thistorytransactions(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    lhistorymainid = models.BigIntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    shistorytype = models.CharField(db_column='sHistoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendor = models.CharField(db_column='sCalibrationVendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendorid = models.CharField(db_column='sCalibrationVendorID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scalibrationresult = models.CharField(db_column='sCalibrationResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtcalibrationdate = models.DateTimeField(db_column='dtCalibrationDate', blank=True, null=True)  # Field name made lowercase.
    fcalibcost = models.FloatField(db_column='fCalibCost', blank=True, null=True)  # Field name made lowercase.
    llplantid = models.BigIntegerField(db_column='llPlantId', blank=True, null=True)  # Field name made lowercase.
    ssplantname = models.CharField(db_column='ssPlantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slplantcode = models.CharField(db_column='slPlantCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    dtreturneddate = models.DateTimeField(db_column='dtReturnedDate', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='sTo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sfrom = models.CharField(db_column='sFrom', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dthistorydate = models.DateTimeField(db_column='dtHistoryDate', blank=True, null=True)  # Field name made lowercase.
    shistorydate = models.CharField(db_column='sHistoryDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sreturneddate = models.CharField(db_column='sReturnedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    llineid = models.BigIntegerField(db_column='lLineId', blank=True, null=True)  # Field name made lowercase.
    slinename = models.CharField(db_column='sLineName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THistoryTransactions'


class Tmsaattribute(models.Model):
    lrrspecificatonid = models.BigAutoField(db_column='lRRSpecificatonID', primary_key=True)  # Field name made lowercase.
    rrdate = models.DateTimeField(db_column='RRDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=350, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.FloatField(db_column='Tolerance', blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductID', blank=True, null=True)  # Field name made lowercase.
    lparts = models.BigIntegerField(db_column='lParts', blank=True, null=True)  # Field name made lowercase.
    ltrials = models.BigIntegerField(db_column='lTrials', blank=True, null=True)  # Field name made lowercase.
    loperators = models.BigIntegerField(db_column='lOperators', blank=True, null=True)  # Field name made lowercase.
    specialcharacter = models.CharField(db_column='SpecialCharacter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    considertolerance = models.CharField(db_column='ConsiderTolerance', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=350)  # Field name made lowercase.
    bcreatetable = models.BooleanField(db_column='bCreateTable', blank=True, null=True)  # Field name made lowercase.
    previouslrrspecificatonid = models.BigIntegerField(db_column='PreviouslRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    reconduct = models.BooleanField(db_column='ReConduct', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    timetaken = models.CharField(db_column='TimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    calibratedby = models.CharField(db_column='CalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    xbarbar = models.FloatField(db_column='XBARBar', blank=True, null=True)  # Field name made lowercase.
    rbar = models.FloatField(db_column='RBar', blank=True, null=True)  # Field name made lowercase.
    uclxbar = models.FloatField(db_column='UCLXBar', blank=True, null=True)  # Field name made lowercase.
    lclxbar = models.FloatField(db_column='LCLXBar', blank=True, null=True)  # Field name made lowercase.
    uclrange = models.FloatField(db_column='UCLRange', blank=True, null=True)  # Field name made lowercase.
    lclrange = models.FloatField(db_column='LCLRange', blank=True, null=True)  # Field name made lowercase.
    dbias = models.FloatField(db_column='dBias', blank=True, null=True)  # Field name made lowercase.
    dsigmarepr = models.FloatField(db_column='dSigmaRepr', blank=True, null=True)  # Field name made lowercase.
    dsigmabias = models.FloatField(db_column='dSigmaBias', blank=True, null=True)  # Field name made lowercase.
    tbias = models.FloatField(db_column='tBias', blank=True, null=True)  # Field name made lowercase.
    tcritical = models.FloatField(db_column='tCritical', blank=True, null=True)  # Field name made lowercase.
    biasstatus = models.FloatField(db_column='BiasStatus', blank=True, null=True)  # Field name made lowercase.
    biasvalue = models.FloatField(db_column='BiasValue', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    bcategory = models.BooleanField(db_column='bCategory', blank=True, null=True)  # Field name made lowercase.
    categoryhistorymsaid = models.BigIntegerField(db_column='CategoryHistoryMSAID', blank=True, null=True)  # Field name made lowercase.
    lcategoryscheduleid = models.BigIntegerField(db_column='lCategoryScheduleID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fanalysisval = models.FloatField(db_column='fAnalysisVal', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1 = models.FloatField(db_column='fAnalysisVal1', blank=True, null=True)  # Field name made lowercase.
    fanalysisval2 = models.FloatField(db_column='fAnalysisVal2', blank=True, null=True)  # Field name made lowercase.
    fanalysisval3 = models.FloatField(db_column='fAnalysisVal3', blank=True, null=True)  # Field name made lowercase.
    fanalysisval4 = models.FloatField(db_column='fAnalysisVal4', blank=True, null=True)  # Field name made lowercase.
    fanalysisval5 = models.FloatField(db_column='fAnalysisVal5', blank=True, null=True)  # Field name made lowercase.
    fanalysisval6 = models.FloatField(db_column='fAnalysisVal6', blank=True, null=True)  # Field name made lowercase.
    fanalysisval7 = models.FloatField(db_column='fAnalysisVal7', blank=True, null=True)  # Field name made lowercase.
    fanalysisval8 = models.FloatField(db_column='fAnalysisVal8', blank=True, null=True)  # Field name made lowercase.
    fanalysisval9 = models.FloatField(db_column='fAnalysisVal9', blank=True, null=True)  # Field name made lowercase.
    fanalysisval10 = models.FloatField(db_column='fAnalysisVal10', blank=True, null=True)  # Field name made lowercase.
    fanalysisval11 = models.FloatField(db_column='fAnalysisVal11', blank=True, null=True)  # Field name made lowercase.
    fanalysisval21 = models.FloatField(db_column='fAnalysisVal21', blank=True, null=True)  # Field name made lowercase.
    fanalysisval31 = models.FloatField(db_column='fAnalysisVal31', blank=True, null=True)  # Field name made lowercase.
    fanalysisval41 = models.FloatField(db_column='fAnalysisVal41', blank=True, null=True)  # Field name made lowercase.
    fanalysisval51 = models.FloatField(db_column='fAnalysisVal51', blank=True, null=True)  # Field name made lowercase.
    fanalysisval61 = models.FloatField(db_column='fAnalysisVal61', blank=True, null=True)  # Field name made lowercase.
    fanalysisval71 = models.FloatField(db_column='fAnalysisVal71', blank=True, null=True)  # Field name made lowercase.
    fanalysisval81 = models.FloatField(db_column='fAnalysisVal81', blank=True, null=True)  # Field name made lowercase.
    fanalysisval91 = models.FloatField(db_column='fAnalysisVal91', blank=True, null=True)  # Field name made lowercase.
    fanalysisval101 = models.FloatField(db_column='fAnalysisVal101', blank=True, null=True)  # Field name made lowercase.
    fanalysisval12 = models.FloatField(db_column='fAnalysisVal12', blank=True, null=True)  # Field name made lowercase.
    fanalysisval22 = models.FloatField(db_column='fAnalysisVal22', blank=True, null=True)  # Field name made lowercase.
    fanalysisval32 = models.FloatField(db_column='fAnalysisVal32', blank=True, null=True)  # Field name made lowercase.
    fanalysisval42 = models.FloatField(db_column='fAnalysisVal42', blank=True, null=True)  # Field name made lowercase.
    fanalysisval52 = models.FloatField(db_column='fAnalysisVal52', blank=True, null=True)  # Field name made lowercase.
    fanalysisval62 = models.FloatField(db_column='fAnalysisVal62', blank=True, null=True)  # Field name made lowercase.
    fanalysisval72 = models.FloatField(db_column='fAnalysisVal72', blank=True, null=True)  # Field name made lowercase.
    fanalysisval82 = models.FloatField(db_column='fAnalysisVal82', blank=True, null=True)  # Field name made lowercase.
    fanalysisval92 = models.FloatField(db_column='fAnalysisVal92', blank=True, null=True)  # Field name made lowercase.
    fanalysisval102 = models.FloatField(db_column='fAnalysisVal102', blank=True, null=True)  # Field name made lowercase.
    fanalysisval13 = models.FloatField(db_column='fAnalysisVal13', blank=True, null=True)  # Field name made lowercase.
    fanalysisval23 = models.FloatField(db_column='fAnalysisVal23', blank=True, null=True)  # Field name made lowercase.
    fanalysisval33 = models.FloatField(db_column='fAnalysisVal33', blank=True, null=True)  # Field name made lowercase.
    fanalysisval43 = models.FloatField(db_column='fAnalysisVal43', blank=True, null=True)  # Field name made lowercase.
    fanalysisval53 = models.FloatField(db_column='fAnalysisVal53', blank=True, null=True)  # Field name made lowercase.
    fanalysisval63 = models.FloatField(db_column='fAnalysisVal63', blank=True, null=True)  # Field name made lowercase.
    fanalysisval73 = models.FloatField(db_column='fAnalysisVal73', blank=True, null=True)  # Field name made lowercase.
    fanalysisval83 = models.FloatField(db_column='fAnalysisVal83', blank=True, null=True)  # Field name made lowercase.
    fanalysisval93 = models.FloatField(db_column='fAnalysisVal93', blank=True, null=True)  # Field name made lowercase.
    fanalysisval103 = models.FloatField(db_column='fAnalysisVal103', blank=True, null=True)  # Field name made lowercase.
    fanalysisval14 = models.FloatField(db_column='fAnalysisVal14', blank=True, null=True)  # Field name made lowercase.
    fanalysisval24 = models.FloatField(db_column='fAnalysisVal24', blank=True, null=True)  # Field name made lowercase.
    fanalysisval34 = models.FloatField(db_column='fAnalysisVal34', blank=True, null=True)  # Field name made lowercase.
    fanalysisval44 = models.FloatField(db_column='fAnalysisVal44', blank=True, null=True)  # Field name made lowercase.
    fanalysisval54 = models.FloatField(db_column='fAnalysisVal54', blank=True, null=True)  # Field name made lowercase.
    fanalysisval64 = models.FloatField(db_column='fAnalysisVal64', blank=True, null=True)  # Field name made lowercase.
    fanalysisval74 = models.FloatField(db_column='fAnalysisVal74', blank=True, null=True)  # Field name made lowercase.
    fanalysisval84 = models.FloatField(db_column='fAnalysisVal84', blank=True, null=True)  # Field name made lowercase.
    fanalysisval94 = models.FloatField(db_column='fAnalysisVal94', blank=True, null=True)  # Field name made lowercase.
    fanalysisval104 = models.FloatField(db_column='fAnalysisVal104', blank=True, null=True)  # Field name made lowercase.
    fanalysisval15 = models.FloatField(db_column='fAnalysisVal15', blank=True, null=True)  # Field name made lowercase.
    fanalysisval25 = models.FloatField(db_column='fAnalysisVal25', blank=True, null=True)  # Field name made lowercase.
    fanalysisval35 = models.FloatField(db_column='fAnalysisVal35', blank=True, null=True)  # Field name made lowercase.
    fanalysisval45 = models.FloatField(db_column='fAnalysisVal45', blank=True, null=True)  # Field name made lowercase.
    fanalysisval55 = models.FloatField(db_column='fAnalysisVal55', blank=True, null=True)  # Field name made lowercase.
    fanalysisval65 = models.FloatField(db_column='fAnalysisVal65', blank=True, null=True)  # Field name made lowercase.
    fanalysisval75 = models.FloatField(db_column='fAnalysisVal75', blank=True, null=True)  # Field name made lowercase.
    fanalysisval85 = models.FloatField(db_column='fAnalysisVal85', blank=True, null=True)  # Field name made lowercase.
    fanalysisval95 = models.FloatField(db_column='fAnalysisVal95', blank=True, null=True)  # Field name made lowercase.
    fanalysisval105 = models.FloatField(db_column='fAnalysisVal105', blank=True, null=True)  # Field name made lowercase.
    fanalysisval16 = models.FloatField(db_column='fAnalysisVal16', blank=True, null=True)  # Field name made lowercase.
    fanalysisval26 = models.FloatField(db_column='fAnalysisVal26', blank=True, null=True)  # Field name made lowercase.
    fanalysisval36 = models.FloatField(db_column='fAnalysisVal36', blank=True, null=True)  # Field name made lowercase.
    fanalysisval46 = models.FloatField(db_column='fAnalysisVal46', blank=True, null=True)  # Field name made lowercase.
    fanalysisval56 = models.FloatField(db_column='fAnalysisVal56', blank=True, null=True)  # Field name made lowercase.
    fanalysisval66 = models.FloatField(db_column='fAnalysisVal66', blank=True, null=True)  # Field name made lowercase.
    fanalysisval76 = models.FloatField(db_column='fAnalysisVal76', blank=True, null=True)  # Field name made lowercase.
    fanalysisval86 = models.FloatField(db_column='fAnalysisVal86', blank=True, null=True)  # Field name made lowercase.
    fanalysisval96 = models.FloatField(db_column='fAnalysisVal96', blank=True, null=True)  # Field name made lowercase.
    fanalysisval106 = models.FloatField(db_column='fAnalysisVal106', blank=True, null=True)  # Field name made lowercase.
    fanalysisval17 = models.FloatField(db_column='fAnalysisVal17', blank=True, null=True)  # Field name made lowercase.
    fanalysisval27 = models.FloatField(db_column='fAnalysisVal27', blank=True, null=True)  # Field name made lowercase.
    fanalysisval37 = models.FloatField(db_column='fAnalysisVal37', blank=True, null=True)  # Field name made lowercase.
    fanalysisval47 = models.FloatField(db_column='fAnalysisVal47', blank=True, null=True)  # Field name made lowercase.
    fanalysisval57 = models.FloatField(db_column='fAnalysisVal57', blank=True, null=True)  # Field name made lowercase.
    fanalysisval67 = models.FloatField(db_column='fAnalysisVal67', blank=True, null=True)  # Field name made lowercase.
    fanalysisval77 = models.FloatField(db_column='fAnalysisVal77', blank=True, null=True)  # Field name made lowercase.
    fanalysisval87 = models.FloatField(db_column='fAnalysisVal87', blank=True, null=True)  # Field name made lowercase.
    fanalysisval97 = models.FloatField(db_column='fAnalysisVal97', blank=True, null=True)  # Field name made lowercase.
    fanalysisval107 = models.FloatField(db_column='fAnalysisVal107', blank=True, null=True)  # Field name made lowercase.
    fanalysisval18 = models.FloatField(db_column='fAnalysisVal18', blank=True, null=True)  # Field name made lowercase.
    fanalysisval28 = models.FloatField(db_column='fAnalysisVal28', blank=True, null=True)  # Field name made lowercase.
    fanalysisval38 = models.FloatField(db_column='fAnalysisVal38', blank=True, null=True)  # Field name made lowercase.
    fanalysisval48 = models.FloatField(db_column='fAnalysisVal48', blank=True, null=True)  # Field name made lowercase.
    fanalysisval58 = models.FloatField(db_column='fAnalysisVal58', blank=True, null=True)  # Field name made lowercase.
    fanalysisval68 = models.FloatField(db_column='fAnalysisVal68', blank=True, null=True)  # Field name made lowercase.
    fanalysisval78 = models.FloatField(db_column='fAnalysisVal78', blank=True, null=True)  # Field name made lowercase.
    fanalysisval88 = models.FloatField(db_column='fAnalysisVal88', blank=True, null=True)  # Field name made lowercase.
    fanalysisval98 = models.FloatField(db_column='fAnalysisVal98', blank=True, null=True)  # Field name made lowercase.
    fanalysisval108 = models.FloatField(db_column='fAnalysisVal108', blank=True, null=True)  # Field name made lowercase.
    fanalysisval19 = models.FloatField(db_column='fAnalysisVal19', blank=True, null=True)  # Field name made lowercase.
    fanalysisval29 = models.FloatField(db_column='fAnalysisVal29', blank=True, null=True)  # Field name made lowercase.
    fanalysisval39 = models.FloatField(db_column='fAnalysisVal39', blank=True, null=True)  # Field name made lowercase.
    fanalysisval49 = models.FloatField(db_column='fAnalysisVal49', blank=True, null=True)  # Field name made lowercase.
    fanalysisval59 = models.FloatField(db_column='fAnalysisVal59', blank=True, null=True)  # Field name made lowercase.
    fanalysisval69 = models.FloatField(db_column='fAnalysisVal69', blank=True, null=True)  # Field name made lowercase.
    fanalysisval79 = models.FloatField(db_column='fAnalysisVal79', blank=True, null=True)  # Field name made lowercase.
    fanalysisval89 = models.FloatField(db_column='fAnalysisVal89', blank=True, null=True)  # Field name made lowercase.
    fanalysisval99 = models.FloatField(db_column='fAnalysisVal99', blank=True, null=True)  # Field name made lowercase.
    fanalysisval109 = models.FloatField(db_column='fAnalysisVal109', blank=True, null=True)  # Field name made lowercase.
    fanalysisval110 = models.FloatField(db_column='fAnalysisVal110', blank=True, null=True)  # Field name made lowercase.
    fanalysisval210 = models.FloatField(db_column='fAnalysisVal210', blank=True, null=True)  # Field name made lowercase.
    fanalysisval310 = models.FloatField(db_column='fAnalysisVal310', blank=True, null=True)  # Field name made lowercase.
    fanalysisval410 = models.FloatField(db_column='fAnalysisVal410', blank=True, null=True)  # Field name made lowercase.
    fanalysisval510 = models.FloatField(db_column='fAnalysisVal510', blank=True, null=True)  # Field name made lowercase.
    fanalysisval610 = models.FloatField(db_column='fAnalysisVal610', blank=True, null=True)  # Field name made lowercase.
    fanalysisval710 = models.FloatField(db_column='fAnalysisVal710', blank=True, null=True)  # Field name made lowercase.
    fanalysisval810 = models.FloatField(db_column='fAnalysisVal810', blank=True, null=True)  # Field name made lowercase.
    fanalysisval910 = models.FloatField(db_column='fAnalysisVal910', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1010 = models.FloatField(db_column='fAnalysisVal1010', blank=True, null=True)  # Field name made lowercase.
    fanalysisval111 = models.FloatField(db_column='fAnalysisVal111', blank=True, null=True)  # Field name made lowercase.
    fanalysisval211 = models.FloatField(db_column='fAnalysisVal211', blank=True, null=True)  # Field name made lowercase.
    fanalysisval311 = models.FloatField(db_column='fAnalysisVal311', blank=True, null=True)  # Field name made lowercase.
    fanalysisval411 = models.FloatField(db_column='fAnalysisVal411', blank=True, null=True)  # Field name made lowercase.
    fanalysisval511 = models.FloatField(db_column='fAnalysisVal511', blank=True, null=True)  # Field name made lowercase.
    fanalysisval611 = models.FloatField(db_column='fAnalysisVal611', blank=True, null=True)  # Field name made lowercase.
    fanalysisval711 = models.FloatField(db_column='fAnalysisVal711', blank=True, null=True)  # Field name made lowercase.
    fanalysisval811 = models.FloatField(db_column='fAnalysisVal811', blank=True, null=True)  # Field name made lowercase.
    fanalysisval911 = models.FloatField(db_column='fAnalysisVal911', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1011 = models.FloatField(db_column='fAnalysisVal1011', blank=True, null=True)  # Field name made lowercase.
    fanalysisval112 = models.FloatField(db_column='fAnalysisVal112', blank=True, null=True)  # Field name made lowercase.
    fanalysisval212 = models.FloatField(db_column='fAnalysisVal212', blank=True, null=True)  # Field name made lowercase.
    fanalysisval312 = models.FloatField(db_column='fAnalysisVal312', blank=True, null=True)  # Field name made lowercase.
    fanalysisval412 = models.FloatField(db_column='fAnalysisVal412', blank=True, null=True)  # Field name made lowercase.
    fanalysisval512 = models.FloatField(db_column='fAnalysisVal512', blank=True, null=True)  # Field name made lowercase.
    fanalysisval612 = models.FloatField(db_column='fAnalysisVal612', blank=True, null=True)  # Field name made lowercase.
    fanalysisval712 = models.FloatField(db_column='fAnalysisVal712', blank=True, null=True)  # Field name made lowercase.
    fanalysisval812 = models.FloatField(db_column='fAnalysisVal812', blank=True, null=True)  # Field name made lowercase.
    fanalysisval912 = models.FloatField(db_column='fAnalysisVal912', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1012 = models.FloatField(db_column='fAnalysisVal1012', blank=True, null=True)  # Field name made lowercase.
    fanalysisval113 = models.FloatField(db_column='fAnalysisVal113', blank=True, null=True)  # Field name made lowercase.
    fanalysisval213 = models.FloatField(db_column='fAnalysisVal213', blank=True, null=True)  # Field name made lowercase.
    fanalysisval313 = models.FloatField(db_column='fAnalysisVal313', blank=True, null=True)  # Field name made lowercase.
    fanalysisval413 = models.FloatField(db_column='fAnalysisVal413', blank=True, null=True)  # Field name made lowercase.
    fanalysisval513 = models.FloatField(db_column='fAnalysisVal513', blank=True, null=True)  # Field name made lowercase.
    fanalysisval613 = models.FloatField(db_column='fAnalysisVal613', blank=True, null=True)  # Field name made lowercase.
    fanalysisval713 = models.FloatField(db_column='fAnalysisVal713', blank=True, null=True)  # Field name made lowercase.
    fanalysisval813 = models.FloatField(db_column='fAnalysisVal813', blank=True, null=True)  # Field name made lowercase.
    fanalysisval913 = models.FloatField(db_column='fAnalysisVal913', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1013 = models.FloatField(db_column='fAnalysisVal1013', blank=True, null=True)  # Field name made lowercase.
    fanalysisval114 = models.FloatField(db_column='fAnalysisVal114', blank=True, null=True)  # Field name made lowercase.
    fanalysisval214 = models.FloatField(db_column='fAnalysisVal214', blank=True, null=True)  # Field name made lowercase.
    fanalysisval314 = models.FloatField(db_column='fAnalysisVal314', blank=True, null=True)  # Field name made lowercase.
    fanalysisval414 = models.FloatField(db_column='fAnalysisVal414', blank=True, null=True)  # Field name made lowercase.
    fanalysisval514 = models.FloatField(db_column='fAnalysisVal514', blank=True, null=True)  # Field name made lowercase.
    fanalysisval614 = models.FloatField(db_column='fAnalysisVal614', blank=True, null=True)  # Field name made lowercase.
    fanalysisval714 = models.FloatField(db_column='fAnalysisVal714', blank=True, null=True)  # Field name made lowercase.
    fanalysisval814 = models.FloatField(db_column='fAnalysisVal814', blank=True, null=True)  # Field name made lowercase.
    fanalysisval914 = models.FloatField(db_column='fAnalysisVal914', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1014 = models.FloatField(db_column='fAnalysisVal1014', blank=True, null=True)  # Field name made lowercase.
    fanalysisval115 = models.FloatField(db_column='fAnalysisVal115', blank=True, null=True)  # Field name made lowercase.
    fanalysisval215 = models.FloatField(db_column='fAnalysisVal215', blank=True, null=True)  # Field name made lowercase.
    fanalysisval315 = models.FloatField(db_column='fAnalysisVal315', blank=True, null=True)  # Field name made lowercase.
    fanalysisval415 = models.FloatField(db_column='fAnalysisVal415', blank=True, null=True)  # Field name made lowercase.
    fanalysisval515 = models.FloatField(db_column='fAnalysisVal515', blank=True, null=True)  # Field name made lowercase.
    fanalysisval615 = models.FloatField(db_column='fAnalysisVal615', blank=True, null=True)  # Field name made lowercase.
    fanalysisval715 = models.FloatField(db_column='fAnalysisVal715', blank=True, null=True)  # Field name made lowercase.
    fanalysisval815 = models.FloatField(db_column='fAnalysisVal815', blank=True, null=True)  # Field name made lowercase.
    fanalysisval915 = models.FloatField(db_column='fAnalysisVal915', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1015 = models.FloatField(db_column='fAnalysisVal1015', blank=True, null=True)  # Field name made lowercase.
    srrdate = models.CharField(db_column='sRRDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate1 = models.CharField(db_column='sDueDate1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSAAttribute'


class Tmsaattributeoperator(models.Model):
    rroperatorid = models.BigAutoField(db_column='RROperatorID', primary_key=True)  # Field name made lowercase.
    lrrspecificatonid = models.BigIntegerField(db_column='lRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.BigIntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    serialno = models.BigIntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    soperatorname = models.CharField(db_column='sOperatorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue = models.BooleanField(db_column='FOperatorValue', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue = models.FloatField(db_column='fOperatorRefValue', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.BigIntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    serialno1 = models.BigIntegerField(db_column='SerialNo1', blank=True, null=True)  # Field name made lowercase.
    soperatorname1 = models.CharField(db_column='sOperatorName1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue1 = models.BooleanField(db_column='FOperatorValue1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea1 = models.BooleanField(db_column='fOperatorRefValueA1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea2 = models.BooleanField(db_column='fOperatorRefValueA2', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea3 = models.FloatField(db_column='fOperatorRefValueA3', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea4 = models.FloatField(db_column='fOperatorRefValueA4', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea5 = models.FloatField(db_column='fOperatorRefValueA5', blank=True, null=True)  # Field name made lowercase.
    operatorid11 = models.BigIntegerField(db_column='OperatorID11', blank=True, null=True)  # Field name made lowercase.
    serialno11 = models.BigIntegerField(db_column='SerialNo11', blank=True, null=True)  # Field name made lowercase.
    soperatorname11 = models.CharField(db_column='sOperatorName11', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue11 = models.BooleanField(db_column='FOperatorValue11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea11 = models.BooleanField(db_column='fOperatorRefValueA11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea21 = models.BooleanField(db_column='fOperatorRefValueA21', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea31 = models.FloatField(db_column='fOperatorRefValueA31', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea41 = models.FloatField(db_column='fOperatorRefValueA41', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea51 = models.FloatField(db_column='fOperatorRefValueA51', blank=True, null=True)  # Field name made lowercase.
    operatorid12 = models.BigIntegerField(db_column='OperatorID12', blank=True, null=True)  # Field name made lowercase.
    serialno12 = models.BigIntegerField(db_column='SerialNo12', blank=True, null=True)  # Field name made lowercase.
    soperatorname12 = models.CharField(db_column='sOperatorName12', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue12 = models.BooleanField(db_column='FOperatorValue12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea12 = models.BooleanField(db_column='fOperatorRefValueA12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea22 = models.BooleanField(db_column='fOperatorRefValueA22', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea32 = models.FloatField(db_column='fOperatorRefValueA32', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea42 = models.FloatField(db_column='fOperatorRefValueA42', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea52 = models.FloatField(db_column='fOperatorRefValueA52', blank=True, null=True)  # Field name made lowercase.
    operatorid13 = models.BigIntegerField(db_column='OperatorID13', blank=True, null=True)  # Field name made lowercase.
    serialno13 = models.BigIntegerField(db_column='SerialNo13', blank=True, null=True)  # Field name made lowercase.
    soperatorname13 = models.CharField(db_column='sOperatorName13', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue13 = models.BooleanField(db_column='FOperatorValue13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea13 = models.BooleanField(db_column='fOperatorRefValueA13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea23 = models.BooleanField(db_column='fOperatorRefValueA23', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea33 = models.FloatField(db_column='fOperatorRefValueA33', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea43 = models.FloatField(db_column='fOperatorRefValueA43', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea53 = models.FloatField(db_column='fOperatorRefValueA53', blank=True, null=True)  # Field name made lowercase.
    operatorid14 = models.BigIntegerField(db_column='OperatorID14', blank=True, null=True)  # Field name made lowercase.
    serialno14 = models.BigIntegerField(db_column='SerialNo14', blank=True, null=True)  # Field name made lowercase.
    soperatorname14 = models.CharField(db_column='sOperatorName14', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue14 = models.BooleanField(db_column='FOperatorValue14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea14 = models.BooleanField(db_column='fOperatorRefValueA14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea24 = models.BooleanField(db_column='fOperatorRefValueA24', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea34 = models.FloatField(db_column='fOperatorRefValueA34', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea44 = models.FloatField(db_column='fOperatorRefValueA44', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea54 = models.FloatField(db_column='fOperatorRefValueA54', blank=True, null=True)  # Field name made lowercase.
    operatorid15 = models.BigIntegerField(db_column='OperatorID15', blank=True, null=True)  # Field name made lowercase.
    serialno15 = models.BigIntegerField(db_column='SerialNo15', blank=True, null=True)  # Field name made lowercase.
    soperatorname15 = models.CharField(db_column='sOperatorName15', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue15 = models.BooleanField(db_column='FOperatorValue15', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea15 = models.BooleanField(db_column='fOperatorRefValueA15', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea25 = models.BooleanField(db_column='fOperatorRefValueA25', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea35 = models.FloatField(db_column='fOperatorRefValueA35', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea45 = models.FloatField(db_column='fOperatorRefValueA45', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea55 = models.FloatField(db_column='fOperatorRefValueA55', blank=True, null=True)  # Field name made lowercase.
    operatorid111 = models.BigIntegerField(db_column='OperatorID111', blank=True, null=True)  # Field name made lowercase.
    serialno111 = models.BigIntegerField(db_column='SerialNo111', blank=True, null=True)  # Field name made lowercase.
    soperatorname111 = models.CharField(db_column='sOperatorName111', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue111 = models.BooleanField(db_column='FOperatorValue111', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea111 = models.BooleanField(db_column='fOperatorRefValueA111', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea211 = models.BooleanField(db_column='fOperatorRefValueA211', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea311 = models.FloatField(db_column='fOperatorRefValueA311', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea411 = models.FloatField(db_column='fOperatorRefValueA411', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea511 = models.FloatField(db_column='fOperatorRefValueA511', blank=True, null=True)  # Field name made lowercase.
    operatorid121 = models.BigIntegerField(db_column='OperatorID121', blank=True, null=True)  # Field name made lowercase.
    serialno121 = models.BigIntegerField(db_column='SerialNo121', blank=True, null=True)  # Field name made lowercase.
    soperatorname121 = models.CharField(db_column='sOperatorName121', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue121 = models.BooleanField(db_column='FOperatorValue121', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea121 = models.BooleanField(db_column='fOperatorRefValueA121', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea221 = models.BooleanField(db_column='fOperatorRefValueA221', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea321 = models.FloatField(db_column='fOperatorRefValueA321', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea421 = models.FloatField(db_column='fOperatorRefValueA421', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea521 = models.FloatField(db_column='fOperatorRefValueA521', blank=True, null=True)  # Field name made lowercase.
    operatorid131 = models.BigIntegerField(db_column='OperatorID131', blank=True, null=True)  # Field name made lowercase.
    serialno131 = models.BigIntegerField(db_column='SerialNo131', blank=True, null=True)  # Field name made lowercase.
    soperatorname131 = models.CharField(db_column='sOperatorName131', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue131 = models.BooleanField(db_column='FOperatorValue131', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea131 = models.BooleanField(db_column='fOperatorRefValueA131', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea231 = models.BooleanField(db_column='fOperatorRefValueA231', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea331 = models.FloatField(db_column='fOperatorRefValueA331', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea431 = models.FloatField(db_column='fOperatorRefValueA431', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea531 = models.FloatField(db_column='fOperatorRefValueA531', blank=True, null=True)  # Field name made lowercase.
    operatorid141 = models.BigIntegerField(db_column='OperatorID141', blank=True, null=True)  # Field name made lowercase.
    serialno141 = models.BigIntegerField(db_column='SerialNo141', blank=True, null=True)  # Field name made lowercase.
    soperatorname141 = models.CharField(db_column='sOperatorName141', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue141 = models.BooleanField(db_column='FOperatorValue141', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea141 = models.BooleanField(db_column='fOperatorRefValueA141', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea241 = models.BooleanField(db_column='fOperatorRefValueA241', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea341 = models.FloatField(db_column='fOperatorRefValueA341', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea441 = models.FloatField(db_column='fOperatorRefValueA441', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea541 = models.FloatField(db_column='fOperatorRefValueA541', blank=True, null=True)  # Field name made lowercase.
    operatorid151 = models.BigIntegerField(db_column='OperatorID151', blank=True, null=True)  # Field name made lowercase.
    serialno151 = models.BigIntegerField(db_column='SerialNo151', blank=True, null=True)  # Field name made lowercase.
    soperatorname151 = models.CharField(db_column='sOperatorName151', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue151 = models.BooleanField(db_column='FOperatorValue151', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea151 = models.BooleanField(db_column='fOperatorRefValueA151', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea251 = models.BooleanField(db_column='fOperatorRefValueA251', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea351 = models.FloatField(db_column='fOperatorRefValueA351', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea451 = models.FloatField(db_column='fOperatorRefValueA451', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea551 = models.FloatField(db_column='fOperatorRefValueA551', blank=True, null=True)  # Field name made lowercase.
    operatorid112 = models.BigIntegerField(db_column='OperatorID112', blank=True, null=True)  # Field name made lowercase.
    serialno112 = models.BigIntegerField(db_column='SerialNo112', blank=True, null=True)  # Field name made lowercase.
    soperatorname112 = models.CharField(db_column='sOperatorName112', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue112 = models.BooleanField(db_column='FOperatorValue112', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea112 = models.BooleanField(db_column='fOperatorRefValueA112', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea212 = models.BooleanField(db_column='fOperatorRefValueA212', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea312 = models.FloatField(db_column='fOperatorRefValueA312', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea412 = models.FloatField(db_column='fOperatorRefValueA412', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea512 = models.FloatField(db_column='fOperatorRefValueA512', blank=True, null=True)  # Field name made lowercase.
    operatorid122 = models.BigIntegerField(db_column='OperatorID122', blank=True, null=True)  # Field name made lowercase.
    serialno122 = models.BigIntegerField(db_column='SerialNo122', blank=True, null=True)  # Field name made lowercase.
    soperatorname122 = models.CharField(db_column='sOperatorName122', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue122 = models.BooleanField(db_column='FOperatorValue122', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea122 = models.BooleanField(db_column='fOperatorRefValueA122', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea222 = models.BooleanField(db_column='fOperatorRefValueA222', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea322 = models.FloatField(db_column='fOperatorRefValueA322', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea422 = models.FloatField(db_column='fOperatorRefValueA422', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea522 = models.FloatField(db_column='fOperatorRefValueA522', blank=True, null=True)  # Field name made lowercase.
    operatorid132 = models.BigIntegerField(db_column='OperatorID132', blank=True, null=True)  # Field name made lowercase.
    serialno132 = models.BigIntegerField(db_column='SerialNo132', blank=True, null=True)  # Field name made lowercase.
    soperatorname132 = models.CharField(db_column='sOperatorName132', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue132 = models.BooleanField(db_column='FOperatorValue132', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea132 = models.BooleanField(db_column='fOperatorRefValueA132', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea232 = models.BooleanField(db_column='fOperatorRefValueA232', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea332 = models.FloatField(db_column='fOperatorRefValueA332', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea432 = models.FloatField(db_column='fOperatorRefValueA432', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea532 = models.FloatField(db_column='fOperatorRefValueA532', blank=True, null=True)  # Field name made lowercase.
    operatorid142 = models.BigIntegerField(db_column='OperatorID142', blank=True, null=True)  # Field name made lowercase.
    serialno142 = models.BigIntegerField(db_column='SerialNo142', blank=True, null=True)  # Field name made lowercase.
    soperatorname142 = models.CharField(db_column='sOperatorName142', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue142 = models.BooleanField(db_column='FOperatorValue142', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea142 = models.BooleanField(db_column='fOperatorRefValueA142', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea242 = models.BooleanField(db_column='fOperatorRefValueA242', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea342 = models.FloatField(db_column='fOperatorRefValueA342', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea442 = models.FloatField(db_column='fOperatorRefValueA442', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea542 = models.FloatField(db_column='fOperatorRefValueA542', blank=True, null=True)  # Field name made lowercase.
    operatorid152 = models.BigIntegerField(db_column='OperatorID152', blank=True, null=True)  # Field name made lowercase.
    serialno152 = models.BigIntegerField(db_column='SerialNo152', blank=True, null=True)  # Field name made lowercase.
    soperatorname152 = models.CharField(db_column='sOperatorName152', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue152 = models.BooleanField(db_column='FOperatorValue152', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea152 = models.BooleanField(db_column='fOperatorRefValueA152', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea252 = models.BooleanField(db_column='fOperatorRefValueA252', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea352 = models.FloatField(db_column='fOperatorRefValueA352', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea452 = models.FloatField(db_column='fOperatorRefValueA452', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea552 = models.FloatField(db_column='fOperatorRefValueA552', blank=True, null=True)  # Field name made lowercase.
    operatorid113 = models.BigIntegerField(db_column='OperatorID113', blank=True, null=True)  # Field name made lowercase.
    serialno113 = models.BigIntegerField(db_column='SerialNo113', blank=True, null=True)  # Field name made lowercase.
    soperatorname113 = models.CharField(db_column='sOperatorName113', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue113 = models.BooleanField(db_column='FOperatorValue113', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea113 = models.BooleanField(db_column='fOperatorRefValueA113', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea213 = models.BooleanField(db_column='fOperatorRefValueA213', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea313 = models.FloatField(db_column='fOperatorRefValueA313', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea413 = models.FloatField(db_column='fOperatorRefValueA413', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea513 = models.FloatField(db_column='fOperatorRefValueA513', blank=True, null=True)  # Field name made lowercase.
    operatorid123 = models.BigIntegerField(db_column='OperatorID123', blank=True, null=True)  # Field name made lowercase.
    serialno123 = models.BigIntegerField(db_column='SerialNo123', blank=True, null=True)  # Field name made lowercase.
    soperatorname123 = models.CharField(db_column='sOperatorName123', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue123 = models.BooleanField(db_column='FOperatorValue123', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea123 = models.BooleanField(db_column='fOperatorRefValueA123', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea223 = models.BooleanField(db_column='fOperatorRefValueA223', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea323 = models.FloatField(db_column='fOperatorRefValueA323', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea423 = models.FloatField(db_column='fOperatorRefValueA423', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea523 = models.FloatField(db_column='fOperatorRefValueA523', blank=True, null=True)  # Field name made lowercase.
    operatorid133 = models.BigIntegerField(db_column='OperatorID133', blank=True, null=True)  # Field name made lowercase.
    serialno133 = models.BigIntegerField(db_column='SerialNo133', blank=True, null=True)  # Field name made lowercase.
    soperatorname133 = models.CharField(db_column='sOperatorName133', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue133 = models.BooleanField(db_column='FOperatorValue133', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea133 = models.BooleanField(db_column='fOperatorRefValueA133', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea233 = models.BooleanField(db_column='fOperatorRefValueA233', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea333 = models.FloatField(db_column='fOperatorRefValueA333', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea433 = models.FloatField(db_column='fOperatorRefValueA433', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea533 = models.FloatField(db_column='fOperatorRefValueA533', blank=True, null=True)  # Field name made lowercase.
    operatorid143 = models.BigIntegerField(db_column='OperatorID143', blank=True, null=True)  # Field name made lowercase.
    serialno143 = models.BigIntegerField(db_column='SerialNo143', blank=True, null=True)  # Field name made lowercase.
    soperatorname143 = models.CharField(db_column='sOperatorName143', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue143 = models.BooleanField(db_column='FOperatorValue143', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea143 = models.BooleanField(db_column='fOperatorRefValueA143', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea243 = models.BooleanField(db_column='fOperatorRefValueA243', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea343 = models.FloatField(db_column='fOperatorRefValueA343', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea443 = models.FloatField(db_column='fOperatorRefValueA443', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea543 = models.FloatField(db_column='fOperatorRefValueA543', blank=True, null=True)  # Field name made lowercase.
    operatorid153 = models.BigIntegerField(db_column='OperatorID153', blank=True, null=True)  # Field name made lowercase.
    serialno153 = models.BigIntegerField(db_column='SerialNo153', blank=True, null=True)  # Field name made lowercase.
    soperatorname153 = models.CharField(db_column='sOperatorName153', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue153 = models.BooleanField(db_column='FOperatorValue153', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea153 = models.BooleanField(db_column='fOperatorRefValueA153', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea253 = models.BooleanField(db_column='fOperatorRefValueA253', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea353 = models.FloatField(db_column='fOperatorRefValueA353', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea453 = models.FloatField(db_column='fOperatorRefValueA453', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea553 = models.FloatField(db_column='fOperatorRefValueA553', blank=True, null=True)  # Field name made lowercase.
    operatorid114 = models.BigIntegerField(db_column='OperatorID114', blank=True, null=True)  # Field name made lowercase.
    serialno114 = models.BigIntegerField(db_column='SerialNo114', blank=True, null=True)  # Field name made lowercase.
    soperatorname114 = models.CharField(db_column='sOperatorName114', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue114 = models.BooleanField(db_column='FOperatorValue114', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea114 = models.BooleanField(db_column='fOperatorRefValueA114', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea214 = models.BooleanField(db_column='fOperatorRefValueA214', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea314 = models.FloatField(db_column='fOperatorRefValueA314', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea414 = models.FloatField(db_column='fOperatorRefValueA414', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea514 = models.FloatField(db_column='fOperatorRefValueA514', blank=True, null=True)  # Field name made lowercase.
    operatorid124 = models.BigIntegerField(db_column='OperatorID124', blank=True, null=True)  # Field name made lowercase.
    serialno124 = models.BigIntegerField(db_column='SerialNo124', blank=True, null=True)  # Field name made lowercase.
    soperatorname124 = models.CharField(db_column='sOperatorName124', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue124 = models.BooleanField(db_column='FOperatorValue124', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea124 = models.BooleanField(db_column='fOperatorRefValueA124', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea224 = models.BooleanField(db_column='fOperatorRefValueA224', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea324 = models.FloatField(db_column='fOperatorRefValueA324', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea424 = models.FloatField(db_column='fOperatorRefValueA424', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea524 = models.FloatField(db_column='fOperatorRefValueA524', blank=True, null=True)  # Field name made lowercase.
    operatorid134 = models.BigIntegerField(db_column='OperatorID134', blank=True, null=True)  # Field name made lowercase.
    serialno134 = models.BigIntegerField(db_column='SerialNo134', blank=True, null=True)  # Field name made lowercase.
    soperatorname134 = models.CharField(db_column='sOperatorName134', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue134 = models.BooleanField(db_column='FOperatorValue134', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea134 = models.BooleanField(db_column='fOperatorRefValueA134', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea234 = models.BooleanField(db_column='fOperatorRefValueA234', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea334 = models.FloatField(db_column='fOperatorRefValueA334', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea434 = models.FloatField(db_column='fOperatorRefValueA434', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea534 = models.FloatField(db_column='fOperatorRefValueA534', blank=True, null=True)  # Field name made lowercase.
    operatorid144 = models.BigIntegerField(db_column='OperatorID144', blank=True, null=True)  # Field name made lowercase.
    serialno144 = models.BigIntegerField(db_column='SerialNo144', blank=True, null=True)  # Field name made lowercase.
    soperatorname144 = models.CharField(db_column='sOperatorName144', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue144 = models.BooleanField(db_column='FOperatorValue144', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea144 = models.BooleanField(db_column='fOperatorRefValueA144', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea244 = models.BooleanField(db_column='fOperatorRefValueA244', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea344 = models.FloatField(db_column='fOperatorRefValueA344', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea444 = models.FloatField(db_column='fOperatorRefValueA444', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea544 = models.FloatField(db_column='fOperatorRefValueA544', blank=True, null=True)  # Field name made lowercase.
    operatorid154 = models.BigIntegerField(db_column='OperatorID154', blank=True, null=True)  # Field name made lowercase.
    serialno154 = models.BigIntegerField(db_column='SerialNo154', blank=True, null=True)  # Field name made lowercase.
    soperatorname154 = models.CharField(db_column='sOperatorName154', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue154 = models.BooleanField(db_column='FOperatorValue154', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea154 = models.BooleanField(db_column='fOperatorRefValueA154', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea254 = models.BooleanField(db_column='fOperatorRefValueA254', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea354 = models.FloatField(db_column='fOperatorRefValueA354', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea454 = models.FloatField(db_column='fOperatorRefValueA454', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea554 = models.FloatField(db_column='fOperatorRefValueA554', blank=True, null=True)  # Field name made lowercase.
    operatorid115 = models.BigIntegerField(db_column='OperatorID115', blank=True, null=True)  # Field name made lowercase.
    serialno115 = models.BigIntegerField(db_column='SerialNo115', blank=True, null=True)  # Field name made lowercase.
    soperatorname115 = models.CharField(db_column='sOperatorName115', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue115 = models.BooleanField(db_column='FOperatorValue115', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea115 = models.BooleanField(db_column='fOperatorRefValueA115', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea215 = models.BooleanField(db_column='fOperatorRefValueA215', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea315 = models.FloatField(db_column='fOperatorRefValueA315', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea415 = models.FloatField(db_column='fOperatorRefValueA415', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea515 = models.FloatField(db_column='fOperatorRefValueA515', blank=True, null=True)  # Field name made lowercase.
    operatorid125 = models.BigIntegerField(db_column='OperatorID125', blank=True, null=True)  # Field name made lowercase.
    serialno125 = models.BigIntegerField(db_column='SerialNo125', blank=True, null=True)  # Field name made lowercase.
    soperatorname125 = models.CharField(db_column='sOperatorName125', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue125 = models.BooleanField(db_column='FOperatorValue125', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea125 = models.BooleanField(db_column='fOperatorRefValueA125', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea225 = models.BooleanField(db_column='fOperatorRefValueA225', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea325 = models.FloatField(db_column='fOperatorRefValueA325', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea425 = models.FloatField(db_column='fOperatorRefValueA425', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea525 = models.FloatField(db_column='fOperatorRefValueA525', blank=True, null=True)  # Field name made lowercase.
    operatorid135 = models.BigIntegerField(db_column='OperatorID135', blank=True, null=True)  # Field name made lowercase.
    serialno135 = models.BigIntegerField(db_column='SerialNo135', blank=True, null=True)  # Field name made lowercase.
    soperatorname135 = models.CharField(db_column='sOperatorName135', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue135 = models.BooleanField(db_column='FOperatorValue135', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea135 = models.BooleanField(db_column='fOperatorRefValueA135', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea235 = models.BooleanField(db_column='fOperatorRefValueA235', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea335 = models.FloatField(db_column='fOperatorRefValueA335', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea435 = models.FloatField(db_column='fOperatorRefValueA435', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea535 = models.FloatField(db_column='fOperatorRefValueA535', blank=True, null=True)  # Field name made lowercase.
    operatorid145 = models.BigIntegerField(db_column='OperatorID145', blank=True, null=True)  # Field name made lowercase.
    serialno145 = models.BigIntegerField(db_column='SerialNo145', blank=True, null=True)  # Field name made lowercase.
    soperatorname145 = models.CharField(db_column='sOperatorName145', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue145 = models.BooleanField(db_column='FOperatorValue145', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea145 = models.BooleanField(db_column='fOperatorRefValueA145', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea245 = models.BooleanField(db_column='fOperatorRefValueA245', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea345 = models.FloatField(db_column='fOperatorRefValueA345', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea445 = models.FloatField(db_column='fOperatorRefValueA445', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea545 = models.FloatField(db_column='fOperatorRefValueA545', blank=True, null=True)  # Field name made lowercase.
    operatorid155 = models.BigIntegerField(db_column='OperatorID155', blank=True, null=True)  # Field name made lowercase.
    serialno155 = models.BigIntegerField(db_column='SerialNo155', blank=True, null=True)  # Field name made lowercase.
    soperatorname155 = models.CharField(db_column='sOperatorName155', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue155 = models.BooleanField(db_column='FOperatorValue155', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea155 = models.BooleanField(db_column='fOperatorRefValueA155', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea255 = models.BooleanField(db_column='fOperatorRefValueA255', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea355 = models.FloatField(db_column='fOperatorRefValueA355', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea455 = models.FloatField(db_column='fOperatorRefValueA455', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea555 = models.FloatField(db_column='fOperatorRefValueA555', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSAAttributeOperator'


class Tmsabiasanalysis(models.Model):
    lrrspecificatonid = models.BigAutoField(db_column='lRRSpecificatonID', primary_key=True)  # Field name made lowercase.
    rrdate = models.DateTimeField(db_column='RRDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=350, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.FloatField(db_column='Tolerance', blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductID', blank=True, null=True)  # Field name made lowercase.
    lparts = models.BigIntegerField(db_column='lParts', blank=True, null=True)  # Field name made lowercase.
    ltrials = models.BigIntegerField(db_column='lTrials', blank=True, null=True)  # Field name made lowercase.
    loperators = models.BigIntegerField(db_column='lOperators', blank=True, null=True)  # Field name made lowercase.
    specialcharacter = models.CharField(db_column='SpecialCharacter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    considertolerance = models.CharField(db_column='ConsiderTolerance', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcreatetable = models.BooleanField(db_column='bCreateTable', blank=True, null=True)  # Field name made lowercase.
    previouslrrspecificatonid = models.BigIntegerField(db_column='PreviouslRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    reconduct = models.BooleanField(db_column='ReConduct', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    timetaken = models.CharField(db_column='TimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    calibratedby = models.CharField(db_column='CalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    xbarbar = models.FloatField(db_column='XBARBar', blank=True, null=True)  # Field name made lowercase.
    rbar = models.FloatField(db_column='RBar', blank=True, null=True)  # Field name made lowercase.
    uclxbar = models.FloatField(db_column='UCLXBar', blank=True, null=True)  # Field name made lowercase.
    lclxbar = models.FloatField(db_column='LCLXBar', blank=True, null=True)  # Field name made lowercase.
    uclrange = models.FloatField(db_column='UCLRange', blank=True, null=True)  # Field name made lowercase.
    lclrange = models.FloatField(db_column='LCLRange', blank=True, null=True)  # Field name made lowercase.
    dbias = models.FloatField(db_column='dBias', blank=True, null=True)  # Field name made lowercase.
    dsigmarepr = models.FloatField(db_column='dSigmaRepr', blank=True, null=True)  # Field name made lowercase.
    dsigmabias = models.FloatField(db_column='dSigmaBias', blank=True, null=True)  # Field name made lowercase.
    tbias = models.FloatField(db_column='tBias', blank=True, null=True)  # Field name made lowercase.
    tcritical = models.FloatField(db_column='tCritical', blank=True, null=True)  # Field name made lowercase.
    biasstatus = models.FloatField(db_column='BiasStatus', blank=True, null=True)  # Field name made lowercase.
    biasvalue = models.FloatField(db_column='BiasValue', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    bcategory = models.BooleanField(db_column='bCategory', blank=True, null=True)  # Field name made lowercase.
    categoryhistorymsaid = models.BigIntegerField(db_column='CategoryHistoryMSAID', blank=True, null=True)  # Field name made lowercase.
    lcategoryscheduleid = models.BigIntegerField(db_column='lCategoryScheduleID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fanalysisval = models.FloatField(db_column='fAnalysisVal', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1 = models.FloatField(db_column='fAnalysisVal1', blank=True, null=True)  # Field name made lowercase.
    fanalysisval2 = models.FloatField(db_column='fAnalysisVal2', blank=True, null=True)  # Field name made lowercase.
    fanalysisval3 = models.FloatField(db_column='fAnalysisVal3', blank=True, null=True)  # Field name made lowercase.
    fanalysisval4 = models.FloatField(db_column='fAnalysisVal4', blank=True, null=True)  # Field name made lowercase.
    fanalysisval5 = models.FloatField(db_column='fAnalysisVal5', blank=True, null=True)  # Field name made lowercase.
    fanalysisval6 = models.FloatField(db_column='fAnalysisVal6', blank=True, null=True)  # Field name made lowercase.
    fanalysisval7 = models.FloatField(db_column='fAnalysisVal7', blank=True, null=True)  # Field name made lowercase.
    fanalysisval8 = models.FloatField(db_column='fAnalysisVal8', blank=True, null=True)  # Field name made lowercase.
    fanalysisval9 = models.FloatField(db_column='fAnalysisVal9', blank=True, null=True)  # Field name made lowercase.
    fanalysisval10 = models.FloatField(db_column='fAnalysisVal10', blank=True, null=True)  # Field name made lowercase.
    fanalysisval11 = models.FloatField(db_column='fAnalysisVal11', blank=True, null=True)  # Field name made lowercase.
    fanalysisval21 = models.FloatField(db_column='fAnalysisVal21', blank=True, null=True)  # Field name made lowercase.
    fanalysisval31 = models.FloatField(db_column='fAnalysisVal31', blank=True, null=True)  # Field name made lowercase.
    fanalysisval41 = models.FloatField(db_column='fAnalysisVal41', blank=True, null=True)  # Field name made lowercase.
    fanalysisval51 = models.FloatField(db_column='fAnalysisVal51', blank=True, null=True)  # Field name made lowercase.
    fanalysisval61 = models.FloatField(db_column='fAnalysisVal61', blank=True, null=True)  # Field name made lowercase.
    fanalysisval71 = models.FloatField(db_column='fAnalysisVal71', blank=True, null=True)  # Field name made lowercase.
    fanalysisval81 = models.FloatField(db_column='fAnalysisVal81', blank=True, null=True)  # Field name made lowercase.
    fanalysisval91 = models.FloatField(db_column='fAnalysisVal91', blank=True, null=True)  # Field name made lowercase.
    fanalysisval101 = models.FloatField(db_column='fAnalysisVal101', blank=True, null=True)  # Field name made lowercase.
    fanalysisval12 = models.FloatField(db_column='fAnalysisVal12', blank=True, null=True)  # Field name made lowercase.
    fanalysisval22 = models.FloatField(db_column='fAnalysisVal22', blank=True, null=True)  # Field name made lowercase.
    fanalysisval32 = models.FloatField(db_column='fAnalysisVal32', blank=True, null=True)  # Field name made lowercase.
    fanalysisval42 = models.FloatField(db_column='fAnalysisVal42', blank=True, null=True)  # Field name made lowercase.
    fanalysisval52 = models.FloatField(db_column='fAnalysisVal52', blank=True, null=True)  # Field name made lowercase.
    fanalysisval62 = models.FloatField(db_column='fAnalysisVal62', blank=True, null=True)  # Field name made lowercase.
    fanalysisval72 = models.FloatField(db_column='fAnalysisVal72', blank=True, null=True)  # Field name made lowercase.
    fanalysisval82 = models.FloatField(db_column='fAnalysisVal82', blank=True, null=True)  # Field name made lowercase.
    fanalysisval92 = models.FloatField(db_column='fAnalysisVal92', blank=True, null=True)  # Field name made lowercase.
    fanalysisval102 = models.FloatField(db_column='fAnalysisVal102', blank=True, null=True)  # Field name made lowercase.
    fanalysisval13 = models.FloatField(db_column='fAnalysisVal13', blank=True, null=True)  # Field name made lowercase.
    fanalysisval23 = models.FloatField(db_column='fAnalysisVal23', blank=True, null=True)  # Field name made lowercase.
    fanalysisval33 = models.FloatField(db_column='fAnalysisVal33', blank=True, null=True)  # Field name made lowercase.
    fanalysisval43 = models.FloatField(db_column='fAnalysisVal43', blank=True, null=True)  # Field name made lowercase.
    fanalysisval53 = models.FloatField(db_column='fAnalysisVal53', blank=True, null=True)  # Field name made lowercase.
    fanalysisval63 = models.FloatField(db_column='fAnalysisVal63', blank=True, null=True)  # Field name made lowercase.
    fanalysisval73 = models.FloatField(db_column='fAnalysisVal73', blank=True, null=True)  # Field name made lowercase.
    fanalysisval83 = models.FloatField(db_column='fAnalysisVal83', blank=True, null=True)  # Field name made lowercase.
    fanalysisval93 = models.FloatField(db_column='fAnalysisVal93', blank=True, null=True)  # Field name made lowercase.
    fanalysisval103 = models.FloatField(db_column='fAnalysisVal103', blank=True, null=True)  # Field name made lowercase.
    fanalysisval14 = models.FloatField(db_column='fAnalysisVal14', blank=True, null=True)  # Field name made lowercase.
    fanalysisval24 = models.FloatField(db_column='fAnalysisVal24', blank=True, null=True)  # Field name made lowercase.
    fanalysisval34 = models.FloatField(db_column='fAnalysisVal34', blank=True, null=True)  # Field name made lowercase.
    fanalysisval44 = models.FloatField(db_column='fAnalysisVal44', blank=True, null=True)  # Field name made lowercase.
    fanalysisval54 = models.FloatField(db_column='fAnalysisVal54', blank=True, null=True)  # Field name made lowercase.
    fanalysisval64 = models.FloatField(db_column='fAnalysisVal64', blank=True, null=True)  # Field name made lowercase.
    fanalysisval74 = models.FloatField(db_column='fAnalysisVal74', blank=True, null=True)  # Field name made lowercase.
    fanalysisval84 = models.FloatField(db_column='fAnalysisVal84', blank=True, null=True)  # Field name made lowercase.
    fanalysisval94 = models.FloatField(db_column='fAnalysisVal94', blank=True, null=True)  # Field name made lowercase.
    fanalysisval104 = models.FloatField(db_column='fAnalysisVal104', blank=True, null=True)  # Field name made lowercase.
    fanalysisval15 = models.FloatField(db_column='fAnalysisVal15', blank=True, null=True)  # Field name made lowercase.
    fanalysisval25 = models.FloatField(db_column='fAnalysisVal25', blank=True, null=True)  # Field name made lowercase.
    fanalysisval35 = models.FloatField(db_column='fAnalysisVal35', blank=True, null=True)  # Field name made lowercase.
    fanalysisval45 = models.FloatField(db_column='fAnalysisVal45', blank=True, null=True)  # Field name made lowercase.
    fanalysisval55 = models.FloatField(db_column='fAnalysisVal55', blank=True, null=True)  # Field name made lowercase.
    fanalysisval65 = models.FloatField(db_column='fAnalysisVal65', blank=True, null=True)  # Field name made lowercase.
    fanalysisval75 = models.FloatField(db_column='fAnalysisVal75', blank=True, null=True)  # Field name made lowercase.
    fanalysisval85 = models.FloatField(db_column='fAnalysisVal85', blank=True, null=True)  # Field name made lowercase.
    fanalysisval95 = models.FloatField(db_column='fAnalysisVal95', blank=True, null=True)  # Field name made lowercase.
    fanalysisval105 = models.FloatField(db_column='fAnalysisVal105', blank=True, null=True)  # Field name made lowercase.
    fanalysisval16 = models.FloatField(db_column='fAnalysisVal16', blank=True, null=True)  # Field name made lowercase.
    fanalysisval26 = models.FloatField(db_column='fAnalysisVal26', blank=True, null=True)  # Field name made lowercase.
    fanalysisval36 = models.FloatField(db_column='fAnalysisVal36', blank=True, null=True)  # Field name made lowercase.
    fanalysisval46 = models.FloatField(db_column='fAnalysisVal46', blank=True, null=True)  # Field name made lowercase.
    fanalysisval56 = models.FloatField(db_column='fAnalysisVal56', blank=True, null=True)  # Field name made lowercase.
    fanalysisval66 = models.FloatField(db_column='fAnalysisVal66', blank=True, null=True)  # Field name made lowercase.
    fanalysisval76 = models.FloatField(db_column='fAnalysisVal76', blank=True, null=True)  # Field name made lowercase.
    fanalysisval86 = models.FloatField(db_column='fAnalysisVal86', blank=True, null=True)  # Field name made lowercase.
    fanalysisval96 = models.FloatField(db_column='fAnalysisVal96', blank=True, null=True)  # Field name made lowercase.
    fanalysisval106 = models.FloatField(db_column='fAnalysisVal106', blank=True, null=True)  # Field name made lowercase.
    fanalysisval17 = models.FloatField(db_column='fAnalysisVal17', blank=True, null=True)  # Field name made lowercase.
    fanalysisval27 = models.FloatField(db_column='fAnalysisVal27', blank=True, null=True)  # Field name made lowercase.
    fanalysisval37 = models.FloatField(db_column='fAnalysisVal37', blank=True, null=True)  # Field name made lowercase.
    fanalysisval47 = models.FloatField(db_column='fAnalysisVal47', blank=True, null=True)  # Field name made lowercase.
    fanalysisval57 = models.FloatField(db_column='fAnalysisVal57', blank=True, null=True)  # Field name made lowercase.
    fanalysisval67 = models.FloatField(db_column='fAnalysisVal67', blank=True, null=True)  # Field name made lowercase.
    fanalysisval77 = models.FloatField(db_column='fAnalysisVal77', blank=True, null=True)  # Field name made lowercase.
    fanalysisval87 = models.FloatField(db_column='fAnalysisVal87', blank=True, null=True)  # Field name made lowercase.
    fanalysisval97 = models.FloatField(db_column='fAnalysisVal97', blank=True, null=True)  # Field name made lowercase.
    fanalysisval107 = models.FloatField(db_column='fAnalysisVal107', blank=True, null=True)  # Field name made lowercase.
    fanalysisval18 = models.FloatField(db_column='fAnalysisVal18', blank=True, null=True)  # Field name made lowercase.
    fanalysisval28 = models.FloatField(db_column='fAnalysisVal28', blank=True, null=True)  # Field name made lowercase.
    fanalysisval38 = models.FloatField(db_column='fAnalysisVal38', blank=True, null=True)  # Field name made lowercase.
    fanalysisval48 = models.FloatField(db_column='fAnalysisVal48', blank=True, null=True)  # Field name made lowercase.
    fanalysisval58 = models.FloatField(db_column='fAnalysisVal58', blank=True, null=True)  # Field name made lowercase.
    fanalysisval68 = models.FloatField(db_column='fAnalysisVal68', blank=True, null=True)  # Field name made lowercase.
    fanalysisval78 = models.FloatField(db_column='fAnalysisVal78', blank=True, null=True)  # Field name made lowercase.
    fanalysisval88 = models.FloatField(db_column='fAnalysisVal88', blank=True, null=True)  # Field name made lowercase.
    fanalysisval98 = models.FloatField(db_column='fAnalysisVal98', blank=True, null=True)  # Field name made lowercase.
    fanalysisval108 = models.FloatField(db_column='fAnalysisVal108', blank=True, null=True)  # Field name made lowercase.
    fanalysisval19 = models.FloatField(db_column='fAnalysisVal19', blank=True, null=True)  # Field name made lowercase.
    fanalysisval29 = models.FloatField(db_column='fAnalysisVal29', blank=True, null=True)  # Field name made lowercase.
    fanalysisval39 = models.FloatField(db_column='fAnalysisVal39', blank=True, null=True)  # Field name made lowercase.
    fanalysisval49 = models.FloatField(db_column='fAnalysisVal49', blank=True, null=True)  # Field name made lowercase.
    fanalysisval59 = models.FloatField(db_column='fAnalysisVal59', blank=True, null=True)  # Field name made lowercase.
    fanalysisval69 = models.FloatField(db_column='fAnalysisVal69', blank=True, null=True)  # Field name made lowercase.
    fanalysisval79 = models.FloatField(db_column='fAnalysisVal79', blank=True, null=True)  # Field name made lowercase.
    fanalysisval89 = models.FloatField(db_column='fAnalysisVal89', blank=True, null=True)  # Field name made lowercase.
    fanalysisval99 = models.FloatField(db_column='fAnalysisVal99', blank=True, null=True)  # Field name made lowercase.
    fanalysisval109 = models.FloatField(db_column='fAnalysisVal109', blank=True, null=True)  # Field name made lowercase.
    fanalysisval110 = models.FloatField(db_column='fAnalysisVal110', blank=True, null=True)  # Field name made lowercase.
    fanalysisval210 = models.FloatField(db_column='fAnalysisVal210', blank=True, null=True)  # Field name made lowercase.
    fanalysisval310 = models.FloatField(db_column='fAnalysisVal310', blank=True, null=True)  # Field name made lowercase.
    fanalysisval410 = models.FloatField(db_column='fAnalysisVal410', blank=True, null=True)  # Field name made lowercase.
    fanalysisval510 = models.FloatField(db_column='fAnalysisVal510', blank=True, null=True)  # Field name made lowercase.
    fanalysisval610 = models.FloatField(db_column='fAnalysisVal610', blank=True, null=True)  # Field name made lowercase.
    fanalysisval710 = models.FloatField(db_column='fAnalysisVal710', blank=True, null=True)  # Field name made lowercase.
    fanalysisval810 = models.FloatField(db_column='fAnalysisVal810', blank=True, null=True)  # Field name made lowercase.
    fanalysisval910 = models.FloatField(db_column='fAnalysisVal910', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1010 = models.FloatField(db_column='fAnalysisVal1010', blank=True, null=True)  # Field name made lowercase.
    fanalysisval111 = models.FloatField(db_column='fAnalysisVal111', blank=True, null=True)  # Field name made lowercase.
    fanalysisval211 = models.FloatField(db_column='fAnalysisVal211', blank=True, null=True)  # Field name made lowercase.
    fanalysisval311 = models.FloatField(db_column='fAnalysisVal311', blank=True, null=True)  # Field name made lowercase.
    fanalysisval411 = models.FloatField(db_column='fAnalysisVal411', blank=True, null=True)  # Field name made lowercase.
    fanalysisval511 = models.FloatField(db_column='fAnalysisVal511', blank=True, null=True)  # Field name made lowercase.
    fanalysisval611 = models.FloatField(db_column='fAnalysisVal611', blank=True, null=True)  # Field name made lowercase.
    fanalysisval711 = models.FloatField(db_column='fAnalysisVal711', blank=True, null=True)  # Field name made lowercase.
    fanalysisval811 = models.FloatField(db_column='fAnalysisVal811', blank=True, null=True)  # Field name made lowercase.
    fanalysisval911 = models.FloatField(db_column='fAnalysisVal911', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1011 = models.FloatField(db_column='fAnalysisVal1011', blank=True, null=True)  # Field name made lowercase.
    fanalysisval112 = models.FloatField(db_column='fAnalysisVal112', blank=True, null=True)  # Field name made lowercase.
    fanalysisval212 = models.FloatField(db_column='fAnalysisVal212', blank=True, null=True)  # Field name made lowercase.
    fanalysisval312 = models.FloatField(db_column='fAnalysisVal312', blank=True, null=True)  # Field name made lowercase.
    fanalysisval412 = models.FloatField(db_column='fAnalysisVal412', blank=True, null=True)  # Field name made lowercase.
    fanalysisval512 = models.FloatField(db_column='fAnalysisVal512', blank=True, null=True)  # Field name made lowercase.
    fanalysisval612 = models.FloatField(db_column='fAnalysisVal612', blank=True, null=True)  # Field name made lowercase.
    fanalysisval712 = models.FloatField(db_column='fAnalysisVal712', blank=True, null=True)  # Field name made lowercase.
    fanalysisval812 = models.FloatField(db_column='fAnalysisVal812', blank=True, null=True)  # Field name made lowercase.
    fanalysisval912 = models.FloatField(db_column='fAnalysisVal912', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1012 = models.FloatField(db_column='fAnalysisVal1012', blank=True, null=True)  # Field name made lowercase.
    fanalysisval113 = models.FloatField(db_column='fAnalysisVal113', blank=True, null=True)  # Field name made lowercase.
    fanalysisval213 = models.FloatField(db_column='fAnalysisVal213', blank=True, null=True)  # Field name made lowercase.
    fanalysisval313 = models.FloatField(db_column='fAnalysisVal313', blank=True, null=True)  # Field name made lowercase.
    fanalysisval413 = models.FloatField(db_column='fAnalysisVal413', blank=True, null=True)  # Field name made lowercase.
    fanalysisval513 = models.FloatField(db_column='fAnalysisVal513', blank=True, null=True)  # Field name made lowercase.
    fanalysisval613 = models.FloatField(db_column='fAnalysisVal613', blank=True, null=True)  # Field name made lowercase.
    fanalysisval713 = models.FloatField(db_column='fAnalysisVal713', blank=True, null=True)  # Field name made lowercase.
    fanalysisval813 = models.FloatField(db_column='fAnalysisVal813', blank=True, null=True)  # Field name made lowercase.
    fanalysisval913 = models.FloatField(db_column='fAnalysisVal913', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1013 = models.FloatField(db_column='fAnalysisVal1013', blank=True, null=True)  # Field name made lowercase.
    fanalysisval114 = models.FloatField(db_column='fAnalysisVal114', blank=True, null=True)  # Field name made lowercase.
    fanalysisval214 = models.FloatField(db_column='fAnalysisVal214', blank=True, null=True)  # Field name made lowercase.
    fanalysisval314 = models.FloatField(db_column='fAnalysisVal314', blank=True, null=True)  # Field name made lowercase.
    fanalysisval414 = models.FloatField(db_column='fAnalysisVal414', blank=True, null=True)  # Field name made lowercase.
    fanalysisval514 = models.FloatField(db_column='fAnalysisVal514', blank=True, null=True)  # Field name made lowercase.
    fanalysisval614 = models.FloatField(db_column='fAnalysisVal614', blank=True, null=True)  # Field name made lowercase.
    fanalysisval714 = models.FloatField(db_column='fAnalysisVal714', blank=True, null=True)  # Field name made lowercase.
    fanalysisval814 = models.FloatField(db_column='fAnalysisVal814', blank=True, null=True)  # Field name made lowercase.
    fanalysisval914 = models.FloatField(db_column='fAnalysisVal914', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1014 = models.FloatField(db_column='fAnalysisVal1014', blank=True, null=True)  # Field name made lowercase.
    fanalysisval115 = models.FloatField(db_column='fAnalysisVal115', blank=True, null=True)  # Field name made lowercase.
    fanalysisval215 = models.FloatField(db_column='fAnalysisVal215', blank=True, null=True)  # Field name made lowercase.
    fanalysisval315 = models.FloatField(db_column='fAnalysisVal315', blank=True, null=True)  # Field name made lowercase.
    fanalysisval415 = models.FloatField(db_column='fAnalysisVal415', blank=True, null=True)  # Field name made lowercase.
    fanalysisval515 = models.FloatField(db_column='fAnalysisVal515', blank=True, null=True)  # Field name made lowercase.
    fanalysisval615 = models.FloatField(db_column='fAnalysisVal615', blank=True, null=True)  # Field name made lowercase.
    fanalysisval715 = models.FloatField(db_column='fAnalysisVal715', blank=True, null=True)  # Field name made lowercase.
    fanalysisval815 = models.FloatField(db_column='fAnalysisVal815', blank=True, null=True)  # Field name made lowercase.
    fanalysisval915 = models.FloatField(db_column='fAnalysisVal915', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1015 = models.FloatField(db_column='fAnalysisVal1015', blank=True, null=True)  # Field name made lowercase.
    srrdate = models.CharField(db_column='sRRDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate1 = models.CharField(db_column='sDueDate1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSABiasAnalysis'


class Tmsabiasoperator(models.Model):
    rroperatorid = models.BigAutoField(db_column='RROperatorID', primary_key=True)  # Field name made lowercase.
    lrrspecificatonid = models.BigIntegerField(db_column='lRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.BigIntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    serialno = models.BigIntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    soperatorname = models.CharField(db_column='sOperatorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue = models.FloatField(db_column='FOperatorValue', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue = models.FloatField(db_column='fOperatorRefValue', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.BigIntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    serialno1 = models.BigIntegerField(db_column='SerialNo1', blank=True, null=True)  # Field name made lowercase.
    soperatorname1 = models.CharField(db_column='sOperatorName1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue1 = models.FloatField(db_column='FOperatorValue1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue1 = models.FloatField(db_column='fOperatorRefValue1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSABiasOperator'


class Tmsalinearityanalysis(models.Model):
    lrrspecificatonid = models.BigAutoField(db_column='lRRSpecificatonID', primary_key=True)  # Field name made lowercase.
    rrdate = models.DateTimeField(db_column='RRDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=350, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.FloatField(db_column='Tolerance', blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductID', blank=True, null=True)  # Field name made lowercase.
    lparts = models.BigIntegerField(db_column='lParts', blank=True, null=True)  # Field name made lowercase.
    ltrials = models.BigIntegerField(db_column='lTrials', blank=True, null=True)  # Field name made lowercase.
    loperators = models.BigIntegerField(db_column='lOperators', blank=True, null=True)  # Field name made lowercase.
    specialcharacter = models.CharField(db_column='SpecialCharacter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    considertolerance = models.CharField(db_column='ConsiderTolerance', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcreatetable = models.BooleanField(db_column='bCreateTable', blank=True, null=True)  # Field name made lowercase.
    previouslrrspecificatonid = models.BigIntegerField(db_column='PreviouslRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    reconduct = models.BooleanField(db_column='ReConduct', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    timetaken = models.CharField(db_column='TimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    calibratedby = models.CharField(db_column='CalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    xbarbar = models.FloatField(db_column='XBARBar', blank=True, null=True)  # Field name made lowercase.
    rbar = models.FloatField(db_column='RBar', blank=True, null=True)  # Field name made lowercase.
    uclxbar = models.FloatField(db_column='UCLXBar', blank=True, null=True)  # Field name made lowercase.
    lclxbar = models.FloatField(db_column='LCLXBar', blank=True, null=True)  # Field name made lowercase.
    uclrange = models.FloatField(db_column='UCLRange', blank=True, null=True)  # Field name made lowercase.
    lclrange = models.FloatField(db_column='LCLRange', blank=True, null=True)  # Field name made lowercase.
    dbias = models.FloatField(db_column='dBias', blank=True, null=True)  # Field name made lowercase.
    dsigmarepr = models.FloatField(db_column='dSigmaRepr', blank=True, null=True)  # Field name made lowercase.
    dsigmabias = models.FloatField(db_column='dSigmaBias', blank=True, null=True)  # Field name made lowercase.
    tbias = models.FloatField(db_column='tBias', blank=True, null=True)  # Field name made lowercase.
    tcritical = models.FloatField(db_column='tCritical', blank=True, null=True)  # Field name made lowercase.
    biasstatus = models.FloatField(db_column='BiasStatus', blank=True, null=True)  # Field name made lowercase.
    biasvalue = models.FloatField(db_column='BiasValue', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    bcategory = models.BooleanField(db_column='bCategory', blank=True, null=True)  # Field name made lowercase.
    categoryhistorymsaid = models.BigIntegerField(db_column='CategoryHistoryMSAID', blank=True, null=True)  # Field name made lowercase.
    lcategoryscheduleid = models.BigIntegerField(db_column='lCategoryScheduleID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fanalysisval = models.FloatField(db_column='fAnalysisVal', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1 = models.FloatField(db_column='fAnalysisVal1', blank=True, null=True)  # Field name made lowercase.
    fanalysisval2 = models.FloatField(db_column='fAnalysisVal2', blank=True, null=True)  # Field name made lowercase.
    fanalysisval3 = models.FloatField(db_column='fAnalysisVal3', blank=True, null=True)  # Field name made lowercase.
    fanalysisval4 = models.FloatField(db_column='fAnalysisVal4', blank=True, null=True)  # Field name made lowercase.
    fanalysisval5 = models.FloatField(db_column='fAnalysisVal5', blank=True, null=True)  # Field name made lowercase.
    fanalysisval6 = models.FloatField(db_column='fAnalysisVal6', blank=True, null=True)  # Field name made lowercase.
    fanalysisval7 = models.FloatField(db_column='fAnalysisVal7', blank=True, null=True)  # Field name made lowercase.
    fanalysisval8 = models.FloatField(db_column='fAnalysisVal8', blank=True, null=True)  # Field name made lowercase.
    fanalysisval9 = models.FloatField(db_column='fAnalysisVal9', blank=True, null=True)  # Field name made lowercase.
    fanalysisval10 = models.FloatField(db_column='fAnalysisVal10', blank=True, null=True)  # Field name made lowercase.
    fanalysisval11 = models.FloatField(db_column='fAnalysisVal11', blank=True, null=True)  # Field name made lowercase.
    fanalysisval21 = models.FloatField(db_column='fAnalysisVal21', blank=True, null=True)  # Field name made lowercase.
    fanalysisval31 = models.FloatField(db_column='fAnalysisVal31', blank=True, null=True)  # Field name made lowercase.
    fanalysisval41 = models.FloatField(db_column='fAnalysisVal41', blank=True, null=True)  # Field name made lowercase.
    fanalysisval51 = models.FloatField(db_column='fAnalysisVal51', blank=True, null=True)  # Field name made lowercase.
    fanalysisval61 = models.FloatField(db_column='fAnalysisVal61', blank=True, null=True)  # Field name made lowercase.
    fanalysisval71 = models.FloatField(db_column='fAnalysisVal71', blank=True, null=True)  # Field name made lowercase.
    fanalysisval81 = models.FloatField(db_column='fAnalysisVal81', blank=True, null=True)  # Field name made lowercase.
    fanalysisval91 = models.FloatField(db_column='fAnalysisVal91', blank=True, null=True)  # Field name made lowercase.
    fanalysisval101 = models.FloatField(db_column='fAnalysisVal101', blank=True, null=True)  # Field name made lowercase.
    fanalysisval12 = models.FloatField(db_column='fAnalysisVal12', blank=True, null=True)  # Field name made lowercase.
    fanalysisval22 = models.FloatField(db_column='fAnalysisVal22', blank=True, null=True)  # Field name made lowercase.
    fanalysisval32 = models.FloatField(db_column='fAnalysisVal32', blank=True, null=True)  # Field name made lowercase.
    fanalysisval42 = models.FloatField(db_column='fAnalysisVal42', blank=True, null=True)  # Field name made lowercase.
    fanalysisval52 = models.FloatField(db_column='fAnalysisVal52', blank=True, null=True)  # Field name made lowercase.
    fanalysisval62 = models.FloatField(db_column='fAnalysisVal62', blank=True, null=True)  # Field name made lowercase.
    fanalysisval72 = models.FloatField(db_column='fAnalysisVal72', blank=True, null=True)  # Field name made lowercase.
    fanalysisval82 = models.FloatField(db_column='fAnalysisVal82', blank=True, null=True)  # Field name made lowercase.
    fanalysisval92 = models.FloatField(db_column='fAnalysisVal92', blank=True, null=True)  # Field name made lowercase.
    fanalysisval102 = models.FloatField(db_column='fAnalysisVal102', blank=True, null=True)  # Field name made lowercase.
    fanalysisval13 = models.FloatField(db_column='fAnalysisVal13', blank=True, null=True)  # Field name made lowercase.
    fanalysisval23 = models.FloatField(db_column='fAnalysisVal23', blank=True, null=True)  # Field name made lowercase.
    fanalysisval33 = models.FloatField(db_column='fAnalysisVal33', blank=True, null=True)  # Field name made lowercase.
    fanalysisval43 = models.FloatField(db_column='fAnalysisVal43', blank=True, null=True)  # Field name made lowercase.
    fanalysisval53 = models.FloatField(db_column='fAnalysisVal53', blank=True, null=True)  # Field name made lowercase.
    fanalysisval63 = models.FloatField(db_column='fAnalysisVal63', blank=True, null=True)  # Field name made lowercase.
    fanalysisval73 = models.FloatField(db_column='fAnalysisVal73', blank=True, null=True)  # Field name made lowercase.
    fanalysisval83 = models.FloatField(db_column='fAnalysisVal83', blank=True, null=True)  # Field name made lowercase.
    fanalysisval93 = models.FloatField(db_column='fAnalysisVal93', blank=True, null=True)  # Field name made lowercase.
    fanalysisval103 = models.FloatField(db_column='fAnalysisVal103', blank=True, null=True)  # Field name made lowercase.
    fanalysisval14 = models.FloatField(db_column='fAnalysisVal14', blank=True, null=True)  # Field name made lowercase.
    fanalysisval24 = models.FloatField(db_column='fAnalysisVal24', blank=True, null=True)  # Field name made lowercase.
    fanalysisval34 = models.FloatField(db_column='fAnalysisVal34', blank=True, null=True)  # Field name made lowercase.
    fanalysisval44 = models.FloatField(db_column='fAnalysisVal44', blank=True, null=True)  # Field name made lowercase.
    fanalysisval54 = models.FloatField(db_column='fAnalysisVal54', blank=True, null=True)  # Field name made lowercase.
    fanalysisval64 = models.FloatField(db_column='fAnalysisVal64', blank=True, null=True)  # Field name made lowercase.
    fanalysisval74 = models.FloatField(db_column='fAnalysisVal74', blank=True, null=True)  # Field name made lowercase.
    fanalysisval84 = models.FloatField(db_column='fAnalysisVal84', blank=True, null=True)  # Field name made lowercase.
    fanalysisval94 = models.FloatField(db_column='fAnalysisVal94', blank=True, null=True)  # Field name made lowercase.
    fanalysisval104 = models.FloatField(db_column='fAnalysisVal104', blank=True, null=True)  # Field name made lowercase.
    fanalysisval15 = models.FloatField(db_column='fAnalysisVal15', blank=True, null=True)  # Field name made lowercase.
    fanalysisval25 = models.FloatField(db_column='fAnalysisVal25', blank=True, null=True)  # Field name made lowercase.
    fanalysisval35 = models.FloatField(db_column='fAnalysisVal35', blank=True, null=True)  # Field name made lowercase.
    fanalysisval45 = models.FloatField(db_column='fAnalysisVal45', blank=True, null=True)  # Field name made lowercase.
    fanalysisval55 = models.FloatField(db_column='fAnalysisVal55', blank=True, null=True)  # Field name made lowercase.
    fanalysisval65 = models.FloatField(db_column='fAnalysisVal65', blank=True, null=True)  # Field name made lowercase.
    fanalysisval75 = models.FloatField(db_column='fAnalysisVal75', blank=True, null=True)  # Field name made lowercase.
    fanalysisval85 = models.FloatField(db_column='fAnalysisVal85', blank=True, null=True)  # Field name made lowercase.
    fanalysisval95 = models.FloatField(db_column='fAnalysisVal95', blank=True, null=True)  # Field name made lowercase.
    fanalysisval105 = models.FloatField(db_column='fAnalysisVal105', blank=True, null=True)  # Field name made lowercase.
    fanalysisval16 = models.FloatField(db_column='fAnalysisVal16', blank=True, null=True)  # Field name made lowercase.
    fanalysisval26 = models.FloatField(db_column='fAnalysisVal26', blank=True, null=True)  # Field name made lowercase.
    fanalysisval36 = models.FloatField(db_column='fAnalysisVal36', blank=True, null=True)  # Field name made lowercase.
    fanalysisval46 = models.FloatField(db_column='fAnalysisVal46', blank=True, null=True)  # Field name made lowercase.
    fanalysisval56 = models.FloatField(db_column='fAnalysisVal56', blank=True, null=True)  # Field name made lowercase.
    fanalysisval66 = models.FloatField(db_column='fAnalysisVal66', blank=True, null=True)  # Field name made lowercase.
    fanalysisval76 = models.FloatField(db_column='fAnalysisVal76', blank=True, null=True)  # Field name made lowercase.
    fanalysisval86 = models.FloatField(db_column='fAnalysisVal86', blank=True, null=True)  # Field name made lowercase.
    fanalysisval96 = models.FloatField(db_column='fAnalysisVal96', blank=True, null=True)  # Field name made lowercase.
    fanalysisval106 = models.FloatField(db_column='fAnalysisVal106', blank=True, null=True)  # Field name made lowercase.
    fanalysisval17 = models.FloatField(db_column='fAnalysisVal17', blank=True, null=True)  # Field name made lowercase.
    fanalysisval27 = models.FloatField(db_column='fAnalysisVal27', blank=True, null=True)  # Field name made lowercase.
    fanalysisval37 = models.FloatField(db_column='fAnalysisVal37', blank=True, null=True)  # Field name made lowercase.
    fanalysisval47 = models.FloatField(db_column='fAnalysisVal47', blank=True, null=True)  # Field name made lowercase.
    fanalysisval57 = models.FloatField(db_column='fAnalysisVal57', blank=True, null=True)  # Field name made lowercase.
    fanalysisval67 = models.FloatField(db_column='fAnalysisVal67', blank=True, null=True)  # Field name made lowercase.
    fanalysisval77 = models.FloatField(db_column='fAnalysisVal77', blank=True, null=True)  # Field name made lowercase.
    fanalysisval87 = models.FloatField(db_column='fAnalysisVal87', blank=True, null=True)  # Field name made lowercase.
    fanalysisval97 = models.FloatField(db_column='fAnalysisVal97', blank=True, null=True)  # Field name made lowercase.
    fanalysisval107 = models.FloatField(db_column='fAnalysisVal107', blank=True, null=True)  # Field name made lowercase.
    fanalysisval18 = models.FloatField(db_column='fAnalysisVal18', blank=True, null=True)  # Field name made lowercase.
    fanalysisval28 = models.FloatField(db_column='fAnalysisVal28', blank=True, null=True)  # Field name made lowercase.
    fanalysisval38 = models.FloatField(db_column='fAnalysisVal38', blank=True, null=True)  # Field name made lowercase.
    fanalysisval48 = models.FloatField(db_column='fAnalysisVal48', blank=True, null=True)  # Field name made lowercase.
    fanalysisval58 = models.FloatField(db_column='fAnalysisVal58', blank=True, null=True)  # Field name made lowercase.
    fanalysisval68 = models.FloatField(db_column='fAnalysisVal68', blank=True, null=True)  # Field name made lowercase.
    fanalysisval78 = models.FloatField(db_column='fAnalysisVal78', blank=True, null=True)  # Field name made lowercase.
    fanalysisval88 = models.FloatField(db_column='fAnalysisVal88', blank=True, null=True)  # Field name made lowercase.
    fanalysisval98 = models.FloatField(db_column='fAnalysisVal98', blank=True, null=True)  # Field name made lowercase.
    fanalysisval108 = models.FloatField(db_column='fAnalysisVal108', blank=True, null=True)  # Field name made lowercase.
    fanalysisval19 = models.FloatField(db_column='fAnalysisVal19', blank=True, null=True)  # Field name made lowercase.
    fanalysisval29 = models.FloatField(db_column='fAnalysisVal29', blank=True, null=True)  # Field name made lowercase.
    fanalysisval39 = models.FloatField(db_column='fAnalysisVal39', blank=True, null=True)  # Field name made lowercase.
    fanalysisval49 = models.FloatField(db_column='fAnalysisVal49', blank=True, null=True)  # Field name made lowercase.
    fanalysisval59 = models.FloatField(db_column='fAnalysisVal59', blank=True, null=True)  # Field name made lowercase.
    fanalysisval69 = models.FloatField(db_column='fAnalysisVal69', blank=True, null=True)  # Field name made lowercase.
    fanalysisval79 = models.FloatField(db_column='fAnalysisVal79', blank=True, null=True)  # Field name made lowercase.
    fanalysisval89 = models.FloatField(db_column='fAnalysisVal89', blank=True, null=True)  # Field name made lowercase.
    fanalysisval99 = models.FloatField(db_column='fAnalysisVal99', blank=True, null=True)  # Field name made lowercase.
    fanalysisval109 = models.FloatField(db_column='fAnalysisVal109', blank=True, null=True)  # Field name made lowercase.
    fanalysisval110 = models.FloatField(db_column='fAnalysisVal110', blank=True, null=True)  # Field name made lowercase.
    fanalysisval210 = models.FloatField(db_column='fAnalysisVal210', blank=True, null=True)  # Field name made lowercase.
    fanalysisval310 = models.FloatField(db_column='fAnalysisVal310', blank=True, null=True)  # Field name made lowercase.
    fanalysisval410 = models.FloatField(db_column='fAnalysisVal410', blank=True, null=True)  # Field name made lowercase.
    fanalysisval510 = models.FloatField(db_column='fAnalysisVal510', blank=True, null=True)  # Field name made lowercase.
    fanalysisval610 = models.FloatField(db_column='fAnalysisVal610', blank=True, null=True)  # Field name made lowercase.
    fanalysisval710 = models.FloatField(db_column='fAnalysisVal710', blank=True, null=True)  # Field name made lowercase.
    fanalysisval810 = models.FloatField(db_column='fAnalysisVal810', blank=True, null=True)  # Field name made lowercase.
    fanalysisval910 = models.FloatField(db_column='fAnalysisVal910', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1010 = models.FloatField(db_column='fAnalysisVal1010', blank=True, null=True)  # Field name made lowercase.
    fanalysisval111 = models.FloatField(db_column='fAnalysisVal111', blank=True, null=True)  # Field name made lowercase.
    fanalysisval211 = models.FloatField(db_column='fAnalysisVal211', blank=True, null=True)  # Field name made lowercase.
    fanalysisval311 = models.FloatField(db_column='fAnalysisVal311', blank=True, null=True)  # Field name made lowercase.
    fanalysisval411 = models.FloatField(db_column='fAnalysisVal411', blank=True, null=True)  # Field name made lowercase.
    fanalysisval511 = models.FloatField(db_column='fAnalysisVal511', blank=True, null=True)  # Field name made lowercase.
    fanalysisval611 = models.FloatField(db_column='fAnalysisVal611', blank=True, null=True)  # Field name made lowercase.
    fanalysisval711 = models.FloatField(db_column='fAnalysisVal711', blank=True, null=True)  # Field name made lowercase.
    fanalysisval811 = models.FloatField(db_column='fAnalysisVal811', blank=True, null=True)  # Field name made lowercase.
    fanalysisval911 = models.FloatField(db_column='fAnalysisVal911', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1011 = models.FloatField(db_column='fAnalysisVal1011', blank=True, null=True)  # Field name made lowercase.
    fanalysisval112 = models.FloatField(db_column='fAnalysisVal112', blank=True, null=True)  # Field name made lowercase.
    fanalysisval212 = models.FloatField(db_column='fAnalysisVal212', blank=True, null=True)  # Field name made lowercase.
    fanalysisval312 = models.FloatField(db_column='fAnalysisVal312', blank=True, null=True)  # Field name made lowercase.
    fanalysisval412 = models.FloatField(db_column='fAnalysisVal412', blank=True, null=True)  # Field name made lowercase.
    fanalysisval512 = models.FloatField(db_column='fAnalysisVal512', blank=True, null=True)  # Field name made lowercase.
    fanalysisval612 = models.FloatField(db_column='fAnalysisVal612', blank=True, null=True)  # Field name made lowercase.
    fanalysisval712 = models.FloatField(db_column='fAnalysisVal712', blank=True, null=True)  # Field name made lowercase.
    fanalysisval812 = models.FloatField(db_column='fAnalysisVal812', blank=True, null=True)  # Field name made lowercase.
    fanalysisval912 = models.FloatField(db_column='fAnalysisVal912', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1012 = models.FloatField(db_column='fAnalysisVal1012', blank=True, null=True)  # Field name made lowercase.
    fanalysisval113 = models.FloatField(db_column='fAnalysisVal113', blank=True, null=True)  # Field name made lowercase.
    fanalysisval213 = models.FloatField(db_column='fAnalysisVal213', blank=True, null=True)  # Field name made lowercase.
    fanalysisval313 = models.FloatField(db_column='fAnalysisVal313', blank=True, null=True)  # Field name made lowercase.
    fanalysisval413 = models.FloatField(db_column='fAnalysisVal413', blank=True, null=True)  # Field name made lowercase.
    fanalysisval513 = models.FloatField(db_column='fAnalysisVal513', blank=True, null=True)  # Field name made lowercase.
    fanalysisval613 = models.FloatField(db_column='fAnalysisVal613', blank=True, null=True)  # Field name made lowercase.
    fanalysisval713 = models.FloatField(db_column='fAnalysisVal713', blank=True, null=True)  # Field name made lowercase.
    fanalysisval813 = models.FloatField(db_column='fAnalysisVal813', blank=True, null=True)  # Field name made lowercase.
    fanalysisval913 = models.FloatField(db_column='fAnalysisVal913', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1013 = models.FloatField(db_column='fAnalysisVal1013', blank=True, null=True)  # Field name made lowercase.
    fanalysisval114 = models.FloatField(db_column='fAnalysisVal114', blank=True, null=True)  # Field name made lowercase.
    fanalysisval214 = models.FloatField(db_column='fAnalysisVal214', blank=True, null=True)  # Field name made lowercase.
    fanalysisval314 = models.FloatField(db_column='fAnalysisVal314', blank=True, null=True)  # Field name made lowercase.
    fanalysisval414 = models.FloatField(db_column='fAnalysisVal414', blank=True, null=True)  # Field name made lowercase.
    fanalysisval514 = models.FloatField(db_column='fAnalysisVal514', blank=True, null=True)  # Field name made lowercase.
    fanalysisval614 = models.FloatField(db_column='fAnalysisVal614', blank=True, null=True)  # Field name made lowercase.
    fanalysisval714 = models.FloatField(db_column='fAnalysisVal714', blank=True, null=True)  # Field name made lowercase.
    fanalysisval814 = models.FloatField(db_column='fAnalysisVal814', blank=True, null=True)  # Field name made lowercase.
    fanalysisval914 = models.FloatField(db_column='fAnalysisVal914', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1014 = models.FloatField(db_column='fAnalysisVal1014', blank=True, null=True)  # Field name made lowercase.
    fanalysisval115 = models.FloatField(db_column='fAnalysisVal115', blank=True, null=True)  # Field name made lowercase.
    fanalysisval215 = models.FloatField(db_column='fAnalysisVal215', blank=True, null=True)  # Field name made lowercase.
    fanalysisval315 = models.FloatField(db_column='fAnalysisVal315', blank=True, null=True)  # Field name made lowercase.
    fanalysisval415 = models.FloatField(db_column='fAnalysisVal415', blank=True, null=True)  # Field name made lowercase.
    fanalysisval515 = models.FloatField(db_column='fAnalysisVal515', blank=True, null=True)  # Field name made lowercase.
    fanalysisval615 = models.FloatField(db_column='fAnalysisVal615', blank=True, null=True)  # Field name made lowercase.
    fanalysisval715 = models.FloatField(db_column='fAnalysisVal715', blank=True, null=True)  # Field name made lowercase.
    fanalysisval815 = models.FloatField(db_column='fAnalysisVal815', blank=True, null=True)  # Field name made lowercase.
    fanalysisval915 = models.FloatField(db_column='fAnalysisVal915', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1015 = models.FloatField(db_column='fAnalysisVal1015', blank=True, null=True)  # Field name made lowercase.
    srrdate = models.CharField(db_column='sRRDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate1 = models.CharField(db_column='sDueDate1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSALinearityAnalysis'


class Tmsalinearityoperator(models.Model):
    rroperatorid = models.BigAutoField(db_column='RROperatorID', primary_key=True)  # Field name made lowercase.
    lrrspecificatonid = models.BigIntegerField(db_column='lRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.BigIntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    serialno = models.BigIntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    soperatorname = models.CharField(db_column='sOperatorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue = models.FloatField(db_column='FOperatorValue', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue = models.FloatField(db_column='fOperatorRefValue', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.BigIntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    serialno1 = models.BigIntegerField(db_column='SerialNo1', blank=True, null=True)  # Field name made lowercase.
    soperatorname1 = models.CharField(db_column='sOperatorName1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue1 = models.FloatField(db_column='FOperatorValue1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue1 = models.FloatField(db_column='fOperatorRefValue1', blank=True, null=True)  # Field name made lowercase.
    operatorid2 = models.BigIntegerField(db_column='OperatorID2', blank=True, null=True)  # Field name made lowercase.
    serialno2 = models.BigIntegerField(db_column='SerialNo2', blank=True, null=True)  # Field name made lowercase.
    soperatorname2 = models.CharField(db_column='sOperatorName2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue2 = models.FloatField(db_column='FOperatorValue2', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue2 = models.FloatField(db_column='fOperatorRefValue2', blank=True, null=True)  # Field name made lowercase.
    operatorid3 = models.BigIntegerField(db_column='OperatorID3', blank=True, null=True)  # Field name made lowercase.
    serialno3 = models.BigIntegerField(db_column='SerialNo3', blank=True, null=True)  # Field name made lowercase.
    soperatorname3 = models.CharField(db_column='sOperatorName3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue3 = models.FloatField(db_column='FOperatorValue3', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue3 = models.FloatField(db_column='fOperatorRefValue3', blank=True, null=True)  # Field name made lowercase.
    operatorid4 = models.BigIntegerField(db_column='OperatorID4', blank=True, null=True)  # Field name made lowercase.
    serialno4 = models.BigIntegerField(db_column='SerialNo4', blank=True, null=True)  # Field name made lowercase.
    soperatorname4 = models.CharField(db_column='sOperatorName4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue4 = models.FloatField(db_column='FOperatorValue4', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue4 = models.FloatField(db_column='fOperatorRefValue4', blank=True, null=True)  # Field name made lowercase.
    operatorid5 = models.BigIntegerField(db_column='OperatorID5', blank=True, null=True)  # Field name made lowercase.
    serialno5 = models.BigIntegerField(db_column='SerialNo5', blank=True, null=True)  # Field name made lowercase.
    soperatorname5 = models.CharField(db_column='sOperatorName5', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue5 = models.FloatField(db_column='FOperatorValue5', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue5 = models.FloatField(db_column='fOperatorRefValue5', blank=True, null=True)  # Field name made lowercase.
    operatorid11 = models.BigIntegerField(db_column='OperatorID11', blank=True, null=True)  # Field name made lowercase.
    serialno11 = models.BigIntegerField(db_column='SerialNo11', blank=True, null=True)  # Field name made lowercase.
    soperatorname11 = models.CharField(db_column='sOperatorName11', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue11 = models.FloatField(db_column='FOperatorValue11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue11 = models.FloatField(db_column='fOperatorRefValue11', blank=True, null=True)  # Field name made lowercase.
    operatorid21 = models.BigIntegerField(db_column='OperatorID21', blank=True, null=True)  # Field name made lowercase.
    serialno21 = models.BigIntegerField(db_column='SerialNo21', blank=True, null=True)  # Field name made lowercase.
    soperatorname21 = models.CharField(db_column='sOperatorName21', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue21 = models.FloatField(db_column='FOperatorValue21', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue21 = models.FloatField(db_column='fOperatorRefValue21', blank=True, null=True)  # Field name made lowercase.
    operatorid31 = models.BigIntegerField(db_column='OperatorID31', blank=True, null=True)  # Field name made lowercase.
    serialno31 = models.BigIntegerField(db_column='SerialNo31', blank=True, null=True)  # Field name made lowercase.
    soperatorname31 = models.CharField(db_column='sOperatorName31', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue31 = models.FloatField(db_column='FOperatorValue31', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue31 = models.FloatField(db_column='fOperatorRefValue31', blank=True, null=True)  # Field name made lowercase.
    operatorid41 = models.BigIntegerField(db_column='OperatorID41', blank=True, null=True)  # Field name made lowercase.
    serialno41 = models.BigIntegerField(db_column='SerialNo41', blank=True, null=True)  # Field name made lowercase.
    soperatorname41 = models.CharField(db_column='sOperatorName41', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue41 = models.FloatField(db_column='FOperatorValue41', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue41 = models.FloatField(db_column='fOperatorRefValue41', blank=True, null=True)  # Field name made lowercase.
    operatorid51 = models.BigIntegerField(db_column='OperatorID51', blank=True, null=True)  # Field name made lowercase.
    serialno51 = models.BigIntegerField(db_column='SerialNo51', blank=True, null=True)  # Field name made lowercase.
    soperatorname51 = models.CharField(db_column='sOperatorName51', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue51 = models.FloatField(db_column='FOperatorValue51', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue51 = models.FloatField(db_column='fOperatorRefValue51', blank=True, null=True)  # Field name made lowercase.
    operatorid12 = models.BigIntegerField(db_column='OperatorID12', blank=True, null=True)  # Field name made lowercase.
    serialno12 = models.BigIntegerField(db_column='SerialNo12', blank=True, null=True)  # Field name made lowercase.
    soperatorname12 = models.CharField(db_column='sOperatorName12', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue12 = models.FloatField(db_column='FOperatorValue12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue12 = models.FloatField(db_column='fOperatorRefValue12', blank=True, null=True)  # Field name made lowercase.
    operatorid22 = models.BigIntegerField(db_column='OperatorID22', blank=True, null=True)  # Field name made lowercase.
    serialno22 = models.BigIntegerField(db_column='SerialNo22', blank=True, null=True)  # Field name made lowercase.
    soperatorname22 = models.CharField(db_column='sOperatorName22', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue22 = models.FloatField(db_column='FOperatorValue22', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue22 = models.FloatField(db_column='fOperatorRefValue22', blank=True, null=True)  # Field name made lowercase.
    operatorid32 = models.BigIntegerField(db_column='OperatorID32', blank=True, null=True)  # Field name made lowercase.
    serialno32 = models.BigIntegerField(db_column='SerialNo32', blank=True, null=True)  # Field name made lowercase.
    soperatorname32 = models.CharField(db_column='sOperatorName32', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue32 = models.FloatField(db_column='FOperatorValue32', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue32 = models.FloatField(db_column='fOperatorRefValue32', blank=True, null=True)  # Field name made lowercase.
    operatorid42 = models.BigIntegerField(db_column='OperatorID42', blank=True, null=True)  # Field name made lowercase.
    serialno42 = models.BigIntegerField(db_column='SerialNo42', blank=True, null=True)  # Field name made lowercase.
    soperatorname42 = models.CharField(db_column='sOperatorName42', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue42 = models.FloatField(db_column='FOperatorValue42', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue42 = models.FloatField(db_column='fOperatorRefValue42', blank=True, null=True)  # Field name made lowercase.
    operatorid52 = models.BigIntegerField(db_column='OperatorID52', blank=True, null=True)  # Field name made lowercase.
    serialno52 = models.BigIntegerField(db_column='SerialNo52', blank=True, null=True)  # Field name made lowercase.
    soperatorname52 = models.CharField(db_column='sOperatorName52', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue52 = models.FloatField(db_column='FOperatorValue52', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue52 = models.FloatField(db_column='fOperatorRefValue52', blank=True, null=True)  # Field name made lowercase.
    operatorid13 = models.BigIntegerField(db_column='OperatorID13', blank=True, null=True)  # Field name made lowercase.
    serialno13 = models.BigIntegerField(db_column='SerialNo13', blank=True, null=True)  # Field name made lowercase.
    soperatorname13 = models.CharField(db_column='sOperatorName13', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue13 = models.FloatField(db_column='FOperatorValue13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue13 = models.FloatField(db_column='fOperatorRefValue13', blank=True, null=True)  # Field name made lowercase.
    operatorid23 = models.BigIntegerField(db_column='OperatorID23', blank=True, null=True)  # Field name made lowercase.
    serialno23 = models.BigIntegerField(db_column='SerialNo23', blank=True, null=True)  # Field name made lowercase.
    soperatorname23 = models.CharField(db_column='sOperatorName23', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue23 = models.FloatField(db_column='FOperatorValue23', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue23 = models.FloatField(db_column='fOperatorRefValue23', blank=True, null=True)  # Field name made lowercase.
    operatorid33 = models.BigIntegerField(db_column='OperatorID33', blank=True, null=True)  # Field name made lowercase.
    serialno33 = models.BigIntegerField(db_column='SerialNo33', blank=True, null=True)  # Field name made lowercase.
    soperatorname33 = models.CharField(db_column='sOperatorName33', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue33 = models.FloatField(db_column='FOperatorValue33', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue33 = models.FloatField(db_column='fOperatorRefValue33', blank=True, null=True)  # Field name made lowercase.
    operatorid43 = models.BigIntegerField(db_column='OperatorID43', blank=True, null=True)  # Field name made lowercase.
    serialno43 = models.BigIntegerField(db_column='SerialNo43', blank=True, null=True)  # Field name made lowercase.
    soperatorname43 = models.CharField(db_column='sOperatorName43', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue43 = models.FloatField(db_column='FOperatorValue43', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue43 = models.FloatField(db_column='fOperatorRefValue43', blank=True, null=True)  # Field name made lowercase.
    operatorid53 = models.BigIntegerField(db_column='OperatorID53', blank=True, null=True)  # Field name made lowercase.
    serialno53 = models.BigIntegerField(db_column='SerialNo53', blank=True, null=True)  # Field name made lowercase.
    soperatorname53 = models.CharField(db_column='sOperatorName53', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue53 = models.FloatField(db_column='FOperatorValue53', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue53 = models.FloatField(db_column='fOperatorRefValue53', blank=True, null=True)  # Field name made lowercase.
    operatorid14 = models.BigIntegerField(db_column='OperatorID14', blank=True, null=True)  # Field name made lowercase.
    serialno14 = models.BigIntegerField(db_column='SerialNo14', blank=True, null=True)  # Field name made lowercase.
    soperatorname14 = models.CharField(db_column='sOperatorName14', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue14 = models.FloatField(db_column='FOperatorValue14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue14 = models.FloatField(db_column='fOperatorRefValue14', blank=True, null=True)  # Field name made lowercase.
    operatorid24 = models.BigIntegerField(db_column='OperatorID24', blank=True, null=True)  # Field name made lowercase.
    serialno24 = models.BigIntegerField(db_column='SerialNo24', blank=True, null=True)  # Field name made lowercase.
    soperatorname24 = models.CharField(db_column='sOperatorName24', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue24 = models.FloatField(db_column='FOperatorValue24', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue24 = models.FloatField(db_column='fOperatorRefValue24', blank=True, null=True)  # Field name made lowercase.
    operatorid34 = models.BigIntegerField(db_column='OperatorID34', blank=True, null=True)  # Field name made lowercase.
    serialno34 = models.BigIntegerField(db_column='SerialNo34', blank=True, null=True)  # Field name made lowercase.
    soperatorname34 = models.CharField(db_column='sOperatorName34', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue34 = models.FloatField(db_column='FOperatorValue34', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue34 = models.FloatField(db_column='fOperatorRefValue34', blank=True, null=True)  # Field name made lowercase.
    operatorid44 = models.BigIntegerField(db_column='OperatorID44', blank=True, null=True)  # Field name made lowercase.
    serialno44 = models.BigIntegerField(db_column='SerialNo44', blank=True, null=True)  # Field name made lowercase.
    soperatorname44 = models.CharField(db_column='sOperatorName44', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue44 = models.FloatField(db_column='FOperatorValue44', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue44 = models.FloatField(db_column='fOperatorRefValue44', blank=True, null=True)  # Field name made lowercase.
    operatorid54 = models.BigIntegerField(db_column='OperatorID54', blank=True, null=True)  # Field name made lowercase.
    serialno54 = models.BigIntegerField(db_column='SerialNo54', blank=True, null=True)  # Field name made lowercase.
    soperatorname54 = models.CharField(db_column='sOperatorName54', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue54 = models.FloatField(db_column='FOperatorValue54', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue54 = models.FloatField(db_column='fOperatorRefValue54', blank=True, null=True)  # Field name made lowercase.
    operatorid15 = models.BigIntegerField(db_column='OperatorID15', blank=True, null=True)  # Field name made lowercase.
    serialno15 = models.BigIntegerField(db_column='SerialNo15', blank=True, null=True)  # Field name made lowercase.
    soperatorname15 = models.CharField(db_column='sOperatorName15', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue15 = models.FloatField(db_column='FOperatorValue15', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue15 = models.FloatField(db_column='fOperatorRefValue15', blank=True, null=True)  # Field name made lowercase.
    operatorid25 = models.BigIntegerField(db_column='OperatorID25', blank=True, null=True)  # Field name made lowercase.
    serialno25 = models.BigIntegerField(db_column='SerialNo25', blank=True, null=True)  # Field name made lowercase.
    soperatorname25 = models.CharField(db_column='sOperatorName25', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue25 = models.FloatField(db_column='FOperatorValue25', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue25 = models.FloatField(db_column='fOperatorRefValue25', blank=True, null=True)  # Field name made lowercase.
    operatorid35 = models.BigIntegerField(db_column='OperatorID35', blank=True, null=True)  # Field name made lowercase.
    serialno35 = models.BigIntegerField(db_column='SerialNo35', blank=True, null=True)  # Field name made lowercase.
    soperatorname35 = models.CharField(db_column='sOperatorName35', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue35 = models.FloatField(db_column='FOperatorValue35', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue35 = models.FloatField(db_column='fOperatorRefValue35', blank=True, null=True)  # Field name made lowercase.
    operatorid45 = models.BigIntegerField(db_column='OperatorID45', blank=True, null=True)  # Field name made lowercase.
    serialno45 = models.BigIntegerField(db_column='SerialNo45', blank=True, null=True)  # Field name made lowercase.
    soperatorname45 = models.CharField(db_column='sOperatorName45', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue45 = models.FloatField(db_column='FOperatorValue45', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue45 = models.FloatField(db_column='fOperatorRefValue45', blank=True, null=True)  # Field name made lowercase.
    operatorid55 = models.BigIntegerField(db_column='OperatorID55', blank=True, null=True)  # Field name made lowercase.
    serialno55 = models.BigIntegerField(db_column='SerialNo55', blank=True, null=True)  # Field name made lowercase.
    soperatorname55 = models.CharField(db_column='sOperatorName55', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue55 = models.FloatField(db_column='FOperatorValue55', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue55 = models.FloatField(db_column='fOperatorRefValue55', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSALinearityOperator'


class Tmsarnranalysis(models.Model):
    lrrspecificatonid = models.BigAutoField(db_column='lRRSpecificatonID', primary_key=True)  # Field name made lowercase.
    rrdate = models.DateTimeField(db_column='RRDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=350, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.FloatField(db_column='Tolerance', blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductID', blank=True, null=True)  # Field name made lowercase.
    lparts = models.BigIntegerField(db_column='lParts', blank=True, null=True)  # Field name made lowercase.
    ltrials = models.BigIntegerField(db_column='lTrials', blank=True, null=True)  # Field name made lowercase.
    loperators = models.BigIntegerField(db_column='lOperators', blank=True, null=True)  # Field name made lowercase.
    specialcharacter = models.CharField(db_column='SpecialCharacter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    considertolerance = models.CharField(db_column='ConsiderTolerance', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcreatetable = models.BooleanField(db_column='bCreateTable', blank=True, null=True)  # Field name made lowercase.
    previouslrrspecificatonid = models.BigIntegerField(db_column='PreviouslRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    reconduct = models.BooleanField(db_column='ReConduct', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    timetaken = models.CharField(db_column='TimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    calibratedby = models.CharField(db_column='CalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    xbarbar = models.FloatField(db_column='XBARBar', blank=True, null=True)  # Field name made lowercase.
    rbar = models.FloatField(db_column='RBar', blank=True, null=True)  # Field name made lowercase.
    uclxbar = models.FloatField(db_column='UCLXBar', blank=True, null=True)  # Field name made lowercase.
    lclxbar = models.FloatField(db_column='LCLXBar', blank=True, null=True)  # Field name made lowercase.
    uclrange = models.FloatField(db_column='UCLRange', blank=True, null=True)  # Field name made lowercase.
    lclrange = models.FloatField(db_column='LCLRange', blank=True, null=True)  # Field name made lowercase.
    dbias = models.FloatField(db_column='dBias', blank=True, null=True)  # Field name made lowercase.
    dsigmarepr = models.FloatField(db_column='dSigmaRepr', blank=True, null=True)  # Field name made lowercase.
    dsigmabias = models.FloatField(db_column='dSigmaBias', blank=True, null=True)  # Field name made lowercase.
    tbias = models.FloatField(db_column='tBias', blank=True, null=True)  # Field name made lowercase.
    tcritical = models.FloatField(db_column='tCritical', blank=True, null=True)  # Field name made lowercase.
    biasstatus = models.FloatField(db_column='BiasStatus', blank=True, null=True)  # Field name made lowercase.
    biasvalue = models.FloatField(db_column='BiasValue', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    bcategory = models.BooleanField(db_column='bCategory', blank=True, null=True)  # Field name made lowercase.
    categoryhistorymsaid = models.BigIntegerField(db_column='CategoryHistoryMSAID', blank=True, null=True)  # Field name made lowercase.
    lcategoryscheduleid = models.BigIntegerField(db_column='lCategoryScheduleID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fanalysisval = models.FloatField(db_column='fAnalysisVal', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1 = models.FloatField(db_column='fAnalysisVal1', blank=True, null=True)  # Field name made lowercase.
    fanalysisval2 = models.FloatField(db_column='fAnalysisVal2', blank=True, null=True)  # Field name made lowercase.
    fanalysisval3 = models.FloatField(db_column='fAnalysisVal3', blank=True, null=True)  # Field name made lowercase.
    fanalysisval4 = models.FloatField(db_column='fAnalysisVal4', blank=True, null=True)  # Field name made lowercase.
    fanalysisval5 = models.FloatField(db_column='fAnalysisVal5', blank=True, null=True)  # Field name made lowercase.
    fanalysisval6 = models.FloatField(db_column='fAnalysisVal6', blank=True, null=True)  # Field name made lowercase.
    fanalysisval7 = models.FloatField(db_column='fAnalysisVal7', blank=True, null=True)  # Field name made lowercase.
    fanalysisval8 = models.FloatField(db_column='fAnalysisVal8', blank=True, null=True)  # Field name made lowercase.
    fanalysisval9 = models.FloatField(db_column='fAnalysisVal9', blank=True, null=True)  # Field name made lowercase.
    fanalysisval10 = models.FloatField(db_column='fAnalysisVal10', blank=True, null=True)  # Field name made lowercase.
    fanalysisval11 = models.FloatField(db_column='fAnalysisVal11', blank=True, null=True)  # Field name made lowercase.
    fanalysisval21 = models.FloatField(db_column='fAnalysisVal21', blank=True, null=True)  # Field name made lowercase.
    fanalysisval31 = models.FloatField(db_column='fAnalysisVal31', blank=True, null=True)  # Field name made lowercase.
    fanalysisval41 = models.FloatField(db_column='fAnalysisVal41', blank=True, null=True)  # Field name made lowercase.
    fanalysisval51 = models.FloatField(db_column='fAnalysisVal51', blank=True, null=True)  # Field name made lowercase.
    fanalysisval61 = models.FloatField(db_column='fAnalysisVal61', blank=True, null=True)  # Field name made lowercase.
    fanalysisval71 = models.FloatField(db_column='fAnalysisVal71', blank=True, null=True)  # Field name made lowercase.
    fanalysisval81 = models.FloatField(db_column='fAnalysisVal81', blank=True, null=True)  # Field name made lowercase.
    fanalysisval91 = models.FloatField(db_column='fAnalysisVal91', blank=True, null=True)  # Field name made lowercase.
    fanalysisval101 = models.FloatField(db_column='fAnalysisVal101', blank=True, null=True)  # Field name made lowercase.
    fanalysisval12 = models.FloatField(db_column='fAnalysisVal12', blank=True, null=True)  # Field name made lowercase.
    fanalysisval22 = models.FloatField(db_column='fAnalysisVal22', blank=True, null=True)  # Field name made lowercase.
    fanalysisval32 = models.FloatField(db_column='fAnalysisVal32', blank=True, null=True)  # Field name made lowercase.
    fanalysisval42 = models.FloatField(db_column='fAnalysisVal42', blank=True, null=True)  # Field name made lowercase.
    fanalysisval52 = models.FloatField(db_column='fAnalysisVal52', blank=True, null=True)  # Field name made lowercase.
    fanalysisval62 = models.FloatField(db_column='fAnalysisVal62', blank=True, null=True)  # Field name made lowercase.
    fanalysisval72 = models.FloatField(db_column='fAnalysisVal72', blank=True, null=True)  # Field name made lowercase.
    fanalysisval82 = models.FloatField(db_column='fAnalysisVal82', blank=True, null=True)  # Field name made lowercase.
    fanalysisval92 = models.FloatField(db_column='fAnalysisVal92', blank=True, null=True)  # Field name made lowercase.
    fanalysisval102 = models.FloatField(db_column='fAnalysisVal102', blank=True, null=True)  # Field name made lowercase.
    fanalysisval13 = models.FloatField(db_column='fAnalysisVal13', blank=True, null=True)  # Field name made lowercase.
    fanalysisval23 = models.FloatField(db_column='fAnalysisVal23', blank=True, null=True)  # Field name made lowercase.
    fanalysisval33 = models.FloatField(db_column='fAnalysisVal33', blank=True, null=True)  # Field name made lowercase.
    fanalysisval43 = models.FloatField(db_column='fAnalysisVal43', blank=True, null=True)  # Field name made lowercase.
    fanalysisval53 = models.FloatField(db_column='fAnalysisVal53', blank=True, null=True)  # Field name made lowercase.
    fanalysisval63 = models.FloatField(db_column='fAnalysisVal63', blank=True, null=True)  # Field name made lowercase.
    fanalysisval73 = models.FloatField(db_column='fAnalysisVal73', blank=True, null=True)  # Field name made lowercase.
    fanalysisval83 = models.FloatField(db_column='fAnalysisVal83', blank=True, null=True)  # Field name made lowercase.
    fanalysisval93 = models.FloatField(db_column='fAnalysisVal93', blank=True, null=True)  # Field name made lowercase.
    fanalysisval103 = models.FloatField(db_column='fAnalysisVal103', blank=True, null=True)  # Field name made lowercase.
    fanalysisval14 = models.FloatField(db_column='fAnalysisVal14', blank=True, null=True)  # Field name made lowercase.
    fanalysisval24 = models.FloatField(db_column='fAnalysisVal24', blank=True, null=True)  # Field name made lowercase.
    fanalysisval34 = models.FloatField(db_column='fAnalysisVal34', blank=True, null=True)  # Field name made lowercase.
    fanalysisval44 = models.FloatField(db_column='fAnalysisVal44', blank=True, null=True)  # Field name made lowercase.
    fanalysisval54 = models.FloatField(db_column='fAnalysisVal54', blank=True, null=True)  # Field name made lowercase.
    fanalysisval64 = models.FloatField(db_column='fAnalysisVal64', blank=True, null=True)  # Field name made lowercase.
    fanalysisval74 = models.FloatField(db_column='fAnalysisVal74', blank=True, null=True)  # Field name made lowercase.
    fanalysisval84 = models.FloatField(db_column='fAnalysisVal84', blank=True, null=True)  # Field name made lowercase.
    fanalysisval94 = models.FloatField(db_column='fAnalysisVal94', blank=True, null=True)  # Field name made lowercase.
    fanalysisval104 = models.FloatField(db_column='fAnalysisVal104', blank=True, null=True)  # Field name made lowercase.
    fanalysisval15 = models.FloatField(db_column='fAnalysisVal15', blank=True, null=True)  # Field name made lowercase.
    fanalysisval25 = models.FloatField(db_column='fAnalysisVal25', blank=True, null=True)  # Field name made lowercase.
    fanalysisval35 = models.FloatField(db_column='fAnalysisVal35', blank=True, null=True)  # Field name made lowercase.
    fanalysisval45 = models.FloatField(db_column='fAnalysisVal45', blank=True, null=True)  # Field name made lowercase.
    fanalysisval55 = models.FloatField(db_column='fAnalysisVal55', blank=True, null=True)  # Field name made lowercase.
    fanalysisval65 = models.FloatField(db_column='fAnalysisVal65', blank=True, null=True)  # Field name made lowercase.
    fanalysisval75 = models.FloatField(db_column='fAnalysisVal75', blank=True, null=True)  # Field name made lowercase.
    fanalysisval85 = models.FloatField(db_column='fAnalysisVal85', blank=True, null=True)  # Field name made lowercase.
    fanalysisval95 = models.FloatField(db_column='fAnalysisVal95', blank=True, null=True)  # Field name made lowercase.
    fanalysisval105 = models.FloatField(db_column='fAnalysisVal105', blank=True, null=True)  # Field name made lowercase.
    fanalysisval16 = models.FloatField(db_column='fAnalysisVal16', blank=True, null=True)  # Field name made lowercase.
    fanalysisval26 = models.FloatField(db_column='fAnalysisVal26', blank=True, null=True)  # Field name made lowercase.
    fanalysisval36 = models.FloatField(db_column='fAnalysisVal36', blank=True, null=True)  # Field name made lowercase.
    fanalysisval46 = models.FloatField(db_column='fAnalysisVal46', blank=True, null=True)  # Field name made lowercase.
    fanalysisval56 = models.FloatField(db_column='fAnalysisVal56', blank=True, null=True)  # Field name made lowercase.
    fanalysisval66 = models.FloatField(db_column='fAnalysisVal66', blank=True, null=True)  # Field name made lowercase.
    fanalysisval76 = models.FloatField(db_column='fAnalysisVal76', blank=True, null=True)  # Field name made lowercase.
    fanalysisval86 = models.FloatField(db_column='fAnalysisVal86', blank=True, null=True)  # Field name made lowercase.
    fanalysisval96 = models.FloatField(db_column='fAnalysisVal96', blank=True, null=True)  # Field name made lowercase.
    fanalysisval106 = models.FloatField(db_column='fAnalysisVal106', blank=True, null=True)  # Field name made lowercase.
    fanalysisval17 = models.FloatField(db_column='fAnalysisVal17', blank=True, null=True)  # Field name made lowercase.
    fanalysisval27 = models.FloatField(db_column='fAnalysisVal27', blank=True, null=True)  # Field name made lowercase.
    fanalysisval37 = models.FloatField(db_column='fAnalysisVal37', blank=True, null=True)  # Field name made lowercase.
    fanalysisval47 = models.FloatField(db_column='fAnalysisVal47', blank=True, null=True)  # Field name made lowercase.
    fanalysisval57 = models.FloatField(db_column='fAnalysisVal57', blank=True, null=True)  # Field name made lowercase.
    fanalysisval67 = models.FloatField(db_column='fAnalysisVal67', blank=True, null=True)  # Field name made lowercase.
    fanalysisval77 = models.FloatField(db_column='fAnalysisVal77', blank=True, null=True)  # Field name made lowercase.
    fanalysisval87 = models.FloatField(db_column='fAnalysisVal87', blank=True, null=True)  # Field name made lowercase.
    fanalysisval97 = models.FloatField(db_column='fAnalysisVal97', blank=True, null=True)  # Field name made lowercase.
    fanalysisval107 = models.FloatField(db_column='fAnalysisVal107', blank=True, null=True)  # Field name made lowercase.
    fanalysisval18 = models.FloatField(db_column='fAnalysisVal18', blank=True, null=True)  # Field name made lowercase.
    fanalysisval28 = models.FloatField(db_column='fAnalysisVal28', blank=True, null=True)  # Field name made lowercase.
    fanalysisval38 = models.FloatField(db_column='fAnalysisVal38', blank=True, null=True)  # Field name made lowercase.
    fanalysisval48 = models.FloatField(db_column='fAnalysisVal48', blank=True, null=True)  # Field name made lowercase.
    fanalysisval58 = models.FloatField(db_column='fAnalysisVal58', blank=True, null=True)  # Field name made lowercase.
    fanalysisval68 = models.FloatField(db_column='fAnalysisVal68', blank=True, null=True)  # Field name made lowercase.
    fanalysisval78 = models.FloatField(db_column='fAnalysisVal78', blank=True, null=True)  # Field name made lowercase.
    fanalysisval88 = models.FloatField(db_column='fAnalysisVal88', blank=True, null=True)  # Field name made lowercase.
    fanalysisval98 = models.FloatField(db_column='fAnalysisVal98', blank=True, null=True)  # Field name made lowercase.
    fanalysisval108 = models.FloatField(db_column='fAnalysisVal108', blank=True, null=True)  # Field name made lowercase.
    fanalysisval19 = models.FloatField(db_column='fAnalysisVal19', blank=True, null=True)  # Field name made lowercase.
    fanalysisval29 = models.FloatField(db_column='fAnalysisVal29', blank=True, null=True)  # Field name made lowercase.
    fanalysisval39 = models.FloatField(db_column='fAnalysisVal39', blank=True, null=True)  # Field name made lowercase.
    fanalysisval49 = models.FloatField(db_column='fAnalysisVal49', blank=True, null=True)  # Field name made lowercase.
    fanalysisval59 = models.FloatField(db_column='fAnalysisVal59', blank=True, null=True)  # Field name made lowercase.
    fanalysisval69 = models.FloatField(db_column='fAnalysisVal69', blank=True, null=True)  # Field name made lowercase.
    fanalysisval79 = models.FloatField(db_column='fAnalysisVal79', blank=True, null=True)  # Field name made lowercase.
    fanalysisval89 = models.FloatField(db_column='fAnalysisVal89', blank=True, null=True)  # Field name made lowercase.
    fanalysisval99 = models.FloatField(db_column='fAnalysisVal99', blank=True, null=True)  # Field name made lowercase.
    fanalysisval109 = models.FloatField(db_column='fAnalysisVal109', blank=True, null=True)  # Field name made lowercase.
    fanalysisval110 = models.FloatField(db_column='fAnalysisVal110', blank=True, null=True)  # Field name made lowercase.
    fanalysisval210 = models.FloatField(db_column='fAnalysisVal210', blank=True, null=True)  # Field name made lowercase.
    fanalysisval310 = models.FloatField(db_column='fAnalysisVal310', blank=True, null=True)  # Field name made lowercase.
    fanalysisval410 = models.FloatField(db_column='fAnalysisVal410', blank=True, null=True)  # Field name made lowercase.
    fanalysisval510 = models.FloatField(db_column='fAnalysisVal510', blank=True, null=True)  # Field name made lowercase.
    fanalysisval610 = models.FloatField(db_column='fAnalysisVal610', blank=True, null=True)  # Field name made lowercase.
    fanalysisval710 = models.FloatField(db_column='fAnalysisVal710', blank=True, null=True)  # Field name made lowercase.
    fanalysisval810 = models.FloatField(db_column='fAnalysisVal810', blank=True, null=True)  # Field name made lowercase.
    fanalysisval910 = models.FloatField(db_column='fAnalysisVal910', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1010 = models.FloatField(db_column='fAnalysisVal1010', blank=True, null=True)  # Field name made lowercase.
    fanalysisval111 = models.FloatField(db_column='fAnalysisVal111', blank=True, null=True)  # Field name made lowercase.
    fanalysisval211 = models.FloatField(db_column='fAnalysisVal211', blank=True, null=True)  # Field name made lowercase.
    fanalysisval311 = models.FloatField(db_column='fAnalysisVal311', blank=True, null=True)  # Field name made lowercase.
    fanalysisval411 = models.FloatField(db_column='fAnalysisVal411', blank=True, null=True)  # Field name made lowercase.
    fanalysisval511 = models.FloatField(db_column='fAnalysisVal511', blank=True, null=True)  # Field name made lowercase.
    fanalysisval611 = models.FloatField(db_column='fAnalysisVal611', blank=True, null=True)  # Field name made lowercase.
    fanalysisval711 = models.FloatField(db_column='fAnalysisVal711', blank=True, null=True)  # Field name made lowercase.
    fanalysisval811 = models.FloatField(db_column='fAnalysisVal811', blank=True, null=True)  # Field name made lowercase.
    fanalysisval911 = models.FloatField(db_column='fAnalysisVal911', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1011 = models.FloatField(db_column='fAnalysisVal1011', blank=True, null=True)  # Field name made lowercase.
    fanalysisval112 = models.FloatField(db_column='fAnalysisVal112', blank=True, null=True)  # Field name made lowercase.
    fanalysisval212 = models.FloatField(db_column='fAnalysisVal212', blank=True, null=True)  # Field name made lowercase.
    fanalysisval312 = models.FloatField(db_column='fAnalysisVal312', blank=True, null=True)  # Field name made lowercase.
    fanalysisval412 = models.FloatField(db_column='fAnalysisVal412', blank=True, null=True)  # Field name made lowercase.
    fanalysisval512 = models.FloatField(db_column='fAnalysisVal512', blank=True, null=True)  # Field name made lowercase.
    fanalysisval612 = models.FloatField(db_column='fAnalysisVal612', blank=True, null=True)  # Field name made lowercase.
    fanalysisval712 = models.FloatField(db_column='fAnalysisVal712', blank=True, null=True)  # Field name made lowercase.
    fanalysisval812 = models.FloatField(db_column='fAnalysisVal812', blank=True, null=True)  # Field name made lowercase.
    fanalysisval912 = models.FloatField(db_column='fAnalysisVal912', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1012 = models.FloatField(db_column='fAnalysisVal1012', blank=True, null=True)  # Field name made lowercase.
    fanalysisval113 = models.FloatField(db_column='fAnalysisVal113', blank=True, null=True)  # Field name made lowercase.
    fanalysisval213 = models.FloatField(db_column='fAnalysisVal213', blank=True, null=True)  # Field name made lowercase.
    fanalysisval313 = models.FloatField(db_column='fAnalysisVal313', blank=True, null=True)  # Field name made lowercase.
    fanalysisval413 = models.FloatField(db_column='fAnalysisVal413', blank=True, null=True)  # Field name made lowercase.
    fanalysisval513 = models.FloatField(db_column='fAnalysisVal513', blank=True, null=True)  # Field name made lowercase.
    fanalysisval613 = models.FloatField(db_column='fAnalysisVal613', blank=True, null=True)  # Field name made lowercase.
    fanalysisval713 = models.FloatField(db_column='fAnalysisVal713', blank=True, null=True)  # Field name made lowercase.
    fanalysisval813 = models.FloatField(db_column='fAnalysisVal813', blank=True, null=True)  # Field name made lowercase.
    fanalysisval913 = models.FloatField(db_column='fAnalysisVal913', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1013 = models.FloatField(db_column='fAnalysisVal1013', blank=True, null=True)  # Field name made lowercase.
    fanalysisval114 = models.FloatField(db_column='fAnalysisVal114', blank=True, null=True)  # Field name made lowercase.
    fanalysisval214 = models.FloatField(db_column='fAnalysisVal214', blank=True, null=True)  # Field name made lowercase.
    fanalysisval314 = models.FloatField(db_column='fAnalysisVal314', blank=True, null=True)  # Field name made lowercase.
    fanalysisval414 = models.FloatField(db_column='fAnalysisVal414', blank=True, null=True)  # Field name made lowercase.
    fanalysisval514 = models.FloatField(db_column='fAnalysisVal514', blank=True, null=True)  # Field name made lowercase.
    fanalysisval614 = models.FloatField(db_column='fAnalysisVal614', blank=True, null=True)  # Field name made lowercase.
    fanalysisval714 = models.FloatField(db_column='fAnalysisVal714', blank=True, null=True)  # Field name made lowercase.
    fanalysisval814 = models.FloatField(db_column='fAnalysisVal814', blank=True, null=True)  # Field name made lowercase.
    fanalysisval914 = models.FloatField(db_column='fAnalysisVal914', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1014 = models.FloatField(db_column='fAnalysisVal1014', blank=True, null=True)  # Field name made lowercase.
    fanalysisval115 = models.FloatField(db_column='fAnalysisVal115', blank=True, null=True)  # Field name made lowercase.
    fanalysisval215 = models.FloatField(db_column='fAnalysisVal215', blank=True, null=True)  # Field name made lowercase.
    fanalysisval315 = models.FloatField(db_column='fAnalysisVal315', blank=True, null=True)  # Field name made lowercase.
    fanalysisval415 = models.FloatField(db_column='fAnalysisVal415', blank=True, null=True)  # Field name made lowercase.
    fanalysisval515 = models.FloatField(db_column='fAnalysisVal515', blank=True, null=True)  # Field name made lowercase.
    fanalysisval615 = models.FloatField(db_column='fAnalysisVal615', blank=True, null=True)  # Field name made lowercase.
    fanalysisval715 = models.FloatField(db_column='fAnalysisVal715', blank=True, null=True)  # Field name made lowercase.
    fanalysisval815 = models.FloatField(db_column='fAnalysisVal815', blank=True, null=True)  # Field name made lowercase.
    fanalysisval915 = models.FloatField(db_column='fAnalysisVal915', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1015 = models.FloatField(db_column='fAnalysisVal1015', blank=True, null=True)  # Field name made lowercase.
    srrdate = models.CharField(db_column='sRRDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate1 = models.CharField(db_column='sDueDate1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSARnRAnalysis'


class Tmsarnroperator(models.Model):
    rroperatorid = models.BigAutoField(db_column='RROperatorID', primary_key=True)  # Field name made lowercase.
    lrrspecificatonid = models.BigIntegerField(db_column='lRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.BigIntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    serialno = models.BigIntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    soperatorname = models.CharField(db_column='sOperatorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue = models.FloatField(db_column='FOperatorValue', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue = models.FloatField(db_column='fOperatorRefValue', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.BigIntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    serialno1 = models.BigIntegerField(db_column='SerialNo1', blank=True, null=True)  # Field name made lowercase.
    soperatorname1 = models.CharField(db_column='sOperatorName1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue1 = models.FloatField(db_column='FOperatorValue1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea1 = models.FloatField(db_column='fOperatorRefValueA1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea2 = models.FloatField(db_column='fOperatorRefValueA2', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea3 = models.FloatField(db_column='fOperatorRefValueA3', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea4 = models.FloatField(db_column='fOperatorRefValueA4', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea5 = models.FloatField(db_column='fOperatorRefValueA5', blank=True, null=True)  # Field name made lowercase.
    operatorid11 = models.BigIntegerField(db_column='OperatorID11', blank=True, null=True)  # Field name made lowercase.
    serialno11 = models.BigIntegerField(db_column='SerialNo11', blank=True, null=True)  # Field name made lowercase.
    soperatorname11 = models.CharField(db_column='sOperatorName11', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue11 = models.FloatField(db_column='FOperatorValue11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea11 = models.FloatField(db_column='fOperatorRefValueA11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea21 = models.FloatField(db_column='fOperatorRefValueA21', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea31 = models.FloatField(db_column='fOperatorRefValueA31', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea41 = models.FloatField(db_column='fOperatorRefValueA41', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea51 = models.FloatField(db_column='fOperatorRefValueA51', blank=True, null=True)  # Field name made lowercase.
    operatorid12 = models.BigIntegerField(db_column='OperatorID12', blank=True, null=True)  # Field name made lowercase.
    serialno12 = models.BigIntegerField(db_column='SerialNo12', blank=True, null=True)  # Field name made lowercase.
    soperatorname12 = models.CharField(db_column='sOperatorName12', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue12 = models.FloatField(db_column='FOperatorValue12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea12 = models.FloatField(db_column='fOperatorRefValueA12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea22 = models.FloatField(db_column='fOperatorRefValueA22', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea32 = models.FloatField(db_column='fOperatorRefValueA32', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea42 = models.FloatField(db_column='fOperatorRefValueA42', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea52 = models.FloatField(db_column='fOperatorRefValueA52', blank=True, null=True)  # Field name made lowercase.
    operatorid13 = models.BigIntegerField(db_column='OperatorID13', blank=True, null=True)  # Field name made lowercase.
    serialno13 = models.BigIntegerField(db_column='SerialNo13', blank=True, null=True)  # Field name made lowercase.
    soperatorname13 = models.CharField(db_column='sOperatorName13', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue13 = models.FloatField(db_column='FOperatorValue13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea13 = models.FloatField(db_column='fOperatorRefValueA13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea23 = models.FloatField(db_column='fOperatorRefValueA23', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea33 = models.FloatField(db_column='fOperatorRefValueA33', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea43 = models.FloatField(db_column='fOperatorRefValueA43', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea53 = models.FloatField(db_column='fOperatorRefValueA53', blank=True, null=True)  # Field name made lowercase.
    operatorid14 = models.BigIntegerField(db_column='OperatorID14', blank=True, null=True)  # Field name made lowercase.
    serialno14 = models.BigIntegerField(db_column='SerialNo14', blank=True, null=True)  # Field name made lowercase.
    soperatorname14 = models.CharField(db_column='sOperatorName14', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue14 = models.FloatField(db_column='FOperatorValue14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea14 = models.FloatField(db_column='fOperatorRefValueA14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea24 = models.FloatField(db_column='fOperatorRefValueA24', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea34 = models.FloatField(db_column='fOperatorRefValueA34', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea44 = models.FloatField(db_column='fOperatorRefValueA44', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea54 = models.FloatField(db_column='fOperatorRefValueA54', blank=True, null=True)  # Field name made lowercase.
    operatorid111 = models.BigIntegerField(db_column='OperatorID111', blank=True, null=True)  # Field name made lowercase.
    serialno111 = models.BigIntegerField(db_column='SerialNo111', blank=True, null=True)  # Field name made lowercase.
    soperatorname111 = models.CharField(db_column='sOperatorName111', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue111 = models.FloatField(db_column='FOperatorValue111', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea111 = models.FloatField(db_column='fOperatorRefValueA111', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea211 = models.FloatField(db_column='fOperatorRefValueA211', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea311 = models.FloatField(db_column='fOperatorRefValueA311', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea411 = models.FloatField(db_column='fOperatorRefValueA411', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea511 = models.FloatField(db_column='fOperatorRefValueA511', blank=True, null=True)  # Field name made lowercase.
    operatorid121 = models.BigIntegerField(db_column='OperatorID121', blank=True, null=True)  # Field name made lowercase.
    serialno121 = models.BigIntegerField(db_column='SerialNo121', blank=True, null=True)  # Field name made lowercase.
    soperatorname121 = models.CharField(db_column='sOperatorName121', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue121 = models.FloatField(db_column='FOperatorValue121', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea121 = models.FloatField(db_column='fOperatorRefValueA121', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea221 = models.FloatField(db_column='fOperatorRefValueA221', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea321 = models.FloatField(db_column='fOperatorRefValueA321', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea421 = models.FloatField(db_column='fOperatorRefValueA421', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea521 = models.FloatField(db_column='fOperatorRefValueA521', blank=True, null=True)  # Field name made lowercase.
    operatorid131 = models.BigIntegerField(db_column='OperatorID131', blank=True, null=True)  # Field name made lowercase.
    serialno131 = models.BigIntegerField(db_column='SerialNo131', blank=True, null=True)  # Field name made lowercase.
    soperatorname131 = models.CharField(db_column='sOperatorName131', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue131 = models.FloatField(db_column='FOperatorValue131', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea131 = models.FloatField(db_column='fOperatorRefValueA131', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea231 = models.FloatField(db_column='fOperatorRefValueA231', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea331 = models.FloatField(db_column='fOperatorRefValueA331', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea431 = models.FloatField(db_column='fOperatorRefValueA431', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea531 = models.FloatField(db_column='fOperatorRefValueA531', blank=True, null=True)  # Field name made lowercase.
    operatorid141 = models.BigIntegerField(db_column='OperatorID141', blank=True, null=True)  # Field name made lowercase.
    serialno141 = models.BigIntegerField(db_column='SerialNo141', blank=True, null=True)  # Field name made lowercase.
    soperatorname141 = models.CharField(db_column='sOperatorName141', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue141 = models.FloatField(db_column='FOperatorValue141', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea141 = models.FloatField(db_column='fOperatorRefValueA141', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea241 = models.FloatField(db_column='fOperatorRefValueA241', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea341 = models.FloatField(db_column='fOperatorRefValueA341', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea441 = models.FloatField(db_column='fOperatorRefValueA441', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea541 = models.FloatField(db_column='fOperatorRefValueA541', blank=True, null=True)  # Field name made lowercase.
    operatorid112 = models.BigIntegerField(db_column='OperatorID112', blank=True, null=True)  # Field name made lowercase.
    serialno112 = models.BigIntegerField(db_column='SerialNo112', blank=True, null=True)  # Field name made lowercase.
    soperatorname112 = models.CharField(db_column='sOperatorName112', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue112 = models.FloatField(db_column='FOperatorValue112', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea112 = models.FloatField(db_column='fOperatorRefValueA112', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea212 = models.FloatField(db_column='fOperatorRefValueA212', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea312 = models.FloatField(db_column='fOperatorRefValueA312', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea412 = models.FloatField(db_column='fOperatorRefValueA412', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea512 = models.FloatField(db_column='fOperatorRefValueA512', blank=True, null=True)  # Field name made lowercase.
    operatorid122 = models.BigIntegerField(db_column='OperatorID122', blank=True, null=True)  # Field name made lowercase.
    serialno122 = models.BigIntegerField(db_column='SerialNo122', blank=True, null=True)  # Field name made lowercase.
    soperatorname122 = models.CharField(db_column='sOperatorName122', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue122 = models.FloatField(db_column='FOperatorValue122', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea122 = models.FloatField(db_column='fOperatorRefValueA122', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea222 = models.FloatField(db_column='fOperatorRefValueA222', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea322 = models.FloatField(db_column='fOperatorRefValueA322', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea422 = models.FloatField(db_column='fOperatorRefValueA422', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea522 = models.FloatField(db_column='fOperatorRefValueA522', blank=True, null=True)  # Field name made lowercase.
    operatorid132 = models.BigIntegerField(db_column='OperatorID132', blank=True, null=True)  # Field name made lowercase.
    serialno132 = models.BigIntegerField(db_column='SerialNo132', blank=True, null=True)  # Field name made lowercase.
    soperatorname132 = models.CharField(db_column='sOperatorName132', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue132 = models.FloatField(db_column='FOperatorValue132', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea132 = models.FloatField(db_column='fOperatorRefValueA132', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea232 = models.FloatField(db_column='fOperatorRefValueA232', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea332 = models.FloatField(db_column='fOperatorRefValueA332', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea432 = models.FloatField(db_column='fOperatorRefValueA432', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea532 = models.FloatField(db_column='fOperatorRefValueA532', blank=True, null=True)  # Field name made lowercase.
    operatorid142 = models.BigIntegerField(db_column='OperatorID142', blank=True, null=True)  # Field name made lowercase.
    serialno142 = models.BigIntegerField(db_column='SerialNo142', blank=True, null=True)  # Field name made lowercase.
    soperatorname142 = models.CharField(db_column='sOperatorName142', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue142 = models.FloatField(db_column='FOperatorValue142', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea142 = models.FloatField(db_column='fOperatorRefValueA142', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea242 = models.FloatField(db_column='fOperatorRefValueA242', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea342 = models.FloatField(db_column='fOperatorRefValueA342', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea442 = models.FloatField(db_column='fOperatorRefValueA442', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea542 = models.FloatField(db_column='fOperatorRefValueA542', blank=True, null=True)  # Field name made lowercase.
    operatorid113 = models.BigIntegerField(db_column='OperatorID113', blank=True, null=True)  # Field name made lowercase.
    serialno113 = models.BigIntegerField(db_column='SerialNo113', blank=True, null=True)  # Field name made lowercase.
    soperatorname113 = models.CharField(db_column='sOperatorName113', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue113 = models.FloatField(db_column='FOperatorValue113', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea113 = models.FloatField(db_column='fOperatorRefValueA113', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea213 = models.FloatField(db_column='fOperatorRefValueA213', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea313 = models.FloatField(db_column='fOperatorRefValueA313', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea413 = models.FloatField(db_column='fOperatorRefValueA413', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea513 = models.FloatField(db_column='fOperatorRefValueA513', blank=True, null=True)  # Field name made lowercase.
    operatorid123 = models.BigIntegerField(db_column='OperatorID123', blank=True, null=True)  # Field name made lowercase.
    serialno123 = models.BigIntegerField(db_column='SerialNo123', blank=True, null=True)  # Field name made lowercase.
    soperatorname123 = models.CharField(db_column='sOperatorName123', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue123 = models.FloatField(db_column='FOperatorValue123', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea123 = models.FloatField(db_column='fOperatorRefValueA123', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea223 = models.FloatField(db_column='fOperatorRefValueA223', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea323 = models.FloatField(db_column='fOperatorRefValueA323', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea423 = models.FloatField(db_column='fOperatorRefValueA423', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea523 = models.FloatField(db_column='fOperatorRefValueA523', blank=True, null=True)  # Field name made lowercase.
    operatorid133 = models.BigIntegerField(db_column='OperatorID133', blank=True, null=True)  # Field name made lowercase.
    serialno133 = models.BigIntegerField(db_column='SerialNo133', blank=True, null=True)  # Field name made lowercase.
    soperatorname133 = models.CharField(db_column='sOperatorName133', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue133 = models.FloatField(db_column='FOperatorValue133', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea133 = models.FloatField(db_column='fOperatorRefValueA133', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea233 = models.FloatField(db_column='fOperatorRefValueA233', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea333 = models.FloatField(db_column='fOperatorRefValueA333', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea433 = models.FloatField(db_column='fOperatorRefValueA433', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea533 = models.FloatField(db_column='fOperatorRefValueA533', blank=True, null=True)  # Field name made lowercase.
    operatorid143 = models.BigIntegerField(db_column='OperatorID143', blank=True, null=True)  # Field name made lowercase.
    serialno143 = models.BigIntegerField(db_column='SerialNo143', blank=True, null=True)  # Field name made lowercase.
    soperatorname143 = models.CharField(db_column='sOperatorName143', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue143 = models.FloatField(db_column='FOperatorValue143', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea143 = models.FloatField(db_column='fOperatorRefValueA143', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea243 = models.FloatField(db_column='fOperatorRefValueA243', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea343 = models.FloatField(db_column='fOperatorRefValueA343', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea443 = models.FloatField(db_column='fOperatorRefValueA443', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea543 = models.FloatField(db_column='fOperatorRefValueA543', blank=True, null=True)  # Field name made lowercase.
    operatorid114 = models.BigIntegerField(db_column='OperatorID114', blank=True, null=True)  # Field name made lowercase.
    serialno114 = models.BigIntegerField(db_column='SerialNo114', blank=True, null=True)  # Field name made lowercase.
    soperatorname114 = models.CharField(db_column='sOperatorName114', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue114 = models.FloatField(db_column='FOperatorValue114', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea114 = models.FloatField(db_column='fOperatorRefValueA114', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea214 = models.FloatField(db_column='fOperatorRefValueA214', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea314 = models.FloatField(db_column='fOperatorRefValueA314', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea414 = models.FloatField(db_column='fOperatorRefValueA414', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea514 = models.FloatField(db_column='fOperatorRefValueA514', blank=True, null=True)  # Field name made lowercase.
    operatorid124 = models.BigIntegerField(db_column='OperatorID124', blank=True, null=True)  # Field name made lowercase.
    serialno124 = models.BigIntegerField(db_column='SerialNo124', blank=True, null=True)  # Field name made lowercase.
    soperatorname124 = models.CharField(db_column='sOperatorName124', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue124 = models.FloatField(db_column='FOperatorValue124', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea124 = models.FloatField(db_column='fOperatorRefValueA124', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea224 = models.FloatField(db_column='fOperatorRefValueA224', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea324 = models.FloatField(db_column='fOperatorRefValueA324', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea424 = models.FloatField(db_column='fOperatorRefValueA424', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea524 = models.FloatField(db_column='fOperatorRefValueA524', blank=True, null=True)  # Field name made lowercase.
    operatorid134 = models.BigIntegerField(db_column='OperatorID134', blank=True, null=True)  # Field name made lowercase.
    serialno134 = models.BigIntegerField(db_column='SerialNo134', blank=True, null=True)  # Field name made lowercase.
    soperatorname134 = models.CharField(db_column='sOperatorName134', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue134 = models.FloatField(db_column='FOperatorValue134', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea134 = models.FloatField(db_column='fOperatorRefValueA134', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea234 = models.FloatField(db_column='fOperatorRefValueA234', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea334 = models.FloatField(db_column='fOperatorRefValueA334', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea434 = models.FloatField(db_column='fOperatorRefValueA434', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea534 = models.FloatField(db_column='fOperatorRefValueA534', blank=True, null=True)  # Field name made lowercase.
    operatorid144 = models.BigIntegerField(db_column='OperatorID144', blank=True, null=True)  # Field name made lowercase.
    serialno144 = models.BigIntegerField(db_column='SerialNo144', blank=True, null=True)  # Field name made lowercase.
    soperatorname144 = models.CharField(db_column='sOperatorName144', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue144 = models.FloatField(db_column='FOperatorValue144', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea144 = models.FloatField(db_column='fOperatorRefValueA144', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea244 = models.FloatField(db_column='fOperatorRefValueA244', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea344 = models.FloatField(db_column='fOperatorRefValueA344', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea444 = models.FloatField(db_column='fOperatorRefValueA444', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea544 = models.FloatField(db_column='fOperatorRefValueA544', blank=True, null=True)  # Field name made lowercase.
    operatorid115 = models.BigIntegerField(db_column='OperatorID115', blank=True, null=True)  # Field name made lowercase.
    serialno115 = models.BigIntegerField(db_column='SerialNo115', blank=True, null=True)  # Field name made lowercase.
    soperatorname115 = models.CharField(db_column='sOperatorName115', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue115 = models.FloatField(db_column='FOperatorValue115', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea115 = models.FloatField(db_column='fOperatorRefValueA115', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea215 = models.FloatField(db_column='fOperatorRefValueA215', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea315 = models.FloatField(db_column='fOperatorRefValueA315', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea415 = models.FloatField(db_column='fOperatorRefValueA415', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea515 = models.FloatField(db_column='fOperatorRefValueA515', blank=True, null=True)  # Field name made lowercase.
    operatorid125 = models.BigIntegerField(db_column='OperatorID125', blank=True, null=True)  # Field name made lowercase.
    serialno125 = models.BigIntegerField(db_column='SerialNo125', blank=True, null=True)  # Field name made lowercase.
    soperatorname125 = models.CharField(db_column='sOperatorName125', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue125 = models.FloatField(db_column='FOperatorValue125', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea125 = models.FloatField(db_column='fOperatorRefValueA125', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea225 = models.FloatField(db_column='fOperatorRefValueA225', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea325 = models.FloatField(db_column='fOperatorRefValueA325', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea425 = models.FloatField(db_column='fOperatorRefValueA425', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea525 = models.FloatField(db_column='fOperatorRefValueA525', blank=True, null=True)  # Field name made lowercase.
    operatorid135 = models.BigIntegerField(db_column='OperatorID135', blank=True, null=True)  # Field name made lowercase.
    serialno135 = models.BigIntegerField(db_column='SerialNo135', blank=True, null=True)  # Field name made lowercase.
    soperatorname135 = models.CharField(db_column='sOperatorName135', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue135 = models.FloatField(db_column='FOperatorValue135', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea135 = models.FloatField(db_column='fOperatorRefValueA135', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea235 = models.FloatField(db_column='fOperatorRefValueA235', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea335 = models.FloatField(db_column='fOperatorRefValueA335', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea435 = models.FloatField(db_column='fOperatorRefValueA435', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea535 = models.FloatField(db_column='fOperatorRefValueA535', blank=True, null=True)  # Field name made lowercase.
    operatorid145 = models.BigIntegerField(db_column='OperatorID145', blank=True, null=True)  # Field name made lowercase.
    serialno145 = models.BigIntegerField(db_column='SerialNo145', blank=True, null=True)  # Field name made lowercase.
    soperatorname145 = models.CharField(db_column='sOperatorName145', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue145 = models.FloatField(db_column='FOperatorValue145', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea145 = models.FloatField(db_column='fOperatorRefValueA145', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea245 = models.FloatField(db_column='fOperatorRefValueA245', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea345 = models.FloatField(db_column='fOperatorRefValueA345', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea445 = models.FloatField(db_column='fOperatorRefValueA445', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvaluea545 = models.FloatField(db_column='fOperatorRefValueA545', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSARnROperator'


class Tmsastabilityanalysis(models.Model):
    lrrspecificatonid = models.BigAutoField(db_column='lRRSpecificatonID', primary_key=True)  # Field name made lowercase.
    rrdate = models.DateTimeField(db_column='RRDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentid = models.CharField(db_column='sInstrumentId', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=350, blank=True, null=True)  # Field name made lowercase.
    tolerance = models.FloatField(db_column='Tolerance', blank=True, null=True)  # Field name made lowercase.
    luomid = models.BigIntegerField(db_column='lUOMID', blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductID', blank=True, null=True)  # Field name made lowercase.
    lparts = models.BigIntegerField(db_column='lParts', blank=True, null=True)  # Field name made lowercase.
    ltrials = models.BigIntegerField(db_column='lTrials', blank=True, null=True)  # Field name made lowercase.
    loperators = models.BigIntegerField(db_column='lOperators', blank=True, null=True)  # Field name made lowercase.
    specialcharacter = models.CharField(db_column='SpecialCharacter', max_length=350, blank=True, null=True)  # Field name made lowercase.
    considertolerance = models.CharField(db_column='ConsiderTolerance', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rangefrom = models.FloatField(db_column='RangeFrom', blank=True, null=True)  # Field name made lowercase.
    rangeto = models.FloatField(db_column='RangeTo', blank=True, null=True)  # Field name made lowercase.
    leastcount = models.FloatField(db_column='LeastCount', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcreatetable = models.BooleanField(db_column='bCreateTable', blank=True, null=True)  # Field name made lowercase.
    previouslrrspecificatonid = models.BigIntegerField(db_column='PreviouslRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    reconduct = models.BooleanField(db_column='ReConduct', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='CurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    calibcost = models.FloatField(db_column='CalibCost', blank=True, null=True)  # Field name made lowercase.
    timetaken = models.CharField(db_column='TimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    calibratedby = models.CharField(db_column='CalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    battributernr = models.BooleanField(db_column='bAttributeRnR', blank=True, null=True)  # Field name made lowercase.
    xbarbar = models.FloatField(db_column='XBARBar', blank=True, null=True)  # Field name made lowercase.
    rbar = models.FloatField(db_column='RBar', blank=True, null=True)  # Field name made lowercase.
    uclxbar = models.FloatField(db_column='UCLXBar', blank=True, null=True)  # Field name made lowercase.
    lclxbar = models.FloatField(db_column='LCLXBar', blank=True, null=True)  # Field name made lowercase.
    uclrange = models.FloatField(db_column='UCLRange', blank=True, null=True)  # Field name made lowercase.
    lclrange = models.FloatField(db_column='LCLRange', blank=True, null=True)  # Field name made lowercase.
    dbias = models.FloatField(db_column='dBias', blank=True, null=True)  # Field name made lowercase.
    dsigmarepr = models.FloatField(db_column='dSigmaRepr', blank=True, null=True)  # Field name made lowercase.
    dsigmabias = models.FloatField(db_column='dSigmaBias', blank=True, null=True)  # Field name made lowercase.
    tbias = models.FloatField(db_column='tBias', blank=True, null=True)  # Field name made lowercase.
    tcritical = models.FloatField(db_column='tCritical', blank=True, null=True)  # Field name made lowercase.
    biasstatus = models.FloatField(db_column='BiasStatus', blank=True, null=True)  # Field name made lowercase.
    biasvalue = models.FloatField(db_column='BiasValue', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    bcategory = models.BooleanField(db_column='bCategory', blank=True, null=True)  # Field name made lowercase.
    categoryhistorymsaid = models.BigIntegerField(db_column='CategoryHistoryMSAID', blank=True, null=True)  # Field name made lowercase.
    lcategoryscheduleid = models.BigIntegerField(db_column='lCategoryScheduleID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    fanalysisval = models.FloatField(db_column='fAnalysisVal', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1 = models.FloatField(db_column='fAnalysisVal1', blank=True, null=True)  # Field name made lowercase.
    fanalysisval2 = models.FloatField(db_column='fAnalysisVal2', blank=True, null=True)  # Field name made lowercase.
    fanalysisval3 = models.FloatField(db_column='fAnalysisVal3', blank=True, null=True)  # Field name made lowercase.
    fanalysisval4 = models.FloatField(db_column='fAnalysisVal4', blank=True, null=True)  # Field name made lowercase.
    fanalysisval5 = models.FloatField(db_column='fAnalysisVal5', blank=True, null=True)  # Field name made lowercase.
    fanalysisval6 = models.FloatField(db_column='fAnalysisVal6', blank=True, null=True)  # Field name made lowercase.
    fanalysisval7 = models.FloatField(db_column='fAnalysisVal7', blank=True, null=True)  # Field name made lowercase.
    fanalysisval8 = models.FloatField(db_column='fAnalysisVal8', blank=True, null=True)  # Field name made lowercase.
    fanalysisval9 = models.FloatField(db_column='fAnalysisVal9', blank=True, null=True)  # Field name made lowercase.
    fanalysisval10 = models.FloatField(db_column='fAnalysisVal10', blank=True, null=True)  # Field name made lowercase.
    fanalysisval11 = models.FloatField(db_column='fAnalysisVal11', blank=True, null=True)  # Field name made lowercase.
    fanalysisval21 = models.FloatField(db_column='fAnalysisVal21', blank=True, null=True)  # Field name made lowercase.
    fanalysisval31 = models.FloatField(db_column='fAnalysisVal31', blank=True, null=True)  # Field name made lowercase.
    fanalysisval41 = models.FloatField(db_column='fAnalysisVal41', blank=True, null=True)  # Field name made lowercase.
    fanalysisval51 = models.FloatField(db_column='fAnalysisVal51', blank=True, null=True)  # Field name made lowercase.
    fanalysisval61 = models.FloatField(db_column='fAnalysisVal61', blank=True, null=True)  # Field name made lowercase.
    fanalysisval71 = models.FloatField(db_column='fAnalysisVal71', blank=True, null=True)  # Field name made lowercase.
    fanalysisval81 = models.FloatField(db_column='fAnalysisVal81', blank=True, null=True)  # Field name made lowercase.
    fanalysisval91 = models.FloatField(db_column='fAnalysisVal91', blank=True, null=True)  # Field name made lowercase.
    fanalysisval101 = models.FloatField(db_column='fAnalysisVal101', blank=True, null=True)  # Field name made lowercase.
    fanalysisval12 = models.FloatField(db_column='fAnalysisVal12', blank=True, null=True)  # Field name made lowercase.
    fanalysisval22 = models.FloatField(db_column='fAnalysisVal22', blank=True, null=True)  # Field name made lowercase.
    fanalysisval32 = models.FloatField(db_column='fAnalysisVal32', blank=True, null=True)  # Field name made lowercase.
    fanalysisval42 = models.FloatField(db_column='fAnalysisVal42', blank=True, null=True)  # Field name made lowercase.
    fanalysisval52 = models.FloatField(db_column='fAnalysisVal52', blank=True, null=True)  # Field name made lowercase.
    fanalysisval62 = models.FloatField(db_column='fAnalysisVal62', blank=True, null=True)  # Field name made lowercase.
    fanalysisval72 = models.FloatField(db_column='fAnalysisVal72', blank=True, null=True)  # Field name made lowercase.
    fanalysisval82 = models.FloatField(db_column='fAnalysisVal82', blank=True, null=True)  # Field name made lowercase.
    fanalysisval92 = models.FloatField(db_column='fAnalysisVal92', blank=True, null=True)  # Field name made lowercase.
    fanalysisval102 = models.FloatField(db_column='fAnalysisVal102', blank=True, null=True)  # Field name made lowercase.
    fanalysisval13 = models.FloatField(db_column='fAnalysisVal13', blank=True, null=True)  # Field name made lowercase.
    fanalysisval23 = models.FloatField(db_column='fAnalysisVal23', blank=True, null=True)  # Field name made lowercase.
    fanalysisval33 = models.FloatField(db_column='fAnalysisVal33', blank=True, null=True)  # Field name made lowercase.
    fanalysisval43 = models.FloatField(db_column='fAnalysisVal43', blank=True, null=True)  # Field name made lowercase.
    fanalysisval53 = models.FloatField(db_column='fAnalysisVal53', blank=True, null=True)  # Field name made lowercase.
    fanalysisval63 = models.FloatField(db_column='fAnalysisVal63', blank=True, null=True)  # Field name made lowercase.
    fanalysisval73 = models.FloatField(db_column='fAnalysisVal73', blank=True, null=True)  # Field name made lowercase.
    fanalysisval83 = models.FloatField(db_column='fAnalysisVal83', blank=True, null=True)  # Field name made lowercase.
    fanalysisval93 = models.FloatField(db_column='fAnalysisVal93', blank=True, null=True)  # Field name made lowercase.
    fanalysisval103 = models.FloatField(db_column='fAnalysisVal103', blank=True, null=True)  # Field name made lowercase.
    fanalysisval14 = models.FloatField(db_column='fAnalysisVal14', blank=True, null=True)  # Field name made lowercase.
    fanalysisval24 = models.FloatField(db_column='fAnalysisVal24', blank=True, null=True)  # Field name made lowercase.
    fanalysisval34 = models.FloatField(db_column='fAnalysisVal34', blank=True, null=True)  # Field name made lowercase.
    fanalysisval44 = models.FloatField(db_column='fAnalysisVal44', blank=True, null=True)  # Field name made lowercase.
    fanalysisval54 = models.FloatField(db_column='fAnalysisVal54', blank=True, null=True)  # Field name made lowercase.
    fanalysisval64 = models.FloatField(db_column='fAnalysisVal64', blank=True, null=True)  # Field name made lowercase.
    fanalysisval74 = models.FloatField(db_column='fAnalysisVal74', blank=True, null=True)  # Field name made lowercase.
    fanalysisval84 = models.FloatField(db_column='fAnalysisVal84', blank=True, null=True)  # Field name made lowercase.
    fanalysisval94 = models.FloatField(db_column='fAnalysisVal94', blank=True, null=True)  # Field name made lowercase.
    fanalysisval104 = models.FloatField(db_column='fAnalysisVal104', blank=True, null=True)  # Field name made lowercase.
    fanalysisval15 = models.FloatField(db_column='fAnalysisVal15', blank=True, null=True)  # Field name made lowercase.
    fanalysisval25 = models.FloatField(db_column='fAnalysisVal25', blank=True, null=True)  # Field name made lowercase.
    fanalysisval35 = models.FloatField(db_column='fAnalysisVal35', blank=True, null=True)  # Field name made lowercase.
    fanalysisval45 = models.FloatField(db_column='fAnalysisVal45', blank=True, null=True)  # Field name made lowercase.
    fanalysisval55 = models.FloatField(db_column='fAnalysisVal55', blank=True, null=True)  # Field name made lowercase.
    fanalysisval65 = models.FloatField(db_column='fAnalysisVal65', blank=True, null=True)  # Field name made lowercase.
    fanalysisval75 = models.FloatField(db_column='fAnalysisVal75', blank=True, null=True)  # Field name made lowercase.
    fanalysisval85 = models.FloatField(db_column='fAnalysisVal85', blank=True, null=True)  # Field name made lowercase.
    fanalysisval95 = models.FloatField(db_column='fAnalysisVal95', blank=True, null=True)  # Field name made lowercase.
    fanalysisval105 = models.FloatField(db_column='fAnalysisVal105', blank=True, null=True)  # Field name made lowercase.
    fanalysisval16 = models.FloatField(db_column='fAnalysisVal16', blank=True, null=True)  # Field name made lowercase.
    fanalysisval26 = models.FloatField(db_column='fAnalysisVal26', blank=True, null=True)  # Field name made lowercase.
    fanalysisval36 = models.FloatField(db_column='fAnalysisVal36', blank=True, null=True)  # Field name made lowercase.
    fanalysisval46 = models.FloatField(db_column='fAnalysisVal46', blank=True, null=True)  # Field name made lowercase.
    fanalysisval56 = models.FloatField(db_column='fAnalysisVal56', blank=True, null=True)  # Field name made lowercase.
    fanalysisval66 = models.FloatField(db_column='fAnalysisVal66', blank=True, null=True)  # Field name made lowercase.
    fanalysisval76 = models.FloatField(db_column='fAnalysisVal76', blank=True, null=True)  # Field name made lowercase.
    fanalysisval86 = models.FloatField(db_column='fAnalysisVal86', blank=True, null=True)  # Field name made lowercase.
    fanalysisval96 = models.FloatField(db_column='fAnalysisVal96', blank=True, null=True)  # Field name made lowercase.
    fanalysisval106 = models.FloatField(db_column='fAnalysisVal106', blank=True, null=True)  # Field name made lowercase.
    fanalysisval17 = models.FloatField(db_column='fAnalysisVal17', blank=True, null=True)  # Field name made lowercase.
    fanalysisval27 = models.FloatField(db_column='fAnalysisVal27', blank=True, null=True)  # Field name made lowercase.
    fanalysisval37 = models.FloatField(db_column='fAnalysisVal37', blank=True, null=True)  # Field name made lowercase.
    fanalysisval47 = models.FloatField(db_column='fAnalysisVal47', blank=True, null=True)  # Field name made lowercase.
    fanalysisval57 = models.FloatField(db_column='fAnalysisVal57', blank=True, null=True)  # Field name made lowercase.
    fanalysisval67 = models.FloatField(db_column='fAnalysisVal67', blank=True, null=True)  # Field name made lowercase.
    fanalysisval77 = models.FloatField(db_column='fAnalysisVal77', blank=True, null=True)  # Field name made lowercase.
    fanalysisval87 = models.FloatField(db_column='fAnalysisVal87', blank=True, null=True)  # Field name made lowercase.
    fanalysisval97 = models.FloatField(db_column='fAnalysisVal97', blank=True, null=True)  # Field name made lowercase.
    fanalysisval107 = models.FloatField(db_column='fAnalysisVal107', blank=True, null=True)  # Field name made lowercase.
    fanalysisval18 = models.FloatField(db_column='fAnalysisVal18', blank=True, null=True)  # Field name made lowercase.
    fanalysisval28 = models.FloatField(db_column='fAnalysisVal28', blank=True, null=True)  # Field name made lowercase.
    fanalysisval38 = models.FloatField(db_column='fAnalysisVal38', blank=True, null=True)  # Field name made lowercase.
    fanalysisval48 = models.FloatField(db_column='fAnalysisVal48', blank=True, null=True)  # Field name made lowercase.
    fanalysisval58 = models.FloatField(db_column='fAnalysisVal58', blank=True, null=True)  # Field name made lowercase.
    fanalysisval68 = models.FloatField(db_column='fAnalysisVal68', blank=True, null=True)  # Field name made lowercase.
    fanalysisval78 = models.FloatField(db_column='fAnalysisVal78', blank=True, null=True)  # Field name made lowercase.
    fanalysisval88 = models.FloatField(db_column='fAnalysisVal88', blank=True, null=True)  # Field name made lowercase.
    fanalysisval98 = models.FloatField(db_column='fAnalysisVal98', blank=True, null=True)  # Field name made lowercase.
    fanalysisval108 = models.FloatField(db_column='fAnalysisVal108', blank=True, null=True)  # Field name made lowercase.
    fanalysisval19 = models.FloatField(db_column='fAnalysisVal19', blank=True, null=True)  # Field name made lowercase.
    fanalysisval29 = models.FloatField(db_column='fAnalysisVal29', blank=True, null=True)  # Field name made lowercase.
    fanalysisval39 = models.FloatField(db_column='fAnalysisVal39', blank=True, null=True)  # Field name made lowercase.
    fanalysisval49 = models.FloatField(db_column='fAnalysisVal49', blank=True, null=True)  # Field name made lowercase.
    fanalysisval59 = models.FloatField(db_column='fAnalysisVal59', blank=True, null=True)  # Field name made lowercase.
    fanalysisval69 = models.FloatField(db_column='fAnalysisVal69', blank=True, null=True)  # Field name made lowercase.
    fanalysisval79 = models.FloatField(db_column='fAnalysisVal79', blank=True, null=True)  # Field name made lowercase.
    fanalysisval89 = models.FloatField(db_column='fAnalysisVal89', blank=True, null=True)  # Field name made lowercase.
    fanalysisval99 = models.FloatField(db_column='fAnalysisVal99', blank=True, null=True)  # Field name made lowercase.
    fanalysisval109 = models.FloatField(db_column='fAnalysisVal109', blank=True, null=True)  # Field name made lowercase.
    fanalysisval110 = models.FloatField(db_column='fAnalysisVal110', blank=True, null=True)  # Field name made lowercase.
    fanalysisval210 = models.FloatField(db_column='fAnalysisVal210', blank=True, null=True)  # Field name made lowercase.
    fanalysisval310 = models.FloatField(db_column='fAnalysisVal310', blank=True, null=True)  # Field name made lowercase.
    fanalysisval410 = models.FloatField(db_column='fAnalysisVal410', blank=True, null=True)  # Field name made lowercase.
    fanalysisval510 = models.FloatField(db_column='fAnalysisVal510', blank=True, null=True)  # Field name made lowercase.
    fanalysisval610 = models.FloatField(db_column='fAnalysisVal610', blank=True, null=True)  # Field name made lowercase.
    fanalysisval710 = models.FloatField(db_column='fAnalysisVal710', blank=True, null=True)  # Field name made lowercase.
    fanalysisval810 = models.FloatField(db_column='fAnalysisVal810', blank=True, null=True)  # Field name made lowercase.
    fanalysisval910 = models.FloatField(db_column='fAnalysisVal910', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1010 = models.FloatField(db_column='fAnalysisVal1010', blank=True, null=True)  # Field name made lowercase.
    fanalysisval111 = models.FloatField(db_column='fAnalysisVal111', blank=True, null=True)  # Field name made lowercase.
    fanalysisval211 = models.FloatField(db_column='fAnalysisVal211', blank=True, null=True)  # Field name made lowercase.
    fanalysisval311 = models.FloatField(db_column='fAnalysisVal311', blank=True, null=True)  # Field name made lowercase.
    fanalysisval411 = models.FloatField(db_column='fAnalysisVal411', blank=True, null=True)  # Field name made lowercase.
    fanalysisval511 = models.FloatField(db_column='fAnalysisVal511', blank=True, null=True)  # Field name made lowercase.
    fanalysisval611 = models.FloatField(db_column='fAnalysisVal611', blank=True, null=True)  # Field name made lowercase.
    fanalysisval711 = models.FloatField(db_column='fAnalysisVal711', blank=True, null=True)  # Field name made lowercase.
    fanalysisval811 = models.FloatField(db_column='fAnalysisVal811', blank=True, null=True)  # Field name made lowercase.
    fanalysisval911 = models.FloatField(db_column='fAnalysisVal911', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1011 = models.FloatField(db_column='fAnalysisVal1011', blank=True, null=True)  # Field name made lowercase.
    fanalysisval112 = models.FloatField(db_column='fAnalysisVal112', blank=True, null=True)  # Field name made lowercase.
    fanalysisval212 = models.FloatField(db_column='fAnalysisVal212', blank=True, null=True)  # Field name made lowercase.
    fanalysisval312 = models.FloatField(db_column='fAnalysisVal312', blank=True, null=True)  # Field name made lowercase.
    fanalysisval412 = models.FloatField(db_column='fAnalysisVal412', blank=True, null=True)  # Field name made lowercase.
    fanalysisval512 = models.FloatField(db_column='fAnalysisVal512', blank=True, null=True)  # Field name made lowercase.
    fanalysisval612 = models.FloatField(db_column='fAnalysisVal612', blank=True, null=True)  # Field name made lowercase.
    fanalysisval712 = models.FloatField(db_column='fAnalysisVal712', blank=True, null=True)  # Field name made lowercase.
    fanalysisval812 = models.FloatField(db_column='fAnalysisVal812', blank=True, null=True)  # Field name made lowercase.
    fanalysisval912 = models.FloatField(db_column='fAnalysisVal912', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1012 = models.FloatField(db_column='fAnalysisVal1012', blank=True, null=True)  # Field name made lowercase.
    fanalysisval113 = models.FloatField(db_column='fAnalysisVal113', blank=True, null=True)  # Field name made lowercase.
    fanalysisval213 = models.FloatField(db_column='fAnalysisVal213', blank=True, null=True)  # Field name made lowercase.
    fanalysisval313 = models.FloatField(db_column='fAnalysisVal313', blank=True, null=True)  # Field name made lowercase.
    fanalysisval413 = models.FloatField(db_column='fAnalysisVal413', blank=True, null=True)  # Field name made lowercase.
    fanalysisval513 = models.FloatField(db_column='fAnalysisVal513', blank=True, null=True)  # Field name made lowercase.
    fanalysisval613 = models.FloatField(db_column='fAnalysisVal613', blank=True, null=True)  # Field name made lowercase.
    fanalysisval713 = models.FloatField(db_column='fAnalysisVal713', blank=True, null=True)  # Field name made lowercase.
    fanalysisval813 = models.FloatField(db_column='fAnalysisVal813', blank=True, null=True)  # Field name made lowercase.
    fanalysisval913 = models.FloatField(db_column='fAnalysisVal913', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1013 = models.FloatField(db_column='fAnalysisVal1013', blank=True, null=True)  # Field name made lowercase.
    fanalysisval114 = models.FloatField(db_column='fAnalysisVal114', blank=True, null=True)  # Field name made lowercase.
    fanalysisval214 = models.FloatField(db_column='fAnalysisVal214', blank=True, null=True)  # Field name made lowercase.
    fanalysisval314 = models.FloatField(db_column='fAnalysisVal314', blank=True, null=True)  # Field name made lowercase.
    fanalysisval414 = models.FloatField(db_column='fAnalysisVal414', blank=True, null=True)  # Field name made lowercase.
    fanalysisval514 = models.FloatField(db_column='fAnalysisVal514', blank=True, null=True)  # Field name made lowercase.
    fanalysisval614 = models.FloatField(db_column='fAnalysisVal614', blank=True, null=True)  # Field name made lowercase.
    fanalysisval714 = models.FloatField(db_column='fAnalysisVal714', blank=True, null=True)  # Field name made lowercase.
    fanalysisval814 = models.FloatField(db_column='fAnalysisVal814', blank=True, null=True)  # Field name made lowercase.
    fanalysisval914 = models.FloatField(db_column='fAnalysisVal914', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1014 = models.FloatField(db_column='fAnalysisVal1014', blank=True, null=True)  # Field name made lowercase.
    fanalysisval115 = models.FloatField(db_column='fAnalysisVal115', blank=True, null=True)  # Field name made lowercase.
    fanalysisval215 = models.FloatField(db_column='fAnalysisVal215', blank=True, null=True)  # Field name made lowercase.
    fanalysisval315 = models.FloatField(db_column='fAnalysisVal315', blank=True, null=True)  # Field name made lowercase.
    fanalysisval415 = models.FloatField(db_column='fAnalysisVal415', blank=True, null=True)  # Field name made lowercase.
    fanalysisval515 = models.FloatField(db_column='fAnalysisVal515', blank=True, null=True)  # Field name made lowercase.
    fanalysisval615 = models.FloatField(db_column='fAnalysisVal615', blank=True, null=True)  # Field name made lowercase.
    fanalysisval715 = models.FloatField(db_column='fAnalysisVal715', blank=True, null=True)  # Field name made lowercase.
    fanalysisval815 = models.FloatField(db_column='fAnalysisVal815', blank=True, null=True)  # Field name made lowercase.
    fanalysisval915 = models.FloatField(db_column='fAnalysisVal915', blank=True, null=True)  # Field name made lowercase.
    fanalysisval1015 = models.FloatField(db_column='fAnalysisVal1015', blank=True, null=True)  # Field name made lowercase.
    srrdate = models.CharField(db_column='sRRDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate1 = models.CharField(db_column='sDueDate1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSAStabilityAnalysis'


class Tmsastabilityoperator(models.Model):
    rroperatorid = models.BigAutoField(db_column='RROperatorID', primary_key=True)  # Field name made lowercase.
    lrrspecificatonid = models.BigIntegerField(db_column='lRRSpecificatonID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.BigIntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    serialno = models.BigIntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    soperatorname = models.CharField(db_column='sOperatorName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue = models.FloatField(db_column='FOperatorValue', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue = models.FloatField(db_column='fOperatorRefValue', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.BigIntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    serialno1 = models.BigIntegerField(db_column='SerialNo1', blank=True, null=True)  # Field name made lowercase.
    soperatorname1 = models.CharField(db_column='sOperatorName1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue1 = models.FloatField(db_column='FOperatorValue1', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue1 = models.FloatField(db_column='fOperatorRefValue1', blank=True, null=True)  # Field name made lowercase.
    operatorid2 = models.BigIntegerField(db_column='OperatorID2', blank=True, null=True)  # Field name made lowercase.
    serialno2 = models.BigIntegerField(db_column='SerialNo2', blank=True, null=True)  # Field name made lowercase.
    soperatorname2 = models.CharField(db_column='sOperatorName2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue2 = models.FloatField(db_column='FOperatorValue2', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue2 = models.FloatField(db_column='fOperatorRefValue2', blank=True, null=True)  # Field name made lowercase.
    operatorid3 = models.BigIntegerField(db_column='OperatorID3', blank=True, null=True)  # Field name made lowercase.
    serialno3 = models.BigIntegerField(db_column='SerialNo3', blank=True, null=True)  # Field name made lowercase.
    soperatorname3 = models.CharField(db_column='sOperatorName3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue3 = models.FloatField(db_column='FOperatorValue3', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue3 = models.FloatField(db_column='fOperatorRefValue3', blank=True, null=True)  # Field name made lowercase.
    operatorid4 = models.BigIntegerField(db_column='OperatorID4', blank=True, null=True)  # Field name made lowercase.
    serialno4 = models.BigIntegerField(db_column='SerialNo4', blank=True, null=True)  # Field name made lowercase.
    soperatorname4 = models.CharField(db_column='sOperatorName4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue4 = models.FloatField(db_column='FOperatorValue4', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue4 = models.FloatField(db_column='fOperatorRefValue4', blank=True, null=True)  # Field name made lowercase.
    operatorid5 = models.BigIntegerField(db_column='OperatorID5', blank=True, null=True)  # Field name made lowercase.
    serialno5 = models.BigIntegerField(db_column='SerialNo5', blank=True, null=True)  # Field name made lowercase.
    soperatorname5 = models.CharField(db_column='sOperatorName5', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue5 = models.FloatField(db_column='FOperatorValue5', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue5 = models.FloatField(db_column='fOperatorRefValue5', blank=True, null=True)  # Field name made lowercase.
    operatorid11 = models.BigIntegerField(db_column='OperatorID11', blank=True, null=True)  # Field name made lowercase.
    serialno11 = models.BigIntegerField(db_column='SerialNo11', blank=True, null=True)  # Field name made lowercase.
    soperatorname11 = models.CharField(db_column='sOperatorName11', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue11 = models.FloatField(db_column='FOperatorValue11', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue11 = models.FloatField(db_column='fOperatorRefValue11', blank=True, null=True)  # Field name made lowercase.
    operatorid21 = models.BigIntegerField(db_column='OperatorID21', blank=True, null=True)  # Field name made lowercase.
    serialno21 = models.BigIntegerField(db_column='SerialNo21', blank=True, null=True)  # Field name made lowercase.
    soperatorname21 = models.CharField(db_column='sOperatorName21', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue21 = models.FloatField(db_column='FOperatorValue21', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue21 = models.FloatField(db_column='fOperatorRefValue21', blank=True, null=True)  # Field name made lowercase.
    operatorid31 = models.BigIntegerField(db_column='OperatorID31', blank=True, null=True)  # Field name made lowercase.
    serialno31 = models.BigIntegerField(db_column='SerialNo31', blank=True, null=True)  # Field name made lowercase.
    soperatorname31 = models.CharField(db_column='sOperatorName31', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue31 = models.FloatField(db_column='FOperatorValue31', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue31 = models.FloatField(db_column='fOperatorRefValue31', blank=True, null=True)  # Field name made lowercase.
    operatorid41 = models.BigIntegerField(db_column='OperatorID41', blank=True, null=True)  # Field name made lowercase.
    serialno41 = models.BigIntegerField(db_column='SerialNo41', blank=True, null=True)  # Field name made lowercase.
    soperatorname41 = models.CharField(db_column='sOperatorName41', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue41 = models.FloatField(db_column='FOperatorValue41', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue41 = models.FloatField(db_column='fOperatorRefValue41', blank=True, null=True)  # Field name made lowercase.
    operatorid51 = models.BigIntegerField(db_column='OperatorID51', blank=True, null=True)  # Field name made lowercase.
    serialno51 = models.BigIntegerField(db_column='SerialNo51', blank=True, null=True)  # Field name made lowercase.
    soperatorname51 = models.CharField(db_column='sOperatorName51', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue51 = models.FloatField(db_column='FOperatorValue51', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue51 = models.FloatField(db_column='fOperatorRefValue51', blank=True, null=True)  # Field name made lowercase.
    operatorid12 = models.BigIntegerField(db_column='OperatorID12', blank=True, null=True)  # Field name made lowercase.
    serialno12 = models.BigIntegerField(db_column='SerialNo12', blank=True, null=True)  # Field name made lowercase.
    soperatorname12 = models.CharField(db_column='sOperatorName12', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue12 = models.FloatField(db_column='FOperatorValue12', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue12 = models.FloatField(db_column='fOperatorRefValue12', blank=True, null=True)  # Field name made lowercase.
    operatorid22 = models.BigIntegerField(db_column='OperatorID22', blank=True, null=True)  # Field name made lowercase.
    serialno22 = models.BigIntegerField(db_column='SerialNo22', blank=True, null=True)  # Field name made lowercase.
    soperatorname22 = models.CharField(db_column='sOperatorName22', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue22 = models.FloatField(db_column='FOperatorValue22', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue22 = models.FloatField(db_column='fOperatorRefValue22', blank=True, null=True)  # Field name made lowercase.
    operatorid32 = models.BigIntegerField(db_column='OperatorID32', blank=True, null=True)  # Field name made lowercase.
    serialno32 = models.BigIntegerField(db_column='SerialNo32', blank=True, null=True)  # Field name made lowercase.
    soperatorname32 = models.CharField(db_column='sOperatorName32', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue32 = models.FloatField(db_column='FOperatorValue32', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue32 = models.FloatField(db_column='fOperatorRefValue32', blank=True, null=True)  # Field name made lowercase.
    operatorid42 = models.BigIntegerField(db_column='OperatorID42', blank=True, null=True)  # Field name made lowercase.
    serialno42 = models.BigIntegerField(db_column='SerialNo42', blank=True, null=True)  # Field name made lowercase.
    soperatorname42 = models.CharField(db_column='sOperatorName42', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue42 = models.FloatField(db_column='FOperatorValue42', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue42 = models.FloatField(db_column='fOperatorRefValue42', blank=True, null=True)  # Field name made lowercase.
    operatorid52 = models.BigIntegerField(db_column='OperatorID52', blank=True, null=True)  # Field name made lowercase.
    serialno52 = models.BigIntegerField(db_column='SerialNo52', blank=True, null=True)  # Field name made lowercase.
    soperatorname52 = models.CharField(db_column='sOperatorName52', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue52 = models.FloatField(db_column='FOperatorValue52', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue52 = models.FloatField(db_column='fOperatorRefValue52', blank=True, null=True)  # Field name made lowercase.
    operatorid13 = models.BigIntegerField(db_column='OperatorID13', blank=True, null=True)  # Field name made lowercase.
    serialno13 = models.BigIntegerField(db_column='SerialNo13', blank=True, null=True)  # Field name made lowercase.
    soperatorname13 = models.CharField(db_column='sOperatorName13', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue13 = models.FloatField(db_column='FOperatorValue13', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue13 = models.FloatField(db_column='fOperatorRefValue13', blank=True, null=True)  # Field name made lowercase.
    operatorid23 = models.BigIntegerField(db_column='OperatorID23', blank=True, null=True)  # Field name made lowercase.
    serialno23 = models.BigIntegerField(db_column='SerialNo23', blank=True, null=True)  # Field name made lowercase.
    soperatorname23 = models.CharField(db_column='sOperatorName23', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue23 = models.FloatField(db_column='FOperatorValue23', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue23 = models.FloatField(db_column='fOperatorRefValue23', blank=True, null=True)  # Field name made lowercase.
    operatorid33 = models.BigIntegerField(db_column='OperatorID33', blank=True, null=True)  # Field name made lowercase.
    serialno33 = models.BigIntegerField(db_column='SerialNo33', blank=True, null=True)  # Field name made lowercase.
    soperatorname33 = models.CharField(db_column='sOperatorName33', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue33 = models.FloatField(db_column='FOperatorValue33', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue33 = models.FloatField(db_column='fOperatorRefValue33', blank=True, null=True)  # Field name made lowercase.
    operatorid43 = models.BigIntegerField(db_column='OperatorID43', blank=True, null=True)  # Field name made lowercase.
    serialno43 = models.BigIntegerField(db_column='SerialNo43', blank=True, null=True)  # Field name made lowercase.
    soperatorname43 = models.CharField(db_column='sOperatorName43', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue43 = models.FloatField(db_column='FOperatorValue43', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue43 = models.FloatField(db_column='fOperatorRefValue43', blank=True, null=True)  # Field name made lowercase.
    operatorid53 = models.BigIntegerField(db_column='OperatorID53', blank=True, null=True)  # Field name made lowercase.
    serialno53 = models.BigIntegerField(db_column='SerialNo53', blank=True, null=True)  # Field name made lowercase.
    soperatorname53 = models.CharField(db_column='sOperatorName53', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue53 = models.FloatField(db_column='FOperatorValue53', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue53 = models.FloatField(db_column='fOperatorRefValue53', blank=True, null=True)  # Field name made lowercase.
    operatorid14 = models.BigIntegerField(db_column='OperatorID14', blank=True, null=True)  # Field name made lowercase.
    serialno14 = models.BigIntegerField(db_column='SerialNo14', blank=True, null=True)  # Field name made lowercase.
    soperatorname14 = models.CharField(db_column='sOperatorName14', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue14 = models.FloatField(db_column='FOperatorValue14', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue14 = models.FloatField(db_column='fOperatorRefValue14', blank=True, null=True)  # Field name made lowercase.
    operatorid24 = models.BigIntegerField(db_column='OperatorID24', blank=True, null=True)  # Field name made lowercase.
    serialno24 = models.BigIntegerField(db_column='SerialNo24', blank=True, null=True)  # Field name made lowercase.
    soperatorname24 = models.CharField(db_column='sOperatorName24', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue24 = models.FloatField(db_column='FOperatorValue24', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue24 = models.FloatField(db_column='fOperatorRefValue24', blank=True, null=True)  # Field name made lowercase.
    operatorid34 = models.BigIntegerField(db_column='OperatorID34', blank=True, null=True)  # Field name made lowercase.
    serialno34 = models.BigIntegerField(db_column='SerialNo34', blank=True, null=True)  # Field name made lowercase.
    soperatorname34 = models.CharField(db_column='sOperatorName34', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue34 = models.FloatField(db_column='FOperatorValue34', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue34 = models.FloatField(db_column='fOperatorRefValue34', blank=True, null=True)  # Field name made lowercase.
    operatorid44 = models.BigIntegerField(db_column='OperatorID44', blank=True, null=True)  # Field name made lowercase.
    serialno44 = models.BigIntegerField(db_column='SerialNo44', blank=True, null=True)  # Field name made lowercase.
    soperatorname44 = models.CharField(db_column='sOperatorName44', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue44 = models.FloatField(db_column='FOperatorValue44', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue44 = models.FloatField(db_column='fOperatorRefValue44', blank=True, null=True)  # Field name made lowercase.
    operatorid54 = models.BigIntegerField(db_column='OperatorID54', blank=True, null=True)  # Field name made lowercase.
    serialno54 = models.BigIntegerField(db_column='SerialNo54', blank=True, null=True)  # Field name made lowercase.
    soperatorname54 = models.CharField(db_column='sOperatorName54', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue54 = models.FloatField(db_column='FOperatorValue54', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue54 = models.FloatField(db_column='fOperatorRefValue54', blank=True, null=True)  # Field name made lowercase.
    operatorid15 = models.BigIntegerField(db_column='OperatorID15', blank=True, null=True)  # Field name made lowercase.
    serialno15 = models.BigIntegerField(db_column='SerialNo15', blank=True, null=True)  # Field name made lowercase.
    soperatorname15 = models.CharField(db_column='sOperatorName15', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue15 = models.FloatField(db_column='FOperatorValue15', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue15 = models.FloatField(db_column='fOperatorRefValue15', blank=True, null=True)  # Field name made lowercase.
    operatorid25 = models.BigIntegerField(db_column='OperatorID25', blank=True, null=True)  # Field name made lowercase.
    serialno25 = models.BigIntegerField(db_column='SerialNo25', blank=True, null=True)  # Field name made lowercase.
    soperatorname25 = models.CharField(db_column='sOperatorName25', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue25 = models.FloatField(db_column='FOperatorValue25', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue25 = models.FloatField(db_column='fOperatorRefValue25', blank=True, null=True)  # Field name made lowercase.
    operatorid35 = models.BigIntegerField(db_column='OperatorID35', blank=True, null=True)  # Field name made lowercase.
    serialno35 = models.BigIntegerField(db_column='SerialNo35', blank=True, null=True)  # Field name made lowercase.
    soperatorname35 = models.CharField(db_column='sOperatorName35', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue35 = models.FloatField(db_column='FOperatorValue35', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue35 = models.FloatField(db_column='fOperatorRefValue35', blank=True, null=True)  # Field name made lowercase.
    operatorid45 = models.BigIntegerField(db_column='OperatorID45', blank=True, null=True)  # Field name made lowercase.
    serialno45 = models.BigIntegerField(db_column='SerialNo45', blank=True, null=True)  # Field name made lowercase.
    soperatorname45 = models.CharField(db_column='sOperatorName45', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue45 = models.FloatField(db_column='FOperatorValue45', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue45 = models.FloatField(db_column='fOperatorRefValue45', blank=True, null=True)  # Field name made lowercase.
    operatorid55 = models.BigIntegerField(db_column='OperatorID55', blank=True, null=True)  # Field name made lowercase.
    serialno55 = models.BigIntegerField(db_column='SerialNo55', blank=True, null=True)  # Field name made lowercase.
    soperatorname55 = models.CharField(db_column='sOperatorName55', max_length=350, blank=True, null=True)  # Field name made lowercase.
    foperatorvalue55 = models.FloatField(db_column='FOperatorValue55', blank=True, null=True)  # Field name made lowercase.
    foperatorrefvalue55 = models.FloatField(db_column='fOperatorRefValue55', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMSAStabilityOperator'


class Tpmhistory(models.Model):
    historyserviceid = models.BigAutoField(db_column='HistoryServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sserviceresult = models.CharField(db_column='sServiceResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtservicedate = models.DateTimeField(db_column='dtServiceDate', blank=True, null=True)  # Field name made lowercase.
    fservicecost = models.FloatField(db_column='fServiceCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredid = models.BigIntegerField(db_column='lEnteredId', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtapprovaldate = models.DateTimeField(db_column='dtApprovalDate', blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.BigIntegerField(db_column='lServiceVendorID', blank=True, null=True)  # Field name made lowercase.
    sservicevendor = models.CharField(db_column='sServiceVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatefile = models.CharField(db_column='sServiceCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatepath = models.CharField(db_column='sServiceCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    lusedbyid = models.BigIntegerField(db_column='lUsedByID', blank=True, null=True)  # Field name made lowercase.
    susedbyname = models.CharField(db_column='sUsedByName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    brefdatail = models.BooleanField(db_column='bRefDatail', blank=True, null=True)  # Field name made lowercase.
    dvendor = models.DateTimeField(db_column='dVendor', blank=True, null=True)  # Field name made lowercase.
    drefdate = models.DateTimeField(db_column='drefDate', blank=True, null=True)  # Field name made lowercase.
    fpmcost = models.FloatField(db_column='fPMCost', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sservicedate = models.CharField(db_column='sServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ssrefdate = models.CharField(db_column='ssrefDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bdvendor = models.BooleanField(db_column='bdVendor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPMHistory'


class Tpmhistorymulti(models.Model):
    lservicemultiid = models.BigAutoField(db_column='lServiceMultiID', primary_key=True)  # Field name made lowercase.
    lhistoryserviceid = models.BigIntegerField(db_column='lHistoryServiceId', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreferenceno = models.CharField(db_column='sReferenceNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcost = models.FloatField(db_column='dCost', blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    lpartid = models.BigIntegerField(db_column='lPartId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPMHistoryMulti'


class Tpartoutward(models.Model):
    historyserviceid = models.BigAutoField(db_column='HistoryServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sserviceresult = models.CharField(db_column='sServiceResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtservicedate = models.DateTimeField(db_column='dtServiceDate', blank=True, null=True)  # Field name made lowercase.
    fservicecost = models.FloatField(db_column='fServiceCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredid = models.BigIntegerField(db_column='lEnteredId', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtapprovaldate = models.DateTimeField(db_column='dtApprovalDate', blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.BigIntegerField(db_column='lServiceVendorID', blank=True, null=True)  # Field name made lowercase.
    sservicevendor = models.CharField(db_column='sServiceVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatefile = models.CharField(db_column='sServiceCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatepath = models.CharField(db_column='sServiceCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    lusedbyid = models.BigIntegerField(db_column='lUsedByID', blank=True, null=True)  # Field name made lowercase.
    susedbyname = models.CharField(db_column='sUsedByName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    brefdatail = models.BooleanField(db_column='bRefDatail', blank=True, null=True)  # Field name made lowercase.
    dvendor = models.DateTimeField(db_column='dVendor', blank=True, null=True)  # Field name made lowercase.
    drefdate = models.DateTimeField(db_column='drefDate', blank=True, null=True)  # Field name made lowercase.
    fpmcost = models.FloatField(db_column='fPMCost', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sservicedate = models.CharField(db_column='sServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ssrefdate = models.CharField(db_column='ssrefDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bdvendor = models.BooleanField(db_column='bdVendor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPartOutward'


class Tpartoutwardmulti(models.Model):
    lservicemultiid = models.BigAutoField(db_column='lServiceMultiID', primary_key=True)  # Field name made lowercase.
    lhistoryserviceid = models.BigIntegerField(db_column='lHistoryServiceId', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreferenceno = models.CharField(db_column='sReferenceNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcost = models.FloatField(db_column='dCost', blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    lpartid = models.BigIntegerField(db_column='lPartId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPartOutwardMulti'


class Tpartpurchase(models.Model):
    historyserviceid = models.BigAutoField(db_column='HistoryServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sserviceresult = models.CharField(db_column='sServiceResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtservicedate = models.DateTimeField(db_column='dtServiceDate', blank=True, null=True)  # Field name made lowercase.
    fservicecost = models.FloatField(db_column='fServiceCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredid = models.BigIntegerField(db_column='lEnteredId', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtapprovaldate = models.DateTimeField(db_column='dtApprovalDate', blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.BigIntegerField(db_column='lServiceVendorID', blank=True, null=True)  # Field name made lowercase.
    sservicevendor = models.CharField(db_column='sServiceVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatefile = models.CharField(db_column='sServiceCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatepath = models.CharField(db_column='sServiceCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    lusedbyid = models.BigIntegerField(db_column='lUsedByID', blank=True, null=True)  # Field name made lowercase.
    susedbyname = models.CharField(db_column='sUsedByName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    brefdatail = models.BooleanField(db_column='bRefDatail', blank=True, null=True)  # Field name made lowercase.
    dvendor = models.DateTimeField(db_column='dVendor', blank=True, null=True)  # Field name made lowercase.
    drefdate = models.DateTimeField(db_column='drefDate', blank=True, null=True)  # Field name made lowercase.
    fpmcost = models.FloatField(db_column='fPMCost', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sservicedate = models.CharField(db_column='sServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ssrefdate = models.CharField(db_column='ssrefDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate2 = models.CharField(db_column='sDueDate2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bdvendor = models.BooleanField(db_column='bdVendor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPartPurchase'


class Tpartpurchasemulti(models.Model):
    lservicemultiid = models.BigAutoField(db_column='lServiceMultiID', primary_key=True)  # Field name made lowercase.
    lhistoryserviceid = models.BigIntegerField(db_column='lHistoryServiceId', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreferenceno = models.CharField(db_column='sReferenceNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcost = models.FloatField(db_column='dCost', blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    lpartid = models.BigIntegerField(db_column='lPartId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPartPurchaseMulti'


class Tpostpone(models.Model):
    lpostponeid = models.BigAutoField(db_column='lPostponeId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibfrequency = models.BigIntegerField(db_column='lCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    scalibfreqtype = models.CharField(db_column='sCalibFreqType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sremarks = models.CharField(db_column='sRemarks', max_length=750, blank=True, null=True)  # Field name made lowercase.
    dtpostponedate = models.DateTimeField(db_column='dtPostponeDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    dtcurdate = models.DateTimeField(db_column='dtCurDate', blank=True, null=True)  # Field name made lowercase.
    lpostponedbyid = models.BigIntegerField(db_column='lPostponedByID', blank=True, null=True)  # Field name made lowercase.
    spostponename = models.CharField(db_column='sPostponeName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile1 = models.CharField(db_column='sCalibrationCertificateFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    spostponedate = models.CharField(db_column='sPostponeDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scurdate = models.CharField(db_column='sCurDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPostpone'


class Tpostponemsaservice(models.Model):
    lpostponemsaserviceid = models.BigAutoField(db_column='lPostponeMSAServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibfrequency = models.BigIntegerField(db_column='lCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    scalibfreqtype = models.CharField(db_column='sCalibFreqType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sremarks = models.CharField(db_column='sRemarks', max_length=750, blank=True, null=True)  # Field name made lowercase.
    dtpostponemsaservicedate = models.DateTimeField(db_column='dtPostponeMSAServiceDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    dtcurdate = models.DateTimeField(db_column='dtCurDate', blank=True, null=True)  # Field name made lowercase.
    lpostponemsaservicedbyid = models.BigIntegerField(db_column='lPostponeMSAServicedByID', blank=True, null=True)  # Field name made lowercase.
    spostponemsaservicename = models.CharField(db_column='sPostponeMSAServiceName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile1 = models.CharField(db_column='sCalibrationCertificateFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    spostponemsaservicedate = models.CharField(db_column='sPostponeMSAServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scurdate = models.CharField(db_column='sCurDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPostponeMSAService'


class Tpostponeservice(models.Model):
    lpostponeserviceid = models.BigAutoField(db_column='lPostponeServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibfrequency = models.BigIntegerField(db_column='lCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    scalibfreqtype = models.CharField(db_column='sCalibFreqType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sremarks = models.CharField(db_column='sRemarks', max_length=750, blank=True, null=True)  # Field name made lowercase.
    dtpostponeservicedate = models.DateTimeField(db_column='dtPostponeServiceDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    dtcurdate = models.DateTimeField(db_column='dtCurDate', blank=True, null=True)  # Field name made lowercase.
    lpostponeservicedbyid = models.BigIntegerField(db_column='lPostponeServicedByID', blank=True, null=True)  # Field name made lowercase.
    spostponeservicename = models.CharField(db_column='sPostponeServiceName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile1 = models.CharField(db_column='sCalibrationCertificateFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    spostponemsaservicedate = models.CharField(db_column='sPostponeMSAServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scurdate = models.CharField(db_column='sCurDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPostponeService'


class Tprepone(models.Model):
    lpreponeid = models.BigAutoField(db_column='lPreponeId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibfrequency = models.BigIntegerField(db_column='lCalibFrequency', blank=True, null=True)  # Field name made lowercase.
    scalibfreqtype = models.CharField(db_column='sCalibFreqType', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sremarks = models.CharField(db_column='sRemarks', max_length=750, blank=True, null=True)  # Field name made lowercase.
    dtpreponedate = models.DateTimeField(db_column='dtPreponeDate', blank=True, null=True)  # Field name made lowercase.
    dtactualdate = models.DateTimeField(db_column='dtActualDate', blank=True, null=True)  # Field name made lowercase.
    dtcurdate = models.DateTimeField(db_column='dtCurDate', blank=True, null=True)  # Field name made lowercase.
    lpreponedbyid = models.BigIntegerField(db_column='lPreponedByID', blank=True, null=True)  # Field name made lowercase.
    spreponename = models.CharField(db_column='sPreponeName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile1 = models.CharField(db_column='sCalibrationCertificateFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    spreponedate = models.CharField(db_column='sPreponeDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sactualdate = models.CharField(db_column='sActualDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scurdate = models.CharField(db_column='sCurDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPrepone'


class Tservicehistory(models.Model):
    historyserviceid = models.BigAutoField(db_column='HistoryServiceId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brepair = models.BooleanField(db_column='bRepair', blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sserviceresult = models.CharField(db_column='sServiceResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtservicedate = models.DateTimeField(db_column='dtServiceDate', blank=True, null=True)  # Field name made lowercase.
    fservicecost = models.FloatField(db_column='fServiceCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredid = models.BigIntegerField(db_column='lEnteredId', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtapprovaldate = models.DateTimeField(db_column='dtApprovalDate', blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lservicevendorid = models.BigIntegerField(db_column='lServiceVendorID', blank=True, null=True)  # Field name made lowercase.
    sservicevendor = models.CharField(db_column='sServiceVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatefile = models.CharField(db_column='sServiceCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sservicecertificatepath = models.CharField(db_column='sServiceCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    lusedbyid = models.BigIntegerField(db_column='lUsedByID', blank=True, null=True)  # Field name made lowercase.
    susedbyname = models.CharField(db_column='sUsedByName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    brefdatail = models.BooleanField(db_column='bRefDatail', blank=True, null=True)  # Field name made lowercase.
    dvendor = models.DateTimeField(db_column='dVendor', blank=True, null=True)  # Field name made lowercase.
    drefdate = models.DateTimeField(db_column='drefDate', blank=True, null=True)  # Field name made lowercase.
    fpmcost = models.FloatField(db_column='fPMCost', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    lnoticedbyid = models.BigIntegerField(db_column='lNoticedByID', blank=True, null=True)  # Field name made lowercase.
    snoticedbyname = models.CharField(db_column='sNoticedByName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreason = models.CharField(db_column='sReason', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdateofnotice = models.DateTimeField(db_column='dtDateofNotice', blank=True, null=True)  # Field name made lowercase.
    llocationid = models.BigIntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocationname = models.CharField(db_column='sLocationName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    brejected = models.BooleanField(db_column='bRejected', blank=True, null=True)  # Field name made lowercase.
    bsentforrepair = models.BooleanField(db_column='bSentforRepair', blank=True, null=True)  # Field name made lowercase.
    ldcrefid = models.BigIntegerField(db_column='lDCRefId', blank=True, null=True)  # Field name made lowercase.
    sservicedate = models.CharField(db_column='sServiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapprovaldate = models.CharField(db_column='sApprovalDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sdispatchdate = models.CharField(db_column='sDispatchDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    srefdate = models.CharField(db_column='srefDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sdateofnotice = models.CharField(db_column='sDateofNotice', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bdvendor = models.BooleanField(db_column='bdVendor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TServiceHistory'


class Tservicehistorymulti(models.Model):
    lservicemultiid = models.BigAutoField(db_column='lServiceMultiID', primary_key=True)  # Field name made lowercase.
    lhistoryserviceid = models.BigIntegerField(db_column='lHistoryServiceId', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreferenceno = models.CharField(db_column='sReferenceNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dcost = models.FloatField(db_column='dCost', blank=True, null=True)  # Field name made lowercase.
    lqty = models.BigIntegerField(db_column='lQty', blank=True, null=True)  # Field name made lowercase.
    lpartid = models.BigIntegerField(db_column='lPartId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TServiceHistoryMulti'


class Tuncertainity(models.Model):
    luncertanityid = models.BigAutoField(db_column='lUncertanityID', primary_key=True)  # Field name made lowercase.
    dtuncertainitydate = models.DateTimeField(db_column='dtUncertainityDate', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentname = models.CharField(db_column='sInstrumentName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    frangefrom = models.FloatField(db_column='fRangeFrom', blank=True, null=True)  # Field name made lowercase.
    frangeto = models.FloatField(db_column='fRangeTo', blank=True, null=True)  # Field name made lowercase.
    fleastcount = models.FloatField(db_column='fLeastCount', blank=True, null=True)  # Field name made lowercase.
    lresolution = models.BigIntegerField(db_column='lResolution', blank=True, null=True)  # Field name made lowercase.
    ftempbegin = models.FloatField(db_column='fTempBegin', blank=True, null=True)  # Field name made lowercase.
    ftempmiddle = models.FloatField(db_column='fTempMiddle', blank=True, null=True)  # Field name made lowercase.
    ftempend = models.FloatField(db_column='fTempEnd', blank=True, null=True)  # Field name made lowercase.
    ftempmean = models.FloatField(db_column='fTempMean', blank=True, null=True)  # Field name made lowercase.
    drh = models.FloatField(db_column='dRH', blank=True, null=True)  # Field name made lowercase.
    lnoofreading = models.BigIntegerField(db_column='lNoofReading', blank=True, null=True)  # Field name made lowercase.
    fxbar = models.FloatField(db_column='fXBar', blank=True, null=True)  # Field name made lowercase.
    fstddev = models.FloatField(db_column='fStdDev', blank=True, null=True)  # Field name made lowercase.
    fstddevmean = models.FloatField(db_column='fStdDevMean', blank=True, null=True)  # Field name made lowercase.
    fdegreeoffreedom = models.FloatField(db_column='fDegreeofFreedom', blank=True, null=True)  # Field name made lowercase.
    falpha = models.FloatField(db_column='fAlpha', blank=True, null=True)  # Field name made lowercase.
    falphaundercalibration = models.FloatField(db_column='fAlphaunderCalibration', blank=True, null=True)  # Field name made lowercase.
    fcombinedstd = models.FloatField(db_column='fCombinedStd', blank=True, null=True)  # Field name made lowercase.
    feffectivedegreeoffreedom = models.FloatField(db_column='fEffectiveDegreeofFreedom', blank=True, null=True)  # Field name made lowercase.
    fcombinedfactor = models.FloatField(db_column='fCombinedFactor', blank=True, null=True)  # Field name made lowercase.
    fexpandaduncertainity = models.FloatField(db_column='fExpandadUncertainity', blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.BigIntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    suncertainitydate = models.CharField(db_column='sUncertainityDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUncertainity'


class Tuncertainityreading(models.Model):
    luncertanityidreading = models.BigAutoField(db_column='lUncertanityIDReading', primary_key=True)  # Field name made lowercase.
    luncertanityid = models.BigIntegerField(db_column='lUncertanityID', blank=True, null=True)  # Field name made lowercase.
    stest = models.CharField(max_length=350, blank=True, null=True)
    ll1 = models.BigIntegerField(blank=True, null=True)
    fxixbar1 = models.FloatField(db_column='fXiXbar1', blank=True, null=True)  # Field name made lowercase.
    fxixbarsqr1 = models.FloatField(db_column='fXiXbarSqr1', blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.BigIntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUncertainityReading'


class Tuncertainityresults(models.Model):
    luncertanityresultid = models.BigAutoField(db_column='lUncertanityResultID', primary_key=True)  # Field name made lowercase.
    luncertanityid = models.BigIntegerField(db_column='lUncertanityID', blank=True, null=True)  # Field name made lowercase.
    ssourceu1 = models.CharField(db_column='sSourceU1', max_length=750, blank=True, null=True)  # Field name made lowercase.
    fsourcevalueu1 = models.FloatField(db_column='fSourceValueU1', blank=True, null=True)  # Field name made lowercase.
    fkfactoru1 = models.FloatField(db_column='fKFactorU1', blank=True, null=True)  # Field name made lowercase.
    fcalculationu1 = models.FloatField(db_column='fCalculationU1', blank=True, null=True)  # Field name made lowercase.
    fstduncu1 = models.FloatField(db_column='fstdUncU1', blank=True, null=True)  # Field name made lowercase.
    fprobablityu1 = models.FloatField(db_column='fProbablityU1', blank=True, null=True)  # Field name made lowercase.
    fstduncertainityu1 = models.FloatField(db_column='fStdUncertainityU1', blank=True, null=True)  # Field name made lowercase.
    fsensitivityu1 = models.FloatField(db_column='fSensitivityU1', blank=True, null=True)  # Field name made lowercase.
    funcertainitycontributionu1 = models.FloatField(db_column='fUncertainityContributionU1', blank=True, null=True)  # Field name made lowercase.
    fcalcu1 = models.FloatField(db_column='fCalcU1', blank=True, null=True)  # Field name made lowercase.
    fdegreeoffreedumcu1 = models.FloatField(db_column='fDegreeofFreedumcU1', blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=750, blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.BigIntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUncertainityResults'


class Tusagetime(models.Model):
    lhistoryusageid = models.BigAutoField(db_column='lHistoryUsageId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lcurrentlocationid = models.BigIntegerField(db_column='lCurrentLocationId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=750, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdetails = models.CharField(db_column='sInstrumentDetails', max_length=750, blank=True, null=True)  # Field name made lowercase.
    slocationname = models.CharField(db_column='sLocationName', max_length=750, blank=True, null=True)  # Field name made lowercase.
    dtreportdate = models.DateTimeField(db_column='dtReportDate', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lenteredbyid = models.BigIntegerField(db_column='lEnteredByID', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lapprovedbyid = models.BigIntegerField(db_column='lApprovedByID', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtapprovaldate = models.DateTimeField(db_column='dtApprovalDate', blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lnewlocationid = models.BigIntegerField(db_column='lNewLocationId', blank=True, null=True)  # Field name made lowercase.
    snewlocationdesc = models.CharField(db_column='sNewLocationDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scheckout = models.CharField(db_column='sCheckOut', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sreportrefno = models.CharField(db_column='sReportRefNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lproductid = models.BigIntegerField(db_column='lProductId', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sreportdate = models.CharField(db_column='sReportDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapprovaldate = models.CharField(db_column='sApprovalDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUsageTime'


class Tutilitylog(models.Model):
    lultilitylogid = models.BigAutoField(db_column='lUltilityLogID', primary_key=True)  # Field name made lowercase.
    butility = models.BooleanField(db_column='bUtility', blank=True, null=True)  # Field name made lowercase.
    bon = models.BooleanField(db_column='bOn', blank=True, null=True)  # Field name made lowercase.
    boff = models.BooleanField(db_column='bOff', blank=True, null=True)  # Field name made lowercase.
    breading = models.BooleanField(db_column='bReading', blank=True, null=True)  # Field name made lowercase.
    lutilityid = models.BigIntegerField(db_column='lUtilityId', blank=True, null=True)  # Field name made lowercase.
    sutilitydescription = models.CharField(db_column='sUtilityDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ddate = models.FloatField(db_column='dDate', blank=True, null=True)  # Field name made lowercase.
    dtime = models.FloatField(db_column='dTime', blank=True, null=True)  # Field name made lowercase.
    dreading = models.FloatField(db_column='dReading', blank=True, null=True)  # Field name made lowercase.
    sremarks = models.CharField(db_column='sRemarks', max_length=750, blank=True, null=True)  # Field name made lowercase.
    lusedid = models.BigIntegerField(db_column='lUsedId', blank=True, null=True)  # Field name made lowercase.
    susedby = models.CharField(db_column='sUsedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedid = models.BigIntegerField(db_column='lApprovedId', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    splantcode = models.CharField(db_column='sPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    sreportdate = models.CharField(db_column='sReportDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sapprovaldate = models.CharField(db_column='sApprovalDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUtilityLog'


class Tverificationmain(models.Model):
    lhistorymainid = models.BigAutoField(db_column='lHistoryMainId', primary_key=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentId', blank=True, null=True)  # Field name made lowercase.
    lscheduleid = models.BigIntegerField(db_column='lScheduleId', blank=True, null=True)  # Field name made lowercase.
    sinstrumentcode = models.CharField(db_column='sInstrumentCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sinstrumentdesc = models.CharField(db_column='sInstrumentDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scurrentstatus = models.CharField(db_column='sCurrentStatus', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationresult = models.CharField(db_column='sCalibrationResult', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtcalibrationdate = models.DateTimeField(db_column='dtCalibrationDate', blank=True, null=True)  # Field name made lowercase.
    fcalibcost = models.FloatField(db_column='fCalibCost', blank=True, null=True)  # Field name made lowercase.
    stimetaken = models.CharField(db_column='sTimeTaken', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sdevicecondition = models.CharField(db_column='sDeviceCondition', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemperature = models.CharField(db_column='sTemperature', max_length=350, blank=True, null=True)  # Field name made lowercase.
    shumidity = models.CharField(db_column='sHumidity', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lenteredbyid = models.BigIntegerField(db_column='lEnteredById', blank=True, null=True)  # Field name made lowercase.
    senteredby = models.CharField(db_column='sEnteredBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lapprovedbyid = models.BigIntegerField(db_column='lApprovedById', blank=True, null=True)  # Field name made lowercase.
    sapprovedby = models.CharField(db_column='sApprovedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    sapprovaldate = models.CharField(db_column='sApprovalDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scomments = models.CharField(db_column='sComments', max_length=750, blank=True, null=True)  # Field name made lowercase.
    scalibrationvendor = models.CharField(db_column='sCalibrationVendor', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcalibrationvendorid = models.BigIntegerField(db_column='lCalibrationVendorID', blank=True, null=True)  # Field name made lowercase.
    spurchaseorderno = models.CharField(db_column='sPurchaseOrderNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatefile = models.CharField(db_column='sCalibrationCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificatepath = models.CharField(db_column='sCalibrationCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dtdispatchdate = models.DateTimeField(db_column='dtDispatchDate', blank=True, null=True)  # Field name made lowercase.
    dtduedate = models.DateTimeField(db_column='dtDueDate', blank=True, null=True)  # Field name made lowercase.
    lcalibratedbyid = models.BigIntegerField(db_column='lCalibratedByID', blank=True, null=True)  # Field name made lowercase.
    scalibratedby = models.CharField(db_column='sCalibratedBy', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bapproved = models.BooleanField(db_column='bApproved', blank=True, null=True)  # Field name made lowercase.
    scalibrationcertificateno = models.CharField(db_column='sCalibrationCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bcertificate = models.BooleanField(db_column='bCertificate', blank=True, null=True)  # Field name made lowercase.
    ftotalerror = models.FloatField(db_column='fTotalError', blank=True, null=True)  # Field name made lowercase.
    facconstant = models.FloatField(db_column='fACConstant', blank=True, null=True)  # Field name made lowercase.
    flc = models.FloatField(db_column='fLC', blank=True, null=True)  # Field name made lowercase.
    fproducttolerance = models.FloatField(db_column='fProductTolerance', blank=True, null=True)  # Field name made lowercase.
    facceptancecriteria = models.FloatField(db_column='fAcceptanceCriteria', blank=True, null=True)  # Field name made lowercase.
    dtindentdate = models.DateTimeField(db_column='dtIndentDate', blank=True, null=True)  # Field name made lowercase.
    dgtreturneddate = models.DateTimeField(db_column='dgtReturnedDate', blank=True, null=True)  # Field name made lowercase.
    dtissuedate = models.DateTimeField(db_column='dtIssueDate', blank=True, null=True)  # Field name made lowercase.
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
    ferrormax = models.FloatField(db_column='fErrorMax', blank=True, null=True)  # Field name made lowercase.
    ferrormin = models.FloatField(db_column='fErrorMin', blank=True, null=True)  # Field name made lowercase.
    ftotalerror1 = models.FloatField(db_column='fTotalError1', blank=True, null=True)  # Field name made lowercase.
    dtrecddate = models.DateTimeField(db_column='dtRecdDate', blank=True, null=True)  # Field name made lowercase.
    dtissueddate = models.DateTimeField(db_column='dtIssuedDate', blank=True, null=True)  # Field name made lowercase.
    scategory = models.CharField(db_column='sCategory', max_length=350, blank=True, null=True)  # Field name made lowercase.
    spurchaseordernosinstdesc = models.CharField(db_column='sPurchaseOrderNosInstDesc', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp1 = models.CharField(db_column='sTemp1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp2 = models.CharField(db_column='sTemp2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp3 = models.CharField(db_column='sTemp3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp4 = models.CharField(db_column='sTemp4', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp5 = models.CharField(db_column='sTemp5', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp6 = models.CharField(db_column='sTemp6', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp7 = models.CharField(db_column='sTemp7', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp8 = models.CharField(db_column='sTemp8', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp9 = models.CharField(db_column='sTemp9', max_length=350, blank=True, null=True)  # Field name made lowercase.
    stemp10 = models.CharField(db_column='sTemp10', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile1 = models.CharField(db_column='sTraceabilityFile1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath1 = models.CharField(db_column='sTraceabilitypath1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile2 = models.CharField(db_column='sTraceabilityFile2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath2 = models.CharField(db_column='sTraceabilitypath2', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilityfile3 = models.CharField(db_column='sTraceabilityFile3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    straceabilitypath3 = models.CharField(db_column='sTraceabilitypath3', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bdcdone = models.BooleanField(db_column='bDCDone', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantcode = models.CharField(db_column='lPlantCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.
    scalibrationdate = models.CharField(db_column='sCalibrationDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sissueddate = models.CharField(db_column='sIssuedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    srecddate = models.CharField(db_column='sRecdDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sissuedate = models.CharField(db_column='sIssueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sgtreturneddate = models.CharField(db_column='sgtReturnedDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sindentdate = models.CharField(db_column='sIndentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sduedate = models.CharField(db_column='sDueDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sdispatchdate = models.CharField(db_column='sDispatchDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    saapprovaldate = models.CharField(db_column='sAApprovalDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TVerificationMain'


class Admin1Atrack(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lhistorymainid = models.BigIntegerField(db_column='lHistoryMainId', blank=True, null=True)  # Field name made lowercase.
    dtdateoftransaction = models.DateTimeField(db_column='dtDateofTransaction', blank=True, null=True)  # Field name made lowercase.
    stimeoftrans = models.CharField(db_column='sTimeofTrans', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepage = models.CharField(db_column='sUsedTypePage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework = models.CharField(db_column='sUsedTypePageWork', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework1 = models.CharField(db_column='sUsedTypePageWork1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedtypepagework2 = models.CharField(db_column='sUsedTypePageWork2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    susedby = models.CharField(db_column='sUsedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin1ATrack'


class Admin1Companyinfo(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    ldays = models.BigIntegerField(db_column='lDays', blank=True, null=True)  # Field name made lowercase.
    dtcurrentdate = models.DateTimeField(db_column='dtCurrentDate', blank=True, null=True)  # Field name made lowercase.
    sdivision = models.CharField(db_column='sDivision', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtreminderdate = models.DateTimeField(db_column='dtReminderDate', blank=True, null=True)  # Field name made lowercase.
    semailsendfrom = models.CharField(db_column='sEmailSendFrom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semailsmtpno = models.CharField(db_column='sEmailSMTPNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lremotesocket = models.BigIntegerField(db_column='lRemoteSocket', blank=True, null=True)  # Field name made lowercase.
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
    ldcno = models.BigIntegerField(db_column='lDCNo', blank=True, null=True)  # Field name made lowercase.
    lmonth = models.BigIntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.BigIntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    ldcno1 = models.BigIntegerField(db_column='lDCNo1', blank=True, null=True)  # Field name made lowercase.
    ldcno2 = models.BigIntegerField(db_column='lDCNo2', blank=True, null=True)  # Field name made lowercase.
    ldcno3 = models.BigIntegerField(db_column='lDCNo3', blank=True, null=True)  # Field name made lowercase.
    ldcno4 = models.BigIntegerField(db_column='lDCNo4', blank=True, null=True)  # Field name made lowercase.
    ldcno5 = models.BigIntegerField(db_column='lDCNo5', blank=True, null=True)  # Field name made lowercase.
    ldcno6 = models.BigIntegerField(db_column='lDCNo6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin1CompanyInfo'


class Adminassetcategorylist(models.Model):
    lcategoryid = models.BigAutoField(db_column='lCategoryID', primary_key=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='CategoryType', max_length=255)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lassetid = models.BigIntegerField(db_column='lAssetID', blank=True, null=True)  # Field name made lowercase.
    btyperef = models.BooleanField(db_column='bTypeRef', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasint', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.BigIntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.BigIntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    btyperef1 = models.BooleanField(db_column='bTypeRef1', blank=True, null=True)  # Field name made lowercase.
    styperefname1 = models.CharField(db_column='sTypeRefName1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring1 = models.BooleanField(db_column='bTypeRefasString1', blank=True, null=True)  # Field name made lowercase.
    btyperefasint1 = models.BooleanField(db_column='bTypeRefasint1', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange1 = models.BooleanField(db_column='bTypeRefasRange1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa1 = models.BooleanField(db_column='bTypeRefasContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob1 = models.BooleanField(db_column='bTypeRefasContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa1 = models.BigIntegerField(db_column='lContinuousNoA1', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob1 = models.BigIntegerField(db_column='lContinuousNoB1', blank=True, null=True)  # Field name made lowercase.
    btyperef2 = models.BooleanField(db_column='bTypeRef2', blank=True, null=True)  # Field name made lowercase.
    styperefname2 = models.CharField(db_column='sTypeRefName2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring2 = models.BooleanField(db_column='bTypeRefasString2', blank=True, null=True)  # Field name made lowercase.
    btyperefasint2 = models.BooleanField(db_column='bTypeRefasint2', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange2 = models.BooleanField(db_column='bTypeRefasRange2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa2 = models.BooleanField(db_column='bTypeRefasContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob2 = models.BooleanField(db_column='bTypeRefasContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa2 = models.BigIntegerField(db_column='lContinuousNoA2', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob2 = models.BigIntegerField(db_column='lContinuousNoB2', blank=True, null=True)  # Field name made lowercase.
    btyperef3 = models.BooleanField(db_column='bTypeRef3', blank=True, null=True)  # Field name made lowercase.
    styperefname3 = models.CharField(db_column='sTypeRefName3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring3 = models.BooleanField(db_column='bTypeRefasString3', blank=True, null=True)  # Field name made lowercase.
    btyperefasint3 = models.BooleanField(db_column='bTypeRefasint3', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange3 = models.BooleanField(db_column='bTypeRefasRange3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa3 = models.BooleanField(db_column='bTypeRefasContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob3 = models.BooleanField(db_column='bTypeRefasContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa3 = models.BigIntegerField(db_column='lContinuousNoA3', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob3 = models.BigIntegerField(db_column='lContinuousNoB3', blank=True, null=True)  # Field name made lowercase.
    btyperef4 = models.BooleanField(db_column='bTypeRef4', blank=True, null=True)  # Field name made lowercase.
    styperefname4 = models.CharField(db_column='sTypeRefName4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring4 = models.BooleanField(db_column='bTypeRefasString4', blank=True, null=True)  # Field name made lowercase.
    btyperefasint4 = models.BooleanField(db_column='bTypeRefasint4', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange4 = models.BooleanField(db_column='bTypeRefasRange4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa4 = models.BooleanField(db_column='bTypeRefasContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob4 = models.BooleanField(db_column='bTypeRefasContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa4 = models.BigIntegerField(db_column='lContinuousNoA4', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob4 = models.BigIntegerField(db_column='lContinuousNoB4', blank=True, null=True)  # Field name made lowercase.
    btyperef5 = models.BooleanField(db_column='bTypeRef5', blank=True, null=True)  # Field name made lowercase.
    styperefname5 = models.CharField(db_column='sTypeRefName5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring5 = models.BooleanField(db_column='bTypeRefasString5', blank=True, null=True)  # Field name made lowercase.
    btyperefasint5 = models.BooleanField(db_column='bTypeRefasint5', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange5 = models.BooleanField(db_column='bTypeRefasRange5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa5 = models.BooleanField(db_column='bTypeRefasContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob5 = models.BooleanField(db_column='bTypeRefasContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa5 = models.BigIntegerField(db_column='lContinuousNoA5', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob5 = models.BigIntegerField(db_column='lContinuousNoB5', blank=True, null=True)  # Field name made lowercase.
    btyperef6 = models.BooleanField(db_column='bTypeRef6', blank=True, null=True)  # Field name made lowercase.
    styperefname6 = models.CharField(db_column='sTypeRefName6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring6 = models.BooleanField(db_column='bTypeRefasString6', blank=True, null=True)  # Field name made lowercase.
    btyperefasint6 = models.BooleanField(db_column='bTypeRefasint6', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange6 = models.BooleanField(db_column='bTypeRefasRange6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa6 = models.BooleanField(db_column='bTypeRefasContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob6 = models.BooleanField(db_column='bTypeRefasContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa6 = models.BigIntegerField(db_column='lContinuousNoA6', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob6 = models.BigIntegerField(db_column='lContinuousNoB6', blank=True, null=True)  # Field name made lowercase.
    btyperef7 = models.BooleanField(db_column='bTypeRef7', blank=True, null=True)  # Field name made lowercase.
    styperefname7 = models.CharField(db_column='sTypeRefName7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring7 = models.BooleanField(db_column='bTypeRefasString7', blank=True, null=True)  # Field name made lowercase.
    btyperefasint7 = models.BooleanField(db_column='bTypeRefasint7', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange7 = models.BooleanField(db_column='bTypeRefasRange7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa7 = models.BooleanField(db_column='bTypeRefasContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob7 = models.BooleanField(db_column='bTypeRefasContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa7 = models.BigIntegerField(db_column='lContinuousNoA7', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob7 = models.BigIntegerField(db_column='lContinuousNoB7', blank=True, null=True)  # Field name made lowercase.
    btyperef8 = models.BooleanField(db_column='bTypeRef8', blank=True, null=True)  # Field name made lowercase.
    styperefname8 = models.CharField(db_column='sTypeRefName8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring8 = models.BooleanField(db_column='bTypeRefasString8', blank=True, null=True)  # Field name made lowercase.
    btyperefasint8 = models.BooleanField(db_column='bTypeRefasint8', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange8 = models.BooleanField(db_column='bTypeRefasRange8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa8 = models.BooleanField(db_column='bTypeRefasContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob8 = models.BooleanField(db_column='bTypeRefasContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa8 = models.BigIntegerField(db_column='lContinuousNoA8', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob8 = models.BigIntegerField(db_column='lContinuousNoB8', blank=True, null=True)  # Field name made lowercase.
    btyperef9 = models.BooleanField(db_column='bTypeRef9', blank=True, null=True)  # Field name made lowercase.
    styperefname9 = models.CharField(db_column='sTypeRefName9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring9 = models.BooleanField(db_column='bTypeRefasString9', blank=True, null=True)  # Field name made lowercase.
    btyperefasint9 = models.BooleanField(db_column='bTypeRefasint9', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange9 = models.BooleanField(db_column='bTypeRefasRange9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa9 = models.BooleanField(db_column='bTypeRefasContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob9 = models.BooleanField(db_column='bTypeRefasContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa9 = models.BigIntegerField(db_column='lContinuousNoA9', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob9 = models.BigIntegerField(db_column='lContinuousNoB9', blank=True, null=True)  # Field name made lowercase.
    btyperef10 = models.BooleanField(db_column='bTypeRef10', blank=True, null=True)  # Field name made lowercase.
    styperefname10 = models.CharField(db_column='sTypeRefName10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring10 = models.BooleanField(db_column='bTypeRefasString10', blank=True, null=True)  # Field name made lowercase.
    btyperefasint10 = models.BooleanField(db_column='bTypeRefasint10', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange10 = models.BooleanField(db_column='bTypeRefasRange10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa10 = models.BooleanField(db_column='bTypeRefasContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob10 = models.BooleanField(db_column='bTypeRefasContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa10 = models.BigIntegerField(db_column='lContinuousNoA10', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob10 = models.BigIntegerField(db_column='lContinuousNoB10', blank=True, null=True)  # Field name made lowercase.
    btyperef11 = models.BooleanField(db_column='bTypeRef11', blank=True, null=True)  # Field name made lowercase.
    styperefname11 = models.CharField(db_column='sTypeRefName11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring11 = models.BooleanField(db_column='bTypeRefasString11', blank=True, null=True)  # Field name made lowercase.
    btyperefasint11 = models.BooleanField(db_column='bTypeRefasint11', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange11 = models.BooleanField(db_column='bTypeRefasRange11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa11 = models.BooleanField(db_column='bTypeRefasContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob11 = models.BooleanField(db_column='bTypeRefasContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa11 = models.BigIntegerField(db_column='lContinuousNoA11', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob11 = models.BigIntegerField(db_column='lContinuousNoB11', blank=True, null=True)  # Field name made lowercase.
    btyperef12 = models.BooleanField(db_column='bTypeRef12', blank=True, null=True)  # Field name made lowercase.
    styperefname12 = models.CharField(db_column='sTypeRefName12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring12 = models.BooleanField(db_column='bTypeRefasString12', blank=True, null=True)  # Field name made lowercase.
    btyperefasint12 = models.BooleanField(db_column='bTypeRefasint12', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange12 = models.BooleanField(db_column='bTypeRefasRange12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa12 = models.BooleanField(db_column='bTypeRefasContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob12 = models.BooleanField(db_column='bTypeRefasContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa12 = models.BigIntegerField(db_column='lContinuousNoA12', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob12 = models.BigIntegerField(db_column='lContinuousNoB12', blank=True, null=True)  # Field name made lowercase.
    btyperef13 = models.BooleanField(db_column='bTypeRef13', blank=True, null=True)  # Field name made lowercase.
    styperefname13 = models.CharField(db_column='sTypeRefName13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring13 = models.BooleanField(db_column='bTypeRefasString13', blank=True, null=True)  # Field name made lowercase.
    btyperefasint13 = models.BooleanField(db_column='bTypeRefasint13', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange13 = models.BooleanField(db_column='bTypeRefasRange13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa13 = models.BooleanField(db_column='bTypeRefasContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob13 = models.BooleanField(db_column='bTypeRefasContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa13 = models.BigIntegerField(db_column='lContinuousNoA13', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob13 = models.BigIntegerField(db_column='lContinuousNoB13', blank=True, null=True)  # Field name made lowercase.
    btyperef14 = models.BooleanField(db_column='bTypeRef14', blank=True, null=True)  # Field name made lowercase.
    styperefname14 = models.CharField(db_column='sTypeRefName14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring14 = models.BooleanField(db_column='bTypeRefasString14', blank=True, null=True)  # Field name made lowercase.
    btyperefasint14 = models.BooleanField(db_column='bTypeRefasint14', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange14 = models.BooleanField(db_column='bTypeRefasRange14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa14 = models.BooleanField(db_column='bTypeRefasContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob14 = models.BooleanField(db_column='bTypeRefasContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa14 = models.BigIntegerField(db_column='lContinuousNoA14', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob14 = models.BigIntegerField(db_column='lContinuousNoB14', blank=True, null=True)  # Field name made lowercase.
    btyperef15 = models.BooleanField(db_column='bTypeRef15', blank=True, null=True)  # Field name made lowercase.
    styperefname15 = models.CharField(db_column='sTypeRefName15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring15 = models.BooleanField(db_column='bTypeRefasString15', blank=True, null=True)  # Field name made lowercase.
    btyperefasint15 = models.BooleanField(db_column='bTypeRefasint15', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange15 = models.BooleanField(db_column='bTypeRefasRange15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa15 = models.BooleanField(db_column='bTypeRefasContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob15 = models.BooleanField(db_column='bTypeRefasContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa15 = models.BigIntegerField(db_column='lContinuousNoA15', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob15 = models.BigIntegerField(db_column='lContinuousNoB15', blank=True, null=True)  # Field name made lowercase.
    btyperef16 = models.BooleanField(db_column='bTypeRef16', blank=True, null=True)  # Field name made lowercase.
    styperefname16 = models.CharField(db_column='sTypeRefName16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring16 = models.BooleanField(db_column='bTypeRefasString16', blank=True, null=True)  # Field name made lowercase.
    btyperefasint16 = models.BooleanField(db_column='bTypeRefasint16', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange16 = models.BooleanField(db_column='bTypeRefasRange16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa16 = models.BooleanField(db_column='bTypeRefasContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob16 = models.BooleanField(db_column='bTypeRefasContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa16 = models.BigIntegerField(db_column='lContinuousNoA16', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob16 = models.BigIntegerField(db_column='lContinuousNoB16', blank=True, null=True)  # Field name made lowercase.
    btyperef17 = models.BooleanField(db_column='bTypeRef17', blank=True, null=True)  # Field name made lowercase.
    styperefname17 = models.CharField(db_column='sTypeRefName17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring17 = models.BooleanField(db_column='bTypeRefasString17', blank=True, null=True)  # Field name made lowercase.
    btyperefasint17 = models.BooleanField(db_column='bTypeRefasint17', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange17 = models.BooleanField(db_column='bTypeRefasRange17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa17 = models.BooleanField(db_column='bTypeRefasContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob17 = models.BooleanField(db_column='bTypeRefasContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa17 = models.BigIntegerField(db_column='lContinuousNoA17', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob17 = models.BigIntegerField(db_column='lContinuousNoB17', blank=True, null=True)  # Field name made lowercase.
    btyperef18 = models.BooleanField(db_column='bTypeRef18', blank=True, null=True)  # Field name made lowercase.
    styperefname18 = models.CharField(db_column='sTypeRefName18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring18 = models.BooleanField(db_column='bTypeRefasString18', blank=True, null=True)  # Field name made lowercase.
    btyperefasint18 = models.BooleanField(db_column='bTypeRefasint18', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange18 = models.BooleanField(db_column='bTypeRefasRange18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa18 = models.BooleanField(db_column='bTypeRefasContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob18 = models.BooleanField(db_column='bTypeRefasContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa18 = models.BigIntegerField(db_column='lContinuousNoA18', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob18 = models.BigIntegerField(db_column='lContinuousNoB18', blank=True, null=True)  # Field name made lowercase.
    btyperef19 = models.BooleanField(db_column='bTypeRef19', blank=True, null=True)  # Field name made lowercase.
    styperefname19 = models.CharField(db_column='sTypeRefName19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring19 = models.BooleanField(db_column='bTypeRefasString19', blank=True, null=True)  # Field name made lowercase.
    btyperefasint19 = models.BooleanField(db_column='bTypeRefasint19', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange19 = models.BooleanField(db_column='bTypeRefasRange19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa19 = models.BooleanField(db_column='bTypeRefasContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob19 = models.BooleanField(db_column='bTypeRefasContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa19 = models.BigIntegerField(db_column='lContinuousNoA19', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob19 = models.BigIntegerField(db_column='lContinuousNoB19', blank=True, null=True)  # Field name made lowercase.
    btyperef20 = models.BooleanField(db_column='bTypeRef20', blank=True, null=True)  # Field name made lowercase.
    styperefname20 = models.CharField(db_column='sTypeRefName20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring20 = models.BooleanField(db_column='bTypeRefasString20', blank=True, null=True)  # Field name made lowercase.
    btyperefasint20 = models.BooleanField(db_column='bTypeRefasint20', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange20 = models.BooleanField(db_column='bTypeRefasRange20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa20 = models.BooleanField(db_column='bTypeRefasContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob20 = models.BooleanField(db_column='bTypeRefasContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa20 = models.BigIntegerField(db_column='lContinuousNoA20', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob20 = models.BigIntegerField(db_column='lContinuousNoB20', blank=True, null=True)  # Field name made lowercase.
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
    lintervalrnr = models.BigIntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.BigIntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lrnr = models.BigIntegerField(db_column='lRnR', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lattribute = models.BigIntegerField(db_column='lAttribute', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lstability = models.BigIntegerField(db_column='lStability', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lbias = models.BigIntegerField(db_column='lBias', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    llinearity = models.BigIntegerField(db_column='lLinearity', blank=True, null=True)  # Field name made lowercase.
    bmsablock = models.BooleanField(db_column='bMSABlock', blank=True, null=True)  # Field name made lowercase.
    lminqty = models.BigIntegerField(db_column='lMinQty', blank=True, null=True)  # Field name made lowercase.
    lmaxqty = models.BigIntegerField(db_column='lMaxQty', blank=True, null=True)  # Field name made lowercase.
    lavailableqty = models.BigIntegerField(db_column='lAvailableQty', blank=True, null=True)  # Field name made lowercase.
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
    ldueday = models.BigIntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.BigIntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.BigIntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lcategorytypeid = models.BigAutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.BigIntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.BigIntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.BigIntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.BigIntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasint', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.BigIntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.BigIntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lcode = models.BigIntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.BigIntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.BigIntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.BigIntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
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
    lcategorytypeid = models.BigAutoField(db_column='lCategoryTypeID', primary_key=True)  # Field name made lowercase.
    scategorytype = models.CharField(db_column='sCategoryType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcategorytype1 = models.BigIntegerField(db_column='lCategoryType1', blank=True, null=True)  # Field name made lowercase.
    lcategorytype2 = models.BigIntegerField(db_column='lCategoryType2', blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.BigIntegerField(db_column='lCode1', blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.BigIntegerField(db_column='lCode2', blank=True, null=True)  # Field name made lowercase.
    styperefname = models.CharField(db_column='sTypeRefName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btyperefasstring = models.BooleanField(db_column='bTypeRefasString', blank=True, null=True)  # Field name made lowercase.
    btyperefasint = models.BooleanField(db_column='bTypeRefasint', blank=True, null=True)  # Field name made lowercase.
    btyperefasrange = models.BooleanField(db_column='bTypeRefasRange', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnoa = models.BooleanField(db_column='bTypeRefasContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    btyperefascontinuousnob = models.BooleanField(db_column='bTypeRefasContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnoa = models.BigIntegerField(db_column='lContinuousNoA', blank=True, null=True)  # Field name made lowercase.
    lcontinuousnob = models.BigIntegerField(db_column='lContinuousNoB', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lcode = models.BigIntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.BigIntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.BigIntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.BigIntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
    stitle = models.CharField(db_column='sTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle1 = models.CharField(db_column='sTitle1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle2 = models.CharField(db_column='sTitle2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle3 = models.CharField(db_column='sTitle3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle4 = models.CharField(db_column='sTitle4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    stitle5 = models.CharField(db_column='sTitle5', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetCategoryTypeList1'


class Adminassetclassificationlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sclassification = models.CharField(db_column='sClassification', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetClassificationList'


class Adminassetcontinuousformatlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scontinuousformat = models.CharField(db_column='sContinuousFormat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcontinuousformat = models.BigIntegerField(db_column='lContinuousFormat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetContinuousFormatList'


class Adminassetserialformatlist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lserialno = models.BigIntegerField(db_column='lSerialNo', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminAssetSerialFormatList'


class Adminassetsparepartslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=350, blank=True, null=True)  # Field name made lowercase.
    srevetails = models.CharField(db_column='sRevetails', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bstock = models.BooleanField(db_column='bStock', blank=True, null=True)  # Field name made lowercase.
    drate = models.FloatField(db_column='dRate', blank=True, null=True)  # Field name made lowercase.
    lopenbal = models.BigIntegerField(db_column='lOpenBal', blank=True, null=True)  # Field name made lowercase.
    linward = models.BigIntegerField(db_column='lInward', blank=True, null=True)  # Field name made lowercase.
    loutward = models.BigIntegerField(db_column='lOutward', blank=True, null=True)  # Field name made lowercase.
    ltotqty = models.BigIntegerField(db_column='lTotQty', blank=True, null=True)  # Field name made lowercase.
    suom = models.CharField(db_column='sUOM', max_length=350, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lcode = models.BigIntegerField(db_column='lCode', blank=True, null=True)  # Field name made lowercase.
    lcode3 = models.BigIntegerField(db_column='lCode3', blank=True, null=True)  # Field name made lowercase.
    lcode4 = models.BigIntegerField(db_column='lCode4', blank=True, null=True)  # Field name made lowercase.
    lcode5 = models.BigIntegerField(db_column='lCode5', blank=True, null=True)  # Field name made lowercase.
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
    lassetid = models.BigAutoField(db_column='lAssetID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lassetid = models.BigAutoField(db_column='lAssetID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lassettypeid = models.BigIntegerField(db_column='lAssetTypeID', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stemperature = models.CharField(db_column='sTemperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shumidity = models.CharField(db_column='sHumidity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCalibConditionsList'


class Admincategoryidcontinuousnolist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lserialno = models.BigIntegerField(db_column='lSerialNo', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCategoryIDContinuousNoList'


class Admincategoryidserialnolist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lserialno = models.BigIntegerField(db_column='lSerialNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCategoryIDSerialNoList'


class Admincustomerlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminCustomerList'


class Adminequipmentlist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    sequipmentname = models.CharField(db_column='sEquipmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminEquipmentList'


class Adminexternalagencylist(models.Model):
    lagencyid = models.BigAutoField(db_column='lAgencyId', primary_key=True)  # Field name made lowercase.
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
    dtnablcertificatevalidity = models.CharField(db_column='dtNABLCertificateValidity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scertificateno = models.CharField(db_column='sCertificateNo', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatedate = models.CharField(db_column='sNABLCertificateDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatefile = models.CharField(db_column='sNABLCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatepath = models.CharField(db_column='sNABLCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.BigIntegerField(db_column='lLocationID', blank=True, null=True)  # Field name made lowercase.
    sgst = models.CharField(db_column='sGST', max_length=350, blank=True, null=True)  # Field name made lowercase.
    span = models.CharField(db_column='sPAN', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminExternalAgencyList'


class Adminexternalagencytraceabilitylist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    straceability = models.CharField(db_column='sTraceability', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatedate = models.CharField(db_column='sNABLCertificateDate', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatefile = models.CharField(db_column='sNABLCertificateFile', max_length=350, blank=True, null=True)  # Field name made lowercase.
    snablcertificatepath = models.CharField(db_column='sNABLCertificatepath', max_length=350, blank=True, null=True)  # Field name made lowercase.
    lagencyid = models.BigIntegerField(db_column='lAgencyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminExternalAgencyTraceabilityList'


class Admingradelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sgradename = models.CharField(db_column='sGradeName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminGradeList'


class Admininstrumentcattypelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scattype = models.CharField(db_column='sCatType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentCatTypeList'


class Admininstrumentcatsubtypelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scattype = models.CharField(db_column='sCatType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcattypeid = models.BigIntegerField(db_column='lCatTypeId', blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentCatsubTypeList'


class Admininstrumentequipmentlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sequipment = models.CharField(db_column='sEquipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentEquipmentList'


class Admininstrumentmateriallist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smaterial = models.CharField(db_column='sMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentMaterialList'


class Admininstrumentoperationlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    soperation = models.CharField(db_column='sOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentOperationList'


class Admininstrumentrangelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentRangeList'


class Admininstrumenttypelist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    sinstrumenttype = models.CharField(db_column='sInstrumentType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminInstrumentTypeList'


class Adminlocationlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    slocationname = models.CharField(db_column='sLocationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scontactperson = models.CharField(db_column='sContactPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scontactemailid = models.CharField(db_column='sContactEMailId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminLocationList'


class Adminmakelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smake = models.CharField(db_column='sMake', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminMakeList'


class Adminmateriallist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    smaterial = models.CharField(db_column='sMaterial', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminMaterialList'


class Adminoperatorlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    soperator = models.CharField(db_column='sOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminOperatorList'


class Adminpartdetailslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spartname = models.CharField(db_column='sPartName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.BigIntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lpantid = models.BigIntegerField(db_column='lPantId', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.BigIntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.BigIntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    smsasopfile = models.CharField(db_column='sMSASOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.BigIntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.BigIntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.BigIntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    ldueday1 = models.BigIntegerField(db_column='lDueDay1', blank=True, null=True)  # Field name made lowercase.
    lduemonth1 = models.BigIntegerField(db_column='lDueMonth1', blank=True, null=True)  # Field name made lowercase.
    ldueyear1 = models.BigIntegerField(db_column='lDueYear1', blank=True, null=True)  # Field name made lowercase.
    ldueday2 = models.BigIntegerField(db_column='lDueDay2', blank=True, null=True)  # Field name made lowercase.
    lduemonth2 = models.BigIntegerField(db_column='lDueMonth2', blank=True, null=True)  # Field name made lowercase.
    ldueyear2 = models.BigIntegerField(db_column='lDueYear2', blank=True, null=True)  # Field name made lowercase.
    ldueday3 = models.BigIntegerField(db_column='lDueDay3', blank=True, null=True)  # Field name made lowercase.
    lduemonth3 = models.BigIntegerField(db_column='lDueMonth3', blank=True, null=True)  # Field name made lowercase.
    ldueyear3 = models.BigIntegerField(db_column='lDueYear3', blank=True, null=True)  # Field name made lowercase.
    ldueday4 = models.BigIntegerField(db_column='lDueDay4', blank=True, null=True)  # Field name made lowercase.
    lduemonth4 = models.BigIntegerField(db_column='lDueMonth4', blank=True, null=True)  # Field name made lowercase.
    ldueyear4 = models.BigIntegerField(db_column='lDueYear4', blank=True, null=True)  # Field name made lowercase.
    ldueday5 = models.BigIntegerField(db_column='lDueDay5', blank=True, null=True)  # Field name made lowercase.
    lduemonth5 = models.BigIntegerField(db_column='lDueMonth5', blank=True, null=True)  # Field name made lowercase.
    ldueyear5 = models.BigIntegerField(db_column='lDueYear5', blank=True, null=True)  # Field name made lowercase.
    ldueday6 = models.BigIntegerField(db_column='lDueDay6', blank=True, null=True)  # Field name made lowercase.
    lduemonth6 = models.BigIntegerField(db_column='lDueMonth6', blank=True, null=True)  # Field name made lowercase.
    ldueyear6 = models.BigIntegerField(db_column='lDueYear6', blank=True, null=True)  # Field name made lowercase.
    bvisualinspection = models.BooleanField(db_column='bVisualInspection', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr1 = models.BigIntegerField(db_column='lIntervalRnR1', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr1 = models.CharField(db_column='sIntervalPeriodRnR1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr1 = models.DateTimeField(db_column='dLastRnR1', blank=True, null=True)  # Field name made lowercase.
    dnextrnr1 = models.DateTimeField(db_column='dNextRnR1', blank=True, null=True)  # Field name made lowercase.
    lalertinterval1 = models.BigIntegerField(db_column='lAlertInterval1', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate1 = models.DateTimeField(db_column='dtRnRDisplayDate1', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr2 = models.BigIntegerField(db_column='lIntervalRnR2', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr2 = models.CharField(db_column='sIntervalPeriodRnR2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr2 = models.DateTimeField(db_column='dLastRnR2', blank=True, null=True)  # Field name made lowercase.
    dnextrnr2 = models.DateTimeField(db_column='dNextRnR2', blank=True, null=True)  # Field name made lowercase.
    lalertinterval2 = models.BigIntegerField(db_column='lAlertInterval2', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate2 = models.DateTimeField(db_column='dtRnRDisplayDate2', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr3 = models.BigIntegerField(db_column='lIntervalRnR3', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr3 = models.CharField(db_column='sIntervalPeriodRnR3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr3 = models.DateTimeField(db_column='dLastRnR3', blank=True, null=True)  # Field name made lowercase.
    dnextrnr3 = models.DateTimeField(db_column='dNextRnR3', blank=True, null=True)  # Field name made lowercase.
    lalertinterval3 = models.BigIntegerField(db_column='lAlertInterval3', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate3 = models.DateTimeField(db_column='dtRnRDisplayDate3', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr4 = models.BigIntegerField(db_column='lIntervalRnR4', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr4 = models.CharField(db_column='sIntervalPeriodRnR4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr4 = models.DateTimeField(db_column='dLastRnR4', blank=True, null=True)  # Field name made lowercase.
    dnextrnr4 = models.DateTimeField(db_column='dNextRnR4', blank=True, null=True)  # Field name made lowercase.
    lalertinterval4 = models.BigIntegerField(db_column='lAlertInterval4', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate4 = models.DateTimeField(db_column='dtRnRDisplayDate4', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr5 = models.BigIntegerField(db_column='lIntervalRnR5', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr5 = models.CharField(db_column='sIntervalPeriodRnR5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr5 = models.DateTimeField(db_column='dLastRnR5', blank=True, null=True)  # Field name made lowercase.
    dnextrnr5 = models.DateTimeField(db_column='dNextRnR5', blank=True, null=True)  # Field name made lowercase.
    lalertinterval5 = models.BigIntegerField(db_column='lAlertInterval5', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate5 = models.DateTimeField(db_column='dtRnRDisplayDate5', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsList'


class AdminpartdetailslistBackup(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    spartno = models.CharField(db_column='sPartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spartname = models.CharField(db_column='sPartName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.BigIntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lpantid = models.BigIntegerField(db_column='lPantId', blank=True, null=True)  # Field name made lowercase.
    brnr = models.BooleanField(db_column='bRnR', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr = models.BigIntegerField(db_column='lIntervalRnR', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr = models.CharField(db_column='sIntervalPeriodRnR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr = models.DateTimeField(db_column='dLastRnR', blank=True, null=True)  # Field name made lowercase.
    dnextrnr = models.DateTimeField(db_column='dNextRnR', blank=True, null=True)  # Field name made lowercase.
    lalertinterval = models.BigIntegerField(db_column='lAlertInterval', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate = models.DateTimeField(db_column='dtRnRDisplayDate', blank=True, null=True)  # Field name made lowercase.
    smsasopfile = models.CharField(db_column='sMSASOPFile', max_length=480, blank=True, null=True)  # Field name made lowercase.
    ldueday = models.BigIntegerField(db_column='lDueDay', blank=True, null=True)  # Field name made lowercase.
    lduemonth = models.BigIntegerField(db_column='lDueMonth', blank=True, null=True)  # Field name made lowercase.
    ldueyear = models.BigIntegerField(db_column='lDueYear', blank=True, null=True)  # Field name made lowercase.
    ldueday1 = models.BigIntegerField(db_column='lDueDay1', blank=True, null=True)  # Field name made lowercase.
    lduemonth1 = models.BigIntegerField(db_column='lDueMonth1', blank=True, null=True)  # Field name made lowercase.
    ldueyear1 = models.BigIntegerField(db_column='lDueYear1', blank=True, null=True)  # Field name made lowercase.
    ldueday2 = models.BigIntegerField(db_column='lDueDay2', blank=True, null=True)  # Field name made lowercase.
    lduemonth2 = models.BigIntegerField(db_column='lDueMonth2', blank=True, null=True)  # Field name made lowercase.
    ldueyear2 = models.BigIntegerField(db_column='lDueYear2', blank=True, null=True)  # Field name made lowercase.
    ldueday3 = models.BigIntegerField(db_column='lDueDay3', blank=True, null=True)  # Field name made lowercase.
    lduemonth3 = models.BigIntegerField(db_column='lDueMonth3', blank=True, null=True)  # Field name made lowercase.
    ldueyear3 = models.BigIntegerField(db_column='lDueYear3', blank=True, null=True)  # Field name made lowercase.
    ldueday4 = models.BigIntegerField(db_column='lDueDay4', blank=True, null=True)  # Field name made lowercase.
    lduemonth4 = models.BigIntegerField(db_column='lDueMonth4', blank=True, null=True)  # Field name made lowercase.
    ldueyear4 = models.BigIntegerField(db_column='lDueYear4', blank=True, null=True)  # Field name made lowercase.
    ldueday5 = models.BigIntegerField(db_column='lDueDay5', blank=True, null=True)  # Field name made lowercase.
    lduemonth5 = models.BigIntegerField(db_column='lDueMonth5', blank=True, null=True)  # Field name made lowercase.
    ldueyear5 = models.BigIntegerField(db_column='lDueYear5', blank=True, null=True)  # Field name made lowercase.
    ldueday6 = models.BigIntegerField(db_column='lDueDay6', blank=True, null=True)  # Field name made lowercase.
    lduemonth6 = models.BigIntegerField(db_column='lDueMonth6', blank=True, null=True)  # Field name made lowercase.
    ldueyear6 = models.BigIntegerField(db_column='lDueYear6', blank=True, null=True)  # Field name made lowercase.
    bvisualinspection = models.BooleanField(db_column='bVisualInspection', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr1 = models.BigIntegerField(db_column='lIntervalRnR1', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr1 = models.CharField(db_column='sIntervalPeriodRnR1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr1 = models.DateTimeField(db_column='dLastRnR1', blank=True, null=True)  # Field name made lowercase.
    dnextrnr1 = models.DateTimeField(db_column='dNextRnR1', blank=True, null=True)  # Field name made lowercase.
    lalertinterval1 = models.BigIntegerField(db_column='lAlertInterval1', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate1 = models.DateTimeField(db_column='dtRnRDisplayDate1', blank=True, null=True)  # Field name made lowercase.
    bstability = models.BooleanField(db_column='bStability', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr2 = models.BigIntegerField(db_column='lIntervalRnR2', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr2 = models.CharField(db_column='sIntervalPeriodRnR2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr2 = models.DateTimeField(db_column='dLastRnR2', blank=True, null=True)  # Field name made lowercase.
    dnextrnr2 = models.DateTimeField(db_column='dNextRnR2', blank=True, null=True)  # Field name made lowercase.
    lalertinterval2 = models.BigIntegerField(db_column='lAlertInterval2', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate2 = models.DateTimeField(db_column='dtRnRDisplayDate2', blank=True, null=True)  # Field name made lowercase.
    bbias = models.BooleanField(db_column='bBias', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr3 = models.BigIntegerField(db_column='lIntervalRnR3', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr3 = models.CharField(db_column='sIntervalPeriodRnR3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr3 = models.DateTimeField(db_column='dLastRnR3', blank=True, null=True)  # Field name made lowercase.
    dnextrnr3 = models.DateTimeField(db_column='dNextRnR3', blank=True, null=True)  # Field name made lowercase.
    lalertinterval3 = models.BigIntegerField(db_column='lAlertInterval3', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate3 = models.DateTimeField(db_column='dtRnRDisplayDate3', blank=True, null=True)  # Field name made lowercase.
    blinearity = models.BooleanField(db_column='bLinearity', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr4 = models.BigIntegerField(db_column='lIntervalRnR4', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr4 = models.CharField(db_column='sIntervalPeriodRnR4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr4 = models.DateTimeField(db_column='dLastRnR4', blank=True, null=True)  # Field name made lowercase.
    dnextrnr4 = models.DateTimeField(db_column='dNextRnR4', blank=True, null=True)  # Field name made lowercase.
    lalertinterval4 = models.BigIntegerField(db_column='lAlertInterval4', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate4 = models.DateTimeField(db_column='dtRnRDisplayDate4', blank=True, null=True)  # Field name made lowercase.
    battribute = models.BooleanField(db_column='bAttribute', blank=True, null=True)  # Field name made lowercase.
    lintervalrnr5 = models.BigIntegerField(db_column='lIntervalRnR5', blank=True, null=True)  # Field name made lowercase.
    sintervalperiodrnr5 = models.CharField(db_column='sIntervalPeriodRnR5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dlastrnr5 = models.DateTimeField(db_column='dLastRnR5', blank=True, null=True)  # Field name made lowercase.
    dnextrnr5 = models.DateTimeField(db_column='dNextRnR5', blank=True, null=True)  # Field name made lowercase.
    lalertinterval5 = models.BigIntegerField(db_column='lAlertInterval5', blank=True, null=True)  # Field name made lowercase.
    dtrnrdisplaydate5 = models.DateTimeField(db_column='dtRnRDisplayDate5', blank=True, null=True)  # Field name made lowercase.
    dcostofwork = models.FloatField(db_column='dCostofWork', blank=True, null=True)  # Field name made lowercase.
    dnextrnrdisplay = models.DateTimeField(db_column='dNextRnRDisplay', blank=True, null=True)  # Field name made lowercase.
    dnextrnralert = models.DateTimeField(db_column='dNextRnRAlert', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsList_Backup'


class Adminpartdetailsforinstrumentlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lpartnoid = models.BigIntegerField(db_column='lPartNoID', blank=True, null=True)  # Field name made lowercase.
    linstrumentid = models.BigIntegerField(db_column='lInstrumentID', blank=True, null=True)  # Field name made lowercase.
    sinstrumentno = models.CharField(db_column='sInstrumentNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPartDetailsforInstrumentList'


class Adminpurchasechecklist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='sDescription', max_length=480, blank=True, null=True)  # Field name made lowercase.
    sspecification = models.CharField(db_column='sSpecification', max_length=480, blank=True, null=True)  # Field name made lowercase.
    bok = models.BooleanField(db_column='bOK', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminPurchaseCheckList'


class Adminrangelist(models.Model):
    lid = models.BigAutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    srange = models.CharField(db_column='sRange', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminRangeList'


class Adminrolelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    srolename = models.CharField(db_column='sRoleName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminRoleList'


class Adminstoragelocationlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sstoragelocation = models.CharField(db_column='sStorageLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lplantid = models.BigIntegerField(db_column='lPlantId', blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminStorageLocationList'


class Admintoleranceclasschartlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    ltoneranceclassid = models.BigIntegerField(db_column='lToneranceClassID', blank=True, null=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbasicsizemin = models.FloatField(db_column='dBasicSizemin', blank=True, null=True)  # Field name made lowercase.
    dbasicsizemax = models.FloatField(db_column='dBasicSizeMax', blank=True, null=True)  # Field name made lowercase.
    dtolmax = models.FloatField(db_column='dTolMax', blank=True, null=True)  # Field name made lowercase.
    dtolmin = models.FloatField(db_column='dTolMin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceClassChartList'


class Admintoleranceclasslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    stoleranceclass = models.CharField(db_column='stoleranceClass', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminToleranceClassList'


class Admintolerancedialgaugelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
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
    lplantid = models.BigAutoField(db_column='lPlantId', primary_key=True)  # Field name made lowercase.
    splantno = models.CharField(db_column='sPlantNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splantname = models.CharField(db_column='sPlantName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='sCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    sccname = models.CharField(db_column='sCCName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd = models.CharField(db_column='sCCEMailAdd', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname1 = models.CharField(db_column='sCCName1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd1 = models.CharField(db_column='sCCEMailAdd1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname2 = models.CharField(db_column='sCCName2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd2 = models.CharField(db_column='sCCEMailAdd2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname3 = models.CharField(db_column='sCCName3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd3 = models.CharField(db_column='sCCEMailAdd3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname4 = models.CharField(db_column='sCCName4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd4 = models.CharField(db_column='sCCEMailAdd4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname5 = models.CharField(db_column='sCCName5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd5 = models.CharField(db_column='sCCEMailAdd5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname6 = models.CharField(db_column='sCCName6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd6 = models.CharField(db_column='sCCEMailAdd6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname7 = models.CharField(db_column='sCCName7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd7 = models.CharField(db_column='sCCEMailAdd7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname8 = models.CharField(db_column='sCCName8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd8 = models.CharField(db_column='sCCEMailAdd8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname9 = models.CharField(db_column='sCCName9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd9 = models.CharField(db_column='sCCEMailAdd9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccname10 = models.CharField(db_column='sCCName10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sccemailadd10 = models.CharField(db_column='sCCEMailAdd10', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUnitList'


class Adminunitofmeasurelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sunitofmeasure = models.CharField(db_column='sUnitofMeasure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sshort = models.CharField(db_column='sShort', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompantname = models.CharField(db_column='sCompantName', max_length=650, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminUnitofMeasureList'


class Adminuseraccesslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    luserid = models.BigIntegerField(db_column='lUserId', blank=True, null=True)  # Field name made lowercase.
    semployeename = models.CharField(db_column='sEmployeeName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    semployeeno = models.CharField(db_column='sEmployeeNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lunitid = models.BigIntegerField(db_column='lUnitId', blank=True, null=True)  # Field name made lowercase.
    sunitno = models.CharField(db_column='sUnitNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sunitname = models.CharField(db_column='sUnitName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
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
    luserid = models.BigAutoField(db_column='lUserId', primary_key=True)  # Field name made lowercase.
    semployeename = models.CharField(db_column='sEmployeeName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    semployeeno = models.CharField(db_column='sEmployeeNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    badmin = models.BooleanField(db_column='bAdmin', blank=True, null=True)  # Field name made lowercase.
    boperator = models.BooleanField(db_column='bOperator', blank=True, null=True)  # Field name made lowercase.
    bmasterlistonlyallplant = models.BooleanField(db_column='bMasterListOnlyAllPlant', blank=True, null=True)  # Field name made lowercase.
    bchangepassword = models.BooleanField(db_column='bChangePassword', blank=True, null=True)  # Field name made lowercase.
    lunitid = models.BigIntegerField(db_column='lUnitId', blank=True, null=True)  # Field name made lowercase.
    sunitno = models.CharField(db_column='sUnitNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sunitname = models.CharField(db_column='sUnitName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lroleid = models.BigIntegerField(db_column='lRoleId', blank=True, null=True)  # Field name made lowercase.
    srolename = models.CharField(db_column='sRoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lgradeid = models.BigIntegerField(db_column='lGradeId', blank=True, null=True)  # Field name made lowercase.
    sgradename = models.CharField(db_column='sGradeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcompanyid = models.BigIntegerField(db_column='lCompanyId', blank=True, null=True)  # Field name made lowercase.
    scompanyname = models.CharField(db_column='sCompanyName', max_length=650, blank=True, null=True)  # Field name made lowercase.
    semailaddress = models.CharField(db_column='sEmailAddress', max_length=350, blank=True, null=True)  # Field name made lowercase.
    bmatrix = models.BooleanField(db_column='bMatrix', blank=True, null=True)  # Field name made lowercase.
    lplant1 = models.BigIntegerField(db_column='lPlant1', blank=True, null=True)  # Field name made lowercase.
    bstores = models.BooleanField(db_column='bStores', blank=True, null=True)  # Field name made lowercase.
    bcalibration = models.BooleanField(db_column='bCalibration', blank=True, null=True)  # Field name made lowercase.
    bservice = models.BooleanField(db_column='bService', blank=True, null=True)  # Field name made lowercase.
    bmsa = models.BooleanField(db_column='bMSA', blank=True, null=True)  # Field name made lowercase.
    breadwrite = models.BooleanField(db_column='bReadWrite', blank=True, null=True)  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly', blank=True, null=True)  # Field name made lowercase.
    ballfeatures = models.BooleanField(db_column='bAllFeatures', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.
    lplant11 = models.BigIntegerField(db_column='lPlant11', blank=True, null=True)  # Field name made lowercase.
    bstores1 = models.BooleanField(db_column='bStores1', blank=True, null=True)  # Field name made lowercase.
    bcalibration1 = models.BooleanField(db_column='bCalibration1', blank=True, null=True)  # Field name made lowercase.
    bservice1 = models.BooleanField(db_column='bService1', blank=True, null=True)  # Field name made lowercase.
    bmsa1 = models.BooleanField(db_column='bMSA1', blank=True, null=True)  # Field name made lowercase.
    breadwrite1 = models.BooleanField(db_column='bReadWrite1', blank=True, null=True)  # Field name made lowercase.
    breadonly1 = models.BooleanField(db_column='bReadOnly1', blank=True, null=True)  # Field name made lowercase.
    ballfeatures1 = models.BooleanField(db_column='bAllFeatures1', blank=True, null=True)  # Field name made lowercase.
    bactive1 = models.BooleanField(db_column='bActive1', blank=True, null=True)  # Field name made lowercase.
    lplant12 = models.BigIntegerField(db_column='lPlant12', blank=True, null=True)  # Field name made lowercase.
    bstores2 = models.BooleanField(db_column='bStores2', blank=True, null=True)  # Field name made lowercase.
    bcalibration2 = models.BooleanField(db_column='bCalibration2', blank=True, null=True)  # Field name made lowercase.
    bservice2 = models.BooleanField(db_column='bService2', blank=True, null=True)  # Field name made lowercase.
    bmsa2 = models.BooleanField(db_column='bMSA2', blank=True, null=True)  # Field name made lowercase.
    breadwrite2 = models.BooleanField(db_column='bReadWrite2', blank=True, null=True)  # Field name made lowercase.
    breadonly2 = models.BooleanField(db_column='bReadOnly2', blank=True, null=True)  # Field name made lowercase.
    ballfeatures2 = models.BooleanField(db_column='bAllFeatures2', blank=True, null=True)  # Field name made lowercase.
    bactive2 = models.BooleanField(db_column='bActive2', blank=True, null=True)  # Field name made lowercase.
    lplant13 = models.BigIntegerField(db_column='lPlant13', blank=True, null=True)  # Field name made lowercase.
    bstores3 = models.BooleanField(db_column='bStores3', blank=True, null=True)  # Field name made lowercase.
    bcalibration3 = models.BooleanField(db_column='bCalibration3', blank=True, null=True)  # Field name made lowercase.
    bservice3 = models.BooleanField(db_column='bService3', blank=True, null=True)  # Field name made lowercase.
    bmsa3 = models.BooleanField(db_column='bMSA3', blank=True, null=True)  # Field name made lowercase.
    breadwrite3 = models.BooleanField(db_column='bReadWrite3', blank=True, null=True)  # Field name made lowercase.
    breadonly3 = models.BooleanField(db_column='bReadOnly3', blank=True, null=True)  # Field name made lowercase.
    ballfeatures3 = models.BooleanField(db_column='bAllFeatures3', blank=True, null=True)  # Field name made lowercase.
    bactive3 = models.BooleanField(db_column='bActive3', blank=True, null=True)  # Field name made lowercase.
    lplant14 = models.BigIntegerField(db_column='lPlant14', blank=True, null=True)  # Field name made lowercase.
    bstores4 = models.BooleanField(db_column='bStores4', blank=True, null=True)  # Field name made lowercase.
    bcalibration4 = models.BooleanField(db_column='bCalibration4', blank=True, null=True)  # Field name made lowercase.
    bservice4 = models.BooleanField(db_column='bService4', blank=True, null=True)  # Field name made lowercase.
    bmsa4 = models.BooleanField(db_column='bMSA4', blank=True, null=True)  # Field name made lowercase.
    breadwrite4 = models.BooleanField(db_column='bReadWrite4', blank=True, null=True)  # Field name made lowercase.
    breadonly4 = models.BooleanField(db_column='bReadOnly4', blank=True, null=True)  # Field name made lowercase.
    ballfeatures4 = models.BooleanField(db_column='bAllFeatures4', blank=True, null=True)  # Field name made lowercase.
    bactive4 = models.BooleanField(db_column='bActive4', blank=True, null=True)  # Field name made lowercase.
    lplant15 = models.BigIntegerField(db_column='lPlant15', blank=True, null=True)  # Field name made lowercase.
    bstores5 = models.BooleanField(db_column='bStores5', blank=True, null=True)  # Field name made lowercase.
    bcalibration5 = models.BooleanField(db_column='bCalibration5', blank=True, null=True)  # Field name made lowercase.
    bservice5 = models.BooleanField(db_column='bService5', blank=True, null=True)  # Field name made lowercase.
    bmsa5 = models.BooleanField(db_column='bMSA5', blank=True, null=True)  # Field name made lowercase.
    breadwrite5 = models.BooleanField(db_column='bReadWrite5', blank=True, null=True)  # Field name made lowercase.
    breadonly5 = models.BooleanField(db_column='bReadOnly5', blank=True, null=True)  # Field name made lowercase.
    ballfeatures5 = models.BooleanField(db_column='bAllFeatures5', blank=True, null=True)  # Field name made lowercase.
    bactive5 = models.BooleanField(db_column='bActive5', blank=True, null=True)  # Field name made lowercase.
    lplant16 = models.BigIntegerField(db_column='lPlant16', blank=True, null=True)  # Field name made lowercase.
    bstores6 = models.BooleanField(db_column='bStores6', blank=True, null=True)  # Field name made lowercase.
    bcalibration6 = models.BooleanField(db_column='bCalibration6', blank=True, null=True)  # Field name made lowercase.
    bservice6 = models.BooleanField(db_column='bService6', blank=True, null=True)  # Field name made lowercase.
    bmsa6 = models.BooleanField(db_column='bMSA6', blank=True, null=True)  # Field name made lowercase.
    breadwrite6 = models.BooleanField(db_column='bReadWrite6', blank=True, null=True)  # Field name made lowercase.
    breadonly6 = models.BooleanField(db_column='bReadOnly6', blank=True, null=True)  # Field name made lowercase.
    ballfeatures6 = models.BooleanField(db_column='bAllFeatures6', blank=True, null=True)  # Field name made lowercase.
    bactive6 = models.BooleanField(db_column='bActive6', blank=True, null=True)  # Field name made lowercase.
    lplant17 = models.BigIntegerField(db_column='lPlant17', blank=True, null=True)  # Field name made lowercase.
    bstores7 = models.BooleanField(db_column='bStores7', blank=True, null=True)  # Field name made lowercase.
    bcalibration7 = models.BooleanField(db_column='bCalibration7', blank=True, null=True)  # Field name made lowercase.
    bservice7 = models.BooleanField(db_column='bService7', blank=True, null=True)  # Field name made lowercase.
    bmsa7 = models.BooleanField(db_column='bMSA7', blank=True, null=True)  # Field name made lowercase.
    breadwrite7 = models.BooleanField(db_column='bReadWrite7', blank=True, null=True)  # Field name made lowercase.
    breadonly7 = models.BooleanField(db_column='bReadOnly7', blank=True, null=True)  # Field name made lowercase.
    ballfeatures7 = models.BooleanField(db_column='bAllFeatures7', blank=True, null=True)  # Field name made lowercase.
    bactive7 = models.BooleanField(db_column='bActive7', blank=True, null=True)  # Field name made lowercase.
    lplant18 = models.BigIntegerField(db_column='lPlant18', blank=True, null=True)  # Field name made lowercase.
    bstores8 = models.BooleanField(db_column='bStores8', blank=True, null=True)  # Field name made lowercase.
    bcalibration8 = models.BooleanField(db_column='bCalibration8', blank=True, null=True)  # Field name made lowercase.
    bservice8 = models.BooleanField(db_column='bService8', blank=True, null=True)  # Field name made lowercase.
    bmsa8 = models.BooleanField(db_column='bMSA8', blank=True, null=True)  # Field name made lowercase.
    breadwrite8 = models.BooleanField(db_column='bReadWrite8', blank=True, null=True)  # Field name made lowercase.
    breadonly8 = models.BooleanField(db_column='bReadOnly8', blank=True, null=True)  # Field name made lowercase.
    ballfeatures8 = models.BooleanField(db_column='bAllFeatures8', blank=True, null=True)  # Field name made lowercase.
    bactive8 = models.BooleanField(db_column='bActive8', blank=True, null=True)  # Field name made lowercase.
    lplant19 = models.BigIntegerField(db_column='lPlant19', blank=True, null=True)  # Field name made lowercase.
    bstores9 = models.BooleanField(db_column='bStores9', blank=True, null=True)  # Field name made lowercase.
    bcalibration9 = models.BooleanField(db_column='bCalibration9', blank=True, null=True)  # Field name made lowercase.
    bservice9 = models.BooleanField(db_column='bService9', blank=True, null=True)  # Field name made lowercase.
    bmsa9 = models.BooleanField(db_column='bMSA9', blank=True, null=True)  # Field name made lowercase.
    breadwrite9 = models.BooleanField(db_column='bReadWrite9', blank=True, null=True)  # Field name made lowercase.
    breadonly9 = models.BooleanField(db_column='bReadOnly9', blank=True, null=True)  # Field name made lowercase.
    ballfeatures9 = models.BooleanField(db_column='bAllFeatures9', blank=True, null=True)  # Field name made lowercase.
    bactive9 = models.BooleanField(db_column='bActive9', blank=True, null=True)  # Field name made lowercase.
    lplant110 = models.BigIntegerField(db_column='lPlant110', blank=True, null=True)  # Field name made lowercase.
    bstores10 = models.BooleanField(db_column='bStores10', blank=True, null=True)  # Field name made lowercase.
    bcalibration10 = models.BooleanField(db_column='bCalibration10', blank=True, null=True)  # Field name made lowercase.
    bservice10 = models.BooleanField(db_column='bService10', blank=True, null=True)  # Field name made lowercase.
    bmsa10 = models.BooleanField(db_column='bMSA10', blank=True, null=True)  # Field name made lowercase.
    breadwrite10 = models.BooleanField(db_column='bReadWrite10', blank=True, null=True)  # Field name made lowercase.
    breadonly10 = models.BooleanField(db_column='bReadOnly10', blank=True, null=True)  # Field name made lowercase.
    ballfeatures10 = models.BooleanField(db_column='bAllFeatures10', blank=True, null=True)  # Field name made lowercase.
    bactive10 = models.BooleanField(db_column='bActive10', blank=True, null=True)  # Field name made lowercase.
    lplant111 = models.BigIntegerField(db_column='lPlant111', blank=True, null=True)  # Field name made lowercase.
    bstores11 = models.BooleanField(db_column='bStores11', blank=True, null=True)  # Field name made lowercase.
    bcalibration11 = models.BooleanField(db_column='bCalibration11', blank=True, null=True)  # Field name made lowercase.
    bservice11 = models.BooleanField(db_column='bService11', blank=True, null=True)  # Field name made lowercase.
    bmsa11 = models.BooleanField(db_column='bMSA11', blank=True, null=True)  # Field name made lowercase.
    breadwrite11 = models.BooleanField(db_column='bReadWrite11', blank=True, null=True)  # Field name made lowercase.
    breadonly11 = models.BooleanField(db_column='bReadOnly11', blank=True, null=True)  # Field name made lowercase.
    ballfeatures11 = models.BooleanField(db_column='bAllFeatures11', blank=True, null=True)  # Field name made lowercase.
    bactive11 = models.BooleanField(db_column='bActive11', blank=True, null=True)  # Field name made lowercase.
    lplant112 = models.BigIntegerField(db_column='lPlant112', blank=True, null=True)  # Field name made lowercase.
    bstores12 = models.BooleanField(db_column='bStores12', blank=True, null=True)  # Field name made lowercase.
    bcalibration12 = models.BooleanField(db_column='bCalibration12', blank=True, null=True)  # Field name made lowercase.
    bservice12 = models.BooleanField(db_column='bService12', blank=True, null=True)  # Field name made lowercase.
    bmsa12 = models.BooleanField(db_column='bMSA12', blank=True, null=True)  # Field name made lowercase.
    breadwrite12 = models.BooleanField(db_column='bReadWrite12', blank=True, null=True)  # Field name made lowercase.
    breadonly12 = models.BooleanField(db_column='bReadOnly12', blank=True, null=True)  # Field name made lowercase.
    ballfeatures12 = models.BooleanField(db_column='bAllFeatures12', blank=True, null=True)  # Field name made lowercase.
    bactive12 = models.BooleanField(db_column='bActive12', blank=True, null=True)  # Field name made lowercase.
    lplant113 = models.BigIntegerField(db_column='lPlant113', blank=True, null=True)  # Field name made lowercase.
    bstores13 = models.BooleanField(db_column='bStores13', blank=True, null=True)  # Field name made lowercase.
    bcalibration13 = models.BooleanField(db_column='bCalibration13', blank=True, null=True)  # Field name made lowercase.
    bservice13 = models.BooleanField(db_column='bService13', blank=True, null=True)  # Field name made lowercase.
    bmsa13 = models.BooleanField(db_column='bMSA13', blank=True, null=True)  # Field name made lowercase.
    breadwrite13 = models.BooleanField(db_column='bReadWrite13', blank=True, null=True)  # Field name made lowercase.
    breadonly13 = models.BooleanField(db_column='bReadOnly13', blank=True, null=True)  # Field name made lowercase.
    ballfeatures13 = models.BooleanField(db_column='bAllFeatures13', blank=True, null=True)  # Field name made lowercase.
    bactive13 = models.BooleanField(db_column='bActive13', blank=True, null=True)  # Field name made lowercase.
    lplant114 = models.BigIntegerField(db_column='lPlant114', blank=True, null=True)  # Field name made lowercase.
    bstores14 = models.BooleanField(db_column='bStores14', blank=True, null=True)  # Field name made lowercase.
    bcalibration14 = models.BooleanField(db_column='bCalibration14', blank=True, null=True)  # Field name made lowercase.
    bservice14 = models.BooleanField(db_column='bService14', blank=True, null=True)  # Field name made lowercase.
    bmsa14 = models.BooleanField(db_column='bMSA14', blank=True, null=True)  # Field name made lowercase.
    breadwrite14 = models.BooleanField(db_column='bReadWrite14', blank=True, null=True)  # Field name made lowercase.
    breadonly14 = models.BooleanField(db_column='bReadOnly14', blank=True, null=True)  # Field name made lowercase.
    ballfeatures14 = models.BooleanField(db_column='bAllFeatures14', blank=True, null=True)  # Field name made lowercase.
    bactive14 = models.BooleanField(db_column='bActive14', blank=True, null=True)  # Field name made lowercase.
    lplant115 = models.BigIntegerField(db_column='lPlant115', blank=True, null=True)  # Field name made lowercase.
    bstores15 = models.BooleanField(db_column='bStores15', blank=True, null=True)  # Field name made lowercase.
    bcalibration15 = models.BooleanField(db_column='bCalibration15', blank=True, null=True)  # Field name made lowercase.
    bservice15 = models.BooleanField(db_column='bService15', blank=True, null=True)  # Field name made lowercase.
    bmsa15 = models.BooleanField(db_column='bMSA15', blank=True, null=True)  # Field name made lowercase.
    breadwrite15 = models.BooleanField(db_column='bReadWrite15', blank=True, null=True)  # Field name made lowercase.
    breadonly15 = models.BooleanField(db_column='bReadOnly15', blank=True, null=True)  # Field name made lowercase.
    ballfeatures15 = models.BooleanField(db_column='bAllFeatures15', blank=True, null=True)  # Field name made lowercase.
    bactive15 = models.BooleanField(db_column='bActive15', blank=True, null=True)  # Field name made lowercase.
    lplant116 = models.BigIntegerField(db_column='lPlant116', blank=True, null=True)  # Field name made lowercase.
    bstores16 = models.BooleanField(db_column='bStores16', blank=True, null=True)  # Field name made lowercase.
    bcalibration16 = models.BooleanField(db_column='bCalibration16', blank=True, null=True)  # Field name made lowercase.
    bservice16 = models.BooleanField(db_column='bService16', blank=True, null=True)  # Field name made lowercase.
    bmsa16 = models.BooleanField(db_column='bMSA16', blank=True, null=True)  # Field name made lowercase.
    breadwrite16 = models.BooleanField(db_column='bReadWrite16', blank=True, null=True)  # Field name made lowercase.
    breadonly16 = models.BooleanField(db_column='bReadOnly16', blank=True, null=True)  # Field name made lowercase.
    ballfeatures16 = models.BooleanField(db_column='bAllFeatures16', blank=True, null=True)  # Field name made lowercase.
    bactive16 = models.BooleanField(db_column='bActive16', blank=True, null=True)  # Field name made lowercase.
    lplant117 = models.BigIntegerField(db_column='lPlant117', blank=True, null=True)  # Field name made lowercase.
    bstores17 = models.BooleanField(db_column='bStores17', blank=True, null=True)  # Field name made lowercase.
    bcalibration17 = models.BooleanField(db_column='bCalibration17', blank=True, null=True)  # Field name made lowercase.
    bservice17 = models.BooleanField(db_column='bService17', blank=True, null=True)  # Field name made lowercase.
    bmsa17 = models.BooleanField(db_column='bMSA17', blank=True, null=True)  # Field name made lowercase.
    breadwrite17 = models.BooleanField(db_column='bReadWrite17', blank=True, null=True)  # Field name made lowercase.
    breadonly17 = models.BooleanField(db_column='bReadOnly17', blank=True, null=True)  # Field name made lowercase.
    ballfeatures17 = models.BooleanField(db_column='bAllFeatures17', blank=True, null=True)  # Field name made lowercase.
    bactive17 = models.BooleanField(db_column='bActive17', blank=True, null=True)  # Field name made lowercase.
    lplant118 = models.BigIntegerField(db_column='lPlant118', blank=True, null=True)  # Field name made lowercase.
    bstores18 = models.BooleanField(db_column='bStores18', blank=True, null=True)  # Field name made lowercase.
    bcalibration18 = models.BooleanField(db_column='bCalibration18', blank=True, null=True)  # Field name made lowercase.
    bservice18 = models.BooleanField(db_column='bService18', blank=True, null=True)  # Field name made lowercase.
    bmsa18 = models.BooleanField(db_column='bMSA18', blank=True, null=True)  # Field name made lowercase.
    breadwrite18 = models.BooleanField(db_column='bReadWrite18', blank=True, null=True)  # Field name made lowercase.
    breadonly18 = models.BooleanField(db_column='bReadOnly18', blank=True, null=True)  # Field name made lowercase.
    ballfeatures18 = models.BooleanField(db_column='bAllFeatures18', blank=True, null=True)  # Field name made lowercase.
    bactive18 = models.BooleanField(db_column='bActive18', blank=True, null=True)  # Field name made lowercase.
    lplant119 = models.BigIntegerField(db_column='lPlant119', blank=True, null=True)  # Field name made lowercase.
    bstores19 = models.BooleanField(db_column='bStores19', blank=True, null=True)  # Field name made lowercase.
    bcalibration19 = models.BooleanField(db_column='bCalibration19', blank=True, null=True)  # Field name made lowercase.
    bservice19 = models.BooleanField(db_column='bService19', blank=True, null=True)  # Field name made lowercase.
    bmsa19 = models.BooleanField(db_column='bMSA19', blank=True, null=True)  # Field name made lowercase.
    breadwrite19 = models.BooleanField(db_column='bReadWrite19', blank=True, null=True)  # Field name made lowercase.
    breadonly19 = models.BooleanField(db_column='bReadOnly19', blank=True, null=True)  # Field name made lowercase.
    ballfeatures19 = models.BooleanField(db_column='bAllFeatures19', blank=True, null=True)  # Field name made lowercase.
    bactive19 = models.BooleanField(db_column='bActive19', blank=True, null=True)  # Field name made lowercase.
    lplant120 = models.BigIntegerField(db_column='lPlant120', blank=True, null=True)  # Field name made lowercase.
    bstores20 = models.BooleanField(db_column='bStores20', blank=True, null=True)  # Field name made lowercase.
    bcalibration20 = models.BooleanField(db_column='bCalibration20', blank=True, null=True)  # Field name made lowercase.
    bservice20 = models.BooleanField(db_column='bService20', blank=True, null=True)  # Field name made lowercase.
    bmsa20 = models.BooleanField(db_column='bMSA20', blank=True, null=True)  # Field name made lowercase.
    breadwrite20 = models.BooleanField(db_column='bReadWrite20', blank=True, null=True)  # Field name made lowercase.
    breadonly20 = models.BooleanField(db_column='bReadOnly20', blank=True, null=True)  # Field name made lowercase.
    ballfeatures20 = models.BooleanField(db_column='bAllFeatures20', blank=True, null=True)  # Field name made lowercase.
    bactive20 = models.BooleanField(db_column='bActive20', blank=True, null=True)  # Field name made lowercase.
    lplant121 = models.BigIntegerField(db_column='lPlant121', blank=True, null=True)  # Field name made lowercase.
    bstores21 = models.BooleanField(db_column='bStores21', blank=True, null=True)  # Field name made lowercase.
    bcalibration21 = models.BooleanField(db_column='bCalibration21', blank=True, null=True)  # Field name made lowercase.
    bservice21 = models.BooleanField(db_column='bService21', blank=True, null=True)  # Field name made lowercase.
    bmsa21 = models.BooleanField(db_column='bMSA21', blank=True, null=True)  # Field name made lowercase.
    breadwrite21 = models.BooleanField(db_column='bReadWrite21', blank=True, null=True)  # Field name made lowercase.
    breadonly21 = models.BooleanField(db_column='bReadOnly21', blank=True, null=True)  # Field name made lowercase.
    ballfeatures21 = models.BooleanField(db_column='bAllFeatures21', blank=True, null=True)  # Field name made lowercase.
    bactive21 = models.BooleanField(db_column='bActive21', blank=True, null=True)  # Field name made lowercase.
    lplant122 = models.BigIntegerField(db_column='lPlant122', blank=True, null=True)  # Field name made lowercase.
    bstores22 = models.BooleanField(db_column='bStores22', blank=True, null=True)  # Field name made lowercase.
    bcalibration22 = models.BooleanField(db_column='bCalibration22', blank=True, null=True)  # Field name made lowercase.
    bservice22 = models.BooleanField(db_column='bService22', blank=True, null=True)  # Field name made lowercase.
    bmsa22 = models.BooleanField(db_column='bMSA22', blank=True, null=True)  # Field name made lowercase.
    breadwrite22 = models.BooleanField(db_column='bReadWrite22', blank=True, null=True)  # Field name made lowercase.
    breadonly22 = models.BooleanField(db_column='bReadOnly22', blank=True, null=True)  # Field name made lowercase.
    ballfeatures22 = models.BooleanField(db_column='bAllFeatures22', blank=True, null=True)  # Field name made lowercase.
    bactive22 = models.BooleanField(db_column='bActive22', blank=True, null=True)  # Field name made lowercase.
    lplant123 = models.BigIntegerField(db_column='lPlant123', blank=True, null=True)  # Field name made lowercase.
    bstores23 = models.BooleanField(db_column='bStores23', blank=True, null=True)  # Field name made lowercase.
    bcalibration23 = models.BooleanField(db_column='bCalibration23', blank=True, null=True)  # Field name made lowercase.
    bservice23 = models.BooleanField(db_column='bService23', blank=True, null=True)  # Field name made lowercase.
    bmsa23 = models.BooleanField(db_column='bMSA23', blank=True, null=True)  # Field name made lowercase.
    breadwrite23 = models.BooleanField(db_column='bReadWrite23', blank=True, null=True)  # Field name made lowercase.
    breadonly23 = models.BooleanField(db_column='bReadOnly23', blank=True, null=True)  # Field name made lowercase.
    ballfeatures23 = models.BooleanField(db_column='bAllFeatures23', blank=True, null=True)  # Field name made lowercase.
    bactive23 = models.BooleanField(db_column='bActive23', blank=True, null=True)  # Field name made lowercase.
    lplant124 = models.BigIntegerField(db_column='lPlant124', blank=True, null=True)  # Field name made lowercase.
    bstores24 = models.BooleanField(db_column='bStores24', blank=True, null=True)  # Field name made lowercase.
    bcalibration24 = models.BooleanField(db_column='bCalibration24', blank=True, null=True)  # Field name made lowercase.
    bservice24 = models.BooleanField(db_column='bService24', blank=True, null=True)  # Field name made lowercase.
    bmsa24 = models.BooleanField(db_column='bMSA24', blank=True, null=True)  # Field name made lowercase.
    breadwrite24 = models.BooleanField(db_column='bReadWrite24', blank=True, null=True)  # Field name made lowercase.
    breadonly24 = models.BooleanField(db_column='bReadOnly24', blank=True, null=True)  # Field name made lowercase.
    ballfeatures24 = models.BooleanField(db_column='bAllFeatures24', blank=True, null=True)  # Field name made lowercase.
    bactive24 = models.BooleanField(db_column='bActive24', blank=True, null=True)  # Field name made lowercase.
    lplant125 = models.BigIntegerField(db_column='lPlant125', blank=True, null=True)  # Field name made lowercase.
    bstores25 = models.BooleanField(db_column='bStores25', blank=True, null=True)  # Field name made lowercase.
    bcalibration25 = models.BooleanField(db_column='bCalibration25', blank=True, null=True)  # Field name made lowercase.
    bservice25 = models.BooleanField(db_column='bService25', blank=True, null=True)  # Field name made lowercase.
    bmsa25 = models.BooleanField(db_column='bMSA25', blank=True, null=True)  # Field name made lowercase.
    breadwrite25 = models.BooleanField(db_column='bReadWrite25', blank=True, null=True)  # Field name made lowercase.
    breadonly25 = models.BooleanField(db_column='bReadOnly25', blank=True, null=True)  # Field name made lowercase.
    ballfeatures25 = models.BooleanField(db_column='bAllFeatures25', blank=True, null=True)  # Field name made lowercase.
    bactive25 = models.BooleanField(db_column='bActive25', blank=True, null=True)  # Field name made lowercase.
    lplant126 = models.BigIntegerField(db_column='lPlant126', blank=True, null=True)  # Field name made lowercase.
    bstores26 = models.BooleanField(db_column='bStores26', blank=True, null=True)  # Field name made lowercase.
    bcalibration26 = models.BooleanField(db_column='bCalibration26', blank=True, null=True)  # Field name made lowercase.
    bservice26 = models.BooleanField(db_column='bService26', blank=True, null=True)  # Field name made lowercase.
    bmsa26 = models.BooleanField(db_column='bMSA26', blank=True, null=True)  # Field name made lowercase.
    breadwrite26 = models.BooleanField(db_column='bReadWrite26', blank=True, null=True)  # Field name made lowercase.
    breadonly26 = models.BooleanField(db_column='bReadOnly26', blank=True, null=True)  # Field name made lowercase.
    ballfeatures26 = models.BooleanField(db_column='bAllFeatures26', blank=True, null=True)  # Field name made lowercase.
    bactive26 = models.BooleanField(db_column='bActive26', blank=True, null=True)  # Field name made lowercase.
    lplant127 = models.BigIntegerField(db_column='lPlant127', blank=True, null=True)  # Field name made lowercase.
    bstores27 = models.BooleanField(db_column='bStores27', blank=True, null=True)  # Field name made lowercase.
    bcalibration27 = models.BooleanField(db_column='bCalibration27', blank=True, null=True)  # Field name made lowercase.
    bservice27 = models.BooleanField(db_column='bService27', blank=True, null=True)  # Field name made lowercase.
    bmsa27 = models.BooleanField(db_column='bMSA27', blank=True, null=True)  # Field name made lowercase.
    breadwrite27 = models.BooleanField(db_column='bReadWrite27', blank=True, null=True)  # Field name made lowercase.
    breadonly27 = models.BooleanField(db_column='bReadOnly27', blank=True, null=True)  # Field name made lowercase.
    ballfeatures27 = models.BooleanField(db_column='bAllFeatures27', blank=True, null=True)  # Field name made lowercase.
    bactive27 = models.BooleanField(db_column='bActive27', blank=True, null=True)  # Field name made lowercase.
    lplant128 = models.BigIntegerField(db_column='lPlant128', blank=True, null=True)  # Field name made lowercase.
    bstores28 = models.BooleanField(db_column='bStores28', blank=True, null=True)  # Field name made lowercase.
    bcalibration28 = models.BooleanField(db_column='bCalibration28', blank=True, null=True)  # Field name made lowercase.
    bservice28 = models.BooleanField(db_column='bService28', blank=True, null=True)  # Field name made lowercase.
    bmsa28 = models.BooleanField(db_column='bMSA28', blank=True, null=True)  # Field name made lowercase.
    breadwrite28 = models.BooleanField(db_column='bReadWrite28', blank=True, null=True)  # Field name made lowercase.
    breadonly28 = models.BooleanField(db_column='bReadOnly28', blank=True, null=True)  # Field name made lowercase.
    ballfeatures28 = models.BooleanField(db_column='bAllFeatures28', blank=True, null=True)  # Field name made lowercase.
    bactive28 = models.BooleanField(db_column='bActive28', blank=True, null=True)  # Field name made lowercase.
    lplant129 = models.BigIntegerField(db_column='lPlant129', blank=True, null=True)  # Field name made lowercase.
    bstores29 = models.BooleanField(db_column='bStores29', blank=True, null=True)  # Field name made lowercase.
    bcalibration29 = models.BooleanField(db_column='bCalibration29', blank=True, null=True)  # Field name made lowercase.
    bservice29 = models.BooleanField(db_column='bService29', blank=True, null=True)  # Field name made lowercase.
    bmsa29 = models.BooleanField(db_column='bMSA29', blank=True, null=True)  # Field name made lowercase.
    breadwrite29 = models.BooleanField(db_column='bReadWrite29', blank=True, null=True)  # Field name made lowercase.
    breadonly29 = models.BooleanField(db_column='bReadOnly29', blank=True, null=True)  # Field name made lowercase.
    ballfeatures29 = models.BooleanField(db_column='bAllFeatures29', blank=True, null=True)  # Field name made lowercase.
    bactive29 = models.BooleanField(db_column='bActive29', blank=True, null=True)  # Field name made lowercase.
    lplant130 = models.BigIntegerField(db_column='lPlant130', blank=True, null=True)  # Field name made lowercase.
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
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type_id = models.BigIntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
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
    user_id = models.BigIntegerField()
    group_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.CharField(max_length=700, blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.CharField(max_length=700)
    content_type_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.CharField(max_length=700)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
