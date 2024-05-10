import os 

from setuptools import setup, find_packages

working_directory = os.path.abspath(os.path.dirname(__file__))
readme = os.path.join(working_directory, 'README.md')
requirements = os.path.join(working_directory, 'requirements.txt')

with open(readme) as rd:
    long_description = rd.read()
with open(requirements) as req:
    install_requires = req.read().splitlines()

setup(
        name='zoomdl',
        description='Download zoom recordings.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        version='0.0.1',
        author='pvpscript',
        url='https://github.com/pvpscript/zoomdl',

        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT Licence',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
        ],
        keywords='zoom, recording, downloader',

        packages=find_packages(),
        scripts=['scripts/zoomdl'],

        python_requires='>=3.6',
        install_requires=install_requires,

        project_urls={
            'Bug Reports': 'https://github.com/pvpscript/zoomdl/issues',
            'Source': 'https://github.com/pvpscript/zoomdl',
        },
)
