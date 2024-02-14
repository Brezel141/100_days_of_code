
This Python script is a password generator. It first defines lists of possible letters, numbers, 
and symbols that can be included in the password.

The user is then prompted to specify how many letters, symbols, and numbers they want in their password.

The script generates a password in two ways:

Easy Level: The password is created by sequentially adding a random letter, symbol, or number to the 
password string based on the user's input. The order of characters in this password is not randomised, 
meaning it follows the order of letters, symbols, and numbers.

Hard Level: The password is created by adding a random letter, symbol, or number to a list. The list 
is then shuffled to randomise the order of the characters. The shuffled list is then converted back 
into a string to form the final password.

Both generated passwords are printed out at the end.