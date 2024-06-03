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



class Region(models.Model):
    """
    Класс региона (Архангельск, Якутия)
    """
    name = models.CharField(max_length=100)
    subject_code = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)# Широта
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)# Долгота
    
    def __str__(self):
        return str(self.name)


class Source(models.Model):
    """
    Источник (VK, Telegramm)
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f'{self.name} + {self.region}')

class Resource(models.Model):
    """
    Ресурс парсинга (Арх.Онлайн и т.п.)
    """
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class ModelDataTest(models.Model):
    """
    Тестовая модель для данных
    """
    data = models.DateField()
    time = models.TimeField()

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    text = models.TextField(null=True, blank=True)
    comment_text = models.TextField(null=True, blank=True)
    type_text = models.CharField(max_length=100)
    
    category = models.CharField(max_length=100)
    tonality = models.CharField(max_length=100)
