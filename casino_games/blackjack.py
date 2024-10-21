# BLACKJACK
import random

game_title = "🃑 Blackjack"

            # 0         1         2      3      4
card_temp = ["┌───┐", "│   │", "| ", " │", "└───┘"]
cards = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "A", 10: "J", 10: "K", 10: "Q"}

status = ["                                                                           \n                                                                           \n     ██████           █████████████ ███████████████ ██████████████████     \n     ██████           █████████████ ███████████████ ██████████████████     \n     ██████           █████████████ ███████████████ ██████████████████     \n     ██████           ████     ████ ████            ████                   \n     ██████           ████     ████ ████            ████                   \n     ██████           ████     ████ ████            ████                   \n     ██████           ████     ████ ████            ██████████████████     \n     ██████           ████     ████ ███████████████ ██████████████████     \n     ██████           ████     ████ ███████████████ ██████████████████     \n     ██████           ████     ████ ███████████████ ████                   \n     ██████           ████     ████            ████ ████                   \n     ██████           ████     ████            ████ ████                   \n     ████████████████ ████     ████            ████ ████                   \n     ████████████████ █████████████ ███████████████ ██████████████████     \n     ████████████████ █████████████ ███████████████ ██████████████████     \n     ████████████████ █████████████ ███████████████ ██████████████████     \n                                                                           \n                                                                           \n",
          "                                                                           \n                                                                           \n        ██████     █████      ██████ ████████ █████████████████████        \n        ██████     █████      ██████ ████████ █████████████████████        \n        ██████     █████      ██████ ████████ █████████████████████        \n        ██████     █████      ██████ ████████ █████████████████████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ██████     █████      ██████ ████████ ███████       ███████        \n        ████████████████████████████ ████████ ███████       ███████        \n        ████████████████████████████ ████████ ███████       ███████        \n        ████████████████████████████ ████████ ███████       ███████        \n        ████████████████████████████ ████████ ███████       ███████        \n                                                                           \n                                                                           \n",
          "                                                                           \n      ████████████████████████████ ████████ █████████████████████████      \n      ████████████████████████████ ████████ █████████████████████████      \n      ████████████████████████████ ████████ █████████████████████████      \n      ████████████████████████████ ████████ █████████████████████████      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████                      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n               ██████████          ████████ █████████████████████████      \n                                                                           \n"]

header = "─" * ((75 - len(game_title)) // 2) + game_title + "─" * ((75 - len(game_title)) // 2)

def render_hand(player, active_terminal, hand, dealer_hand):
    hand_str = "═" * ((75 - 9) // 2) + "Your Hand" + "═" * ((75 - 9) // 2) +"\n"
    for i in range(0,4):
        hand_str += " " * ((75 - (len(hand) * 6)) // 2)
        for card in hand:
            if(i == 2):
                if(card[2] == False):
                    hand_str += card_temp[i] + card[1] + card_temp[i+1] + " "
                else:
                    hand_str += card_temp[i] + " " + card_temp[i+1] + " "
            elif(i == 3):
                hand_str += card_temp[i+1] + " "
            else:
                hand_str += card_temp[i] + " "
        hand_str += "\n"

    dealer_hand_str = "═" * ((75 - 13) // 2) + "Dealer's Hand" + "═" * ((75 - 13) // 2) +"\n"
    for i in range(0,4):
        dealer_hand_str += " " * ((75 - (len(dealer_hand) * 6)) // 2)
        for card in dealer_hand:
            if(i == 2):
                if(card[2] == False):
                    dealer_hand_str += card_temp[i] + card[1] + card_temp[i+1] + " "
                else:
                    dealer_hand_str += card_temp[i] + " " + card_temp[i+1] + " "
            elif(i == 3):
                dealer_hand_str += card_temp[i+1] + " "
            else:
                dealer_hand_str += card_temp[i] + " "
        dealer_hand_str += "\n"
    
    player.ss.update_quadrant(active_terminal, header + f"\n\n{dealer_hand_str} {"\n" * 5}{hand_str}")
    player.ss.print_screen()

def draw(player, dealer, hidden,score):
    card_value, card_type = random.choice(list(cards.items()))
    if(card_value == 11 and not dealer and score[0] + 11 > 21):
        card_value = 1
        card_type = "1"
    return [card_value, card_type, hidden]

def turn(player, active_terminal, turn):
    hand = []
    dealer_hand = []
    score = [0,0,0,0]

    input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\nPlayer {turn}: DRAW CARD")
    player.ss.overwrite("\r" + " " * 40)

    hand.append(draw(player, False, False, score))
    score[turn - 1] += hand[-1][0]
    hand.append(draw(player, False, False, score))
    score[turn - 1] += hand[-1][0]

    dealer_hand.append(draw(player, True, False, score))
    score[turn] += dealer_hand[-1][0]
    dealer_hand.append(draw(player, True, True, score))
    score[turn] += dealer_hand[-1][0]

    render_hand(player, active_terminal, hand, dealer_hand)

    if(score[turn - 1] == 21):
        dealer_hand[-1][-1] = False
        render_hand(player, active_terminal, hand, dealer_hand)
        if(score[turn] == 21):
            input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: STAND-OFF!")
            player.ss.overwrite("\r" + " " * 40)
            return "TIE"
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: YOU GOT A NATURAL!")
        player.ss.overwrite("\r" + " " * 40)
        return "WIN"
    elif(score[turn] == 21):
        dealer_hand[-1][-1] = False
        render_hand(player, active_terminal, hand, dealer_hand)
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: DEALER GOT A NATURAL!")
        player.ss.overwrite("\r" + " " * 40)
        return "BUST"

    while score[turn - 1] < 21:
        render_hand(player, active_terminal, hand, dealer_hand)
        choice = input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: You have {score[turn - 1]}. HIT? (y/N)")
        player.ss.overwrite("\r" + " " * 40)
        if(choice.lower() == "y"):
            input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: DRAW CARD")
            player.ss.overwrite("\r" + " " * 40)
            hand.append(draw(player, False, False, score))
            score[turn - 1] += hand[-1][0]
            render_hand(player, active_terminal, hand, dealer_hand)
        else: break
        if(score[turn - 1] > 21):
            input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: YOU BUST!")
            player.ss.overwrite("\r" + " " * 40)
            return "BUST"
        if(score[turn - 1] == 21):
            dealer_hand[-1][-1] = False
            render_hand(player, active_terminal, hand, dealer_hand)
            input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: YOU GOT A 21!")
            player.ss.overwrite("\r" + " " * 40)
            return "WIN"
    
    while(score[turn] < 17):
        dealer_hand.append(draw(player, True, True, score))
        score[turn] += dealer_hand[-1][0]
    for card in dealer_hand:
        card[-1] = False
    render_hand(player, active_terminal, hand, dealer_hand)
    if(score[turn] > 21):
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: DEALER BUST!")
        player.ss.overwrite("\r" + " " * 40)
        return "WIN"
    if(score[turn - 1] < score[turn]):
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: DEALER WINS!")
        player.ss.overwrite("\r" + " " * 40)
        return "BUST"
    elif(score[turn - 1] > score[turn]):
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: YOU WIN!")
        player.ss.overwrite("\r" + " " * 40)
        return "WIN"
    else:
        input(player.COLORS.backYELLOW+player.COLORS.BLACK+f"\rPlayer {turn}: STAND-OFF!")
        player.ss.overwrite("\r" + " " * 40)
        return "TIE"
    
    

def play(player, active_terminal, bet):
    outcome = turn(player, active_terminal, 1)

    match outcome:
        case "WIN":
            player.ss.update_quadrant(active_terminal, header + f"\n{status[1]}")
            bet *= 2
        case "BUST":
            player.ss.update_quadrant(active_terminal, header + f"\n{status[0]}")
            bet = 0
        case "TIE":
            player.ss.update_quadrant(active_terminal, header + f"\n{status[2]}")

    player.ss.print_screen()
    input("\r")
    player.ss.overwrite("\r" + " " * 40)
    return bet