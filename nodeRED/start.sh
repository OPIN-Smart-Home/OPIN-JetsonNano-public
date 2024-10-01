#!/bin/bash

# Start PostgreSQL service
service postgresql start

# Wait for PostgreSQL to be ready
until pg_isready -h localhost -p 5432; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Start Node-RED
exec node-red
