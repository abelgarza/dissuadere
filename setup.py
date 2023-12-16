# setup.py

from setuptools import setup, find_packages
import os

# Uso de setuptools_scm para el versionado
setup(
    name='dissuadere',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias, reemplaza con las reales
        'numpy',
        'pandas',
        # etc.
    ],
    author='Abel Garza',
    author_email='abel@ciberdata.net',
    description='Breve descripción del juego dissuadere',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://tu-repositorio-del-juego.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
