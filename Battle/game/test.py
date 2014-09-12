import Actor
import TurnOrder

vesto = Actor.Actor('vesto', 'img')

pers = Actor.Spirit('pers', 'img') # speed = 10
logi = Actor.Spirit('logi', 'img', speed = 20)

bane = Actor.Bane('bob', 'img', speed = 7)
bob = Actor.Bane('jeff', 'img', speed = 199)

spirits = [pers, logi]
banes = [bane, bob]

aa = TurnOrder.TurnOrder(spirits, banes)
