from ast import Or
import re
from django.db import connection
from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################


def student_list(request):

    posts = Student.objects.all()

    print('queryset------>>>>>', posts)
    print()
    print('hello i am sql query------>>>>', posts.query)
    print()
    print('sql query information------>>>>', connection.queries)

    return render(request, 'output.html', {'posts': posts})

# or queries


def student_list(request):
    posts = Student.objects.filter(
        Q(surname__startswith="a")) | Student.objects.filter(Q(firstname__endswith="a"))
    print()
    print("i am filter---------->>>>", posts)
    return render(request, 'output.html', {'posts': posts})

# unionThe SQL UNION clause/operator is used to combine the results of
# two or more SELECT statements without returning any duplicate rows


def student_list(request):
    data = Student.objects.all().values_list("firstname").union(
        Teacher.objects.all().values_list("firstname"))
    print('data union------>>>>', data)
    print()
    print("connection union------->>>>>", connection.queries)
    return render(request, 'output.html', {'data': data})


# Select and Output individual fields example
# lt
# gt
# gte
# lte
def student_list(request):
    data = Student.objects.filter(age__lte=20).only('firstname')
    print('data only------>>>>', data)
    print()
    print("connection only------->>>>>", connection.queries)
    return render(request, 'output.html', {'data': data})

# Performing raw SQL queries


def student_list(request):
    data = Student.objects.raw('SELECT * from student_student')
    print(' raw SQL queries------>>>>', data)
    print()
    print("connection  raw SQL queries------->>>>>", connection.queries)
    return render(request, 'output.html', {'data': data})

###############################
# Performing raw SQL queries without the ORM


def student_list(request):
    cursor = connection.cursor()
    cursor.execute("select count(*) from student_student")
    r = cursor.fetchone()
    print(r)
    return render(request, 'output.html', {'data': r})
