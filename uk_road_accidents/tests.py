from django.urls import reverse
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import *


# helper function that deletes db model objects and resets factory sequences

def generalTearDown(self):
    CollisionSeverity.objects.all().delete()
    DayOfWeek.objects.all().delete()
    RoadClass.objects.all().delete()
    RoadType.objects.all().delete()
    LightCondition.objects.all().delete()
    WeatherCondition.objects.all().delete()
    RoadSurfaceCondition.objects.all().delete()
    Collision.objects.all().delete()
    CollisionSeverityFactory.reset_sequence(0)
    DayOfWeekFactory.reset_sequence(0)
    RoadClassFactory.reset_sequence(0)
    RoadTypeFactory.reset_sequence(0)
    LightConditionFactory.reset_sequence(0)
    WeatherConditionFactory.reset_sequence(0)
    RoadSurfaceConditionFactory.reset_sequence(0)
    CollisionFactory.reset_sequence(0)


# Testing collision serializer, SUCCESS/FAIL

class CollisionSerializerTest(APITestCase):
    collision = None
    serializer = None

    def setUp(self):
        self.collision = CollisionFactory.create(pk=111000111)
        self.collisionserializer = CollisionSerializer(instance=self.collision)

    def tearDown(self):
        generalTearDown(self)

    def test_collisionSerializer(self):
        data = self.collisionserializer.data
        self.assertEqual(set(data.keys()), set(['collision_ref', 'uk_grid_ref_x', 'uk_grid_ref_y', 'collision_severity', 'no_of_vehicles',
                                                'no_of_casualties', 'date', 'day_of_week', 'road_class', 'road_type', 'speed_limit',
                                                'light_condition', 'weather_condition', 'road_surface_condition']))

    def test_collisionSerializerIDHasCorrectData(self):
        data = self.collisionserializer.data
        self.assertEqual(data['collision_ref'], 0)


# Testing collision detail, SUCCESS/FAIL/DELETE

class CollisionTest(APITestCase):

    collision1 = None
    collision2 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.collision1 = CollisionFactory.create(pk=111000111)
        self.collision2 = CollisionFactory.create(pk=101010101)
        self.good_url = reverse('api_collision', kwargs={'pk': 111000111})
        self.bad_url = 'api/collision/BAD'
        self.delete_url = reverse('api_collision', kwargs={'pk': 111000111})

    def tearDown(self):
        generalTearDown(self)

    def test_collisionDetailReturnSuccess(self):
        response = self.client.get(self.good_url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_collisionDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_collisionDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)


# Testing collisions list, SUCCESS/FAIL

class CollisionsListTest(APITestCase):

    collision1 = None
    collision2 = None
    collision3 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.collision1 = CollisionFactory.create(pk=111000111)
        self.collision2 = CollisionFactory.create(pk=101010101)
        self.collision3 = CollisionFactory.create(pk=111111111)
        self.good_url = reverse('api_collisions_list')
        self.bad_url = 'api/collisionsBAD'

    def tearDown(self):
        generalTearDown(self)

    def test_collisionsListReturnSuccess(self):
        response = self.client.get(self.good_url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_collisionsListReturnFailOnBadPath(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
