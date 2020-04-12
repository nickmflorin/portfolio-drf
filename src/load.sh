#!/bin/bash

declare -A apps
apps[0]='schools'
apps[1]='education'
apps[2]='courses'
apps[3]='companies'
apps[4]='experience'
apps[5]='projects'
apps[6]='experience'
apps[7]='skills'
apps[8]='profile'
apps[9]='comments'


migrate_database(){
  # Initial Migration for Django Tables
  python manage.py migrate

  for (( i=0; i<${#apps[@]}; i++ ))
  do
    local application=${apps[i]}
    echo "Performing Migrations for Application ${application}"
    python manage.py makemigrations ${application}
    python manage.py migrate ${application}
  done
}

load_data() {
  for (( i=0; i<${#apps[@]}; i++ ))
  do
    local application=${apps[i]}
    echo "Loading Data for Application ${application}"
    sudo python manage.py loaddata ./portfolio/fixtures/${application}.json
  done
}

manage_admin(){
  python manage.py createsuperuser --email nickmflorin@gmail.com --username nickmflorin
}

migrate_database
load_data
manage_admin
