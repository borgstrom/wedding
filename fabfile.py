'''
Wedding fabric file

This file provides deployment through garment as well as a number of tasks
for loading data and content from production

These tasks are meant to be run from the vagrant box after SSHing in.
'''

import datetime

from garment import *  # noqa

from fabric.api import task, run, local, hosts, execute
from fabric.operations import get, put

PRODUCTION = 'weddingrsvp@fame.unixpimps.com'

TS = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S%z')
DUMPFILE = '/tmp/%s.sql' % TS
DUMPFILEGZ = '.'.join([DUMPFILE, 'gz'])


@task
def fetch_sql():
    '''
    Fetches the current data as an .sql.gz file from the specified host
    '''
    run(
        'mysqldump --opt -u"$DB_USER" -h"$DB_HOST" -p"$DB_PASS" "$DB_NAME" '
        '> "%s"' % DUMPFILE
    )
    run('gzip %s' % DUMPFILE)
    get(DUMPFILEGZ, DUMPFILEGZ)
    run('rm -f %s' % DUMPFILEGZ)


@task
def load_sql(func=local):
    '''
    Loads a .sql.gz file, can be used locally or remotely
    '''
    # so it can be set on the cli if needed
    if func == 'run':
        func = run

    func('zcat %s | mysql -uwedding -pwedding wedding' % DUMPFILEGZ)
    func('rm -f %s' % DUMPFILEGZ)


@task
@hosts(PRODUCTION)
def load_prod_sql():
    '''
    Load SQL data from the production instance into your local instance
    '''
    fetch_sql()
    load_sql()


def _sync_media(host):
    local('rsync -avz --progress --stats -e ssh '
          '%s:media/ '
          '/home/vagrant/media/' % (
              host,
          ))


@task
@hosts()
def sync_prod_media():
    '''
    Synchronize media from the production host to your local instance
    '''
    _sync_media(PRODUCTION)


@task
@hosts()
def dev():
    '''
    Run the dev server
    '''
    local('django-admin.py runserver 0:8000')


@task
@hosts()
def scss():
    '''
    Compile the SCSS into CSS
    '''
    local('cd /vagrant/wedding/ui; grunt sass')


@task
@hosts()
def scss_watch():
    '''
    Start the watch process to compile SCSS into CSS on changes
    '''
    local('cd /vagrant/wedding/ui; grunt watch')
