import json
from functions.back_end import gerar_api
from functions.front_end.pagina.alterar import gerar_alterar_js
from functions.front_end.pagina.consultar import gerar_consultar_html, gerar_consultar_js
from functions.front_end.pagina.incluir import gerar_incluir_html, gerar_incluir_js
from functions.front_end.pagina.visualizar import gerar_visualizar_html, gerar_visualizar_js
from functions.front_end.scripts.router import gerar_router_js
from functions.front_end.scripts.service import gerar_service_js
from functions.back_end.gerar_service import gerar_service
from functions.back_end.gerar_dto import gerar_dto
from functions.back_end.gerar_model import gerar_model
from functions.back_end.gerar_xml_mapping import gerar_xml_mapping
from functions.entidade import identificar_entidade_funcoes_service, identificar_entidade_model
from functions.utils.arquivo import salvar_arquivos_gerados

def gerar_todos_componentes(sql):
    print("🔧 Gerando NHibernate Mapping...")
    mapping = gerar_xml_mapping(sql)
    print("### XML Mapping ###\n", mapping)

    print("🔧 Identificando entidades e propriendade da model...")
    entidade = identificar_entidade_model(mapping)
    print("### XML Mapping ###\n", entidade)

    dados = json.loads(entidade)
    nomeEntidade = dados["Entidade"]

    print("\n📦 Gerando Model...")
    model = gerar_model(entidade)
    print("### Model ###\n", model)    
    
    print("\n📦 Gerando DTO...")
    dto = gerar_dto(entidade)
    print("### DTO ###\n", dto)    

    print("\n🛠️ Gerando Service...")
    service = gerar_service(entidade)
    print("### Service ###\n", service)

    print("\n🌐 Gerando API...")
    api = gerar_api(service)
    print("### API ###\n", api)
    
    print("\n🌐 Gerando Service JS...")
    service_js = gerar_service_js(api)
    print("### Service JS ###\n", service_js)
    
    print("🔧 Identificando entidades e funçoes da service...")
    entidadeService = identificar_entidade_funcoes_service(mapping)
    print("### XML Mapping ###\n", entidadeService)
    
    uniaoEntidade = f"Entidade :\n{entidade}\nService:\n{entidadeService}"
        
    print("\n🌐 Gerando Router JS...")
    router_js = gerar_router_js(uniaoEntidade)
    print("### Router JS ###\n", router_js)   

    print("\n🖋️ Gerando Visualizar HTML...")
    visualizar_html = gerar_visualizar_html(entidade)
    print("### Visualizar HTML ###\n", visualizar_html)

    print("\n🖋️ Gerando Incluir HTML...")
    incluir_html = gerar_incluir_html(entidade)
    print("### Incluir HTML ###\n", incluir_html)
    
    print("\n🖋️ Gerando Consultar HTML...")
    consultar_html = gerar_consultar_html(entidade)
    print("### Consultar HTML ###\n", consultar_html)
    
    print("\n🖋️ Gerando Visualizar JS...")
    visualizar_js = gerar_visualizar_js(uniaoEntidade)
    print("### Visualizar JS ###\n", visualizar_js)

    print("\n🖋️ Gerando Alterar JS...")
    alterar_js = gerar_alterar_js(uniaoEntidade)
    print("### Alterar JS ###\n", alterar_js)

    print("\n🖋️ Gerando Consultar JS...")
    consultar_js = gerar_consultar_js(uniaoEntidade)
    print("### Consultar JS ###\n", consultar_js)

    print("\n🖋️ Gerando Incluir JS...")
    incluir_js = gerar_incluir_js(uniaoEntidade)
    print("### Incluir JS ###\n", incluir_js)
    
    salvar_arquivos_gerados("./", nomeEntidade,model, dto, service, api, mapping, service_js, router_js, visualizar_html, incluir_html, consultar_html, visualizar_js, alterar_js, consultar_js, incluir_js)
  