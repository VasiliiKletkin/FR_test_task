from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    date_start = models.DateTimeField(verbose_name="Mailing start")
    date_end = models.DateTimeField(verbose_name="End of mailing")
    time_start = models.TimeField(verbose_name="Start time to send message")
    time_end = models.TimeField(verbose_name="End time to send message")
    text = models.TextField(max_length=255, verbose_name="Message text")
    tag = models.CharField(
        max_length=100, verbose_name="Search by tags", blank=True)
    mobile_operator_code = models.CharField(
        verbose_name="Search by mobile operator code", max_length=3, blank=True
    )

    @property
    def to_send(self) -> bool:
        return self.date_start <= timezone.now() <= self.date_end

    def __str__(self):
        return f"Mailing {self.id} from {self.date_start}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
