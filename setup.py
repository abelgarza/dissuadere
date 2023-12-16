from setuptools import setup, find_packages
import os

# Lee las dependencias desde requirements.txt
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

# Uso de setuptools_scm para el versionado
setup(
    name='dissuadere',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=install_requires,  # Utiliza las dependencias de requirements.txt
    author='Abel Garza',
    author_email='abel@ciberdata.net',
    description='Breve descripción del juego dissuadere',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abelgarza/dissuadere',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
