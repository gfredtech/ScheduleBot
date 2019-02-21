# Cloudinary settings for Django. Add to your settings file.
CLOUDINARY = {
    'cloud_name': 'dhpzvfror',
    'api_key': '189133823467731',
    'api_secret': 'bG5lE7HT0KwhrvoRecQefpPak4s',
}

# Cloudinary settings using environment variables. Add to your .bashrc


# Cloudinary settings using python code. Run before cloudinary is used.
import cloudinary

cloudinary.config(
    cloud_name='dhpzvfror',
    api_key='189133823467731',
    api_secret='bG5lE7HT0KwhrvoRecQefpPak4s'
)
