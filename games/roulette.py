import numpy as np
import ipdb
# American Roulette with 0 and 00.  Numbers are from 1:38.
# European Roulette with 0.  Numbers are from 1:37

# TAKE THIS SECTION OUT WHEN DONE TESTING~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~
#def play(game_name):
 #   game_name.single_play()
#~~~~~~~~~~~~~~~~~~~~~

class Roulette:
    def __init__(self, account_balance, num_of_games, play_type):
        self.account_balance = account_balance
        self.num_of_games = num_of_games
        self.play_type = play_type

    possible_outcomes = {
        1:['1', 'RED', 'ODD', '1 TO 18', '1 TO 12', '1ST 12'],
        2:['2', 'BLACK', 'EVEN', '1 TO 18', '1 TO 12', '2ND 12'],
        3:['3', 'RED', 'ODD', '1 TO 18', '1 TO 12', '3RD 12'],
        4:['4', 'BLACK', 'EVEN', '1 TO 18', '1 TO 12', '1ST 12'],
        5:['5', 'RED', 'ODD', '1 TO 18', '1 TO 12', '2ND 12'],
        6:['6', 'BLACK', 'EVEN', '1 TO 18', '1 TO 12', '3RD 12'],
        7:['7', 'RED', 'ODD', '1 TO 18', '1 TO 12', '1ST 12'],
        8:['8', 'BLACK', 'EVEN', '1 TO 18', '1 TO 12', '2ND 12'],
        9:['9', 'RED', 'ODD', '1 TO 18', '1 TO 12', '3RD 12'],
        10:['10', 'BLACK', 'EVEN', '1 TO 18', '1 TO 12', '1ST 12'],
        11:['11', 'BLACK', 'ODD', '1 TO 18', '1 TO 12', '2ND 12'],
        12:['12', 'RED', 'EVEN', '1 TO 18', '1 TO 12', '3RD 12'],
        13:['13', 'BLACK', 'ODD', '1 TO 18', '13 TO 24', '1ST 12'],
        14:['14', 'RED', 'EVEN', '1 TO 18', '13 TO 24', '2ND 12' ],
        15:['15', 'BLACK', 'ODD', '1 TO 18', '13 TO 24', '3RD 12'],
        16:['16', 'RED', 'EVEN', '1 TO 18', '13 TO 24', '1ST 12'],
        17:['17', 'BLACK', 'ODD', '1 TO 18', '13 TO 24', '2ND 12'],
        18:['18', 'RED', 'EVEN', '1 TO 18', '13 TO 24', '3RD 12'],
        19:['19', 'RED', 'ODD', '19 TO 36', '13 TO 24', '1ST 12'],
        20:['20', 'BLACK', 'EVEN', '19 TO 36', '13 TO 24', '2ND 12'],
        21:['21', 'RED', 'ODD', '19 TO 36', '13 TO 24', '3RD 12'],
        22:['22', 'BLACK', 'EVEN', '19 TO 36', '13 TO 24', '1ST 12'],
        23:['23', 'RED', 'ODD', '19 TO 36', '13 TO 24', '2ND 12'],
        24:['24', 'BLACK', 'EVEN', '19 TO 36', '13 TO 24', '3RD 12'],
        25:['25', 'RED', 'ODD', '19 TO 36', '25 TO 36', '1ST 12'],
        26:['26', 'BLACK', 'EVEN', '19 TO 36', '25 TO 36', '2ND 12'],
        27:['27', 'RED', 'ODD', '19 TO 36', '25 TO 36', '3RD 12'],
        28:['28', 'BLACK', 'EVEN', '19 TO 36', '25 TO 36', '1ST 12'],
        29:['29', 'BLACK', 'ODD', '19 TO 36', '25 TO 36', '2ND 12'],
        30:['30', 'RED', 'EVEN', '19 TO 36', '25 TO 36', '3RD 12'],
        31:['31', 'BLACK', 'ODD', '19 TO 36', '25 TO 36', '1ST 12'],
        32:['32', 'RED', 'EVEN', '19 TO 36', '25 TO 36', '2ND 12'],
        33:['33', 'BLACK', 'ODD', '19 TO 36', '25 TO 36', '3RD 12'],
        34:['34', 'RED', 'EVEN', '19 TO 36', '25 TO 36', '1ST 12'],
        35:['35', 'BLACK', 'ODD', '19 TO 36', '25 TO 36', '2ND 12'],
        36:['36', 'RED', 'EVEN', '19 TO 36', '25 TO 36', '3RD 12'],
        37:['0', 'GREEN', 'ZERO', 'ZERO', 'ZERO'],
        38:['D-00', 'GREEN', 'Double 0', 'Double 0', 'Double 0'],
    }

    payout_ratios = {
        # payout ratios are the ratio of what user is paid against a bet of $1
        '1': 35, '2': 35, '3': 35, '4': 35, '5': 35, '6': 35, '7': 35, 
        '8': 35, '9': 35, '10': 35, '11': 35, '12': 35, '12': 35, 
        '13': 35, '14': 35, '15': 35, '16': 35, '17': 35, '18': 35, 
        '19': 35, '20': 35, '21': 35, '22': 35,'23': 35, '24': 35,
        '25': 35, '26': 35, '27': 35, '28': 35, '29': 35, '30': 35,
        '31': 35, '32': 35, '33': 35, '34': 35, '35': 35, '36': 35,
        '0': 35, '00': 35, 'RED': 1, 'BLACK': 1, 'ODD': 1,
        'EVEN': 1, '1 TO 18': 1, '19 TO 36': 1, '1 TO 12': 2, '13 TO 24': 2,
        '25 TO 36': 2, '1ST 12': 2, '2ND 12': 2, '3RD 12': 2,
    }

    def single_play():
        number_of_games = input('WELCOME TO ROULETTE!! \n WE ARE READY TO TAKE YOUR MONEY!!!  \n \n HOW MANY GAMES WILL YOU BE PLAYING? ')
        account_balance = 1000
        for each_game in range(int(number_of_games)):
            bets = {}
            betting_phase = True
            while betting_phase == True:
                print('HERE ARE THE BETS YOU CAN MAKE:')
                for each_space, payout in Roulette.payout_ratios.items():
                    print(each_space + ' Pays ' + str(payout) + ' TO 1')
                bet_number_str = input('Where would you like to place your bet? ')
                bet_amount_int = input('How much would you like to bet? ') 
                bets[bet_number_str] = int(bet_amount_int)
                continue_betting = input('Would you like to place another bet? Y/N? ')
                if continue_betting.upper() == 'N':
                    betting_phase = False

            random_play = Roulette.possible_outcomes[np.random.randint(1, len(Roulette.possible_outcomes))]
            print(random_play[0], random_play[1])   
        
            profit_and_loss_this_turn = 0
            for bet_number, bet_amount in bets.items(): 
                if bet_number in random_play:
                    win_amount = Roulette.payout_ratios[bet_number] * bets[bet_number]
                    profit_and_loss_this_turn += win_amount
                else:
                    loss_amount = bets[bet_number]
                    profit_and_loss_this_turn -= loss_amount
            if profit_and_loss_this_turn > 0:
                print('YOU WON $' + str(profit_and_loss_this_turn) + '!!!')
            elif profit_and_loss_this_turn < 0:
                print('YOU LOST $' + str((-1 * profit_and_loss_this_turn)) + '.')
            else:
                print('ITS A BREAKEVEN PUSH!')
            account_balance += profit_and_loss_this_turn
            print('YOUR ACCOUNT BALANCE IS NOW $' + str(account_balance))
    
    
    def martingale(bets_placed = ['1 TO 12', '13 TO 24', '25 TO 36'], amplifier = 5, max_bet = 625, streak_trigger = 0):
        #amplifier is the amount that is multiplied by the previous bet.  Default martingale is
            #doubling each bet, this would be a multiplier of 2.  If 3 is set, it will multiply the 
            #previous bet by 3.  
        
        #max_bet is the maximum amount that can be bet on a given space.  Martingale will cap
            # at 128 by default.  

        #streak_trigger represents the amount of a loss streak that must occur in order for 
            # a bet to be placed.  
        streak = {}
        martingale_count = {}
        account_balance = 1000
        for each_bet in bets_placed:
                streak[each_bet] = 1
                martingale_count[each_bet] = 1  
        for each_run in range(1, 100):
            #ipdb.set_trace()
            random_play = Roulette.possible_outcomes[np.random.randint(1, len(Roulette.possible_outcomes))]
            for each_bet in bets_placed:
                if each_bet in random_play and streak[each_bet] > streak_trigger:
                    account_balance += martingale_count[each_bet] * Roulette.payout_ratios[each_bet]
                    streak[each_bet] = 1
                    martingale_count[each_bet] = 1
                    
                elif streak[each_bet] > streak_trigger and each_bet not in random_play:
                    account_balance -= martingale_count[each_bet]
                    if martingale_count[each_bet] >= max_bet:
                        martingale_count[each_bet] = 1
                    else:
                        martingale_count[each_bet] = martingale_count[each_bet] * amplifier
                    streak[each_bet] += 1

                elif streak[each_bet] <= streak_trigger:
                    streak[each_bet] += 1
        print(account_balance)

    def reverse_martingale(bets_placed = ['1 TO 12', '13 TO 24', '25 TO 36'], amplifier = 2, max_bet = 1000):
            #amplifier is the amount that is multiplied by the previous bet.  Default martingale is
                #doubling each bet, this would be a multiplier of 2.  If 3 is set, it will multiply the 
                #previous bet by 3.  
            
            #max_bet is the maximum amount that can be bet on a given space.  Martingale will cap
                # at 1000 by default.  

            martingale_count = {}
            account_balance = 1000
            for each_bet in bets_placed:
                    martingale_count[each_bet] = 1  
            for each_run in range(1, 100):
                ipdb.set_trace()
                random_play = Roulette.possible_outcomes[np.random.randint(1, len(Roulette.possible_outcomes))]
                for each_bet in bets_placed:
                    if each_bet in random_play:
                        account_balance += (martingale_count[each_bet] * Roulette.payout_ratios[each_bet])
                        martingale_count[each_bet] *= amplifier
                    else:
                        account_balance -= martingale_count[each_bet]
                        martingale_count[each_bet] = 1 
                    
            print(account_balance)
    
    def dual_martingale(bets_placed = ['1 TO 12', '13 TO 24', '25 TO 36'], amplifier = 2, max_bet = 900):
        #amplifier is the amount that is multiplied by the previous bet.  Default martingale is
            #doubling each bet, this would be a multiplier of 2.  If 3 is set, it will multiply the 
            #previous bet by 3.  
        
        #max_bet is the maximum amount that can be bet on a given space.  Martingale will cap
            # at 128 by default.  

        martingale_count = {}
        martingale_type = {} #tells whether current system is in a standard martingale, reverse
        #martingale, or dual martingale system.
        account_balance = 1000
        for each_bet in bets_placed:
                martingale_count[each_bet] = 1
                martingale_type[each_bet] = 'dual'  
        for each_run in range(1, 100):
            #ipdb.set_trace()
            random_play = Roulette.possible_outcomes[np.random.randint(1, len(Roulette.possible_outcomes))]
            for each_bet in bets_placed:
                if each_bet in random_play and martingale_type[each_bet] == 'standard':
                    account_balance += martingale_count[each_bet] * Roulette.payout_ratios[each_bet]
                    martingale_count[each_bet] = 1
                    martingale_type[each_bet] = 'dual'
                    
                elif each_bet not in random_play and martingale_type[each_bet] == 'standard':
                    account_balance -= martingale_count[each_bet]
                    if martingale_count[each_bet] == max_bet or martingale_count[each_bet] > max_bet:
                        martingale_count[each_bet] = 1
                        martingale_type[each_bet] = 'dual'
                    else:
                        martingale_count[each_bet] *= amplifier
                
                elif each_bet in random_play and martingale_type[each_bet] == 'reverse':
                    account_balance += martingale_count[each_bet] * Roulette.payout_ratios[each_bet]
                    if martingale_count[each_bet] == max_bet or martingale_count[each_bet] > max_bet:
                        martingale_count[each_bet] = 1
                        martingale_type[each_bet] = 'dual'
                    else:
                        martingale_count[each_bet] *= amplifier

                elif each_bet not in random_play and martingale_type[each_bet] == 'reverse':
                    account_balance -= martingale_count[each_bet]
                    martingale_count[each_bet] = 1
                    martingale_type[each_bet] = 'dual'

                elif each_bet in random_play and martingale_type[each_bet] == 'dual':
                    account_balance += martingale_count[each_bet] * Roulette.payout_ratios[each_bet]
                    martingale_count[each_bet] *= amplifier
                    martingale_type[each_bet] = 'reverse'
                
                elif each_bet not in random_play and martingale_type[each_bet] == 'dual':
                    account_balance -= martingale_count[each_bet]
                    martingale_count[each_bet] *= amplifier
                    martingale_type[each_bet] = 'standard'
   
        print(account_balance)


#~~~~~~~~~~~~~~~~~~
#play(Roulette)
#~~~~~~~~~~~~~~~~~~