import shelve

sh = shelve.open('Timer')
print(list(sh.keys()), list(sh.values()))
sh.close()