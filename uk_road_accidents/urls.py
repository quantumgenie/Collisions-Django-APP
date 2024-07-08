from django.urls import path
from . import views
from . import api


# URL paths we use to access pages in out app that contain DB data

urlpatterns = [
    path('',  views.CollisionList.as_view(), name='index'),
    path('collision/<int:pk>', views.CollisionDetail.as_view(), name='collision'),
    path('list/<int:collision_severity>', views.CollisionListBySeverity.as_view(),
         name='list'),
    path('date/<str:date>', views.CollisionListByDate.as_view(), name='date'),
    path('delete/<int:pk>', views.CollisionDelete.as_view(), name='delete'),
    path('add_weather_condition/', views.WeatherConditionAdd.as_view(),
         name='add_weather_condition'),
    path('add_collision/', views.CollisionAdd.as_view(), name='add_collision'),
    path('update/<int:pk>', views.CollisionUpdate.as_view(), name='update'),
    path('api/collision/<int:pk>', api.CollisionDetails.as_view(),
         name='api_collision'),
    path('api/collisions/', api.CollisionList.as_view(),
         name='api_collisions_list'),
]
