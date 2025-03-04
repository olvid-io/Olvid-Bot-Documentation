import os
from olvid import __version__ as olvid_version
from olvid import __docker_version__ as docker_version

project = 'Olvid Bots'
copyright = '2024, Olvid'
author = 'Olvid'
version = olvid_version
release = olvid_version

# -- General configuration ---------------------------------------------------

extensions = [
	"sphinx.ext.autodoc",  # document python classes and module automatically
	"sphinx.ext.todo",
	"sphinx_click",  # generate documentation for CLI
	"sphinx_design",  # add dropdown menus and panels
	"myst_parser",  # enable myst syntax (extended markdown)
	"sphinx.ext.napoleon",  # allows support for Google docstring format
	"sphinx_copybutton",  # add copy button to code blocks
	"sphinx_substitution_extensions",  # use substitutions in code blocks
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'
locale_dirs = ['../locale']
gettext_compact = False
# Show non-translated texts in red
# translation_progress_classes = "untranslated"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_static_path = ['_static']
html_logo = "_static/images/olvid-bots-horizontal.png"
html_favicon = "_static/images/olvid.png"
html_copy_source = True  # can be disabled

# -- Html Themes Options --------------------------------------------
html_css_files = [
	# custom css for book theme
	'css/book-theme.css',
	# necessary for font-awesome icons
	"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]
html_theme_options = {
	"collapse_navbar": True,
	"show_navbar_depth": 2,
	"show_toc_level": 2,
	# hide some buttons
	"use_download_button": False,
	"use_fullscreen_button": False,
	"show_prev_next": False,
	###########
	# repository settings
	"repository_url": os.getenv("REPOSITORY_URL", "https://github.com/olvid-io/Olvid-Bot-Documentation"),
	"use_repository_button": True,
	"use_source_button": True,
	"use_edit_page_button": True,
	"use_issues_button": True,
	"path_to_docs": "/source",
	"repository_branch": "main",
	###########
	# templates
	"article_header_start": [],  # remove toggle primary sidebar button
	# workaround: remove simple quote char added by readthedocs in env variables.
	"announcement": os.getenv("BANNER_MESSAGE", "🚧 Documentation Under Construction! 🚧").removeprefix("'").removesuffix("'")
}

# -- Extensions -----------------------------------------------------
# MySt configuration
myst_enable_extensions = ["colon_fence", "deflist", "substitution"]
myst_heading_anchors = 4

myst_substitutions = {
  "version": version,
  "docker_version": docker_version,
  "python_version": version,
}

# -- Custom scripts -------------------------------------------------
import subprocess
subprocess.run(["python3", "../_scripts/generate_cli_commands.py"],)
