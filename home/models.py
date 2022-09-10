from django.db import models
from django.template import context
from django.utils.translation import activate, gettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)
from projectsinfo.models import ProjectNews

class HomePage(Page):
    seo_desctiption = models.CharField(_('SEO Description'), max_length=180, default='')
    seo_keywords =  models.CharField(_('SEO Keywords'), max_length=180, default='')

    template = 'home/home_page.html'
    max_count = 1

    def get_context(self, request):
        # https://learnwagtail.com/tutorials/how-to-paginate-your-wagtail-pages/
        # https://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super(HomePage, self).get_context(request)
        all_projects = Page.get_children(self).live()  # Projects index page
        paginator_projects = Paginator(all_projects, 3)
        page_prj = request.GET.get("page_proj")
        try:
            # If the page exists and the ?page=x is an int
            projects_page = paginator_projects.page(page_prj)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            projects_page = paginator_projects.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            projects_page = paginator_projects.page(paginator_projects.num_pages)
        context['proj'] = projects_page

        all_news = ProjectNews.objects.live()  # Projects index page
        # Paginate all posts by 2 per page
        paginator = Paginator(all_news, 3)
        # Try to get the ?page=x value
        page_news = request.GET.get("news")
        try:
            # If the page exists and the ?page=x is an int
            news_posts = paginator.page(page_news)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            news_posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last
            news_posts = paginator.page(paginator.num_pages)

        context['proj_news'] = news_posts
        return context

    class Meta:
        verbose_name = "B2B main page"

    content_panels = Page.content_panels + [

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

    promote_panels = Page.promote_panels + [
        FieldPanel('seo_desctiption'),
        FieldPanel('seo_keywords'),
    ]
