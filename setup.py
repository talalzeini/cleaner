# python3 -m pip install py2app
# python3 setup.py py2app

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('data', ['data/extensions.json', 'data/directories.json'])
]

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'image.png', 
}

setup(
    app=APP,
    name="Cleaner",
    data_files=DATA_FILES,
    version="0.0.1",
    options={'py2app': OPTIONS},
    setup_requires=["py2app"]
)