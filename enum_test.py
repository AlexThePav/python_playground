from enum import Enum

class InstanceType(Enum):
    DEF = 1
    CLEAN = 2

print(InstanceType.CLEAN)
for thing in InstanceType:
    print(thing)
