import telegram
import constants
import random
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def log(message, answer):
    print("\n ---------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))
    print(answer)


def answer_transformation(answer):
    answer = answer.strip().lower()
    return answer


def main_menu_markup(bot, message, answer):
    user_markup = [[constants.button_choose_quest, constants.button_info],
                   [constants.button_feedback, constants.button_support]]
    bot.send_message(message.from_user.id, answer,
                     reply_markup = ReplyKeyboardMarkup(user_markup, True))
    log(message, answer)


def answering_phrase(bot, message, answer):
    bot.send_message(message.from_user.id, answer)
    log(message, answer)


def quest_menu_markup(bot, message, answer):
    """ТУКСТ ДУБЛИРОВАН В ТТ, ЭТО НАДО НЕ ЗАБЫТЬ!!!!!!!!!!!!!!!!!"""
    user_markup = [[constants.name_game1], [constants.name_game2, constants.name_game3],
                   [constants.button_back]]
    bot.send_message(message.from_user.id, answer, reply_markup=ReplyKeyboardMarkup(user_markup, True))
    log(message, answer)


def in_quest_markup(bot, message, answer):
    user_markup = [[constants.button_hint, constants.button_replay],
                   [constants.button_change_choice, constants.button_repeat_question]]
    # user_markup.row(constants.button_repeat_question)
    bot.send_message(message.from_user.id, answer, reply_markup=ReplyKeyboardMarkup(user_markup, True))
    log(message, answer)


def check_to_reply_inline_markup(bot, message, answer):
    keyboard = [[InlineKeyboardButton("Да", callback_data=constants.inline_button_yes_to_reply),
                 InlineKeyboardButton("Нет", callback_data=constants.inline_button_no_to_reply)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # keyboard.add(callback_button1)
    bot.send_message(message.chat.id, answer, reply_markup=reply_markup)


def change_stage(result, next_stage, now_stage):
    if result == 1:
        return next_stage
    elif result == 0:
        return now_stage
    elif result == 2:
        return 0
    elif result == -1:
        return -1


def usual_stage(bot, message, answer, next_phrase, next_question, hint, current_question):
    if answer_transformation(message.text) in answer:
        answering_phrase(bot, message, next_phrase)
        answering_phrase(bot, message, next_question)
        return 1
    elif message.text == constants.button_hint:
        answering_phrase(bot, message, hint)
        return 0
    elif message.text == constants.button_replay:
        check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        answering_phrase(bot, message, current_question)
        return 0
    elif message.text == constants.button_change_choice:
        """МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА"""
        return -1
    else:
        answering_phrase(bot, message, random.choice(constants.wa))
        return 0
