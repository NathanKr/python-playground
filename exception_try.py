import traceback


try:
    raise Exception("some exception !!")
except Exception as e:
    print(e)
    traceback.print_exc()


