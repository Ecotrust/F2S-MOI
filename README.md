# F2S-MOI
##Farm To School - Measuring Our Impact

### Installation
#### Vagrant (Dev)
 * Install rsync_pull with `vagrant plugin install vagrant-rsync-pull`
 * Launch your box with `vagrant up`
 * Access your box with `vagrant ssh`
 * In another terminal, keep local changes synced with `vagrant rsync-auto`
 * When you want to sync files FROM the VM to the host, use `vagrant rsync-pull`
 * run the following commands
```
 sudo ln -s /home/vagrant/sync/ /usr/local/apps
 sudo /usr/local/apps/deploy/install_vagrant_reqs.sh
 cd ~/
 virtualenv env
 source env/bin/activate
 cd /usr/local/apps/moi
 pip install --upgrade pip
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
