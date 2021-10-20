#!/usr/bin/env python3

"""Bond present value calculator.
This script calculates the present value of bond with following parameters:

"""

import argparse
import sys
import math


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFormatter)

    g = parser.add_argument_group("bond pv settings")
    g.add_argument("--period", metavar="N",
                   default=1,
                   type=float,
                   help="used only in compounding percent - count of coupon payments per year; 0 means continuous compounding")


    parser.add_argument("nominal", type=int, help="Nominal of the bond")
    parser.add_argument("percent", type=str, help="Type of coupon counting;" \
                                                      "'simple' or 's' counts a coupon as nominal * coupon;" \
                                                      "'comp' or 'c' counts a coupon as a compounding percentages with a 'period' payments per year")
    parser.add_argument("coupon", type=float, help="Coupon value in percent to nominal")
    parser.add_argument("years", type=int, help="The number of years till the nominal payment")
    parser.add_argument("disc_rate", type=float, help="Discount rate")


    return parser.parse_args(args)


options = parse_args()
nominal = options.nominal
percent = options.percent
coupon = options.coupon
years = options.years
disc_rate = options.disc_rate
period = options.period


present_value = 0
discount = 1 + disc_rate


present_value = 0
discount = 1 + disc_rate
for i in range(years):
    if percent == 'simple' or percent == 's':
        present_value += coupon * nominal / discount
    elif percent == 'comp' or percent == 'c':
        if period == 0:
            present_value += nominal * (math.exp(coupon) - 1) / discount
        else:
            present_value += nominal * ((1 + coupon / period) ** period - 1) / discount
    else:
        raise ValueError("percent must be 'comp', 'c', 'simple' or 's'")

    if i == years - 1:
        present_value += nominal / discount
    discount *= 1 + disc_rate

print(present_value)

