docker run -d --name brazil-e-commerce-postgres \
-e POSTGRES_PASSWORD=brazilpw \
-v $HOME/postgres-data/:/var/lib/postgresql/data \
-p 5431:5432 postgres

psql -h localhost -p 5431 -U postgres -c "CREATE USER tc with password 'brazilpw';"
psql -h localhost -p 5431 -U postgres -c "CREATE DATABASE ecommerce WITH TEMPLATE = template0;"
psql -h localhost -p 5431 -U postgres -c "ALTER DATABASE ecommerce OWNER to tc;"
