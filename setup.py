from setuptools import find_packages, setup


with open('requirements.txt') as fin:
    REQUIREMENTS = [line.strip() for line in fin if '#' not in line]


with open('README.md') as readme:
    README = readme.read()


setup(
    name='django-logging-context',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    long_description_content_type="text/markdown",
    description=(
        'Django library extending default logging context'),
    long_description=README,
    install_requires=REQUIREMENTS,
    url='https://github.com/pik-software/django-logging-context',
    author='Pik Digital',
    author_email='nsi-dev@pik.ru',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: Log Analysis',
        'Topic :: System :: Logging',
    ]
)
