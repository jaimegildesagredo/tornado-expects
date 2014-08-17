===============
Tornado Expects
===============

.. image:: https://img.shields.io/pypi/v/tornado-expects.svg
    :target: https://pypi.python.org/pypi/tornado-expects
    :alt: Latest version

.. image:: https://img.shields.io/pypi/dm/tornado-expects.svg
    :target: https://pypi.python.org/pypi/tornado-expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/tornado-expects.svg?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/tornado-expects

Tornado-Expects is a matchers library for the `Expects <https://github.com/jaimegildesagredo/expects>`_ assertion library. It provides matchers for the `Tornado web framework <https://pypi.python.org/pypi/tornado>`_ request and response objects.

Installation
============

You can install the last stable release from PyPI using *pip* or *easy_install*.

.. code-block:: bash

    $ pip install tornado-expects

Also you can install the latest sources from *Github*.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/tornado-expects.git#egg=tornado-expects

Usage
=====

Just import the ``expect`` callable and the Tornado-Expects matchers and start writing assertions for test doubles.

.. code-block:: python

    from expects import expect
    from tornado_expects import *
    from tornado.httpclient import HTTPClient

    response = http_client.fetch('https://example.com')

    expect(response).to(be_ok)

Matchers
========

be_ok
-----

.. code-block:: python

    expect(response).to(be_ok)
    expect(response).not_to(be_ok)

be_json
-------

.. code-block:: python

    expect(response).to(be_json)
    expect(response).not_to(be_json)


have_header
-----------

.. code-block:: python

    expect(response).to(have_header('Content-Type'))
    expect(response).to(have_header('Content-Type', 'text/xml'))
    expect(response).to(have_header('Content-Type', start_with('text/xml')))
    expect(response).not_to(have_header('ETag'))

have_headers
------------

.. code-block:: python

    expect(response).to(have_headers('Content-Type', 'Content-Length'))
    expect(response).to(have_headers({'Content-Type': 'text/html'}))
    expect(response).not_to(have_headers('Etag', 'Authorization'))

have_status
-----------

.. code-block:: python

    expect(response).to(have_status(304))
    expect(response).not_to(have_status(500))

Specs
=====

To run the specs you should install the testing requirements and then run ``mamba``.

.. code-block:: bash

    $ python setup.py develop
    $ pip install -r test-requirements.txt
    $ mamba

License
=======

The Tornado-Expects is released under the `Apache2 license <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
