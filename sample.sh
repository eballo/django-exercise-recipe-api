# -----------------------------------------------------
#    Sample script that create few example recipes
# -----------------------------------------------------

## Create Ingredients
curl -X POST -H "Content-Type: application/json" --data '{"name": "oil"}' http://localhost:8000/api/recipes/ingredients/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "salt"}' http://localhost:8000/api/recipes/ingredients/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "tomatoes"}' http://localhost:8000/api/recipes/ingredients/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "potatoes"}' http://localhost:8000/api/recipes/ingredients/

## Create Tags
curl -X POST -H "Content-Type: application/json" --data '{"name": "meal"}' http://localhost:8000/api/recipes/tags/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "desert"}' http://localhost:8000/api/recipes/tags/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "vegetarian"}' http://localhost:8000/api/recipes/tags/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "breakfast"}' http://localhost:8000/api/recipes/tags/

## Create Recipes
curl -X POST -H "Content-Type: application/json" --data '{"name": "Pizza","description": "Put it in the oven", "time_minutes": 10, "price": 5.0, "ingredients": [ 1, 2 ,3], "tags": [ 3 ] }' http://localhost:8000/api/recipes/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "Tortilla Patatas","description": "Tipical spanish omelete", "time_minutes": 10, "price": 5.0,"ingredients": [ 1, 2, 4 ], "tags": [ 3 ] }' http://localhost:8000/api/recipes/ &&
curl -X POST -H "Content-Type: application/json" --data '{"name": "Greek Salad","description": "Tipical Greek Salad", "time_minutes": 10, "price": 5.0,"ingredients": [ 1, 2, 4 ], "tags": [ 3 ] }' http://localhost:8000/api/recipes/

## Update Images
curl -F 'image=@./images/pizza.jpg' http://localhost:8000/api/recipes/1/upload-image/ &&
curl -F 'image=@./images/tortillapatatas.jpg' http://localhost:8000/api/recipes/2/upload-image/ &&
curl -F 'image=@./images/greekSalad.jpeg' http://localhost:8000/api/recipes/3/upload-image/