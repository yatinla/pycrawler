try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

setup(name='pycrawler',
        version='0.1.0',
        description="A Python module for crawling through json to find the value of given attribute",
        long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
        author='Mike Taylor',
        author_email='mike@taylorwebhome.org',
        packages = ['pycrawler'],
        url="https://mediomuerto@bitbucket.org/mediomuerto/crawler.git",
        download_url="git@bitbucket.org:mediomuerto/crawler.git",
        license=open('LICENSE').read,
        data_files=[('', ['HISTORY.rst']),('',['LICENSE'])],
        include_package_data=True,
      )

