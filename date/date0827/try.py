def safe(obj):
    try:
        ret=float(obj)
        print 111
    except Exception,e:
        ret='bad'
    except ValueError:
        ret='not'
    return ret
