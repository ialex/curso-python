# -*- coding: utf-8 -*-

"""
    Main app
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import sys
from random import randint
from pymongo import Connection
 
class Object(object):
    """
        Object base class
    """

    position_x = 0
    position_y = 0


class World(object):
    """
        World class
    """
    objects = []


class Player(object):
    """
        Players class
    """

    name = None
    points = 10
    max_life = 10
    current_life = 5
    position_x = 49#randint(0,100)
    position_y = 49#randint(0,100)
    db = None

    def __init__(self, db):

        self.db = db

        print '##########################################'
        print '### Bienvenido nuevo jugador'
        print '##########################################'
        
        self.name = raw_input('Escribe tu nombre: ')
        player = db.players.find_one({'name': self.name})
        if player is None:
            self.status()
            self.__distribute_points('life')
        else:
            self.position_x = player.position_x
            self.position_y = player.position_y
            self.current_life = player.current_life
            self.max_life = player.max_life
            self.points = player.points
            self.status()

    
    def status(self):
        empty_box = self.max_life - self.current_life
        barlife = ('[·]'*self.current_life) + ('[ ]'*empty_box)
        print '##########################################'
        print '### STATUS: %s' % (self.name)
        print '### CORDS: X=%d,Y=%d ' % (self.position_x, self.position_y)
        print '##########################################'
        print '### VIDA: %s' % (barlife)
        print '##########################################'
        return self.current_life
    
    def command(self, command):
        if command == 'up': 
            if self.position_y == 100:
                print "No puedes avanzar mas"
            else:
                self.position_y += 1
        elif command == 'down':
            if self.position_y == 0:
                print "No puedes avanzar mas"
            else:
                self.position_y -= 1
        elif command == 'left':
            if self.position_x == 0:
                print "No puedes avanzar mas"
            else:
                self.position_x -= 1
        elif command == 'right':
            if self.position_x == 100:
                print "No puedes avanzar mas"
            else:
                self.position_x += 1
        elif command == 'exit':
            player = {
                    'name': self.name,
                    'position_x': self.position_x,
                    'position_y': self.position_y,
                    'current_life': self.current_life,
                    'max_life': self.max_life,
                    'points': self.points
                    }
            self.db.players.insert(player)
            sys.exit()
        else:
            print "Comando no valido"

    def __distribute_points(self, category):
       
        print 'Tienes %d puntos para repartir' % (self.points)

        if category == 'life':    
            while True:
                points = raw_input('Cuantos puntos le agregas a tu barra de vida?: ')
                if points.isdigit():
                    points = int(points)
                    if points <= self.points:
                        break
                    else:
                        print "No tienes tantos puntos"

            self.points -= points
            self.current_life += points
            if self.max_life == self.current_life:
                self.max_life += points

            print 'Agregaste %d puntos a tu barra de vida' % (points) 
            print 'Ahora tienes %d puntos de vida' % (self.current_life)
            self.status()


if __name__ == '__main__':


    connection = Connection()
    db = connection.game
    items = db.items.find() 
    
    player = Player(db)
    world = World()


    for item in items:
        x = 50 #randint(1,100)
        y = 50 #randint(1,100)
        i = type(str(item['type']), (Object,), {'health':item['health']})
        obj = i()
        obj.position_x = x
        obj.position_y = y
        world.objects.append(obj)
        print "Debug: ", x, y, item['type']
    
    while True:
        prompt = '(%d, %d) : ' % (player.position_x, player.position_y)
        command = raw_input(prompt)
        player.command(command)

        for obj in world.objects:
            object_cords = (obj.position_x, obj.position_y)
            player_cords = (player.position_x, player.position_y)

            if object_cords == player_cords:
                if obj.__class__.__name__.lower() == 'posion':
                    player.current_life += int(obj.health)
                    print 'Te sumamos %d puntos de vida' % (obj.health,)
                else:    
                    print "Hay algo aqui"

