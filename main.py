import os
import telebot
from buttons import functionList
from hand import Hand
from utils import TILE_MAP, TILE_TO_TILE_OPTION_MAP
import sticker as stickerSet
import game
from game import number_of_tiles_on_my_hand
import time

from telebot.types import (BotCommand, InlineKeyboardButton,
InlineKeyboardMarkup, InlineQueryResultCachedSticker)

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# Set the shortcuts
bot.set_my_commands([  
    BotCommand('start', 'Starts a new game'),
    BotCommand('newgame', 'Restarts the game'),
    BotCommand('kill', 'Stops the game'),
    BotCommand('functions', 'Show the supported functions again')
])

is_hand_initialized = lambda user_id : game.number_of_tiles_on_my_hand(user_id) < 13   

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    """
    Command that welcomes the user and configures the required initial setup
    """
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.chat.type == 'private':
        chat_user = message.chat.first_name
    else:
        chat_user = message.chat.title

    # Image link of the start message
    img_url = "https://cdn.dribbble.com/users/1390683/screenshots/4321150/__2.png?compress=1&resize=200x200"

    # Create the response button
    buttons = []
    for functions in functionList:
        row = []
        option = InlineKeyboardButton(functions, callback_data=functions)
        row.append(option)
        buttons.append(row)

    if user_id in game.gameState and game.gameState[user_id] == True:
        # Game already started
        message = f'Hi {chat_user}, a game has already been started...\nTo play the tiles, please use the sticker pack provided ' + "<a href='https://t.me/addstickers/MahjongTiles'>here.</a>"
        bot.send_message(
            chat_id,
            message,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
        return

    elif (user_id in game.gameState and game.gameState[user_id] == False) or (user_id not in game.gameState):
        # Starts a new game
        game.gameState[user_id] = True
        game.myHand[user_id] = game.emptyHand.copy()
        game.action[user_id] = game.initialAction.copy()
        message = f'Hi {chat_user}, the game has started, please update your starting hand.\nTo play the tiles, please use the sticker pack provided ' + "<a href='https://t.me/addstickers/MahjongTiles'>here.</a>"
        bot.send_photo(chat_id, img_url)
        bot.send_message(
            chat_id,
            message,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )


        while game.gameState[user_id] == True:
          if game.number_of_tiles_on_my_hand(user_id) < 13:
            bot.send_message(chat_id, "You do not have enough cards on hand")
            game.action[user_id]["initialise"] = True
            while (game.number_of_tiles_on_my_hand(user_id) < 13):
                time.sleep(3)
          if game.number_of_tiles_on_my_hand(user_id) == 13:
            bot.send_message(chat_id, "What card did you add into your hand?")
            game.action[user_id]["draw"] = True
            while (game.number_of_tiles_on_my_hand(user_id) == 13):
                time.sleep(3)
          if game.number_of_tiles_on_my_hand(user_id) == 14:
            bot.send_message(chat_id, "After our careful recommendations, you should throw this tile!")
            recommend(user_id, chat_id)
            game.action[user_id]["throw"] = True
            bot.send_message(chat_id, "What card did you throw?")
            while (game.number_of_tiles_on_my_hand(user_id) == 14):
                time.sleep(3)
        return


@bot.message_handler(commands=['functions'])
def functions(message):
    """
    Command that lists all available functions
    """
    chat_id = message.chat.id

    chat_text = 'Select what you would like to do'

    buttons = []
    for functions in functionList:
        row = []
        option = InlineKeyboardButton(functions, callback_data=functions)
        row.append(option)
        buttons.append(row)

    bot.send_message(
        chat_id=chat_id,
        text=chat_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    return


@bot.message_handler(commands=['kill'])
def kill(message):
    """
    Command that stops the game
    """
    user_id = message.from_user.id
    chat_id = message.chat.id

    if (user_id not in game.gameState) or (user_id in game.gameState and game.gameState[user_id] == False):
        # There is no game started by the user
        chat_text = "No game is currently being played..."

    elif game.gameState[user_id] == True:
        # Game is killed successfully
        chat_text = "Game stopped, hope you won the game~"
        game.gameState[user_id] = False
        game.myHand[user_id] = game.emptyHand.copy()
        game.action[user_id] = game.initialAction.copy()

    # Send reply message to user
    bot.send_message(
        chat_id=chat_id,
        text=chat_text,
    )
    return


@bot.message_handler(commands=['newgame'])
def newgame(message):
    """
  Command that starts a new game
  """
    chat_id = message.chat.id
    user_id = message.from_user.id

    if (user_id not in game.gameState) or (game.gameState[user_id] == False):
        # No game started to restart
        chat_text = "There is no game started. Please use the /start command."
        bot.send_message(
            chat_id=chat_id,
            text=chat_text,
        )
        return

    else:
        game.myHand[user_id] = game.sampleHand.copy()
        game.action[user_id] = game.initialAction.copy()
        print("initialised sample")
        chat_text = "Game has been restarted."
        bot.send_message(
            chat_id=chat_id,
            text=chat_text,
        )
        return


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    """
    Handles the execution of the respective functions upon receipt of the callback query
    """
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    data = call.data

    if data.split()[0] == "Best":
        user_hand = game.myHand

        tiles_in_hand = []

        if not user_hand:
            chat_text = "You should have 14 tiles before you need to discard a tile."
            bot.send_message(chat_id=chat_id, text=chat_text)
            return

        for (tile_string_rep, count) in user_hand[user_id].items():
            for i in range(count):
                tiles_in_hand.append(TILE_MAP[tile_string_rep])

        # not enough tiles to be able to discard
        if len(tiles_in_hand) < 14:
            chat_text = "You should have 14 tiles before you need to discard a tile."
            bot.send_message(chat_id=chat_id, text=chat_text)
            return

        hand = Hand(tiles_in_hand)

        is_winning_hand = hand.isWinningHand()

        if is_winning_hand:
            chat_text = "You have won the game. There is no need to discard a tile."
            bot.send_message(chat_id=chat_id, text=chat_text)
        else:
            tile_to_throw = Hand.getTilesToThrow(tiles_in_hand)
            bot.send_sticker(
                chat_id,
                stickerSet.dictOld[TILE_TO_TILE_OPTION_MAP[tile_to_throw]])

    elif data.split()[0] == "Initialise":
        game.action[user_id]["initialise"] = True
        bot.send_message(chat_id, "Select the 13 tiles at the beginning")

    elif data.split()[0] == "Update":
        game.action[user_id]["throw"] = True
        bot.send_message(chat_id, "Please indicate the latest tile you discarded")

    elif data.split()[0] == "Drawn":
        game.action[user_id]["draw"] = True
        bot.send_message(chat_id, "Please indicate the latest tile you drew")

    elif data.split()[0] == "Fast":
        game.action[user_id]["initialise"] = True
        bot.send_message(chat_id, "Please type the string of tiles")

    return


@bot.message_handler(
    func=lambda message: game.gameState[message.from_user.id] == True and game.action[message.from_user.id]["initialise"] == True)
def fastInit(message):
    stringOfTiles = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id
    for tiles in stringOfTiles.split():
        if tiles.startswith("wan"):
            numsString = tiles[3:]

            for num in numsString:
                newString = num + "wan"
                game.myHand[user_id][newString] += 1

        elif tiles.startswith("tong"):
            numsString = tiles[4:]
            for num in numsString:
                newString = num + "tong"
                game.myHand[user_id][newString] += 1
        elif tiles.startswith("tiao"):
            numsString = tiles[4:]

            for num in numsString:
                newString = num + "tiao"
                game.myHand[user_id][newString] += 1
        else:
            bot.send_message(chat_id, "Please type the string of tiles")
            return

    number = sum(game.myHand[user_id].values())
    if number > 13:
        game.myHand[user_id] = game.emptyHand.copy()
        bot.send_message(chat_id, "Too many tiles added. Please reinitialise")
        return
    elif number == 13:
        game.action[user_id]["initialise"] = False

    bot.send_message(chat_id, str(number) + "tiles added.")


@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    results = []
    count = 0
    print("requested...")
    user_id = inline_query.from_user.id

    # Determine the current action
    action = determineAction(user_id)
    if (action == "none"):
        if (game.gameState[user_id] == True):
            for tiles in list(game.myHand[user_id].keys()):
                for i in range(game.myHand[user_id][tiles]):
                    sticker = InlineQueryResultCachedSticker(
                        id=count, sticker_file_id=stickerSet.dictOld[tiles])
                    results.append(sticker)
                    count += 1
            bot.answer_inline_query(inline_query.id, results, cache_time=5)
        return

    elif (action == "initialise" or action == "draw"):
        for tiles in list(game.completeHand.keys()):
            for i in range(game.completeHand[tiles]):
                sticker = InlineQueryResultCachedSticker(
                    id=count, sticker_file_id=stickerSet.dictOld[tiles])
                results.append(sticker)
                count += 1
        bot.answer_inline_query(inline_query.id, results, cache_time=5)
        return

    elif (action == "throw"):
        for tiles in list(game.myHand[user_id].keys()):
            for i in range(game.myHand[user_id][tiles]):
                sticker = InlineQueryResultCachedSticker(
                    id=count, sticker_file_id=stickerSet.dictOld[tiles])
                results.append(sticker)
                count += 1
        bot.answer_inline_query(inline_query.id, results, cache_time=5)
        return


def determineAction(user_id):
    dictOfActions = game.action[user_id]
    for key, value in dictOfActions.items():
        if value == True:
            return key
    return "none"


@bot.message_handler(
    content_types=["sticker"],
    func=lambda sticker: sticker.via_bot.username == "helpme_mahjong_bot")
def updateData(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if (all(value == 0 for value in game.action[user_id].values())):
        # No action taking place
        return

    action = determineAction(user_id)
    if action == "none":
      return
    if action == "draw":
      draw(message.sticker.file_unique_id, user_id, chat_id)
      return
    if action == "throw":
      throw(message.sticker.file_unique_id, user_id, chat_id)
      return
    if action == "initialise":
      initialise(message.sticker.file_unique_id, user_id, chat_id)
      return

def decodeTile(file_id):
    for tileTuple in stickerSet.tupleOfTiles:
        if tileTuple[1] == file_id:
            return tileTuple[0]

def recommend(user_id, chat_id):
    """
    Runs the algorithm to recommend the tile to discard
    """

    user_hand = game.myHand

    tiles_in_hand = []

    for (tile_string_rep, count) in user_hand[user_id].items():
        for i in range(count):
            tiles_in_hand.append(TILE_MAP[tile_string_rep])

    hand = Hand(tiles_in_hand)
    print(len(hand.insideTiles))
    is_winning_hand = hand.isWinningHand()

    if is_winning_hand:
        print("WIN LIAO")
        chat_text = "Congrats! Run /kill to end the game!"
        bot.send_message(chat_id=chat_id, text=chat_text)
        
    else:
        tile_to_throw = Hand.getTilesToThrow(tiles_in_hand)
        bot.send_sticker(
            chat_id,
            stickerSet.dictOld[TILE_TO_TILE_OPTION_MAP[tile_to_throw]])

    # if not user_hand:
    #     chat_text = "You should have 14 tiles before you need to discard a tile."
    #     bot.send_message(chat_id=chat_id, text=chat_text)
    #     return

    # not enough tiles to be able to discard
    # if len(tiles_in_hand) < 14:
    #     chat_text = "You should have 14 tiles before you need to discard a tile."
    #     bot.send_message(chat_id=chat_id, text=chat_text)
    #     return

    return

def draw(sticker_id, user_id, chat_id):
    tileName = decodeTile(sticker_id)
    game.myHand[user_id][tileName] += 1
    bot.send_message(chat_id, "Tile Drawn: " + tileName)
    game.action[user_id]["draw"] = False
    # if game.number_of_tiles_on_my_hand(user_id) == 14: 
    #     recommend(user_id, chat_id)

def throw(sticker_id, user_id, chat_id):
    tileName = decodeTile(sticker_id)
    game.myHand[user_id][tileName] -= 1
    bot.send_message(chat_id, "Tile Thrown: " + tileName)
    game.action[user_id]["throw"] = False

def initialise(sticker_id, user_id, chat_id):
    tileName = decodeTile(sticker_id)
    game.myHand[user_id][tileName] += 1
    number = sum(game.myHand[user_id].values())
    bot.send_message(chat_id, "Tile " + str(number) + ": " + tileName)
    if number >= 13:
        game.action[user_id]["initialise"] = False
        bot.send_message(chat_id, "All 13 tiles have been initialised")




@bot.message_handler(commands=['check'])
def check(message):
    print(game.myHand[message.chat.id].items())




bot.infinity_polling()
