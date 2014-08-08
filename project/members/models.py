from django.core.urlresolvers import reverse
from django.db import models
from personal_shoppers.models import PersonalShopper
from regions.models import Region


def assign_personal_shopper(region):
    #Exclude inactive personal shoppers and keep those only in the selected region
    personal_shoppers = PersonalShopper.objects.exclude(is_active=False).filter(regions__in=[region])

    #Order by least amount of leads
    shoppers = [
        #[personal_shopper, leads],
    ]
    for personal_shopper in personal_shoppers:
        leads = personal_shopper.member_set.filter(ordered_recently=False).count()
        shoppers.append([personal_shopper, leads])

    #Get the shopper with least amount of leads
    shoppers.sort(key=lambda x: x[1])
    return shoppers[0][0]


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField(blank=True, null=True)
    region = models.ForeignKey(Region)
    personal_shopper = models.ForeignKey(PersonalShopper, blank=True, null=True)
    ordered_recently = models.BooleanField(default=False)  # check this with a cronjob

    def save(self, *args, **kwargs):
        if not self.personal_shopper:
            #Assign to personal shopper with least leads
            self.personal_shopper = assign_personal_shopper(self.region)
        super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s" % self.first_name, self.last_name

    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.pk)])


class Order(models.Model):
    """
    Simulate ordered boxes to generate leads
    """
    member = models.ForeignKey(Member)
    order_date = models.DateField()