import io

def createSQLrecord(tab1, listRecord):
    s = io.StringIO()   # String builder
    s.write(f"INSERT INTO {tab1} VALUES (")
    for i,lis in enumerate(listRecord):
        if i == 0:
            s.write(f"'{lis}'")
        else:
            s.write(f", '{lis}'")
    s.write(");")
    return s.getvalue()

