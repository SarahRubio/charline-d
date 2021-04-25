# Generated by Django 3.1.2 on 2021-04-25 11:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='Nom de la compétence')),
                ('slug', models.SlugField(blank=True, help_text='Laissez vide pour que le champ se remplisse seul.', verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description complète de la compétence')),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competences',
            },
        ),
    ]
