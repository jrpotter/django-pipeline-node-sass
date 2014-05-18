Django Pipeline Node Sass
=========================
[VERSION 1.0.0 - 05/18/2014]

django-pipeline-node-sass is a compiler for [django-pipeline](https://github.com/cyberdelia/django-pipeline). 

Installation
------------

```bash
$ pip install django-pipeline-node-sass
$ pip install git+https://github.com/jrpotter/django-pipeline-node-sass.git
```

Usage
-----

```python
# settings.py

# Default: '/usr/bin/env node-sass'
PIPELINE_NODE_SASS_BINARY = '...'

# Default: '--output-style compressed'
PIPELINE_NODE_SASS_ARGUMENTS = '...'

PIPELINE_COMPILERS = (
    'pipeline_node_sass.comiplers.NodeSassCompiler',
)
```
