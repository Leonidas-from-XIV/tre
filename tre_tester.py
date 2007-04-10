#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Testing module for TRE
"""

from tre import *

preg = byref(regex_t())

result = libtre.regcomp(preg, r'a[0-9]a', 1)
print 'reg compile result:', reg_errcode_t[result]

pmatch = (regmatch_t*5)()
nmatch = c_size_t(5)
test_st = tmp_str = 'bcda7aefga8ah'
offset = 0

matches = []
while True:
    res = libtre.regexec(preg, tmp_str, nmatch, pmatch, 0)
    if reg_errcode_t[res] != 'REG_OK':
        print 'Error in regexec', reg_errcode_t[res]
        break

    m = []
    for match in pmatch:
        if match.rm_so != -1:
            m.append((match.rm_so, match.rm_eo))
    matches.append(m)

    # search on after the match
    tmp_str = tmp_str[match.rm_eo:]
    offset += match.rm_eo

print matches
libtre.regfree(preg)
for match in matches:
    for start, end in match:
        print test_st[start:end]

# new API
print 'Using high level API'
pattern = compile('a([0-9])a')
print pattern.findall('bcda7aefga8ah')
