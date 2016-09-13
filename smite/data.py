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

import datetime


class Data:

    """
    Represents the data usage limits for the Smite API

    Attributes
    ----------
    concurrent_limit : int
        The number of maximum concurrent sessions allowed
    request_limit : int
        The number of requests allowed daily
    sessions_today : int
        The number of sessions made today
    active_sessions : int
        The number of active sessions
    requests_today : int
        The number of requests made today
    session_limit : int
        The number of sessions allowed daily
    session_time_limit : datetime.timedelta
        The maximum amount of time per session
    """

    def __init__(self, **kwargs):
        self.concurrent_limit = kwargs.get('Concurrent_Sessions')
        self.request_limit = kwargs.get('Request_Limit_Daily')
        self.sessions_today = kwargs.get('Total_Sessions_Today')
        self.active_sessions = kwargs.get('Active_Sessions')
        self.requests_today = kwargs.get('Total_Requests_Today')
        self.session_limit = kwargs.get('Session_Cap')

        stl = datetime.timedelta(minutes=kwargs.get('Session_Time_Limit'))
        self.session_time_limit = stl
