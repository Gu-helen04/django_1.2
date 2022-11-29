import copy

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_dictionary(dish):
    DATA_copy = DATA.copy()
    if dish == 'omlet':
        context = DATA_copy.get('omlet')
        return context
    elif dish == 'pasta':
        context = DATA_copy.get('pasta')
        return context
    elif dish == 'buter':
        context = DATA_copy.get('buter')
        return context


def total_ingredients(dish, serving):
    total_ingredients_ = {}
    list_of_dishes = recipe_dictionary(dish)
    for ing, amount in list_of_dishes.items():
        total_ingredients_[ing] = amount * serving
    context = {'recipe': total_ingredients_}
    return context


def omlet(request):
    servings = int(request.GET.get("servings", 1))
    context = total_ingredients('omlet', servings)
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    context = total_ingredients('pasta', servings)
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get("servings", 1))
    context = total_ingredients('buter', servings)
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
