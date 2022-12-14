# Generated by Django 4.0.7 on 2022-09-12 14:16

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projectsinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=True))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
