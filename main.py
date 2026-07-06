#!/usr/bin/env python3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, SERVICES, MANAGERS, COMPANY_INFO, ARTICLE_LINK, PRICE_LINK
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = """🎯 FreaksServis Bot

Мы создали бот с полезной информацией и навигацией.

Выбирайте услугу → Пишите менеджеру

Просто делаем дело. ✅

Всем профитов! 💰"""
    
    try:
        if os.path.exists('freaksservis_video.mp4'):
            with open('freaksservis_video.mp4', 'rb') as video:
                await update.message.reply_video(
                    video=video,
                    caption=welcome_message,
                    reply_markup=get_main_menu()
                )
        else:
            await update.message.reply_text(welcome_message, reply_markup=get_main_menu())
    except:
        await update.message.reply_text(welcome_message, reply_markup=get_main_menu())


def get_main_menu() -> InlineKeyboardMarkup:
    keyboard = []
    
    keyboard.append([InlineKeyboardButton(text="📰 Что такое рефаунд?", url=ARTICLE_LINK)])
    
    keyboard.append([InlineKeyboardButton(
        text="📦 Дроп сервис",
        callback_data="service_drop_service"
    )])
    
    keyboard.append([InlineKeyboardButton(
        text="🎨 Отрисовка",
        url="https://t.me/risujudljatebja"
    )])
    
    keyboard.append([InlineKeyboardButton(
        text="💰 Скуп товаров",
        url="https://t.me/PROFIT_ASD"
    )])
    
    keyboard.append([InlineKeyboardButton(
        text="📦 Услуги Boxera",
        url="https://t.me/ASDSDA88"
    )])
    
    keyboard.append([InlineKeyboardButton(
        text="📚 Обучение",
        url="https://t.me/PROFIT_ASD"
    )])
    
    return InlineKeyboardMarkup(keyboard)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass
    
    if query.data.startswith("service_"):
        service_key = query.data.replace("service_", "")
        if service_key in SERVICES:
            service = SERVICES[service_key]
            manager = MANAGERS.get(service_key, {})
            username = manager.get('username', 'freakservis')
            
            message = f"""{service['emoji']} {service['name']}

{service.get('description', '')}"""
            
            keyboard = [
                [InlineKeyboardButton(
                    text=f"💬 Написать @{username}",
                    url=f"https://t.me/{username}"
                )]
            ]
            
            if service_key == 'drop_service':
                keyboard.append([InlineKeyboardButton(
                    text="💰 Прайс",
                    url=PRICE_LINK
                )])
            
            keyboard.append([InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main")])
            
            await context.bot.send_message(
                chat_id=chat_id,
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    
    elif query.data == "back_to_main":
        welcome_message = """🎯 FreaksServis Bot

Мы создали бот с полезной информацией и навигацией.

Выбирайте услугу → Пишите менеджеру

Просто делаем дело. ✅

Всем профитов! 💰"""
        await context.bot.send_message(
            chat_id=chat_id,
            text=welcome_message,
            reply_markup=get_main_menu()
        )


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    print("🤖 FreaksServis бот запущен!")
    application.run_polling()


if __name__ == '__main__':
    main()
