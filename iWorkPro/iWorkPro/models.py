# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Projectdoclist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectid = models.BigIntegerField(db_column='lProjectId', blank=True, null=True)  # Field name made lowercase.
    lsubprojectid = models.BigIntegerField(db_column='lsubProjectID', blank=True, null=True)  # Field name made lowercase.
    lprojecttaskid = models.BigIntegerField(db_column='lProjectTaskId', blank=True, null=True)  # Field name made lowercase.
    sfiledesc = models.CharField(db_column='sFileDesc', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sfilename = models.CharField(db_column='sFileName', max_length=290, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectDocList'


class Projectmainlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectno = models.BigIntegerField(db_column='lProjectNo', blank=True, null=True)  # Field name made lowercase.
    lprojectsubnocount = models.BigIntegerField(db_column='lProjectSubNoCount', blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.BigIntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid = models.BigIntegerField(db_column='lProjectOwnerID', blank=True, null=True)  # Field name made lowercase.
    ltotalsubproject = models.IntegerField(db_column='lTotalSubProject', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojectopen = models.IntegerField(db_column='lTotalSubProjectOpen', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojectclosed = models.IntegerField(db_column='lTotalSubProjectClosed', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojecttask = models.IntegerField(db_column='lTotalSubProjectTask', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojectopentask = models.IntegerField(db_column='lTotalSubProjectOpenTask', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojectclosedtask = models.IntegerField(db_column='lTotalSubProjectClosedTask', blank=True, null=True)  # Field name made lowercase.
    bclosed = models.IntegerField(db_column='bClosed', blank=True, null=True)  # Field name made lowercase.
    bcompleted = models.IntegerField(db_column='bCompleted', blank=True, null=True)  # Field name made lowercase.
    bdiscarded = models.IntegerField(db_column='bDiscarded', blank=True, null=True)  # Field name made lowercase.
    bstoppedtemporary = models.IntegerField(db_column='bStoppedTemporary', blank=True, null=True)  # Field name made lowercase.
    lplannedtotalhours = models.IntegerField(db_column='lPlannedTotalHours', blank=True, null=True)  # Field name made lowercase.
    lactualtotalhours = models.IntegerField(db_column='lActualTotalHours', blank=True, null=True)  # Field name made lowercase.
    dtcreatedon = models.DateTimeField(db_column='dtCreatedOn', blank=True, null=True)  # Field name made lowercase.
    dtclosedon = models.DateTimeField(db_column='dtClosedOn', blank=True, null=True)  # Field name made lowercase.
    dtplannedstarton = models.DateTimeField(db_column='dtPlannedStartOn', blank=True, null=True)  # Field name made lowercase.
    dtplannedendon = models.DateTimeField(db_column='dtPlannedEndOn', blank=True, null=True)  # Field name made lowercase.
    sprojectno = models.CharField(db_column='sProjectNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    screatedon = models.CharField(db_column='sCreatedOn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scompletedon = models.CharField(db_column='sCompletedOn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splannedstarton = models.CharField(db_column='sPlannedStartOn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splannedendon = models.CharField(db_column='sPlannedEndOn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sprojectowner = models.CharField(db_column='sProjectOwner', max_length=280, blank=True, null=True)  # Field name made lowercase.
    bcustomervisible = models.IntegerField(db_column='bCustomerVisible', blank=True, null=True)  # Field name made lowercase.
    lcustomerpriority = models.CharField(db_column='lCustomerPriority', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lcategoryid = models.BigIntegerField(db_column='lCategoryID', blank=True, null=True)  # Field name made lowercase.
    scategory = models.CharField(db_column='sCategory', max_length=280, blank=True, null=True)  # Field name made lowercase.
    btaststarted = models.IntegerField(db_column='bTastStarted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectMainList'


class Projectsublist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectid = models.BigIntegerField(db_column='lProjectId', blank=True, null=True)  # Field name made lowercase.
    lprojectsubno = models.BigIntegerField(db_column='lProjectSubNo', blank=True, null=True)  # Field name made lowercase.
    lprojectsubtasknocount = models.BigIntegerField(db_column='lProjectSubTaskNoCount', blank=True, null=True)  # Field name made lowercase.
    lcategoryid = models.BigIntegerField(db_column='lCategoryId', blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.BigIntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid = models.BigIntegerField(db_column='lProjectOwnerID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid1 = models.BigIntegerField(db_column='lProjectOwnerID1', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid2 = models.BigIntegerField(db_column='lProjectOwnerID2', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid3 = models.BigIntegerField(db_column='lProjectOwnerID3', blank=True, null=True)  # Field name made lowercase.
    fplannedcost = models.FloatField(db_column='fPlannedCost', blank=True, null=True)  # Field name made lowercase.
    factualcost = models.FloatField(db_column='fActualCost', blank=True, null=True)  # Field name made lowercase.
    brequirementreceived = models.IntegerField(db_column='bRequirementReceived', blank=True, null=True)  # Field name made lowercase.
    bproposalgiven = models.IntegerField(db_column='bProposalGiven', blank=True, null=True)  # Field name made lowercase.
    bclosed = models.IntegerField(db_column='bClosed', blank=True, null=True)  # Field name made lowercase.
    bcompleted = models.IntegerField(db_column='bCompleted', blank=True, null=True)  # Field name made lowercase.
    bdiscarded = models.IntegerField(db_column='bDiscarded', blank=True, null=True)  # Field name made lowercase.
    bstoppedtemporary = models.IntegerField(db_column='bStoppedTemporary', blank=True, null=True)  # Field name made lowercase.
    bporecd = models.IntegerField(db_column='bPORecd', blank=True, null=True)  # Field name made lowercase.
    badvancerecd = models.IntegerField(db_column='bAdvanceRecd', blank=True, null=True)  # Field name made lowercase.
    bpaymentrecd = models.IntegerField(db_column='bPaymentRecd', blank=True, null=True)  # Field name made lowercase.
    bdesigncompleted = models.IntegerField(db_column='bDesignCompleted', blank=True, null=True)  # Field name made lowercase.
    bdevcompleted = models.IntegerField(db_column='bDevCompleted', blank=True, null=True)  # Field name made lowercase.
    bqualitycompleted = models.IntegerField(db_column='bQualityCompleted', blank=True, null=True)  # Field name made lowercase.
    bimplementcompleted = models.IntegerField(db_column='bImplementCompleted', blank=True, null=True)  # Field name made lowercase.
    busertestcompleted = models.IntegerField(db_column='bUserTestCompleted', blank=True, null=True)  # Field name made lowercase.
    blive = models.IntegerField(db_column='bLive', blank=True, null=True)  # Field name made lowercase.
    bbillable = models.IntegerField(db_column='bBillable', blank=True, null=True)  # Field name made lowercase.
    lplannedtotaltime = models.IntegerField(db_column='lPlannedTotalTime', blank=True, null=True)  # Field name made lowercase.
    lactualtotaltime = models.IntegerField(db_column='lActualTotalTime', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojecttask = models.IntegerField(db_column='lTotalSubProjectTask', blank=True, null=True)  # Field name made lowercase.
    ltotalsubprojectopentask = models.IntegerField(db_column='lTotalSubProjectOpenTask')  # Field name made lowercase.
    ltotalsubprojectclosedtask = models.IntegerField(db_column='lTotalSubProjectClosedTask', blank=True, null=True)  # Field name made lowercase.
    dtprojectstartdate = models.DateTimeField(db_column='dtProjectStartDate', blank=True, null=True)  # Field name made lowercase.
    dtprojectenddate = models.DateTimeField(db_column='dtProjectEndDate', blank=True, null=True)  # Field name made lowercase.
    dtreqrecddate = models.DateTimeField(db_column='dtReqRecdDate', blank=True, null=True)  # Field name made lowercase.
    dtproposaldate = models.DateTimeField(db_column='dtProposalDate', blank=True, null=True)  # Field name made lowercase.
    dtporecddate = models.DateTimeField(db_column='dtPORecdDate', blank=True, null=True)  # Field name made lowercase.
    badvancerecdon = models.DateTimeField(db_column='bAdvanceRecdOn', blank=True, null=True)  # Field name made lowercase.
    dtpaymentrecdon = models.DateTimeField(db_column='dtPaymentRecdOn', blank=True, null=True)  # Field name made lowercase.
    dtdesigncompletedon = models.DateTimeField(db_column='dtDesignCompletedOn', blank=True, null=True)  # Field name made lowercase.
    dtdevcompletedon = models.DateTimeField(db_column='dtDevCompletedOn', blank=True, null=True)  # Field name made lowercase.
    dtqualitycompletedon = models.DateTimeField(db_column='dtQualityCompletedOn', blank=True, null=True)  # Field name made lowercase.
    dtimplementcompletedon = models.DateTimeField(db_column='dtImplementCompletedOn', blank=True, null=True)  # Field name made lowercase.
    dtusertestcompletedon = models.DateTimeField(db_column='dtUserTestCompletedOn', blank=True, null=True)  # Field name made lowercase.
    bliveon = models.DateTimeField(db_column='bLiveOn', blank=True, null=True)  # Field name made lowercase.
    sprojectsubno = models.CharField(db_column='sProjectSubNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssubprojectname = models.CharField(db_column='sSubProjectName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectname = models.CharField(db_column='sProjectName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    scategoryname = models.CharField(db_column='sCategoryName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner = models.CharField(db_column='sProjectOwner', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner1 = models.CharField(db_column='sProjectOwner1', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner2 = models.CharField(db_column='sProjectOwner2', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner3 = models.CharField(db_column='sProjectOwner3', max_length=280, blank=True, null=True)  # Field name made lowercase.
    lcustomerpriority = models.CharField(db_column='lCustomerPriority', max_length=1, blank=True, null=True)  # Field name made lowercase.
    btaststarted = models.IntegerField(db_column='bTastStarted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectSubList'


class Projecttaskdetailslist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectid = models.BigIntegerField(db_column='lProjectId', blank=True, null=True)  # Field name made lowercase.
    ltaskno = models.BigIntegerField(db_column='lTaskNo', blank=True, null=True)  # Field name made lowercase.
    lsubprojectid = models.BigIntegerField(db_column='lSubProjectId', blank=True, null=True)  # Field name made lowercase.
    lsubprojecttaskid = models.BigIntegerField(db_column='lSubProjectTaskId', blank=True, null=True)  # Field name made lowercase.
    lfollowupeduptaskid = models.BigIntegerField(db_column='lFollowupedUpTaskId', blank=True, null=True)  # Field name made lowercase.
    lasignedid = models.BigIntegerField(db_column='lAsignedID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid = models.BigIntegerField(db_column='lProjectOwnerID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid1 = models.BigIntegerField(db_column='lProjectOwnerID1', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid2 = models.BigIntegerField(db_column='lProjectOwnerID2', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid3 = models.BigIntegerField(db_column='lProjectOwnerID3', blank=True, null=True)  # Field name made lowercase.
    dtplannedstarttime = models.DateTimeField(db_column='dtPlannedStartTime', blank=True, null=True)  # Field name made lowercase.
    dtplannedendtime = models.DateTimeField(db_column='dtPlannedEndTime', blank=True, null=True)  # Field name made lowercase.
    dtactualstarttime = models.DateTimeField(db_column='dtActualStartTime', blank=True, null=True)  # Field name made lowercase.
    dtactualendtime = models.DateTimeField(db_column='dtActualEndTime', blank=True, null=True)  # Field name made lowercase.
    dtteststarttime = models.DateTimeField(db_column='dtTestStartTime', blank=True, null=True)  # Field name made lowercase.
    dttestendtime = models.DateTimeField(db_column='dtTestEndTime', blank=True, null=True)  # Field name made lowercase.
    dtcustomertestendtime = models.DateTimeField(db_column='dtCustomerTestEndTime', blank=True, null=True)  # Field name made lowercase.
    bclosed = models.IntegerField(db_column='bClosed', blank=True, null=True)  # Field name made lowercase.
    bcompleted = models.IntegerField(db_column='bCompleted', blank=True, null=True)  # Field name made lowercase.
    bdiscarded = models.IntegerField(db_column='bDiscarded', blank=True, null=True)  # Field name made lowercase.
    bstoppedtemporary = models.IntegerField(db_column='bStoppedTemporary', blank=True, null=True)  # Field name made lowercase.
    btested = models.IntegerField(db_column='bTested', blank=True, null=True)  # Field name made lowercase.
    btestok = models.IntegerField(db_column='bTestOK', blank=True, null=True)  # Field name made lowercase.
    bcustomertested = models.IntegerField(db_column='bCustomerTested', blank=True, null=True)  # Field name made lowercase.
    bcustomertestok = models.IntegerField(db_column='bCustomerTestOK', blank=True, null=True)  # Field name made lowercase.
    bfollowuptask = models.IntegerField(db_column='bFollowupTask', blank=True, null=True)  # Field name made lowercase.
    bbillable = models.IntegerField(db_column='bBillable', blank=True, null=True)  # Field name made lowercase.
    bdirectmanreqd = models.IntegerField(db_column='bDirectManReqd', blank=True, null=True)  # Field name made lowercase.
    bteamreqd = models.IntegerField(db_column='bTeamReqd', blank=True, null=True)  # Field name made lowercase.
    bmaterialreqd = models.IntegerField(db_column='bMaterialReqd', blank=True, null=True)  # Field name made lowercase.
    bmachinereqd = models.IntegerField(db_column='bMachineReqd', blank=True, null=True)  # Field name made lowercase.
    bindirectmanreqd = models.IntegerField(db_column='bIndirectManReqd', blank=True, null=True)  # Field name made lowercase.
    btravelreqd = models.IntegerField(db_column='bTravelReqd', blank=True, null=True)  # Field name made lowercase.
    botherindirectcostreqd = models.IntegerField(db_column='bOtherIndirectCostReqd', blank=True, null=True)  # Field name made lowercase.
    bapprovalreqd = models.IntegerField(db_column='bApprovalReqd', blank=True, null=True)  # Field name made lowercase.
    bapproved1 = models.IntegerField(db_column='bApproved1', blank=True, null=True)  # Field name made lowercase.
    bapproved2 = models.IntegerField(db_column='bApproved2', blank=True, null=True)  # Field name made lowercase.
    lapprovalid2 = models.IntegerField(db_column='lApprovalId2', blank=True, null=True)  # Field name made lowercase.
    bapproved3 = models.IntegerField(db_column='bApproved3', blank=True, null=True)  # Field name made lowercase.
    bapproved4 = models.IntegerField(db_column='bApproved4', blank=True, null=True)  # Field name made lowercase.
    bapproved5 = models.IntegerField(db_column='bApproved5', blank=True, null=True)  # Field name made lowercase.
    brecalled = models.IntegerField(db_column='bReCalled', blank=True, null=True)  # Field name made lowercase.
    btask = models.IntegerField(db_column='bTask', blank=True, null=True)  # Field name made lowercase.
    bactionitem = models.IntegerField(db_column='bActionItem', blank=True, null=True)  # Field name made lowercase.
    bmeetingpoint = models.IntegerField(db_column='bMeetingPoint', blank=True, null=True)  # Field name made lowercase.
    bfollowup = models.IntegerField(db_column='bFollowup', blank=True, null=True)  # Field name made lowercase.
    breminder = models.IntegerField(db_column='bReminder', blank=True, null=True)  # Field name made lowercase.
    lpriority = models.IntegerField(db_column='lPriority', blank=True, null=True)  # Field name made lowercase.
    lsequence = models.IntegerField(db_column='lSequence', blank=True, null=True)  # Field name made lowercase.
    lsequencefollowup = models.IntegerField(db_column='lSequenceFollowup', blank=True, null=True)  # Field name made lowercase.
    lplannedperiod = models.IntegerField(db_column='lPlannedPeriod', blank=True, null=True)  # Field name made lowercase.
    lactualperiod = models.IntegerField(db_column='lActualPeriod', blank=True, null=True)  # Field name made lowercase.
    lplannedtotaltime = models.IntegerField(db_column='lPlannedTotalTime', blank=True, null=True)  # Field name made lowercase.
    lactualtotaltime = models.IntegerField(db_column='lActualTotalTime', blank=True, null=True)  # Field name made lowercase.
    lapprovallevel = models.IntegerField(db_column='lApprovalLevel', blank=True, null=True)  # Field name made lowercase.
    lapprovalid1 = models.IntegerField(db_column='lApprovalId1', blank=True, null=True)  # Field name made lowercase.
    lapprovalid3 = models.IntegerField(db_column='lApprovalId3', blank=True, null=True)  # Field name made lowercase.
    lapprovalid4 = models.IntegerField(db_column='lApprovalId4', blank=True, null=True)  # Field name made lowercase.
    lapprovalid5 = models.IntegerField(db_column='lApprovalId5', blank=True, null=True)  # Field name made lowercase.
    lteammemberid1 = models.IntegerField(db_column='lTeamMemberId1', blank=True, null=True)  # Field name made lowercase.
    lteammemberid2 = models.IntegerField(db_column='lTeamMemberId2', blank=True, null=True)  # Field name made lowercase.
    lteammemberid3 = models.IntegerField(db_column='lTeamMemberId3', blank=True, null=True)  # Field name made lowercase.
    lteammemberid4 = models.IntegerField(db_column='lTeamMemberId4', blank=True, null=True)  # Field name made lowercase.
    lteammemberid5 = models.IntegerField(db_column='lTeamMemberId5', blank=True, null=True)  # Field name made lowercase.
    fplannedcost = models.FloatField(db_column='fPlannedCost', blank=True, null=True)  # Field name made lowercase.
    factualcost = models.FloatField(db_column='fActualCost', blank=True, null=True)  # Field name made lowercase.
    fcostperhourplanned = models.FloatField(db_column='fCostperHourPlanned', blank=True, null=True)  # Field name made lowercase.
    staskno = models.CharField(db_column='sTaskNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    staskname = models.CharField(db_column='sTaskName', max_length=290, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommentcustomer = models.CharField(db_column='sCommentCustomer', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommenttestteam = models.CharField(db_column='sCommentTestTeam', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommentpm = models.CharField(db_column='sCommentPM', max_length=900, blank=True, null=True)  # Field name made lowercase.
    sasignedto = models.CharField(db_column='sAsignedTo', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname1 = models.CharField(db_column='sApprovalName1', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname2 = models.CharField(db_column='sApprovalName2', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname3 = models.CharField(db_column='sApprovalName3', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname4 = models.CharField(db_column='sApprovalName4', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname5 = models.CharField(db_column='sApprovalName5', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername1 = models.CharField(db_column='sTeamMemberName1', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername2 = models.CharField(db_column='sTeamMemberName2', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername3 = models.CharField(db_column='sTeamMemberName3', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername4 = models.CharField(db_column='sTeamMemberName4', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername5 = models.CharField(db_column='sTeamMemberName5', max_length=290, blank=True, null=True)  # Field name made lowercase.
    srecallreason = models.CharField(db_column='sReCallReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sdiscarded = models.CharField(db_column='sDiscarded', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sprojectowner = models.CharField(db_column='sProjectOwner', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner1 = models.CharField(db_column='sProjectOwner1', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner2 = models.CharField(db_column='sProjectOwner2', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner3 = models.CharField(db_column='sProjectOwner3', max_length=280, blank=True, null=True)  # Field name made lowercase.
    lcustomerpriority = models.CharField(db_column='lCustomerPriority', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bcustomervisible = models.IntegerField(db_column='bCustomerVisible', blank=True, null=True)  # Field name made lowercase.
    btaststarted = models.IntegerField(db_column='bTastStarted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectTaskDetailsList'


class Projecttasklist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectid = models.BigIntegerField(db_column='lProjectId', blank=True, null=True)  # Field name made lowercase.
    ltaskno = models.BigIntegerField(db_column='lTaskNo', blank=True, null=True)  # Field name made lowercase.
    lsubprojectid = models.BigIntegerField(db_column='lSubProjectId', blank=True, null=True)  # Field name made lowercase.
    lfollowupeduptaskid = models.BigIntegerField(db_column='lFollowupedUpTaskId', blank=True, null=True)  # Field name made lowercase.
    lasignedid = models.BigIntegerField(db_column='lAsignedID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid = models.BigIntegerField(db_column='lProjectOwnerID', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid1 = models.BigIntegerField(db_column='lProjectOwnerID1', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid2 = models.BigIntegerField(db_column='lProjectOwnerID2', blank=True, null=True)  # Field name made lowercase.
    lprojectownerid3 = models.BigIntegerField(db_column='lProjectOwnerID3', blank=True, null=True)  # Field name made lowercase.
    dtplannedstarttime = models.DateTimeField(db_column='dtPlannedStartTime', blank=True, null=True)  # Field name made lowercase.
    dtplannedendtime = models.DateTimeField(db_column='dtPlannedEndTime', blank=True, null=True)  # Field name made lowercase.
    dtactualstarttime = models.DateTimeField(db_column='dtActualStartTime', blank=True, null=True)  # Field name made lowercase.
    dtactualendtime = models.DateTimeField(db_column='dtActualEndTime', blank=True, null=True)  # Field name made lowercase.
    dtteststarttime = models.DateTimeField(db_column='dtTestStartTime', blank=True, null=True)  # Field name made lowercase.
    dttestendtime = models.DateTimeField(db_column='dtTestEndTime', blank=True, null=True)  # Field name made lowercase.
    dtcustomertestendtime = models.DateTimeField(db_column='dtCustomerTestEndTime', blank=True, null=True)  # Field name made lowercase.
    bclosed = models.IntegerField(db_column='bClosed', blank=True, null=True)  # Field name made lowercase.
    bcompleted = models.IntegerField(db_column='bCompleted', blank=True, null=True)  # Field name made lowercase.
    bdiscarded = models.IntegerField(db_column='bDiscarded', blank=True, null=True)  # Field name made lowercase.
    bstoppedtemporary = models.IntegerField(db_column='bStoppedTemporary', blank=True, null=True)  # Field name made lowercase.
    btested = models.IntegerField(db_column='bTested', blank=True, null=True)  # Field name made lowercase.
    btestok = models.IntegerField(db_column='bTestOK', blank=True, null=True)  # Field name made lowercase.
    bcustomertested = models.IntegerField(db_column='bCustomerTested', blank=True, null=True)  # Field name made lowercase.
    bcustomertestok = models.IntegerField(db_column='bCustomerTestOK', blank=True, null=True)  # Field name made lowercase.
    bfollowuptask = models.IntegerField(db_column='bFollowupTask', blank=True, null=True)  # Field name made lowercase.
    bbillable = models.IntegerField(db_column='bBillable', blank=True, null=True)  # Field name made lowercase.
    bdirectmanreqd = models.IntegerField(db_column='bDirectManReqd', blank=True, null=True)  # Field name made lowercase.
    bteamreqd = models.IntegerField(db_column='bTeamReqd', blank=True, null=True)  # Field name made lowercase.
    bmaterialreqd = models.IntegerField(db_column='bMaterialReqd', blank=True, null=True)  # Field name made lowercase.
    bmachinereqd = models.IntegerField(db_column='bMachineReqd', blank=True, null=True)  # Field name made lowercase.
    bindirectmanreqd = models.IntegerField(db_column='bIndirectManReqd', blank=True, null=True)  # Field name made lowercase.
    btravelreqd = models.IntegerField(db_column='bTravelReqd', blank=True, null=True)  # Field name made lowercase.
    botherindirectcostreqd = models.IntegerField(db_column='bOtherIndirectCostReqd', blank=True, null=True)  # Field name made lowercase.
    bapprovalreqd = models.IntegerField(db_column='bApprovalReqd', blank=True, null=True)  # Field name made lowercase.
    bapproved1 = models.IntegerField(db_column='bApproved1', blank=True, null=True)  # Field name made lowercase.
    bapproved2 = models.IntegerField(db_column='bApproved2', blank=True, null=True)  # Field name made lowercase.
    lapprovalid2 = models.IntegerField(db_column='lApprovalId2', blank=True, null=True)  # Field name made lowercase.
    bapproved3 = models.IntegerField(db_column='bApproved3', blank=True, null=True)  # Field name made lowercase.
    bapproved4 = models.IntegerField(db_column='bApproved4', blank=True, null=True)  # Field name made lowercase.
    bapproved5 = models.IntegerField(db_column='bApproved5', blank=True, null=True)  # Field name made lowercase.
    brecalled = models.IntegerField(db_column='bReCalled', blank=True, null=True)  # Field name made lowercase.
    btask = models.IntegerField(db_column='bTask', blank=True, null=True)  # Field name made lowercase.
    bactionitem = models.IntegerField(db_column='bActionItem', blank=True, null=True)  # Field name made lowercase.
    bmeetingpoint = models.IntegerField(db_column='bMeetingPoint', blank=True, null=True)  # Field name made lowercase.
    bfollowup = models.IntegerField(db_column='bFollowup', blank=True, null=True)  # Field name made lowercase.
    breminder = models.IntegerField(db_column='bReminder', blank=True, null=True)  # Field name made lowercase.
    lpriority = models.IntegerField(db_column='lPriority', blank=True, null=True)  # Field name made lowercase.
    lsequence = models.IntegerField(db_column='lSequence', blank=True, null=True)  # Field name made lowercase.
    lsequencefollowup = models.IntegerField(db_column='lSequenceFollowup', blank=True, null=True)  # Field name made lowercase.
    lplannedperiod = models.IntegerField(db_column='lPlannedPeriod', blank=True, null=True)  # Field name made lowercase.
    lactualperiod = models.IntegerField(db_column='lActualPeriod', blank=True, null=True)  # Field name made lowercase.
    lplannedtotaltime = models.IntegerField(db_column='lPlannedTotalTime', blank=True, null=True)  # Field name made lowercase.
    lactualtotaltime = models.IntegerField(db_column='lActualTotalTime', blank=True, null=True)  # Field name made lowercase.
    lapprovallevel = models.IntegerField(db_column='lApprovalLevel', blank=True, null=True)  # Field name made lowercase.
    lapprovalid1 = models.IntegerField(db_column='lApprovalId1', blank=True, null=True)  # Field name made lowercase.
    lapprovalid3 = models.IntegerField(db_column='lApprovalId3', blank=True, null=True)  # Field name made lowercase.
    lapprovalid4 = models.IntegerField(db_column='lApprovalId4', blank=True, null=True)  # Field name made lowercase.
    lapprovalid5 = models.IntegerField(db_column='lApprovalId5', blank=True, null=True)  # Field name made lowercase.
    lteammemberid1 = models.IntegerField(db_column='lTeamMemberId1', blank=True, null=True)  # Field name made lowercase.
    lteammemberid2 = models.IntegerField(db_column='lTeamMemberId2', blank=True, null=True)  # Field name made lowercase.
    lteammemberid3 = models.IntegerField(db_column='lTeamMemberId3', blank=True, null=True)  # Field name made lowercase.
    lteammemberid4 = models.IntegerField(db_column='lTeamMemberId4', blank=True, null=True)  # Field name made lowercase.
    lteammemberid5 = models.IntegerField(db_column='lTeamMemberId5', blank=True, null=True)  # Field name made lowercase.
    fplannedcost = models.FloatField(db_column='fPlannedCost', blank=True, null=True)  # Field name made lowercase.
    factualcost = models.FloatField(db_column='fActualCost', blank=True, null=True)  # Field name made lowercase.
    fcostperhourplanned = models.FloatField(db_column='fCostperHourPlanned', blank=True, null=True)  # Field name made lowercase.
    staskno = models.CharField(db_column='sTaskNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    staskname = models.CharField(db_column='sTaskName', max_length=290, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='sComment', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommentcustomer = models.CharField(db_column='sCommentCustomer', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommenttestteam = models.CharField(db_column='sCommentTestTeam', max_length=900, blank=True, null=True)  # Field name made lowercase.
    scommentpm = models.CharField(db_column='sCommentPM', max_length=900, blank=True, null=True)  # Field name made lowercase.
    sasignedto = models.CharField(db_column='sAsignedTo', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname1 = models.CharField(db_column='sApprovalName1', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname2 = models.CharField(db_column='sApprovalName2', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname3 = models.CharField(db_column='sApprovalName3', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname4 = models.CharField(db_column='sApprovalName4', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sapprovalname5 = models.CharField(db_column='sApprovalName5', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername1 = models.CharField(db_column='sTeamMemberName1', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername2 = models.CharField(db_column='sTeamMemberName2', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername3 = models.CharField(db_column='sTeamMemberName3', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername4 = models.CharField(db_column='sTeamMemberName4', max_length=290, blank=True, null=True)  # Field name made lowercase.
    steammembername5 = models.CharField(db_column='sTeamMemberName5', max_length=290, blank=True, null=True)  # Field name made lowercase.
    srecallreason = models.CharField(db_column='sReCallReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sdiscarded = models.CharField(db_column='sDiscarded', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sprojectowner = models.CharField(db_column='sProjectOwner', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner1 = models.CharField(db_column='sProjectOwner1', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner2 = models.CharField(db_column='sProjectOwner2', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sprojectowner3 = models.CharField(db_column='sProjectOwner3', max_length=280, blank=True, null=True)  # Field name made lowercase.
    lcustomerpriority = models.CharField(db_column='lCustomerPriority', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bcustomervisible = models.IntegerField(db_column='bCustomerVisible', blank=True, null=True)  # Field name made lowercase.
    btaststarted = models.IntegerField(db_column='bTastStarted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectTaskList'


class Acustomercontactlist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scustomercontactname = models.CharField(db_column='sCustomerContactName', max_length=240, blank=True, null=True)  # Field name made lowercase.
    suserid = models.CharField(db_column='sUserID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=14, blank=True, null=True)  # Field name made lowercase.
    bactive = models.IntegerField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.
    sempemailid = models.CharField(db_column='sEmpEmailID', max_length=210, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lcustomerid = models.IntegerField(db_column='lCustomerID', blank=True, null=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=280, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aCustomerContactList'


class Acustomerlst(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scustomername = models.CharField(db_column='sCustomerName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=280, blank=True, null=True)  # Field name made lowercase.
    bdomestric = models.IntegerField(db_column='bDomestric', blank=True, null=True)  # Field name made lowercase.
    binternational = models.IntegerField(db_column='bInternational', blank=True, null=True)  # Field name made lowercase.
    bprioritya = models.IntegerField(db_column='bPriorityA', blank=True, null=True)  # Field name made lowercase.
    bpriorityb = models.IntegerField(db_column='bPriorityB', blank=True, null=True)  # Field name made lowercase.
    bpriorityc = models.IntegerField(db_column='bPriorityC', blank=True, null=True)  # Field name made lowercase.
    bpriorityd = models.IntegerField(db_column='bPriorityD', blank=True, null=True)  # Field name made lowercase.
    lprojecctnocount = models.IntegerField(db_column='lProjecctNoCount', blank=True, null=True)  # Field name made lowercase.
    scustomerabv = models.CharField(db_column='sCustomerAbv', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aCustomerLst'


class Adepartmentlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdeptname = models.CharField(db_column='sDeptName', max_length=280, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aDepartmentList'


class Adesignationlist(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    sdesignation = models.CharField(db_column='sDesignation', max_length=280, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aDesignationList'


class Aemployeedoclist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lemployeeid = models.BigIntegerField(db_column='lEmployeeId', blank=True, null=True)  # Field name made lowercase.
    sfiledesc = models.CharField(db_column='sFileDesc', max_length=290, blank=True, null=True)  # Field name made lowercase.
    sfilename = models.CharField(db_column='sFileName', max_length=290, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aEmployeeDocList'


class Aemployeelist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    susername = models.CharField(db_column='sUserName', max_length=240, blank=True, null=True)  # Field name made lowercase.
    sempid = models.CharField(db_column='sEmpID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=14, blank=True, null=True)  # Field name made lowercase.
    sempemailid = models.CharField(db_column='sEmpEmailID', max_length=210, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdeptname = models.CharField(db_column='sDeptName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sreportmanager = models.CharField(db_column='sReportManager', max_length=280, blank=True, null=True)  # Field name made lowercase.
    sdesignation = models.CharField(db_column='sDesignation', max_length=280, blank=True, null=True)  # Field name made lowercase.
    dtdateofjleft = models.CharField(db_column='dtDateofJLeft', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdateofjoin = models.CharField(db_column='sDateofJoin', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spfno = models.CharField(db_column='sPFNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesino = models.CharField(db_column='sESINo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sadharno = models.CharField(db_column='sAdharNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spanno = models.CharField(db_column='sPanNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sbloodgroup = models.CharField(db_column='sBloodGroup', max_length=10, blank=True, null=True)  # Field name made lowercase.
    saddress = models.CharField(db_column='sAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sspousename = models.CharField(db_column='sSpouseName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sscontact = models.CharField(db_column='sSContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sfathername = models.CharField(db_column='sFatherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sfathercontact = models.CharField(db_column='sFatherContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smothername = models.CharField(db_column='sMotherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schildrenname1 = models.CharField(db_column='sChildrenName1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schildrenname2 = models.CharField(db_column='sChildrenName2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schildrenname3 = models.CharField(db_column='sChildrenName3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schildrenname4 = models.CharField(db_column='sChildrenName4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schildrenname5 = models.CharField(db_column='sChildrenName5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdateofbirth = models.CharField(db_column='sDateofBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sphotofile = models.CharField(db_column='sPhotoFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sinsurancedetails = models.CharField(db_column='sInsuranceDetails', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sbankname = models.CharField(db_column='SBankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sifsccode = models.CharField(db_column='sIFSCCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankaccountno = models.CharField(db_column='BankAccountNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtdateofjoin = models.DateTimeField(db_column='dtDateofJoin', blank=True, null=True)  # Field name made lowercase.
    ldeptid = models.IntegerField(db_column='lDeptId', blank=True, null=True)  # Field name made lowercase.
    lreportmanagerid = models.IntegerField(db_column='lReportManagerId', blank=True, null=True)  # Field name made lowercase.
    ldesignationid = models.IntegerField(db_column='lDesignationId', blank=True, null=True)  # Field name made lowercase.
    lage = models.IntegerField(db_column='lAge', blank=True, null=True)  # Field name made lowercase.
    badmin = models.IntegerField(db_column='bAdmin', blank=True, null=True)  # Field name made lowercase.
    bpm = models.IntegerField(db_column='bPM', blank=True, null=True)  # Field name made lowercase.
    bprojectmanager = models.IntegerField(db_column='bProjectManager', blank=True, null=True)  # Field name made lowercase.
    bdeveloper = models.IntegerField(db_column='bDeveloper', blank=True, null=True)  # Field name made lowercase.
    btester = models.IntegerField(db_column='bTester', blank=True, null=True)  # Field name made lowercase.
    bothers = models.IntegerField(db_column='bOthers', blank=True, null=True)  # Field name made lowercase.
    bactive = models.IntegerField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.
    bmanagement = models.IntegerField(db_column='bManagement', blank=True, null=True)  # Field name made lowercase.
    bit = models.IntegerField(db_column='bIT', blank=True, null=True)  # Field name made lowercase.
    binsurance = models.IntegerField(db_column='bInsurance', blank=True, null=True)  # Field name made lowercase.
    bta = models.IntegerField(db_column='bTA', blank=True, null=True)  # Field name made lowercase.
    bmedicalallow = models.IntegerField(db_column='bMedicalAllow', blank=True, null=True)  # Field name made lowercase.
    bda = models.IntegerField(db_column='bDA', blank=True, null=True)  # Field name made lowercase.
    bpf = models.IntegerField(db_column='bPF', blank=True, null=True)  # Field name made lowercase.
    besi = models.IntegerField(db_column='bESI', blank=True, null=True)  # Field name made lowercase.
    fcosttocompanyperhour = models.FloatField(db_column='fCosttoCompanyperHour', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany1 = models.FloatField(db_column='fCosttoCompany1', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany2 = models.FloatField(db_column='fCosttoCompany2', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany3 = models.FloatField(db_column='fCosttoCompany3', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany4 = models.FloatField(db_column='fCosttoCompany4', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany5 = models.FloatField(db_column='fCosttoCompany5', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany6 = models.FloatField(db_column='fCosttoCompany6', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany7 = models.FloatField(db_column='fCosttoCompany7', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany8 = models.FloatField(db_column='fCosttoCompany8', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany9 = models.FloatField(db_column='fCosttoCompany9', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany10 = models.FloatField(db_column='fCosttoCompany10', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany11 = models.FloatField(db_column='fCosttoCompany11', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany12 = models.FloatField(db_column='fCosttoCompany12', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany13 = models.FloatField(db_column='fCosttoCompany13', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany14 = models.FloatField(db_column='fCosttoCompany14', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany15 = models.FloatField(db_column='fCosttoCompany15', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany16 = models.FloatField(db_column='fCosttoCompany16', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany17 = models.FloatField(db_column='fCosttoCompany17', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany18 = models.FloatField(db_column='fCosttoCompany18', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany19 = models.FloatField(db_column='fCosttoCompany19', blank=True, null=True)  # Field name made lowercase.
    fcosttocompany20 = models.FloatField(db_column='fCosttoCompany20', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aEmployeeList'


class Aprojectcategorylist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    scategoryname = models.CharField(db_column='sCategoryName', max_length=280, blank=True, null=True)  # Field name made lowercase.
    bcustomervisible = models.IntegerField(db_column='bCustomerVisible', blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate1 = models.CharField(db_column='sSubProjectTemplate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate2 = models.CharField(db_column='sSubProjectTemplate2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate3 = models.CharField(db_column='sSubProjectTemplate3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate4 = models.CharField(db_column='sSubProjectTemplate4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate5 = models.CharField(db_column='sSubProjectTemplate5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate6 = models.CharField(db_column='sSubProjectTemplate6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate7 = models.CharField(db_column='sSubProjectTemplate7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate8 = models.CharField(db_column='sSubProjectTemplate8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate9 = models.CharField(db_column='sSubProjectTemplate9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate10 = models.CharField(db_column='sSubProjectTemplate10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate11 = models.CharField(db_column='sSubProjectTemplate11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate12 = models.CharField(db_column='sSubProjectTemplate12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate13 = models.CharField(db_column='sSubProjectTemplate13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate14 = models.CharField(db_column='sSubProjectTemplate14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate15 = models.CharField(db_column='sSubProjectTemplate15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate16 = models.CharField(db_column='sSubProjectTemplate16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate17 = models.CharField(db_column='sSubProjectTemplate17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate18 = models.CharField(db_column='sSubProjectTemplate18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate19 = models.CharField(db_column='sSubProjectTemplate19', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssubprojecttemplate20 = models.CharField(db_column='sSubProjectTemplate20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ltotalsubcount = models.IntegerField(db_column='lTotalSubCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aProjectCategoryList'


class Aprojectcategorysublist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectcategoryid = models.IntegerField(db_column='lProjectCategoryID', blank=True, null=True)  # Field name made lowercase.
    ssubname = models.CharField(db_column='sSubName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aProjectCategorysubList'


class Aprojectcategorysubtasklist(models.Model):
    lid = models.BigAutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    lprojectcategoryid = models.IntegerField(db_column='lProjectCategoryID', blank=True, null=True)  # Field name made lowercase.
    lprojectcategorysubid = models.IntegerField(db_column='lProjectCategorySubID', blank=True, null=True)  # Field name made lowercase.
    ssubname = models.CharField(db_column='sSubName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aProjectCategorysubTaskList'


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
