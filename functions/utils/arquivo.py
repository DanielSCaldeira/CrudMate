import os

def salvar_arquivos_gerados(
    output_dir,
    entidade,    
    model=None,
    dto=None,
    service=None,
    api=None,
    mapping=None,
    service_js=None,
    router_js=None,
    visualizar_html=None,
    incluir_html=None,
    consultar_html=None,
    visualizar_js=None,
    alterar_js=None,
    consultar_js=None,
    incluir_js=None
):
    """
    Salva os conteúdos gerados em arquivos com extensões apropriadas, organizados em uma estrutura de pastas.
    Todos os parâmetros de conteúdo são opcionais.
    """
    arquivos_dir = os.path.join(output_dir, "arquivos")
    os.makedirs(arquivos_dir, exist_ok=True)

    back_end_dir = os.path.join(arquivos_dir, "back-end", entidade)
    front_end_dir = os.path.join(arquivos_dir, "front-end", entidade)
    os.makedirs(back_end_dir, exist_ok=True)
    os.makedirs(front_end_dir, exist_ok=True)

    alterar_dir = os.path.join(front_end_dir, "alterar")
    consultar_dir = os.path.join(front_end_dir, "consultar")
    incluir_dir = os.path.join(front_end_dir, "incluir")
    visualizar_dir = os.path.join(front_end_dir, "visualizar")
    scripts_dir = os.path.join(front_end_dir, "scripts")

    for subdir in [alterar_dir, consultar_dir, incluir_dir, visualizar_dir, scripts_dir]:
        os.makedirs(subdir, exist_ok=True)

    arquivos = {
        os.path.join(back_end_dir, f"{entidade}.cs"): model,
        os.path.join(back_end_dir, f"{entidade}DTO.cs"): dto,
        os.path.join(back_end_dir, f"{entidade}Service.cs"): service,
        os.path.join(back_end_dir, f"{entidade}Controller.cs"): api,
        os.path.join(back_end_dir, f"{entidade}.mapping.nbm.xml"): mapping,
        os.path.join(alterar_dir, "alterar.js"): alterar_js,
        os.path.join(consultar_dir, "consultar.html"): consultar_html,
        os.path.join(consultar_dir, "consultar.js"): consultar_js,
        os.path.join(incluir_dir, "incluir.html"): incluir_html,
        os.path.join(incluir_dir, "incluir.js"): incluir_js,
        os.path.join(visualizar_dir, "visualizar.html"): visualizar_html,
        os.path.join(visualizar_dir, "visualizar.js"): visualizar_js,
        os.path.join(scripts_dir, f"{entidade}.service.js"): service_js,
        os.path.join(scripts_dir, f"{entidade}.router.js"): router_js,
    }

    for caminho_arquivo, conteudo in arquivos.items():
        if conteudo is not None:
            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(conteudo)
            print(f"Arquivo gerado: {caminho_arquivo}")
