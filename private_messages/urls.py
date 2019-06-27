from django.urls import path

from .views import get_user_autocomplete, MessageView, CreateMessageView
# from .views import DialogsView, MessagesView, CreateDialogView

app_name = 'private_messages'

urlpatterns = [
    # path('dialogs/', DialogsView.as_view(), name='dialogs'),
    # path('dialogs/create/<int:user_id>/', CreateDialogView.as_view(), name='create_dialog'),
    # url(r'^dialogs/(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
    path('create/autocomplete/', get_user_autocomplete),
    path('create/', CreateMessageView.as_view(), name='create_message'),
    path('', MessageView.as_view(), name='dialogs'),
]
