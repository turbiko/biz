# Generated by Django 4.0.7 on 2022-09-09 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_desctiption', models.CharField(default='', max_length=180, verbose_name='SEO Description')),
                ('seo_keywords', models.CharField(default='', max_length=180, verbose_name='SEO Keywords')),
            ],
            options={
                'verbose_name': 'B2B main page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
