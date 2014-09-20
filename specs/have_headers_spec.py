# -*- coding: utf-8 -*-

import tornado.httpclient

from expects import expect
from expects.testing import failure
from tornado_expects import have_headers

A_HEADER_KEY = 'a header key'
A_HEADER_VALUE = 'a header value'
ANOTHER_HEADER_KEY = 'another header key'
ANOTHER_HEADER_VALUE = 'another header value'
NON_EXISTING_HEADER_KEY = 'non existing header key'

with describe('have_headers'):
    with before.each:
        self.response = response(headers={
            A_HEADER_KEY: A_HEADER_VALUE,
            ANOTHER_HEADER_KEY: ANOTHER_HEADER_VALUE
        })

    with it('passes if response has header'):
        expect(self.response).to(have_headers(A_HEADER_KEY))

    with it('passes if response has headers'):
        expect(self.response).to(have_headers({
            A_HEADER_KEY: A_HEADER_VALUE,
            ANOTHER_HEADER_KEY: ANOTHER_HEADER_VALUE
        }))

    with it('fails if response has not header'):
        with failure:
            expect(self.response).to(have_headers(NON_EXISTING_HEADER_KEY))


def response(headers):
    return tornado.httpclient.HTTPResponse(
        tornado.httpclient.HTTPRequest('foo'),
        200,
        headers=headers)
