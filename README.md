## ������ "����� �����, ��� ����!"
## ��������� ���������� �� ����������� Agile:Scrum
## ���� ��� ��������

### ������� ������������ � �������

�������� ��������� ����������:

* Ubuntu 20.04 LTS
* Python 3.9
* Django 4.1
* ����������� (Python) �� requirements.txt

### ��������� ������������ ��
#### ��������� ���������� � ������������
```
apt update
```
#### ��������� nginx, Git, virtualenv, gunicorn
```
apt install nginx
```
Git
```
apt install git-core
```
virtualenv
```
apt install python3-venv
```
gunicorn
```
apt install gunicorn
```
#### ����������� ����������� ���������
��� �������������, ��� ��������� ��������� ������� pip ��������� �������:
```
apt install python3-pip
```
������� � ���������� ����������� ���������:
```
mkdir /opt/venv
python3 -m venv /opt/venv/team_work_env
source /opt/venv/team_work_env/bin/activate
```
������� ���������� ��� ����:
```
mkdir /opt/venv/team_work_env/run/
mkdir /opt/venv/team_work_env/logs/
mkdir /opt/venv/team_work_env/logs/nginx/
```
������������� �����:
```
chown -R hh /opt/venv/team_work_env
```
��������� �����������:
```
git clone https://github.com/GeekbrainsProject/team_work.git /opt/venv/team_work_env/src
cd team_work_env/
```
������ �����������:
```
pip3 install -r /opt/venv/team_work_env/src/team_work/requirements.txt
```
#### �����������������
```
python3 manage.py createsuperuser
```
� ������� (�����/������): admin:admin
#### ���������� �������� � ���� ����������� ������ �������
��������� ��������:
```
python3 manage.py migrate
```
�������� �������:
```
python3 manage.py collectstatic
```
#### ��������� ���� ������ ��������� ������� (�� �����������)
```
python3 manage.py fill_db
```
#### ���� �������
```
python3 manage.py runserver
```
#### ���������� ���� �������
```
chown -R xabr /home/team_work_env/
chmod -R 755 /home/team_work_env/team_work/
```
�������� ��������� ������ �gunicorn�
```
sudo nano /etc/systemd/system/gunicorn.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=USER_NAME
Group=www-data
WorkingDirectory=/home/team_work_env/team_work
ExecStart=/home/team_work_env/team_work/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/team_work_env/team_work/team_work.sock xabr.wsgi

[Install]
WantedBy=multi-user.target

```
������������� � ������ �������
```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```
��������� ���������� ��� nginx
```
sudo nano /etc/nginx/sites-available/team_work.conf

server {
    listen 80;
    server_name 151.248.117.226; ### server_name ��������� �������� ip-����� �������

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/team_work_env/team_work;
    }

    location /media/ {
        root /home/team_work_env/team_work;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/team_work/team_work/team_work.sock;
    }
}
```
������������� ������ �nginx�
```
sudo systemctl restart nginx
```
#### �������������� ����
```
sudo ln -s /etc/nginx/sites-available/team_work /etc/nginx/sites-enabled
```

### ����� ����� � �������� ����� ������ ip-����� ������� � ��������� ������.
#### ����� ��������� �� Git:
```
source /opt/venv/team_work/bin/activate
cd /opt/venv/team_work/src
git pull origin master
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic