#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from datetime import datetime, timezone

from app.model.base import ApiBase
from sqlalchemy import UniqueConstraint, func, TIMESTAMP
from sqlmodel import Field, Column


# 导入所需的模块


class UserModel(ApiBase, table=True):
    __tablename__ = "users"

    # 定义模型字段
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                 sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=None))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                 sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(),
                                                  onupdate=func.now()))

    __table_args__ = (
        # 国家区号+手机号码唯一约束
        UniqueConstraint('country_code', 'phone_number', name='uq_countrycode_phonenumber'),
    )
