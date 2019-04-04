import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="vidtext",
    version="1.0",
    url="https://github.com/anubhavshakya/vidtext",
    license='MIT',

    author="Anubhav Shakya",
    author_email="inbox.anubhavshakya@gmail.com",

    description="This Project or Package Is Made for to Convert the Text to Video",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=["pillow","google_images_download","rake_nltk","opencv-python"],

    classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: System Administrators', 
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3'
    ],
)
