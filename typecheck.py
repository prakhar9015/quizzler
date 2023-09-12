# age: int
name: str
height: float
is_human: bool


# type hints and arrows

# age = "two"

def police_check(age: int) -> bool:  # age: int = using type hint for parameter and
    # -> bool = is a way to declare that this function will only return a boolean value

    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "ww"


print(police_check("twelve"))
