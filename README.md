# 📝 Projeto Flask com Autenticação e Gerenciamento de Atividades

Este projeto é uma aplicação web feita com **Flask** e **Flask-Login**, utilizando **SQLite** como banco de dados.  
Ela permite autenticação de usuários e o gerenciamento de atividades.

---

## 🚀 Instruções para rodar localmente

1️⃣ Clonar o repositório
```bash
git clone https://github.com/flauber/projeto_psi.git
cd projeto_psi

2️⃣ Criar e ativar o ambiente virtual

No linux:
python3 -m venv venv
source venv/bin/activate

No Windows:
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências

O projeto já possui o arquivo requirements.txt com todas as bibliotecas necessárias.

Basta executar:

pip install -r requirements.txt

4️⃣ Inicializar o banco de dados

Antes de rodar o servidor, é necessário criar as tabelas do banco.
Execute:
python iniciar.py

5️⃣ Rodar a aplicação

Após criar o banco, execute:

python app.py

Por padrão, o Flask roda em http://127.0.0.1:5000.


⚙️ Tecnologias Utilizadas

- Flask

- Flask-Login

- SQLite3

- HTML5 / CSS3

- Jinja2

🛠️ Possíveis Problemas

Ambiente virtual não ativa: verifique se está no diretório do projeto e se executou o comando correto para o seu sistema operacional.

Erro de módulo não encontrado: execute novamente pip install -r requirements.txt.

Banco não encontrado: execute python iniciar.py antes de rodar app.py.


# 📅 Entregas Semanais – Projeto Flask

Este documento serve como controle de progresso do projeto, permitindo registrar quem realizou cada tarefa.

---

## ✅ Semana 1 (04/07 – 10/07)
-  Criação do repositório no GitHub — **Responsável: Flauber Sauan** 
-  Escolha do tema do sistema — **Responsável: Flauber Sauan e Alan Pereira** 
-  Documento de Requisitos Funcionais completo no repositório — **Responsável: Flauber Sauab** 
-  Estrutura inicial do projeto (ambiente virtual, `app.py`, `requirements.txt`) — **Responsável: Flauber Sauan e Alan Pereira** 
-  Configuração inicial do banco SQLite (tabela de usuários) — **Responsável: Alan** 

---

## ✅ Semana 2 (11/07 – 17/07)
-  Implementar autenticação:
  -  Página de registro — **Responsável:*Flauber Sauan * 
  -  Página de login — **Responsável:*Flauber Sauan * 
  -  Senha com hash seguro — **Responsável:*Alan* 
  -  Sessão ou Flask-Login para manter usuário autenticado — *Bruno*:** 
  -  Logout funcional — **Responsável:*Alan* 
-  Templates com `extends`/`includes` para base e navbar — **Flauber Sauan:** 

---

## ✅ Semana 3 (18/07 – 24/07)
-  Implementar CRUD do recurso escolhido:
  -  Criar — **Responsável:*Isaac* 
  -  Listar — **Responsável:*Bruno* 
  -  Editar — **Responsável:*Flauber Sauan * 
  -  Excluir — **Responsável:*Alan Pereira* 
-  Restrição de acesso: cada usuário só pode ver/editar/excluir seus dados — *Todos*:** 

---

## ✅ Semana 4 (25/07 – 31/07)
-  Uso refinado de Flask:
  -  Uso de `request` para formulários/dados — *Todos*:** 
  -  Uso de `redirect` e `url_for` — **Todos:** 
  -  Uso de `make_response` (cookies ou headers customizados) — **Ninguém:** 
-  Tratamento de erros:
  -  Página personalizada para **404** — **Bruno:** 
  -  Página personalizada para **500** — **Isaac:** 

---

## ✅ Semana 5 (01/08 – 13/08)
-  Testes manuais completos — **Todos:** 
-  Estilização básica com CSS ou Bootstrap — **Flauber Sauan, Bruno, Isaac:** 
-  Ajustes finais no código — **Flauber Sauan:** 
-  README bem elaborado:
  -  Instruções para rodar localmente — **Flauber Sauan:** 






