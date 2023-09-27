from setuptools import setup

APP = ['whatsapp_mac.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app_icon.icns',
    'plist': {
        'CFBundleName': 'whatsapp_mac',
        'CFBundleShortVersionString': '1.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'de.tm_marketing_service.whatsapp_mac',
        'CFBundleExecutable': 'whatsapp_mac',
        'CFBundleIconFile': 'app_icon.icns',
        'LSUIElement': '1',
    },
    'packages': ['webdriver-manager', 'selenium'],
    'includes': ['tkinter'],
    'arch': 'i386,x86_64',
}

setup(
    app=APP,
    name='whatsapp_mac',
    author='TM_marketing_service',
    author_email='kontakt@tm-marketingservice.de',
    maintainer='TM',
    maintainer_email='kontakt@tm-marketingservice.de',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)