import os
from google import genai

client = genai.Client()
result = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='A highly professional, dark-mode, cyberpunk-aesthetic 1:1 square thumbnail image, neon lines, abstract technology and AI themes',
    config=dict(
        number_of_images=1,
        output_mime_type="image/jpeg",
        aspect_ratio="1:1"
    )
)
for generated_image in result.generated_images:
    with open('test_image.jpg', 'wb') as f:
        f.write(generated_image.image.image_bytes)
