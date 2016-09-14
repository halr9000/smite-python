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


class Skin:

    """
    Represents a Smite god's skin

    Attributes
    ----------
    name : str
        The name of the skin
    god_name : str
        The name of the god that owns the skin
    god_id : int
        The ID of the god that owns the skin
    obtainability : str
        The obtainability of the skin
    id_1 : int
        The ID of the skin (1)
    id_2 : int
        The ID of the skin (2)
    favor : int
        The favor price of the skin
    gems : int
        The gems price of the skin
    icon_url : str
        The URL to the icon for the skin
    card_url : str
        The URL to the card for the skin

    Representation
    --------------
    name : str
        The name of the skin
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('skin_name')
        self.god_name = kwargs.get('god_name')
        self.god_id = kwargs.get('god_id')
        self.obtainability = kwargs.get('obtainability')
        self.id_1 = kwargs.get('skin_id1')
        self.id_2 = kwargs.get('skin_id2')
        self.favor = kwargs.get('price_favor')
        self.gems = kwargs.get('price_gems')
        self.icon_url = kwargs.get('godIcon_URL')
        self.card_url = kwargs.get('godSkin_URL')

    def __repr__(self):
        return self.name
