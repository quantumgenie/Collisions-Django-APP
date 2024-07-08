from django.db import models


# Model classes for all the tables in the db

class CollisionSeverity(models.Model):
    col_sev_no = models.IntegerField(null=False, blank=False, primary_key=True)
    col_sev = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.col_sev


class DayOfWeek(models.Model):
    day_of_week_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    day_of_week = models.CharField(max_length=9, null=False, blank=False)

    def __str__(self):
        return self.day_of_week


class RoadClass(models.Model):
    road_class_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    road_class = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.road_class


class RoadType(models.Model):
    road_type_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    road_type = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.road_type


class LightCondition(models.Model):
    light_cond_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    light_cond = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.light_cond


class WeatherCondition(models.Model):
    weather_cond_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    weather_cond = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.weather_cond


class RoadSurfaceCondition(models.Model):
    road_surf_cond_no = models.IntegerField(
        null=False, blank=False, primary_key=True)
    road_surf_cond = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.road_surf_cond


class Collision(models.Model):
    collision_ref = models.IntegerField(null=False, blank=False, db_index=True)
    uk_grid_ref_x = models.IntegerField(null=False, blank=False)
    uk_grid_ref_y = models.IntegerField(null=False, blank=False)
    collision_severity = models.ForeignKey(
        CollisionSeverity, on_delete=models.DO_NOTHING)
    no_of_vehicles = models.IntegerField(null=False, blank=False)
    no_of_casualties = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now=False)
    day_of_week = models.ForeignKey(
        DayOfWeek, on_delete=models.DO_NOTHING)
    road_class = models.ForeignKey(
        RoadClass, on_delete=models.DO_NOTHING)
    road_type = models.ForeignKey(
        RoadType, on_delete=models.DO_NOTHING)
    speed_limit = models.IntegerField(null=False, blank=False)
    light_condition = models.ForeignKey(
        LightCondition, on_delete=models.DO_NOTHING)
    weather_condition = models.ForeignKey(
        WeatherCondition, on_delete=models.DO_NOTHING)
    road_surface_condition = models.ForeignKey(
        RoadSurfaceCondition, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.collision_ref)
