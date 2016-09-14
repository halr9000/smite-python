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

from .ability import Ability, BasicAttack


class God:

    """
    Represents a Smite god

    Attributes
    ----------
    id : int
        The ID of the god
    name : str
        The name of the god
    title : str
        The title that the god has
    type : str
        The type of god it is
    rotation : bool
        Indicates if the god is on free rotation
    pantheon : str
        The pantheon that the god belongs to
    pros : str
        The advantages that the god has
    cons : str
        The disadvantages that the god has
    lore : str
        The in-game lore text for the god
    stats : :class:`GodStats`
        The stats that the god has
    abilities : list of :class:`Ability`
        The abilities that the god has
    basic_attack : :class:`BasicAttack`
        The basic attack that the god has
    god_card_url : str
        The URL for the god's card
    god_icon_url : str
        The URL for the god's icon

    Representation
    --------------
    name : str
        The name of the god
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('Name')
        self.title = kwargs.get('Title')
        self.type = kwargs.get('Type').strip()
        self.rotation = (kwargs.get('OnFreeRotation').lower() == 'true')
        self.pantheon = kwargs.get('Pantheon')
        self.pros = kwargs.get('Pros').strip()
        self.cons = kwargs.get('Cons').strip()
        self.lore = kwargs.get('Lore').strip()

        if 'magical' in self.type.lower():
            self.stats = MagicalGodStats(**kwargs)
        elif 'physical' in self.type.lower():
            self.stats = PhysicalGodStats(**kwargs)
        else:
            # If for some reason the god isn't either
            self.stats = GodStats(**kwargs)

        abilities = [kwargs.get('Ability_1'), kwargs.get('Ability_2'), kwargs.get(
            'Ability_3'), kwargs.get('Ability_4'), kwargs.get('Ability_5')]
        self.abilities = [Ability(**x) for x in abilities]

        self.basic_attack = BasicAttack(**kwargs)
        self.god_card_url = kwargs.get('godCard_URL')
        self.god_icon_url = kwargs.get('godIcon_URL')

    def __repr__(self):
        return self.name


class GodStats:

    """
    Represents a Smite god's stats

    Attributes
    ----------
    speed : int
        God's base speed
    mana : int
        God's base mana
    mana_per_five : int
        God's MP5
    mana_per_level : int
        God's mana per level
    health : int
        God's base health
    health_per_five : int
        God's HP5
    health_per_level : int
        God's health per level
    mana_per_five_per_level : int
        God's MP5 per level
    magical_proteection : int
        God's magical protection
    magical_protection_per_level : int
        God's magical protection per level
    physical_protection : int
        God's physical protection
    physical_protection_per_level : int
        God's physical protection per level
    attack_speed : int
        God's attack speed
    attack_speed_per_level : int
        God's attack speed per level
    """

    def __init__(self, **kwargs):
        self.speed = kwargs.get('Speed')
        self.mana = kwargs.get('Mana')
        self.mana_per_five = kwargs.get('ManaPerFive')
        self.mana_per_level = kwargs.get('ManaPerLevel')
        self.health = kwargs.get('Health')
        self.health_per_five = kwargs.get('HealthPerFive')
        self.health_per_level = kwargs.get('HealthPerLevel')
        self.mana_per_five_per_level = kwargs.get('MP5PerLevel')
        self.magical_protection = kwargs.get('MagicProtection')
        self.magical_protection_per_level = kwargs.get('MagicProtectionPerLevel')
        self.physical_protection = kwargs.get('PhysicalProtection')
        self.physical_protection_per_level = kwargs.get('PhysicalProtectionPerLevel')
        self.attack_speed = kwargs.get('AttackSpeed')
        self.attack_speed_per_level = kwargs.get('AttackSpeedPerLevel')


class PhysicalGodStats(GodStats):

    """
    Represents a physical Smite god's stats

    Inherits :class:`GodStats`

    Attributes
    ----------
    physical_power : int
        God's physical power
    physical_power_per_level : int
        God's physical power per level
    """

    def __init__(self, **kwargs):
        self.physical_power = kwargs.get('PhysicalPower')
        self.physical_power_per_level = kwargs.get('PhysicalPowerPerLevel')


class MagicalGodStats(GodStats):

    """
    Represents a magical Smite god's stats

    Inherits :class:`GodStats`

    Attributes
    ----------
    magical_power : int
        God's magical power
    magical_power_per_level : int
        God's magical power per level
    """

    def __init__(self, **kwargs):
        self.magical_power = kwargs.get('MagicalPower')
        self.magical_power_per_level = kwargs.get('MagicalPowerPerLevel')
