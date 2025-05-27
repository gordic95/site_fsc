from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    author_from = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Автор сообщения'))
    author_to = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='messages_received', verbose_name=_('Получатель сообщения'))
    message = models.TextField(verbose_name=_('Сообщение'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    is_read = models.BooleanField(default=False, verbose_name=_('Прочитано'))


    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')


    def __str__(self):
        return f'{self.author_to}: {self.message}'