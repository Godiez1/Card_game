from Card import Card
from Player import BlackJackPlayer


# from rich.console import Console

# c = Console()


class ComputerPlayer(BlackJackPlayer):
    """create an computer player for black jack"""

    num = 0

    def __init__(self):
        super().__init__(self)
        ComputerPlayer.num += 1
        self.name = 'BOT' + str(ComputerPlayer.num)

    def draw_one_turn(self, game):
        """draw card until computer hand values more than 17"""
        while self.value <= 17:
            self.draw(game.deck.deck)
            if not self.check_if_hand_valid() or self.blackjack():
                break


class Game:
    """Entire game object"""

    def __init__(self, name_list: list[str]):
        self.Player_list = [BlackJackPlayer(name) for name in name_list]
        # create an player list
        self.dealer = ComputerPlayer()  # create an dealer player
        self.deck = Card()

    def deal_card(self):
        """deal card to all player"""
        for _ in range(2):
            self.dealer.draw(self.deck.deck)
            for player in self.now_player:
                player.draw(self.deck.deck)

    def show_every_player_card(self, show_len=False):
        """show every player card unblinded and show the length of it if show_len"""
        for player in self.now_player:
            player.show_unblined_card()
            if show_len:
                print(f'Have {len(player.hand)} Card')
            print()

    def draw_all_player(self):
        """Draw card to all payer"""
        self.show_every_player_card()
        self.dealer.show_unblined_card()
        print()

        for player in self.now_player:
            print(f"{player}'s Turn:")
            player.draw_one_turn(self)
            print()
        self.dealer.draw_one_turn(self)

    def finalize(self):
        """Finalize the game whether player get money or lose money"""
        print(f'Dealer hand are {self.dealer.hand}\nDealer Score are {self.dealer.value}\n')
        if not self.dealer.check_if_hand_valid():
            print('Dealer Burst:')
            for player in self.now_player:
                player.finalize(win=True)
        elif self.dealer.blackjack():
            print('Dealer Blackjack!')
            for player in self.now_player:
                if player.value != 21:
                    player.finalize(win=False)
                else:
                    player.finalize(win='Draw')
        else:
            for player in self.now_player:
                player.finalize(win=player.if_win(self.dealer))

    def call_all(self):
        """call all Player"""
        for player in self.now_player:
            player.call()

    def set_played(self):
        for player in self.Player_list:
            if player.money > 0:
                player.played = True
            else:
                player.played = False

    def play(self):
        """This Func Use to play one game"""
        self.set_played()
        self.call_all()
        self.deal_card()
        self.draw_all_player()
        self.show_every_player_card(show_len=True)
        self.finalize()
        self.set_played()

    @property
    def now_player(self):
        """return an player which not knock(money>=0)"""
        return [player for player in self.Player_list if player.played]

    def reset(self):
        self.deck.reset()
        self.dealer.reset()
        for player in self.Player_list:
            player.reset()

    def run(self):
        # c.print('welcome', style='blue on white')
        time = 0
        while len(self.now_player) > 1 or time == 0:
            time += 1
            print(f'round{time}:')
            self.play()
            self.reset()
            print('_____________________' * 2 + '\n')
        else:
            try:
                print(f'{self.now_player[0]} win')
            except IndexError:
                print('Dealer win')


def main():
    """main func"""
    money = float(input('Enter each player money: '))
    BlackJackPlayer.set_player_money(money)
    g = Game(['God', 'Tonwan'])
    g.run()


if __name__ == '__main__':
    main()


# TODO: main part at tmrw xD.
