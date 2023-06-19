from flask import Flask, render_template, request
from utils import SQL

app = Flask(__name__)
sql = SQL('root', 'Gatitcha1', 'test_1')

@app.route('/')
def login_form():
    return render_template('index1.html')

@app.route('/sing_up')
def sing_form():
    return render_template('index2.html')

@app.route('/pass', methods=['GET'])
def take_login():
    user = request.args.get('user_inserte')
    email = request.args.get('mail')
    phone = request.args.get('phone')
    senha = request.args.get('password')

    cmd = f'''
        INSERT INTO login (senha_login, email_login, nome_login, phone)
        VALUES (%s, %s, %s, %s);
    '''
    cs = sql.executar(cmd, [senha, email, user, phone])
    return render_template('index1.html')


@app.route('/login', methods=['GET'])
def process_login():
    user = request.args.get('user')
    senha = request.args.get('senha')

    # Faça o processamento necessário com os valores recebidos
    # Neste exemplo, vamos apenas retornar os valores dentro de uma função

    def login_data(username, password):
        query = f"SELECT id_login FROM login WHERE nome_login = %s AND senha_login = %s"
        cs = sql.consultar(query, [username, password])
        result = cs.fetchone()
        if result:
            return render_template('index.html')
        else:
            return render_template('index1.html')

    result = login_data(user, senha)
    return result

@app.route('/go')
def process():
  return render_template('index.html', nome="")

  # Faça o processamento necessário com os valores recebidos
  # Neste exemplo, vamos apenas retornar os valores dentro de uma função

  # banco = bd.SQL("root", "art88043101", "test_1")
  # comando = "select * from Automoveis ORDER BY  Modelo;"
  # cs = banco.consultar(comando, [])

  # def login_data(username, password):
  #   banco = bd.SQL("root", "art88043101", "test_1")
  #   comando = f"SELECT id_login FROM login WHERE nome_login = %s AND senha_login = %s"
  #   cs = banco.consultar(comando, [username, password])
  #
  #   if result:
  #     return render_template('teste.html', dados=dados)
  #   else:
  #     return render_template('.html')
  #
  # result = login_data(user, senha)
  # return result

@app.route('/select_a')
def a():
  comando = "SELECT DISTINCT modelo, ano, marca FROM automoveis WHERE marca = 'Toyota' ORDER BY ano ASC;"
  cs = sql.consultar(comando, [])
  dados = ""
  for (modelo, ano,marca) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Modelo : {}</p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(modelo,modelo ,ano,marca)
  return render_template('accordion.html', dados = dados)

@app.route('/select_a2')
def a2():
  comando = """
  SELECT contato, sigla
FROM agencia
WHERE nome LIKE 'A%'
ORDER BY sigla ASC;
  """
  cs = sql.consultar(comando, [])
  dados = ""
  for (contato, sigla) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>sigla : {}</p>
                            <p>contato : {} </p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(contato, sigla,contato)
  return render_template('accordion.html', dados = dados)

@app.route('/select_a3')
def a3():

  comando = """
  SELECT nome, salario
FROM pessoa_fisica
WHERE salario > 1000
ORDER BY salario DESC;
  """
  cs = sql.consultar(comando, [])
  dados = ""
  for (nome, salario) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>nome : {}</p>
                            <p>salario : {} </p>
                          </td>
                      </table>
                  </div>
               '''.format(nome, salario)
  return render_template('accordion.html', dados = dados)

@app.route('/select_b')
def b():
  comando = """SELECT pf.Nome AS Nome_Pessoa, ag.Sigla AS Sigla_Agencia
FROM Pessoa_Fisica pf
JOIN Contrata c ON pf.CPF = c.fk_Pessoa_Fisica_CPF
JOIN Agencia ag ON c.fk_Agencia_CNPJ = ag.CNPJ
ORDER BY pf.Nome;"""
  cs = sql.consultar(comando, [])
  dados = ""
  for (Nome_Pessoa,Sigla_Agencia) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Nome Pessoa: {}</p>
                            <p>Sigla Agencia : {}</p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Sigla_Agencia,Nome_Pessoa,Sigla_Agencia)
  return render_template('accordion.html', dados = dados)


@app.route('/select1')
def accordion():
  comando = "select * from Automoveis ORDER BY  Modelo;"
  cs = sql.consultar(comando, [])
  dados = ""
  for (Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Placa : {}</p>
                            <p>Modelo : {}</p>
                            <p>Valor diaria: R$ {}0  </p>
                            <p>Cor : {} </p>
                            <p>Quantidade de Portas : {}</p>
                            <p>chassi : {} </p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Modelo,Placa,Marca,Valor_diaria,Cor,Qtd_Portas,chassi,Ano,Marca)
  return render_template('accordion.html', dados = dados)
  #Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi)

@app.route('/select2')
def select2():
  comando = "select * from Automoveis ORDER BY  Valor_diaria ;"
  cs = sql.consultar(comando, [])
  dados = ""
  for (Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Placa : {}</p>
                            <p>Modelo : {}</p>
                            <p>Valor diaria: R$ {}0  </p>
                            <p>Cor : {} </p>
                            <p>Quantidade de Portas : {}</p>
                            <p>chassi : {} </p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Modelo,Placa,Marca,Valor_diaria,Cor,Qtd_Portas,chassi,Ano,Marca)
  return render_template('accordion.html', dados = dados)
  #Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi)
@app.route('/select3')
def select3():
  comando = "SELECT a.modelo, a.Marca, ag.nome FROM possui p JOIN agencia ag ON ag.CNPJ = p.fk_Agencia_CNPJ JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi ORDER BY a.modelo ASC;"
  cs = sql.consultar(comando, [])
  dados = ""
  for (modelo, Marca, nome ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Nome : {}</p>
                            <p>Modelo : {}</p>
                            <p>Marca : {}</p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(nome, nome, modelo, Marca )
  return render_template('accordion.html', dados = dados)
@app.route('/select4')
def select4():
  comando = "SELECT c.fk_Pessoa_Fisica_CPF AS CPF, s.Agencia_de_seguro, s.valor FROM cliente c JOIN locacao l ON c.Codigo_Cliente = l.fk_Cliente_Codigo_Cliente JOIN seguro s ON l.Codigo_locacao = s.fk_Locacao_Codigo_Locacao ORDER BY s.valor DESC;"
  cs = sql.consultar(comando, [])
  dados = ""
  for (cpf, Agencia_de_seguro, valor ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>CPF : {}</p>
                            <p>Agenciab de seguro : {}</p>
                            <p>valor : R$ {}0</p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Agencia_de_seguro, cpf, Agencia_de_seguro, valor )
  return render_template('accordion.html', dados = dados)
@app.route('/select5')
def select5():

 comando = """SELECT f.nome, a.modelo, ag.Sigla , ag.nome
FROM pessoa_fisica f
JOIN contrata c ON c.fk_Pessoa_Fisica_CPF = f.CPF
JOIN agencia ag ON c.fk_Agencia_CNPJ = ag.CNPJ
JOIN possui p ON ag.CNPJ = p.fk_Agencia_CNPJ
JOIN automoveis a ON p.fk_Automoveis_chassi = a.chassi
ORDER BY f.nome ASC;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (fnome, modelo, Sigla,agnome ) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome F : {}</p>
                           <p>Agenci Nome : {}</p>
                           <p>Sigla : {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(modelo,fnome,agnome , Sigla,)
 return render_template('accordion.html', dados = dados)

@app.route('/select6')
def select6():
 comando = """SELECT ag.nome, l.forma_pagamento, SUM(a.valor_diaria) AS valor_total_diaria
FROM agencia ag
JOIN possui p ON ag.cnpj = p.fk_agencia_cnpj
JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi
JOIN tem t ON t.fk_Automoveis_chassi = a.chassi
JOIN locacao l ON t.fk_Locacao_Codigo_locacao = l.Codigo_locacao
GROUP BY ag.nome, l.forma_pagamento
ORDER BY ag.nome ASC;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (agnome, forma_pagamento, valor_total_diaria ) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome F : {}</p>
                           <p>Forma Pagamento : {}</p>
                           <p>valor Total Diaria : R${}0</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(agnome,agnome, forma_pagamento, valor_total_diaria )
 return render_template('accordion.html', dados = dados)

@app.route('/select7')
def select7():
 comando = """SELECT ag.nome, f.nome, a.modelo, r.data_retira, l.preco
FROM agencia ag
JOIN retirada r ON ag.cnpj = r.fk_agencia_cnpj
JOIN locacao l ON r.fk_locacao_codigo_locacao = l.codigo_locacao
JOIN cliente c ON l.fk_cliente_codigo_cliente = c.codigo_cliente
JOIN pessoa_fisica f ON c.fk_Pessoa_Fisica_CPF = f.CPF
JOIN tem t ON t.fk_Locacao_Codigo_locacao = l.Codigo_locacao
JOIN automoveis a ON t.fk_Automoveis_chassi = a.chassi
ORDER BY ag.nome ASC;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (agnome, fnome, modelo, data_retira, preco) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome AG : {}</p>
                           <p>Nome F: {}</p>
                           <p>data_retira: {} </p>
                           <p>Preco: R${}0 </p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format( modelo,agnome, fnome, data_retira, preco)
 return render_template('accordion.html', dados = dados)

@app.route('/select81')
def select81():

 comando = """SELECT ag.nome, COUNT(a.chassi) AS quantidade
 FROM agencia ag
 JOIN possui p ON ag.cnpj = p.fk_agencia_cnpj
 JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi
 WHERE a.status = 1
 GROUP BY ag.nome;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (agnome, quantidade) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome AG : {}</p>
                           <p>Quantidade: {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(agnome,agnome, quantidade)
 return render_template('accordion.html', dados = dados)

@app.route('/select82')
def select82():
 comando = """SELECT ag.nome, AVG(pf.salario) AS media_salario
 FROM agencia ag
 JOIN contrata c ON ag.cnpj = c.fk_agencia_cnpj
 JOIN pessoa_fisica pf ON c.fk_pessoa_fisica_cpf = pf.cpf
 GROUP BY ag.nome;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (agnome, media_salario) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Media Salario : {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(agnome, media_salario)
 return render_template('accordion.html', dados = dados)


@app.route('/select83')
def select83():
 comando = """SELECT p.nome, COUNT(l.codigo_locacao) AS quantidade_locacoes, SUM(l.preco) AS total_gasto
 FROM cliente c
 JOIN locacao l ON c.codigo_cliente = l.fk_cliente_codigo_cliente
 JOIN pessoa_fisica p ON c.fk_Pessoa_Fisica_CPF = p.CPF
 GROUP BY p.nome;"""
 cs = sql.consultar(comando, [])
 dados = ""
 for (Pnome, quantidade_locacoes, total_gasto) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome  : {}</p>
                           <p>Quantidade Locacoes: {}</p>
                           <p>data_retira: {} </p>
                           <p>Total Gasto: R${}0 </p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(Pnome, quantidade_locacoes, total_gasto)
 return render_template('accordion.html', dados = dados)


app.run(debug=True)

