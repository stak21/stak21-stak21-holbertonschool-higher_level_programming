#!/usr/bin/python3
""" Function: class_to_json """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure """
    return obj.__dict__
