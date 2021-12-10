from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
import requests,json
from .models import Player
from .serializers import PlayerSerializer


# Create your views here.

class PlayerView(APIView):
    """
    this view creates  DRF interface for the user to get the data from a custom API or connect to frontend
    """

    def put(self,format=None):
        """
        This function fetch the data form API of mac-eight into our custom database, is meant to be the first step to configure database.
        """
        api_data = requests.get('https://mach-eight.uc.r.appspot.com/')
        if api_data.status_code == 200:
            info = json.loads(api_data.text)
            serializer = PlayerSerializer(data=info['values'],many=True)
            if serializer.is_valid():
                serializer.save()
                return Response('Succesful DataStream')
            return Response('unsuccesful Updated data Stream')

    def get(self,format=None):
        """
        This will get data serialized as a JSON Object:

        output:
        {"id": 768,"first_name": "Nate","last_name": "Robinson","h_in": 69,"h_meters": 1.75},
        """
        players = Player.objects.all().order_by('h_in')
        serializer = PlayerSerializer(players,many=True)
        return Response(serializer.data)

class Index(TemplateView):
    """
    This index ask the user for the target value
    """
    template_name = 'index.html'

def targetHeight(request):
    target = int(request.GET['height_sum'])
    all_players = Player.objects.all().order_by('h_in')
    tup = []
    for player in all_players:
        tup.append((player.id,player.h_in))
    
    l = 0
    h = len(tup)-1

    def two_sum(tup=tup,l=l,h=h,target=target):
        """
        This function iterates trough the Data table and gets all the sum values that matches the target value

        output:
        [player:<name player1>,player:<name player2>...player:<name player n>,player:<name player n+1>]  

        """
        arr = []
        while l<=h:
            if (tup[l][1]+tup[h][1])== target:
                p1 = Player.objects.get(id = tup[l][0])
                p2 = Player.objects.get(id= tup[h][0])
                arr.append((p1,p2))
                l+=1
                h-=1

            elif (tup[l][1]+tup[h][1]) < target:
                l+=1

            else :
                h-=1

        if arr == []:
            arr.append('NO MATCHES FOUND')
            return arr

        return arr

    context = {
        'LOP': two_sum()
    }
    
    return render(request,'detail.html',context)

        
       
    

