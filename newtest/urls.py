from django.urls import path
from .views import Index, Search, Find, Detail, Nothing, Login, Register, Logout

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('search/', Search.as_view(), name='search'),
    path('find/', Find.as_view(), name='find'),
    path('nothing/', Nothing.as_view(), name='nothing'),
    path('detail/<int:id>', Detail.as_view(), name='detail'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),

]
