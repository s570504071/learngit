def safe(obj):
    try:
        ret=float(obj)
        print 111
    except Exception,e:
        ret=str(e)
    except ValueError:
        ret='not'
    return ret
