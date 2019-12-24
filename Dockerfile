# ベースイメージ
FROM python:3.8

RUN mkdir /var/www
WORKDIR /var/www

COPY pyproject.toml ./
COPY poetry.lock ./
RUN pip install poetry
RUN poetry install

WORKDIR /var/www/src

RUN apt-get update
RUN apt-get install -y curl

RUN curl http://nginx.org/keys/nginx_signing.key | sudo apt-key add -

VCNAME=`cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2` && sudo -E sh -c "echo \"deb http://nginx.org/packages/ubuntu/ $VCNAME nginx\" >> /etc/apt/sources.list"
VCNAME=`cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2` && sudo -E sh -c "echo \"deb-src http://nginx.org/packages/ubuntu/ $VCNAME nginx\" >> /etc/apt/sources.list"

sudo apt-get update
sudo apt-get install nginx

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
