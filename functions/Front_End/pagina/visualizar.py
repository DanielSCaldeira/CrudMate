from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_visualizar_js(service_code):
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef.controller')
        .controller('VisualizarTipoAtoDecisorioController', VisualizarTipoAtoDecisorioController);

    VisualizarTipoAtoDecisorioController.$inject = ['$stateParams', '$message', '$state', 'TipoAtoDecisorioService', 'SOLICITACAOPAGTIPODESPESA'];

    function VisualizarTipoAtoDecisorioController($stateParams, $message, $state, TipoAtoDecisorioService, SOLICITACAOPAGTIPODESPESA) {

        var vm = this;
        vm.id = $stateParams.id;
        vm.excluir = excluir;
        vm.SOLICITACAOPAGTIPODESPESA = SOLICITACAOPAGTIPODESPESA;
        init();

        function init() {
            buscar();
        }

        function buscar() {
            TipoAtoDecisorioService.buscar(vm.id).then(function (response) {
                vm.tipoAtoDecisorio = response.data.resultado;
            }, function (response) {
                $message.erro(response.data.mensagem ? response.data.mensagem : 'Não foi possivel listar os cabeçalhos!');
            });
        }

        function excluir() {
            $message.confirmacao('Excluir TipoAtoDecisorio', 'Deseja realmente excluir este tipoAtoDecisorio?', function () {
                TipoAtoDecisorioService.excluir(vm.id).then(function (response) {
                    $message.sucesso('Registro removido com sucesso!');
                    $state.go('tipo-ato-decisorio.consultar');
                }, function (response) {
                    $message.erro(response.data.mensagem ? response.data.mensagem : 'Não foi possível remover tipoAtoDecisorio!');
                });
            });
        }
    }
})();

1) Gere o JS de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo."""""
    return gerar_codigo(prompt, service_code)

def gerar_visualizar_html(service_code):
    prompt = """    
<ngf-page-header title="Informações do Tipo Ato Decisorio  #{{vm.id}}" voltar="tipo-ato-decisorio.consultar">
    <button class="btn btn-primary" ui-sref="tipo-ato-decisorio.alterar({id: vm.id})">
        <i class="fa fa-edit"></i> Editar Tipo Ato Decisorio         
    </button>
    <button class="btn btn-danger" ng-click="vm.excluir()">
        <i class="fa fa-trash"></i> Excluir Tipo Ato Decisorio         
    </button>
</ngf-page-header>

<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">
            <i class="fa fa-calendar"></i>
            Visualizar Tipo Ato Decisorio 
        </h3>
    </div>
    <div class="panel-body">
        <div class="panel">
            <div class="panel-body pb-0">
                <div class="grid-view">
					<dl class="mb-0">
		            	<dt>Descrição</dt>
                        <dd ngf-empty="">{{vm.tipoAtoDecisorio.Nome}}</dd>
					</dl>
                    <dl class="mb-0">
                        <dt>Ativo</dt>
                        <dd ngf-empty>
                            <span ng-show="vm.tipoAtoDecisorio.Ativo" class="label label-success">Sim</span>
                            <span ng-show="!vm.tipoAtoDecisorio.Ativo" class="label label-danger">Não</span>
                        </dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</div>

1) Gere a página HTML conforme o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo."""
    return gerar_codigo(prompt, service_code)