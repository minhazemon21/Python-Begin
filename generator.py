def remote_control_next():
    yield "CNN"
    yield "ESPN"
itr = remote_control_next()
print(itr)
a = next(itr)
print(a)
for emon in remote_control_next():
    print(emon)