from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock

class SocialBlock(blocks.StructBlock):
    """Cards with image and title and link."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=60)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="Social link",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/social_block.html"
        icon = "placeholder"
        label = "URL Social"


class ParamsBlock(blocks.StructBlock):
    """Cards with image and title and link."""

    title = blocks.CharBlock(required=True, help_text="Add parameter name")

    params = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock(required=True, max_length=60)),
                ("param", blocks.CharBlock(required=True, max_length=60)),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/social_block.html"
        icon = "placeholder"
        label = "Parameter"