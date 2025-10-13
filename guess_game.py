from random import randint
import winsound
import time
class Guess_Number:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.max_attempts = 5
        self.reset_game()
    def reset_game(self):
        self.attempts = 0
        self.secret_number = None
        self.game_over = False
        sound_type = None
    def play_sound(self, sound_type):
        if sound_type == 'welcome':
            winsound.Beep(1500, 200)
            time.sleep(1)
        elif sound_type == 'correct':
            print('\a')
            print('\a')
            time.sleep(1)
        elif sound_type == 'wrong':
            winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
        elif sound_type == 'game_over':
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
             
    def generate_number(self):
        self.secret_number = randint(self.low, self.high)
        print(self.secret_number)
        print('欢迎来到猜数字王国')
        self.play_sound('welcome')
        print(f'我已经想好一个 {self.low} ~ {self.high} 的数字,你来猜猜看')
    def display_status(self):
        
        remmning = self.max_attempts - self.attempts 
        print(f'共有{self.max_attempts}次机会,还可以尝试{remmning}次.')
        
    def get_user_number(self):
        
        while True:
            try:
                guess = int(input())
                if self.low <= guess <= self.high:
                    return guess
                
                else:
                    print(f'请输入{self.low} ~ {self.high}之间的数字.')
            except ValueError:
                print('请输入有效的数字!!!')
    
            
    def check_value(self, guess):
        secret_number = self.secret_number
        self.attempts += 1
        
        if guess == secret_number:
            print(f'太棒了,你只用了{self.attempts}次就猜中了')
            self.game_over = True
            self.play_sound('correct')
            return True
        elif guess > secret_number:
            print('有点大了!!!')
    
        else:
            print('有点小了!!!')
        return False
        self.play_sound('wrong')
    def ask_play_again(self):
        while True:
            chioce = input('重玩一局？(y/n)：').lower()
            if chioce in ('y','yes'):
                return True
            elif chioce in ('n','no'):
                return False
            else:
                print('请输入 "yes"" or "no"')
        
        
        
    def play_ground(self):
        self.generate_number()
        while not self.game_over and self.attempts < self.max_attempts:
            guess = self.get_user_number()
            self.check_value(guess)
            if not self.game_over:
                self.display_status()
        if not self.game_over:
            print(f'游戏结束了,正确的数字是:{self.secret_number}')
            self.play_sound('game_over')
        
    def run(self):
        while True:
            self.reset_game()
            self.play_ground()
            if not self.ask_play_again():
                print('谢谢游玩！')
                break
game = Guess_Number(low=1, high=100)
game.run()
    
        
            
            
            
        
        
            
        
        