from django.db import models
from vote.models import VoteModel
from markupfield.fields import MarkupField


class Build(VoteModel, models.Model):

    GUARDIAN = 1
    WARRIOR = 2
    ENGINEER = 3
    RANGER = 4
    THIEF = 5
    ELE = 6
    MESMER = 7
    NECRO = 8
    REVENANT = 9

    PROFESSIONS = (
        (GUARDIAN, 'Guardian'),
        (WARRIOR, 'Warrior'),
        (ENGINEER, 'Engineer'),
        (RANGER, 'Ranger'),
        (THIEF, 'Thief'),
        (ELE, 'Elementalist'),
        (MESMER, 'Mesmer'),
        (NECRO, 'Necromancer'),
        (REVENANT, 'Revenant'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    build_name = models.CharField("Build Name", max_length=50)

    visible = models.BooleanField("Build Visibility", default=False)

    build_description = models.TextField("Build Description", max_length=200)

    build_usage = MarkupField(markup_type='markdown')

    build_upload_date = models.DateField("build upload date", auto_now_add=True)
    build_last_edit_date = models.DateField("Build's last edit date", auto_now=True)

    gw2skills_link = models.URLField("Link to build on gw2skills.net", null=True)

    # -Build Section
    # --Profession
    profession = models.PositiveSmallIntegerField("Profession ID", null=True, choices=PROFESSIONS)

    # --Weapon sets
    # ---Weapon set #1
    s1mh = models.PositiveSmallIntegerField("Weapon set 1's main hand weapon", null=True)
    s1oh = models.PositiveSmallIntegerField("Weapon set 1's off hand weapon", null=True)
    # ---Weapon set #2
    s2mh = models.PositiveSmallIntegerField("Weapon set 2's main hand weapon", null=True)
    s2oh = models.PositiveSmallIntegerField("Weapon set 2's off hand weapon", null=True)

    # --Slot skills
    heal = models.PositiveIntegerField("Healing skill", null=True)
    uti1 = models.PositiveIntegerField("Utility skill #1", null=True)
    uti2 = models.PositiveIntegerField("Utility skill #2", null=True)
    uti3 = models.PositiveIntegerField("Utility skill #3", null=True)
    elite = models.PositiveIntegerField("Elite skill #1", null=True)

    # --Specializations
    # ---Traitline #1
    t1id = models.PositiveSmallIntegerField("Specialization #1", null=True)
    t1t1 = models.PositiveIntegerField("Spec. #1's Adept Trait", null=True)
    t1t2 = models.PositiveIntegerField("Spec. #1's Master Trait", null=True)
    t1t3 = models.PositiveIntegerField("Spec. #1's Grandmaster Trait", null=True)
    # ---Traitline #2
    t2id = models.PositiveSmallIntegerField("Specialization #2", null=True)
    t2t1 = models.PositiveIntegerField("Spec. #2's Adept Trait", null=True)
    t2t2 = models.PositiveIntegerField("Spec. #2's Master Trait", null=True)
    t2t3 = models.PositiveIntegerField("Spec. #2's Grandmaster Trait", null=True)
    # ---Traitline #3
    t3id = models.PositiveSmallIntegerField("Specialization #3", null=True)
    t3t1 = models.PositiveIntegerField("Spec. #3's Adept Trait", null=True)
    t3t2 = models.PositiveIntegerField("Spec. #3's Master Trait", null=True)
    t3t3 = models.PositiveIntegerField("Spec. #3's Grandmaster Trait", null=True)

    def __str__(self):
        return self.build_name
