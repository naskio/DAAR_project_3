from django.db import models
from .utils import extract_text_from_file
# from .utils import parse_resume
import os
from django.conf import settings


class Resume(models.Model):
    first_name = models.CharField("First Name", blank=True, null=True, default=None, max_length=60)
    last_name = models.CharField("Last Name", blank=True, null=True, default=None, max_length=60)
    attached_file = models.FileField("CV", upload_to='CVs', blank=False, null=False)

    def __str__(self):
        return self.full_name or f"{self.id}"

    @property
    def full_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.upper()}"
        if self.first_name:
            return self.first_name.capitalize()
        if self.last_name:
            return self.last_name.capitalize()
        return ""

    @property
    def text(self) -> str:
        if self.attached_file:
            return extract_text_from_file(os.path.join(settings.BASE_DIR, self.attached_file.path)) or ""
        else:
            return ""

    # @property
    # def parsed(self):
    #     if self.attached_file:
    #         return parse_resume(os.path.join(settings.BASE_DIR, self.attached_file.path))
    #     else:
    #         return {}

    class Meta:
        verbose_name_plural = "resumes"
        verbose_name = "resume"
