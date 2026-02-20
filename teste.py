import json
import signal
from typing import Callable, Dict, List, Union

from dotenv import load_dotenv
from InquirerPy import inquirer
from rich.align import Align
from rich.console import Console
from rich.text import Text
import pyfiglet

from consts import API, DTO, MAPPING, MODEL, SQL
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
from functions.utils.arquivo import salvar_arquivos_gerados

load_dotenv()
console = Console()

# Mapping between option labels and generator functions
GeneratorFunc = Callable[[str], Union[str, None]]

OPTION_FUNCTIONS: Dict[str, GeneratorFunc] = {
    # Back-End
    "🔧 Model (Back-End)": gerar_model,
    "🔧 DTO (Back-End)": gerar_dto,
    "🔧 Service (Back-End)": gerar_service,
    "🔧 API (Back-End)": gerar_api,
    "🔧 XML Mapping (NHibernate)": gerar_xml_mapping,
    # Front-End Scripts
    "🎨 Service JS": gerar_service_js,
    "🎨 Router JS": gerar_router_js,
    # Front-End Pages
    "🖋️ Visualizar HTML": gerar_visualizar_html,
    "🖋️ Visualizar JS": gerar_visualizar_js,
    "🖋️ Incluir HTML": gerar_incluir_html,
    "🖋️ Incluir JS": gerar_incluir_js,
    "🖋️ Consultar HTML": gerar_consultar_html,
    "🖋️ Consultar JS": gerar_consultar_js,
    "🖋️ Alterar JS": gerar_alterar_js,
}

# Prompts for each function
PROMPTS: Dict[str, str] = {
    "Model": "Informe a estrutura da Model (ex: nome:Tipo, outro:Tipo)",
    "DTO": "Liste os campos para o DTO (um por linha)",
    "Service": "Descreva lógica específica para a Service, se necessário",
    "API": "Configurações específicas para a API, se houver",
    "XML Mapping": "Forneça o script SQL da tabela para o mapeamento XML",
    "Service JS": "Descreva personalizações para o Service JS",
    "Router JS": "Informe rotas para o Router JS (ex: /entidades)",
    "HTML": "Forneça estrutura HTML base, se houver",
    "JS": "Descreva lógica JS inicial, se necessário",
}


def signal_handler(sig, frame):
    console.print("\n[bold red]Execução interrompida pelo usuário.[/bold red]")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


def show_banner() -> None:
    """Exibe o banner inicial no console."""
    title = pyfiglet.figlet_format("Gerador de CRUD", font="small")
    console.print(Align.center(Text(title, style="bold blue")))
    console.print(Align.center(Text("Assistente de Geração de CRUD IA", style="bold green")))
    console.print()


def choose_options() -> List[str]:
    """Apresenta um menu de seleção e retorna as opções escolhidas."""
    show_banner()
    choices = list(OPTION_FUNCTIONS.keys())
    return inquirer.checkbox(
        message="Utilize a tecla *Espaço* do teclado para selecionar a função:",
        choices=choices,
        validate=lambda ans: ans or "Selecione ao menos uma opção.",
    ).execute()


def prompt_for_input(option: str) -> str:
    """Retorna o input do usuário baseado na opção selecionada."""
    key = next((k for k in PROMPTS if k in option), None)
    message = PROMPTS.get(key, "Insira informação necessária:")
    console.print(f"[bold yellow]Entrada para:[/bold yellow] [bold magenta]{option}[/bold magenta]")
    return inquirer.text(message=f"{option}: {message}").execute()


def execute_option(option: str, user_input: str) -> str:
    """Executa a função correspondente à opção e retorna seu resultado."""
    func = OPTION_FUNCTIONS[option]
    console.print(f"Executando [bold magenta]{option}[/bold magenta]...")
    result = func(user_input)
    console.print(f"[bold green]Concluído {option}![/bold green]\n")
    return result or ""


def main() -> None:
    selected = choose_options()
    results: Dict[str, str] = {}

    for opt in selected:
        inp = prompt_for_input(opt)
        results[opt] = execute_option(opt, inp)

    salvar_arquivos_gerados(
        output_dir="./",
        entidade=_extract_entity_name(results),
        model=results.get("🔧 Model (Back-End)"),
        dto=results.get("🔧 DTO (Back-End)"),
        service=results.get("🔧 Service (Back-End)"),
        api=results.get("🔧 API (Back-End)"),
        mapping=results.get("🔧 XML Mapping (NHibernate)"),
        service_js=results.get("🎨 Service JS"),
        router_js=results.get("🎨 Router JS"),
        visualizar_html=results.get("🖋️ Visualizar HTML"),
        incluir_html=results.get("🖋️ Incluir HTML"),
        consultar_html=results.get("🖋️ Consultar HTML"),
        visualizar_js=results.get("🖋️ Visualizar JS"),
        alterar_js=results.get("🖋️ Alterar JS"),
        consultar_js=results.get("🖋️ Consultar JS"),
        incluir_js=results.get("🖋️ Incluir JS"),
    )
    console.print("[bold green]✔ Todos os arquivos foram salvos com sucesso![/bold green]")


def _extract_entity_name(results: Dict[str, str]) -> str:
    """Extrai o nome da entidade a partir do mapeamento XML gerado."""
    mapping = results.get("🔧 XML Mapping (NHibernate)", "{}")
    try:
        data = json.loads(identificar_entidade_model(mapping))
        return data.get("Entidade", "")
    except Exception:
        return ""


if __name__ == "__main__":
    main()