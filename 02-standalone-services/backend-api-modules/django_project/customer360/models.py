from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    social_media = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        ordering = ["-id"]
        # Permission specific to Managers
        permissions = [
            ("can_manage_customers", "Can create and provision customer profiles"),
        ]

    def __str__(self):
        return f"{self.name} (ID: {self.id})"


class Interaction(models.Model):
    class ChannelChoices(models.TextChoices):
        PHONE = 'phone', _('Phone')
        SMS = 'sms', _('SMS')
        EMAIL = 'email', _('Email')
        LETTER = 'letter', _('Letter')
        SOCIAL_MEDIA = 'social_media', _('Social Media')

    class DirectionChoices(models.TextChoices):
        INBOUND = 'inbound', _('Inbound')
        OUTBOUND = 'outbound', _('Outbound')

    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='interactions'
    )
    channel = models.CharField(max_length=15, choices=ChannelChoices.choices)
    direction = models.CharField(max_length=10, choices=DirectionChoices.choices)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()

    class Meta:
        verbose_name = _("Interaction")
        verbose_name_plural = _("Interactions")
        ordering = ["-interaction_date"]
        # Permission specific to Agents
        permissions = [
            ("can_log_interactions", "Can log and record customer interactions"),
        ]

    def __str__(self):
        return f"{self.customer.name} - {self.get_channel_display()} ({self.interaction_date})"