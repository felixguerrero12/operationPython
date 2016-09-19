# Import Random and String packages
import random
import string

# Add ascii, digits and punctuation to the variable characters
characters = string.ascii_letters + string.digits + string.punctuation

# The length of your password
pw_length = 15
mypw = ""

# 1. Create a list of the 'pw_length' number. - range(pw_length)
# 2. Do a for loop for each number in the list. - for i in range(pw_length)
# 3. Calculate how much characters are in this variable - len(characters)
# 4. Randomly choose a number from the variable length - random.randrange()
# 5. Give number to next_index. next_index = random.randrange(len(characters))
# 6. Use number as index for the characters variable. - characters[next_index]
# 7. add that character to the variable mypw.
# 8. This runs till pw_length is done.
for i in range(pw_length):
    next_index = random.randrange(len(characters))
    mypw = mypw + characters[next_index]

# Print Variable mypw after the for loop is complete.
print('Your new password: ' + mypw)
