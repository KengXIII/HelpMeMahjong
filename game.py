from utils import TILE_OPTIONS

'''
A database storing the full set of tiles.

gameState {
  chat_id: true
}
'''

gameState = {}

'''
A database storing the user's current hand.

myHand {
  user_id: sampleHand
}
'''
myHand = {}

number_of_tiles_on_my_hand = lambda user_id : 0 if not myHand else sum(myHand[user_id].values())

is_started = lambda : False

completeHand = {k: 1 for k in TILE_OPTIONS}

# completeHand = {
#   "dong" : 1,
#   "nan" : 1,
#   "xi" : 1,
#   "bei" : 1,
#   "fa" : 1,
#   "zhong" : 1,
#   "bai" : 1,
#   "1wan" : 1,
#   "2wan" : 1,
#   "3wan" : 1,
#   "4wan" : 1,
#   "5wan" : 1,
#   "6wan" : 1,
#   "7wan" : 1,
#   "8wan" : 1,
#   "9wan" : 1,
#   "1tiao" : 1,
#   "2tiao" : 1,
#   "3tiao" : 1,
#   "4tiao" : 1,
#   "5tiao" : 1,
#   "6tiao" : 1,
#   "7tiao" : 1,
#   "8tiao" : 1,
#   "9tiao" : 1,
#   "1tong" : 1,
#   "2tong" : 1,
#   "3tong" : 1,
#   "4tong" : 1,
#   "5tong" : 1,
#   "6tong" : 1,
#   "7tong" : 1,
#   "8tong" : 1,
#   "9tong" : 1
# }

sampleHand = {
  "dong" : 1,
  "nan" : 0,
  "xi" : 0,
  "bei" : 0,
  "fa" : 0,
  "zhong" : 1,
  "bai" : 0,
  "1wan" : 0,
  "2wan" : 0,
  "3wan" : 2,
  "4wan" : 0,
  "5wan" : 0,
  "6wan" : 3,
  "7wan" : 0,
  "8wan" : 0,
  "9wan" : 0,
  "1tiao" : 0,
  "2tiao" : 0,
  "3tiao" : 0,
  "4tiao" : 0,
  "5tiao" : 0,
  "6tiao" : 0,
  "7tiao" : 0,
  "8tiao" : 0,
  "9tiao" : 0,
  "1tong" : 0,
  "2tong" : 0,
  "3tong" : 0,
  "4tong" : 0,
  "5tong" : 0,
  "6tong" : 0,
  "7tong" : 0,
  "8tong" : 0,
  "9tong" : 0
}

emptyHand = {k: 0 for k in TILE_OPTIONS}

# emptyHand = {
#   "dong" : 0,
#   "nan" : 0,
#   "xi" : 0,
#   "bei" : 0,
#   "fa" : 0,
#   "zhong" : 0,
#   "bai" : 0,
#   "1wan" : 0,
#   "2wan" : 0,
#   "3wan" : 0,
#   "4wan" : 0,
#   "5wan" : 0,
#   "6wan" : 0,
#   "7wan" : 0,
#   "8wan" : 0,
#   "9wan" : 0,
#   "1tiao" : 0,
#   "2tiao" : 0,
#   "3tiao" : 0,
#   "4tiao" : 0,
#   "5tiao" : 0,
#   "6tiao" : 0,
#   "7tiao" : 0,
#   "8tiao" : 0,
#   "9tiao" : 0,
#   "1tong" : 0,
#   "2tong" : 0,
#   "3tong" : 0,
#   "4tong" : 0,
#   "5tong" : 0,
#   "6tong" : 0,
#   "7tong" : 0,
#   "8tong" : 0,
#   "9tong" : 0,
# }

initialAction = {
  "draw" : False,
  "throw" : False,
  "initialise" : False
}

action = {}