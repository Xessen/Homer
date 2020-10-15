import random
import time
import tracemalloc

from discord.ext import commands

tracemalloc.start()

GBplayers= {}
GBnames= {}
GBalive= {}
GBdead={}
'''

###Eğer ki performans kötü olursa her rol için dict içinde list hazırla ve rol yeteneklerini aktifleştirirken o listleri iteratele

GBDedective={}
GBScout={}'''



def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1

class Dedective():
    def __init__(self,target=None,user=None):
        self.target=target
        self.user=user
class Sorceress():
    def __init__(self,target=None,user=None):
        self.target=target
        self.user=user
class Nurse():
    def __init__(self,target=None,user=None):
        self.target=target
        self.user=user
class Scout():
    def __init__(self,target=None,user=None):
        self.target=target
        self.user=user
#
roleList = [Dedective(),Sorceress(),Nurse(),Scout()]\




class GBAbilites(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def target(self,ctx,target):
        ctxindex=GBnames[idx].index(str(ctx.author))
        try:
            GBplayers[idx][ctxindex].target=target
            GBplayers[idx][ctxindex].user=ctx.author
        except:
            pass







class GB(commands.Cog):
    def __init__(self,client):
        self.client=client


    @commands.command()
    async def test(self, ctx):
        await ctx.send("Success")


    @commands.command()
    async def join(self,ctx):
        global idx
        idx = ctx.message.guild.id

        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
        members=voiceChannel.members
        Game=True
        memberCount=len(members)
        day=0
        night=1
        GBplayers[idx] = []
        GBalive[idx] = []
        GBnames[idx] = []
        GBdead[idx] = []

        for i in range(memberCount):
            await ctx.send(f"{str(members[i])}={str(i)}")
            GBplayers[idx].append(members[i])
            GBalive[idx].append(members[i])
            GBnames[idx].append(str(members[i]))
            GBplayers[idx][i]=random.choice(roleList)
        GBplayers[idx][0] = Scout()
        GBplayers[idx][1] = Dedective()
        while Game:
            for i in range(0,10000):
                if i%2==0:
                    await ctx.send(f"```Day {day}```")



                    countdown(18)
                    day+=1


                elif i%2!=0:
                    await ctx.send(f"```Night {night}```")


                    for player in GBplayers[idx]:
                        if player.target is not None and str(player.__class__.__name__)=="Dedective" and GBalive[idx].count(player.user)==1:
                            de_result = GBplayers[idx][int(player.target)].__class__.__name__
                            gameresult = [de_result, de_result,de_result,random.choice(roleList).__class__.__name__]
                            await player.user.send(str(random.choice(gameresult)))
                    for player in GBplayers[idx]:
                        if player.target is not None and str(player.__class__.__name__)=="Scout" and GBalive[idx].count(player.user)==1:
                            try:
                                sc_result=GBplayers[idx][int(player.target)].target
                                await player.user.send(sc_result)
                            except:
                                await player.user.send("Your target didn't move")



                    countdown(3)
                    night+=1







def setup(client):
    client.add_cog(GB(client))
    client.add_cog(GBAbilites(client))
    '''
async def de_invest(self,ctx=,target,result='None'):

ctxindex=GBnames[idx].index(str(ctx.author))
if str(ctx.author)==GBnames[idx][int(ctxindex)] and str(GBplayers[idx][ctxindex].__class__.__name__)=="Dedective":
GBplayers[idx][ctxindex].target=str(target)
result=GBplayers[idx][int(target)].__class__.__name__
gameresult=[result,result,result,random.choice(roleList).__class__.__name__]
await ctx.author.send(str(random.choice(gameresult)))'''


'''
    @commands.command()
    async def sc_track(self,ctx,target):
        ctxindex=GBnames[idx].index(str(ctx.author))
        if str(ctx.author) == GBnames[idx][int(ctxindex)] and str(GBplayers[idx][ctxindex].__class__.__name__) == "Scout":
            if GBplayers[idx][int(target)].target is not None:
            #try:
                result = GBplayers[idx][int(target)].target
                await ctx.author.send(str(result))

            else:
            #except:
                await ctx.author.send("Your target didn't move")

'''