from calculator.views import cook

urlpatterns = [
    path('<recipe_name>/', cook),
]
