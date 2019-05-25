# -*- coding: utf-8 -*-
# Note: on Windows, use Lucida Console font and
# run chcp 65001 from the command line

from __future__ import print_function, unicode_literals

import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_3, custom_style_2, custom_style_1

import parse
import pretty_print as pp


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


# Question askers

def ask_main():
    main_prompt = {
        'type': 'list',
        'name': 'action',
        'message': 'Select an action:',
        'choices': ['View', 'Update', 'Quit']
    }
    answers = prompt(main_prompt, style=custom_style_1)
    return answers['action']


def ask_view():
    view_prompt = {
        'type': 'list',
        'name': 'action',
        'message': 'Select view:',
        'choices': [{'name': 'View list', 'value': 1},
                    {'name': 'View all details', 'value': 2},
                    {'name': 'View by status', 'value': 3},
                    {'name': 'Go back', 'value': 0}]
    }
    answers = prompt(view_prompt, style=custom_style_1)
    return answers['action']


def ask_update():
    upd_prompt = {
        'type': 'list',
        'name': 'action',
        'message': 'What update do you want to make?',
        'choices': [{'name': 'Add project', 'value': 1},
                    {'name': 'Edit project', 'value': 2},
                    {'name': 'Delete project', 'value': 3},
                    {'name': 'Go back', 'value': 0}]
    }
    answers = prompt(upd_prompt, style=custom_style_1)
    return answers['action']


# Prompt function calls

def main():
    print("\nMain menu:")
    main_menu()


def main_menu():
    """ Prompt user option from main menu """
    action = ask_main()
    if action == "View":
        view()
    elif action == "Update":
        update()
    else:
        print("Bye bye!")


def view():
    action = ask_view()
    if action == 1:  # list
        act.print_projects("list")
        view()
    elif action == 2: # descriptions
        print("TODO")
        view()
    elif action == 3: # status
        act.print_projects("status")
        view()
    elif action == 0:
        main()
    else:
        print("Invalid option!")
        view()

def update():
    action = ask_update()
    if action == "Add project":
        pass
    elif action == "Delete project":
        pass
    elif action == "Edit project":
        pass
    elif action == 0:
        main()
    else:
        print("Invalid option!")
        update()

if __name__ == '__main__':
    print(chr(27) + "[2J")
    act = parse.Activity()
    pp.pprint_headings("Welcome to Side Project Selector!")
    main()
