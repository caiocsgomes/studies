FROM debian:bullseye

RUN apt-get update && apt-get install -y apache2 && apt-get clean
RUN chown www-data:www-data /var/lock
# set environment variables inside the container
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

COPY index.html /var/www/html  

USER root

WORKDIR /var/www/html

LABEL description="Webserver"
LABEL version="1.0.0"

VOLUME /var/www/html
EXPOSE 80

# ENTRYPOINT is the default container process
# if not specified the DEFAULT is /bin/sh
ENTRYPOINT ["/usr/sbin/apachectl"]

# CMD is the parameter from the ENTRYPOINT
# there is no default CMD  
CMD ["-D", "FOREGROUND"]