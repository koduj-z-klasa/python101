# stupid 2.6.1 by peterm

import random
import math
import rg

def around(l):
    return rg.locs_around(l)

def diag(l1, l2):
    if rg.wdist(l1, l2) == 2:
        if abs(l1[0] - l2[0]) == 1:
            return True
    return False

def infront(l1, l2):
    if rg.wdist(l1, l2) == 2:
        if diag(l1, l2):
            return False
        else:
            return True
    return False

def mid(l1, l2):
    return (int((l1[0]+l2[0]) / 2), int((l1[1]+l2[1]) / 2))

class Robot:
     def act(self, game):
        robots = game['robots']

        def isenemy(l):
            if robots.get(l) != None:
                if robots[l]['player_id'] != self.player_id:
                    return True
            return False

        def isempty(l):
            if ('normal' in rg.loc_types(l)) and not ('obstacle' in rg.loc_types(l)):
                if robots.get(l) == None:
                    return True
            return False

        def isspawn(l):
            if 'spawn' in rg.loc_types(l):
                return True
            return False

        # scan the area around
        enemies = []
        for loc in around(self.location):
            if isenemy(loc):
                enemies.append(loc)

        moveable = []
        moveable_safe = []
        for loc in around(self.location):
            if isempty(loc):
                moveable.append(loc)
            if isempty(loc) and not isspawn(loc):
                moveable_safe.append(loc)

        def guard():
            return ['guard']

        def suicide():
            return ['suicide']

        def canflee():
            return len(moveable) > 0

        def flee():
            if len(moveable_safe) > 0:
                return ['move', random.choice(moveable_safe)]
            if len(moveable) > 0:
                return ['move', random.choice(moveable)]
            return guard()

        def canattack():
            return len(enemies) > 0

        def attack():
            r = enemies[0]
            for loc in enemies:
                if robots[loc]['hp'] > robots[r]['hp']:
                    r = loc
            return ['attack', r]

        def panic():
            if canflee():
                return flee()
            elif canattack():
                return attack()
            else:
                return guard()

        if len(enemies) > 1:
			# if we gonna die next turn if we don't move
			if self.hp <= len(enemies)*10:
				# it's ok to suicide if you take someone else with you
				for loc in enemies:
					if robots[loc]['hp'] <= 15:
						return suicide()
			return panic()
        elif len(enemies) == 1:
			if self.hp <= 10:
				if robots[enemies[0]]['hp'] > 15:
					return panic()
				elif robots[enemies[0]]['hp'] <= 10:
					return attack()
				else:
					# might tweak this
					return suicide()
			else:
				if robots[enemies[0]]['hp'] <= 10:
					# avoid suiciders
					return panic()
				else:
					return attack()

        # if we're at spawn, get out
        if isspawn(self.location):
            return panic()

        # if there are enemies in 2 squares, predict and attack
        for loc, bot in game.get('robots').items():
            if isenemy(loc):
                if rg.wdist(loc, self.location) == 2:
                    if infront(loc, self.location):
                        return ['attack', mid(loc, self.location)]
                    if rg.wdist(rg.toward(loc, rg.CENTER_POINT), self.location) == 1:
                        return ['attack', rg.toward(loc, rg.CENTER_POINT)]
                    else:
                        return ['attack', (self.location[0], loc[1])]

        # move randomly
        return panic()
