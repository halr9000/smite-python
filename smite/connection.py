"""
MIT License

Copyright (c) 2016 Jayden Bailey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from . import __version__ as version

import sys
import hashlib
import datetime
import requests


class HTTPClient:

    """
    Represents HTTP requests being sent to the Smite API

    Parameters
    ----------
    smite : :class:Client
        An initialized Client class
    """

    def __init__(self, smite):
        self.smite = smite
        self._session = None

        ua = "smite-python {0} (https://github.com/jaydenkieran/smite-python) Python/{1[0]}.{1[1]}"
        self.user_agent = ua.format(version, sys.version_info)

        self.base = 'http://api.smitegame.com/smiteapi.svc/'

    def create_session(self):
        """
        Creates a new Smite API session
        """
        url = self.build_request_url('createsession', require_session=False)
        r = self.make_request(url, require_session=False)
        return r

    def test_session(self):
        """
        Tests cached session against the Smite API
        """
        url = self.build_request_url('testsession', require_test=False)
        r = self.make_request(url, require_test=False)
        return "successful" in r

    def make_request(self, url, method='GET', require_session=True, require_test=True):
        """
        Makes a request to the Smite API

        Parameters
        ----------
        url : str
            Request URL
        method : str
            [Optional] Method to use
        require_session : bool
            [Optional] Indicates whether an active session is required
        """
        if require_session:
            if not self._session:
                self._session = self.create_session()
            if require_test:
                if not self.test_session():
                    self._session = self.create_session()

        if method == 'GET':
            r = requests.get(url)
            if r.status_code != 200:
                print("not 200")  # TODO: exception here
            if 'application/json' in r.headers['content-type']:
                return r.json()
            else:
                return r.text()

    def create_signature(self, endpoint):
        """
        Creates a new MD5 hashed signature

        Parameters
        ----------
        endpoint : str
            The endpoint to create a signature for
        """
        dt = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return hashlib.md5(self.smite.dev_id.encode('utf-8') + endpoint.encode(
            'utf-8') + self.smite.auth_key.encode('utf-8') + dt.encode('utf-8')).hexdigest()

    def build_request_url(self, endpoint, params=(), require_session=True, require_test=True):
        """
        Build a Smite API request URL

        Parameters
        ----------
        endpoint : str
            The endpoint to create a request URL for
        params : list
            [Optional] Parameters to provide in the URL
        require_session : bool
            [Optional] Indicates whether an active session is required
        """
        if require_session:
            if not self._session:
                self._session = self.create_session()
            if require_test:
                if not self.test_session():
                    self._session = self.create_session()

        signature = self.create_signature(endpoint)
        timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        if require_session:
            path = [endpoint + 'Json', self.smite.dev_id, signature, self._session.get('session_id'), timestamp]
        else:
            path = [endpoint + 'Json', self.smite.dev_id, signature, timestamp]
        if params:
            path += [str(param) for param in params]
        return self.base + '/'.join(path)
