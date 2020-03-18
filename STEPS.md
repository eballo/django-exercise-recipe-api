Good Practices for Python

### Steps done creating this project

1- Create a ``virutalenv`` for each project
```
> python3.6 -m venv --prompt Django .venv
```
2- activate the virtual env
```
source venv/bin/activate
```
3- Initialize git and add the venv directory to .gitignore
```
git init
echo 'venv' > .gitignore
```
4- Installing Django
```
python -m pip install --upgrade 'pip<20' 
pip install django
```
5- Freeze the requirements
pip freeze > requirements.txt

6- create django project
```
~/work/eballo/exercise-recipe-api/
(venv)  > django-admin startproject app
```

7- start the server 
```
~/work/eballo/exercise-recipe-api/app/
> python manage.py runserver
```

8- check all is working on http://127.0.0.1:8000/

9- create a app recipe
```
tk841it: ~/work/eballo/exercise-tp/recipeapp [git:master] 11:56:56
(venv)  > python manage.py startapp recipe
```

10- recipe/views.py
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the recipe index.")
```

11- recipe/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

12- recipeapp/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('recipes/', include('recipe.urls')),
    path('admin/', admin.site.urls),
]
```

13- start the server and check that everything is working as expected
```
python manage.py runserver
```
Check http://127.0.0.1:8000/recipes/
