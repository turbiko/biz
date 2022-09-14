import os
from datetime import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate, gettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.models import Page, Orderable
from . import blocks


# Genres functionality
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectGenres(Orderable):
    genre = models.ForeignKey(Genre, related_name='+', null=True, on_delete=models.SET_NULL)
    page = ParentalKey('projectsinfo.Project', related_name='project_genres')
    panels = [
        FieldPanel('genre'),
    ]
# end Genres functionality

def file_path(instance, filename):
    print('file_path Instance= ', instance)
    basefilename, file_extension= os.path.splitext(filename)
    filename= datetime.now().strftime('%Y/%m/%d/')+'file-'+uuid.uuid4().hex
    return 'projects/{project_filename}{ext}'.format( project_filename= filename, ext= file_extension)


class Project(Page):
    template = 'projectsinfo'+os.sep+'project.html'
    parent_page_types = ['Projects']
    subpage_types = ['ProjectNews', 'ProjectFiles']
    date = models.DateField(auto_now_add=False,  blank=True, null=True)
    representative_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        ImageChooserPanel('representative_image'),
        MultiFieldPanel(
                [InlinePanel("project_genres",  label="Genre")],
                heading="Genres",
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
    def get_context(self, request): # https://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super(Project, self).get_context(request)
        context['files'] = self.get_children().type(ProjectFiles)
        return context

    class Meta:
        ordering = ['-date']

class Projects(Page):
    template = 'projectsinfo'+os.sep+'projects.html'
    max_count = 1
    subpage_types = ['Project']
    parent_page_types = ['home.HomePage']
    page_description = "Projects index page"


class ProjectNews(Page):
    template = 'projectsinfo'+os.sep+'project_news.html'
    parent_page_types = ['Project']
    subpage_types = []
    page_description = "current project news"
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
    article_date = models.DateField(verbose_name=_('Created'), auto_now_add=True,)
    description  = RichTextField(blank=True)

    feature_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('description'),
        ImageChooserPanel('feature_image'),
    ]


class ProjectAllNews(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
    page_description = "All projects news"


class ProjectFiles(Page):
    parent_page_types = ['Project']
    subpage_types = []
    representative_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )
    description = models.CharField(max_length=250, null=True, blank=True)
    content = StreamField([
        ("cards", blocks.ProjectImagesBlock()),
    ],
            null=True,
            blank=True,
    )

    panels = [
        FieldPanel('description'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    def get_context(self, request): # https://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super().get_context(request)

        return context