import json
import requests
import base64
from nbt import nbt
from io import BytesIO

api = '9c7381cb-309e-4aa2-a019-75a54c63f863'

#Meathods used throughout the program making it easier for the creator

def welcome():
#Welcome message
    print('████████████████████████████████████████████████████████████████████████████████████████\n█─█─█▄─█─▄█▄─▄▄─█▄─▄█▄─▀─▄█▄─▄▄─█▄─▄█████─▄▄▄▄█▄─█─▄█▄─█─▄█▄─▄─▀█▄─▄███─▄▄─█─▄▄▄─█▄─█─▄█\n█─▄─██▄─▄███─▄▄▄██─███▀─▀███─▄█▀██─██▀███▄▄▄▄─██─▄▀███▄─▄███─▄─▀██─██▀█─██─█─███▀██─▄▀██\n█▄█▄██▄▄▄██▄▄▄███▄▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄▄▄▄███▄▄▄▄▄█▄▄█▄▄██▄▄▄██▄▄▄▄██▄▄▄▄▄█▄▄▄▄█▄▄▄▄▄█▄▄█▄▄█\n████████████████████████████████████████████████████\n█▄─▀█▄─▄█▄─▄▄─█─▄─▄─█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█─▄─▄─█─█─█\n██─█▄▀─███─▄█▀███─████─█─█─█─██─██─██─▄─▄███─███─▄─█\n█▄▄▄██▄▄█▄▄▄▄▄██▄▄▄███▄▄▄█▄▄▄██▄▄▄▄█▄▄█▄▄██▄▄▄██▄█▄█\n█████████████████████████████████████████████████████████████\n█─▄▄▄─██▀▄─██▄─▄███─▄▄▄─█▄─██─▄█▄─▄████▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█\n█─███▀██─▀─███─██▀█─███▀██─██─███─██▀██─▀─████─███─██─██─▄─▄█\n█▄▄▄▄▄█▄██▄▄█▄▄▄▄▄█▄▄▄▄▄██▄▄▄▄██▄▄▄▄▄█▄▄█▄▄██▄▄▄██▄▄▄▄█▄▄█▄▄█\n')

#Notice
    print('    █▄ █ █▀█ ▀█▀ █ █▀▀ █▀▀\n    █ ▀█ █▄█  █  █ █▄▄ ██▄\n')
    print('Thank you for using "Hypixel Skyblock NetWorth Calculator" created by The_Nose_!')
    print('If you do like this program please be sure to upvote the reddit post and like the forums post.')
    print('For this calculator to work most effectivly make sure you have any items of value in a place')
    print('accessable by the api. These can be in your inventory, ender chest, or talismanbag for a few')
    print('examples. The calculator will take into account special reforges, enchants, and and')
    print('upgrades on an item so don\'t worry about those things. The program can not access your bank')
    print('through the api but it can access your purse, so be sure to keep that in mind.')
    print('All prices are taken from the public github repo for Jerry Bot by SkyBlockZ')
    print('Be sure to join their discord at discord.gg/skyblock')
    print('All items the program does not know will be stated so you can take those into account after')
    print('the fact. Remeber this program is still in a very early state and i need')
    print('all the feedback i can get. If there are any items that are not being taken into account')
    print('please tell me. You can contact me through out discord at https://discord.gg/sXMwhJH')
    print('-------------------------------------------------------------------------------------------')

def net_getIndex(data, autocor, xautocor, name):
    for i in range(len(xautocor)):
        if xautocor[i]['src'] == name:
            name = xautocor[i]['dest']
    
    for i in range(len(autocor)):
        if autocor[i]['src'] == name:
            name = autocor[i]['dest']
            
    for i in range(len(autocor)):
        if autocor[i]['src'] == name:
            name = autocor[i]['dest']
            
    for i in range(len(data)):
        if data[i]['name'] == name:
            return i
    return -1

def net_prockeck(data, name):
    for i in range(len(data)):
        if data[list(data)[i]]['cute_name'] == name:
            return data[list(data)[i]]['profile_id']
    return -1

def net_decode_data(raw):
   return nbt.NBTFile(fileobj = BytesIO(base64.b64decode(raw)))

def net_gitdataload(data):
    data = requests.get(data)
    data = data.text
    return json.loads(data)
    return -1

def net_petsvalue(pets):
    pass

def net_minions(minions, data, minautocor):
    minions.sort()
    global networthhi
    global networthlow
    for i in range(len(minions)):
        try:
            if minions[i].rsplit('_', 1)[1] >= minions[i+1].rsplit('_', 1)[1]:
                temp = minions[i].rsplit('_', 1)
                for i in range(len(minautocor)):
                    if minautocor[i]['src'] == temp[0]:
                        temp[0] = minautocor[i]['dest']
                summary = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=9c7381cb-309e-4aa2-a019-75a54c63f863&name=The_Nose_&productId="+temp[0]).json()
                networthhi += summary['product_info']['buy_summary'][0]['pricePerUnit'] * data[temp[0]][int(temp[1])]
                networthlow += summary['product_info']['buy_summary'][0]['pricePerUnit'] * data[temp[0]][int(temp[1])]
        except:
            if i != len(minions)-1:
                print('Couldn\'t find ' + temp[0] + ' minion data.')

def net_slayer(slayer):
    global networthhi
    global networthlow
    global itemname
    global itemlist

#Zombie
    try:
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_0'] * 100
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_0'] * 100
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_1'] * 2000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_1'] * 2000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_2'] * 10000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_2'] * 10000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_3'] * 50000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['zombie']['boss_kills_tier_3'] * 50000
    except:
        print('Some Zombie data missing.')

#Spider
    try:
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_0'] * 100
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_0'] * 100
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_1'] * 2000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_1'] * 2000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_2'] * 10000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_2'] * 10000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_3'] * 50000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['spider']['boss_kills_tier_3'] * 50000
    except:
        print('Some Spider data missing.')
        
#Wolf
    try:
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_0'] * 100
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_0'] * 100
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_1'] * 2000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_1'] * 2000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_2'] * 10000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_2'] * 10000
        networthlow += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_3'] * 50000
        networthhi += profile['profile']['members'][uuid]['slayer_bosses']['wolf']['boss_kills_tier_3'] * 50000
    except:
        print('Some Wolf data missing.')

#Main function for calculating net worth
def net_netcalc(inv):
    #Defining important variables
    global networthhi
    global networthlow
    global itemname
    global itemlist

    #Calculating the value of inventory by going item by item
    for i in range(len(inv[0])):
        x = 0
        
        #Checking if this item is even existant
        try:
            itemname = str(inv[0][i]['tag']['ExtraAttributes']['id'])
            itemlist.append(itemname)
        except:
            x=-1
        
        if x != -1:

            #Finds value of bare item
            x = net_getIndex(data, autocor, xautocor, itemname.lower())
            if x != -1:
                try:
                    networthhi += (data[x]['hi'] * int(str(inv[0][i]['Count'])))
                    networthlow += (data[x]['low'] * int(str(inv[0][i]['Count'])))
                except:
                    networthhi += data[x]['hi']
                    networthlow += data[x]['low']
            else:
                print(str(inv[0][i]['tag']['ExtraAttributes']['id']) + ' could not be found')

            if (itemname == 'GREATER_BACKPACK') or (itemname == 'LARGE_BACKPACK') or (itemname == 'MEDIUM_BACKPACK') or (itemname == 'SMALL_BACKPACK'):
                n = nbt.NBTFile(fileobj = BytesIO(bytearray(inv[0][i]['tag']['ExtraAttributes'][itemname.lower() + '_data'])))
                net_netcalc(n)

            #Calculates values of HPB if applicaple
            try:
                index = net_getIndex(data, autocor, 'hot_potato_book')
                networthhi += int(str(inv[0][i]['tag']['ExtraAttributes']['hot_potato_count'])) * data[index]['hi']
                networthlow += int(str(inv[0][i]['tag']['ExtraAttributes']['hot_potato_count'])) * data[index]['low']
            except:
                pass

            #Calculates value of encahnts if applicaple
            try:
                enchants = inv[0][i]['tag']['ExtraAttributes']['enchantments']
            except:
                pass

            #Giant Killer 6
            try:
                if int(str(enchants['giant_killer'])) == 6:
                    index = net_getIndex(data, autocor, 'giant_killer_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Growth 6
            try:
                if int(str(enchants['growth'])) == 6:
                    index = net_getIndex(data, autocor, 'growth_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Power 6
            try:
                if int(str(enchants['power'])) == 6:
                    index = net_getIndex(data, autocor, 'power_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Protection 6
            try:
                if int(str(enchants['protection'])) == 6:
                    index = net_getIndex(data, autocor, 'protection_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Sharpness 6
            try:
                if int(str(enchants['sharpness'])) == 6:
                    index = net_getIndex(data, autocor, 'sharpness_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Angler 6
            try:
                if int(str(enchants['angler'])) == 6:
                    index = net_getIndex(data, autocor, 'angle_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass
            
            #Caster 6
            try:
                if int(str(enchants['caster'])) == 6:
                    index = net_getIndex(data, autocor, 'caster_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Frail 6
            try:
                if int(str(enchants['frail'])) == 6:
                    index = net_getIndex(data, autocor, 'frail_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Luck of the Sea 6
            try:
                if int(str(enchants['luck_of_the_sea'])) == 6:
                    index = net_getIndex(data, autocor, 'luck_of_the_sea_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Magnet 6
            try:
                if int(str(enchants['magnet'])) == 6:
                    index = net_getIndex(data, autocor, 'magnet_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Lure 6
            try:
                if int(str(enchants['lure'])) == 6:
                    index = net_getIndex(data, autocor, 'lure_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Spiked Hook 6
            try:
                if int(str(enchants['spiked_hook'])) == 6:
                    index = net_getIndex(data, autocor, 'spiked_hook_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Dragon hunter
            try:
                if int(str(enchants['dragon_hunter'])) != 0:
                    index = net_getIndex(data, autocor, 'dragon_hunter_'+str(enchants['dragon_hunter']))
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Ender Slayer 6
            try:
                if int(str(enchants['ender_slayer'])) == 6:
                    index = net_getIndex(data, autocor, 'ender_slayer_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Smite 6
            try:
                if int(str(enchants['smite'])) == 6:
                    index = net_getIndex(data, autocor, 'smite_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Critical 6
            try:
                if int(str(enchants['critical'])) == 6:
                    index = net_getIndex(data, autocor, 'critical_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Bane of Arthropods 6
            try:
                if int(str(enchants['bane_of_arthropods'])) == 6:
                    index = net_getIndex(data, autocor, 'bane_of_anthropods_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Life Steal 4
            try:
                if int(str(enchants['life_steal'])) == 4:
                    index = net_getIndex(data, autocor, 'life_steal_iv')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Vampirism 6
            try:
                if int(str(enchants['vampirism'])) == 6:
                    index = net_getIndex(data, autocor, 'vampirism_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Experience 4
            try:
                if int(str(enchants['experience'])) == 4:
                    index = net_getIndex(data, autocor, 'experience_iv')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Luck 6
            try:
                if int(str(enchants['luck'])) == 6:
                    index = net_getIndex(data, autocor, 'luck_vi')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Looting 4
            try:
                if int(str(enchants['looting'])) == 4:
                    index = net_getIndex(data, autocor, 'looting_iv')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Scavenger 4
            try:
                if int(str(enchants['scavenger'])) == 4:
                    index = net_getIndex(data, autocor, 'scavenger_iv')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

            #Sugar Rush 3
            try:
                if int(str(enchants['sugar_rush'])) == 3:
                    index = net_getIndex(data, autocor, 'sugar_rush_iii')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']

            except:
                pass

            #True protection
            try:
                if int(str(enchants['true_protection'])) == 1:
                    index = net_getIndex(data, autocor, 'true_protection_i')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass
            
        #Checks for a wooden singularity on the item
            try:
                if int(str(inv[0][i]['tag']['ExtraAttributes']['wood_singularity_count'])) == 1:
                    index = net_getIndex(data, autocor, 'wood_singularity')
                    networthhi += data[index]['hi']
                    networthlow += data[index]['low']
            except:
                pass

        #Checks for fishing rod reforges
            #Salty
            try:
                if str(inv[0][i]['tag']['ExtraAttributes']['modifier']) == 'salty':
                    index = net_getIndex(data, autocor, 'hunk_of_ice')
                    networthhi += int(str(data[index]['hi'])) * 64
                    networthlow += int(str(data[index]['low'])) * 64
            except:
                pass

            #Treacherous
            try:
                if str(inv[0][i]['tag']['ExtraAttributes']['modifier']) == 'treacherous':
                    index = net_getIndex(data, autocor, 'hunk_of_blue_ice')
                    networthhi += int(str(data[index]['hi'])) * 64
                    networthlow += int(str(data[index]['low'])) * 64
            except:
                pass

x = 0

welcome()

#Getting IGN from player and converting it to a uuid
while x != 1:
    try:
        uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/"+input('IGN: ')).json()['id']
        x = 1
    except:
        print('Could not find account. Check spelling and capitalization.\nPlease try again.\n-----------------------')

#Accessing Player data with hypixel API

usr = requests.get('https://api.hypixel.net/player?key=' + api + '&uuid=' + str(uuid)).json()

#Asking which profile to check

pros = usr['player']['stats']['SkyBlock']['profiles']

x = -1
while x != 1:
    print('-----------------------')
    for i in range(len(list(pros))):
        print(pros[list(pros)[i]]['cute_name'], end = '   ')
    proid = net_prockeck(pros, input('\nSelect profile: ').lower().capitalize())
    if proid != -1:
        x=1
    else:
        print('Could not find profile please try again.')

print('-----------------------')

networthhi = 0
networthlow = 0
itemname = ''
itemlist = []

#Useing GitHub API to take skyblockz bots prices and alias' for future use

data = net_gitdataload('https://raw.githubusercontent.com/skyblockz/pricecheckbot/master/data.json')

autocor = net_gitdataload('https://raw.githubusercontent.com/skyblockz/pricecheckbot/master/alias.json')

xautocor = net_gitdataload('https://raw.githubusercontent.com/thenose2003/networth-extras/master/ExtraAutoCor.json')

mindata = net_gitdataload('https://raw.githubusercontent.com/thenose2003/networth-extras/master/MinionData.json')

minautocor = net_gitdataload('https://raw.githubusercontent.com/thenose2003/networth-extras/master/MinionNameToItem.json')

#Grabbing player data from the specified profile and converting into understandable NBT files using the hypixel API
profile = requests.get('https://api.hypixel.net/skyblock/profile?key=' + api + '&profile=' + proid).json()

    #Inventory
try:
    inv = net_decode_data(profile['profile']['members'][uuid]['inv_contents']['data'])
    net_netcalc(inv)
except:
    print('Couldn\'t find inventory data!')

    #Talisman Bag
try:
    talis = net_decode_data(profile['profile']['members'][uuid]['talisman_bag']['data'])
    net_netcalc(talis)
except:
    print('Couldn\'t find talisman data!')

    #Armor
try:
    armor = net_decode_data(profile['profile']['members'][uuid]['inv_armor']['data'])
    net_netcalc(armor)
except:
    print('Couldn\'t find armor data!')

    #Pets
try:
    pets = profile['profile']['members'][uuid]['pets']
except:
    print('Couldn\'t find pets data!')

    #Coins
try:
    coins = profile['profile']['members'][uuid]['coin_purse']
    networthhi += coins
    networthlow += coins
except:
    print('Couldn\'t find coin data!')

    #Ender Chest
try:
    echest = net_decode_data(profile['profile']['members'][uuid]['ender_chest_contents']['data'])
    net_netcalc(echest)
except:
    print('Couldn\'t find ender chest data!')

    #Candy
try:
    candy = net_decode_data(profile['profile']['members'][uuid]['candy_inventory_contents']['data'])
    net_netcalc(candy)
except:
    print('Couldn\'t find candy data!')

    #Slayer
net_slayer(profile['profile']['members'][uuid]['slayer_bosses'])

    #Minions
net_minions(profile['profile']['members'][uuid]['crafted_generators'], mindata, minautocor)

#Printing the final values for your calculated net worth
print('\n--------Items--------\n' + str(itemlist) + '\n\n-------Net-Worth-------')
if networthlow >= 1000000:
    print('Net Worth High: '+ str(round(networthhi/1000000, 2)) + 'm')
    print('Net Worth low: ' + str(round(networthlow/1000000, 2)) + 'm')
else:
    print('Net Worth High: '+ str(round(networthhi/1000, 2)) + 'k')
    print('Net Worth low: ' + str(round(networthlow/1000, 2)) + 'k')
while True:
    pass
