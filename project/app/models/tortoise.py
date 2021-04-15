# project/app/models/tortoise.py

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


# Check https://tortoise-orm.readthedocs.io/en/latest/contrib/pydantic.html?highlight=pydantic_model_creator#basic-usage
# to understand how to generate pydantic model from tortoise
SummarySchema = pydantic_model_creator(TextSummary)
