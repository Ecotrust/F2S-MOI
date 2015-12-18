#!/bin/bash
rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
yum -y update
yum install vim python-virtualenv python-devel python-pip postgresql-devel libjpeg-devel zlib-devel postgresql-server postgresql-contrib virtualenvwrapper -y
yum group install "Development Tools" -y
postgresql-setup initdb
cp /usr/local/apps/deploy/postgres_config.conf /var/lib/pgsql/data/pg_hba.conf
systemctl start postgresql
systemctl enable postgresql
