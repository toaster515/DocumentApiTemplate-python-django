from celery import shared_task
from infrastructure.documents.models import FileRecord

@shared_task
def save_metadata_to_db(file_name, provider, object_key, url):
    FileRecord.objects.create(
        file_name=file_name,
        provider=provider,
        object_key=object_key,
        url=url
    )