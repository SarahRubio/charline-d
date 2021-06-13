from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Recommandation(models.Model):

    name = models.CharField(
        'Nom de la recommandation',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul.',
        blank=True)
    author = models.CharField(
        'Auteur de la recommandation',
        max_length=256,
        db_index=True)
    text = RichTextField(
        'Texte de la recommandation',
        null=True, blank=True)

    class Meta:
        verbose_name = 'Recommandation'
        verbose_name_plural = 'Recommandations'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]