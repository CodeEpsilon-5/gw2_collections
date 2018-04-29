from django.db import models
from vote.models import VoteModel
from markupfield.fields import MarkupField


class Build(VoteModel, models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    build_name = models.CharField("Build Name", max_length=50)

    build_description = models.TextField("Build Description", max_length=200)

    build_usage = MarkupField(markup_type='markdown')

    build_upload_date = models.DateField("build upload date", auto_now_add=True)
    build_last_edit_date = models.DateField("Build's last edit date", auto_now=True)

    gw2skills_link = models.URLField("Link to build on gw2skills.net", null=True)

    traits = models.CharField("Traits, Deltaconnected-style decoded(Base64)", max_length=27, null=True)
    skills = models.CharField("Skills, Deltaconnected-style decoded(Base64)", max_length=23, null=True)

    def __str__(self):
        return self.build_name
