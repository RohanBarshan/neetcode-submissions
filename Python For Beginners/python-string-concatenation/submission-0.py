def concatenate(s1: str, s2: str) -> str:
    total_length = len(s1) + len(s2)
    if total_length > 10:
        return "Too long!"
    else:
        return s1 + s2
    




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
