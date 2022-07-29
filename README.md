# Zhas-Hackathon

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## Idea

In competition we chose case from [KeepItFresh](https://www.instagram.com/keepitfresh.beauty/) on creating a recommendation system for a user based on his/her current cosmetic bag. I was responsible for building the recommendation engine and building the REST API.

For this project, I decided to use the Django REST Framework with PostgreSQL to write the API. The recommendation engine was built on the Scikit-Learn library using cosine similarity. The API has CRUD functionality and a request method for the recommendation engine.

[WEBSITE](https://zhas-hackathon.herokuapp.com/api/v1/recommend/555.324.1320/3)

![image1](https://github.com/elamirKad/zhas-hackathon/blob/main/github/Screenshot1.png)
![image2](https://github.com/elamirKad/zhas-hackathon/blob/main/github/Screenshot2.png)

# Installation
Run installation command:
```
pip install requirements.txt
```
Then go to the project's main folder:
```
cd zhas-hackathon
```
Create PosgreSQL database
```
createdb db_name
```
Configure zhasHackathon/settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
Migrate:
```
python manage.py makemigrations
python manage.py migrate
```
Load data from cosmetics_cleaned2v.csv:
```
python manage.py loaddata datadump.json
```
Start server:
```
python manage.py runserver
```

# Usage

### CRUD API
GET request: to get all rows
```
https://zhas-hackathon.herokuapp.com/api/v1/cosmetics/
```
GET request: to get specific row by pk (pk==id)
```
https://zhas-hackathon.herokuapp.com/api/v1/cosmetics/<int:pk>/
```
POST request: to add new rows
```
https://zhas-hackathon.herokuapp.com/api/v1/cosmetics/
```
PUT request: to partially change specific row by pk (pk==id)
```
https://zhas-hackathon.herokuapp.com/api/v1/cosmetics/<int:pk>/
```
DELETE request: to delete specific row by pk (pk==id)
```
https://zhas-hackathon.herokuapp.com/api/v1/cosmetics/<int:pk>/
```

### Recommendation API

To request recommendations you need to create GET request:
```
https://zhas-hackathon.herokuapp.com/api/v1/recommend/<str:pk>/<int:amount>
```
Example 1:
```
https://zhas-hackathon.herokuapp.com/api/v1/recommend/555/
```
In this case, we receive 5 recommendations based on row with id=555

Example 2:
```
https://zhas-hackathon.herokuapp.com/api/v1/recommend/555.12.278/3
```
In this case, we receive 3 recommendations for each row with id's 555, 12, 278
