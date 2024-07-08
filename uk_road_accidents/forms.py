from django import forms
from django.forms import ModelForm
from .models import *


# Models form used for entering data in the db.
# Each model is catered after the model and the fields of each table (Weather Conditon / Collision )

class WeatherConditionForm(ModelForm):
    class Meta:
        model = WeatherCondition
        fields = ['weather_cond_no', 'weather_cond']


class CollisionForm(ModelForm):
    class Meta:
        model = Collision
        fields = ['collision_ref', 'uk_grid_ref_x', 'uk_grid_ref_y', 'collision_severity', 'no_of_vehicles', 'no_of_casualties', 'date',
                  'day_of_week', 'road_class', 'road_type', 'speed_limit', 'light_condition', 'weather_condition', 'road_surface_condition',]

    def clean(self):
        cleaned_data = super(CollisionForm, self).clean()

        # check if the user entered integers in the fields
        fields = [
            "collision_ref",
            "uk_grid_ref_x",
            "uk_grid_ref_y",
            "no_of_vehicles",
            "no_of_casualties",
            "speed_limit"
        ]
        for field in fields:
            value = cleaned_data.get(field)
            if not self.is_integer(value):
                raise forms.ValidationError(
                    f"{field.replace('_', ' ').capitalize()} has to be an integer")

            # check if speed limit entered is a multiple of 10
            if field == "speed_limit":
                if int(value) % 10 != 0:
                    raise forms.ValidationError(f"{field.replace(
                        '_', ' ').capitalize()} has to be a multiple of 10")

    def is_integer(self, value):
        try:
            int(value)
            return True
        except (TypeError, ValueError):
            return False
