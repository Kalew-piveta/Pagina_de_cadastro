# Aplicativo de Cadastro de Pessoas

Este é um exemplo de aplicativo web de cadastro de pessoas desenvolvido utilizando Flask, HTML, CSS e Bootstrap. O aplicativo permite que os usuários preencham um formulário com informações pessoais e realiza a validação dos dados de entrada. Os dados são armazenados em um arquivo CSV e uma mensagem de sucesso é exibida ao usuário após o cadastro.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Python 3
- Flask

## Instalação

1. Clone ou faça o download deste repositório para o seu computador.

2. Abra um terminal e navegue até o diretório raiz do projeto.

3. Crie um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando:

   ```shell
   python3 -m venv venv
   ```

4. Ative o ambiente virtual. Dependendo do seu sistema operacional, o comando pode variar. Aqui estão alguns exemplos:

   - macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

   - Windows:

     ```shell
     venv\Scripts\activate
     ```

5. Instale as dependências do projeto executando o seguinte comando:

   ```shell
   pip install -r requirements.txt
   ```

## Uso

1. No diretório raiz do projeto, execute o seguinte comando para iniciar o servidor Flask:

   ```shell
   python app.py
   ```

2. Abra o navegador e acesse o endereço `http://localhost:5000`.

3. Você será redirecionado para a página de cadastro, onde poderá preencher o formulário com as informações solicitadas.

4. Após preencher o formulário e enviar os dados, você será redirecionado para a página inicial e uma mensagem de sucesso será exibida.

5. Os dados de cadastro serão armazenados no arquivo `cadastros.csv` localizado no diretório raiz do projeto.

## Personalização

Você pode personalizar o aplicativo de acordo com suas necessidades. Aqui estão algumas sugestões:

- Modificar o layout e o estilo do formulário no arquivo `templates/cadastro.html`.

- Adicionar mais campos ao formulário no arquivo `templates/cadastro.html` e ajustar a lógica de processamento do formulário no arquivo `main.py`.

- Implementar mais validações de entrada e melhorar as mensagens de erro no arquivo `main.py` e `templates/cadastro.html`.

- Personalizar a página de sucesso no arquivo `templates/success.html` e estilizá-la de acordo com suas preferências.

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork e enviar suas melhorias via pull request.

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).

## Autor

Escrito por Kalew Piveta