import sys, os

# should be able to safely do this now.
from setuptools import setup, find_packages

setup(name='pairadise',
      version='1.0.0',
      packages = find_packages('src'),  # include all packages under src
			package_dir = {'':'src'},   # all distutils packages are under src
      entry_points={'console_scripts': ['pairadise_annotate=pairadise_annotate.scripts.annotate:main','pairadise_assign=pairadise_assign.scripts.assign:main','pairadise_count=pairadise_count.scripts.count:main','pairadise_map=pairadise_map.scripts.map:main','pairadise_personalize=pairadise_personalize.scripts.personalize:main']},
			description = 'pairadise',
			author = 'Emad Bahrami-Samani, Shayna R. Stein',
			author_email = 'bahramise1@email.chop.edu',
			url = 'https://github.com/bahrmis/pairadise',
			download_url = 'https://github.com/bahramis/pairadise/tarball/pairadise_1.0.0',
			license='GPL3',
			keywords = [],
			classifiers = [],
)
