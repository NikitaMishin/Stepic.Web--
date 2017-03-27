sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart



sudo ln -sf /home/box/web/etc/guniconf_hello.py   /etc/gunicorn.d/guniconf_hello
sudo ln -sf /home/box/web/etc/guniconf_django.py   /etc/gunicorn.d/guniconf_django
sudo /etc/init.d/gunicorn restart

sudo gunicorn -c /etc/gunicorn.d/guniconf_hello hello:app

sudo gunicorn -c /etc/gunicorn.d/guniconf_django ask.wsgi:application
