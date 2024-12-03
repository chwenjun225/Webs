# Running commands:
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management

celery -A SynerSocial worker -l info

docker run -it --rm --name redis -p 6379:6379 redis:7.2.4

stripe listen --forward-to localhost:8000/payment/webhook/

python manage.py runserver

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
