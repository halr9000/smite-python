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


class BasicAttack:
    """
    Represents a Smite basic attack

    Attributes
    ----------
    damage : str
        The damage that each basic attack does
    progression : str
        The progression tree for the basic attack. Could be None
    """

    def __init__(self, **kwargs):
        self.damage = None
        self.progression = None

        description = kwargs.get('basicAttack')['itemDescription']
        for i in description['menuitems']:
            if 'damage' in i['description'].lower():
                self.damage = i['value']
            elif 'progression' in i['description'].lower():
                if i['value'].lower() != 'None':
                    self.progression = i['value']


class Ability:

    """
    Represents a Smite ability

    Attributes
    ----------
    id : int
        The ID of the ability
    name : str
        The name of the ability
    icon_url : str
        The URL to the image of the ability's icon
    passive : bool
        Indicates if the ability is a passive ability
    cooldown : str
        The cooldown for the ability. Could be empty
    cost : str
        The cost of the ability. Could be empty
    description : str
        The description of the ability
    affects : str
        The entity that the ability affects. Could be None
    damage : str
        The type of damage that the ability does. Could be None
    damage_per_tick : str
        The damage per tick that the ability does. Could be None
    type : str
        The type of ability it is. Could be None
    radius : str
        The radius the ability has. Could be None

    Representation
    --------------
    name : str
        The name of the ability
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('Id')
        self.name = kwargs.get('Summary')
        self.icon_url = kwargs.get('URL')

        description = kwargs.get('Description')['itemDescription']

        if not description['cooldown'] and not description['cost']:
            # Assume that the ability is a passive one
            self.passive = True
        else:
            self.passive = False

        self.cooldown = description['cooldown']
        self.cost = description['cost']
        self.description = description['description']

        self.affects = None
        self.damage = None
        self.damage_per_tick = None
        self.type = None
        self.radius = None

        for i in description['menuitems']:
            if 'affects' in i['description'].lower():
                self.affects = i['value']
            elif 'damage' in i['description'].lower():
                self.damage = i['value']
            elif 'ability' in i['description'].lower():
                self.type = i['value']
            elif 'radius' in i['description'].lower():
                self.radius = i['value']

        for i in description['rankitems']:
            if 'damage per tick' in i['description'].lower():
                self.damage_per_tick = i['value']

    def __repr__(self):
        return self.name
