from django.db import models
from django.conf import settings
 

User = settings.AUTH_USER_MODEL
# Create your models here.
class Problems(models.Model):
    title = models.TextField()
    problem_statement = models.TextField()
    input_data = models.TextField()
    output_data = models.TextField()
    test_cases = models.TextField()    
    correct_output = models.TextField()
    difficulty = models.IntegerField()
    time_limit = models.IntegerField() #inseconds

    class Meta:
        verbose_name_plural = "Problems"

    def __str__(self):
        return f"{self.title}"


class Submissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problemid = models.IntegerField()
    submit_date = models.DateTimeField(auto_now_add=True, blank=True)
    submit_date.editable=True
    sourcecode = models.TextField()
    verdict = models.TextField()

    class Meta:
        verbose_name_plural = "Submissions"

    def __str__(self):
        return f"{self.user}"

        
class Data(models.Model):
    problemid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    class Meta:
        verbose_name_plural = "Data"

