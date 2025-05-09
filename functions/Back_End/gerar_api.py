from functions.back_end.gerar_codigo import gerar_codigo

def gerar_api(service_code):
    prompt = """    
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
    public class TipoAtoDecisorioController : BaseSistemaController
    {
        const string CodigoFuncao = "PFCNFSNC";

        [HttpPost]
        [Autorizacao(CodigoFuncao, Permissao.Listar)]
        public ActionResult Index()
        {
            try
            {
                using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
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
        public ActionResult Consultar(Filtro filtro, TipoAtoDecisorioFiltroDTO pesquisa = null)
        {
            try
            {
                using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
                {
                    //Retorna a listagem com pesquisa informada pelo usuÃ¡rio
                    IQueryable<TipoAtoDecisorio> lst = service.Consultar(pesquisa);
                    lst = lst.OrderBy(filtro.sort != null ? $"{filtro.sort.predicate} {(filtro.sort.reverse ? "DESC" : "")}" : "Id DESC");

                    //Efetua paginaÃ§Ã£o e conversÃ£o para Lista
                    lst = filtro?.pagination?.start != null && filtro?.pagination?.number != null ? lst.Skip(filtro.pagination.start).Take(filtro.pagination.number) : lst;

                    var lstRetorno = lst.Select(x => x.ToDTO<TipoAtoDecisorio, TipoAtoDecisorioDTO>())
                        .ToList();

                    //Retorna como Json
                    RetornoJson<List<TipoAtoDecisorioDTO>> retorno = new RetornoJson<List<TipoAtoDecisorioDTO>>
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
                using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
                {
                    TipoAtoDecisorioDTO resultado = service.Buscar(id).ToDTO<TipoAtoDecisorio, TipoAtoDecisorioDTO>();
                    RetornoJson<TipoAtoDecisorioDTO> retorno = new RetornoJson<TipoAtoDecisorioDTO>
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
        public ActionResult Incluir(TipoAtoDecisorioDTO registro)
        {
            if (!ModelState.IsValid)
            {
                throw new CoreException(Erro(ModelState));
            }

            using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
            {
                using (var transacao = service.sessao.BeginTransaction())
                {
                    try
                    {
                        TipoAtoDecisorio model = registro.ToModel<TipoAtoDecisorio, TipoAtoDecisorioDTO>(service.sessao);
                        service.sessao.Persist(model);
                        transacao.Commit();
                        return Sucesso("Incluido com sucesso!" + MensagemSucesso.MSGS0001);
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
        public ActionResult Alterar(TipoAtoDecisorioDTO registro)
        {
            if (!ModelState.IsValid)
            {
                throw new CoreException(Erro(ModelState));
            }

            using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
            {
                using (var transacao = service.sessao.BeginTransaction())
                {
                    try
                    {
                        TipoAtoDecisorio model = registro.ToModel<TipoAtoDecisorio, TipoAtoDecisorioDTO>(service.sessao);
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
                using (TipoAtoDecisorioService service = new TipoAtoDecisorioService())
                {
                    var resultado = service.Buscar(id) ?? throw new CoreException(MensagemErro.MSGE0008, "ExclusÃ£o");
                    service.Excluir(resultado);
                    return Sucesso("Excluido com sucesso!" + MensagemSucesso.MSGS0003);
                }
            }
            catch (Exception ex)
            {
                throw new Exception(string.Format(MensagemErro.MSGE0007, "Excluir"), ex);
            }
        }
    }
}

1) Gere um Controller C# de acordo com o exemplo acima, utilizando a classe Service fornecida no exemplo abaixo."""""
    return gerar_codigo(prompt, service_code)