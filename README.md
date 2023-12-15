Please review the API - The testing path are as follows:

http://127.0.0.1:8000/reservations/                  (this will show the current reseravations -HTML file)
http://127.0.0.1:8000/menu/                           (this will show the menu items and will support get option
http://127.0.0.1:8000/menu/<int:pk>                         (this will support the post and delete operations but need authentication via token)
http://127.0.0.1:8000/api-token-auth/              (this will support obtaining auth token using the existing user - {"username": "admin1", "password" :"Password#"}
http://127.0.0.1:8000/tables/                        (this will support table reservation and table views)



