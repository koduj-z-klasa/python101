# jeżeli obok są przeciwnicy, atakuj
# wersja z pętlą przeglądającą wszystkie pola zajęte przez roboty
for poz, robot in game.robots.iteritems():
    if robot.player_id != self.player_id:
        if rg.dist(poz, self.location) <= 1:
            return ['attack', poz]
