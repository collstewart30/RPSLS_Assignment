            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Scissors':
                print('Rock crushes Scissors')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Paper':
                print('Scissors cuts Paper')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Rock':
                print('Paper covers Rock')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Lizard':
                print('Rock crushes Lizard')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Spock':
                print('Lizard poisons Spock')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Scissors':
                print('Spock smashes Scissors')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Lizard':
                print('Scissors decapitates Lizard')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Paper':
                print('Lizard eats Paper')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Spock':
                print('Paper disproves Spock')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Rock':
                print('Spock vaporizes Rock')
                self.player_one.score += 1
                print('{self.player_one.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
            else:
                self.player_two.score += 1
                print('{self.player_two.name} wins!')
                print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
