from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_KEY")
import talk_keh as tk
import gemini as gem
import movie
import melon
import market
import diet

async def start(update, context):  # async는 비동기 처리를 하는 것(스레드 처리와 비슷) !
    await update.message.reply_text("마법의 소라고둥님이 깨어나는 중입니다...")  # 뭔가 할 부분은 await 넣어주면 된다 !

async def send_photo(update, context):
    user_text = update.message.text
    for key, photo_url in tk.TRIGGER_WORDS.items():
        if key in user_text:
            await update.message.reply_photo(photo=photo_url,caption=caption)
            break

async def monitor_chat(update, context):
    user_text = update.message.text    # 감지된 메세지 모두 다 
    chat_id  = update.message.chat_id  # chat_id : 메세지가 온 채팅방을 뜻함! > 어디서든 답장할 수 있게 됨 갸아아악

    if "소라고둥님" in user_text:
        res = gem.aiai(user_text.replace("소라고둥님",""))
        await context.bot.send_message(chat_id=chat_id,text=res) #parse_mode="MarkdownV2" : 아직 실험중
        
    elif "음악" in user_text:
        res = melon.mel()
        await update.message.reply_text(res)

    elif "영화" in user_text:
        res = movie.mov()
        await update.message.reply_text(res)

    elif "주식" in user_text:
        res = market.finance()
        await update.message.reply_text(res)

    elif "오늘 메뉴" in user_text:
        res = diet.busan_menu()
        await update.message.reply_text(res)
        
    elif "도둑" in user_text:
        for key, photo_url in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await update.message.reply_photo(photo=photo_url,caption="❣️천사소녀 네티가 당신의 마음을 훔침 !💘")

    elif "자라" in user_text:
        for key, photo_url in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await update.message.reply_photo(photo=photo_url,caption="⚠️ 이런! 코난🧐이 당신에게 수면총💥을 맞춤 !😴")
                break

    elif "풍악" in user_text:
        for key, photo_url in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await update.message.reply_photo(photo=photo_url,caption="🎶🎊전하🫅께서 풍악🪕을 울리라신다 !🎊🎵")
                break
    
    elif "흥이 다 깨" in user_text:
        for key, photo_url in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await update.message.reply_photo(photo=photo_url,caption="🎸🎶👥 네! 알겠습니다 디오니소스님 !🎵👤🎸")
                break
                
    elif "따봉" in user_text:
        for key, photo_url in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await update.message.reply_photo(photo=photo_url,caption="🐾🦔 ...따봉도치가 조용히 엄지를 들어 올림 !👍💞")
                break
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id=chat_id,text=res)
                break   # 한 개의 키워드에만 반응하도록 !

def main():
    app = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 추가
    app.add_handler(CommandHandler("start",start))

    # 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))  # 명령어는 제외하라.
    
    
    print("마법의 소라고둥님은 가만히 질문을 기다립니다 ...")
    app.run_polling()
    

if __name__=='__main__':
    main()