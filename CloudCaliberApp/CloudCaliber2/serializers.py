from rest_framework import serializers
from CloudCaliber.models import Adminuserlist


class AdminuserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adminuserlist
        fields=('luserid','semployeename','semployeeno','spassword')
