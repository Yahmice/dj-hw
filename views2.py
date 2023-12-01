from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    for dishes, ingredients in DATA.items():
        if dishes == 'omlet':
            ingredient = ingredients
    servings = request.GET['servings']
    context = {
        'data': ingredient,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    for dishes, ingredients in DATA.items():
        if dishes == 'pasta':
            ingredient = ingredients
    context = {
        'data': ingredient
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    for dishes, ingredients in DATA.items():
        if dishes == 'buter':
            ingredient = ingredients
    context = {
        'data': ingredient
    }
    return render(request, 'calculator/index.html', context)
