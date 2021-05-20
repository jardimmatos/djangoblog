from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import PublicadoManager
from django.urls import reverse


class Post(models.Model):
    POST_STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    titulo = models.CharField(max_length=250, blank=False, null=True, verbose_name='Título')
    slug = models.SlugField(max_length=250, unique_for_date='publicado_em')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    conteudo = models.TextField(blank=False, null=True, verbose_name='Conteúdo')
    status = models.CharField(max_length=20, choices=POST_STATUS, default='rascunho')
    publicado_em = models.DateTimeField(default=timezone.now)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    publicados = PublicadoManager()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:detail', args=[
            self.publicado_em.year,
            self.publicado_em.month,
            self.publicado_em.day,
            self.slug
            ])

    def get_share_url(self):
        return reverse('blog:share', args=[self.pk])
        

    class Meta:
        ordering = ('-publicado_em',)