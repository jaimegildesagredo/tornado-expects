# -*- coding: utf-8 -*-

import tornado.httpclient

from expects import expect
from expects.testing import failure
from tornado_expects import be_json

with describe('be_json'):
    with it("passes if response content type is 'application/json'"):
        expect(response(content_type='application/json')).to(be_json)

    with it("passes if response content type is 'application/json; charset=utf-8'"):
        expect(response(content_type='application/json; charset=utf-8')).to(be_json)

    with it('fails if response content type is text/xml'):
        with failure:
            expect(response(content_type='text/xml')).to(be_json)


def response(content_type):
    return tornado.httpclient.HTTPResponse(
        tornado.httpclient.HTTPRequest('foo'),
        200,
        headers={'Content-Type': content_type})
