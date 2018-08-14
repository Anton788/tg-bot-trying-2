import main_functions
import constants
import game_1
import const_1
#import bd
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext.dispatcher import run_async
from time import sleep
#import logging

# Enable logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)
#logger = logging.getLogger(__name__)


class Player:
    def __init__(self):
        self.quest_num = 0 # Обозначает номер игры, в которой сейчас участвует игрок. 0 - ни в какой.
        self.id = 0
        self.stages = [0, 0, 0, 0] # 0 номер не трогаем, мб его сделать как quest_num
        self.request = 0 # Обозначает этап общения с ботом. 0 - в квестах. 1-2 - в обратной связи
        self.points = 0


class Game:
    def __init__(self):
        self.player = Player()
        self.players = []


GG = Game()
PP = Player()


def player_in_list(message):
    for p in GG.players:
        if p.id == message.from_user.id:
            return p
    py = Player()
    py.id = message.from_user.id
    GG.players.append(py)
    return py


def num_player_in_list(message):
    for i in range(len(GG.players)):
        if GG.players[i].id == message.from_user.id:
            return i
    py = Player()
    py.id = message.from_user.id
    GG.players.append(py)
    return len(GG.players) - 1


def command_start(bot, update):
    #print(update)
    #ПРОВЕРКА НА НАЛИЧИЕ ИГРОКА В БАЗЕ!!!
#    bd.insert_user(update.message.from_user.id)
    n = num_player_in_list(update.message)
    main_functions.main_menu_markup(bot, update.message, constants.start_message)
    # main_functions.check_to_reply_inline_markup(bot, update.message, constants.button_repeat_question)
    GG.players[n].request = 0


def command_help(bot, update):
    main_functions.answering_phrase(bot, update.message, constants.help_message)


def command_go(bot, update):
    n = num_player_in_list(update.message)
    GG.players[n].quest_num = 0
    GG.players[n].request = -1
    main_functions.quest_menu_markup(bot, update.message, constants.go_message)


def command_rating(bot, update):
    main_functions.answering_phrase(bot, update.message, constants.rating_message)


def command_rules(bot, update):
    main_functions.answering_phrase(bot, update.message, constants.rules_message)


def command_support(bot, update):
    main_functions.answering_phrase(bot, update.message, constants.support_message)


def command_feedback(bot, update):
    n = num_player_in_list(update.message)
    GG.players[n].request = 1
    answer = constants.feedback_message
    bot.send_message(update.message.from_user.id, answer, reply_markup=ReplyKeyboardRemove())
    main_functions.log(update.message, answer)


def command_send_message(bot, update):
    n = num_player_in_list(update.message)
    GG.players[n].request = 3
    bot.send_message(update.message.from_user.id, "Введите код для доступа:")


def _0_request(bot, update, n):
    if update.message.text == constants.button_feedback:
        GG.players[n].request = 1
        answer = constants.feedback_message
        bot.send_message(update.message.from_user.id, answer, reply_markup=ReplyKeyboardRemove())
        main_functions.log(update.message, answer)
    elif update.message.text == constants.button_choose_quest:
        main_functions.quest_menu_markup(bot, update.message, constants.go_message)
        GG.players[n].request = -1
    elif update.message.text == constants.button_info:
        main_functions.answering_phrase(bot, update.message, constants.help_message)
    elif update.message.text == constants.button_support:
        main_functions.answering_phrase(bot, update.message, constants.support_message)
    else:
        main_functions.answering_phrase(bot, update.message, constants.unreal_menu_point)


def _minus1_request(bot, update, n):
    if GG.players[n].quest_num == 0:
        if update.message.text == constants.button_back:
            main_functions.main_menu_markup(bot, update.message, constants.in_main_menu)
            GG.players[n].request = 0
        elif update.message.text == constants.name_game1:
            GG.players[n].quest_num = 1
            if GG.players[n].stages[1] == 0:
                user_markup = [[constants.button_play],
                               [constants.button_change_choice]]
                # user_markup.row(constants.button_repeat_question)
                bot.send_message(update.message.from_user.id, const_1.phrases[0], reply_markup=ReplyKeyboardMarkup(user_markup, True))
                main_functions.log(update.message, const_1.phrases[0])
                #GG.players[n].stages[1] = 1
                # main_functions.in_quest_markup(bot, update.message, const_1.questions[0])
            else:
                main_functions.in_quest_markup(bot, update.message, constants.after_stopping)
                main_functions.in_quest_markup(bot, update.message, const_1.questions[GG.players[n].stages[1] - 1])
        elif update.message.text == constants.name_game2:
            main_functions.quest_menu_markup(bot, update.message, constants.in_development)
        elif update.message.text == constants.name_game3:
            main_functions.quest_menu_markup(bot, update.message, constants.in_development)
        else:
            main_functions.answering_phrase(bot, update.message, constants.name_unreal)
    elif GG.players[n].quest_num == 1:
        new_stage = game_1.game1(bot, update.message, GG.players[n].stages[1])
        if new_stage == 0:
            GG.players[n].stages[1] = 0
            user_markup = [[constants.button_play],
                           [constants.button_change_choice]]
            bot.send_message(update.message.from_user.id, const_1.phrases[0],
                             reply_markup=ReplyKeyboardMarkup(user_markup, True))
            main_functions.log(update.message, const_1.phrases[0])
        elif new_stage == -1:
            GG.players[n].quest_num = 0
            main_functions.quest_menu_markup(bot, update.message, constants.go_message)
        else:
            GG.players[n].stages[1] = new_stage
    elif GG.players[n].quest_num == 2:
        pass


def _1_request(bot, update, n):
    # Также создать отдельную таблицу по отзывы
    # Добавить функцию заноса отзывов в таблицу
    # Для обратной связи и отзывов: прописать /feedback
    user_markup = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]
    bot.send_message(update.message.from_user.id, "Благодарю.\nОцени проект по шкале от 1 до 10.",
                     reply_markup=ReplyKeyboardMarkup(user_markup, True))
    GG.players[n].request = 2


def _2_request(bot, update, n):
    t = update.message.text
    if t == '1' or t == '2' or t == '3' or t == '4' or t == '5' or t == '6' or t == '7' or t == '8' or t == '9' or t == '10':
        # to main menu with quests
        GG.players[n].request = 0
        # main_functions.answering_phrase(message, constants.feedback_message_2)
        """ПЕРЕВОДИМ В СТАРТОВОЕ ПОЛОЖЕНИЕ ДЛЯ ОПРЕДЕЛЕННОСТИ"""
        # answer = constants.go_message
        main_functions.main_menu_markup(bot, update.message, constants.feedback_message_2)
        GG.players[n].quest_num = 0
    else:
        user_markup = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]
        bot.send_message(update.message.from_user.id, "Оцени проект по шкале от 1 до 10.",
                         reply_markup=ReplyKeyboardMarkup(user_markup, True))
        GG.players[n].request = 2


def _3_request(bot, update, n):
    t = update.message.text
    if t == "Apple365":
        bot.send_message(update.message.from_user.id, "Введите сообщение для пользователей:")
        GG.players[n].request = 4
    else:
        bot.send_message(update.message.from_user.id, "Неверно")
        GG.players[n].request = 0


def _4_request(bot, update, n):
    for p in GG.players:
        bot.send_message(p.id, update.message.text)
    GG.players[n].request = 0


@run_async
def usual_text(bot, update):
    n = num_player_in_list(update.message)
    if GG.players[n].request == 0:
        _0_request(bot, update, n)
    elif GG.players[n].request == -1:
        _minus1_request(bot, update, n)
    elif GG.players[n].request == 1:
        _1_request(bot, update, n)
    elif GG.players[n].request == 2:
        _2_request(bot, update, n)
    elif GG.players[n].request == 3:
        _3_request(bot, update, n)
    elif GG.players[n].request == 4:
        _4_request(bot, update, n)


def edit_message(bot, update):
    #bot.send_message(chat_id=update.edited_message.chat.id,
    #                      text=constants.after_redacting_message)
    bot.edit_message_text(chat_id=update.edited_message.chat.id,
                          text=constants.after_redacting_message,
                          message_id=update.edited_message.message_id + 1)


def button(bot, update):
    #n = num_player_in_list(update.message)
    query = update.callback_query
    n = num_player_in_list(query)
    if query.data == constants.inline_button_yes_to_reply:
        bot.edit_message_text(text="Принял",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        GG.players[n].stages[GG.players[n].quest_num] = 1
        #print(GG.players[n].quest_num)
        #print(GG.players[n].stages)
        user_markup = [[constants.button_hint, constants.button_replay],
                       [constants.button_change_choice, constants.button_repeat_question]]
        # user_markup.row(constants.button_repeat_question)
        if GG.players[n].quest_num == 1:
            bot.send_message(query.from_user.id, constants.to_reply_quest)
            GG.players[n].stages[1] = 0
            user_markup = [[constants.button_play],
                           [constants.button_change_choice]]
            bot.send_message(query.message.from_user.id, const_1.phrases[0],
                             reply_markup=ReplyKeyboardMarkup(user_markup, True))
            main_functions.log(query.message, const_1.phrases[0])
    elif query.data == constants.inline_button_no_to_reply:
        bot.edit_message_text(text="Тогда остаемся",
                              chat_id=query.message.chat.id,
                              message_id=query.message.message_id)


def main():
    updater = Updater(token=constants.token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', command_start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', command_help)
    dispatcher.add_handler(help_handler)

    go_handler = CommandHandler('go', command_go)
    dispatcher.add_handler(go_handler)

    rating_handler = CommandHandler('rating', command_rating)
    dispatcher.add_handler(rating_handler)

    rules_handler = CommandHandler('rules', command_rules)
    dispatcher.add_handler(rules_handler)

    support_handler = CommandHandler('support', command_support)
    dispatcher.add_handler(support_handler)

    feedback_handler = CommandHandler('feedback', command_feedback)
    dispatcher.add_handler(feedback_handler)

    send_message_handler = CommandHandler('sendforall', command_send_message)
    dispatcher.add_handler(send_message_handler)

    # dispatcher.add_handler(MessageHandler(Filters.text, edit_message, edited_updates=True))

    message_handler = MessageHandler(Filters.text, usual_text)
    dispatcher.add_handler(message_handler)

    dispatcher.add_handler(MessageHandler(Filters.text, edit_message,
                                          edited_updates=True))

    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

    #while True:
    #    print(5)
    #    sleep(1)


if __name__ == '__main__':
    main()


"""
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
                input_message_content=InputTextMessageContent(query.upper())
            )
        )
    bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
"""
