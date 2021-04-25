from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Competence( models.Model):

    name = models.CharField(
        'Nom de la compétence',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul.',
        blank=True)
    description = RichTextField(
        'Description complète de la compétence',
        null=True, blank=True)

    class Meta:
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]