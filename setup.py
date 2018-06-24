import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sqlinspector2",
    version="1.0.1",
    author="Franklin Sarmiento",
    author_email="franklinitiel@gmail.com",
    description="Middleware that allow check the times applied and the SQL amount used on any request and response process on django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/franklintiel/sqlinspector2.git",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="sql inspector sqlinspector django2",
    project_urls={
        'Documentation': "https://github.com/franklintiel/sqlinspector2",
        'Source': "https://github.com/franklintiel/sqlinspector2",
        'Tracker': "https://github.com/franklintiel/sqlinspector2/issues"
    },
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=["Django"],
    python_requires=">=3.*"
    )