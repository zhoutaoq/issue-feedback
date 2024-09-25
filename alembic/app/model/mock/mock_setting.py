#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入所需的模块
import uuid
from datetime import datetime, timezone

from app.model.base import MockBase
from sqlalchemy import func, TIMESTAMP
from sqlmodel import Field, Column


class MockSetting(MockBase, table=True):
    __tablename__ = "mock_setting"
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                 sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=None))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                 sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(),
                                                  onupdate=func.now()))
