# Generated by Django 4.0.7 on 2022-09-14 11:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('projectsinfo', '0006_alter_projectfiles_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfiles',
            name='representative_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='projectfiles',
            name='content',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('block_number', wagtail.blocks.IntegerBlock(required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
