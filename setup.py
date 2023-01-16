import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serialmidi",
    version="0.0.1",
    author="originated by raspy135, modified by tantanGH",
    author_email="",
    license='Apache License 2.0',
    description="modified version of serialmidi with pip install capability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/serialmidi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'serialmidi=serialmidi.serialmidi:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    setup_requires=["setuptools"],
    install_requires=["pyserial","python-rtmidi"],
)
