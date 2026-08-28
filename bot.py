import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 建立 bot 物件
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 自訂訊息列表 - 修改這裡來設定你想發送的 5 則訊息
CUSTOM_MESSAGES = [
    "😂 這是第一條訊息",
    "🎉 這是第二條訊息",
    "✨ 這是第三條訊息",
    "🚀 這是第四條訊息",
    "💯 這是第五條訊息"
]

@bot.event
async def on_ready():
    print(f'{bot.user} 已登入')
    try:
        synced = await bot.tree.sync()
        print(f"同步了 {len(synced)} 個斜線命令")
    except Exception as e:
        print(f"同步命令時出錯: {e}")

@bot.tree.command(name="sblol", description="發送 5 則自訂訊息")
async def sblol(interaction: discord.Interaction):
    """發送 5 則連續的自訂訊息"""
    await interaction.response.defer()
    
    # 發送 5 則訊息
    for i, message in enumerate(CUSTOM_MESSAGES, 1):
        try:
            await interaction.followup.send(message)
        except Exception as e:
            await interaction.followup.send(f"發送第 {i} 則訊息時出錯: {e}")
    
    await interaction.followup.send("✅ 已發送完成所有 5 則訊息！")

# 啟動 bot
if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ 錯誤: 請在 .env 文件中設定 DISCORD_TOKEN")
    else:
        bot.run(token)
