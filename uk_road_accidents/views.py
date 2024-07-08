from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import *
from .forms import *

# View classes that retrieve DB data and work with URL paths and HTML pages to display it the App UI


# Show list of all collisions in the DB table

class CollisionList(ListView):
    model = Collision
    context_object_name = 'master_collisions'
    template_name = 'uk_road_accidents/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collision_dates'] = Collision.objects.values_list(
            'date', flat=True).distinct()
        return context


# Show details of an entry in the Ccllision table

class CollisionDetail(DetailView):
    model = Collision
    context_object_name = 'collision'
    template_name = 'uk_road_accidents/collision.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_collisions'] = Collision.objects.all()
        return context


# List of collisions by severity

class CollisionListBySeverity(ListView):
    model = Collision
    context_object_name = 'master_collisions'
    template_name = 'uk_road_accidents/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collisions'] = Collision.objects.filter(
            collision_severity__exact=self.kwargs['collision_severity'])
        severity = CollisionSeverity.objects.get(
            col_sev_no__exact=self.kwargs['collision_severity'])
        context['severity_type'] = severity.col_sev
        return context


# List of collisions by severity

class CollisionListByDate(ListView):
    model = Collision
    context_object_name = 'master_collisions'
    template_name = 'uk_road_accidents/list_by_date.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collisions'] = Collision.objects.filter(
            date=self.kwargs['date'])
        return context


# Delete entry from Collision table

class CollisionDelete(DeleteView):
    model = Collision
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_collisions'] = Collision.objects.all()
        return context


# Update entry in Collision table

class CollisionUpdate(UpdateView):
    model = Collision
    fields = ['collision_ref', 'uk_grid_ref_x', 'uk_grid_ref_y', 'collision_severity', 'no_of_vehicles', 'no_of_casualties', 'date',
              'day_of_week', 'road_class', 'road_type', 'speed_limit', 'light_condition', 'weather_condition', 'road_surface_condition',]
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_collisions'] = Collision.objects.all()
        return context


# Add new weather condition to the Weather Condition table

class WeatherConditionAdd(CreateView):
    model = WeatherCondition
    template_name = 'uk_road_accidents/add_weather_cond.html'
    form_class = WeatherConditionForm
    success_url = "/add_weather_condition/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_collisions'] = Collision.objects.all()
        context['weather_conditions'] = WeatherCondition.objects.all()
        return context


# Add a new entry to the Collision table

class CollisionAdd(CreateView):
    model = Collision
    template_name = 'uk_road_accidents/add_collision.html'
    form_class = CollisionForm
    success_url = "/add_collision/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_collisions'] = Collision.objects.all()
        return context
