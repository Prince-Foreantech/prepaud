# Generated by Django 4.1.6 on 2023-02-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_details_category_blog_details_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_details',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]