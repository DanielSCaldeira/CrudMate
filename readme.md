# CrudMate - Gerador de CRUD com IA

O **CrudMate** é uma ferramenta automatizada para geração de componentes de CRUD (Create, Read, Update, Delete) para aplicações web. Ele utiliza entradas fornecidas pelo usuário para criar arquivos de back-end e front-end, otimizando o desenvolvimento de sistemas baseados em entidades.

## Geração Baseada em Modelo de Código com IA

O grande diferencial do CrudMate é o uso de **Inteligência Artificial** para gerar o código com base em um modelo de referência. A IA analisa os padrões do projeto e gera os componentes seguindo a estrutura definida pela equipe de desenvolvimento. Isso garante consistência, agilidade e menor margem de erro.

## Funcionalidades

O CrudMate suporta a geração dos seguintes componentes:

### Back-End
- **Model**: Classe de modelo em C#.
- **DTO**: Objeto de transferência de dados.
- **Service**: Classe de serviço para lógica de negócios.
- **API**: Controlador para endpoints REST.
- **XML Mapping**: Arquivo de mapeamento NHibernate.

### Front-End
- **Service JS**: Serviço AngularJS para comunicação com a API.
- **Router JS**: Configuração de rotas AngularJS.
- **Páginas HTML e JS**:
  - Visualizar
  - Incluir
  - Consultar
  - Alterar

## Estrutura do Projeto

```
├── arquivos/            # Diretório onde os arquivos gerados são salvos
│   ├── back-end/        # Arquivos gerados para o back-end
│   └── front-end/       # Arquivos gerados para o front-end
├── functions/           # Funções principais para geração de código
│   ├── back_end/        # Funções específicas para o back-end
│   ├── front_end/       # Funções específicas para o front-end
│   └── utils/           # Utilitários auxiliares
├── main.py              # Arquivo principal para execução do gerador
├── consts.py            # Constantes e mapeamentos de funções
├── requirements.txt     # Dependências do projeto
└── .env                 # Configurações de ambiente
```

## Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- Instalar dependências do projeto:
```bash
pip install -r requirements.txt
```

### Execução
Execute o arquivo principal:
```bash
python main.py
```

Escolha as opções desejadas no menu interativo.
Insira as informações solicitadas para cada componente.
Os arquivos gerados serão salvos no diretório `arquivos/`.

## Configuração da API da OpenAI

O arquivo `.env` é utilizado para armazenar variáveis de ambiente que configuram o comportamento do projeto. No caso do CrudMate, ele contém as seguintes configurações relacionadas à API da OpenAI:

### Estrutura do `.env`
```
OPENAI_API_KEY=sk-<sua-chave-secreta>
OPENAI_MODEL=gpt-<versão-do-modelo>
```

### Explicação das Variáveis
- **OPENAI_API_KEY**: Chave secreta fornecida pela OpenAI para autenticação.
- **OPENAI_MODEL**: Versão do modelo GPT a ser utilizada (ex: `gpt-3.5-turbo`, `gpt-4`).

**Importante:** Certifique-se de que o arquivo `.env` não seja compartilhado publicamente.

## Exemplo de Uso

Ao selecionar a opção **Gerar Todas opções**, forneça o script SQL da tabela, como no exemplo:

```sql
CREATE TABLE core.Produto (
    Id INT PRIMARY KEY,
    Nome VARCHAR(100),
    Preco DECIMAL(10,2),
    Estoque INT
);
```

O CrudMate criará automaticamente todos os componentes necessários para a entidade `Produto`.

## Personalização

- As mensagens e prompts podem ser ajustados no arquivo `consts.py`.
- A estrutura e estilo do código gerado seguem um modelo base que pode ser modificado conforme o padrão da sua equipe.

## Contribuição

Contribuições são bem-vindas!

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
```bash
git checkout -b minha-feature
```
3. Faça commit das suas alterações:
```bash
git commit -m "Minha nova feature"
```
4. Envie suas alterações:
```bash
git push origin minha-feature
```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).