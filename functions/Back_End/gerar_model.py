from functions.back_end.gerar_codigo import gerar_codigo

def gerar_model(mapping_xml):
    prompt = """
using PortalFinanceiro.Model.Enum;
using System;
namespace PortalFinanceiro.Model
{
    public class TipoAtoDecisorio : IComparable, IComparable<TipoAtoDecisorio>
    {
        public TipoAtoDecisorio()
        {
        }        
        public virtual int? Id { get; set; }
        public virtual string Nome { get; set; }
        public virtual bool Ativo { get; set; }
        public virtual TipoDestacamento Tipo { get; set; }        
        public virtual int CompareTo(object obj)
        {
            var aux = obj as TipoAtoDecisorio;
            if (Id.HasValue)
            {
                return aux != null ? Id.Value.CompareTo(aux.Id.Value) : 1;
            }
            else
            {
                return aux == null || !aux.Id.HasValue ? 0 : -1;
            }
        }
        public virtual int CompareTo(TipoAtoDecisorio other)
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
            if (!(other is TipoAtoDecisorio registro)) return false;
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
}

1) Eu preciso de uma classe C# Model com a mesma estrutura baseada no exemplo acima. Use a entidade e suas propriedades abaixo para a construção do arquivo."""
    return gerar_codigo(prompt, mapping_xml)
