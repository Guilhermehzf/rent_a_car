from utils import SQL

sql = SQL('root', 'SENHA', 'DB')
cmd = "SELECT * FROM guilherme.login ;"
cs = sql.consultar(cmd, [])
result = cs.fetchone()
print(result)
