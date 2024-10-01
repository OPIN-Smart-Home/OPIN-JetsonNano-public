# Use the official Node-RED Docker image as the base
FROM nodered/node-red:latest-debian

# Switch to root user to install system packages
USER root

# Install PostgreSQL and Python
RUN apt-get update && apt-get install -y postgresql postgresql-contrib python3 python3-pip docker.io && apt-get clean

# Install the Python 'requests' library
RUN pip3 install requests

# Set work directory
WORKDIR /usr/src/node-red

# Copy the files into the container
COPY . .
COPY ./pg_hba.conf /etc/postgresql/13/main
COPY ./postgresql.conf /etc/postgresql/13/main
RUN chmod +x /usr/src/node-red/start.sh

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=opin
ENV POSTGRES_PASSWORD=postgresql
ENV POSTGRES_DB=opin

# Start PostgreSQL service and create the database and user
RUN pg_ctlcluster 13 main start && \
    sleep 5 && \
    psql -U postgres -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD' SUPERUSER CREATEDB;" && \
    psql -U postgres -c "CREATE DATABASE $POSTGRES_DB;" && \
    psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;" && \
    export PGPASSWORD=$POSTGRES_PASSWORD && \
    psql -U $POSTGRES_USER -d $POSTGRES_DB -f ./opin.pgsql && \
    unset PGPASSWORD && \
    python3 /usr/src/node-red/init.py && \
    cp /usr/src/node-red/flows.json /data/ && \
    pg_ctlcluster 13 main stop

# Copy and set permissions for the credentials file
COPY ./flows_cred.json /data

# Copy the Node-RED package into the container
WORKDIR /root/.node-red
RUN cp /usr/src/node-red/flows.json .
COPY ./flows_cred.json .
COPY ./package.json .
RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production

# Back to work directory
WORKDIR /usr/src/node-red

# Expose Node-RED and PostgreSQL ports
EXPOSE 1880 5432

# Use entrypoint to manage services
ENTRYPOINT ["/usr/src/node-red/start.sh"]

# Default command
CMD ["node-red"]
