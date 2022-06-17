import pytcm


outs, errs = pytcm.execute('ls', [pytcm.Flag('-a', True)])

print(outs)
print(errs)