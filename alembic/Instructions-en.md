我想用
- [alembic.ini](alembic.ini) To relate [alembic](alembic) Maintenance api library
- [alembic_mock.ini](alembic_mock.ini) To relate [alembic_mock](alembic_mock) Maintenance mock library

As you can see, I want to pass [base.py](app%2Fmodel%2Fbase.py) ApiBase and MockBase To associate the api and mock library, respectively
But when I run
```shell
alembic --config alembic_mock.ini revision --autogenerate -m "initial mock trade model"
```
[user.py](app%2Fmodel%2Fuser.py) Will also be associated with [versions](alembic_mock%2Fversions) 


