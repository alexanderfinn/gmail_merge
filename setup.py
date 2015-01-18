from setuptools import setup


setup(
    name='gmail_merge',
    version='0.1.0',
    description='Send bulk e-mails from templates using GMail',
    author='Alexander Finn',
    author_email='finnam@gmail.com',
    url='https://github.com/alexanderfinn/gmail_merge',
    packages=['gmail_merge',],
    install_requires=['google-api-python-client',],
)