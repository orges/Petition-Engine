from datetime import datetime,timedelta
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.flatpages.models import FlatPage
from django.utils.timezone import now
from account.models import Account, Organization

CAMP_STAT_CHOICES = (
    ('1', _('Draft')),
    ('2', _('Publish'))
)

CAMP_OPT_CHOICES = (
    ('1', _('Public')),
    ('2', _('Private')),
    ('3', _('Only Me')),
)


class Campaign(FlatPage):

    date_create = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    date_start = models.DateTimeField(_("Start Date"), default=datetime.now)
    slug = models.SlugField(_("Slug"), unique=True)
    allow_comments = models.BooleanField(_("Allow comments"), default=True)

    date_end = models.DateTimeField(_("End Date"),
                                    default=datetime.now() + timedelta(days=3650))

    status = models.CharField(_("Status"), max_length=2,
                              choices=CAMP_STAT_CHOICES,
                              default=CAMP_STAT_CHOICES[0][0])

    accessibility = models.CharField(_("Accessibility"), max_length=2,
                                     choices=CAMP_OPT_CHOICES,
                                     default=CAMP_OPT_CHOICES[0][0])

    starter_account = models.ForeignKey(Account,
                                        verbose_name=_("Starter Account"),
                                        null=True, blank=True,
                                        on_delete=models.SET_NULL)

    starter_org = models.ForeignKey(Organization,
                                    verbose_name=_("Starter Organization"),
                                    null=True, blank=True,
                                    on_delete=models.SET_NULL)

    deleted_starter = models.CharField(_("Deleted Starter"), max_length=128,
                                       null=True, blank=True)

    def get_starter(self):
        return self.starter_org or self.starter_account or \
               self.deleted_starter or "Deleted User"

