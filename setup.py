import os
import sys
import uwsgiconfig as uc
import shutil

from setuptools import setup
from setuptools.dist import Distribution
from setuptools.command.install import install
from setuptools.command.build_ext import build_ext

class uWSGIBuilder(build_ext):

	def run(self):
		uc.parse_vars()
		uc.build_uwsgi(sys.prefix + '/bin/' + uc.UWSGI_BIN_NAME)


class uWSGIInstall(install):

	def run(self):
		if self.record:
			record_file = open(self.record,'w')
			sys.stdout = record_file
			sys.stderr = record_file
		uc.parse_vars()
		uc.build_uwsgi(sys.prefix + '/bin/' + uc.UWSGI_BIN_NAME)

class uWSGIDistribution(Distribution):

	def __init__(self, *attrs):
		Distribution.__init__(self, *attrs)
		self.cmdclass['install'] = uWSGIInstall
		self.cmdclass['build_ext'] = uWSGIBuilder
		


setup(name='uWSGI',
      version='0.9.5',
      description='The uWSGI server',
      author='Unbit',
      author_email='info@unbit.it',
      url='http://projects.unbit.it/uwsgi/',
      license='GPL2',
      distclass = uWSGIDistribution,
     )



