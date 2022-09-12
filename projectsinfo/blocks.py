from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock

class ProjectImagesBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock( blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=60)),
            ]
    ))

    class Meta:  # noqa
        template = "projectsinfo/project_images.html"
        icon = "placeholder"
        label = "Project Gallery"