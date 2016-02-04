Proof of concept
================

When haystack uses whoosh as a backend and indexes more than one model, using
SearchQuerySet.models return a value having less value than advertised in its
length.


Usage
-----

The bootstrap sets a Sqlite3 database with 2 models, and register 100 instance
of each with lorem ipsum.

    $ ./bootstrap

The expect runs a SearchQuerySet on a value occuring randomly in the models on
one model class. It shows the len() and the number of value in the iteration.


    $ ./venv/bin/python bin/poc expect
