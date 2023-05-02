import a2_support
from a2_support import *


class Card:
    """
    A class representing a card in the game

    Attributes:
        None
    """
    def __init__(self):
        """
        Initialize the class having only self attributes

        Return:
            nothing
        """
        pass

    def get_damage_amount(self) -> int:
        """
        It returns the damage done by the card to the target. By default, the damage done by it is zero.

        Returns:
            int: damage done ot the target
        """
        return 0

    def get_block(self) -> int:
        """
        It gives the amount of block this card add to its user. By default, the amount of block given by a card is zero.

        Returns:
            int: amount of block a card does to a user.
        """
        return 0

    def get_energy_cost(self) -> int:
        """
        Here this return the amount of energy this card cost to play. By default, it cost 1.

        Returns:
            int: amount of energy it cost to play
        """
        return 1

    def get_status_modifiers(self) -> dict[str, int]:
        """
        It describes the status of modifiers when card is played. No modifier is applied by default.

        Returns:
            dict [str, int]: Returns the dictionary with status
        """
        return {}

    def get_name(self) -> str:
        """
        Give out the name of the card

        Returns:
            str: Returns the name of card
        """
        return f'{type(self).__name__}'

    def get_description(self) -> str:
        """
        Gives the description of the card.

        Returns:
            str: return the description
        """
        return 'A card.'

    def requires_target(self) -> bool:
        """
        Check if the current card requires target. By default, it doesn't need any target.

        Returns:
            bool: gives true if it requires the target, otherwise False.
        """
        return True

    def __str__(self) -> str:
        return f"{self.get_name()}: {self.get_description()}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


class Strike(Card):
    """
    A card that deals 6 damage.

    Attributes:
        None
    """
    def get_damage_amount(self):
        return 6

    def get_description(self):
        return 'Deal 6 damage.'


class Defend(Card):
    """
    A card that gain 5 block.

    Attributes:
        None
    """
    def get_block(self) -> int:
        return 5

    def get_description(self):
        return 'Gain 5 block.'

    def requires_target(self):
        return False


class Bash(Card):
    """
    A card that deals 7 damage and gains 5 block with 2 energy cost.

    Attributes:
        None
    """
    def get_damage_amount(self):
        return 7

    def get_block(self):
        return 5

    def get_energy_cost(self):
        return 2

    def get_description(self):
        return 'Deal 7 damage. Gain 5 block.'


class Neutralize(Card):
    """
    A card that deals 3 damage and apply 1 weak and 2 vulnerable.

    Attributes:
        None
    """
    def get_damage_amount(self):
        return 3

    def get_energy_cost(self):
        return 0

    def get_status_modifiers(self):
        return {'weak': 1, 'vulnerable': 2}

    def get_description(self):
        return 'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.'


class Survivor(Card):
    """
    A card that gain 8 block without target and apply 1 strength.

    Attributes:
        None
    """

    def get_block(self):
        return 8

    def get_status_modifiers(self):
        return {'strength': 1}

    def requires_target(self):
        return False

    def get_description(self):
        return 'Gain 8 block and 1 strength.'


class Eruption(Card):
    """
    A card that deals 9 damage with 2 energy cost.

    Attributes:
        None
    """
    def get_damage_amount(self):
        return 9

    def get_energy_cost(self):
        return 2

    def get_description(self):
        return 'Deal 9 damage'


class Vigilance(Card):
    """
    A card that gain 8 block and apply 1 strength which cost 2 energy without any target.

    Attributes:
        None
    """
    def get_energy_cost(self):
        return 2

    def get_block(self):
        return 8

    def get_status_modifiers(self):
        return {'strength': 1}

    def requires_target(self):
        return False

    def get_description(self):
        return 'Gain 8 block and 1 strength'


class Entity:
    """
    Base class for inheritance.

    Attributes:
        max_hp (int): Maximum Health Point for this entity.
    """
    def __init__(self, max_hp: int) -> None:
        """
        Initializes a new Entity object with the specified maximum HP.

        Args:
            max_hp: Maximum health point.
        """
        self._max_hp = max_hp
        self.current_hp = max_hp
        self.block = 0
        self.weak = 0
        self.strength = 0
        self.vulnerable = 0

    def get_hp(self) -> int:
        """
        Gives current HP for this entity.

        Returns:
            int : returns out the current level of HP.
        """
        return self.current_hp if self.current_hp >= 0 else 0

    def get_max_hp(self) -> int:
        """
        Gives Maximum or the initial possible Health Point for the entity.

        Returns:
            int : return the initial possible HP of the entity.
        """
        return self._max_hp

    def get_block(self) -> int:
        """
        Gives the amount of block for this entity.

        Returns:
            int : return the amount of block.
        """
        return self.block

    def get_strength(self) -> int:
        """
        Gives the amount of strength for this entity.

        Returns:
            int : return the amount of strength.
        """
        return self.strength

    def get_weak(self) -> int:
        """
        Gives the amount of weak for this entity.

        Returns:
            int : return the amount of weak.
        """
        return self.weak

    def get_vulnerable(self) -> int:
        """
        Gives the amount of vulnerable for this entity.

        Returns:
            int : return the amount of vulnerable.
        """
        return self.vulnerable

    def get_name(self) -> str:
        """
        Gives the name of this entity.

        Returns:
            str : returns a string that is a name of particular class entity.
        """
        return f"{type(self).__name__}"

    def reduce_hp(self, amount: int) -> None:
        """
        Reduce the amount of HP including the amount of block(if block != 0).

        Args:
            amount: value that will impact the HP and block for this entity.

        Returns:
            None : returns nothing.
        """
        if self.block >= amount:
            self.block -= amount
        else:
            amount -= self.block
            self.block = 0
            self.current_hp -= amount

        self.current_hp = max(self.current_hp, 0)

    def is_defeated(self) -> bool:
        """
        Gives out the update on this entity if it is defeated.

        Returns:
            bools : returns true if this entity is defeated.
        """
        return True if self.current_hp <= 0 else False

    def add_block(self, amount: int) -> None:
        """
        Adds certain amount to block for this entity.

        Args:
            amount: value that should be added to the block of this entity.

        Returns:
            None: returns nothing.
        """
        self.block += amount
        return

    def add_strength(self, amount: int) -> None:
        """
        Adds certain amount to strength for this entity.

        Args:
            amount: value that should be added to the strength of this entity.

        Returns:
            None: returns nothing.
        """
        self.strength += amount
        return

    def add_weak(self, amount: int) -> None:
        """
        Adds certain amount to weak for this entity.

        Args:
            amount: value that should be added to weak of this entity.

        Returns:
            None: returns nothing.
        """
        self.weak += amount
        return

    def add_vulnerable(self, amount: int) -> None:
        """
        Adds certain amount to vulnerable for this entity.

        Args:
            amount: value that should be added to vulnerable of this entity.

        Returns:
            None: returns nothing.
        """
        self.vulnerable += amount
        return

    def new_turn(self) -> None:
        """
        Apply status change that occur when new turn begins which rolls back the block to 0,
        and weak, vulnerable reduced by 1 if not 0 before.

        Returns:
            None: returns nothing.
        """
        self.block = 0
        if self.weak != 0:
            self.weak -= 1
        if self.vulnerable != 0:
            self.vulnerable -= 1

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.current_hp}/{self._max_hp} HP"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._max_hp})"


class Player(Entity):
    """
    A Player is a type of entity that user control.

    Attributes:
        max_hp(int): The Maximum Health Point of Player
        cards(list[Card]): List of Card
    """
    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """
        Initialize a new Player object
        Args:
            max_hp: The Maximum Health Point of this Player
            cards: A list of Card
        """
        super().__init__(max_hp)
        self.energy = 3
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.cards = cards
        if self.cards is not None:
            self.deck = self.cards

    def get_energy(self) -> int:
        """
        Shows the current energy level of the user.

        Returns:
            int: Amount of Energy level.
        """
        return self.energy

    def get_hand(self) -> list[Card]:
        """
        Shows the current hand of the player.

        Returns:
            list[Card]: Returns the list of players current hand.
        """
        return self.hand

    def get_deck(self) -> list[Card]:
        """
        Shows the current deck of the player.

        Returns:
            list[Card]: Returns the list of players current deck.

        """
        return self.deck

    def get_discarded(self) -> list[Card]:
        """
        Shows the current discard pile of the player.

        Returns:
            list[Card]: Returns the list of players current discard pile.

        """
        return self.discard_pile

    def start_new_encounter(self) -> None:
        """
        Adds all cards from the player's discard pile to the end of their deck, and sets the discard pile to be
        an empty list. A pre-condition to this method is that the player's hand should be empty when it is called.

        Returns:
            None: return nothing
        """
        if len(self.hand) == 0:
            self.deck = self.deck + self.get_discarded()
            self.discard_pile = []
        return

    def end_turn(self) -> None:
        """
        Adds all remaining cards from the player's hand to the end of their discard pile, and sets their
        hand back to an empty list.

        Returns:
            None: return nothing
        """
        self.discard_pile = self.discard_pile + self.hand
        self.hand = []
        return

    def new_turn(self) -> None:
        """
        Sets the player up for a new turn. This involves everything that a regular entity requires for a new
        turn, but also requires that the player be dealt a new hand of 5 cards, and energy be reset to 3.

        Returns:
            None: return nothing
        """
        super().new_turn()
        self.energy = 3
        draw_cards(self.get_deck(), self.get_hand(), self.get_discarded())
        return

    def play_card(self, card_name: str) -> Card | None:
        """
        This checks if a player has a specific card in their hand and enough energy to play it.

        Returns:
            Card | None: return the Card class or return nothing
        """
        for card in self.hand:
            if card.get_name() == card_name and card.get_energy_cost() <= self.get_energy():
                self.hand.remove(card)
                self.discard_pile.append(card)
                self.energy -= card.get_energy_cost()
                return card
        return None

    def __repr__(self) -> str:
        if self.cards is None:
            return f"{type(self).__name__}({self._max_hp}, None)"
        else:
            return f"{type(self).__name__}({self._max_hp}, {self.cards})"


class IronClad(Player):
    """
    Type of Player with 80 HP and 5 Strike cards, 4 Defend cards, 1 Bash cards
    """
    def __init__(self):
        """
        Initialize Ironclad class with only self attribute

        Returns:
            None
        """
        super().__init__(80, [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Bash()])

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


class Silent(Player):
    """
    Type of Player with 70 HP and 5 Strike cards, 5 Defend cards, 1 Neutralize cards, 1 Survivor
    """
    def __init__(self):
        """
        Initialize Silent class with only self attribute

        Returns:
            None
        """
        super().__init__(70, [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Defend(), Neutralize(), Survivor()])

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


class Watcher(Player):
    """
    Type of Player with 72 HP and 4 Strike cards, 4 Defend cards, 1 Eruption card, 1 Vigilance card
    """
    def __init__(self):
        """
        Initialize Watcher class with only self attribute.

        Returns:
            None
        """
        super().__init__(72, [Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Eruption(), Vigilance()])

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


class Monster(Entity):
    """
    It is a type of entity that the user battles using encounter.

    Attributes:
        unique_id (class): ID for every monster created.
        max_hp (instance): Maximum Health Point for this type monster.
    """
    unique_id = 0

    def __init__(self, max_hp: int) -> None:
        """
        Initialize Monster class with certain Health Point.

        Args:
            max_hp: Maximum Health Point.
        """
        super().__init__(max_hp)
        self._id = Monster.unique_id
        Monster.unique_id += 1

    def get_id(self) -> int:
        """
        Gives Unique ID for every monster created.

        Returns:
            int : ID of the Monster
        """
        return self._id

    def action(self) -> dict[str, int]:
        """
        Performs the current action for this monster, and returns a dictionary.

        Returns:
            dict[str, int]: returns a dictionary describing the effects this monster's action to its target

        Raises:
            NotImplementedError: raise this error if only in the monster class
        """
        raise NotImplementedError


class Louse(Monster):
    """
    A type of Monster that attacks with a random amount of damage between 5 and 7 (inclusive).

    Attributes:
        max_hp (class): Maximum Health Point of Louse
        damage (instance): damage point
    """

    def __init__(self, max_hp: int) -> None:
        """
        Initialize the Class Louse with certain HP.

        Args:
            max_hp: Maximum Health Point
        """
        super().__init__(max_hp)
        self.damage = random_louse_amount()

    def action(self) -> dict[str, int]:
        """
        It simply returns a dictionary of {damage: amount}, where amount is an amount
        between 5 and 7 (inclusive).

        Returns:
            dict[str, int]: returns a dictionary describing the effects this monster's action to its target
        """
        return {'damage': self.damage}


class Cultist(Monster):
    """
    A type of Monster that attacks and weaken the player with some damage and weak.

    Attributes:
        max_hp (class): Maximum Health Point of Louse
        num_calls (instance): Cult monster call counter
        weak_amount (instance): Weak amount point
        damage_amount (instance): damage amount point
    """

    def __init__(self, max_hp: int) -> None:
        """
        Initialize the Class Cultist with certain HP.

        Args:
            max_hp: Maximum Health Point
        """
        super().__init__(max_hp)
        self.num_calls = 0
        self.weak_amount = 0
        self.damage_amount = 0

    def action(self) -> dict[str, int]:
        """
        The Cultist's action method returns a dictionary containing 'damage' and 'weak' keys.
        The 'damage' value increases by 6 + _num_calls with each call, while the 'weak' value alternates between 0 and 1

        Returns:
            dict[str, int]: returns a dictionary describing the effects this monster's action to its target
        """
        if self.num_calls == 0:
            self.num_calls += 1
            return {'damage': self.damage_amount, 'weak': self.weak_amount}
        elif self.num_calls == 1:
            self.damage_amount += (6 + self.num_calls)
            self.weak_amount = 1 - self.weak_amount
            self.num_calls += 1
            return {'damage': self.damage_amount, 'weak': self.weak_amount}
        else:
            self.damage_amount += 1
            self.weak_amount = 1 - self.weak_amount
            self.num_calls += 1
            return {'damage': self.damage_amount, 'weak': self.weak_amount}


class JawWorm(Monster):
    """
    A subclass of Monster representing a Jaw Worm enemy in a game.

    """

    def action(self) -> dict[str, int]:
        """
        Performs action for this JawWorm, and returns a dictionary.

        Returns:
            dict[str, int]: returns a dictionary describing the effects this JawWorm's action to its target.
        """
        damage_taken = self.get_max_hp() - self.get_hp()
        block_amount = (damage_taken + 1) // 2
        damage_amount = damage_taken // 2
        self.block += block_amount
        return {'damage': damage_amount}


class Encounter:
    """
    This class manages one player and a set of 1 to 3 monsters, and facilitates the interactions between them.

    Attributes:
        player (instance): Player instance where user control.
        monsters (instance): list of tuples describing type of the monster with max HP.
    """

    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        Initialize an Encounter instance with a player and list of monster.

        Args:
            player: Player instance where user control.
            monsters: list of tuples describing type of the monster with max HP
        """
        self.player = player
        self.monsters = [globals()[name](amount) for name, amount in monsters]
        self.player.start_new_encounter()
        self.start_new_turn()

    def start_new_turn(self) -> None:
        """
        Sets to be the player instance and start new turn.

        Returns:
            None: Return Nothing
        """
        self.player.new_turn()

    def end_player_turn(self) -> None:
        """
        Sets it to not be the player's turn and end turn.

        Returns:
            None: return nothing.
        """
        self.player.end_turn()
        for monster in self.monsters:
            monster.new_turn()

    def get_player(self) -> Player:
        """
        Shows the player in this encounter.

        Returns:
            Player: Return Player in encounter.
        """
        return self.player

    def get_monsters(self) -> list[Monster]:
        """
        Shows the monster in this encounter.

        Returns:
            list[Monster]: Returns list of monster.
        """
        return self.monsters

    def is_active(self) -> bool:
        """
        Checks if there is any monster in this encounter.

        Returns:
            bool: Return true if there is any monster left else false.
        """
        return len(self.monsters) > 0

    def player_apply_card(self, card_name: str, target_id: int | None = None) -> bool:
        """
         It attempts to apply the first card with the given name from the player's hand.

        Args:
            card_name: name of the card in player's hand.
            target_id: It specifies the target for the card.

        Returns:
            bool: Return True if player attempt to play was satisfied by the criteria.
        """
        try:
            target_monster = next((monster for monster in self.monsters if monster.get_id() == target_id), None)
            if not self.player.get_hand():
                return False
            elif globals()[card_name]().requires_target() and target_monster is None:
                return False

            card_checker = self.player.play_card(card_name)
            if card_checker is None:
                return False
            else:
                card = card_checker
                strength_value = card.get_status_modifiers().get('strength', 0)
                self.player.add_block(card.get_block())
                self.player.add_strength(strength_value)

                weak_value = card.get_status_modifiers().get('weak', 0)
                vulnerable_value = card.get_status_modifiers().get('vulnerable', 0)
                if target_monster is not None:
                    target_monster.add_weak(weak_value)
                    target_monster.add_vulnerable(vulnerable_value)

                    damage = card.get_damage_amount() + self.get_player().get_strength()
                    if target_monster.get_vulnerable() > 0:
                        damage *= 1.5
                    elif self.player.get_weak() > 0:
                        damage *= 0.75

                    final_damage = int(damage)
                    target_monster.reduce_hp(final_damage)

                    if target_monster.is_defeated():
                        self.monsters.remove(target_monster)
                return True
        except KeyError:
            return False

    def enemy_turn(self) -> None:
        """
        It attempts to allow all remaining monsters in the encounter to take an action.

        Returns:
            None
        """
        if not self.monsters or bool(self.player.get_hand()):
            return

        if not self.player.get_hand():
            for monster in self.monsters:
                action_dict = monster.action()
                self.player.add_weak(action_dict.get('weak', 0))
                self.player.add_vulnerable(action_dict.get('vulnerable', 0))

                monster.add_strength(action_dict.get('strength', 0))
                monster_strength = monster.get_strength()

                damage = action_dict.get('damage', 0) + monster_strength
                if self.player.get_vulnerable() > 0:
                    damage *= 1.5
                elif monster.get_weak() > 0:
                    damage *= 0.75
                self.player.reduce_hp(int(damage))

            self.start_new_turn()
            return


def main():

    player_type = input("Enter a player type: ")
    player = ''
    if player_type.lower().strip() == "ironclad":
        player = IronClad()
    elif player_type.lower().strip() == "silent":
        player = Silent()
    elif player_type.lower().strip() == "watcher":
        player = Watcher()

    file_name = input("Enter a game file: ")
    encounters = a2_support.read_game_file(file_name)

    for encounter in encounters:
        print("New encounter!\n")
        x = Encounter(player, encounter)
        a2_support.display_encounter(x)

        while x.is_active():

            move = input("Enter a move: ").strip()

            if move == "end turn":
                x.end_player_turn()
                x.enemy_turn()
                if x.get_player().is_defeated():
                    return print(f'{a2_support.GAME_LOSE_MESSAGE}')
                else:
                    a2_support.display_encounter(x)

            elif move.startswith("inspect"):
                _, pile_type = move.split()
                if pile_type.lower() == "deck":
                    print(f'\n{x.get_player().get_deck()}\n')

                elif pile_type.lower() == "discard":
                    print(f'\n{x.get_player().get_discarded()}\n')

            elif move.startswith("play"):
                if len(move.split()) == 2:
                    _, card_name = move.split()
                    target_id = None
                else:
                    _, card_name, target_id = move.split()
                    target_id = int(target_id)
                if x.player_apply_card(card_name, target_id):
                    a2_support.display_encounter(x)
                else:
                    print(a2_support.CARD_FAILURE_MESSAGE)

            elif move.startswith('describe'):
                _, card_name = move.split()
                print(f'\n{globals()[card_name]().get_description()}\n')

        print(a2_support.ENCOUNTER_WIN_MESSAGE)

    return print(a2_support.GAME_WIN_MESSAGE)


if __name__ == '__main__':
    main()
