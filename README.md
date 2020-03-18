# Recipe API

Web application created using Django to provide the following end points to
be able to manage a recipe with ingredients:

- Add Recipe
- Add Ingredient
- Add Ingredient to a recipe
- Delete Recipe
- Delete Ingredient

# Data Models

**Recipe:** Name, Description
**Ingredient:** Name, Recipe (ForeignKey)

**Assumption:** a given ingredient belongs only to one recipe, 
even if that means multiple Ingredient instances with the exact same name

## Getting up and running
TODO: Describe the installation process

## Usage

Example:

### GET /recipes/1/ 
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
[
    {
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
    }
]
```
## GET /recipes/?name=Pi
```
[
    {
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
    }
]
```

### POST /recipes/
```
{
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}
```
Response:
```
{
	“id”: 1,
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}
```