from reversion.models import Version

from django.db import models
from django.utils.functional import cached_property


class MetaDataModel(models.Model):
    class Meta:
        abstract = True

    @cached_property
    def versions(self):
        return list(Version.objects.get_for_object(self))

    @property
    def created_at(self):
        if self.versions:
            return self.versions[0].revision.date_created

        return None

    @property
    def updated_at(self):
        if self.versions:
            return self.versions[-1].revision.date_created

        return None

    @property
    def deleted_at(self):
        return None
