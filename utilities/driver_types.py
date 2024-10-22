import enum

@enum.unique
class DriverTypes(enum.IntEnum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3