from pathlib import Path
from setuptools import setup, find_packages

with (Path(__file__).resolve().parent / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="brookie_plugin_library_calibre",
    version="0.1.0",
    description="Calibre library plugin for brookie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeanMarc-Moly/brookie_plugin_library_calibre",
    author="MOLY Jean-Marc",
    author_email="jeanmarc.moly@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="development",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.9.*, <4",
    install_requires=[
        "aiosqlite==0.17.0",
        "databases[sqlite]==0.4.3",
        "python-libarchive==4.0.1.post1",
        "sqlalchemy==1.3.24; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "typing-extensions==3.10.0.0",
    ],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={"dev": []},  # Optional
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # Sometimes you’ll want to use packages that are properly arranged with
    # setuptools, but are not published to PyPI. In those cases, you can specify
    # a list of one or more dependency_links URLs where the package can
    # be downloaded, along with some additional hints, and setuptools
    # will find and install the package correctly.
    # see https://python-packaging.readthedocs.io/en/latest/dependencies.html#packages-not-on-pypi
    #
    dependency_links=[
        "git+https://github.com/JeanMarc-Moly/brookie_plugin_library_abstract.git@5655ac2667f04abfebe35dcc1852e8143056a2f8#egg=brookie-plugin-library-abstract"
    ],
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={"sample": ["package_data.dat"]},  # Optional
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[("my_data", ["data/data_file"])],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={"console_scripts": ["sample=sample:main"]},  # Optional
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        "Bug Reports": "https://github.com/pypa/sampleproject/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "http://saythanks.io/to/example",
        "Source": "https://github.com/pypa/sampleproject/",
    },
)
