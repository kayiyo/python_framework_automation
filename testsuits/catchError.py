try:
    a = 10
    b = 0
    print a/b
# except (ZeroDivisionError, TypeError, NameError):
#     print "Catch done!"
except Exception as e:
    print('Test Fail.', e)
    print('Test Fail.', format(e))