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


class Player:

    """
    Represents a basic Smite player

    Attributes
    ----------
    name : str
        The name of the player
    id : int
        THe ID of the player

    Representation
    --------------
    name : str
        The name of the player
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('Name')
        self.id = kwargs.get('Id')

        # Cater for other raw API calls that only return name and ID
        if self.name is None:
            self.name = kwargs.get('name')
        if self.id is None:
            self.id = kwargs.get('player_id')

    def __repr__(self):
        return self.name


class PlayerInfo(Player):

    """
    Represents a Smite player with additional information

    This class is a subclass of :class:`Player`

    Attributes
    ----------
    status : str
        The player's personal status message
    region : str
        The player's region
    team_id : int
        The player's clan ID. Could be None
    team_name : str
        The player's clan name. Could be None
    avatar_url : str
        The URL to the player's avatar
    achievements : int
        The total amount of achievements a player has
    worshippers : int
        The total amount of worshippers a player has
    level : int
        The level of the player
    leaves : int
        The amount of times the player left a game
    losses : int
        The amount of times the player lost a game
    wins : int
        The amount of times the player won a game
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = kwargs.get('Personal_Status_Message')
        self.region = kwargs.get('Region')
        self.team_id = kwargs.get('TeamId')
        self.team_name = kwargs.get('Team_Name')
        self.avatar_url = kwargs.get('Avatar_URL')
        self.achievements = kwargs.get('Total_Achievements')  # TODO: fetch achivements and return achievement object
        self.worshippers = kwargs.get('Total_Worshippers')
        self.mastery = kwargs.get('MasteryLevel')
        self.level = kwargs.get('Level')
        self.leaves = kwargs.get('Leaves')
        self.losses = kwargs.get('Losses')
        self.wins = kwargs.get('Wins')
