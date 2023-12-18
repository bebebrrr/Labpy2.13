#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def symbol(a, b):
    def stroke(s):
        s.replace(a, b)
    return stroke
