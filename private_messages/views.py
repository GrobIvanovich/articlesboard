from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
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


class CreateMessageView(CreateView, LoginRequiredMixin):
    
    template_name = 'private_messages/create_message.html'
    model = Message
    form_class = CreateMessageForm
    
    def get(self, *args, **kwargs):
        form = CreateMessageForm(initial={'sender': self.request.user.username})
        return render(self.request, self.template_name, context={'form': form})
    
    def post(self, *args, **kwargs):
        form = CreateMessageForm(self.request.POST)
        user = get_object_or_404(AdvUser, username=self.request.POST['receiver'])
        if form.is_valid():
            print('valid')
            dl = Dialog.objects.filter(members__contains=self.request.user.username)
            Message.objects.create(dialog=dl, sender=self.request.user.username, receiver=user.username, message=self.request.POST['message'])
            # messages.add_message(self.request, messages.SUCCESS, 'Сообщение успешно отправлено')
            
        else:
            # messages.add_message(self.request, messages.ERROR, 'Форма не валидна')
            return redirect('private_messages:messages')
        
        return HttpResponseRedirect(reverse_lazy('private_messages:messages'))
        
    class Meta:
        model = Message
        fields = ('__all__', )
            
    

# Add getting messages not only by a sender field.
class MessageView(CreateView, UpdateView, LoginRequiredMixin):
    
    template_name = 'private_messages/messages.html'
    model = Message
    
    def get(self, *args, **kwargs):
        messages = Message.objects.filter(Q(receiver=self.request.user.username) | Q(sender=self.request.user.username)).order_by('-created_at')
        dialogs = dict()
        for msg in messages:
            if msg.receiver in dialogs.keys():
                dialogs[msg.receiver].append(msg)
            else:
                dialogs[msg.receiver] = msg
        context = {'dialogs': dialogs}
        
        return render(self.request, self.template_name, context=context)


class DialogView(CreateView, UpdateView, LoginRequiredMixin):
    
    template_name = 'private_messages/dialog.html'
    model = Message
    
    def get(self, *args, **kwargs):
        messages = Message.objects.filter(sender=self.request.user).order_by('-created_at')