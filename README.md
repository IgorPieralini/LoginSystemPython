# 🔒 LoginPage - Sistema de Login em Python

Este projeto implementa uma página de login utilizando Python com a biblioteca Tkinter e conexão a um banco de dados MariaDB/MySQL. O objetivo é autenticar usuários utilizando um formulário gráfico, permitindo um login simples e eficaz para sistemas desktop. Após o login bem-sucedido, o sistema redireciona o usuário para a página de cadastro.

## ⚙️ Funcionalidades
- 🔐 Autenticação de usuários através de um formulário gráfico (GUI) com email e senha.
- 🔗 Conexão com banco de dados MariaDB/MySQL para validação dos usuários.
- ⚠️ Tratamento de erros, como falha de conexão com o banco de dados ou credenciais inválidas.
- ➡️ Redirecionamento para a página de cadastro após um login bem-sucedido.

## 📂 Estrutura do Projeto
- **LoginForm**: Classe responsável pela interface gráfica do login, tratamento dos eventos e autenticação do usuário.
- **CadastroForm**: Classe responsável pela interface gráfica do cadastro de novos usuários e conexão com o banco de dados para armazenar os dados.

## 🛠️ Requisitos
- 🐍 **Python 3.8+**
- 🐬 **MariaDB/MySQL**
- 📦 **Bibliotecas Python necessárias**:
  - `mysql-connector-python`
  - `tkinter` (já incluída no Python padrão)

Você pode instalar o conector MySQL usando o seguinte comando:
```bash
pip install mysql-connector-python
```

## ⚙️ Configuração do Banco de Dados
1. 🖥️ Inicie o servidor MariaDB/MySQL através do XAMPP ou outra ferramenta.
2. 📊 Crie um banco de dados chamado `pieralini__login`.
3. 📝 Crie uma tabela `users` com os seguintes campos:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100) UNIQUE,
       phone VARCHAR(15),
       adress VARCHAR(255),
       password VARCHAR(100)
   );
   ```
4. ➕ Insira alguns registros de teste para validar o sistema de login.

## ▶️ Como Executar
1. 💻 Certifique-se de que o Python 3 está instalado em seu sistema.
2. ⚙️ Configure o banco de dados conforme as instruções acima.
3. 🐍 Execute o script Python para iniciar a aplicação:
   ```bash
   python login_form.py
   ```

## 📞 Contato
- **Dev**: Igor Pieralini
- ✉️ **Email**: [igorpieralini@gmail.com](mailto:igorpieralini@gmail.com)

Fique à vontade para entrar em contato em caso de dúvidas ou sugestões!

## 🌟 Melhorias Futuras
- 🔒 Implementação de hashing de senha para maior segurança.
- ➕ Adicionar opções de recuperação de senha.
- 🎨 Melhorar a interface gráfica para torná-la mais amigável e responsiva.

