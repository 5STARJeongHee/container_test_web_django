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

ADD ~/django_app_config.sh /home/ubuntu/test_web

RUN chmod 777 /home/ubuntu/test_web/django_app_config.sh

ENV DB="mysql" DB_HOST="mysql" DB_NAME="student_list" DB_USER="root" DB_PASSWORD="0000" settings_dir="container_test_web_django/web_project/Project1/settings.py" APP_PORT="8000"

ADD ~/start.sh /home/ubuntu/test_web

RUN chmod 777 /home/ubuntu/test_web/start.sh

ENTRYPOINT /home/ubuntu/test_web/start.sh $settings_dir $DB $DB_HOST $DB_NAME $DB_USER $DB_PASSWORD $APP_PORT