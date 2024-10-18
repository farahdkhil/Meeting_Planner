
from django.urls import path
from meetings.views import delete, detail, meetings_list_view,add,update

urlpatterns = [
    path('',meetings_list_view,name='meetings_list_view'),
    path('detail/<int:id>/',detail,name='detail'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
    path('add',add,name='add'),
]