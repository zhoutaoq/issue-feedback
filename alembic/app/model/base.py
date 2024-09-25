from sqlmodel import SQLModel


class ApiBase(SQLModel, table=False):
    pass


class MockBase(SQLModel, table=False):
    pass
