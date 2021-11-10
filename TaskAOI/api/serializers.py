from rest_framework import fields, serializers

#modeldagi malumotlarni json kurinshga uzgartirish
from django.contrib.auth import get_user_model
#models
from talabaApp.models import Student
from homiy.models import Homiy

class HomiySerializer(serializers.ModelSerializer):
    #author-username
    # author = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Homiy
        fields = '__all__'
        
class TalabaSerializers(serializers.ModelSerializer):
    #user-posts-id
    # talaba = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'