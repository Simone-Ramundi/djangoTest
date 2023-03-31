from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

# Creare model di student

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "student"

# Creare classe PostBlog  con connessione DB
class PostBlog(models.Model):
    titolo = models.CharField(max_length=50)
    contenuto = models.TextField(max_length=1000, null=True)
    autore = models.CharField(max_length=20)
    tag = models.CharField(null=True, max_length=20)
    data = models.DateField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    time = models.TimeField(null=True)

    class Meta:
        db_table = "library"

    def __str__(self):
        return f"{self.titolo} {self.autore}"