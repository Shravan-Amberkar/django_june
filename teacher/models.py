from django.db import models

# Create your models here.
# python manage.py inspectdb

class TeacherCustomerContact(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'teacher_customer_contact'
