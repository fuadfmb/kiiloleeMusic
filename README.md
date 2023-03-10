![Screenshot 1](https://github.com/fuadfmb/kiiloleeMusic/blob/master/static/Screenshot%202023-01-05%20at%2009-23-26%20Kiilolee%20Music.png?raw=true)


# Kiilolee Music
## Music & Lyrics site for East Africa


Kiilolee Music is a music and lyrics website powered with Django web framework. The Aim of this project is putting together representative samples of music in East Africa/archiving all east African music on a our server and allowing others to access those resources in an easy way. The site routes are designed in a way that search engines can easily index the site.

This project contains different models. some of the models are : 

- Language
- Category
- Artist
- Album
- Song
- Lyrics
- Gallery
- ArtImage
- AlbumComments
- SongComments
- SongLikes and
- Playlist

## How the Model is designed

According to this project:- 
- An **Artist** can have many **Albums**.
- When a new **Artist** created, an new **Album** that belongs to an **Artist** called **'Singles'** will be added to **Albums**.
- An **Album** always belongs to an **Artist**.
- A Song always belongs to an **Album** or **Singles** album.
- and a **Lyrics** always belongs to a **Song**.
- A **Song** belongs to a **Language**

## Other Features

- An Admin can CRUD an **Artist, Album, Song, Lyrics** and every model using django admin
- A user can then create his own **Playlist**.
- A user can then add a **Song** to his **favorites** folder.
- A user can also write a **comment** on an Album or a Song.
- 


This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Technologies used in this project
- Python 3
- Html & CSS
- Javascript + JQuery
- Bootstrap

## Admin Route
- **Admin** : /o/k/admin/

## Installation

After cloning this project, open the folder that have **_manage . py_**. and make sure there is a databse file called **db.sqlite3**.
then open CMD and run the following commands respectively.

- create super user with username, email & password
```sh
python manage.py createsuperuser
```
- make DB Migrations
```sh
python manage.py makemigrations
```
- Migrate
```sh
python manage.py migrate
```
- Run dev server
```sh
python manage.py runserver
```

**And then you can test your site using :** 
- as a (USER) : http://127.0.0.1:8000/
- as an (ADMIN) : http://127.0.0.1:8000/o/k/admin/

## Last but not least
- You should create 3 pages : **Disclaimer, Tos & privacy policy** page using django-admin.
