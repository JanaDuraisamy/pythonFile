import cx_Oracle
con=cx_Oracle.connect("system/pass@localhost")
print(con.version)
con.close()