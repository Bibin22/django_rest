from rest_framework import serializers
from watchlist_app.models import *



class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamingPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = "__all__"












class MovieListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movies
        fields = "__all__"

    # def get_len_name(self, object):
    #     return len(object.name)
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError(" Name is too short")
#
#
# class MovieListSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self,validated_data):
#         return Movies.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         return instance
#
#     def validate(self, data): #object level validation
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(" fields shouldnt be same")
#         else:
#             return data

    
    # def validate_name(self, value): #field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too Short")
    #     else:
    #         return value
