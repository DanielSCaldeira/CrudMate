from functions.back_end.gerar_codigo import gerar_codigo

def gerar_service(model_code):
    prompt = """    
using FuncefEngine.Base;
using FuncefEngine.Enumeracoes;
using FuncefEngine.Exceptions;
using PortalFinanceiro.Core;
using PortalFinanceiro.Model;
using PortalFinanceiro.Transport;
using System;
using System.Linq;

namespace PortalFinanceiro.Service
{
    public class TipoAtoDecisorioService : ServiceBase<TipoAtoDecisorio>
    {
        public TipoAtoDecisorioService()
            : base(Contexto.GetConfiguracao(BancoDados.Tibero))
        {
        }
        public IQueryable<TipoAtoDecisorio> Consultar(TipoAtoDecisorioFiltroDTO registro = null)
        {
            try
            {
                var lista = base.Listar();
                lista = registro.Id.HasValue ? lista.Where(x => x.Id == registro.Id) : lista;
                lista = registro.Nome != null ? lista.Where(x => x.Nome.ToUpper().Contains(registro.Nome.ToUpper())) : lista;
                lista = registro.Ativo.HasValue ? lista.Where(x => x.Ativo == registro.Ativo) : lista;

                var resultado = lista.Select(x => new TipoAtoDecisorio()
                {
                    Id = x.Id,
                    Ativo = x.Ativo,
                    Tipo = x.Tipo,
                    Nome = x.Nome
                });

                return resultado;
            }
            catch (CoreException ex)
            {
                throw ex;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
    }
}    

1) Gere uma classe de SERVICE C# a partir do exemplo acima. Use a entidade e suas propriedades abaixo para a construção do arquivo."""
    return gerar_codigo(prompt, model_code)