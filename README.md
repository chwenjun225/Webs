# Working:
- https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_02.xhtml#_idParaDest-109
- https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_04.xhtml#_idParaDest-150

# Running commands:
## MySite
python manage.py runserver
docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=P00778076 -p 5432:5432 -d postgres:16.2

# Bug logs:
1. ✔ Error when translate to Spain language (https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_11.xhtml#_idParaDest-327)

2. ✔ 
```
ConnectionError at /en/6/living-room-sofas-and-chairs/
Error 111 connecting to localhost:6379. Connection refused.
Request Method:	GET
Request URL:	http://127.0.0.1:8000/en/6/living-room-sofas-and-chairs/
Django Version:	4.2.16
Exception Type:	ConnectionError
Exception Value:	
Error 111 connecting to localhost:6379. Connection refused.
Exception Location:	/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/site-packages/redis/connection.py, line 282, in connect
Raised during:	shop.views.product_detail
Python Executable:	/home/chwenjun225/miniconda3/envs/Webs/bin/python
Python Version:	3.9.20
Python Path:	
['/home/chwenjun225/Webs/SynerSocial',
 '/home/chwenjun225/Webs/SynerSocial',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python39.zip',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/lib-dynload',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/site-packages']
Server time:	Sun, 01 Dec 2024 16:35:56 +0000
```
