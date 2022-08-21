# Generated by Django 4.0.7 on 2022-08-19 19:24

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='About project text')),
                ('parameters', wagtail.fields.StreamField([('params', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add parameter name', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=True)), ('button_url', wagtail.blocks.URLBlock(help_text='Parameters link', required=False))])))]))], blank=True, null=True, use_json_field=None)),
                ('social_data', wagtail.fields.StreamField([('social', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=True)), ('button_url', wagtail.blocks.URLBlock(help_text='Social link', required=False))])))]))], blank=True, null=True, use_json_field=None)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projectimage', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
