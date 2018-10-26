#!/usr/bin/env bash
export PGPASSWORD=${POSTGRES_PASSWORD}
psql --host fogerty.upc.es \
     --user ${POSTGRES_USER} \
     --dbname ${POSTGRES_DB} \
     --command "CREATE USER postgres SUPERUSER;" \
    || echo "User postgres not created"

exit 0
