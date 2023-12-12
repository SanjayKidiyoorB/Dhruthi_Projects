# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aemailescallationlist(models.Model):
    lid = models.AutoField(db_column='lId', primary_key=True)  # Field name made lowercase.
    semailid = models.CharField(db_column='sEmailID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='sName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aEmailEscallationList'


class Alogoimage(models.Model):
    lid = models.AutoField(db_column='lID', primary_key=True)  # Field name made lowercase.
    simage = models.BinaryField(db_column='sImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aLogoImage'


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


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


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


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


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


class Mcompanylist(models.Model):
    locationid = models.AutoField(db_column='LocationId', primary_key=True)  # Field name made lowercase.
    scompanyname = models.CharField(db_column='sCompanyName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=150, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    splace = models.CharField(db_column='sPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lpin = models.CharField(db_column='lPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lsupervisorid = models.IntegerField(db_column='lSupervisorId', blank=True, null=True)  # Field name made lowercase.
    ssupervisorname = models.CharField(db_column='sSupervisorName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid1 = models.IntegerField(db_column='lTempId1', blank=True, null=True)  # Field name made lowercase.
    stempname1 = models.CharField(db_column='sTempName1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid2 = models.IntegerField(db_column='lTempId2', blank=True, null=True)  # Field name made lowercase.
    stempname2 = models.CharField(db_column='sTempName2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid3 = models.IntegerField(db_column='lTempId3', blank=True, null=True)  # Field name made lowercase.
    stempname3 = models.CharField(db_column='sTempName3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid4 = models.IntegerField(db_column='lTempId4', blank=True, null=True)  # Field name made lowercase.
    stempname4 = models.CharField(db_column='sTempName4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid5 = models.IntegerField(db_column='lTempId5', blank=True, null=True)  # Field name made lowercase.
    stempname5 = models.CharField(db_column='sTempName5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    bcritical = models.BooleanField(db_column='bCritical', blank=True, null=True)  # Field name made lowercase.
    bnoncritical = models.BooleanField(db_column='bNonCritical', blank=True, null=True)  # Field name made lowercase.
    sgstno = models.CharField(db_column='sGSTNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spanno = models.CharField(db_column='sPAnNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    binactive = models.BooleanField(db_column='bInactive', blank=True, null=True)  # Field name made lowercase.
    linvoice1 = models.IntegerField(db_column='lInvoice1', blank=True, null=True)  # Field name made lowercase.
    linvoice2 = models.IntegerField(db_column='lInvoice2', blank=True, null=True)  # Field name made lowercase.
    linvoice3 = models.IntegerField(db_column='lInvoice3', blank=True, null=True)  # Field name made lowercase.
    linvoice4 = models.IntegerField(db_column='lInvoice4', blank=True, null=True)  # Field name made lowercase.
    linvoice5 = models.IntegerField(db_column='lInvoice5', blank=True, null=True)  # Field name made lowercase.
    linvoice6 = models.IntegerField(db_column='lInvoice6', blank=True, null=True)  # Field name made lowercase.
    linvoice7 = models.IntegerField(db_column='lInvoice7', blank=True, null=True)  # Field name made lowercase.
    linvoice8 = models.IntegerField(db_column='lInvoice8', blank=True, null=True)  # Field name made lowercase.
    linvoice9 = models.IntegerField(db_column='lInvoice9', blank=True, null=True)  # Field name made lowercase.
    linvoice10 = models.IntegerField(db_column='lInvoice10', blank=True, null=True)  # Field name made lowercase.
    linvoice11 = models.IntegerField(db_column='lInvoice11', blank=True, null=True)  # Field name made lowercase.
    linvoice12 = models.IntegerField(db_column='lInvoice12', blank=True, null=True)  # Field name made lowercase.
    linvoice13 = models.IntegerField(db_column='lInvoice13', blank=True, null=True)  # Field name made lowercase.
    linvoice14 = models.IntegerField(db_column='lInvoice14', blank=True, null=True)  # Field name made lowercase.
    linvoice15 = models.IntegerField(db_column='lInvoice15', blank=True, null=True)  # Field name made lowercase.
    linvoice16 = models.IntegerField(db_column='lInvoice16', blank=True, null=True)  # Field name made lowercase.
    linvoice17 = models.IntegerField(db_column='lInvoice17', blank=True, null=True)  # Field name made lowercase.
    linvoice18 = models.IntegerField(db_column='lInvoice18', blank=True, null=True)  # Field name made lowercase.
    linvoice19 = models.IntegerField(db_column='lInvoice19', blank=True, null=True)  # Field name made lowercase.
    linvoice20 = models.IntegerField(db_column='lInvoice20', blank=True, null=True)  # Field name made lowercase.
    lmonth = models.IntegerField(db_column='lMonth', blank=True, null=True)  # Field name made lowercase.
    lyear = models.IntegerField(db_column='lYear', blank=True, null=True)  # Field name made lowercase.
    sformat = models.CharField(db_column='sFormat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat1 = models.CharField(db_column='sFormat1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat2 = models.CharField(db_column='sFormat2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat3 = models.CharField(db_column='sFormat3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat4 = models.CharField(db_column='sFormat4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat5 = models.CharField(db_column='sFormat5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat6 = models.CharField(db_column='sFormat6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat7 = models.CharField(db_column='sFormat7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat8 = models.CharField(db_column='sFormat8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat9 = models.CharField(db_column='sFormat9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat10 = models.CharField(db_column='sFormat10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat11 = models.CharField(db_column='sFormat11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat12 = models.CharField(db_column='sFormat12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat13 = models.CharField(db_column='sFormat13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat14 = models.CharField(db_column='sFormat14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat15 = models.CharField(db_column='sFormat15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat16 = models.CharField(db_column='sFormat16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat17 = models.CharField(db_column='sFormat17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat18 = models.CharField(db_column='sFormat18', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat19 = models.CharField(db_column='sFormat19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sformat20 = models.CharField(db_column='sFormat20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scomments1 = models.TextField(db_column='sComments1', blank=True, null=True)  # Field name made lowercase.
    scomments2 = models.TextField(db_column='sComments2', blank=True, null=True)  # Field name made lowercase.
    scomments3 = models.TextField(db_column='sComments3', blank=True, null=True)  # Field name made lowercase.
    scomments4 = models.TextField(db_column='sComments4', blank=True, null=True)  # Field name made lowercase.
    scomments5 = models.TextField(db_column='sComments5', blank=True, null=True)  # Field name made lowercase.
    scomments6 = models.TextField(db_column='sComments6', blank=True, null=True)  # Field name made lowercase.
    scomments7 = models.TextField(db_column='sComments7', blank=True, null=True)  # Field name made lowercase.
    scomments8 = models.TextField(db_column='sComments8', blank=True, null=True)  # Field name made lowercase.
    scomments9 = models.TextField(db_column='sComments9', blank=True, null=True)  # Field name made lowercase.
    scomments10 = models.TextField(db_column='sComments10', blank=True, null=True)  # Field name made lowercase.
    scomments11 = models.TextField(db_column='sComments11', blank=True, null=True)  # Field name made lowercase.
    scomments12 = models.TextField(db_column='sComments12', blank=True, null=True)  # Field name made lowercase.
    scomments13 = models.TextField(db_column='sComments13', blank=True, null=True)  # Field name made lowercase.
    scomments14 = models.TextField(db_column='sComments14', blank=True, null=True)  # Field name made lowercase.
    scomments15 = models.TextField(db_column='sComments15', blank=True, null=True)  # Field name made lowercase.
    scomments16 = models.TextField(db_column='sComments16', blank=True, null=True)  # Field name made lowercase.
    scomments17 = models.TextField(db_column='sComments17', blank=True, null=True)  # Field name made lowercase.
    scomments18 = models.TextField(db_column='sComments18', blank=True, null=True)  # Field name made lowercase.
    scomments19 = models.TextField(db_column='sComments19', blank=True, null=True)  # Field name made lowercase.
    scomments20 = models.TextField(db_column='sComments20', blank=True, null=True)  # Field name made lowercase.
    sterms = models.TextField(db_column='sTerms', blank=True, null=True)  # Field name made lowercase.
    sterms1 = models.TextField(db_column='sTerms1', blank=True, null=True)  # Field name made lowercase.
    sterms2 = models.TextField(db_column='sTerms2', blank=True, null=True)  # Field name made lowercase.
    sterms3 = models.TextField(db_column='sTerms3', blank=True, null=True)  # Field name made lowercase.
    sterms4 = models.TextField(db_column='sTerms4', blank=True, null=True)  # Field name made lowercase.
    sterms5 = models.TextField(db_column='sTerms5', blank=True, null=True)  # Field name made lowercase.
    sterms6 = models.TextField(db_column='sTerms6', blank=True, null=True)  # Field name made lowercase.
    sterms7 = models.TextField(db_column='sTerms7', blank=True, null=True)  # Field name made lowercase.
    sterms8 = models.TextField(db_column='sTerms8', blank=True, null=True)  # Field name made lowercase.
    sterms9 = models.TextField(db_column='sTerms9', blank=True, null=True)  # Field name made lowercase.
    sterms10 = models.TextField(db_column='sTerms10', blank=True, null=True)  # Field name made lowercase.
    sterms11 = models.TextField(db_column='sTerms11', blank=True, null=True)  # Field name made lowercase.
    sterms12 = models.TextField(db_column='sTerms12', blank=True, null=True)  # Field name made lowercase.
    sterms13 = models.TextField(db_column='sTerms13', blank=True, null=True)  # Field name made lowercase.
    sterms14 = models.TextField(db_column='sTerms14', blank=True, null=True)  # Field name made lowercase.
    sterms15 = models.TextField(db_column='sTerms15', blank=True, null=True)  # Field name made lowercase.
    sterms16 = models.TextField(db_column='sTerms16', blank=True, null=True)  # Field name made lowercase.
    sterms17 = models.TextField(db_column='sTerms17', blank=True, null=True)  # Field name made lowercase.
    sterms18 = models.TextField(db_column='sTerms18', blank=True, null=True)  # Field name made lowercase.
    sterms19 = models.TextField(db_column='sTerms19', blank=True, null=True)  # Field name made lowercase.
    sterms20 = models.TextField(db_column='sTerms20', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mCompanyList'


class Mcustomerlist(models.Model):
    customerid = models.BigAutoField(db_column='customerID', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lpin = models.CharField(db_column='lPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstd = models.CharField(db_column='sSTD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scontactno = models.CharField(db_column='sContactNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfax = models.CharField(db_column='sFax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customersalestax = models.CharField(db_column='CustomerSalestax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cst = models.BooleanField(db_column='CST', blank=True, null=True)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gstno = models.CharField(db_column='GSTNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mCustomerList'


class Mpartdetailslist(models.Model):
    partid = models.BigAutoField(db_column='PartID', primary_key=True)  # Field name made lowercase.
    partno = models.CharField(db_column='partNo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    brandid = models.BigIntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    sbrandname = models.CharField(db_column='sBrandName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    unitofmeasure = models.CharField(db_column='Unitofmeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    openingstock = models.BigIntegerField(db_column='OpeningStock', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mPartDetailsList'


class Msitelist(models.Model):
    lcontactdetailnoid = models.BigAutoField(db_column='lContactDetailNoID', primary_key=True)  # Field name made lowercase.
    customerid = models.BigIntegerField(db_column='customerID', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=150, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smobile = models.CharField(db_column='sMobile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    splace = models.CharField(db_column='sPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lpin = models.CharField(db_column='lPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lsupervisorid = models.IntegerField(db_column='lSupervisorId', blank=True, null=True)  # Field name made lowercase.
    ssupervisorname = models.CharField(db_column='sSupervisorName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid1 = models.IntegerField(db_column='lTempId1', blank=True, null=True)  # Field name made lowercase.
    stempname1 = models.CharField(db_column='sTempName1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid2 = models.IntegerField(db_column='lTempId2', blank=True, null=True)  # Field name made lowercase.
    stempname2 = models.CharField(db_column='sTempName2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid3 = models.IntegerField(db_column='lTempId3', blank=True, null=True)  # Field name made lowercase.
    stempname3 = models.CharField(db_column='sTempName3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid4 = models.IntegerField(db_column='lTempId4', blank=True, null=True)  # Field name made lowercase.
    stempname4 = models.CharField(db_column='sTempName4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ltempid5 = models.IntegerField(db_column='lTempId5', blank=True, null=True)  # Field name made lowercase.
    stempname5 = models.CharField(db_column='sTempName5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    bcritical = models.BooleanField(db_column='bCritical', blank=True, null=True)  # Field name made lowercase.
    bnoncritical = models.BooleanField(db_column='bNonCritical', blank=True, null=True)  # Field name made lowercase.
    bsez = models.BooleanField(db_column='bSEZ', blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mSiteList'


class Msupplierlist(models.Model):
    supplierid = models.BigAutoField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sstatus = models.CharField(db_column='sStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lpin = models.CharField(db_column='lPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstd = models.CharField(db_column='sSTD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scontactno = models.CharField(db_column='sContactNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfax = models.CharField(db_column='sFax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suppliersalestax = models.CharField(db_column='SupplierSalestax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cst = models.BooleanField(db_column='CST', blank=True, null=True)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gstno = models.CharField(db_column='GSTNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mSupplierList'


class Tcreditnotedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCreditNoteDetailsList'


class Tcreditnotelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCreditNoteList'


class Tdcdetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDCDetailsList'


class Tdclist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDCList'


class Tdebitnotedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDebitNoteDetailsList'


class Tdebitnotelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDebitNoteList'


class Tgrndetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tGRNDetailsList'


class Tgrnlist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stermms1 = models.CharField(db_column='sTermms1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms2 = models.CharField(db_column='sTermms2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms3 = models.CharField(db_column='sTermms3', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms4 = models.CharField(db_column='sTermms4', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms5 = models.CharField(db_column='sTermms5', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms6 = models.CharField(db_column='sTermms6', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms7 = models.CharField(db_column='sTermms7', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms8 = models.CharField(db_column='sTermms8', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms9 = models.CharField(db_column='sTermms9', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms10 = models.CharField(db_column='sTermms10', max_length=450, blank=True, null=True)  # Field name made lowercase.
    sprofile1 = models.TextField(db_column='sProfile1', blank=True, null=True)  # Field name made lowercase.
    sprofile2 = models.TextField(db_column='sProfile2', blank=True, null=True)  # Field name made lowercase.
    sprofile3 = models.TextField(db_column='sProfile3', blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails1 = models.CharField(db_column='sPaymentRecdDetails1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails2 = models.CharField(db_column='sPaymentRecdDetails2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails3 = models.CharField(db_column='sPaymentRecdDetails3', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tGRNList'


class Tinvoicedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tInvoiceDetailsList'


class Tinvoicelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    breversechargemechanism = models.BooleanField(db_column='bReverseChargeMechanism', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tInvoiceList'


class Torderacceptancedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tOrderAcceptanceDetailsList'


class Torderacceptancelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stermms1 = models.CharField(db_column='sTermms1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms2 = models.CharField(db_column='sTermms2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms3 = models.CharField(db_column='sTermms3', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms4 = models.CharField(db_column='sTermms4', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms5 = models.CharField(db_column='sTermms5', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms6 = models.CharField(db_column='sTermms6', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms7 = models.CharField(db_column='sTermms7', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms8 = models.CharField(db_column='sTermms8', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms9 = models.CharField(db_column='sTermms9', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms10 = models.CharField(db_column='sTermms10', max_length=450, blank=True, null=True)  # Field name made lowercase.
    sprofile1 = models.TextField(db_column='sProfile1', blank=True, null=True)  # Field name made lowercase.
    sprofile2 = models.TextField(db_column='sProfile2', blank=True, null=True)  # Field name made lowercase.
    sprofile3 = models.TextField(db_column='sProfile3', blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails1 = models.CharField(db_column='sPaymentRecdDetails1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails2 = models.CharField(db_column='sPaymentRecdDetails2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails3 = models.CharField(db_column='sPaymentRecdDetails3', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tOrderAcceptanceList'


class Tproformadetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProformaDetailsList'


class Tproformalist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProformaList'


class Tproformaserviceinvoicedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ltaxrate = models.FloatField(db_column='lTaxRate', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt = models.FloatField(db_column='lTaxRateAmt', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt1 = models.FloatField(db_column='lTaxRateAmt1', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt2 = models.FloatField(db_column='lTaxRateAmt2', blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProformaServiceInvoiceDetailsList'


class Tproformaserviceinvoicelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.BigIntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.IntegerField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.IntegerField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.IntegerField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.IntegerField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.IntegerField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.IntegerField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.IntegerField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.IntegerField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.IntegerField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.IntegerField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.IntegerField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.IntegerField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.IntegerField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProformaServiceInvoiceList'


class Tproposaldetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProposalDetailsList'


class Tproposallist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stermms1 = models.CharField(db_column='sTermms1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms2 = models.CharField(db_column='sTermms2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms3 = models.CharField(db_column='sTermms3', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms4 = models.CharField(db_column='sTermms4', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms5 = models.CharField(db_column='sTermms5', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms6 = models.CharField(db_column='sTermms6', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms7 = models.CharField(db_column='sTermms7', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms8 = models.CharField(db_column='sTermms8', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms9 = models.CharField(db_column='sTermms9', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms10 = models.CharField(db_column='sTermms10', max_length=450, blank=True, null=True)  # Field name made lowercase.
    sprofile1 = models.TextField(db_column='sProfile1', blank=True, null=True)  # Field name made lowercase.
    sprofile2 = models.TextField(db_column='sProfile2', blank=True, null=True)  # Field name made lowercase.
    sprofile3 = models.TextField(db_column='sProfile3', blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails1 = models.CharField(db_column='sPaymentRecdDetails1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails2 = models.CharField(db_column='sPaymentRecdDetails2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails3 = models.CharField(db_column='sPaymentRecdDetails3', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProposalList'


class Tpurchaseorderdetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPurchaseOrderDetailsList'


class Tpurchaseorderlist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.IntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.BooleanField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.BooleanField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.BooleanField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.BooleanField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.BooleanField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.BooleanField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.BooleanField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.BooleanField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.BooleanField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.BooleanField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.BooleanField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.BooleanField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.BooleanField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    dsgst01 = models.FloatField(db_column='dSGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst01 = models.FloatField(db_column='dCGST01', blank=True, null=True)  # Field name made lowercase.
    dcgst00 = models.FloatField(db_column='dCGST00', blank=True, null=True)  # Field name made lowercase.
    dsgst5 = models.FloatField(db_column='dSGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst5 = models.FloatField(db_column='dCGST5', blank=True, null=True)  # Field name made lowercase.
    dcgst50 = models.FloatField(db_column='dCGST50', blank=True, null=True)  # Field name made lowercase.
    dsgst12 = models.FloatField(db_column='dSGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst12 = models.FloatField(db_column='dCGST12', blank=True, null=True)  # Field name made lowercase.
    dcgst120 = models.FloatField(db_column='dCGST120', blank=True, null=True)  # Field name made lowercase.
    dsgst18 = models.FloatField(db_column='dSGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst18 = models.FloatField(db_column='dCGST18', blank=True, null=True)  # Field name made lowercase.
    dcgst180 = models.FloatField(db_column='dCGST180', blank=True, null=True)  # Field name made lowercase.
    dsgst28 = models.FloatField(db_column='dSGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst28 = models.FloatField(db_column='dCGST28', blank=True, null=True)  # Field name made lowercase.
    dcgst280 = models.FloatField(db_column='dCGST280', blank=True, null=True)  # Field name made lowercase.
    dgst28cess = models.FloatField(db_column='dGST28Cess', blank=True, null=True)  # Field name made lowercase.
    dsgst0pt5 = models.FloatField(db_column='dSGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt5 = models.FloatField(db_column='dCGST0pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst0pt50 = models.FloatField(db_column='dCGST0pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt0 = models.FloatField(db_column='dSGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt0 = models.FloatField(db_column='dCGST2pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt00 = models.FloatField(db_column='dCGST2pt00', blank=True, null=True)  # Field name made lowercase.
    dsgst2pt5 = models.FloatField(db_column='dSGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt5 = models.FloatField(db_column='dCGST2pt5', blank=True, null=True)  # Field name made lowercase.
    dcgst2pt50 = models.FloatField(db_column='dCGST2pt50', blank=True, null=True)  # Field name made lowercase.
    dsgst1p0 = models.FloatField(db_column='dSGST1p0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt0 = models.FloatField(db_column='dCGST1pt0', blank=True, null=True)  # Field name made lowercase.
    dcgst1pt00 = models.FloatField(db_column='dCGST1pt00', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    saddressclient1 = models.TextField(db_column='sAddressClient1', blank=True, null=True)  # Field name made lowercase.
    saddresssite1 = models.TextField(db_column='sAddressSite1', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress1 = models.TextField(db_column='sCompanyAddress1', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stermms1 = models.CharField(db_column='sTermms1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms2 = models.CharField(db_column='sTermms2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms3 = models.CharField(db_column='sTermms3', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms4 = models.CharField(db_column='sTermms4', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms5 = models.CharField(db_column='sTermms5', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms6 = models.CharField(db_column='sTermms6', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms7 = models.CharField(db_column='sTermms7', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms8 = models.CharField(db_column='sTermms8', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms9 = models.CharField(db_column='sTermms9', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stermms10 = models.CharField(db_column='sTermms10', max_length=450, blank=True, null=True)  # Field name made lowercase.
    sprofile1 = models.TextField(db_column='sProfile1', blank=True, null=True)  # Field name made lowercase.
    sprofile2 = models.TextField(db_column='sProfile2', blank=True, null=True)  # Field name made lowercase.
    sprofile3 = models.TextField(db_column='sProfile3', blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails1 = models.CharField(db_column='sPaymentRecdDetails1', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails2 = models.CharField(db_column='sPaymentRecdDetails2', max_length=450, blank=True, null=True)  # Field name made lowercase.
    spaymentrecddetails3 = models.CharField(db_column='sPaymentRecdDetails3', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPurchaseOrderList'


class Trentinvoicedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ltaxrate = models.FloatField(db_column='lTaxRate', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt = models.FloatField(db_column='lTaxRateAmt', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt1 = models.FloatField(db_column='lTaxRateAmt1', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt2 = models.FloatField(db_column='lTaxRateAmt2', blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tRentInvoiceDetailsList'


class Trentinvoicelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.BigIntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.IntegerField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.IntegerField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.IntegerField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.IntegerField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.IntegerField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.IntegerField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.IntegerField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.IntegerField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.IntegerField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.IntegerField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.IntegerField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.IntegerField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.IntegerField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tRentInvoiceList'


class Tserviceinvoicedetailslist(models.Model):
    salesordermultiid = models.BigAutoField(db_column='SalesOrderMultiID', primary_key=True)  # Field name made lowercase.
    salesbillid = models.BigIntegerField(db_column='SalesBillID', blank=True, null=True)  # Field name made lowercase.
    sdesc = models.CharField(db_column='sDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partid = models.BigIntegerField(db_column='PartID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ddescitemtotal = models.FloatField(db_column='dDescItemTotal', blank=True, null=True)  # Field name made lowercase.
    shsn = models.CharField(db_column='SHSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssac = models.CharField(db_column='SSAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smanrate = models.CharField(db_column='SMANRATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staxnotify = models.CharField(db_column='STAXNOTIFY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ltaxrate = models.FloatField(db_column='lTaxRate', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt = models.FloatField(db_column='lTaxRateAmt', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt1 = models.FloatField(db_column='lTaxRateAmt1', blank=True, null=True)  # Field name made lowercase.
    ltaxrateamt2 = models.FloatField(db_column='lTaxRateAmt2', blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tServiceInvoiceDetailsList'


class Tserviceinvoicelist(models.Model):
    salesbillid = models.AutoField(db_column='SalesBillID', primary_key=True)  # Field name made lowercase.
    salesbillno = models.IntegerField(db_column='SalesBillNo', blank=True, null=True)  # Field name made lowercase.
    finyear = models.IntegerField(db_column='FinYear', blank=True, null=True)  # Field name made lowercase.
    sinvoicerefno = models.CharField(db_column='sInvoiceRefNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1 = models.CharField(db_column='sAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2 = models.CharField(db_column='sAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3 = models.CharField(db_column='sAddress3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spin = models.CharField(db_column='sPin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scity = models.CharField(db_column='sCity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstate = models.CharField(db_column='sState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomerpan = models.CharField(db_column='sCustomerPan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scustomergst = models.CharField(db_column='sCustomerGST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customernamesite = models.CharField(db_column='CustomerNameSite', max_length=150, blank=True, null=True)  # Field name made lowercase.
    saddress1site = models.CharField(db_column='sAddress1Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress2site = models.CharField(db_column='sAddress2Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saddress3site = models.CharField(db_column='sAddress3Site', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spinsite = models.CharField(db_column='sPinSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scitysite = models.CharField(db_column='sCitySite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstatesite = models.CharField(db_column='sStateSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pono = models.CharField(db_column='PONo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtotal = models.FloatField(db_column='dTotal', blank=True, null=True)  # Field name made lowercase.
    dgsttrate = models.FloatField(db_column='dGSTTRate', blank=True, null=True)  # Field name made lowercase.
    dgst = models.FloatField(db_column='DGST', blank=True, null=True)  # Field name made lowercase.
    dtotalfinal = models.FloatField(db_column='dTotalFinal', blank=True, null=True)  # Field name made lowercase.
    swords = models.CharField(db_column='sWords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sgstsplit = models.CharField(db_column='sGSTSplit', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note1 = models.TextField(db_column='Note1', blank=True, null=True)  # Field name made lowercase.
    note2 = models.TextField(db_column='Note2', blank=True, null=True)  # Field name made lowercase.
    inr = models.IntegerField(db_column='INR', blank=True, null=True)  # Field name made lowercase.
    scategoryofservice = models.CharField(db_column='sCategoryofService', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='sType1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile1 = models.CharField(db_column='sFile1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder1 = models.CharField(db_column='sFolder1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    snumber1 = models.BigIntegerField(db_column='sNumber1', blank=True, null=True)  # Field name made lowercase.
    customersiteid = models.IntegerField(db_column='CustomerSiteID', blank=True, null=True)  # Field name made lowercase.
    sstatecode = models.CharField(db_column='sStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sfromdate = models.CharField(db_column='sFromDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stodate = models.CharField(db_column='sToDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgst0 = models.FloatField(db_column='dSGST0', blank=True, null=True)  # Field name made lowercase.
    dcgst0 = models.FloatField(db_column='dCGST0', blank=True, null=True)  # Field name made lowercase.
    digst0 = models.FloatField(db_column='dIGST0', blank=True, null=True)  # Field name made lowercase.
    lnoofedit = models.IntegerField(db_column='lNoofEdit', blank=True, null=True)  # Field name made lowercase.
    ddateofedit = models.CharField(db_column='dDateofEdit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartmentname = models.CharField(db_column='sDepartmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bdelete = models.IntegerField(db_column='bDelete', blank=True, null=True)  # Field name made lowercase.
    bcancelcopy = models.IntegerField(db_column='bCancelCopy', blank=True, null=True)  # Field name made lowercase.
    bapproval0 = models.IntegerField(db_column='bApproval0', blank=True, null=True)  # Field name made lowercase.
    bapproval01 = models.IntegerField(db_column='bApproval01', blank=True, null=True)  # Field name made lowercase.
    bapproval02 = models.IntegerField(db_column='bApproval02', blank=True, null=True)  # Field name made lowercase.
    bapproval03 = models.IntegerField(db_column='bApproval03', blank=True, null=True)  # Field name made lowercase.
    bapproval04 = models.IntegerField(db_column='bApproval04', blank=True, null=True)  # Field name made lowercase.
    bapproval05 = models.IntegerField(db_column='bApproval05', blank=True, null=True)  # Field name made lowercase.
    bapproval06 = models.IntegerField(db_column='bApproval06', blank=True, null=True)  # Field name made lowercase.
    bapproval07 = models.IntegerField(db_column='bApproval07', blank=True, null=True)  # Field name made lowercase.
    bapproval08 = models.IntegerField(db_column='bApproval08', blank=True, null=True)  # Field name made lowercase.
    bapproval09 = models.IntegerField(db_column='bApproval09', blank=True, null=True)  # Field name made lowercase.
    bapproval010 = models.IntegerField(db_column='bApproval010', blank=True, null=True)  # Field name made lowercase.
    scomments = models.TextField(db_column='sComments', blank=True, null=True)  # Field name made lowercase.
    scommentsdelete = models.TextField(db_column='sCommentsDelete', blank=True, null=True)  # Field name made lowercase.
    lorderid = models.IntegerField(db_column='lOrderId', blank=True, null=True)  # Field name made lowercase.
    saddressclient = models.TextField(db_column='sAddressClient', blank=True, null=True)  # Field name made lowercase.
    saddresssite = models.TextField(db_column='sAddressSite', blank=True, null=True)  # Field name made lowercase.
    scompanyaddress = models.TextField(db_column='sCompanyAddress', blank=True, null=True)  # Field name made lowercase.
    inrno = models.CharField(db_column='INRNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ackno = models.CharField(db_column='ACKNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewayno = models.CharField(db_column='eWayNo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ewaydate = models.CharField(db_column='eWayDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ewaydate1 = models.CharField(db_column='eWayDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='sDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sdate1 = models.CharField(db_column='sDate1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    llocationid = models.IntegerField(db_column='lLocationId', blank=True, null=True)  # Field name made lowercase.
    slocation = models.CharField(db_column='sLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slocationstatecode = models.CharField(db_column='sLocationStateCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slocationgstno = models.CharField(db_column='sLocationGSTNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationpanno = models.CharField(db_column='sLocationPANNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    slocationformat = models.CharField(db_column='sLocationFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bsitesez = models.IntegerField(db_column='bSiteSEZ', blank=True, null=True)  # Field name made lowercase.
    sworkfrom = models.CharField(db_column='sWorkFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sworkfto = models.CharField(db_column='sWorkFTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ackdate = models.CharField(db_column='ackDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ackdate1 = models.CharField(db_column='ackDate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    podate1 = models.CharField(db_column='PODate1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bsamestate = models.IntegerField(db_column='bSameState', blank=True, null=True)  # Field name made lowercase.
    sfile11 = models.CharField(db_column='sFile11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder11 = models.CharField(db_column='sFolder11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile12 = models.CharField(db_column='sFile12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder12 = models.CharField(db_column='sFolder12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile13 = models.CharField(db_column='sFile13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder13 = models.CharField(db_column='sFolder13', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile14 = models.CharField(db_column='sFile14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder14 = models.CharField(db_column='sFolder14', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfile15 = models.CharField(db_column='sFile15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sfolder15 = models.CharField(db_column='sFolder15', max_length=150, blank=True, null=True)  # Field name made lowercase.
    slutno = models.CharField(db_column='sLUTNo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    breversechargemechanism = models.BooleanField(db_column='bReverseChargeMechanism', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tServiceInvoiceList'


class Unotevalues(models.Model):
    slno = models.BigAutoField(db_column='Slno', primary_key=True)  # Field name made lowercase.
    squotationterm = models.TextField(db_column='sQuotationTerm', blank=True, null=True)  # Field name made lowercase.
    stermsorderack = models.TextField(db_column='sTermsOrderAck', blank=True, null=True)  # Field name made lowercase.
    sorderpayment = models.TextField(db_column='sOrderPayment', blank=True, null=True)  # Field name made lowercase.
    sorderbanker = models.TextField(db_column='sOrderBanker', blank=True, null=True)  # Field name made lowercase.
    sorderlogin1 = models.TextField(db_column='sOrderlogin1', blank=True, null=True)  # Field name made lowercase.
    sorderbankerinr = models.TextField(db_column='sOrderBankerINR', blank=True, null=True)  # Field name made lowercase.
    sorderlogin3 = models.TextField(db_column='sOrderLogin3', blank=True, null=True)  # Field name made lowercase.
    sorderlogin4 = models.TextField(db_column='sorderLogin4', blank=True, null=True)  # Field name made lowercase.
    sorderlogin5 = models.CharField(db_column='sorderLogin5', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sorderlogin6 = models.CharField(db_column='sorderLogin6', max_length=150, blank=True, null=True)  # Field name made lowercase.
    spayment1 = models.CharField(db_column='sPayment1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    spayment2 = models.CharField(max_length=150, blank=True, null=True)
    sstock1 = models.CharField(db_column='sStock1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sstock2 = models.CharField(db_column='sStock2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    billto = models.CharField(db_column='BillTo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    billaddress = models.TextField(db_column='BillAddress', blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.TextField(db_column='ShipAddress', blank=True, null=True)  # Field name made lowercase.
    spayment = models.CharField(db_column='sPayment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sprice = models.CharField(db_column='sPrice', max_length=150)  # Field name made lowercase.
    sdelivery = models.CharField(db_column='sDelivery', max_length=150, blank=True, null=True)  # Field name made lowercase.
    squotationorderinfavor = models.CharField(db_column='sQuotationOrderinFavor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    billtoinr = models.CharField(db_column='BillToINR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billtoaddressinr = models.TextField(db_column='BillToAddressINR', blank=True, null=True)  # Field name made lowercase.
    shiptoaddressinr = models.TextField(db_column='ShipToAddressINR', blank=True, null=True)  # Field name made lowercase.
    shiptoinr = models.CharField(db_column='shipToINR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    squotationterminr = models.TextField(db_column='sQuotationTermINR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uNoteValues'


class Userlist(models.Model):
    luserid = models.AutoField(db_column='lUserID', primary_key=True)  # Field name made lowercase.
    u1_username = models.CharField(max_length=80, blank=True, null=True)
    u1_password = models.CharField(max_length=80, blank=True, null=True)
    u1_short = models.CharField(db_column='u1_Short', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bcustomer = models.BooleanField(db_column='bCustomer', blank=True, null=True)  # Field name made lowercase.
    bsupplier = models.BooleanField(db_column='bSupplier', blank=True, null=True)  # Field name made lowercase.
    bitem = models.BooleanField(db_column='bItem', blank=True, null=True)  # Field name made lowercase.
    bmaintenancebill = models.BooleanField(db_column='bMaintenanceBill', blank=True, null=True)  # Field name made lowercase.
    bworkcontractbill = models.BooleanField(db_column='bWorkContractBill', blank=True, null=True)  # Field name made lowercase.
    breadwrite = models.BooleanField(db_column='bReadWrite', blank=True, null=True)  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly', blank=True, null=True)  # Field name made lowercase.
    ball = models.BooleanField(db_column='bAll', blank=True, null=True)  # Field name made lowercase.
    bpo = models.BooleanField(db_column='bPO', blank=True, null=True)  # Field name made lowercase.
    smodify = models.BooleanField(db_column='sModify', blank=True, null=True)  # Field name made lowercase.
    bblock = models.BooleanField(db_column='bBlock', blank=True, null=True)  # Field name made lowercase.
    sreport = models.BooleanField(db_column='sReport', blank=True, null=True)  # Field name made lowercase.
    sadmin = models.BooleanField(db_column='sAdmin', blank=True, null=True)  # Field name made lowercase.
    u1_sregion = models.CharField(db_column='u1_sRegion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bho = models.BooleanField(db_column='bHO', blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='sName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ldepartmentid = models.IntegerField(db_column='lDepartmentId', blank=True, null=True)  # Field name made lowercase.
    sdepartment = models.CharField(db_column='sDepartment', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userlist'
