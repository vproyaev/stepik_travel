from random import randint

from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render

from templates.stepik_tours.data import departures, description, title, tours, picture


def main_view(request):
    tour = {}
    while len(tour) != 6:
        for i in range(1, 7):
            ran = randint(1, len(tours))
            tour[ran] = tours[ran]
    context = {
        'tour': tour,
        'title': title,
        'description': description,
        'picture': picture,
        'departures': departures,

    }
    return render(request, 'stepik_tours/index.html', context=context)


def departure_view(request, departure):
    that_departure = {key: that_tour for key, that_tour in tours.items() if that_tour['departure'] == departure}
    price = [i['price'] for i in that_departure.values()]
    nights = [i['nights'] for i in that_departure.values()]
    context = {
        'departures': departures,
        'departure': departures[departure],
        'that_departure': that_departure,
        'amount_departure': len(that_departure),
        'min_price': min(price),
        'max_price': max(price),
        'min_nights': min(nights),
        'max_nights': max(nights),
    }
    return render(request, 'stepik_tours/departure.html', context=context)


def tour_view(request, tour):
    _tour = tours[tour]
    context = {
        'title': _tour['title'],
        'country': _tour['country'],
        'dep': departures[_tour['departure']],
        'nights': _tour['nights'],
        'picture': _tour['picture'],
        'description': _tour['description'],
        'price': _tour['price'],
        'stars': int(_tour['stars']) * '★',
        'departures': departures,
    }
    return render(request, 'stepik_tours/tour.html', context=context)


def custom404(request, exception):
    return Http404('Похоже вы что-то напутали. Лучше вернитесь на главную страницу!')


def custom500(request):
    return HttpResponseNotFound('У-уупс. Подождите-ка! А пока вернитесь на главную!')


def custom503(request):
    return HttpResponseNotFound('Что-то HEROKU мудрит. Подождите пожалуйста =)')
