from collections import defaultdict
import csv
import django
import sys
import os

sys.path.append(
    'D:/WORK/University of London/Advanced Web Development/MidTerm/MidTermProject/roadstats/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadstats.settings')

django.setup()
from uk_road_accidents.models import *

collision_sev = set()
day_of_week = set()
road_class = set()
road_type = set()
light_condition = set()
weather_condition = set()
road_surface_condition = set()

data_file = './collision_severity.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        collision_sev.add((row[0], row[1]))

data_file = './day_of_week.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        day_of_week.add((row[0], row[1]))

data_file = './road_class.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        road_class.add((row[0], row[1]))

data_file = './road_type.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        road_type.add((row[0], row[1]))

data_file = './light_condition.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        light_condition.add((row[0], row[1]))

data_file = './weather_condition.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        weather_condition.add((row[0], row[1]))

data_file = './road_surface_condition.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        road_surface_condition.add((row[0], row[1]))

CollisionSeverity.objects.all().delete()
DayOfWeek.objects.all().delete()
RoadClass.objects.all().delete()
RoadType.objects.all().delete()
CollisionSeverity.objects.all().delete()
LightCondition.objects.all().delete()
WeatherCondition.objects.all().delete()

for data in collision_sev:
    row = CollisionSeverity.objects.create(
        col_sev_no=data[0],
        col_sev=data[1]
    )
    row.save()

for data in day_of_week:
    row = DayOfWeek.objects.create(
        day_of_week_no=data[0],
        day_of_week=data[1]
    )
    row.save()

for data in road_class:
    row = RoadClass.objects.create(
        road_class_no=data[0],
        road_class=data[1]
    )
    row.save()

for data in road_type:
    row = RoadType.objects.create(
        road_type_no=data[0],
        road_type=data[1]
    )
    row.save()

for data in light_condition:
    row = LightCondition.objects.create(
        light_cond_no=data[0],
        light_cond=data[1]
    )
    row.save()

for data in weather_condition:
    row = WeatherCondition.objects.create(
        weather_cond_no=data[0],
        weather_cond=data[1]
    )
    row.save()

for data in road_surface_condition:
    row = RoadSurfaceCondition.objects.create(
        road_surf_cond_no=data[0],
        road_surf_cond=data[1]
    )
    row.save()
