Installation
============

[![Python package](https://github.com/chdemko/pandoc-latex-french-spaces/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-french-spaces/actions/workflows/python-package.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-french-spaces/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-french-spaces?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-french-spaces.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-french-spaces/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-latex-french-spaces/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-latex-french-spaces/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-french-spaces/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-french-spaces)
[![Codacy](https://img.shields.io/codacy/grade/2548c9dc7d39429597188a9df6e0d1a0.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-french-spaces/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-french-spaces.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-french-spaces/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-french-spaces.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-french-spaces/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-french-spaces.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-french-spaces/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-french-spaces?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-french-spaces)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-french-spaces.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-french-spaces/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-french-spaces.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-french-spaces/)
[![Poetry version](https://img.shields.io/badge/poetry-1.2%20|%201.3%20|%201.4%20|%201.5%20|%201.6%20|%201.7-blue.svg?logo=poetry)](https://python-poetry.org/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-french-spaces.svg?logo=github)](https://github.com/chdemko/pandoc-latex-french-spaces/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-french-spaces/develop?logo=github)](https://github.com/chdemko/pandoc-latex-french-spaces/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-french-spaces.svg?logo=github)](http://pandoc-latex-french-spaces.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-french-spaces.svg?logo=github)](http://pandoc-latex-french-spaces.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-french-spaces.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-french-spaces)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-french-spaces.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-french-spaces.readthedocs.io/en/latest/)

*pandoc-latex-french-spaces* is a [pandoc] filter for dealing with french
spacing rules for ponctuations in *LaTeX*.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-french-spaces* requires [python], a programming language that
comes pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-french-spaces* as using the bash command

~~~shell-session
$ pipx install pandoc-latex-french-spaces
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-french-spaces
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-french-spaces*, please feel
welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-french-spaces/issues

Contribute
==========

Instructions
------------

Install `poetry`, then run

~~~shell-session
$ poetry install
$ poetry shell
~~~

And submit your changes. When you commit, hooks will be executed to check
your code.

