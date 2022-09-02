# Generated by Django 4.0.7 on 2022-08-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Main Page'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_desctiption',
            field=models.CharField(default='', max_length=180, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_keywords',
            field=models.CharField(default='', max_length=180, verbose_name='SEO Keywords'),
        ),
    ]
