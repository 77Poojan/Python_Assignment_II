#Mario Game Basic Structure

class Topscore:
    
    def __init__(self):
        pass
    
    def top_score(self, score):
        pass

topscore = Topscore()


class Dragon:
    dragon_velocity = 10
    
    def __init__(self):
        pass
    
    def update(self):
        pass


class Flames:
    flames_velocity = 30
    
    def __init__(self):
        pass    
        
    def update(self):
        pass

    
class Mario:
    velocity = 10

    def __init__(self):
        pass

    def update(self):
        pass

def game_over():
    game_loop()
    
def start_game():
    while True:
        pass
    
def check_level(SCORE):
    pass

def game_loop():
    while True:
        dragon = Dragon()
        flames = Flames()
        mario = Mario()
        check_level()
        dragon.update()
        mario.update()

start_game()


