#INSTALLATION
##Install MongoDB
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee/etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo nano /lib/systemd/system/mongod.service

sudo service mongod start

tail -f /var/log/mongodb/mongod.log 

##Instal pip3 and virtualenv
sudo apt-get install python-pip

sudo pip install virtualenv

mkdir spidr

cd spidr/

virtualenv spidr-env

source spidr-env/bin/activate

##Install Django
pip install django

pip install pymongo

