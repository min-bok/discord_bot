import os
import discord
import dotenv
dotenv.load_dotenv()

client = discord.Client(intents=discord.Intents.default())
token = os.environ.get("MY_TOKEN")


# 목표
# thread_list = [["스레드 이름", "스레드 생성 날짜", {이름: 메시지수}], ["스레드 이름", "스레드 생성 날짜", {이름: 메시지수}]....]
# 를 엑셀로 출력

thread_list = []
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
            name_list = []
            name_dict = {}
            total_list = []
            total_list.append(th) # 스레드 이름
            total_list.append(str(th.archive_timestamp)[0:10]) # 스레드 생성 날짜
            cnt = 0
            async for msg in th.history(limit=200):
                name = msg.author.name # 스레드에 메시지 올린 유저 이름
                name_list.append(name)
                cnt += 1
            for key in name_list:
                name_dict[key] = name_dict.get(key, 0) + 1

            total_list.append(name_dict)
            thread_list.append(total_list)

    # print(thread_list[0][0])
    # print(thread_list[0][1])
    # print(thread_list[0][2])

    # print(thread_list[1][0])
    # print(thread_list[1][1])
    # print(thread_list[1][2])

client.run(token)