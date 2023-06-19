from utils import SQL

sql = SQL('root', 'Gatitcha1', 'guilherme')
cmd = "SELECT * FROM guilherme.login ;"
cs = sql.consultar(cmd, [])
result = cs.fetchone()
print(result)