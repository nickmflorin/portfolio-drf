#!/bin/bash
find . -name "*.sqlite3" -delete

cd src/portfolio/app
find . -name "migrations" -type d -print0|xargs -0 rm -r --
cd ../../
python manage.py migrate

declare -A arr
arr[0,0]='schools'
arr[0,1]='companies'
arr[0,2]='projects'
arr[1,0]='education'
arr[1,1]='courses'
arr[1,2]='experience'
arr[1,3]='skills'

for (( i=0; i<=2; i++ ))
do
  python manage.py makemigrations ${arr[0,i]}
done
python manage.py migrate

for (( i=0; i<=3; i++ ))
do
  python manage.py makemigrations ${arr[1,i]}
done
python manage.py migrate

python manage.py createsuperuser --email nickmflorin@gmail.com --username nickmflorin
