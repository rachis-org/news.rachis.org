# helpers
_copy-env-file:
	cp environment-files/readthedocs.yml blog/_static/environment.yml

_copy-data:
	@if [ -d "blog/data/" ]; then \
		cp -r blog/data/ blog/_build/html/data/; \
		echo "Copied data directory."; \
	else \
		echo "blog/data/ not found, skipping copy."; \
	fi

_build-html:
	cd blog && jupyter book build --html

_build-fast-preview:
	cd blog && Q2DOC_FASTMODE= jupyter book build --html

_build-preview:
	cd blog && Q2DOC_PREVIEW= jupyter book build --html

# main targets

autodoc:
	q2doc autodoc --singlepage --plugin news.rachis.org --output plugin-reference blog


html: _copy-env-file _build-html _copy-data

fast-preview: _copy-env-file _build-fast-preview _copy-data

preview: _copy-env-file _build-preview _copy-data

serve:
	npx serve blog/_build/html/ -p 4000

clean:
	rm -rf blog/_build/html/