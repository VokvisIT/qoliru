from django.db import models

class ModelData(models.Model):
    Data = models.DateField()
    Time = models.TimeField() #
    Resource_Name = models.CharField(max_length=200)
    Header = models.CharField(max_length=200, null=True, blank=True)#
    Text = models.TextField(null=True, blank=True)#
    Comments_Count = models.IntegerField(null=True, blank=True)
    Views = models.IntegerField(null=True, blank=True)
    Rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Count_Positive_Reactions = models.IntegerField(null=True, blank=True)#
    Count_Negative_Reactions = models.IntegerField(null=True, blank=True)#
    Reposts = models.IntegerField(null=True, blank=True)#
    Comment_Text = models.TextField(null=True, blank=True)
    Type = models.CharField(max_length=100)#
    Garbage = models.BooleanField(null=True)
    Healthcare = models.BooleanField(null=True)
    Housing_and_Public_Utilities = models.BooleanField(null=True)
    Education = models.BooleanField(null=True)
    Infrastructure = models.BooleanField(null=True)
    Culture = models.BooleanField(null=True)
    Environmental_Conditions = models.BooleanField(null=True)
    Social_Security = models.BooleanField(null=True)
    Politics = models.BooleanField(null=True)
    Safety = models.BooleanField(null=True)
    Availability_of_Goods_and_Services = models.BooleanField(null=True)
    Official_Statements = models.BooleanField(null=True)
    Tourism = models.BooleanField(null=True)
    Facts = models.BooleanField(null=True)
    Positive = models.BooleanField(null=True)
    Negative = models.BooleanField(null=True)
    Neutral = models.BooleanField(null=True)