from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import SendMessageForm
from . models import Message

class MyMessagesView(LoginRequiredMixin, ListView):
    """Функция для просмотра собственных сообщений пользователя"""
    model = Message
    template_name = 'messages/my_messages.html'
    context_object_name = 'my_messages'
    extra_context = {'title': 'Сообщения пользователя'}

    def get_queryset(self):
        return Message.objects.filter(author_to=self.request.user)

class SendMessageView(LoginRequiredMixin, CreateView):
    """Функция для отправки сообщений пользователю"""
    model = Message
    form_class = SendMessageForm
    template_name = 'messages/send_message.html'
    extra_context = {'title': 'Отправка сообщения пользователя'}

    def get_success_url(self):
        return reverse_lazy('messages:my_messages')
