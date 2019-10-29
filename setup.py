from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='FASTA_parser',
      version='0.1',
      description='A first try on FASTA files parsing',
      classifiers=[
        'Development Status :: Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Bioinformatics :: FASTA',
        ],
      keywords='FASTA files parser',
      url='https://github.com/Fercho120/FASTA',
      author='Fernando Garcia',
      author_email='dfgr0316@gmail.com',
      license='MIT',
      packages=['FASTA_parser'],
      install_requires = ["biopython >= 1.72",],
      include_package_data=True,
      zip_safe=False,
      entry_points = {
        'console_scripts': ['is_fasta=FASTA_parser.command_line:main'],
      },
      )
