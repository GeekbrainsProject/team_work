import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, UserProfile


# Create your models here.
class Article(models.Model):
    guid = models.CharField(primary_key=True, max_length=64, editable=False, default=uuid.uuid4, db_column='guid')
    author_id = models.ForeignKey(User, db_column='author_id', on_delete=models.CASCADE)
    creation_date = models.DateField(db_column='creation_date', auto_now_add=True)
    topic = models.CharField(max_length=1024, null=False)
    article_body = models.TextField(null=False)
    blocked = models.BooleanField(default=False)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return f'Статья {self.topic}, ' \
               f'автор: {self.author_id.email} ' \
               f'от {self.creation_date}'


class ArticleHistory(models.Model):
    CREATE = 'Создание'
    EDIT = 'Изменение'
    BLOCK = 'Блокировка'

    ARTICLE_STATUSES = (
        (CREATE, 'Создание'),
        (EDIT, 'Редактирование'),
        (BLOCK, 'Блокировка')
    )

    guid = models.CharField(primary_key=True, max_length=64, editable=False, default=uuid.uuid4, db_column='guid')
    article_uid = models.ForeignKey(Article, db_column='article_uid', on_delete=models.CASCADE)
    changer_id = models.ForeignKey(User, verbose_name='Автор изменения', db_column='editor_id',
                                   on_delete=models.DO_NOTHING)
    record_date = models.DateTimeField(verbose_name='Дата изменения', auto_now_add=True)
    change_type = models.CharField(verbose_name='Вид изменения', max_length=1024, choices=ARTICLE_STATUSES)

    def __str__(self):
        return f'Статья {self.article_uid.topic}, ' \
               f'автор: {self.article_uid.author_id.email} ' \
               f'изменение {self.change_type} ' \
               f'от {self.record_date}, ' \
               f'автор: {self.changer_id}'

    @receiver(post_save, sender=Article)
    def create_article(sender, instance, created, **kwargs):
        if created:
            ArticleHistory.objects.create(changer_id=instance.author_id, article_uid=instance, change_type='Создание')
        else:
            if instance.blocked:
                ArticleHistory.objects.create(changer_id=instance.author_id, article_uid=instance,
                                              change_type='Удаление')
            else:
                ArticleHistory.objects.create(changer_id=instance.author_id, article_uid=instance,
                                              change_type='Редактирование')