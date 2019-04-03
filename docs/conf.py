# -*- coding: utf-8 -*-
#
# HiCExplorer documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 23 13:37:43 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from unittest.mock import Mock

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


# import mock

MOCK_MODULES = ['numpy', 'numpy.core', 'numpy.core.multiarray', 'numpy.distutils.core', 'pandas', 'pysam', 'intervaltree',
                'scipy', 'scipy.sparse', 'scipy.stats', 'scipy.ndimage',
                'matplotlib', 'matplotlib.pyplot', 'matplotlib.gridspec', 'matplotlib.ticker',
                'matplotlib.textpath', 'matplotlib.patches', 'matplotlib.colors', 'matplotlib.cm',
                'mpl_toolkits', 'mpl_toolkits.axisartist', 'mpl_toolkits.mplot3d', 'mpl_toolkits.axes_grid1',
                'Bio', 'Bio.Seq', 'Bio.Alphabet', 'pyBigWig', 'tables', 'pytables', 'future', 'past', 'past.builtins',
                'future.utils', 'cooler', 'logging', 'unidecode', 'hic2cool', 'hicmatrix', 'hicmatrix.HiCMatrix',
                'hicmatrix.lib', 'krbalancing', 'fit_nbinom']

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

autodoc_mock_imports = MOCK_MODULES
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinxarg.ext'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'HiCExplorer'
copyright = u'2019, Fidel Ramírez, Bjoern Gruening, Vivek Bhardwaj, Joachim Wolff, Leily Rabbani'
author = u'Fidel Ramírez, Bjoern Gruening, Vivek Bhardwaj, Joachim Wolff, Leily Rabbani'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#


def get_version():
    import re
    try:
        f = open("../hicexplorer/_version.py")
    except EnvironmentError:
        return None
    for line in f.readlines():
        mo = re.match("__version__ = '([^']+)'", line)
        if mo:
            ver = mo.group(1)
            return ver
    return None


version = get_version()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
