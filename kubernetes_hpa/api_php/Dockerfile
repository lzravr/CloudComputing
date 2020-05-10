FROM php:7-apache
RUN cd /usr/local/etc/php/conf.d/ && echo 'memory_limit = -1' >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini
COPY index.php /var/www/html/
