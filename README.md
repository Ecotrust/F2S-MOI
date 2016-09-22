# F2S-MOI
##Farm To School - Measuring Our Impact

### Installation
#### Vagrant (Dev)
 * Make sure your vagrant and virtual box are up-to-date
 * Install rsync_pull with `vagrant plugin install vagrant-rsync-pull`
 * Launch your box with `vagrant up`
   * **Note**: If vagrant appears sluggish, install `vagrant plugin install vagrant-faster` to help allocate more memory/CPU based on your machine's capacity
 * Access your box with `vagrant ssh`
 * In another terminal, keep local changes synced with `vagrant rsync-auto`
    * **Note**: If `vagrant rysnc-auto` seems to hang or appears progressively slow within vagrant, use  `vagrant plugin install vagrant-gatling-rsync` instead
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
 python manage.py bower install
 python manage.py runserver 0.0.0.0:8000
```
* use your browser to hit localhost:8005

##### Joys and pain of rsync-auto and rsync-pull
* As mentioned above, `rsync-auto` will watch your local/host changes and sync them to your virtual machine (VM)
* `rsync-pull` is used to retrieve changes from VM and bring them to your host
   * More often than not, most of your changes will be going from host to VM. However since migration changes to python models are done to the DB on the VM side, those changes will need to be pulled locally. 
   * **Note**:  initiating an `rsync-pull` without your changes saved on your host, can result in those changes being blown away
   * **If**  you have `rsync-auto` running and forget to turn it off to retrieve any migrations from the VM anc continue working on other models, etc. - you *sadly* may need to follow the steps below:
  ```
   #turn off rsync-auto
   [ctrl+c]
   
   # drop old and create new DB
   sudo su postgres
   dropdb moi
   createdb moi 
   psql moi 
   CREATE ROLE vagrant WITH PASSWORD 'vagrant'; 
   ALTER ROLE vagrant WITH LOGIN; 
   GRANT ALL PRIVILEGES ON DATABASE moi TO vagrant; 
   \q
   exit
   
   #checkout commit prior to model update and migration
   git checkout [SHA hash of commit you want to be at]
   
   #Load DB Schema
   python manage.py migrate
   
   #Clear out conflicts with most recent fixture
   python manage.py shell
   import django
   django.contrib.contenttypes.models.ContentType.objects.all().delete()
   [ctrl+d]
   
   #Load Fixture
   python manage.py loaddata fixtures/[some-name-here-fixture].json
   
   #checkout branch you're working on
   git checkout [branchname]
   
   #load additional schema
   python manage.py migrate
   
   #pull from VM
   vagrant rsync-pull
  ```
  
### Deployment
 * ssh into server
 * `cd ~/webapps/f2smoi/F2S-MOI/` - puts you at the app root
 * `git pull origin master` - or use fetch, etc - to grab code from github
 * `python manage.py compress --force && python manage.py collectstatic` at `cd moi/` - grab css/js files
 * `~/webapps/f2smoi/apache2/bin/restart` - restart server
 
