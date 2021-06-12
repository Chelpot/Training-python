import discord
import random
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

class Player():
    name = ''
    inventory = []
    health = 100
    
    __init__(self, name, inventory):
        self.name = name

    fill_inventory():
        pass

    


    pass


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        
        arg = message.content
        list_arg = arg.split()
        print(arg)
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if arg.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if arg.startswith('!d20'):
            result = random.randint(1, 20)
            await message.channel.send('Resultat du lance : '.format(message) + str(result))

        if arg.startswith('!inventory add'):
            f= open("inventory.txt","w+")
            a = ''
            for i in range(2, len(list_arg)):
                a += (list_arg[i] + '\n')
                f.write(list_arg[i] + '\n')
            f.close()
     
            await message.channel.send('Nouveau contenu de l\'inventaire : \n'.format(message) + a)
        if arg.startswith('!test'):
            data = {}
            data['players'] = []
            data['players'].append({
                'name': '{0.author.mention}',
                'website': 'stackabuse.com',
                'from': 'Nebraska'
            })
            data['players'].append({
                'name': 'Larry',
                'website': 'google.com',
                'from': 'Michigan'
            })
            data['players'].append({
                'name': 'Tim',
                'website': 'apple.com',
                'from': 'Alabama'
            })

            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            await message.channel.send('Test effectué'.format(message))

    
client = MyClient()
client.run('ODMwNDk5NzAwMDk1NDUxMjE2.YHHlHg.ZJjwsx8nAeaHqP8eo-tgo7nxIhQ')
