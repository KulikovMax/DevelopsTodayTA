Important links:
	Heroku Link: https://stark-crag-63771.herokuapp.com/
	Postman Collection: https://www.getpostman.com/collections/cc410f60431d16954c53
	Docker image: kulikovmax/newsmvp


Usage API with Heroku:
 Add "api/" to Heroku link (e.g."https://stark-crag-63771.herokuapp.com/api/") to get list of news and related comments and ability to add news;
 Add "api/news_article_id/" to get detailed view on news article(e.g. for article with id=1: "https://stark-crag-63771.herokuapp.com/api/1/");
 Add "api/news_article_id/comments/" to get list of comments of related news article and ability to add comment (e.g. for article with id=1: "https://stark-crag-63771.herokuapp.com/api/1/comments/");
 Add "api/news_article_id/comments/cimment_id/" to get detailed view on comment(e.g. for article with id=1 and comment with id=2: "https://stark-crag-63771.herokuapp.com/api/1/comments/2");

Docker usage:
 Install docker
 Inside bash/cmd go to the directory where "docker-compose.yml" file placed
 Print "docker-compose build"
 Print "docker-compose up"
 Try to go to 127.0.0.1:8000. If it doesn't work, continue reading.

 Print "docker ps" and copy CONTAINER ID of the image that contains "newsmvp"
 Print "docker exec -t -i <place here CONTAINER ID> bash"
 When in bash, run "python3 manage.py makemigrations" and "python3 manage.py migrate"
 Then run "docker-compose up" one more time
 Now it should work.
