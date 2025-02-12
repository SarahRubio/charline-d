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
    meta_title = models.CharField(
        'Titre (balise meta)',
        max_length=256,
        blank=True,
        default="",
        help_text="Le titre qui sera affiché dans les SERP")
    meta_description = models.CharField(
        'Description (balise meta)',
        max_length=256,
        blank=True,
        default="",
        help_text="La description qui sera affichée dans les SERP")

    class Meta:
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'

    def __str__(self):
        return self.name

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.name)[:50]