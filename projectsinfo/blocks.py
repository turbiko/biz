from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class ProjectImagesBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add your title")
    block_number = blocks.IntegerBlock(required=True)
    cards = blocks.ListBlock( blocks.StructBlock(
            [
                ("file", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=False, max_length=60)),
            ],
    ))

    class Meta:  # noqa
        template = "projectsinfo/project_images.html"
        icon = "placeholder"
        label = "Project Gallery"

