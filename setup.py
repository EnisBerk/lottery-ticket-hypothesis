from setuptools import setup,find_packages

SHORT_DESCRIPTION = """
An implementation of the lottery ticket hypothesis experiment.""".strip()

DEPENDENCIES = [
    'six',
    'fire',
    'tensorflow',
    'keras',
    'numpy',
    'absl-py',
]

VERSION = '1'

setup(
    name='lottery_ticket',
    version=VERSION,
    description=SHORT_DESCRIPTION,

    author='Jonathan Frankle',
    author_email='jfrankle@google.com',
    license='Apache Software License',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],

    keywords='lottery ticket hypothesis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    # package_dir={'lottery_ticket': '.',
    #              'lottery_ticket.foundations': './foundations',
    #              'lottery_ticket.datasets': './datasets',
    #              'lottery_ticket.mnist_fc': './mnist_fc'},

    install_requires=DEPENDENCIES,
)
