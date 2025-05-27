from django.urls import path

from .views import MyMessagesView, SendMessageView

app_name = 'messages'

urlpatterns = [
    path('my_messages/', MyMessagesView.as_view(), name='my_messages'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
]