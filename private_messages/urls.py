from django.urls import path

from .views import get_user_autocomplete, DialogsView, DialogMessagesView
# from .views import DialogsView, MessagesView, CreateDialogView

app_name = 'private_messages'

urlpatterns = [
    # path('dialogs/', DialogsView.as_view(), name='dialogs'),
    # path('dialogs/create/<int:user_id>/', CreateDialogView.as_view(), name='create_dialog'),
    # url(r'^dialogs/(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
    # path('dialogs/', DialogView.as_view(), name='show_dialog'),
    path('create/autocomplete/', get_user_autocomplete),
    # path('create/', CreateMessageView.as_view(), name='create_message'),
    path('dialog/<int:dlg_id>/', DialogMessagesView.as_view(), name='dialog_page'),
    path('', DialogsView.as_view(), name='dialogs'),
]
