from distutils.core import setup

setup(
    name='cmptcomplexity',
    version='0.99',
    packages=['cmptcomplexity', 'cmptcomplexity.scripts'],
    url='https://github.com/AGHPythonCourse2017/zad2-moskalap',
    license='GNU General Public License v3.0',
    author='moskalap',
    author_email='przemyslaw.moskala@gmail.com',
    description='a module for counting complexity of algorithm',
    requires=['numpy', 'scipy', 'matplotlib']
)
