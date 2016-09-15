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

import re

from . import __version__ as version
from .connection import HTTPClient
from .data import Data
from .god import God
from .skin import Skin
from .error import NoResult
from .item import Item
from .player import Player, PlayerInfo


class Client:

    """
    Represents a connection to the Smite API

    Parameters
    ----------
    dev_id : str
        The private developer ID supplied by Hi-Rez Studios.
    auth_key : str
        The authorization key supplied by Hi-Rez Studios.
    lang : int
        [Optional] The language code to use for API queries.
    """

    def __init__(self, dev_id, auth_key, lang=1):
        self.dev_id = dev_id
        self.auth_key = auth_key
        self.lang = lang

        self.http = HTTPClient(self)

    def get_data_used(self):
        """
        Gets the daily usage limits of the Smite API

        Returns
        -------
        :class:`Data`
            The data usage limits
        """
        url = self.http.build_request_url('getdataused')
        r = self.http.make_request(url)
        return Data(**r[0])

    def get_gods(self):
        """
        Gets a list of all Smite gods and their various attributes

        Returns
        -------
        list of :class:`God`
            All Smite gods returned by the API
        """
        url = self.http.build_request_url('getgods', params=[self.lang])
        r = self.http.make_request(url)
        gods = [God(**x) for x in r]
        return gods

    def get_god_skins(self, god_id):
        """
        Gets a list of all of a god's available skins

        Parameters
        ----------
        god_id : int
            The ID of the god to query

        Returns
        -------
        list of :class:`Skin`
            All god skins returned by the API
        """
        url = self.http.build_request_url('getgodskins', params=[str(god_id), self.lang])
        r = self.http.make_request(url)
        skins = [Skin(**x) for x in r]
        return skins

    def get_god(self, god):
        """
        Gets a :class:`God` object based on given arguments

        Parameters
        ----------
        One of the two parameters below must be passed

        god : str or int
            The god to retrieve

        Returns
        -------
        :class:`God`
            The god requested

        Raises
        ------
        :class:`NoResult`
            No god was found with given arguments
        """
        gods = self.get_gods()
        for i in gods:
            if type(god) == str:
                if god and i.name.lower() == god.lower():
                    return i
            elif type(god) == int:
                if god and i.id == int(id):
                    return i
        raise NoResult("No god was found with given arguments")

    def get_items(self):
        """
        Gets a list of all Smite items and their various attributes

        Returns
        -------
        list of :class:`Item`
            All Smite items returned by the API
        """
        url = self.http.build_request_url('getitems', params=[self.lang])
        r = self.http.make_request(url)
        items = [Item(**x) for x in r]
        return items

    def get_item(self, item):
        """
        Gets a :class:`Item` object based on given arguments

        Parameters
        ----------
        One of the two parameters below must be passed

        item : str or int
            The item name or ID

        Returns
        -------
        :class:`Item`
            The Item requested

        Raises
        ------
        :class:`NoResult`
            No item was found with given arguments
        """
        items = self.get_items()
        for i in items:
            if type(item) == str:
                if item and i.name.lower() == item.lower():
                    return i
            elif type(item) == int:
                if item and i.id == int(id):
                    return i
        raise NoResult("No item was found with given arguments")

    def get_player(self, player):
        """
        Returns the :class:`PlayerInfo` object for a player

        Parameters
        ----------
        player : str or int
            The player to get the object for

        Returns
        -------
        :class:`PlayerInfo`
            The player

        Raises
        ------
        :class:`NoResult`
            No item was found with given arguments
        """
        url = self.http.build_request_url('getplayer', params=[player])
        r = self.http.make_request(url)
        return PlayerInfo(**r[0])

    def get_friends(self, user):
        """
        Returns the friends of a player

        Parameters
        ----------
        user : str or int or :class:`PlayerInfo`
            The player to check

        Returns
        -------
        list of :class:`Player`
            A list of the player's friend
        """
        if type(user) == PlayerInfo:
            # Remove brackets if user is in a clan
            user = re.sub("[\(\[].*?[\)\]]", "", user.name)
        print
        url = self.http.build_request_url('getfriends', params=[user])
        r = self.http.make_request(url)
        friends = [Player(**x) for x in r]
        return friends
