# rent_a_car
index.html: Este arquivo contém o formulário de login. Ele possui campos para user/nome e senha, além de um botão de login. Também contém links para a página de registro (index2.html). O formulário é enviado para a rota /login no método GET.

index2.html: Este arquivo contém o formulário de registro. Ele possui campos para nome de usuário, email, telefone, senha e confirmação de senha. Também contém um botão de registro. O formulário é enviado para a rota /pass no método GET.

login.css: Este arquivo é uma folha de estilo CSS que define a aparência dos formulários de login e registro.

utils.py: Este arquivo contém uma classe chamada SQL, que é responsável por lidar com a interação com o banco de dados MySQL. Ela possui métodos para executar comandos SQL e consultas no banco de dados.

app.py: Este é o arquivo principal do aplicativo Flask. Ele importa as dependências necessárias e cria uma instância do aplicativo Flask. Além disso, ele instancia a classe SQL do arquivo utils.py. O arquivo contém as seguintes rotas:
Rota '/' (rota raiz): Renderiza o template index.html para exibir o formulário de login.

Rota '/sing_up': Renderiza o template index2.html para exibir o formulário de registro.

Rota '/pass' (rota para o registro): Recebe os dados do formulário de registro através do método GET e insere esses dados no banco de dados MySQL usando a classe SQL. Após a conclusão, redireciona para a página de login (index.html).

Rota '/login' (rota para o login): Recebe os dados do formulário de login através do método GET e faz uma consulta ao banco de dados MySQL usando a classe SQL. Se o usuário existir e a senha estiver correta, redireciona para uma página de teste (teste.html). Caso contrário, redireciona novamente para a página de login (index.html).

O aplicativo Flask é executado quando o arquivo app.py é executado diretamente.

Nesta seção do site, você encontrará opções de seleção para visualizar informações provenientes do banco de dados. Além disso, o nome de usuário que realizou o login será exibido no título da guia.

![Captura de tela 2023-06-18 215636](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/08c6ba22-aa4b-48c4-8c04-f74d1afea028)

Nesta seção, você pode notar que ao posicionar o cursor do mouse sobre os retângulos que contêm as perguntas sobre o que deseja fazer, eles mudam de cor para um tom de azul escuro.
![Captura de tela 2023-06-18 215656](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/78f72197-6696-4392-905e-7d15e0806eb7)

Com base nas duas imagens, é possível observar que ao passar o cursor sobre a opção "Retornar ao Menu", o texto e o retângulo nos quais o texto está contido aumentam de tamanho. Além disso, há um efeito de iluminação de fundo que é aplicado ao texto, dando destaque a essa opção específica.  
![Captura de tela 2023-06-18 215719](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/1e503d4a-5337-4623-bd7a-0d625d1c55ec)
![Captura de tela 2023-06-18 215740](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/91cd7feb-e8d9-448e-aa0f-e7a689d29823)

Nesta seção, é possível visualizar informações relevantes sobre o veículo, como o modelo, placa e preço. Essas informações são disponibilizadas de forma clara e acessível, permitindo que você obtenha os dados necessários de maneira rápida e fácil.
![Captura de tela 2023-06-18 220210](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/c5df8aa0-a3de-4dc3-9c3e-64cd668b93ec)

Nesta funcionalidade, o sistema busca informações das agências de seguro e as apresenta, incluindo o nome da agência e o valor correspondente. Isso permite que você tenha acesso às informações atualizadas sobre as diferentes opções de seguro disponíveis, facilitando a comparação e escolha da melhor alternativa para suas necessidades.
![Captura de tela 2023-06-18 220258](https://github.com/Guilhermehzf/rent_a_car/assets/110517542/f4be06f3-2b06-4397-9b5a-d02b5f842468)

É relevante ressaltar que todas as informações fornecidas, desde a criação da conta até os dados apresentados no site, são provenientes de um banco de dados que foi criado e vinculado às páginas web utilizando o framework Flask. Isso garante que os dados sejam armazenados de forma segura e possam ser acessados e atualizados conforme necessário. A integração entre o banco de dados e as páginas web permite uma experiência consistente e confiável para os usuários. 

Integrantes: 
Guilherme Henrique Paes Zioli Fernandes
Arthur Arash Briceno Heidari
Arthur de Resende Graca Gomes
Vinicius Gurgel Serrao
Guilherme Nobrega Gomes Dantas
