import json
import signal
from typing import  Dict, List
from dotenv import load_dotenv
from InquirerPy import inquirer
from rich.align import Align
from rich.console import Console
from rich.text import Text
import pyfiglet
from consts import API, DTO, MAPPING, MODEL, SQL, OPTION_FUNCTIONS, PROMPTS

from functions.entidade import identificar_entidade_model
from functions.utils.arquivo import salvar_arquivos_gerados

load_dotenv()
console = Console()

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
    selected = inquirer.checkbox(
        message="Utilize a tecla *Espaço* do teclado para selecionar a função:",
        choices=choices,
        validate=lambda ans: ans or "Selecione ao menos uma opção.",
    ).execute()
    print("Selecionado:", selected)
    return selected


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

def _extract_entity_name(results: Dict[str, str]) -> str:
    """Extrai o nome da entidade a partir do mapeamento XML gerado."""
    mapping = results.get("🔧 XML Mapping (NHibernate)", "{}")
    try:
        data = json.loads(identificar_entidade_model(mapping))
        return data.get("Entidade", "")
    except Exception:
        return ""


def main():        
    selected = choose_options()
    results: Dict[str, str] = {}
    for opt in selected:
        inp = prompt_for_input(opt)
        if "🔧 Gerar Todas opções" not in selected:
            results[opt] = execute_option(opt, inp)
        else:
            results = execute_option("🔧 Gerar Todas opções", inp)
            break

    if "🔧 Gerar Todas opções" not in selected:
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

if __name__ == "__main__":
    main()




