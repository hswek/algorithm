mem={}
def solve(card_idx, coin,have_card,card_shop):
    what_make=len(cards)+1
    if card_idx>=len(cards):
        return 0
    next_card,next_card2=cards[card_idx],cards[card_idx+1]
    card_shop=card_shop|{next_card,next_card2}
    d={}
    for i in have_card:
        d[i]=True
        if what_make-i in d:
            return solve(card_idx+2,coin,have_card-{i,what_make-i},card_shop)+1
    if coin<1:
        return 0
    for i in card_shop:
        if what_make-i in have_card:
            return solve(card_idx+2,coin-1,have_card-{what_make-i},card_shop)+1
    d={}
    if coin<2:
        return 0
    for i in card_shop:
        d[i]=True
        if what_make-i in d:
            return solve(card_idx+2,coin-2,have_card,card_shop-{i})+1
    return 0
def solution(coin, c):
    global cards
    cards=c
    answer = 0
    return solve(len(cards)//3,coin,set(cards[:len(cards)//3]),set([]))+1