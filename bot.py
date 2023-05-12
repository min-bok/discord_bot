import os
import discord
import dotenv
dotenv.load_dotenv()

client = discord.Client(intents=discord.Intents.default())
token = os.environ.get("MY_TOKEN")

이혜영 = 0
전유진 = 0
백경현 = 0

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("이달의 오르미 선발"))
    print("구동중")
    print("=======")
    channels = client.guilds
    for ch in channels:
        channel = ch.get_channel(1105732842861887551)
        threads = channel.threads

        for th in threads:
            print(th) # 스레드 이름
            print(str(th.archive_timestamp)[0:10]) # 스레드 생성 날짜
            cnt = 0
            async for msg in th.history(limit=200):
                name = msg.author.name
                print(name) # 스레드에 메시지 올린 유저 이름
                cnt += 1
        

client.run(token)