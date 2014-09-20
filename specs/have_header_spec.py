# -*- coding: utf-8 -*-

import tornado.httpclient

from expects import expect
from expects.testing import failure
from tornado_expects import have_header

A_HEADER_KEY = 'a header key'
A_HEADER_VALUE = 'a header value'
ANOTHER_HEADER_KEY = 'another header key'

with describe('have_header'):
    with before.each:
        self.response = response(headers={A_HEADER_KEY: A_HEADER_VALUE})

    with it('passes if response has header'):
        expect(self.response).to(have_header(A_HEADER_KEY))

    with it('passes if response has header value'):
        expect(self.response).to(have_header(A_HEADER_KEY, A_HEADER_VALUE))

    with it('fails if response has not header'):
        with failure:
            expect(self.response).to(have_header(ANOTHER_HEADER_KEY))


def response(headers):
    return tornado.httpclient.HTTPResponse(
        tornado.httpclient.HTTPRequest('foo'),
        200,
        headers=headers)
