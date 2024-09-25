我想用
- [alembic.ini](alembic.ini) 来关联 [alembic](alembic) 维护 api 库
- [alembic_mock.ini](alembic_mock.ini) 来关联 [alembic_mock](alembic_mock) 维护测试库

如你所见，我想通过 [base.py](app%2Fmodel%2Fbase.py) 的 ApiBase 和 MockBase 来分别关联 api 和 mock 库
但是当我运行
```shell
alembic --config alembic_mock.ini revision --autogenerate -m "initial mock trade model"
```
[user.py](app%2Fmodel%2Fuser.py) 也会被关联到 [versions](alembic_mock%2Fversions) 中


