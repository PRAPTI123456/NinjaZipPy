from setuptools import setup, find_packages

setup(
    name="ninjazippy",  # Name of your package
    version="0.1",      # Initial version
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "py7zr"  # Dependency for 7z compression
    ],
    entry_points={
        "console_scripts": [
            "ninjazippy=ninjazippy.cli:main",  # Allows running `ninjazippy` from terminal
        ],
    },
    author="Your Name",
    description="A Python utility to zip/unzip .7z archives (migrated from bit7z)",
    python_requires='>=3.7',
)
