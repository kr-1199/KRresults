from django.db import models

class student(models.Model):
    hall_ticket=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    telugu=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    @property
    def total_marks(self):
        return 600
    @property
    def obtained_marks(self):
        return self.telugu+self.hindi+self.english+self.maths+self.science+self.social
    
    def percentage(self):
        return round((self.obtained_marks/self.total_marks)*100,2)
    def __str__(self):
        return self.name
# Create your models here.

