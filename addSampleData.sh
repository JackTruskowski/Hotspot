rm db.sqlite3 && python2 manage.py makemigrations && python2 manage.py migrate && python2 manage.py shell < readRestaurantData.py
