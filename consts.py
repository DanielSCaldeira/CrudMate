from functions.back_end.gerar_api import gerar_api
from functions.back_end.gerar_dto import gerar_dto
from functions.back_end.gerar_model import gerar_model
from functions.back_end.gerar_service import gerar_service
from functions.back_end.gerar_xml_mapping import gerar_xml_mapping
from functions.front_end.pagina.alterar import gerar_alterar_js
from functions.front_end.pagina.consultar import gerar_consultar_html, gerar_consultar_js
from functions.front_end.pagina.incluir import gerar_incluir_html, gerar_incluir_js
from functions.front_end.pagina.visualizar import gerar_visualizar_html, gerar_visualizar_js
from functions.front_end.scripts.router import gerar_router_js
from functions.front_end.scripts.service import gerar_service_js
from functions.entidade import identificar_entidade_funcoes_service, identificar_entidade_model
from functions.gerar_todos import gerar_todos_componentes
from typing import Callable, Dict, List, Union

# Mapping between option labels and generator functions
GeneratorFunc = Callable[[str], Union[str, None]]
PROMPTDEFAULTMENSAGEMENTIDADE = """
    ex: 
    {
        "Entidade": "Produto",
        "Propriedades": [""id: int", "nome: string", "preco: decimal"]
    }"""
PROMPTDEFAULTMENSAGEMSERVICE = """
    ex:
    {
        "Service": "ProdutoService",
        "Funcoes": ["incluirProduto", "alterarProduto", "consultarProduto", "visualizarProduto"]
    }"""
UNIPROMPTDEFAULTMENSAGEMSERVICE = f"Entidade :\n{PROMPTDEFAULTMENSAGEMSERVICE}\nService:\n{PROMPTDEFAULTMENSAGEMENTIDADE}"
MENSAGEMDEFAULTENT = f"Informe a entidade. {PROMPTDEFAULTMENSAGEMENTIDADE}"
MENSAGEMDEFAULTUNIAO = f"Informe a entidade. {UNIPROMPTDEFAULTMENSAGEMSERVICE}"

OPTION_FUNCTIONS: Dict[str, GeneratorFunc] = {
    # Todas as opções (geração completa)
    "🚀 Gerar Todas opções": gerar_todos_componentes,
    # Back-End
    "🏗️ Model (Back-End)": gerar_model,
    "🧩 DTO (Back-End)": gerar_dto,
    "🛠️ Service (Back-End)": gerar_service,
    "🔌 API (Back-End)": gerar_api,
    "🗂️ XML Mapping (NHibernate)": gerar_xml_mapping,

    # Front-End Scripts
    "🖥️ Service JS": gerar_service_js,
    "🖥️ Router JS": gerar_router_js,

    # Front-End Pages
    "📝 Visualizar HTML": gerar_visualizar_html,
    "🖥️ Visualizar JS": gerar_visualizar_js,
    "📝 Incluir HTML": gerar_incluir_html,
    "🖥️ Incluir JS": gerar_incluir_js,
    "📝 Consultar HTML": gerar_consultar_html,
    "🖥️ Consultar JS": gerar_consultar_js,
    "🖥️ Alterar JS": gerar_alterar_js,
}
# Prompts for each function
PROMPTS: Dict[str, str] = {
    "🚀 Gerar Todas opções": "Forneça o script SQL da tabela (CREATE TABLE)",
    "🏗️ Model (Back-End)": MENSAGEMDEFAULTENT,
    "🧩 DTO (Back-End)": MENSAGEMDEFAULTENT,
    "🛠️ Service (Back-End)": MENSAGEMDEFAULTENT,
    "🔌 API (Back-End)": MENSAGEMDEFAULTENT,
    "🗂️ XML Mapping (NHibernate)": "Forneça o script SQL da tabela (CREATE TABLE)",
    "🖥️ Service JS": MENSAGEMDEFAULTUNIAO,
    "🖥️ Router JS": MENSAGEMDEFAULTUNIAO,
    "📝 Visualizar HTML": MENSAGEMDEFAULTENT,
    "🖥️ Visualizar JS": MENSAGEMDEFAULTUNIAO,
    "📝 Incluir HTML": MENSAGEMDEFAULTENT,
    "🖥️ Incluir JS": MENSAGEMDEFAULTUNIAO,
    "📝 Consultar HTML": MENSAGEMDEFAULTENT,
    "🖥️ Consultar JS": MENSAGEMDEFAULTUNIAO,
    "🖥️ Alterar JS": MENSAGEMDEFAULTUNIAO,
}

################### TESTE ###############################

SQL = """CREATE TABLE core.Produto (
        Id INT PRIMARY KEY,
        Nome VARCHAR(100),
        Preco DECIMAL(10,2),
        Estoque INT
    );
"""
MAPPING = """
        <class name="Produto" table="Produto" schema="core">
            <id name="Id" column="Id">
                <generator class="sequence">
                    <param name="sequence">SQ_Produto</param>
                </generator>
            </id>
            <property name="Nome" column="Nome" />
            <property name="Preco" column="Preco" />
            <property name="Estoque" column="Estoque" />
            </class>
        </hibernate-mapping>
        """
MODEL = """### Model ###
        ```csharp
            using System;
            namespace PortalFinanceiro.Model
            {
                public class Produto : IComparable, IComparable<Produto>
                {
                    public Produto()
                    {
                    }

                    public virtual int? Id { get; set; }
                    public virtual string Nome { get; set; }
                    public virtual decimal Preco { get; set; }
                    public virtual int Estoque { get; set; }

                    public virtual int CompareTo(object obj)
                    {
                        var aux = obj as Produto;
                        if (Id.HasValue)
                        {
                            return aux != null ? Id.Value.CompareTo(aux.Id.Value) : 1;
                        }
                        else
                        {
                            return aux == null || !aux.Id.HasValue ? 0 : -1;
                        }
                    }

                    public virtual int CompareTo(Produto other)
                    {
                        if (Id.HasValue)
                        {
                            return other != null ? Id.Value.CompareTo(other.Id.Value) : 1;
                        }
                        else
                        {
                            return other == null || !other.Id.HasValue ? 0 : -1;
                        }
                    }

                    public override bool Equals(object other)
                    {
                        if (this == other) return true;
                        if (!(other is Produto registro)) return false;
                        if (!registro.Id.HasValue) return false;
                        if (registro.Id != Id) return false;

                        return true;
                    }

                    public override int GetHashCode()
                    {
                        unchecked
                        {
                            int result;
                            result = 29 * Id.GetHashCode();
                            return result;
                        }
                    }
                }
            }"""
API = """### API ###
    ```csharp
    using FuncefEngine.Base;
    using FuncefEngine.Enumeracoes;
    using FuncefEngine.Exceptions;
    using FuncefEngine.Json;
    using FuncefEngine.Models;
    using PortalFinanceiro.Core.Mensageria;
    using PortalFinanceiro.Model;
    using PortalFinanceiro.Service;
    using PortalFinanceiro.Transport;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Linq.Dynamic;
    using System.Web.Mvc;

    namespace PortalFinanceiro.Api.Controllers
    {
        public class ProdutoController : BaseSistemaController
        {
            const string CodigoFuncao = "PFCNFSNC";

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Listar)]
            public ActionResult Index()
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        List<ItemDTO> lstRetorno = service.Listar()
                            .Select(x => new ItemDTO()
                            {
                                Id = x.Id,
                                Nome = x.Nome
                            }).ToList();
                        RetornoJson<List<ItemDTO>> retorno = new RetornoJson<List<ItemDTO>>
                        {
                            resultado = lstRetorno,
                            qtdRegistros = lstRetorno.Count()
                        };
                        return Sucesso(retorno);
                    }
                }
                catch (Exception ex)
                {
                    throw new Exception(string.Format(MensagemErro.MSGE0007, "Listar"), ex);
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Consultar)]
            public ActionResult Consultar(Filtro filtro, ProdutoFiltroDTO pesquisa = null)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        //Retorna a listagem com pesquisa informada pelo usuário
                        IQueryable<Produto> lst = service.Consultar(pesquisa);
                        lst = lst.OrderBy(filtro.sort != null ? $"{filtro.sort.predicate} {(filtro.sort.reverse ? "DESC" : "")}" : "Id DESC");

                        //Efetua paginação e conversão para Lista
                        lst = filtro?.pagination?.start != null && filtro?.pagination?.number != null ? lst.Skip(filtro.pagination.start).Take(filtro.pagination.number) : lst;

                        var lstRetorno = lst.Select(x => x.ToDTO<Produto, ProdutoDTO>())
                            .ToList();

                        //Retorna como Json
                        RetornoJson<List<ProdutoDTO>> retorno = new RetornoJson<List<ProdutoDTO>>
                        {
                            resultado = lstRetorno,
                            qtdRegistros = lst.Count()
                        };
                        return Sucesso(retorno);
                    }
                }
                catch (Exception ex)
                {
                    throw new Exception(string.Format(MensagemErro.MSGE0007, "Consultar"), ex);
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Visualizar)]
            public ActionResult Buscar(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        ProdutoDTO resultado = service.Buscar(id).ToDTO<Produto, ProdutoDTO>();
                        RetornoJson<ProdutoDTO> retorno = new RetornoJson<ProdutoDTO>
                        {
                            resultado = resultado
                        };
                        return Sucesso(retorno);
                    }
                }
                catch (Exception ex)
                {
                    throw new Exception(string.Format(MensagemErro.MSGE0007, "Buscar"), ex);
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Incluir)]
            public ActionResult Incluir(ProdutoDTO registro)
            {
                if (!ModelState.IsValid)
                {
                    throw new CoreException(Erro(ModelState));
                }

                using (ProdutoService service = new ProdutoService())
                {
                    using (var transacao = service.sessao.BeginTransaction())
                    {
                        try
                        {
                            Produto model = registro.ToModel<Produto, ProdutoDTO>(service.sessao);
                            service.sessao.Persist(model);
                            transacao.Commit();
                            return Sucesso("Incluído com sucesso!" + MensagemSucesso.MSGS0001);
                        }
                        catch (Exception ex)
                        {
                            transacao.Rollback();
                            throw new Exception(string.Format(MensagemErro.MSGE0007, "Incluir"), ex);
                        }
                    }
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Alterar)]
            public ActionResult Alterar(ProdutoDTO registro)
            {
                if (!ModelState.IsValid)
                {
                    throw new CoreException(Erro(ModelState));
                }

                using (ProdutoService service = new ProdutoService())
                {
                    using (var transacao = service.sessao.BeginTransaction())
                    {
                        try
                        {
                            Produto model = registro.ToModel<Produto, ProdutoDTO>(service.sessao);
                            service.sessao.Persist(model);
                            transacao.Commit();
                            return Sucesso("Alterado com sucesso!", MensagemSucesso.MSGS0002);
                        }
                        catch (Exception ex)
                        {
                            transacao.Rollback();
                            throw new Exception(string.Format(MensagemErro.MSGE0007, "Alterar"), ex);
                        }
                    }
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Excluir)]
            public ActionResult Excluir(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                    }
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Excluir)]
            public ActionResult Excluir(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                }
            }

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Excluir)]
            public ActionResult Excluir(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)

            [HttpPost]
            [Autorizacao(CodigoFuncao, Permissao.Excluir)]
            public ActionResult Excluir(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
            [Autorizacao(CodigoFuncao, Permissao.Excluir)]
            public ActionResult Excluir(int id)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
            {
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                try
                {
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                    using (ProdutoService service = new ProdutoService())
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                    {
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                        var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "Exclusão");
                        service.Excluir(resultado);
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                        return Sucesso("Excluído com sucesso!" + MensagemSucesso.MSGS0003);
                    }
                }
                catch (Exception ex)
                }
                catch (Exception ex)
                {
                    throw new Exception(string.Format(MensagemErro.MSGE0007, "Excluir"), ex);
                }
            }
        }
    }"""
DTO = """### DTO ###
    ```csharp
    using FuncefEngine.Base;
    using FuncefEngine.Models;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web.Mvc;

    namespace PortalFinanceiro.Transport
    {
        public class ProdutoDTO : BaseDTO<ProdutoDTO, Produto>
        {
            public ProdutoDTO()
            {
            }

            public virtual int? Id { get; set; }
            public virtual string Nome { get; set; }
            public virtual decimal Preco { get; set; }
            public virtual int Estoque { get; set; }
        }
    }"""
