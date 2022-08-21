from setuptools import setup, find_packages

version = '0.1.4'

setup(name='django-ping',
      version=version,
      description="Django Monitoring and Availability Utility",
      long_description="",
      classifiers=[
          "Development Status :: 1",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='',
      author='Rohit Rehan',
      url='',
      license='MIT',
      packages=find_packages(),
      install_requires = [],
      include_package_data=True,
      zip_safe=False,
    )