def remove_fourth_character(word: str) -> str:
    removed_character = word[:3]
    removed_character1 = word[4:]
    return removed_character + removed_character1


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
