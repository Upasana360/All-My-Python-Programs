class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<5:
        raise NameTooShortError('name is too short')

username=input("Enter  ur name:")
validate(username)
print(f"hii{username}")