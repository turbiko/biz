import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate, gettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.models import Page, Orderable
from . import blocks


# Create your models here.
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


def file_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    project_filename= 'prj_file'
    return 'projects/{project_filename}{ext}'.format( project_filename= project_filename, ext= file_extension)


class ProjectFile(Orderable):
    prj_file = models.FileField(upload_to=file_path, max_length=150)
    page = ParentalKey('projectsinfo.Project', related_name='project_file')
    description = models.CharField(max_length=250, null=True, blank=True)
    panels = [
        FieldPanel('prj_file'),
        FieldPanel('description'),
    ]


class Project(Page):
    template = 'projectsinfo'+os.sep+'project.html'
    parent_page_types = ['Projects']
    subpage_types = ['ProjectNews']
    date = models.DateField(auto_now_add=False,  blank=True, null=True)
    representative_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )
    body = RichTextField(blank=True)

    content = StreamField([
        ("cards", blocks.ProjectImagesBlock()),
    ],
            null=True,
            blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        ImageChooserPanel('representative_image'),
        MultiFieldPanel(
                [InlinePanel("project_genres",  label="Genre")],
                heading="Genres",
        ),
        StreamFieldPanel("content"),

    ]
    files_tab_panels = [
        MultiFieldPanel(
                [InlinePanel("project_file", label="Project file")],
                heading="Files",
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(files_tab_panels, heading='Project files'),
        ObjectList(Page.promote_panels, heading='Promote'),
    ])
    def get_context(self, request): # https://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super(Project, self).get_context(request)
        return context

    class Meta:
        ordering = ['date']

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
