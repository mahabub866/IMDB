
from rest_framework import serializers

from WatchMate.models import Review, WatchList,StreamPlateform


class ReviewSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    review_user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Review
        exclude=('watchlist',)
        # fields="__all__"  #['id','name','descroption']

class WatchListSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"  #['id','name','descroption']
class StreamSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model=StreamPlateform
        fields="__all__"  #['id','name','descroption']


        # exclude=['active']
    # def get_len_name(self,object):
    #     length=len(object.name)
    #     return length
    # def validate(self, data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Title and description should be different")
    #     else:
    #         return data

    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too Short!")
    #     else:
    #         return value


# def name_lenth(value):
#     if len(value)<3:
#             raise serializers.ValidationError("Name is too Short!")
#     else:
#         return value

# class MoiveSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_lenth])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Moive.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data

    # def validate_name(self,value):
    #     if len(value)<3:
    #         raise serializers.ValidationError("Name is too Short!")
    #     else:
    #         return value
            
    
