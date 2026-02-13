# 🏦 Sistema Bancário em Python

> Sistema bancário orientado a objetos com gestão de contas, usuários e transações — desenvolvido como desafio da **Digital Innovation One (DIO)** com foco em **POO** e **regras de negócio**.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/OOP-Oriented-blue?style=for-the-badge)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🎯 Sobre o Projeto

Sistema bancário CLI (Command-Line Interface) que simula operações bancárias reais com múltiplos usuários, contas e transações. Implementa regras de negócio, validações e persistência de estado durante a sessão.

**Desenvolvido como progressão de desafios da DIO**, demonstrando evolução de código através de **3 versões**, cada uma adicionando complexidade e boas práticas de programação.

---

## ✨ Funcionalidades

### Operações Implementadas

- 💰 **Depósito** — Adicionar valores à conta
- 💸 **Saque** — Retirar valores com validações de limite
- 📊 **Extrato** — Visualizar histórico completo de transações
- 👤 **Cadastro de Usuários** — Criar novos usuários no sistema
- 🏦 **Criação de Contas** — Associar contas a usuários existentes
- 📋 **Listagem de Contas** — Visualizar todas as contas cadastradas
- 🔄 **Seleção de Conta** — Escolher conta para operações
- 💵 **Exibição de Saldo** — Consultar saldo atual

---

## 📐 Regras de Negócio

O sistema implementa as seguintes validações e restrições:

### Limites de Saque
- ⚠️ **Máximo de 3 saques** por sessão
- ⚠️ **Valor máximo de R$ 500,00** por saque
- ⚠️ **Saldo insuficiente** bloqueia operação

### Validações Gerais
- ✅ **Valores positivos** — Não permite depósitos ou saques negativos
- ✅ **Numeração automática** — Contas recebem número incremental
- ✅ **Agência fixa** — Todas contas vinculadas à agência "0001"
- ✅ **Múltiplas contas** — Um usuário pode ter várias contas
- ✅ **Histórico completo** — Todas operações registradas no extrato

---

## 🗂️ Estrutura do Projeto

```
DIO-Desafio-Criando-um-Sistema-Bancario-com-Python/
│
├── src/                    # Versão principal (mais recente)
│   └── sistema_bancario.py
│
├── v1.1/                   # Versão 1.1 - Funções refatoradas
│   └── sistema_bancario_v1.1.py
│
├── v0.1/                   # Versão 0.1 - Implementação inicial
│   └── sistema_bancario_v0.1.py
│
├── .gitignore
└── README.md
```

### Evolução das Versões

| Versão | Características | Conceitos Aplicados |
|--------|----------------|---------------------|
| **v0.1** | Implementação básica com funções simples | Funções, loops, condicionais |
| **v1.1** | Refatoração com funções parametrizadas | Modularização, argumentos posicionais/nomeados |
| **src/** | POO completo com classes e métodos | Classes, herança, encapsulamento |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado

### Execução

```bash
# Clone o repositório
git clone https://github.com/rapassos/DIO-Desafio-Criando-um-Sistema-Bancario-com-Python.git

# Entre na pasta
cd DIO-Desafio-Criando-um-Sistema-Bancario-com-Python

# Execute a versão principal
python .\src\sistema_bancario.py

# Ou execute versões anteriores
python v1.1/sistema_bancario_v1.1.py
python v0.1/sistema_bancario_v0.1.py
```

---

## 💻 Exemplo de Uso

### Menu Principal

```
################################################################################
                                 Rapassos Bank
################################################################################
Cliente atual: Nenhum
--------------------------------------------------------------------------------
Menu:
1 - Adicionar cliente
2 - Listar/Selecionar cliente
3 - Adicionar conta
4 - Selecionar Conta
5 - Exibir saldo
6 - Deposito
7 - Saque
8 - Extrato
0 - Sair
Escolha uma opção:
```

### Fluxo de Operação

```bash
# 1. Adicionar cliente / conta
Informe o nome do cliente:João Silva
Informe o CPF do cliente:12345678900

# 2. Listar / selecionar cliente
Informe o nome do cliente:João Silva
Informe o CPF do cliente:12345678900

# 3. Adiciona conta
(cria conta para o cliente selecionado)

# 4. Lista / seleciona conta
Contas:
0001-01 12345678900     João Silva
0002-01 12345678900     João Silva
Informe o número da conta:0002-01

# 5. Exibir saldo
Seu saldo é de R$700.00

# 6. Depositar
Informe o valor do depósito:1000
Depósito realizado com sucesso!

# 7. Saque
Informe o valor do saque:300
Saque realizado com sucesso!

# 8. Extrato
####################################Extrato:####################################
Conta: 0001-01  CPF: 12345678900        Nome: João Silva
--------------------------------------------------------------------------------
13/02/2026 07:26:20     1000.00 Depósito
13/02/2026 07:26:57     300.00  Saque
--------------------------------------------------------------------------------
Seu saldo é de R$700.00
################################################################################
Pressione Enter para continuar...
```

---

## 🧩 Arquitetura (Versão POO)

### Classes Principais

```python
class Banco:
    - Gerencia as regras de negocio
    - Parametriza o sistema
    
class Cliente:
    - Gerencia dados do usuário

class Conta:
    - Controla saldo e histórico

class Operacoes:
    - Registra operações realizadas
    - Mantém histórico completo
    - Valida operações de saque/depósito
```

### Diagrama Conceitual

```
Cliente
  └── possui múltiplas Contas
        └── cada conta tem Transações
              └── Depósito / Saque
```

---

## 📚 Conceitos de Programação Demonstrados

### Fundamentos
- ✅ Variáveis e tipos de dados
- ✅ Estruturas condicionais (if/elif/else)
- ✅ Loops (while, for)
- ✅ Listas e dicionários

### Funções
- ✅ Funções com parâmetros
- ✅ Argumentos posicionais vs. nomeados (keyword-only)
- ✅ Retorno de múltiplos valores

### Orientação a Objetos
- ✅ Classes e instâncias
- ✅ Atributos e métodos
- ✅ Encapsulamento
- ✅ Composição

### Boas Práticas
- ✅ Validação de entrada
- ✅ Tratamento de erros
- ✅ Código modular
- ✅ Nomenclatura clara

---

## 🔮 Próximas Evoluções (Roadmap)

Possíveis melhorias para versões futuras:

- [ ] **Persistência de dados** — Salvar em JSON ou SQLite
- [ ] **Múltiplos tipos de conta** — Poupança, Corrente
- [ ] **Transferências entre contas**
- [ ] **Juros e rendimentos**
- [ ] **Autenticação** — Login com senha
- [ ] **Interface gráfica** — GUI com tkinter
- [ ] **API REST** — Backend com Flask/FastAPI
- [ ] **Testes unitários** — Pytest para validações
- [ ] **Logs de auditoria** — Registro de todas operações

---

## 🎓 Contexto de Aprendizado

### Desafio DIO

Este projeto foi desenvolvido como parte do desafio **"Criando um Sistema Bancário com Python"** da Digital Innovation One, que propõe:

1. **Versão Inicial** — Implementar operações básicas com funções
2. **Refatoração** — Melhorar código com parametrização
3. **POO** — Reescrever usando Programação Orientada a Objetos

### Objetivos Alcançados

- ✅ Aplicar conceitos de POO em projeto real
- ✅ Implementar regras de negócio complexas
- ✅ Praticar refatoração e evolução de código
- ✅ Validar entrada de dados e tratar casos extremos
- ✅ Organizar código em versões progressivas

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3.12.1
- **Paradigma:** Orientação a Objetos
- **Interface:** CLI (Command-Line Interface)
- **Ambiente:** Linux (compatível com Windows/macOS)

---

## 👤 Autor

**Rafael Passos Guimarães**

Full-Stack Developer | Python • Java • JavaScript | 15+ anos em TI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rapassos)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rapassos)
[![GitLab](https://img.shields.io/badge/GitLab-FCA121?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/rapassos)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🔗 Links Úteis

- [Digital Innovation One](https://web.dio.me/)
- [Documentação Python](https://docs.python.org/3/)
- [POO em Python - Real Python](https://realpython.com/python3-object-oriented-programming/)

---

> 💡 **Reflexão:** Este projeto demonstra a importância da evolução contínua de código. A progressão de v0.1 (código procedural) → v1.1 (funções modulares) → src (POO completo) reflete o caminho natural de aprendizado em desenvolvimento de software — começar simples, refatorar, aplicar padrões.
