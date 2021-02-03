# insta-clone

insta-clone is clone of some features of instagram using django and channels not the best but it was great to work in and iam still adding features


## features


1 /profile page where you can add and see all your photos 


<img src="/media/profile-page.png" width="350" title="hover text">



2 /see others profile and follow


<img src="/media/see others profile and follow.png" width="350" title="hover text">


3 /caht where you can talk too others


<img src="/media/chat.png" width="350" title="hover text">




## Installation

1- downlad the repo
```bash
git clone https://github.com/seif-elden/insta-clone-using-django
```

2- install Redis server and run it on the port 6379

note: if you are in windows you can install memurai to work as channel layer

3- make virtual env (optional)

   
4- install requirements
```bash
pip install -r requirements.txt
```
5- create superuser
```bash
py manage.py createsuperuser
```

6-run server 
```bash
py manage.py runserver
```

<hr>

 I used "django-channels-chat" as the main chating feature on this repo if you want to download the source code you will find it here: https://github.com/narrowfail/django-channels-chat/
