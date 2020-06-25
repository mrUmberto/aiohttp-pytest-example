import uuid

from peewee import CharField, UUIDField
from engine.db import BaseModel


class Bread(BaseModel):
    class Meta:
        table_name = 'bread'

    id = UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    name = CharField()
