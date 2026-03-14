from pyrogram import Client, filters
from config import 36158990, 2bc759ef58bff2cdfbcd7a7c7a857711, 8724563518:AAHV2euLVvpraVbElRUaei9XoyoRXqkMh0g

app = Client(
    "rage_bot",
    api_id=36158990
    api_hash=2bc759ef58bff2cdfbcd7a7c7a857711
    bot_token=8724563518:AAHV2euLVvpraVbElRUaei9XoyoRXqkMh0g
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🔥 Rage TG Downloader Bot is ONLINE!")

print("Bot is starting...")

app.run()
