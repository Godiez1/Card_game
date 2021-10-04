
class Player:

    initial_money = 0

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = Player.initial_money
        self.had_bet = 0

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    @property
    def value(self):
        return self.calculate_val()

    @value.getter
    def calculate_val(self):
        s = 0
        for card in self.hand:
            val = card.split()[0]
            if val == 'Ace':
                s += 1
            elif val in ('King', 'Queen', 'Jack', 'King'):
                s += 10
            else:
                s += int(val)
        return s

    @classmethod
    def set_player_money(cls, money):
        cls.initial_money = money

    def draw(self, deck, more=False):
        tmp = deck.pop()
        self.hand.append(tmp)
        if more:
            print(f'{self} has Draw {tmp}')

    def show_hand(self):
        print(f'{self.name} had {self.hand}')
        print(f'value = {self.value}')

    def show_unblined_card(self):
        print(f'{self}:')
        print(f'have: {self.hand[0]}')


class Black_Jack_player(Player):
    
    def __init__(self, name):
        super().__init__(name)
        self.money = Black_Jack_player.initial_money

    @property
    def value(self):
        return self.calculate_val()

    @value.getter
    def calculate_val(self):
        s = ace_count = 0
        for card in self.hand:
            val = card.split()[0]
            if val == 'Ace':
                ace_count += 1
            elif val in ('King', 'Queen', 'Jack', 'King'):
                s += 10
            else:
                s += int(val)

        while ace_count:
            if s + 11 <= 23:
                s += 11
            else:
                s += 1
            ace_count -= 1

        return s
