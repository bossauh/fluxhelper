from distutils.core import setup
setup(
    name="fluxhelper",
    packages=["fluxhelper"],
    version="0.1",
    license="MIT",
    description="Helper library made for my projects",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="",
    download_url="",
    keywords=["helper"],
    install_requires=[
        "pycaw",
        "termcolor"
    ],
    classifiers=[
        "Development Status :: 5 - Production",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
