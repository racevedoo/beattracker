rm mainapp/tracker/*.wav.txt
rm media/*.wav
./manage.py sqlclear mainapp | ./manage.py dbshell
./manage.py syncdb
