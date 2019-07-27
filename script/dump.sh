#!/bin/bash
# -*- coding: utf-8 -*-
PYTHON=/home/orten/orten.in.ua/virtualenv/bin/python3.7
MANAGE=/home/orten/orten.in.ua/orten/manage.py
DUMP_DIR=/home/orten/orten.in.ua/fixtures
BACKUP_DIR=/home/orten/orten.in.ua/backup

Category=shop.Category
Product=shop.Product
Service=shop.Services
Flatpages=flatpages
Polygraphy=shop.Polygraphy
Redirects=redirects

$PYTHON $MANAGE dumpdata $Category > $DUMP_DIR/Category_dump.json &
$PYTHON $MANAGE dumpdata $Service > $DUMP_DIR/Services_dump.json &
$PYTHON $MANAGE dumpdata $Flatpages > $DUMP_DIR/Flatpages_dump.json &
$PYTHON $MANAGE dumpdata $Polygraphy > $DUMP_DIR/Polygraphy_dump.json &
$PYTHON $MANAGE dumpdata $Redirects > $DUMP_DIR/Redirects_dump.json &
$PYTHON $MANAGE dumpdata $Product > $DUMP_DIR/Product_dump.json &&
cd $DUMP_DIR &&
tar -jcf $BACKUP_DIR/dumpDB-`date "+%d-%m-%Y"`.tar.bz2 *
find $BACKUP_DIR -type f -name "*.tar.bz2" -mtime +30 -print -delete

################## archive log file #################################

LOG_DIR=/home/orten/orten.in.ua/log/

cd $LOG_DIR &&
tar -jcf uwsgi_orten-`date "+%d-%m-%Y"`.gz uwsgi_orten.log &&
tar -jcf ngnix_error-`date "+%d-%m-%Y"`.gz ngnix_error.log &&
tar -jcf ngnix_access-`date "+%d-%m-%Y"`.gz ngnix_access.log &&
find $LOG_DIR -type f -name "*.log" -mtime +1 -print -delete
