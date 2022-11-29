from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as csv_file:
        station_list = csv.DictReader(csv_file, delimiter=",")
        page_number = request.GET.get("page", 1)
        paginator = Paginator(list(station_list), 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
