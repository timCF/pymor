from distutils.core import setup
setup(
  name = 'pymorc',
  packages = ['pymor'],
  version = '0.1',
  description = 'Simple console util for morph analysis',
  author = 'timCF',
  author_email = 'llStrainll@gmail.com',
  url = 'https://github.com/timCF/pymor', # use the URL to the github repo
  download_url = 'https://github.com/timCF/pymor/tarball/0.1', # I'll explain this in a second
  keywords = ['morphology', 'russian', 'pymorphy2', 'pymorphy', 'console'], # arbitrary keywords
  classifiers = [],
  install_requires=['sys','pymorphy2','pipe']
)