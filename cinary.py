import os
import sys

from cloudinary.api import resources_by_tag, delete_resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('cloud_settings.py'):
    exec(open('cloud_settings.py').read())

DEFAULT_TAG = "time_table"


def upload_timetables(loader):
    urls = []
    for i in loader:
        response = upload(i, tags=DEFAULT_TAG)
        url, options = cloudinary_url(
            response['public_id'],
            format=response['format'],
            width=3000,
            crop="scale"
        )
        print(url)
        urls.append(url)


def cleanup():
    response = resources_by_tag(DEFAULT_TAG)
    resources = response.get('resources', [])
    if not resources:
        print("No images found")
        return
    print("Deleting {0:d} images...".format(len(resources)))
    delete_resources_by_tag(DEFAULT_TAG)
    print("Done!")


if __name__ == '__main__':
    load = ['pizza.jpg', 'test.jpg']
    # upload_timetables(load)
    cleanup()
