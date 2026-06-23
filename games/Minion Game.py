def minion_game(string: str):
    """Print the winner of the game and the score."""
    kevin = stuart = 0
    length: int = len(string)
    for i, char in enumerate(string):
        points: int = length - i
        if char in {"A", "E", "I", "O", "U"}:
            kevin += points
        else:
            stuart += points
    if kevin == stuart:
        print("Draw")
    else:
        print(*("Stuart", stuart) if stuart > kevin else ("Kevin", kevin))
if __name__ == '__main__':
    s = input()
    minion_game(s)
