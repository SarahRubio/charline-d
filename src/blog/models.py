from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from model_utils import Choices

from ckeditor.fields import RichTextField


STATUS_CHOICES = Choices(
    ('draft', 'Brouillon'),
    ('reviewable', 'En revue'),
    ('published', 'Publié'),
    ('deleted', 'Supprimé'),
)

class Post(models.Model):

    title = models.CharField(
        'Titre de l\'article',
        max_length=256,
        db_index=True)
    author = models.CharField(
        'Auteur de l\'article',
        max_length=256,
        db_index=True)
    slug = models.SlugField(
        'Slug',
        help_text='Laissez vide pour que le champ se remplisse seul',
        blank=True)
    text = RichTextField(
        'corps de l\'article',
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


    status = models.CharField(
        verbose_name='Statut',
        choices=STATUS_CHOICES,
        default="draft",
        max_length=256,
    )
    date_created = models.DateTimeField(
        'Date de création',
        default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def set_slug(self):
        """Set the object's slug if it is missing."""
        if not self.slug:
            self.slug = slugify(self.title)[:50]

    def is_draft(self):
        return self.status == PostWorkflow.states.draft

    def is_published(self):
        return self.status == PostWorkflow.states.published
