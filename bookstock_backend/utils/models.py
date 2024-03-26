from django.db import models
import uuid


class DatedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        abstract = True


class BaseModel(DatedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
