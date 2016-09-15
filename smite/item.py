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


class Item:

    """
    Represents a Smite god's item

    Attributes
    ----------
    name : str
        The name of the item
    id : int
        The ID of the item
    root_id : int
        The ID of the item that precedes this one
    tier : int
        The tier of the item
    starting : bool
        Indicates if the item is a starting item
    description : str
        The description of the item. Could be None
    icon_url : str
        The URL to the icon for the item
    icon_id : int
        The ID of the item's icon
    type : str
        The type of item

    Extra Attributes
    ----------------
    All of these attributes can return None

    secondary_description : str
    health : str
    mana : str
    physical_protection : str
    magical_protection : str
    physical_power : str
    magical_power : str
    attack_speed : str
    physical_penetration : str
    magical_penetration : str
    physical_lifesteal : str
    magical_lifesteal : str
    cooldown_reduction : str
    mp5 : str
    hp5 : str
    movement_speed : str
    crowd_control_reduction : str
    crit_chance : str
    unlocks_at : str

    Representation
    --------------
    name : str
        The name of the item
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('DeviceName')
        self.id = kwargs.get('ItemId')
        self.root_id = kwargs.get('RootItemId')
        self.tier = kwargs.get('ItemTier')
        self.starting = kwargs.get('StartingItem')
        self.description = kwargs.get('ItemDescription')['Description']

        if not self.description:
            self.description = kwargs.get('ShortDesc')
            if not self.description:
                self.description = None

        self.icon_url = kwargs.get('itemIcon_URL')
        self.icon_id = kwargs.get('IconId')
        self.type = kwargs.get('Type')

        self.secondary_description = None
        s = kwargs.get('ItemDescription')['SecondaryDescription']
        if s:
            self.secondary_description = s

        self.health = None
        self.mana = None
        self.physical_protection = None
        self.magical_protection = None
        self.physical_power = None
        self.magical_power = None
        self.attack_speed = None
        self.physical_penetration = None
        self.magical_penetration = None
        self.physical_lifesteal = None
        self.magical_lifesteal = None
        self.cooldown_reduction = None
        self.mp5 = None
        self.hp5 = None
        self.movement_speed = None
        self.crowd_control_reduction = None
        self.crit_chance = None
        self.unlocks_at = None

        mi = kwargs.get('ItemDescription')['Menuitems']
        for i in mi:
            d = i['Description'].lower()
            v = i['Value']
            if 'health' in d:
                self.health = v
            elif 'mana' in d:
                self.mana = v
            elif 'physical protection' in d:
                self.physical_protection = v
            elif 'magical protection' in d:
                self.magical_protection = v
            elif 'physical power' in d:
                self.physical_power = v
            elif 'magical power' in d:
                self.magical_power = v
            elif 'attack speed' in d:
                self.attack_speed = v
            elif 'physical penetration' in d:
                self.physical_penetration = v
            elif 'magical penetration' in d:
                self.magical_penetration = v
            elif 'physical lifesteal' in d:
                self.physical_lifesteal = v
            elif 'magical lifesteal' in d:
                self.magical_lifesteal = v
            elif 'cooldown reduction' in d:
                self.cooldown_reduction = v
            elif 'mp5' in d:
                self.mp5 = v
            elif 'hp5' in d:
                self.hp5 = v
            elif 'movement speed' in d:
                self.movement_speed = v
            elif 'crowd control reduction' in d:
                self.crowd_control_reduction = v
            elif 'critical strike chance' in d:
                self.crit_chance = v
            elif 'unlocks at' in d:
                self.unlocks_at = d.replace('unlocks at', '').strip()

    def __repr__(self):
        return self.name
