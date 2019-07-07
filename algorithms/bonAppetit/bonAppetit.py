#!/usr/bin/env python3


def bonAppetit(bill, k, b):
    total = sum(bill)
    accurate = total - bill[k]

    if accurate / 2 != b:
        return int(b - accurate / 2) 
    return 'Bon Appetit'
