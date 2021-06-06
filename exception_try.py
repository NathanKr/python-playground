import traceback


try:
    raise Exception("some exception !!")
except Exception as e:
    traceback.print_exc()


print('...')
