from .views import Animeview,Animepost,RegisterView,AnimeDetail,Animeupdate,AnimeDeleteView
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('all/',Animeview.as_view() ),
    path('anime/<int:pk>/',AnimeDetail.as_view() ),
    path("up/<int:pk>/",Animeupdate.as_view()),
    path("del/<int:pk>/",AnimeDeleteView.as_view()),
    path('post/',Animepost.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view())
]
