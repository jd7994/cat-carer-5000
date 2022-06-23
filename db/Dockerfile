FROM mysql:latest
ENV MYSQL_DATABASE=flask-db
COPY Create.sql /docker-entrypoint-initdb.d/
# Add the content of the .sql file to your image
# All scripts copied to docker-entrypoint-initdb.d/ are automatically
# executed during container startup