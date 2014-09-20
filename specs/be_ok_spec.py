# -*- coding: utf-8 -*-

import tornado.httpclient

from expects import expect
from expects.testing import failure
from tornado_expects import be_ok

with describe('be_ok'):
    with it('passes if response status code is 200'):
        expect(response(status=200)).to(be_ok)

    with it('passes if response status code is 304'):
        expect(response(status=304)).to(be_ok)

    with it('fails if response status code is 400'):
        with failure:
            expect(response(status=400)).to(be_ok)


def response(status):
    return tornado.httpclient.HTTPResponse(
        tornado.httpclient.HTTPRequest('foo'),
        status)
