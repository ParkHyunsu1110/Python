for i in range(10):
    try:
        print(10/i)
##    except ZeroDivisionError:
##        print("nonono")
    except ZeroDivisionError as e:
        print(e)
