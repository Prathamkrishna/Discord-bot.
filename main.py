import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad", "depressed", "hate", "unhappy"]

starter_encouragement = [
  "cheer up",
  "you got this",
  "cmon lessgooo",
]

dont_swear = [
  "your mom",
  "that's gay",
  "you're gay",
]

sarcasm_text = [
  "haha",
  "very funny",
  "v funny",
  "lol",
  "lmao",
  "lmfao",
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if message.content.startswith('hello bot'):
    await message.channel.send('hello')
  if message.content.startswith('hello'):
    await message.channel.send('hi')
   if message.content.startswith('who developed you sicko?'):
    await message.channel.send('@prathamkrishna did')

  if any(word in msg for word in sarcasm_text):
    await message.channel.send('funny')

  if message.content.startswith('inspire me'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in dont_swear):
    await message.channel.send("warning you bruh")

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragement))

  if msg.startswith("who are you"):
    await message.channel.send("hi im sicko, nice meeting you")

keep_alive()

client.run(os.getenv('TOKEN'))

