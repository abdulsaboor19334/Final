from django.db import models
from users.models import User


class Cpv(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fb_cpv = models.DecimalField(decimal_places=2,max_digits=3)
    insta_cpv = models.DecimalField(decimal_places=2,max_digits=3)
    twitter_cpv = models.DecimalField(decimal_places=2,max_digits=3)


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
    
    def fb_reach(self):
        cost = Cpv.objects.all().order_by('-date')[0].fb_cpv
        return int(self.fb_buget/cost)
    
    def fb_qtty(self):
        return self.fb_reach()/1000

    def insta_reach(self):
        cost = Cpv.objects.all().order_by('-date')[0].insta_cpv
        return int(self.fb_buget/cost)

    def insta_qtty(self):
        return self.insta_reach()/1000

    def twitter_reach(self):
        cost = Cpv.objects.all().order_by('-date')[0].twitter_cpv
        return int(self.fb_buget/cost)
    
    def total_reach(self):
        insta = self.insta_reach()
        twitter = self.twitter_reach()
        fb = self.fb_reach()
        total = fb + insta + twitter
        return int(total)
    
    def percentage_reach(self):
        total = self.total_reach()
        current = self.current_reach
        per = current/total
        percentage = per*100
        return int(percentage)