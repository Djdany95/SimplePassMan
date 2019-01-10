from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SimplePassMan',
    description='Simple CLI password manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=['Windows', 'Linux', 'MacOS'],
    version='0.1',
    url='https://github.com/djdany01/SimplePassMan',
    author='Daniel J. Pérez Nieto',
    author_email='djdany.djesus@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Topic :: System :: Shells'
    ],
    license='MIT',
    packages=['SimplePassMan'],
    entry_points={
        'console_scripts': [
            'spm = SimplePassMan.__main__:main'
        ]
    })
