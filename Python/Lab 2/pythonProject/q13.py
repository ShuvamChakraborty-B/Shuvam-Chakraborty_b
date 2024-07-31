# 13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2
# # and having a common ratio of 3.
# A
# geometric
# sequence is a
# sequence
# of
# numbers
# where
# each
# term
# after
# the
# first is found
# by
# multiplying
# the
# previous
# term
# by
# a
# fixed, non - zero
# number
# called
# the
# common
# ratio.
#
# For
# this
# problem:
#
# Starting
# term(first
# term) is 2.
# Common
# ratio is 3.
# We
# need
# to
# print
# the
# first
# 6
# terms
# of
# this
# sequence.
# To
# find
# each
# term in the
# sequence:
#
# The
# first
# term is given as 2.
# The
# second
# term is
# 2
# ×
# 3
# =
# 6
# 2×3 = 6.
# The
# third
# term is
# 6
# ×
# 3
# =
# 18
# 6×3 = 18.
# The
# fourth
# term is
# 18
# ×
# 3
# =
# 54
# 18×3 = 54.
# The
# fifth
# term is
# 54
# ×
# 3
# =
# 162
# 54×3 = 162.
# The
# sixth
# term is
# 162
# ×
# 3
# =
# 486
# 162×3 = 486.
def geo_sequence(first,ratio,terms):
    current_term=first
    for i in range(terms):
        print(current_term)
        current_term*=ratio


start_term=2
ratio=3
no_of_terms=6
print("The first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3: ")
geo_sequence(start_term,ratio,no_of_terms)
