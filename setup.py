from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    name="hungr.ai",
    version=__version__,
    description="Hungry hippos with AI",
    author="Raphael Koh",
    author_email="raph.koh@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=0.10.0",
        "Flask-Webpack>=0.0.7"
    ]
)
