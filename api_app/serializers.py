from rest_framework import serializers
from api_app.models import Phonelist, BuyPlatforms

class PhonelistSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()
    Phonelist_status =serializers.SerializerMethodField()

    class Meta:
        model = Phonelist
        fields = "__all__"

    def get_len_name(self, obj):
        return len(obj.model_name)

class BuyPlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyPlatforms
        fields = "__all__"

    # def get_Phonelist_status(self, obj):
    #     if obj.rating < 4:
    #         return 'it\'s Good Phonelist You can Watch'
    #     if obj.rating > 4: 
    #         return 'it\'s super Phonelist You can Watch'

