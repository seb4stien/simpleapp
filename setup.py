import setuptools

setuptools.setup(
    name="simpleapp",
    version="0.0.1",
    author="seb4stien",
    author_email="seb4stien@georget.name",
    description="Simple app",
    packages=["simpleapp"],
    python_requires=">3.4.3",
    install_requires=["Flask", "redis", "requests"],
)
