from setuptools import setup, find_packages

setup(
    name='thinrest',
    version='2.0.0',
    description='Rest implementation using Tastypie.',
    long_description=open('README.md').read(),
    author='Anurag Agarwal',
    author_email='anurag26@gmail.com',
    url='https://github.com/anuragal/thinrest',
    packages=find_packages(),
    keywords='rest implementation tastypie',
    license=open('LICENSE').read(),
    zip_safe=False,
    install_requires = (
            'Django==1.11.29',
            'django-tastypie>=0.12.2',
            'South>=0.7.6'
        ),
    package_data={b'thinrest.fixtures': ['sample.json']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)