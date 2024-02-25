#!/usr/bin/python3


def remove_char_at(stru, n):
        if n < 0:
            return stru
        copy_of_stru = stru[:n] + stru[n+1:]
        return copy_of_stru
