from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
TOKEN = '8080267661:AAFqsRJ3u12HZF1031dItC2vhYWzl1301KpjMplMHec'
import talk_keh as tk

# TRIGGER_WORDS = {
#     "안녕":"...소라고둥님이 당신을 바라봅니다.",
#     "정보":"...소라고둥님은 당신이 질문하기를 기다립니다.",
#     "기분":"...소라고둥님은 기분에 반응하지 않습니다.",
#     "ㅠㅠ":"...소라고둥님은 눈물에 관심이 없습니다.",
#     "집?":"...아니오.",
#     "지금 자도 될까요?":"...아니오.",
#     "집에 가도 될까요?":"...예.",
#     "마법의 소라고둥님":"...소라고둥님이 눈을 떴습니다.",
#     "바보":"...소라고둥님은 당신을 외면합니다."

# }

async def start(update, context):  # async는 비동기 처리를 하는 것(스레드 처리와 비슷) !
    await update.message.reply_text("마법의 소라고둥님이 깨어나는 중입니다...")  # 뭔가 할 부분은 await 넣어주면 된다 !
async def monitor_chat(update, context):
    user_text = update.message.text    # 감지된 메세지 모두 다 
    chat_id  = update.message.chat_id  # chat_id : 메세지가 온 채팅방을 뜻함! > 어디서든 답장할 수 있게 됨 갸아아악

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