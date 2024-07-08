from collections import defaultdict
import csv
import django
import sys
import os

sys.path.append(
    'D:/WORK/University of London/Advanced Web Development/MidTerm/MidTermProject/roadstats')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadstats.settings')

django.setup()
from uk_road_accidents.models import *

data_file = './road-collision2023.csv'

collision = defaultdict(list)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        collision[row[0]] = row[1:14]

Collision.objects.all().delete()

for collision_ref, data in collision.items():

    collision_severity_inst = CollisionSeverity.objects.get(col_sev_no=data[2])
    day_of_week_inst = DayOfWeek.objects.get(day_of_week_no=data[6])
    road_class_inst = RoadClass.objects.get(road_class_no=data[7])
    road_type_inst = RoadType.objects.get(road_type_no=data[8])
    light_condition_inst = LightCondition.objects.get(light_cond_no=data[10])
    weather_condition_inst = WeatherCondition.objects.get(
        weather_cond_no=data[11])
    road_surface_condition_inst = RoadSurfaceCondition.objects.get(
        road_surf_cond_no=data[12])

    row = Collision.objects.create(
        collision_ref=collision_ref,
        uk_grid_ref_x=data[0],
        uk_grid_ref_y=data[1],
        collision_severity=collision_severity_inst,
        no_of_vehicles=data[3],
        no_of_casualties=data[4],
        date=data[5],
        day_of_week=day_of_week_inst,
        road_class=road_class_inst,
        road_type=road_type_inst,
        speed_limit=data[9],
        light_condition=light_condition_inst,
        weather_condition=weather_condition_inst,
        road_surface_condition=road_surface_condition_inst
    )
    row.save()
