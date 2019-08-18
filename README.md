# beam-server

# To run Heroku Procfile locally:
```
heroku local web
```

# To create a new migration:
```
alembic revision -m "Add a column"
```

# To run a migration locally:
```
alembic upgrade head
alembic downgrade -1

```
# To run a migration on Heroku:
```
heroku run alembic upgrade head
heroku run alembic downgrade -1
```

# To deploy to Heroku:
```
heroku push origin master
```

# To start Postgresql console on Heroku:
```
heroku pg:psql
```