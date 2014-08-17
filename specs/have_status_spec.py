# -*- coding: utf-8 -*-

import tornado.httpclient

from expects import expect
from expects.testing import failure
from tornado_expects import have_status

with describe('have_status'):
    with it('passes if response status code is 200'):
        expect(response(status=200)).to(have_status(200))

    with it('passes if response status code is 304'):
        expect(response(status=304)).to(have_status(304))

    with it('fails if response status code is not 200'):
        with failure(''):
            expect(response(status=301)).to(have_status(200))


def response(status):
    return tornado.httpclient.HTTPResponse(
        tornado.httpclient.HTTPRequest('foo'),
        status)
