# Generated by Django 3.2.3 on 2021-05-29 15:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='specs',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
