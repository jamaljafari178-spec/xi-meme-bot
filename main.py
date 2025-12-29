import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

BOT_TOKEN = "8569486551:AAGhne1XWPuoZiQ9C9g2Z8vxjvdVkM5Kxa4"
FAL_API_KEY = "e9f920d6-896f-4068-92d3-782df838676a:3fe3ef70848fb7e8eab0e9a96f5aa4dd"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌌 سلام به $XI Meme Generator! 🚀\n\n"
        "بات پیشرفته برای ساخت memeهای holographic و futuristic\n"
        "فقط prompt بنویس، meme خفن تحویل بگیر!\n\n"
        "مثال:\n"
        "• XI logo with neon blue eye in cosmic space\n"
        "• $XI rocket launching to the moon\n"
        "• Futuristic XI token in dark space\n\n"
        "#XItoTheMoon"
    )

@dp.message(F.text & ~F.command)
async def generate_meme(message: Message):
    prompt = message.text.strip()
    
    full_prompt = f"{prompt}, highly detailed holographic futuristic art, neon blue glowing effects, dark cosmic background, ultra sharp, cinematic lighting, sci-fi atmosphere"
    
    await message.answer("🧠 در حال ساخت meme... (۱۰-۳۰ ثانیه) 🚀")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/flux/schnell",
            headers={
                "Authorization": f"Key {FAL_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": full_prompt,
                "image_size": "square_hd"
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            image_url = data["images"][0]["url"]
            await message.answer_photo(
                image_url,
                caption=f"ممه آماده شد! 🌌\nPrompt: {prompt}\n#XItoTheMoon"
            )
        else:
            await message.answer("خطا در ساخت meme – دوباره امتحان کن.")
    
    except Exception as e:
        await message.answer("مشکل فنی موقت! بعداً امتحان کن 😅")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("$XI Meme Generator Bot در حال اجراست 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
