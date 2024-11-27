# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

serve: export BANNER_MESSAGE=🚧 Documentation en cours de rédaction! 🚧
serve:
	sphinx-autobuild "$(SOURCEDIR)" /tmp/doc-fr $(SPHINXOPTS) -D language=fr $(O) --ignore ./source/cli/cli_commands.rstinc --watch ./locale --port 8080

serve-en: export BANNER_MESSAGE=🚧 Documentation Under Construction! 🚧
serve-en:
	sphinx-autobuild "$(SOURCEDIR)" /tmp/doc-en $(SPHINXOPTS) -D language=en $(O) --ignore ./source/cli/cli_commands.rstinc --watch ./locale --port 8081

update-translation: gettext
	sphinx-intl update -w 0 -p _build/gettext --no-obsolete -l en
