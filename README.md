# 📝 Projeto Flask com Autenticação e Gerenciamento de Atividades

Este projeto é uma aplicação web desenvolvida com **Flask** e **Flask-Login**, utilizando **SQLite** como banco de dados.  
O sistema permite **autenticação de usuários** e o **gerenciamento de atividades**, servindo como prática dos conceitos de programação para web.

---

## 🚀 Como Rodar Localmente

### 1️⃣ Clonar o repositório
git clone https://github.com/flauber/projeto_psi.git  
cd projeto_psi  

### 2️⃣ Criar e ativar o ambiente virtual
**No Linux:**
- python3 -m venv venv  
- source venv/bin/activate  

**No Windows:**
- python -m venv venv  
- venv\Scripts\activate  

### 3️⃣ Instalar dependências
O projeto já possui o arquivo `requirements.txt` com todas as bibliotecas necessárias:  
- pip install -r requirements.txt  

### 4️⃣ Inicializar o banco de dados
Antes de rodar o servidor, é necessário criar as tabelas:  
- python iniciar.py  

### 5️⃣ Rodar a aplicação
- python app.py  

Por padrão, o Flask roda em:  
👉 http://127.0.0.1:5000  

---

## ⚙️ Tecnologias Utilizadas
- Flask  
- Flask-Login  
- SQLite3  
- HTML5 / CSS3  
- Jinja2  

---

## 🛠️ Possíveis Problemas e Soluções

- **Ambiente virtual não ativa** → Verifique se está no diretório do projeto e execute o comando correto para o seu sistema operacional.  
- **Erro de módulo não encontrado** → Rode novamente `pip install -r requirements.txt`.  
- **Banco não encontrado** → Execute `python iniciar.py` antes de rodar `app.py`.  

---

# 📅 Entregas Semanais – Projeto Flask

Este documento também serve como **controle de progresso** do projeto, registrando quem foi responsável por cada tarefa.

---

## ✅ Semana 1 (04/07 – 10/07)
- Criação do repositório no GitHub — **Responsável: Flauber Sauan**  
- Escolha do tema do sistema — **Responsáveis: Flauber Sauan e Alan Pereira**  
- Documento de Requisitos Funcionais completo no repositório — **Responsável: Flauber Sauan**  
- Estrutura inicial do projeto (`app.py`, `requirements.txt`, ambiente virtual) — **Responsáveis: Flauber Sauan e Alan Pereira**  
- Configuração inicial do banco SQLite (tabela de usuários) — **Responsável: Alan Pereira**  

---

## ✅ Semana 2 (11/07 – 17/07)
- Implementar autenticação:
  - Página de registro — **Responsável: Flauber Sauan**  
  - Página de login — **Responsável: Flauber Sauan**  
  - Senha com hash seguro — **Responsável: Alan Pereira**  
  - Sessão ou Flask-Login para manter usuário autenticado — **Responsável: Bruno**  
  - Logout funcional — **Responsável: Alan Pereira**  
- Templates com `extends`/`includes` para base e navbar — **Responsável: Flauber Sauan**  

---

## ✅ Semana 3 (18/07 – 24/07)
- Implementar CRUD do recurso escolhido:
  - Criar — **Responsável: Isaac**  
  - Listar — **Responsável: Bruno**  
  - Editar — **Responsável: Flauber Sauan**  
  - Excluir — **Responsável: Alan Pereira**  
- Restrição de acesso: cada usuário só pode ver/editar/excluir seus próprios dados — **Todos**  

---

## ✅ Semana 4 (25/07 – 31/07)
- Uso refinado de Flask:
  - Uso de `request` para formulários/dados — **Todos**  
  - Uso de `redirect` e `url_for` — **Todos**  
  - Uso de `make_response` (cookies ou headers customizados) — **(Não implementado)**  
- Tratamento de erros:
  - Página personalizada para **404** — **Responsável: Bruno**  
  - Página personalizada para **500** — **Responsável: Isaac**  

---

## ✅ Semana 5 (01/08 – 13/08)
- Testes manuais completos — **Todos**  
- Estilização básica com CSS ou Bootstrap — **Responsáveis: Flauber Sauan, Bruno e Isaac**  
- Ajustes finais no código — **Responsável: Flauber Sauan**  
- README bem elaborado (instruções para rodar localmente) — **Responsável: Flauber Sauan**  

---

✍️ Desenvolvido por **Flauber Sauan e equipe**
