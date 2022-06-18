import pytcm

binary = 'python'
opts = [
    pytcm.Flag('--version', True)
]

cmd = pytcm.Command(binary, opts)
cmd.execute()

print(cmd.out)  # Python 3.9.7
print(cmd.err)  #
print(cmd.returncode)  # 0