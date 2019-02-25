from django.db import models


class Employee(models.Model):

    CEO = 'Chief Executive Officer'

    full_name = models.CharField(
        max_length=120,
        verbose_name='Employee Full Name'
    )

    position = models.CharField(
        max_length=120,
        verbose_name='Employee Position'
    )

    join_date = models.DateField(verbose_name='Employee Join Date')

    salary = models.PositiveIntegerField(
        verbose_name='Employee Salary'
    )

    chief = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,  # TODO add set_chief method later
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name

    def get_children(self):
        return Employee.objects.filter(chief=self)

    class Meta:
        db_table = 'employees'
        verbose_name_plural = 'Employees'
        verbose_name = 'Employee'
