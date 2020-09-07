from django.db import models
from users.models import User

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    business = models.ForeignKey(User, on_delete=models.CASCADE)
    #total_budget = models.IntegerField()
    fb_buget = models.IntegerField()
    insta_budget = models.IntegerField()
    twitter_budget = models.IntegerField()
    is_active = models.BooleanField(default=False)
    #estimated_reach = models.IntegerField()
    current_reach = models.IntegerField(default=0)
    package = models.SmallIntegerField(null=True)
    

    def total_budget(self):
        return self.fb_buget + self.insta_budget + self.twitter_budget
