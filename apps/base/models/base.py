from django.db import models
import uuid


# base table common for all tables
class BaseModel(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        # ordering based on created date and time and this table not stored in DB
        ordering = ["-created_at"]
        abstract = True
        db_table = "base"
