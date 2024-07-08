from rest_framework import serializers
from .models import *

# Serializer class models for all the tables in the db


class CollisionSeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollisionSeverity
        fields = ['col_sev_no', 'col_sev']


class DayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fields = ['day_of_week_no', 'day_of_week']


class RoadClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadClass
        fields = ['road_class_no', 'road_class']


class RoadTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadType
        fields = ['road_type', 'road_type']


class LightConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightCondition
        fields = ['light_cond_no', 'light_cond']


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = ['weather_cond', 'weather_cond_no']


class RoadSurfaceConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSurfaceCondition
        fields = ['road_surf_cond_no', 'road_surf_cond']


class CollisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collision
        fields = ['collision_ref', 'uk_grid_ref_x', 'uk_grid_ref_y', 'collision_severity', 'no_of_vehicles', 'no_of_casualties', 'date',
                  'day_of_week', 'road_class', 'road_type', 'speed_limit', 'light_condition', 'weather_condition', 'road_surface_condition']

    def create(self, validated_data):
        collision = Collision(**{**validated_data})
        collision.save()
        return collision
