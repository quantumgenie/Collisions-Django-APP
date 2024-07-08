from django.contrib import admin
from .models import *


# Admin Model used for viewing and manipulating the db in admin mode

class CollisionAdmin(admin.ModelAdmin):
    list_display = ('collision_ref', 'uk_grid_ref_x', 'uk_grid_ref_y', 'collision_severity', 'no_of_vehicles', 'no_of_casualties',
                    'date', 'day_of_week', 'road_class', 'road_type', 'speed_limit', 'light_condition', 'weather_condition', 'road_surface_condition')


class CollisionSeverityAdmin(admin.ModelAdmin):
    list_display = ('col_sev_no', 'col_sev')


class DayOfWeekAdmin(admin.ModelAdmin):
    list_display = ('day_of_week_no', 'day_of_week')


class RoadClassAdmin(admin.ModelAdmin):
    list_display = ('road_class_no', 'road_class')


class RoadTypeAdmin(admin.ModelAdmin):
    list_display = ('road_type_no', 'road_type')


class LightConditionAdmin(admin.ModelAdmin):
    list_display = ('light_cond_no', 'light_cond')


class WeatherConditionAdmin(admin.ModelAdmin):
    list_display = ('weather_cond_no', 'weather_cond')


class RoadSurfaceConditionAdmin(admin.ModelAdmin):
    list_display = ('road_surf_cond_no', 'road_surf_cond')


admin.site.register(Collision, CollisionAdmin)
admin.site.register(CollisionSeverity, CollisionSeverityAdmin)
admin.site.register(DayOfWeek, DayOfWeekAdmin)
admin.site.register(RoadClass, RoadClassAdmin)
admin.site.register(RoadType, RoadTypeAdmin)
admin.site.register(LightCondition, LightConditionAdmin)
admin.site.register(WeatherCondition, WeatherConditionAdmin)
admin.site.register(RoadSurfaceCondition, RoadSurfaceConditionAdmin)
