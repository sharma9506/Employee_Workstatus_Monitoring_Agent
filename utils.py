from io import BytesIO
from PIL import Image

def compress_image(image_data):
    # Open image from bytes
    image = Image.open(BytesIO(image_data))
    
    # Compress image by saving it to a new BytesIO buffer
    buffer = BytesIO()
    image.save(buffer, format='JPEG', quality=85)  # quality is adjustable (0-100)
    
    return buffer.getvalue()  # Return compressed image as bytes
