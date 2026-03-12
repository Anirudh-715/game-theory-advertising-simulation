import random

def payoff(a,b):

    if a=="NoAd" and b=="NoAd":
        return 10,10
    if a=="Ad" and b=="NoAd":
        return 15,2
    if a=="NoAd" and b=="Ad":
        return 2,15
    if a=="Ad" and b=="Ad":
        return 5,5


def always_ad(history):
    return "Ad"

def never_ad(history):
    return "NoAd"

def tit_for_tat(history):
    if not history:
        return "NoAd"
    return history[-1][1]


def play(strategyA,strategyB,rounds=100):

    history=[]
    profitA=0
    profitB=0

    for _ in range(rounds):

        moveA=strategyA(history)
        moveB=strategyB(history)

        pA,pB=payoff(moveA,moveB)

        profitA+=pA
        profitB+=pB

        history.append((moveA,moveB))

    return profitA,profitB


strategies={
    "AlwaysAd":always_ad,
    "NeverAd":never_ad,
    "TitForTat":tit_for_tat
}

names=list(strategies.keys())

for i in range(len(names)):
    for j in range(i+1,len(names)):

        s1=names[i]
        s2=names[j]

        result=play(strategies[s1],strategies[s2])

        print(s1,"vs",s2,"->",result)