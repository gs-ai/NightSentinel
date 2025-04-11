import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_file_metadata(file_path):
    """Extracts basic metadata from a file."""
    try:
        metadata = {
            'file_name': os.path.basename(file_path),
            'file_size': os.path.getsize(file_path),
            'file_type': os.path.splitext(file_path)[-1]
        }
        return metadata
    except Exception as e:
        print(f"Error extracting file metadata: {e}")
        return None

def extract_image_metadata(image_path):
    """Extracts EXIF metadata from an image."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        metadata = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
        return metadata
    except Exception as e:
        print(f"Error extracting image metadata: {e}")
        return None