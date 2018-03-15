from django.db import models
from vote.models import VoteModel
from djrichtextfield.models import RichTextField


class Specializations(VoteModel, models.Model):

    build_name = models.CharField("Build Name", max_length=50)

    build_description = models.TextField("Build Description", max_length=200)

    build_usage = RichTextField()

    build_upload_date = models.DateField("Build upload date", auto_now_add=True)
    build_last_edit_date = models.DateField("Build's last edit date", auto_now=True)

    gw2skills_link = models.URLField("Link to build on gw2skills.net")

#   For buildtemplates traits and skills code generation:
    profession = models.CharField("Profession", max_length=15)

    spec1 = models.IntegerField("Specialization 1", default=0)
    minor1_1 = models.IntegerField("Spec.1 Minor Adept Trait", default=0)
    major1_1 = models.IntegerField("Spec.1 Major Adept Trait", default=0)
    minor1_2 = models.IntegerField("Spec.1 Minor Master Trait", default=0)
    major1_2 = models.IntegerField("Spec.1 Major Master Trait", default=0)
    minor1_3 = models.IntegerField("Spec.1 Minor Grandmaster Trait", default=0)
    major1_3 = models.IntegerField("Spec.1 Major Grandmaster Trait", default=0)

    spec2 = models.IntegerField("Specialization 2", default=0)
    minor2_1 = models.IntegerField("Spec.2 Minor Adept Trait", default=0)
    major2_1 = models.IntegerField("Spec.2 Major Adept Trait", default=0)
    minor2_2 = models.IntegerField("Spec.2 Minor Master Trait", default=0)
    major2_2 = models.IntegerField("Spec.2 Major Master Trait", default=0)
    minor2_3 = models.IntegerField("Spec.2 Minor Grandmaster Trait", default=0)
    major2_3 = models.IntegerField("Spec.2 Major Grandmaster Trait", default=0)

    spec3 = models.IntegerField("Specialization 3", default=0)
    minor3_1 = models.IntegerField("Spec.3 Minor Adept Trait", default=0)
    major3_1 = models.IntegerField("Spec.3 Major Adept Trait", default=0)
    minor3_2 = models.IntegerField("Spec.3 Minor Master Trait", default=0)
    major3_2 = models.IntegerField("Spec.3 Major Master Trait", default=0)
    minor3_3 = models.IntegerField("Spec.3 Minor Grandmaster Trait", default=0)
    major3_3 = models.IntegerField("Spec.3 Major Grandmaster Trait", default=0)

    skill1 = models.IntegerField("Weapon Skill 1", default=0)
    skill2 = models.IntegerField("Weapon Skill 2", default=0)
    skill3 = models.IntegerField("Weapon Skill 3", default=0)
    skill4 = models.IntegerField("Weapon Skill 4", default=0)
    skill5 = models.IntegerField("Weapon Skill 5", default=0)
    skill6 = models.IntegerField("Healing Skill", default=0)
    skill7 = models.IntegerField("Utility Skill 1", default=0)
    skill8 = models.IntegerField("Utility Skill 2", default=0)
    skill9 = models.IntegerField("Utility Skill 3", default=0)
    skill0 = models.IntegerField("Elite Skill", default=0)
