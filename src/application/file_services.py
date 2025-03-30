import uuid
from infrastructure.storage.s3_service import S3StorageService
from infrastructure.storage.blob_service import BlobStorageService
from infrastructure.documents.tasks import save_metadata_to_db

def handle_file_upload(file, provider):
    object_key = f"files/{uuid.uuid4()}-{file.name}"

    if provider.upper() == 'S3':
        storage = S3StorageService()
    elif provider.upper() == 'AZURE':
        storage = BlobStorageService()
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    url = storage.upload_file(file, object_key)

    save_metadata_to_db.delay(file.name, provider, object_key, url)

    return {"message": "Upload queued", "object_key": object_key, "url": url}
