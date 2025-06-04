from enum import Enum
import random
class Gender(Enum):
    MALE=1
    FEMALE=2
    OTHER=3

print(Gender.MALE.value)
randomValue=random.choice(list(Gender))
print(randomValue)