def cook(request, recipe_name):
    if recipe_name in DATA.keys():
        servings = request.GET.get('servings', 1)
        data = {}
        for ingredient in DATA[recipe_name]:
            data[ingredient] = round(DATA[recipe_name][ingredient] * int(servings), 2)

        context = {
            'recipe': data
        }

    else:
        context = {}

    return render(request, 'calculator/index.html', context)
