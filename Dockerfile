FROM mysql/mysql-server

ENV MYSQL_DATABASE=door2door \
    MYSQL_ROOT_PASSWORD=123 \
    MYSQL_ROOT_HOST=%

ADD door2door-schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306