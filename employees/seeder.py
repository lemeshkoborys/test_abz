import factory
import factory.django
from .models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Employee

    full_name = factory.Faker('full_name')
    position = factory.Faker('position')
    join_date = factory.Faker('join_date')
    salary = factory.Faker('salary')
    chief = factory.Faker('chief')
