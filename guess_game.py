import random
class GuessNumberPlay:
    
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.secert_number = random.randint(low, high)
        self.attempts = 0
        self.max_attempts = 5
    def get_user_guess(self):
        print(f'一共能猜{self.max_attempts}次，你已猜了{self.attempts}次')
        while True:
            self.attempts += 1
            try:
                guess = int(input())
                if self.low <= guess <= self.high:
                    return guess
                else:
                    print(f'请输入{self.low}~{self.high}的整数。')
            except ValueError:
                print('请输入一个有效的数字!!!')
        
    def start_game(self):
        print(f'我们来玩猜数字游戏，我想好了一个 {self.low} ~ {self.high} 的数字，你来猜猜看？')
        print(self.secert_number)
        
        while self.attempts < self.max_attempts:
            guess = self.get_user_guess()
            
             
            if guess == self.secert_number:
                print(f'太棒了，你只用了{self.attempts}次就猜对了，太厉害了！！！')
                break
            elif guess > self.secert_number:
                print('猜的有点大了，再小点')
                
            else:
                print('猜的有点小了， 再大点')
        else:
            print(f'游戏结束，正确答案是{self.secert_number}')
            
        
g = GuessNumberPlay(low=1, high=200)

g.start_game()
        
            
        
        