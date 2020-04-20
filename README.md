# Backend Exercise - Recipe API

[![Build Status](https://travis-ci.org/eballo/exercise-recipe-api.svg?branch=master)](https://travis-ci.org/eballo/exercise-recipe-api)

Backend Web application created using Django to provide the following end points to
be able to manage a recipe with ingredients:

- Add Recipe
- Get a Recipe
- Get a List of Recipes
- Filter a Recipe
- Update a Recipe 
- Delete Recipe

# Data Models

**Recipe:** Name, Description
**Ingredient:** Name, Recipe (ForeignKey)

**Assumption:** a given ingredient belongs only to one recipe, 
even if that means multiple Ingredient instances with the exact same name

## Getting up and running
### With Docker
```> docker-compose -up ```
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

## Execute Migrations

``` docker-compose run --rm app sh -c "python manage.py makemigrations" ```

## Exute Tests

``` docker-compose run --rm app sh -c "python manage.py test && flake8" ```

## Usage

### POST /recipes/
```
{
	"name": "Pizza",
	"description": "Put it in the oven",
	"ingredients": [{"name": "dough"}, {"name": "cheese"}, {"name": "tomato"}]
}
```
CURL command
```
curl -X POST -H "Content-Type: application/json" --data '{"name": "Pizza","description": "Put it in the oven","ingredients": [{"name": "dough"}, {"name": "cheese"}, {"name": "tomato"}]
}' http://localhost:8000/api/recipes/
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
    “ingredients”: [{“name”: “casa-tarradellas”}]
}
```
Should delete the previous existing ingredients and put “casa-tarradellas” as only ingredient for recipe.

CURL command
```
curl -X PATCH -H "Content-Type: application/json" --data '{"name": "Pizza","description": "Put it in the oven","ingredients": [{"name": "casa-tarradellas"}]
}' http://localhost:8000/api/recipes/1/
```

Response:
```
{
	“id”: 1,
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “casa-tarradellas”}]
}
```

### GET /recipes/1/ 
```
curl -X GET http://localhost:8000/api/recipes/1/
```
```
{
	“id”: 1,
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}
```
## GET /recipes/?name=Pi 
```
curl -X GET http://localhost:8000/api/recipes/?name=Pi
```

```
[
    {
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
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
