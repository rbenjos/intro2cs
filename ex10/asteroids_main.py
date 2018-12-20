from screen import Screen
from ship import *
from asteroid import *
from torpedo import *
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    HEADING_DEFAULT = 0
    ASTEROID_SPEED_RANGE = [1,4]
    ASTEROID_DEFAULT_SIZE = 3
    HIT_TITLE = "oh no!"
    HIT_MESSAGE = "you were hit by an astroid"
    BIG_ASTEROID = 3
    MED_ASTEROID = 2
    SMALL_ASTEROID = 1
    BIG_SCORE = 100
    MED_SCORE = 50
    SMALL_SCORE = 20
    TORPEDO_LIFETIME = 200
    WINNING_TITLE = "Congratulations!"
    WINNING_MESSAGE = "you have won the game"
    LOSING_TITLE = "Game over!"
    LOSING_MESSAGE = "you have lost the game, try again"
    QUIT_TITLE = "Bye!"
    QUIT_MESSAGE = "we hope to see you again!"


    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        ship_location = self.random_location()
        self.__game_ship = Ship(ship_location)

        self.ast_amount = asteroids_amount
        self.ast_list = []
        self.__create_astroids(asteroids_amount)

        self.torpedo_list = []
        self.score = 0

    def __create_astroids(self, asteroids_amount):
        for i in range(asteroids_amount):
            ast = self.create_rand_ast()
            self.ast_list.append(ast)
            self.__screen.register_asteroid(ast, ast.get_size())

    def random_location(self):
        x_cor = random.randrange(self.__screen_min_x, self.__screen_max_x)
        y_cor = random.randrange(self.__screen_min_y, self.__screen_max_y)
        location = [x_cor, y_cor]
        return location

    def create_rand_ast(self):

        ast_location = self.random_location()
        ast_x_speed = random.randrange(self.ASTEROID_SPEED_RANGE[0],
                                       self.ASTEROID_SPEED_RANGE[1])

        ast_y_speed = random.randrange(self.ASTEROID_SPEED_RANGE[0],
                                       self.ASTEROID_SPEED_RANGE[1])

        ast_speed = [ast_x_speed, ast_y_speed]
        ast = Asteroid(ast_location, ast_speed, self.ASTEROID_DEFAULT_SIZE)
        return ast

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):

        # ship
        self.ship_update()

        # astroid
        self.asteroid_update()

        # torpedo

        self.torpedo_update()

        self.endgame()

    def endgame(self):
        if len(self.ast_list) == 0:
            self.__screen.show_message(self.WINNING_TITLE,self.WINNING_MESSAGE)
            self.__screen.end_game()
            sys.exit()
        elif self.__game_ship.get_life() == 0:
            self.__screen.show_message(self.LOSING_TITLE,self.LOSING_MESSAGE)
            self.__screen.end_game()
            sys.exit()

        elif self.__screen.should_end():
            self.__screen.show_message(self.QUIT_TITLE,self.QUIT_MESSAGE)
            self.__screen.end_game()
            sys.exit()




    def ship_update(self):

        x_cor = self.__game_ship.get_location()[0]
        y_cor = self.__game_ship.get_location()[1]
        self.__screen.draw_ship(x_cor,y_cor,self.__game_ship.get_direction())
        ship_new_loc = self.new_coordinates(self.__game_ship)
        self.__game_ship.set_location(ship_new_loc)
        ship_new_dir = self.new_direction(self.__game_ship)
        self.__game_ship.set_direction(ship_new_dir)
        ship_new_sp = self.new_speed(self.__game_ship)
        self.__game_ship.set_speed(ship_new_sp)

        if self.__screen.is_teleport_pressed():
            location_unavailable = True
            while location_unavailable:
                location_unavailable = False
                tele_location = self.random_location()
                for ast in self.ast_list:
                    if ast.get_location == tele_location:
                        location_unavailable = True
            self.__game_ship.set_location(tele_location)


    def asteroid_update(self):

        self.ast_update_visual()
        self.ast_ship_interactions()
        self.ast_tor_interactions()

    def ast_update_visual(self):
        for ast in self.ast_list:
            ast_new_loc = self.new_coordinates(ast)
            ast.set_location(ast_new_loc)
            ast_x,ast_y = ast.get_location()
            self.__screen.draw_asteroid(ast,ast_x,ast_y)

    def ast_ship_interactions(self):
        for ast in self.ast_list:
            if self.__game_ship.get_life() > 0:
                if ast.has_intersection(self.__game_ship):
                    self.__game_ship.reduce_life()
                    self.__screen.remove_life()
                    self.__screen.show_message(self.HIT_TITLE,
                                               self.HIT_MESSAGE)
                    self.__screen.unregister_asteroid(ast)
                    self.ast_list.remove(ast)

    def ast_tor_interactions(self):
        for ast in self.ast_list:
            for tor in self.torpedo_list:
                if ast.has_intersection(tor):
                    self.ast_tor_hit(ast,tor)

    def ast_tor_hit(self,ast,tor):
        if ast.get_size() == self.BIG_ASTEROID:
            self.set_score(self.score+self.BIG_SCORE)
            self.split(ast,tor)

        elif ast.get_size() == self.MED_ASTEROID:
            self.set_score(self.score+self.MED_SCORE)
            self.split(ast,tor)

        elif ast.get_size() == self.SMALL_ASTEROID:
            self.set_score(self.score+self.SMALL_SCORE)
            self.ast_list.remove(ast)
            self.__screen.unregister_asteroid(ast)

        self.__screen.set_score(self.score)
        self.torpedo_list.remove(tor)
        self.__screen.unregister_torpedo(tor)

    def split(self,ast,tor):
        tor_speed_x,tor_speed_y = tor.get_speed()
        cur_speed_x,cur_speed_y = ast.get_speed()
        new_speed_x = (tor_speed_x+cur_speed_x)/\
                      ((cur_speed_x**2+cur_speed_y**2)**0.5)
        new_speed_y = (tor_speed_y+cur_speed_y)/ \
                      ((cur_speed_x**2+cur_speed_y**2)**0.5)

        ast1_speed = [new_speed_x,new_speed_y]
        ast2_speed = [-new_speed_x,-new_speed_y]

        ast1 = Asteroid(ast.get_location(),ast1_speed,ast.get_size()-1)
        ast2 = Asteroid(ast.get_location(),ast2_speed,ast.get_size()-1)

        self.ast_list.append(ast1)
        self.ast_list.append(ast2)

        self.__screen.register_asteroid(ast1,ast1.get_size())
        self.__screen.register_asteroid(ast2,ast2.get_size())

        self.ast_list.remove(ast)
        self.__screen.unregister_asteroid(ast)








    def torpedo_update(self):
        if self.__screen.is_space_pressed():
            if len(self.torpedo_list)<10:
                torpedo = self.fire_torpedo(self.__game_ship)
                self.__screen.register_torpedo(torpedo)
                self.torpedo_list.append(torpedo)

        if len(self.torpedo_list) > 0:
            for torpedo in self.torpedo_list:
                tor_new_loc = self.new_coordinates(torpedo)
                torpedo.set_location(tor_new_loc)
                tor_x,tor_y = torpedo.get_location()
                tor_heading = torpedo.get_direction()
                self.__screen.draw_torpedo(torpedo,tor_x,tor_y,tor_heading)

            for torpedo in self.torpedo_list:
                new_age = torpedo.get_age()+1
                torpedo.set_age(new_age)
                if new_age >= 200:
                    self.torpedo_list.remove(torpedo)
                    self.__screen.unregister_torpedo(torpedo)





    def fire_torpedo(self,ship):
        tor_loc = ship.get_location()
        ship_x_speed,ship_y_speed = ship.get_speed()
        tor_direction = ship.get_direction()
        direction_in_rad = self.deg_to_rad(tor_direction)

        tor_speed_x = ship_x_speed + 2*math.cos(direction_in_rad)
        tor_speed_y = ship_y_speed + 2*math.sin(direction_in_rad)

        tor_speed = [tor_speed_x,tor_speed_y]

        torpedo = Torpedo(tor_loc,tor_speed,tor_direction)
        return torpedo






    def new_coordinates (self, obj):
            delta_x = self.__screen_max_x - self.__screen_min_x
            delta_y = self.__screen_max_y - self.__screen_min_y
            speed_x,speed_y =obj.get_speed()[0],obj.get_speed()[1]
            old_x_cor, old_y_cor = obj.get_location()[0],obj.get_location()[1]

            new_x_cor = (speed_x + old_x_cor - self.__screen_min_x)%\
                        delta_x + self.__screen_min_x
            new_y_cor = (speed_y + old_y_cor - self.__screen_min_y)% \
                        delta_y + self.__screen_min_y

            new_location = [new_x_cor,new_y_cor]
            return new_location


    def new_direction (self, ship):
        direction = ship.get_direction()
        if self.__screen.is_left_pressed():
            direction += 7
        if self.__screen.is_right_pressed():
            direction -= 7
        return (direction)

    def new_speed (self,ship):

        speed_x,speed_y =ship.get_speed()[0],ship.get_speed()[1]
        new_speed = [speed_x,speed_y]
        direction_in_rad = self.deg_to_rad(ship.get_direction())

        if self.__screen.is_up_pressed():
            new_speed_x = speed_x + math.cos(direction_in_rad)
            new_speed_y = speed_y + math.sin(direction_in_rad)
            new_speed = [new_speed_x,new_speed_y]

        return new_speed



    def deg_to_rad (self, deg):
        return deg*(math.pi/float(180))

    def rad_to_deg (self, rad):
        return rad*(float(180)/math.pi)

    def get_score (self):
        return self.score

    def set_score (self,score):
        self.score = score






def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
