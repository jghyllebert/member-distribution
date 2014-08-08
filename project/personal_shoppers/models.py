from django.core.urlresolvers import reverse
from django.db import models
from regions.models import Region


class PersonalShopper(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    regions = models.ManyToManyField(Region, null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % self.first_name, self.last_name

    def get_absolute_url(self):
        return reverse('p_shopper_detail', args=[str(self.pk),])