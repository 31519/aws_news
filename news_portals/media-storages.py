# AWS S3 Media Files Configuration


from django.core.files.storage  import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False



