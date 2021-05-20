from django.db import models

class PublicadoManager(models.Manager):

    def get_queryset(self):
        return super(PublicadoManager, self)\
            .get_queryset()\
                .filter(status='publicado')
