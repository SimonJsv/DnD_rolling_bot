# Roll service -> splits up the different parts of the command to get the calculate equation
# Example 3d6 + 3d4 + 2
# Separate different die rolls from input so 3d6 on its own + 3d4 on its own 
# Dice roller - rolls the dice
import random
# RollService class
class RollService:
    def __init__(self):
        pass

    def _dice_roller(self, amount, faces):
        # generate a random number based on the die "X" random between - 1-6
        # random.randint(1,X)
        # Make die into an object  -> make the die into an object
        rolls = [random.randint(1, faces) for i in range(amount)]
        return rolls

# Checks the inserted command and splits it up into the different component parts 
# First checks incase the roll starts with a "d10" for example and then just returns that calculation
    def _roll_command(self, command):
        if command.startswith('d'):
            amount = 1
            faces = command[1:]
        else:
            amount, faces = command.split('d')
        amount = int(amount)
        faces = int(faces)
        rolls = self._dice_roller(amount, faces)
        rolls_str = self.dice_formatter(rolls)
        return f"Rolling {amount}d{faces}'s = {rolls_str}"
    
    def _integer_command(self, command):
        return f"Adding {command}"

# Dice formatter -> Format each calculation of the dice rolled to be human-readable

    def _calculation_splitter(self, message):
        # split on + 3d6/3d4
        # number before the "d" is amount of times the die should be rolled
        # number after the "d" is amount of faces on the die, i.e 6 sides so from 1-6, 10 sides from 1-10 etc.
        # so the first number doesnt have to have the the "d" part inside of it, the second part needs that.
        parts = message.split('+')
        results = []
        for part in parts:
            if 'd' in part:
                result = self._roll_command(part)
                results.append(result)
            elif part.isdigit():
                result = self._integer_command(part)
                results.append(result)
        return results

# Dice formatter -> Format each calculation of the dice rolled to be human-readable
# Move to a different class/service
    def dice_formatter(self,rolls):
        rolls_str = ", ".join(str(roll) for roll in rolls)
        return rolls_str

# Process the roll command and finalizes the dice_formatters job before returning it.
    def process_roll_command(self, command):
        if '+' in command:
            results = self._calculation_splitter(command)
            response = " + ".join(results)
            return response
        else:
            result = self._roll_command(command)
            return result
