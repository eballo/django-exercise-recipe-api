# Backend Exercise - Recipe API

[![Build Status](https://travis-ci.org/eballo/django-exercise-recipe-api.svg?branch=master)](https://travis-ci.org/eballo/django-exercise-recipe-api)

Backend Web application created using Django to provide the following end points to
be able to manage a recipe with ingredients:

- Add Recipe
- Get a Recipe
- Get a List of Recipes
- Filter a Recipe
- Update a Recipe 
- Delete Recipe
- Add a Ingredient
- Add a Tag
- Add a Image

# Data Models

### Version 2.0:
- **Recipe:** Name, Description, time_minutes, price, link, image
- **Ingredient:** Name, Recipe (ForeignKey)
- **Tags:** Name, Recipe (ForeignKey)

A given ingredient or tag belongs to one or many recipes

### Version 1.0:
- **Recipe:** Name, Description
- **Ingredient:** Name, Recipe (ForeignKey)

- **Assumption:** a given ingredient belongs only to one recipe, 
even if that means multiple Ingredient instances with the exact same name

## Getting up and running
### With virtualenv

- Check out the project
- Create the virtualenv
```
> pyenv install 3.7.0 
> pyenv virtualenv 3.7.0 Django
```
- create a local env

```> pyenv local Django```
- Install requirements.txt

```> pip install -r requirements.txt```

- Start the server

```> python manage.py runserver ```

### With Docker
```> docker-compose -up ```

If we want some sample data

```> ./sample.sh ```
#### Execute Migrations

``` docker-compose run --rm app sh -c "python manage.py makemigrations" ```

#### Exute Tests

``` docker-compose run --rm app sh -c "python manage.py test && flake8" ```

## Usage

### POST /recipes/
```
{
    "name": "Pizza",
    "description": "Put it in the oven", 
    "time_minutes": 10, 
    "price": 5.0, 
    "ingredients": [ 1, 2 ,3], 
    "tags": [ 3 ] 
}
```
CURL command
```
curl -X POST -H "Content-Type: application/json" --data '{"name": "Pizza","description": "Put it in the oven", "time_minutes": 10, "price": 5.0, "ingredients": [ 1, 2 ,3], "tags": [ 3 ] }' http://localhost:8000/api/recipes/
```
Response:
```
{"id":1,"name":"Pizza","description":"Put it in the oven","ingredients":[{"name":"tomato"},{"name":"cheese"},{"name":"dough"}]}
```

## PATCH /recipes/1/
```
{
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [1]
}
```
Should delete the previous existing ingredients and put 1 as only ingredient for recipe.

CURL command
```
curl -X PATCH -H "Content-Type: application/json" --data '{"name": "Pizza","description": "Put it in the oven","ingredients": [1]
}' http://localhost:8000/api/recipes/1/
```

Response:
```
{
    "id":1,
    "name":"Pizza",
    "ingredients":[1],
    "tags":[3],
    "description":"Put it in the oven",
    "time_minutes":10,
    "price":"5.00",
    "image":"http://localhost:8000/media/uploads/recipe/6ab14a0f-7f91-4655-a033-cc47673fc87d.jpg",
    "link":""
}
```

### GET /recipes/1/ 
```
curl -X GET http://localhost:8000/api/recipes/1/
```
```
{
    "id":1,
    "name":"Pizza",
    "ingredients":[
                    {"id":1,"name":"oil"},
                    {"id":2,"name":"salt"},
                    {"id":3,"name":"tomatoes"}
                ],
    "tags":[{"id":3,"name":"vegetarian"}],
    "description":"Put it in the oven",
    "time_minutes":10,
    "price":"5.00",
    "image":"http://localhost:8000/media/uploads/recipe/6ab14a0f-7f91-4655-a033-cc47673fc87d.jpg",
    "link":""
}
```
## GET /recipes/?name=Pi 
```
curl -X GET http://localhost:8000/api/recipes/?name=Pi
```

```
[
    {
        "id":1,
        "name":"Pizza",
        "ingredients":[1,2,3],
        "tags":[3],
        "description":"Put it in the oven",
        "time_minutes":10,
        "price":"5.00",
        "image":"http://localhost:8000/media/uploads/recipe/6ab14a0f-7f91-4655-a033-cc47673fc87d.jpg",
        "link":""
    }
]
```

## DELETE /recipes/1/

```
curl -X DELETE http://localhost:8000/api/recipes/1/ 
```

Response:
```
HTTP 204 (NO CONTENT)
```

Should delete the targeted recipe AND its ingredients.
