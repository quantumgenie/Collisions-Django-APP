import factory
from random import randint, choice
from .models import *


# Model factory classes to use for unit testing
# It is used as template to create table entries for the unit testing


class CollisionSeverityFactory(factory.django.DjangoModelFactory):
    col_sev_no = factory.Sequence(lambda n: n)
    col_sev = 'Fatal'

    class Meta:
        model = CollisionSeverity


class DayOfWeekFactory(factory.django.DjangoModelFactory):
    day_of_week_no = factory.Sequence(lambda n: n)
    day_of_week = 'Tuesday'

    class Meta:
        model = DayOfWeek


class RoadClassFactory(factory.django.DjangoModelFactory):
    road_class_no = factory.Sequence(lambda n: n)
    road_class = 'Motorway'

    class Meta:
        model = RoadClass


class RoadTypeFactory(factory.django.DjangoModelFactory):
    road_type_no = factory.Sequence(lambda n: n)
    road_type = 'One way street'

    class Meta:
        model = RoadType


class LightConditionFactory(factory.django.DjangoModelFactory):
    light_cond_no = factory.Sequence(lambda n: n)
    light_cond = 'Daylight'

    class Meta:
        model = LightCondition


class WeatherConditionFactory(factory.django.DjangoModelFactory):
    weather_cond_no = factory.Sequence(lambda n: n)
    weather_cond = 'Raining no high winds'

    class Meta:
        model = WeatherCondition


class RoadSurfaceConditionFactory(factory.django.DjangoModelFactory):
    road_surf_cond_no = factory.Sequence(lambda n: n)
    road_surf_cond = 'Dry'

    class Meta:
        model = RoadSurfaceCondition


class CollisionFactory(factory.django.DjangoModelFactory):
    collision_ref = factory.Sequence(lambda n: n)
    uk_grid_ref_x = randint(400000, 600000)
    uk_grid_ref_y = randint(100000, 200000)
    collision_severity = factory.SubFactory(CollisionSeverityFactory)
    no_of_vehicles = randint(1, 100)
    no_of_casualties = randint(1, 100)
    date = choice(['2024-01-01', '2024-01-02', '2024-01-03'])
    day_of_week = factory.SubFactory(DayOfWeekFactory)
    road_class = factory.SubFactory(RoadClassFactory)
    road_type = factory.SubFactory(RoadTypeFactory)
    speed_limit = choice(range(20, 71, 10))
    light_condition = factory.SubFactory(LightConditionFactory)
    weather_condition = factory.SubFactory(WeatherConditionFactory)
    road_surface_condition = factory.SubFactory(RoadSurfaceConditionFactory)

    class Meta:
        model = Collision
