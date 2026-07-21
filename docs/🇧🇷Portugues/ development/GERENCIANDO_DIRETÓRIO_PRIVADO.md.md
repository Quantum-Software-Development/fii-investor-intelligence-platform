# Gerenciando o Diretório `private/`

Este documento explica como utilizar o diretório `private/` e por que alguns comandos Git devem ser executados no terminal, e **não** adicionados ao arquivo `.gitignore`.

<br><br>

## O que é o `.gitignore`?

O arquivo `.gitignore` informa ao Git quais arquivos e diretórios **não devem ser rastreados** pelo controle de versão.

Ele contém apenas regras de exclusão, como:

<br>

```gitignore
private/
.env
venv/
__pycache__/
```

<br>

O `.gitignore` **não executa comandos**. Seu único objetivo é informar ao Git quais arquivos devem ser ignorados.

<br><br>

## Adicionando o diretório `private/`

Caso deseje armazenar arquivos pessoais, experimentos, credenciais ou qualquer outro conteúdo que não deva ser publicado no repositório, adicione o diretório `private/` ao `.gitignore`:

<br>

```bash
echo "private/" >> .gitignore
```

<br>

> [!TIP]
> 
> ### O que esse comando faz?
>
> * Cria a regra `private/` no final do arquivo `.gitignore`.
>  A partir desse momento, novos arquivos criados dentro desse diretório não serão rastreados pelo Git.


<br><br>

## Quando isso não é suficiente?

Se o diretório `private/` **já foi commitado anteriormente**, apenas adicioná-lo ao `.gitignore` não fará o Git parar de rastreá-lo.

Nesse caso, execute:

<br>

```bash
git rm -r --cached private/
```

<br>

### O que esse comando faz?

* Remove o diretório do índice (index) do Git.
* Mantém todos os arquivos intactos no seu computador.
* Apenas interrompe o rastreamento pelo Git.

Nenhum arquivo local é apagado.

<br><br>

## Registrando a alteração

Depois de remover o diretório do controle de versão, registre a mudança:

<br>

```bash
git commit -m "chore: stop tracking private directory"
```

<br>

Esse commit informa que o diretório continuará existindo localmente, mas deixará de fazer parte do repositório.

<br><br>

## Resumo dos comandos

<br>

| Comando                         | Finalidade                                                              |
| ------------------------------- | ----------------------------------------------------------------------- |
| `echo "private/" >> .gitignore` | Adiciona `private/` ao `.gitignore`.                                    |
| `git rm -r --cached private/`   | Remove o diretório do controle de versão sem apagar os arquivos locais. |
| `git commit -m "..."`           | Salva essa alteração no histórico do repositório.                       |


<br><br>

## Boas práticas

* Utilize `private/` para arquivos pessoais, credenciais, testes locais e experimentos.
* Nunca armazene segredos (`.env`, chaves de API, tokens, senhas) no repositório.
* Mantenha o `.gitignore` contendo **apenas regras de exclusão**.
* Execute comandos Git sempre no terminal, nunca dentro do `.gitignore`.

