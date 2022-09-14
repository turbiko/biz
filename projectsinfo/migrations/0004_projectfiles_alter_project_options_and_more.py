# Generated by Django 4.0.7 on 2022-09-13 17:51

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('projectsinfo', '0003_alter_project_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('content', wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('block_number', wagtail.blocks.IntegerBlock(required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=60, required=True))])))]))], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='content',
        ),
        migrations.DeleteModel(
            name='ProjectFile',
        ),
    ]
