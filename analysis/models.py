from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class WaterNetwork(models.Model):
    # Basic Information
    name = models.CharField(max_length=255, verbose_name="Network Name")
    description = models.TextField(blank=True, verbose_name="Description")
    
    # File Information
    file = models.FileField(
        upload_to='networks/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['inp'])],
        verbose_name="EPANET .inp File"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Upload Date")
    
    # User Association
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='water_networks',
        verbose_name="Uploaded By",
        null=True,  # Temporary for migration
        blank=True  # Temporary for migration
    )
    
    # Analysis Parameters
    PRESSURE_LIMIT = 30.0  # Default 30m pressure limit
    pressure_limit = models.FloatField(
        default=PRESSURE_LIMIT,
        verbose_name="Maximum Pressure Limit (m)"
    )
    
    # Status Tracking
    ANALYSIS_STATUS = [
        ('uploaded', 'Uploaded'),
        ('processing', 'Processing'),
        ('analyzed', 'Analyzed'),
        ('error', 'Error'),
    ]
    status = models.CharField(
        max_length=20,
        choices=ANALYSIS_STATUS,
        default='uploaded',
        verbose_name="Analysis Status"
    )
    
    # Metadata
    node_count = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Nodes")
    link_count = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Links")
    
    class Meta:
        verbose_name = "Water Network"
        verbose_name_plural = "Water Networks"
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.name} (Uploaded by {self.user.username if self.user else 'unknown'})"
    
    def save(self, *args, **kwargs):
        """Custom save method to extract metadata on creation"""
        if not self.pk:  # Only on creation
            try:
                import wntr
                wn = wntr.network.WaterNetworkModel(self.file.path)
                self.node_count = len(wn.nodes)
                self.link_count = len(wn.links)
                self.status = 'analyzed'
            except Exception as e:
                self.status = 'error'
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('network_detail', kwargs={'pk': self.pk})
    
    @property
    def file_size(self):
        """Returns the file size in KB"""
        if self.file:
            return self.file.size / 1024
        return 0