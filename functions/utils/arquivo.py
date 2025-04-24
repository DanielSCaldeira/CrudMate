import os

def salvar_arquivos_gerados(output_dir, model, dto, service, api, mapping, service_js, router_js, visualizar_html, incluir_html, consultar_html, visualizar_js, alterar_js, consultar_js, incluir_js, entidade):
    """
    Salva os conteúdos gerados em arquivos com extensões apropriadas, organizados em uma estrutura de pastas.
    """
    # Criar a pasta principal "arquivos"
    arquivos_dir = os.path.join(output_dir, "arquivos")
    if not os.path.exists(arquivos_dir):
        os.makedirs(arquivos_dir)

    # Criar subpastas "back-end" e "front-end"
    back_end_dir = os.path.join(arquivos_dir, "back-end", entidade)
    front_end_dir = os.path.join(arquivos_dir, "front-end", entidade)
    if not os.path.exists(back_end_dir):
        os.makedirs(back_end_dir)
    if not os.path.exists(front_end_dir):
        os.makedirs(front_end_dir)

    # Criar subpastas dentro de "front-end" para "alterar", "consultar", "incluir" e "visualizar"
    alterar_dir = os.path.join(front_end_dir, "alterar")
    consultar_dir = os.path.join(front_end_dir, "consultar")
    incluir_dir = os.path.join(front_end_dir, "incluir")
    visualizar_dir = os.path.join(front_end_dir, "visualizar")
    scripts_dir = os.path.join(front_end_dir, "scripts")

    for subdir in [alterar_dir, consultar_dir, incluir_dir, visualizar_dir, scripts_dir]:
        if not os.path.exists(subdir):
            os.makedirs(subdir)


    # Mapear os arquivos para suas respectivas pastas
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
        os.path.join(scripts_dir, f"{entidade}.router.js"): router_js ,
    }

    # Salvar os arquivos nas pastas apropriadas
    for caminho_arquivo, conteudo in arquivos.items():
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(f"Arquivo gerado: {caminho_arquivo}")