from setuptools import setup, find_packages

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='hbase-browser',
    version='0.0.1',
    description='HBase Browser with Python',
    license='Apache License 2.0',
    author='Ahmet Emre Aladağ',
    author_email='emre.aladag@agmlab.com',
    url='http://github.com/AGMLab/hbase-browser',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    tests_require=[
#        'unittest2',
#        'nose',
    ],
    #test_suite='runtests.collector',
    zip_safe=False,
    include_package_data=True,
)
