from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)

from streams import blocks

# Create your models here.

class Project(Page):
    image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.PROTECT,
                                           related_name="projectimage")
    description = RichTextField(_("About project text"), null=True, blank=True,)

    parameters = StreamField([
        ("params", blocks.ParamsBlock()),
    ],
            null=True,
            blank=True,
    )

    social_data = StreamField([
        ("social", blocks.SocialBlock()),
    ],
            null=True,
            blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('description'),
        StreamFieldPanel("parameters"),
        StreamFieldPanel("social_data"),
    ]