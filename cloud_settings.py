# Cloudinary settings for Django. Add to your settings file.
CLOUDINARY = {
    'cloud_name': '',
    'api_key': '',
    'api_secret': '',
}

# Cloudinary settings using python code. Run before cloudinary is used.
import cloudinary

cloudinary.config(
    cloud_name='',
    api_key='',
    api_secret=''
)
