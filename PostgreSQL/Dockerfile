FROM postgres:latest

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

COPY ./init-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 5432
