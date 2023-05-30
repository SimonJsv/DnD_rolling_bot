from roll_service import RollService
# Event handling - hook into messages in the channel or the reaction events
# handles all the events

# Message handling -> Look if the message command and then sends it to the correct command handler
# handles all the messages
# Is message=command true
# What is the command?
# Rolling command -> Roll service 

# Roll service -> splits up the different parts of the command to get the calculate equation
# Example 3d6 + 3d4 + 2
# Separate different die rolls from input so 3d6 on its own + 3d4 on its own 
# Dice roller - rolls the dice

# Dice formatter -> Format each calculation of the dice rolled to be human-readable

# Mailman -> mailman delivers the mail(messges) to message the discord channel 

# Reaction handling
# Reaction command
# Reaction on roles ->
BOT_PREFIX = "+"
ROLL_PREFIX = "roll "
message1, message2, message3 = "+Roll d10+10", "+roll 6d6+8d8", "roll 6d6"
roll_service = RollService()

def EventHandler(message):
    if not message.startswith(BOT_PREFIX):
        return
    
    message = message[len(BOT_PREFIX):]
    if message.lower().startswith(ROLL_PREFIX):
        roll_command = message[len(ROLL_PREFIX):].strip()
        print(f"Roll command: {roll_command}")
        split_command = roll_command.split('+')
        
        response = ""
        for command in split_command:
            if 'd' in command:
                result = roll_service.process_roll_command(command)
                response += result + "\n"
        
        print(f"Split command: {split_command}")
        print(response)


EventHandler(message1)
