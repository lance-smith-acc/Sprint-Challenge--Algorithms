'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Loop through each letter in pairs to check if it is 'th' until the length of the word is under two
    # Set a counter
    totalTh = 0
    # Set the pair to be the next two letters
    pair = word[:2]

    # If the length is less than 2, there aren't enough letters for th and it stops
    if len(word) < 2:
        return totalTh
    # If the pair is th, count and recur, skipping the next letter(h)
    elif pair == 'th':
        totalTh += 1
        totalTh += count_th(word[2:])
    # Otherwise, recur to the next letter
    else:
        totalTh += count_th(word[1:])
    return totalTh