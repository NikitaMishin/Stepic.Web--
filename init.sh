sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
# sudo ln -sf /home/box/web/etc/guniconf.py   /etc/gunicorn.d/guniconf
# sudo /etc/init.d/gunicorn restart
# sudo gunicorn -c /etc/gunicorn.d/guniconf wsgi:application
# sudo rm -r /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
# sudo /etc/init.d/nginx restart

# sudo rm -r /etc/gunicorn.d/*
# sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
# sudo ln -sf /home/box/web/etc/quniconf.py   /etc/gunicorn.d/quniconf.py
# sudo /etc/init.d/gunicorn restart



#sudo pip3 install --upgrade django
#sudo pip3 install --upgrade gunicorn
sudo nano /usr/sbin/gunicorn-debian
sudo nano /usr/bin/gunicorn
sudo nano /usr/bin/gunicorn_django
sudo nano /usr/bin/gunicorn_paster

sudo ln -sf /home/box/web/etc/guniconf_hello.py   /etc/gunicorn.d/guniconf_hello
sudo ln -sf /home/box/web/etc/guniconf_django.py   /etc/gunicorn.d/guniconf_django
sudo /etc/init.d/gunicorn restart

sudo gunicorn -c /etc/gunicorn.d/guniconf_hello hello:app
cd ask/
sudo gunicorn -c /etc/gunicorn.d/guniconf_django ask.wsgi:application
