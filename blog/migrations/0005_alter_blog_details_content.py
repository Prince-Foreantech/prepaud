# Generated by Django 4.1.6 on 2023-02-06 06:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_details_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_details',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
