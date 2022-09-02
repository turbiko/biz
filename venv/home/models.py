from django.db import models
from django.template import context
from django.utils.translation import activate, gettext_lazy as _

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)

from project.models import (
    Project,
    ProjectNews,
                            )


class HomePage(Page):
    seo_desctiption = models.CharField(_('SEO Description'), max_length=180, default='')
    seo_keywords =  models.CharField(_('SEO Keywords'), max_length=180, default='')

    template = 'home/home_page.html'
    parent_page_type = ['wagtailcore.Page']
    subpage_types = ['project.Project']
    max_count = 1
    def get_context(self, request): # https://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super(HomePage, self).get_context(request)
        context['projects'] = Project.objects.all()
        context['projects_news'] = ProjectNews.objects.all()
        return context
    class Meta:
        verbose_name = "Main Page"

    content_panels = Page.content_panels + [
        FieldPanel('seo_desctiption'),
        FieldPanel('seo_keywords'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('seo_desctiption'),
        index.SearchField('seo_keywords'),
    ]

    edit_handler = TabbedInterface(
            [
                ObjectList(content_panels, heading=_('Editor content')),
                ObjectList(Page.promote_panels, heading=_('SEO components')),
                ObjectList(Page.settings_panels, heading=_('Page settings')),
            ]
    )
