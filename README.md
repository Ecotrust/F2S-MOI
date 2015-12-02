# F2S-MOI
##Farm To School - Measuring Our Impact

### Installation
#### Vagrant (Dev)
 * Launch your box with `vagrant up`
 * Access your box with `vagrant ssh`
 * run the following commands
```
 sudo /usr/local/apps/deploy/install_vagrant_reqs.sh
 cd /usr/local/apps/moi
 virtualenv env
 source env/bin/activate
 pip install -r /usr/local/apps/requirements.txt
 sudo su postgres
 createdb moi
 psql moi
 CREATE ROLE vagrant WITH PASSWORD 'vagrant';
 ALTER ROLE vagrant WITH LOGIN;
 GRANT ALL PRIVILEGES ON DATABASE moi TO vagrant;
 \q
 exit
```
* If you changed the db user or password, update moi/moi/settings/base.py
```
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver 0.0.0.0:8000
```
* use your browser to hit localhost:8005
