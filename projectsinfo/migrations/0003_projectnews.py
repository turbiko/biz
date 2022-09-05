# Generated by Django 4.0.7 on 2022-08-29 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectsinfo', '0002_project_body_project_representative_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectNews',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('article_date', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('feature_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]