My Personal Web Page, built with [Hyde](http://hyde.github.io/)

See the rendered version at http://http://www.as.utexas.edu/~kgulliks/

Building
========
Requires hyde:

    pip install hyde

Generate version for local development:

    make gen

Preview local version
(this is previewable in the browser at localhost:8080 -- Kill with ctrl-C)

    make serve

Generate site for production:

    make gen-production

Publish site via SSH (SSH publisher requires hyde version > 0.8.6):

    make publish

License
=======
This work is under a [BSD 2-clause license](http://opensource.org/licenses/BSD-2-Clause)

