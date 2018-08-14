import const_1
import main_functions
import constants
import random

"""
def game1_stage1(bot, message):
    if message.text == const_1.answers[1]:
        main_functions.answering_phrase(bot, message, const_1.phrases[2])
        main_functions.answering_phrase(bot, message, const_1.questions[2])
        return 1
    elif message.text == constants.button_hint:
        main_functions.answering_phrase(bot, message, const_1.hints[1])
        return 0
    elif message.text == constants.button_replay:
        main_functions.check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        main_functions.answering_phrase(bot, message, const_1.questions[1])
        return 0
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, random.choice(constants.wa))
        return 0
"""


def game1_stage0(bot, message):
    if message.text == constants.button_play:
        main_functions.answering_phrase(bot, message, const_1.phrases[1])
        main_functions.in_quest_markup(bot, message, const_1.questions[1])
        return 1
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, constants.unreal_menu_point)
        return 0


def game1_stage1(bot, message):
    t = main_functions.answer_transformation(message.text)
    if t == const_1.answers[1]:
        main_functions.answering_phrase(bot, message, const_1.phrases[2])
        main_functions.answering_phrase(bot, message, const_1.questions[2])
        return 1
    elif message.text == constants.button_hint:
        main_functions.answering_phrase(bot, message, const_1.hints[1])
        return 0
    elif message.text == constants.button_replay:
        main_functions.check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        main_functions.answering_phrase(bot, message, const_1.questions[1])
        return 0
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, random.choice(constants.wa))
        return 0


def game1_stage2(bot, message):
    t = main_functions.answer_transformation(message.text)
    if t == const_1.answers[2]:
        main_functions.answering_phrase(bot, message, const_1.phrases[3])
        main_functions.answering_phrase(bot, message, const_1.questions[3])
        return 1
    elif message.text == constants.button_hint:
        main_functions.answering_phrase(bot, message, const_1.hints[2])
        return 0
    elif message.text == constants.button_replay:
        main_functions.check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        main_functions.answering_phrase(bot, message, const_1.questions[2])
        return 0
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, random.choice(constants.wa))
        return 0



def game1_stage3(bot, message):
    t = main_functions.answer_transformation(message.text)
    if t == const_1.answers[3]:
        main_functions.answering_phrase(bot, message, const_1.phrases[4])
        main_functions.answering_phrase(bot, message, const_1.questions[4])
        return 1
    elif message.text == constants.button_hint:
        main_functions.answering_phrase(bot, message, const_1.hints[3])
        return 0
    elif message.text == constants.button_replay:
        main_functions.check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        main_functions.answering_phrase(bot, message, const_1.questions[3])
        return 0
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, random.choice(constants.wa))
        return 0


def game1_stage4(bot, message):
    t = main_functions.answer_transformation(message.text)
    if t == const_1.answers[4]:
        main_functions.answering_phrase(bot, message, const_1.phrases[5])
        main_functions.answering_phrase(bot, message, const_1.questions[5])
        return 1
    elif message.text == constants.button_hint:
        main_functions.answering_phrase(bot, message, const_1.hints[4])
        return 0
    elif message.text == constants.button_replay:
        main_functions.check_to_reply_inline_markup(bot, message, constants.answering_before_reply_quest)
        return 0
    elif message.text == constants.button_repeat_question:
        main_functions.answering_phrase(bot, message, const_1.questions[4])
        return 0
    elif message.text == constants.button_change_choice:
        # МБ ВСТАВИТЬ КАКУЮ-ТО ФРАЗУ ДЛЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ОТСЮДА
        return -1
    else:
        # Вставаить тут рандомный выбор из фраз неправильных ответов
        main_functions.answering_phrase(bot, message, random.choice(constants.wa))
        return 0



def to_usual_stage(bot, message, n):
    return main_functions.usual_stage(bot, message, const_1.answers[n - 1], const_1.phrases[n],
                                const_1.questions[n], const_1.hints[n - 1], const_1.questions[n - 1])


def game1(bot, message, stage):
    if stage == 0:
        # a = game1_stage1(message)
        a = game1_stage0(bot, message)
        return main_functions.change_stage(a, 1, 0)
    if stage == 1:
        # a = game1_stage1(message)
        a = to_usual_stage(bot, message, 2)
        return main_functions.change_stage(a, 2, 1)
    elif stage == 2:
        a = to_usual_stage(bot, message, 3)
        return main_functions.change_stage(a, 3, 2)
    elif stage == 3:
        a = to_usual_stage(bot, message, 4)
        return main_functions.change_stage(a, 4, 3)
    elif stage == 4:
        a = to_usual_stage(bot, message, 5)
        return main_functions.change_stage(a, 5, 4)
    elif stage == 5:
        a = to_usual_stage(bot, message, 6)
        return main_functions.change_stage(a, 6, 5)
    elif stage == 6:
        a = to_usual_stage(bot, message, 7)
        return main_functions.change_stage(a, 7, 6)
