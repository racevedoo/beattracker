from django.db import models

def track_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'tracks/{0}'.format(filename)

# Create your models here.
class Track(models.Model):
    length = models.IntegerField(default=0)
    track_file = models.FileField(upload_to=track_directory_path)