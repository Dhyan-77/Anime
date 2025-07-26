from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animemodel
from rest_framework.permissions import IsAuthenticated
from .serializers import Animemodelserial
from .serializers import Signupserializers
from rest_framework.generics import RetrieveAPIView



class Animeview(APIView):
    def get(self,request):
        anime = Animemodel.objects.all().order_by("created_at")
        serializer = Animemodelserial(anime, many=True)
        return Response(serializer.data)
    


class Animepost(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = Animemodelserial(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    

class RegisterView(APIView):
    def post(self, request):
        serializer = Signupserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.


class AnimeDetail(RetrieveAPIView):
   
        queryset = Animemodel.objects.all()
        serializer_class = Animemodelserial