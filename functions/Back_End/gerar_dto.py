from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_dto(service_code):
    prompt = """    
    using FuncefEngine.Base;
    using NHibernate;
    using PortalFinanceiro.Model;
    using PortalFinanceiro.Model.Enum;
    using System.ComponentModel.DataAnnotations;

    namespace PortalFinanceiro.Transport
    {
        public class TipoAtoDecisorioDTO : BaseDTO<TipoAtoDecisorio, TipoAtoDecisorioDTO>
        {

            public TipoAtoDecisorioDTO()
            {
            }
            
            public TipoAtoDecisorioDTO(TipoAtoDecisorio model) : base(model)
            {
                Id = model.Id;
                Nome = model.Nome;
                Ativo = model.Ativo;
                Tipo = model.Tipo;
            }

            public override TipoAtoDecisorio Modelo(ISession sessao)
            {
                TipoAtoDecisorio model;
                if (Id.HasValue)
                {
                    model = sessao.Get<TipoAtoDecisorio>(Id);
                } else {
                    model = new TipoAtoDecisorio();
                }
                
                model.Nome = Nome;
                model.Ativo = Ativo.Value;
                model.Tipo = Tipo.Value;

                return model;
            }
            
            [Display(Name = "Identificador Ato Decisorio")]
            public int? Id { get; set; }

            [Display(Name = "Nome Ato Decisorio")]
            public string Nome { get; set; }

            [Display(Name = "Indicador Ativo")]
            public bool? Ativo { get; set; }

            [Display(Name = "Identificador Tipo Destacam")]
            public TipoDestacamento? Tipo { get; set; }
        }
    }
           
1) Gere a DTO C# de acordo com o exemplo acima. Use a entidade e suas propriedades abaixo para a construção do arquivo."""
    return gerar_codigo(prompt, service_code)