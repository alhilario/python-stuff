#! /usr/bin/env python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
	aux = balance - payment
	aux = add_monthly_interest(aux)
	return aux

new_bill = make_payment(bill / 2, bill)
print make_payment(100, new_bill)
