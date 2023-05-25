# python3 -m pip install py2app
# python3 setup.py py2app

from setuptools import setup

APP = ['main.py']

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'image.png', 
}

setup(
    app=APP,
    name="Cleaner",
    version="0.0.1",
    options={'py2app': OPTIONS},
    setup_requires=["py2app"]
)