from setuptools import setup

setup(
    name='Flask-Redtask',
    version='0.1',
    url='http://github.com/muromec/flask-redtask',
    license='BSD',
    author='Ilya Petrov',
    author_email='ilya.muromec@gmail.com',
    description='Redqueue integration for flask',
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'python-memcached',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
