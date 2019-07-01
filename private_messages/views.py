from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
import json


from articles.models import AdvUser
from .models import Message, Dialog
from .forms import CreateMessageForm


def get_user_autocomplete(request):

    users = AdvUser.objects.filter(username__contains=request.POST['username']).order_by('username')[0:5]
    users_json = json.dumps(list(users.values('username')))

    return JsonResponse({'users': users_json})


class DialogsView(View, LoginRequiredMixin):
    
    template_name = 'private_messages/dialogs.html'
    
    def get(self, *args, **kwargs):
        dlg = Dialog.objects.filter(members=self.request.user).distinct()
        return render(self.request, self.template_name, context={'dialogs': dlg})


class DialogMessagesView(UpdateView, LoginRequiredMixin):
    
    template_name = 'private_messages/dialog_page.html'
    dialog = Dialog.objects.none()
    
    def get(self, *args, **kwargs):
        form = CreateMessageForm(initial={'sender': self.request.user.username})
        self.dialog = Dialog.objects.get(id=kwargs['dlg_id'])
        user_messages = Message.objects.filter(dialog=kwargs['dlg_id']).order_by('-created_at')
        
        return render(self.request, self.template_name, context={'user_messages': user_messages, 'dialog': self.dialog, 'form': form})
    
    def post(self, *args, **kwargs):
        form = CreateMessageForm(self.request.POST, self.request.FILES, initial={'sender': self.request.user.username})
        if not self.dialog:
            self.dialog = Dialog.objects.get(id=self.request.POST['dlg_id'])
        Message.objects.create(
            sender=self.request.POST['sender'],
            receiver=self.request.POST['receiver'],
            message=self.request.POST['message'],
            dialog=self.dialog,
        )
        
        user_messages = Message.objects.filter(dialog=self.request.POST['dlg_id']).order_by('-created_at')
        # messages = Message.objects.filter((Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)) & Q(dialog=dlg)).order_by('-created_at')
        users = {'sender': user_messages[0].sender, 'receiver': user_messages[0].receiver}
        print(users)
        return render(self.request, self.template_name, context={'user_messages': user_messages, 'dialog': self.dialog, 'form': form, 'users': users})



# class CreateMessageView(CreateView, LoginRequiredMixin):
    
#     template_name = 'private_messages/create_message.html'
#     model = Message
#     form_class = CreateMessageForm
    
#     def get(self, *args, **kwargs):
#         form = CreateMessageForm(initial={'sender': self.request.user.username})
#         return render(self.request, self.template_name, context={'form': form})
    
#     def post(self, *args, **kwargs):
#         form = CreateMessageForm(self.request.POST)
#         user = get_object_or_404(AdvUser, username=self.request.POST['receiver'])
#         if form.is_valid():
#             # print('valid')
#             dlg = Dialog()
#             try:
#                 # If message was sent to other user.
#                 if self.request.user.__ne__(user):
#                     dlg = Dialog.objects.prefetch_related('members').filter(members=user).filter(members=self.request.user).distinct()
#                 # If message was sent to yourself.
#                 else:
#                     dlg = Dialog.objects.prefetch_related('members').filter(message__sender=self.request.user).filter(message__receiver=user).distinct()
#                 print(dlg)
#                 if len(dlg) == 0:
#                     raise Dialog.DoesNotExist
#                 else:
#                     print(f'Exists -- {dlg}')
#                     dlg = dlg[0]

#             except Dialog.DoesNotExist:
#                 users = AdvUser.objects.filter(Q(username=self.request.user.username) | Q(username=user.username))
#                 print(f'Not exists -- {users}')
#                 instance = Dialog.objects.create()
#                 instance.members.add(*users)
#                 dlg = instance
                
#             Message.objects.create(dialog=dlg, sender=self.request.user.username, receiver=user.username, message=self.request.POST['message'])

            
#         else:
            
#             return redirect('private_messages:dialogs')
        
#         dlg = Dialog.objects.get(id=self.request.POST['id'])
#         user_messages = Message.objects.filter(Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)).order_by('-created_at')
        
#         return render(self.request, 'private_messages/dialog_page.html', context={'dialog': dlg, 'user_messages': user_messages, 'form': form})
        
#     class Meta:
#         model = Message
#         fields = ('__all__', )
            

# # class DialogMessageView(UpdateView, LoginRequiredMixin):
    
# #     template_name = 'private_messages/create_message.html'
# #     model = Message
# #     form_class = CreateMessageForm
    
# #     def get(self, *args, **kwargs):
# #         form = CreateMessageForm(initial={'sender': self.request.user.username})
# #         # receiver = 
# #         return render(self.request, self.template_name, context={'form': form})
    
# #     def post(self, *args, **kwargs):
# #         form = CreateMessageForm(self.request.POST)
# #         user = get_object_or_404(AdvUser, username=self.request.POST['receiver'])
# #         if form.is_valid():
# #             # print('valid')
# #             dlg = Dialog()
# #             try:
# #                 # If message was sent to other user.
# #                 if self.request.user.__ne__(user):
# #                     dlg = Dialog.objects.prefetch_related('members').filter(members=user).filter(members=self.request.user).distinct()
# #                 # If message was sent to yourself.
# #                 else:
# #                     dlg = Dialog.objects.prefetch_related('members').filter(message__sender=self.request.user).filter(message__receiver=user).distinct()
# #                 print(dlg)
# #                 if len(dlg) == 0:
# #                     raise Dialog.DoesNotExist
# #                 else:
# #                     print(f'Exists -- {dlg}')
# #                     dlg = dlg[0]

# #             except Dialog.DoesNotExist:
# #                 users = AdvUser.objects.filter(Q(username=self.request.user.username) | Q(username=user.username))
# #                 print(f'Not exists -- {users}')
# #                 instance = Dialog.objects.create()
# #                 instance.members.add(*users)
# #                 dlg = instance
                
# #             Message.objects.create(dialog=dlg, sender=self.request.user.username, receiver=user.username, message=self.request.POST['message'])

            
# #         else:
            
# #             return redirect('private_messages:dialogs')
        
# #         dlg = Dialog.objects.get(id=self.request.POST['id'])
# #         user_messages = Message.objects.filter(Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)).order_by('-created_at')
        
# #         return render(self.request, 'private_messages/dialog_page.html', context={'dialog': dlg, 'user_messages': user_messages, 'form': form})
        
# #     class Meta:
# #         model = Message
# #         fields = ('__all__', )




# # Add getting messages not only by a sender field.
# class MessageView(CreateView, UpdateView, LoginRequiredMixin):
    
#     template_name = 'private_messages/dialogs.html'
#     model = Message
    
#     def get(self, *args, **kwargs):
#         dialogs = Dialog.objects.filter(members=self.request.user)
#         print(dialogs)
#         messages = Message.objects.filter(Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)).order_by('-created_at')
#         print(messages)
#         return render(self.request, self.template_name, context={'dialogs': dialogs})


# class DialogView(CreateView, UpdateView, LoginRequiredMixin):
    
#     template_name = 'private_messages/dialog_page.html'
#     model = Dialog
    
#     # def get(self, *args, **kwargs):
#     #     dlg = Dialog.objects.get(id=self.request.GET['dialog_id'])
#     #     return render(self.request, 'private_messages/dialog_page.html', context={'dialog': dlg})
    
#     def post(self, *args, **kwargs):
#         dlg = Dialog.objects.get(id=self.request.POST['id'])
#         messages = Message.objects.filter((Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)) & Q(dialog=dlg)).order_by('-created_at')
#         users = {'sender': messages[0].sender, 'receiver': messages[0].receiver}
#         print(users)
        # return render(self.request, 'private_messages/dialog_page.html', context={'dialog': dlg, 'user_messages': messages, 'users': users })
