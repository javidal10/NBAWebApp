from django.test import TestCase,Client
from django.urls import reverse,resolve


from .models import Player
from .serializers import PlayerSerializer
from .views import targetHeight,Index


class TestUserModel(TestCase):
    """
    This Test case will make sure Player Model & PlayerSerializer be working properly
    """
    def setUp(self):
        self.serialized_data = {
            'first_name' : 'Anthony',
            'last_name' : 'Yoshua',
            'h_in': '71',
            'h_meters': '180'
        }
        self.testModel = Player.objects.create(
            first_name = 'Anthony',last_name = 'Yoshua',h_in = 71,h_meters = 180
        )
        self.testSerializer = PlayerSerializer(data=self.serialized_data)
    
    def test_model_entry(self):
        self.assertTrue(isinstance(self.testModel,Player))
    
    def test_serializer_entry(self):
        self.assertTrue(self.testSerializer.is_valid())


class TestViews(TestCase):
    """
    This test views resolves and url response

    example:
        Detail = func --> targetHeight
        Index = class --> Index
    """
    def setUp(self):
        self.testPlayer1 = Player.objects.create(
            first_name = 'Anthony',last_name = 'Yoshua',h_in = 71,h_meters = 180
        )
        self.testPlayer2 = Player.objects.create(
            first_name = 'John',last_name = 'Jones',h_in = 80,h_meters = 180
        )
        self.client = Client()
        self.index_url = reverse('index')
        self.detail_url = reverse('detail')
        

    def test_index_view_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class,Index)
    
    def test_detail_view_resolves(self):
        url = reverse('detail')
        self.assertEqual(resolve(url).func,targetHeight)
    
    def test_detail_view_entry(self):
        self.context = {
            'height_sum':151
        }
        self.assertEqual(self.client.get(self.detail_url,self.context).status_code,200)
