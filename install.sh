echo "Starting installation process."
echo "Installing Python3 and PostgreSQL."
apt-get install python3 python3-pip #Python3 and its package manager.
apt-get install postgresql postgresql-server-dev-9.3 #PostgreSQL DB

echo "Installing SQLAlchemy, Flask, and Psycopg2."
pip3 install psycopg2
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install sqlalchemy

#Add the required nginx and uwsgi stuff right here ------    ------------
#                                                       |    |          |
#                                                    ----    |          |
#                                                    |       |          |
#                                                    ---------          |
#                                                                       V


##############################

echo "Installation Complete."
