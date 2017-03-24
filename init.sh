sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/guniconf.py   /etc/gunicorn.d/guniconf
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /etc/gunicorn.d/guniconf wsgi:application
# sudo rm -r /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
# sudo /etc/init.d/nginx restart

# sudo rm -r /etc/gunicorn.d/*
# sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
# sudo ln -sf /home/box/web/etc/quniconf.py   /etc/gunicorn.d/quniconf.py
# sudo /etc/init.d/gunicorn restart
