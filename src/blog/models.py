from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from model_utils import Choices
from django_xworkflows import models as xwf_models

from ckeditor.fields import RichTextField


class PostWorkflow(xwf_models.Workflow):
    """Defines statuses for Posts."""

    log_model = ''

    states = Choices(
        ('draft', 'Brouillon'),
        ('reviewable', 'En revue'),
        ('published', 'Publié'),
        ('deleted', 'Supprimé'),
    )
    initial_state = 'draft'
    transitions = (
        ('submit', 'draft', 'reviewable'),
        ('publish', 'reviewable', 'published'),
        ('unpublish', ('reviewable', 'published'), 'draft'),
    )


class Post(xwf_models.WorkflowEnabled, models.Model):

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

    status = xwf_models.StateField(
        PostWorkflow,
        verbose_name='Statut')
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
