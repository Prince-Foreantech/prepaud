# Generated by Django 4.1.6 on 2023-02-04 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_seo_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo_discription',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seo.seo_category'),
        ),
    ]