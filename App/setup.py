from setuptools import setup
from setuptools import find_packages


setup(
	name="sheng_nlp",
	version='0.0.1',
	packages=find_packages(),
	install_requires=[
	"click"
	],
	entry_points='''
	[console_scripts]
	sheng_nlp=App/main:sheng_nlp
	'''	
)