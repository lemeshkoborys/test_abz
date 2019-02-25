from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Employee


def render_employees(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 5)

    page = request.GET.get('page')
    employees = paginator.get_page(page)
    return render(request, 'employees/employees_tree.html', {'employees': employees})
