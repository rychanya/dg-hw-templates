from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as file:
        header = file.readline().strip().split(';')
        data = list(csv.reader(file, delimiter=';'))
    context = {
        'header': header,
        'data': data,
    }
    return render(request, template_name, context)