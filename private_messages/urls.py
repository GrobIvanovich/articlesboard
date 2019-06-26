from django.urls import path

from .views import MessageView, CreateMessageView, get_user_autocomplete

app_name = 'private_messages'

urlpatterns = [
    path('create/autocomplete/', get_user_autocomplete),
    path('create/', CreateMessageView.as_view(), name='create_message'),
    path('', MessageView.as_view(), name='messages'),
]
