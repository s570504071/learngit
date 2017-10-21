params=dict(user=user,password=password,database=database,host=host,port=port)
defaults=dict(use_unicode=True,charset='utf-8',collation='utf8_general_ci',autocommit=False)
for k,v in defaults.iteritems():
    params[k]=kw.pop(k,v)
params.update(kw)
params['buffered']=True
