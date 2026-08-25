# rachis project news source

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

## Development instructions

The following sub-sections illustrate how to develop this documentation.

### Create the development environment

To build this documentation locally for development purposes, first create your development environment.

```
cd news.rachis.org
conda env create -n news.rachis.org --file environment-files/readthedocs.yml
conda activate news.rachis.org
q2doc refresh-cache
```

### Build the book

Next, build the book:

```
make html
```

### Serve the book locally

Finally, run the following to serve the built documentation locally:

```
make serve
```

### Live preview during development

Alternatively, run the following to serve the book with live reload, so edits to source files appear in the browser without rebuilding:

```
make live
```

This uses `jupyter book start`, which serves the site at http://localhost:3000 by default.
Note that this serves through the live MyST theme, so run `make html` for a final check before publishing.

Have fun! 🍇
