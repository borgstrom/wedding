#
# Django state file
#
# Deploys Django for development
#

include:
  - avahi
  - nginx
  - mysql.server
  - virtualenv
  - supervisor

{% from "utils/users.sls" import skeleton -%}
{% from "mysql/macros.sls" import mysql_user_db -%}
{% from "nginx/macros.sls" import nginxsite -%}
{% from "supervisor/macros.sls" import supervise -%}

{% set short_name = pillar['project']['short_name'] -%}
{% set home = "/home/vagrant" -%}
{% set virtualenv = home + "/virtualenv" -%}
{% set project = home + "/domains/" + short_name -%}
{% set appdir = home + "/domains/" + short_name + "/" + short_name -%}
{% set app_user = "vagrant" -%}
{% set app_group = "vagrant" -%}

{{ skeleton(app_user, 1000, 1000, remove_groups=False) }}

curl:
  pkg:
    - installed

{{ short_name }}_virtualenv:
  virtualenv:
    - managed
    - name: {{ virtualenv }}
    - requirements: {{ project }}/requirements/dev.txt
    - user: vagrant
    - no_chown: True
    - system_site_packages: True
    - require:
      - pkg: virtualenv_pkgs

{{ short_name }}_requirements:
  cmd:
    - run
    - name: "source {{ virtualenv }}/bin/activate; pip install -r {{ project }}/requirements/dev.txt"
    - shell: /bin/bash
    - env:
        DJANGO_SETTINGS_MODULE: luminato.settings.dev
        PYTHON_PATH: /vagrant/luminato
    - user: vagrant
    - require:
      - virtualenv: {{ short_name }}_virtualenv

{{ mysql_user_db(short_name, short_name) }}

{{ short_name }}_profile_setup:
  file:
    - append
    - name: /home/vagrant/.profile
    - require:
      - user: vagrant
    - text:
      - export DJANGO_SETTINGS_MODULE=luminato.settings.dev
      - export PYTHONPATH=/vagrant/luminato
      - source ~/virtualenv/bin/activate
      - cd /vagrant

{{ short_name }}_screenrc:
  file:
    - managed
    - name: /home/vagrant/.screenrc
    - require:
      - user: vagrant
    - owner: vagrant
    - mode: 644
    - source: salt://files/screenrc

# setup node & ruby for foundation
install_nvm:
  cmd:
    - run
    - name: curl https://raw.githubusercontent.com/creationix/nvm/v0.5.1/install.sh | sh
    - unless: test -d ~/.nvm/
    - user: vagrant
    - require:
      - user: vagrant
      - pkg: curl

install_node:
  cmd:
    - run
    - name: source ~/.nvm/nvm.sh; nvm install 0.10 && nvm alias default 0.10 && nvm use 0.10
    - shell: /bin/bash
    - unless: source ~/.nvm/nvm.sh; nvm ls | grep -q 'default -> 0.10'
    - user: vagrant
    - require:
      - cmd: install_nvm

install_rvm:
  cmd:
    - run
    - name: "\\curl -sSL https://get.rvm.io | bash -s stable --ruby=1.9"
    - unless: source ~/.rvm/scripts/rvm; rvm info | grep -q '^ruby-1.9'
    - user: vagrant
    - require:
      - pkg: curl

# install foundation
install_bower_grunt:
  cmd:
    - run
    - name: source ~/.nvm/nvm.sh; npm install -g bower grunt-cli
    - unless: test -x `which bower` && test -x `which grunt`
    - user: vagrant
    - require:
      - cmd: install_node

install_foundation:
  cmd:
    - run
    - name: source ~/.rvm/scripts/rvm; gem install foundation
    - unless: gem list --local | grep -q '^foundation'
    - user: vagrant
    - require:
      - cmd: install_rvm
      - cmd: install_bower_grunt

# vim: set ft=yaml ts=2 sw=2 sts=2 et ai :
