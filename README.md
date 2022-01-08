# HelpMeMahjong

## Inspiration
It's not uncommon to see NUS students gathering (legally) in groups of 4 to play an intense game of Mahjong late in the evening, including ourselves! With Chinese New Year just around the corner as well, we felt that it would be a great idea to create a Telegram bot that helps newer players decide what is the best tile to throw from your hand!

## What it does
**HelpMeMahjong** works by having the user type out the tiles in their hand or key it in manually using Telegram stickers.

The Telegram bot is then able to identify:
- Whether the user is one tile away from winning (and which tile the user is waiting for)
- Which is the best tile to throw out for any given hand

## How we built it
We split our development process into two parts and delegated our manpower accordingly:
1. Creating a Telegram bot that for you to put in your tiles information easily and provide you our best advice (i.e., the best tile to throw) to the user
2. Coming up with an algorithm to determine whether the user is one tile away from winning, whether the user has already won, and what is the best tile to throw out

## Challenges we ran into
It was tough coming up with an algorithm that could get us from a completely random set of tiles to an ideal hand and we had to reference multiple videos and research papers to find existing solutions that we could use. We eventually came up with the solution we have now, which is able to identify the best tile to throw out and the last tile needed for a player to win. 

Getting the user's input was another challenge that we had to tackle. While we initially wanted to use image recognition to achieve this, we realized that there were no existing resources for us to rely on and it would be difficult to train a bot to identify Mahjong tiles in a single day. Hence, we relied on a mix of getting users to tap on Telegram stickers, which is a slower but more beginner-friendly method for inputting tiles, and using shorthand notation for a faster initialization of the hand.

Integrating the front-end to the back-end was also a tough challenge as more bugs started to surface and we spent a huge amount of time debugging these issues.

## Accomplishments that we're proud of
Each time we reached a new milestone or fixed a particularly challenging bug, we felt a mix of relief and pride at our ability to push on. Overall, we were proud of our tenacity and our perseverance to code for long hours with only breaks for meals without giving up, even though we felt the pressure of the looming deadline and the millions of bugs we had to fix.

Of course, we are also immensely proud of the product that we came up with in less than a day's worth of work.

## What we learned
This was our first experience making Telegram bots and we felt that this was a good learning experience. 

For two of our group members, this was their first experience with Mahjong and they had to pick up the game rather quickly before starting on this Telegram bot. Hopefully they'll be able to win some money while using the bot! We also learned about how to calculate whether a Mahjong hand is complete or not using various mathematical methods that we never thought of using before.

## What's next for HelpMeMahjong
Our main goal, which we feel would enhance our project immensely, would be to include image recognition for user input by having users snap a picture of their hand and have the individual tiles be parsed by the bot. We ran into some difficulty accomplishing this task with the limited time that we had, but would love to take up this challenge to improve the bot further in the future!
