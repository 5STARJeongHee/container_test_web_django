1.7v 쓰는게 좋아요 간단한 장고 앱으로 이름과 관련 정보를 입력하면

mysql db 컨테이너와 통신하여 저장된 정보를 출력해주는 간단한 앱입니다.

-------------------------------------------------------------------------

# dockerfile

~~~
FROM qhxmaoflr/ftp_nginx:1v

RUN apt-get update && \

apt-get upgrade -y

RUN apt-get install -y python3.7 python3.6 python3-pip libmysqlclient-dev libssl-dev git

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

RUN pip3 install --upgrade pip

RUN pip3 install virtualenv

WORKDIR /home/ubuntu

RUN virtualenv --python=python3.6 test_web

WORKDIR /home/ubuntu/test_web

RUN git clone https://github.com/5STARJeongHee/container_test_web_django.git

RUN chmod 777 bin/activate && \

bin/activate && \

pip install mysqlclient django

ADD django_app_config.sh /home/ubuntu/test_web

RUN chmod 777 /home/ubuntu/test_web/django_app_config.sh

ENV DB="mysql" DB_HOST="mysql" DB_NAME="student_list" DB_USER="root" DB_PASSWORD="0000" settings_dir="container_test_web_django/web_project/Project1/settings.py" APP_PORT="8000"

ADD start.sh /home/ubuntu/test_web

RUN chmod 777 /home/ubuntu/test_web/start.sh

ENTRYPOINT /home/ubuntu/test_web/start.sh $settings_dir $DB $DB_HOST $DB_NAME $DB_USER $DB_PASSWORD $APP_PORT

~~~
-----------------------------------------------------------------------------------

# django_app_config.sh

~~~
'''bash
#!/bin/bash

sed -i "/ENGINE/ s/mysql/$2/" $1

sed -i "/HOST/ s/mysql/$3/" $1

sed -i "71,90 s/student_list/$4/g" $1

sed -i "71,90 s/root/$5/g" $1

sed -i "71,90 s/0000/$6/g" $1
'''
~~~
------------------------------------------------------------------------------------------------------

# start.sh

~~~
#!/bin/bash

/home/ubuntu/test_web/django_app_config_sh $1 $2 $3 $4 $5 $6

/home/ubuntu/test_web/bin/activate

python container_test_web_django/web_project/manage.py migrate

python container_test_web_django/web_project/manage.py runserver 0:$7
~~~

## usage

먼저 mysql 서버 컨테이너를 허브에서 받아서 실행 sudo docker run --name mysql -v /fordocker:/home/ailab/DB -e MYSQL_ROOT_PASSWORD='0000' -dit mysql 그 뒤 db 컨테이너에 접속하 database 생성

장고 웹 어플을 실행하려면 위의 과정이 우선 되어 있어야 된다. 이제 장고 웹어플을 실행해보자

sudo docker run -e DB_NAME=student -e DB_PASSRD=0000 --link=mysql --rm -it -p 60000:8000 qhxmaoflr/django_app:1.7v

옵션 DB_ HOST(--link 옵션으로 연결할 db 컨테이너 이름), DB_NAME(db서버의 데이터베이스 이름), DB_USER(DB 유저 이름 기본 root), DB_PASSWORD(db 패스워드)

# docker-compose.yml

~~~
version: '3.0'

services:

db:

      image: mysql

      restart: always

      volumes:

           - /home:/home/ailab/DB

      environment:

          - MYSQL_ROOT_PASSWORD=0000

          - MYSQL_DATABASE=student_info

          - MYSQL_USER=heyhey

          - MYSQL_PASSWORD=0000


django:

      image: qhxmaoflr/django_app:1.7v

      restart: always

      environment:

          - DB=mysql

          - DB_HOST=db

          - DB_NAME=student_info

          - DB_PASSWORD=0000

          - DB_USER=heyhey

      ports:

          - "60000:8000"

          - "10000-11000:10000-11000"

          - "8080:80"

          - "60001-60002:20-21"
~~~
