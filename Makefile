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

# start dev server for french version
serve:
	sphinx-autobuild "$(SOURCEDIR)" /tmp/doc-fr $(SPHINXOPTS) -D language=fr $(O) --ignore ./source/cli/cli_commands.rstinc --ignore ./source/reference --ignore ./source/_build --watch ./locale --port 8080

# start dev server for english version
serve-en:
	sphinx-autobuild "$(SOURCEDIR)" /tmp/doc-en $(SPHINXOPTS) -D language=en $(O) --ignore ./source/cli/cli_commands.rstinc --ignore ./source/reference --ignore ./source/_build --watch ./locale --port 8081

# extract translatable strings
update-translation: gettext
	sphinx-intl update -w 0 -p _build/gettext --no-obsolete -l en

# translate translatable strings using ollama
translate: update-translation
	python3 translate/translate.py ./locale/en

# update daemon api description (cannot be compiled by readthedocs)
update-api-description:
	mkdir -p ./source/_protobuf
	buf build -o ./source/_protobuf/daemon_descriptor.pb ./protobuf

# update api reference section from protobuf repository
reference: update-api-description
	python3 ./_scripts/generate_reference.py ./source/_protobuf/daemon_descriptor.pb ./source/reference
