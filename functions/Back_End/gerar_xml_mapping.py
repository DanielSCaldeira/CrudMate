from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_xml_mapping(sql_create):
    assembly = input("Assembly: ")
    namespace = input("Namespace: ")
    
    prompt = f"""Gere um arquivo de mapeamento NHibernate (.hbm.xml) com base no seguinte exemplo: 
    <?xml version="1.0" encoding="utf-8" ?>
    <hibernate-mapping xmlns="urn:nhibernate-mapping-2.2"
        assembly="PortalFinanceiro.Model"
        namespace="PortalFinanceiro.Model"
        default-lazy="true"
        default-cascade="none">    
        
        <typedef class="FuncefEngine.NHibernateHelpers.ZeroOneType, FuncefEngine" name="ZeroOneType"/>
        <typedef class="FuncefEngine.NHibernateHelpers.SNType, FuncefEngine" name="SNType"/>
        
        <class name="TipoAtoDecisorio" table="TIPO_ATO_DECISORIO" schema="CORE_PORTAL_FINANCEIRO">
            <id name="Id" column="ID_ATO_DECISORIO">
            <generator class="sequence">
                <param name="sequence">SQ_TIPO_ATO_DECISORIO</param>
            </generator>
            </id>
            <property name="Nome" column="DS_ATO_DECISORIO" />
            <property name="Ativo" column="IN_ATIVO" type="ZeroOneType"/>
            <property name="Tipo" column="ID_TIPO_DESTACAM" />
        </class>
    </hibernate-mapping>
    
    # Sempre incluir no arquivo as tags typedef
    # Sequence segue o padrão SQ_NOME_TABELA
    # Nome assembly "{assembly}"
    # Nome namespace "{namespace}"
    # Comando SQL de CREATE TABLE:"""
    
    
    
    return gerar_codigo(prompt, sql_create)