import sys
import os

# patch sys.path to include olvid sources (used in dev olnly)
#sys.path.insert(0, os.path.abspath('../'))
#from olvid import __version__ as olvid_version


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Olvid Bots'
copyright = '2024, Olvid'
author = 'Olvid'
#version = olvid_version
#release = olvid_version
# TODO update
version = "1.1.0"
release = "1.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	"sphinx.ext.autodoc",  # document python classes and module automatically
	"sphinx.ext.todo",
	"sphinx_click",  # generate documentation for CLI
	"sphinx_design",  # add dropdown menus and panels
	"myst_parser",  # enable myst syntax (extended markdown)
	"sphinx.ext.napoleon",  # allows support for Google docstring format
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'
locale_dirs = ['locale']
gettext_compact = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
# html_theme = 'sphinx_rtd_theme'
# TODO re-enable
# html_title = olvid_version

html_static_path = ['_static']
html_logo = "_static/images/olvid-bots-horizontal.png"
html_favicon = "_static/images/olvid.png"
html_copy_source = True  # can be disabled

# -- Html Themes Options --------------------------------------------
# Book theme
if html_theme == "sphinx_book_theme":
	html_css_files = ['css/book-theme.css']
	templates_path = ["_templates"]
	html_theme_options = {
		"collapse_navbar": True,
		"show_navbar_depth": 2,
		"show_toc_level": 2,
		"announcement": "🚧 Documentation Under Construction! 🚧",
		# hide some buttons
		"use_download_button": False,
		"use_fullscreen_button": False,
		"show_prev_next": False,
		###########
		# repository settings
		"repository_url": os.getenv("REPOSITORY_URL", "https://github.com/olvid-io/Olvid-Bot-Quickstart"),
		"use_repository_button": True,
		"use_source_button": True,
		"use_issues_button": True,
		"path_to_docs": "/docs",
		"repository_branch": "main",
		###########
		# templates
		"article_header_start": [],  # remove toggle primary sidebar button
	}
# Read The Docs theme
elif html_theme == "sphinx_rtd_theme":
	html_css_files = ['css/rtd-theme.css']
	html_theme_options = {
		"prev_next_buttons_location": "None",
		"logo_only": True
	}

# -- Extensions -----------------------------------------------------
# MySt configuration
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 4

# -- Custom scripts -------------------------------------------------
import subprocess
subprocess.run(["python3", "_scripts/generate_cli_commands.py"],)
