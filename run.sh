#!binsh
echo "------ Starting APP ------"
USER="212634269"
MAIL="Daniel.Flavin@ge.com"
PASS="makeovermainapis"

if [-z $VCAP_APP_PORT];
	then SERVER_PORT=5000;
	else SERVER_PORT=$VCAP_APP_PORT;
fi

echo ------ Create database tables ------
python manage.py makemigrations makeoverapp
python manage.py migrate --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${USER}', '${MAIL}', '${PASS}')" | python manage.py shell

echo ------Starting server ------
python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload
