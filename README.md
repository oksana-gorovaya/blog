# Simple blog app
This app is using docker compose. So you can have it up and running with the following steps:
1. copy this repository 
2. make sure you have docker compose installed
3. run "docker-compose up" in the directory where docker-compose.yml is located
4. run "python3 manage.py migrate" in your web container to apply migrations
5. open http://127.0.0.1:8000/ in browser and check it out :)

P.S: you will see no posts or comments as the blog is shiny new. You'll need ti sign up first to add some content.
