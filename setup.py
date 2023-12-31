from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='animaloc',
    version='0.1.0',
    description='Segmentation semantique',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ElvinaAlphna/ProjetDoctoral',

    # Author details
    author='Elvina Alphna',
    author_email='Elvina.Alphna.Mekui.Me.Kemoe@usherbrooke.ca',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='~=3.8',
    # What does your project relate to?
    keywords='classification de loccupation du sol',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=['animaloc'],
    # package_dir={'phd-code': 'animaloc'},
    packages=find_packages()
)