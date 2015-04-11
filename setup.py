from setuptools import setup
from setuptools import Extension
import platform

if platform.system() == 'Windows':
	scsi_compile_args = []
else:
	scsi_compile_args = ["-Wno-write-strings"]


setup(	name='pybadusb',
		version='0.2',
		packages=['pybadusb'],
		ext_package='pybadusb',
		ext_modules=[Extension('scsi', ['pybadusb/src/scsi.cpp'], extra_compile_args = scsi_compile_args)],
	)
