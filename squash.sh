#!/bin/bash
find . -name "*.sqlite3" -delete

cd src/portfolio/app
find . -name "migrations" -type d -print0|xargs -0 rm -r --
cd ../../
python manage.py migrate

declare -A arr
arr[0]='schools'
arr[1]='companies'
arr[2]='projects'
arr[3]='education'
arr[4]='courses'
arr[5]='experience'
arr[6]='skills'

for (( i=0; i<=3; i++ ))
do
  echo "Migrating ${arr[i]}"
  python manage.py makemigrations ${arr[i]}
done
python manage.py migrate
echo "First Set of Migrations Done"

for (( i=3; i<=6; i++ ))
do
  echo "Migrating ${arr[i]}"
  python manage.py makemigrations ${arr[i]}
done
python manage.py migrate

python manage.py createsuperuser --email nickmflorin@gmail.com --username nickmflorin
