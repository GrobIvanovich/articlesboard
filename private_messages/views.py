from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
import json


from articles.models import AdvUser
from .models import Message
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
            Message.objects.create(sender=self.request.user.username, receiver=user.username, message=self.request.POST['message'])
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
        messages = Message.objects.filter(sender=self.request.user).order_by('-created_at')
        grouped_messages = dict()
        for msg in messages:
            if msg.receiver in grouped_messages.keys():
                grouped_messages[msg.receiver] = msg
            else:
                grouped_messages[msg.receiver] = msg
        context = {'private_messages': grouped_messages}
        
        return render(self.request, self.template_name, context=context)
