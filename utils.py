from tile import SuitedTile, HonorTile

MIN_TILES_ON_HAND = 13

TILE_OPTIONS = [
    # Circle
    "1tong",
    "2tong",
    "3tong",
    "4tong",
    "5tong",
    "6tong",
    "7tong",
    "8tong",
    "9tong",
    # Number
    "1wan",
    "2wan",
    "3wan",
    "4wan",
    "5wan",
    "6wan",
    "7wan",
    "8wan",
    "9wan",
    # Bamboo
    "1tiao",
    "2tiao",
    "3tiao",
    "4tiao",
    "5tiao",
    "6tiao",
    "7tiao",
    "8tiao",
    "9tiao",
    # Wind
    "dong",
    "nan",
    "xi",
    "bei",
    # Dragon
    "fa",
    "zhong",
    "bai"
]

SUITED_TILE_SET = [
    # Circle
    SuitedTile("Circle", 1),
    SuitedTile("Circle", 2),
    SuitedTile("Circle", 3),
    SuitedTile("Circle", 4),
    SuitedTile("Circle", 5),
    SuitedTile("Circle", 6),
    SuitedTile("Circle", 7),
    SuitedTile("Circle", 8),
    SuitedTile("Circle", 9),
    # Number
    SuitedTile("Number", 1),
    SuitedTile("Number", 2),
    SuitedTile("Number", 3),
    SuitedTile("Number", 4),
    SuitedTile("Number", 5),
    SuitedTile("Number", 6),
    SuitedTile("Number", 7),
    SuitedTile("Number", 8),
    SuitedTile("Number", 9),
    # Bamboo
    SuitedTile("Bamboo", 1),
    SuitedTile("Bamboo", 2),
    SuitedTile("Bamboo", 3),
    SuitedTile("Bamboo", 4),
    SuitedTile("Bamboo", 5),
    SuitedTile("Bamboo", 6),
    SuitedTile("Bamboo", 7),
    SuitedTile("Bamboo", 8),
    SuitedTile("Bamboo", 9),
    # Wind
    HonorTile("EastWind"),
    HonorTile("SouthWind"),
    HonorTile("WestWind"),
    HonorTile("NorthWind"),
    # Dragon
    HonorTile("GreenDragon"),
    HonorTile("RedDragon"),
    HonorTile("WhiteDragon")
]

TILE_MAP = {}

for (i, j) in zip(TILE_OPTIONS, SUITED_TILE_SET):
    TILE_MAP[i] = j
    
TILE_TO_TILE_OPTION_MAP = {v: k for (k, v) in TILE_MAP.items()}
