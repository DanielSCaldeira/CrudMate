from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_consultar_html(service_code):    
    prompt = """    
<ngf-page-header title="Tipo Ato Decisorio ">
    <button class="btn btn-primary" ui-sref="tipo-ato-decisorio.incluir">
        <i class="fa fa-plus"></i> Incluir Tipo Ato Decisorio
    </button>
</ngf-page-header>

<div class="panel panel-default">
    <div class="panel-heading" data-toggle="collapse" data-target="#painel-tipoAtoDecisorio">
        <h3 class="panel-title">
            <i class="fa fa-filter"></i>
            Filtro
            <i class="fa fa-caret-left pull-right" aria-hidden="true"></i>
        </h3>
    </div>

    <div class="panel-body collapse in" id="painel-tipoAtoDecisorio">
        <form name="vm.form" ngf-validate ng-submit="vm.submitPesquisa()" novalidate>
            <div class="row">
                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 form-group">
                    <label class="control-label" for="Id">
                        Id
                        <small class="block">Id Ato decisório.</small>
                    </label>
                    <input type="text" ng-model="vm.pesquisa.Id" name="Id" id="Id" class="form-control" ngf-mask="numerico" placeholder="Pesquisa por Id" />
                </div>
                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 form-group">
                    <label class="control-label" for="Nome">
                        Nome
                        <small class="block">Nome Ato decisório.</small>
                    </label>
                    <input type="text" ng-model="vm.pesquisa.Nome" name="Nome" id="Nome" class="form-control" placeholder="Descrição" />
                </div>
                <div class="col-xs-12 col-sm-4 col-md-4">
                    <label class="control-label" for="possui-multa">
                        Ativo
                        <small class="block">Ato decisório ativo?</small>
                    </label>
                    <div>
                        <div class="radio3 radio-inline radio-success radio-check">
                            <input type="radio" name="Multa sim" id="possui-multa-sim"
                                   value="true"
                                   ng-model="vm.pesquisa.Ativo"
                                   ng-checked="vm.pesquisa.Ativo == 'true'" />
                            <label for="possui-multa-sim" class="control-label">Sim</label>
                        </div>
                        <div class="radio3 radio-inline radio-danger radio-check">
                            <input type="radio" name="Multa sim" id="possui-multa-nao"
                                   value="false"
                                   ng-model="vm.pesquisa.Ativo"
                                   ng-checked="vm.pesquisa.Ativo == 'false'" />
                            <label for="possui-multa-nao" class="control-label">Não </label>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div id="painelSearchLight" class="panel-collapse collapse in"></div>
                <div class="col-sm-12 form-group">
                    <button type="submit" class="btn btn-primary" ng-click="vm.submitPesquisa">
                        <i class="fa fa-search"></i> Pesquisar
                    </button>
                    <button type="button" class="btn btn-default" ng-click="vm.limpar()">
                        <i class="fa fa-eraser"></i> Limpar
                    </button>
                </div>
            </div>
        </form>
    </div>
</div>

<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">
            <i class="fa fa-list"></i>
            Tipo Ato Decisorio
        </h3>
    </div>
    <div class="panel-body">
        <ngf-summary filtro="vm.filtro" ng-show="vm.tipoAtoDecisorios.length" model-page="vm.filtro.pagination.number"></ngf-summary>
        <div st-pipe="vm.pesquisarServidor" st-table="vm.tipoAtoDecisorios" ng-show="vm.tipoAtoDecisorios.length">
            <table class="table">
                <thead>
                    <tr>
                        <th st-sort="Id">Id</th>
                        <th st-sort="Nome">Nome</th>
                        <th st-sort="Ativo">Ativo</th>
                        <th st-sort="Tipo">Tipo</th>
                        <th width="130" class="text-right">Opções</th>
                    </tr>
                </thead>
                <tbody>
                    <tr ng-repeat="item in vm.tipoAtoDecisorios">
                        <td>{{item.Id}}</td>
                        <td>{{item.Nome}}</td>
                        <td ngf-empty>
                            <span ng-show="item.Ativo" class="label label-success">Sim</span>
                            <span ng-show="!item.Ativo" class="label label-danger">Não</span>
                        </td>
                        <td>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Contrato.Valor" class="label label-default">Contrato</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Compra.Valor" class="label label-default">Compra</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Outras.Valor" class="label label-default">Outras</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Imobiliaria.Valor" class="label label-default">Imobiliária</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Juridica.Valor" class="label label-default">Jurídica</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.GEAPE.Valor" class="label label-default">GEAPE</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.DIBEN.Valor" class="label label-default">DIBEN</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Multa.Valor" class="label label-default">Multa</span>
                            <span ng-if="item.Tipo == vm.SOLICITACAOPAGTIPODESPESA.Autorizada.Valor" class="label label-default">Solicitação previamente autorizada</span>
                        </td>
                        <td class="text-center">
                            <div class="btn-group">
                                <button type="button" ui-sref="tipo-ato-decisorio.visualizar({id: item.Id})"
                                        class="btn btn-default btn-sm"
                                        uib-tooltip="Ver Detalhes">
                                    <i class="fa fa-eye"></i>
                                </button>
                                <button type="button"
                                        class="btn btn-default dropdown-toggle btn-sm"
                                        data-toggle="dropdown"
                                        uib-tooltip="Outras Opções">
                                    <span class="caret"></span>
                                </button>
                                <ul class="dropdown-menu dropdown-menu-right">
                                    <li>
                                        <a ui-sref="tipo-ato-decisorio.alterar({id: item.Id})">
                                            <i class="fa fa-edit mr-5"></i>
                                            Editar
                                        </a>
                                    </li>
                                    <li>
                                        <a ng-click="vm.excluir(item)">
                                            <i class="fa fa-trash mr-5"></i>
                                            Excluir
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
            <ngf-pagination filtro="vm.filtro" qtd-registro="vm.qtdRegistros"></ngf-pagination>
        </div>
        <div ngf-empty icon-empty="true" text-empty="Nenhum resultado para pesquisa informada!" ng-hide="vm.tipoAtoDecisorios.length"></div>
    </div>
</div>

1) Gere o HTML de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo. Substitua a entidade principal pela entidade abaixo."""
    return gerar_codigo(prompt, service_code)


def gerar_consultar_js(service_code):    
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef.controller')
        .controller('ConsultarTipoAtoDecisorioController', ConsultarTipoAtoDecisorioController);

    ConsultarTipoAtoDecisorioController.$inject = ['$message', '$cookies', 'TipoAtoDecisorioService', 'SOLICITACAOPAGTIPODESPESA'];

    function ConsultarTipoAtoDecisorioController($message, $cookies, TipoAtoDecisorioService, SOLICITACAOPAGTIPODESPESA) {
        var vm = this;
        vm.pesquisa = {};
        vm.pesquisa.Ativo = 'true';
        vm.cookiePesquisa = 'pesquisaTipoAtoDecisorio';
        vm.cookieFiltro = 'filtroTipoAtoDecisorio';
        vm.form = null;
        vm.SOLICITACAOPAGTIPODESPESA = SOLICITACAOPAGTIPODESPESA;
        vm.pesquisarServidor = pesquisarServidor;
        vm.submitPesquisa = submitPesquisa;
        vm.alterarSituacao = alterarSituacao;
        vm.limpar = limpar;
        vm.excluir = excluir;

        init();

        ////////////

        function init() {
            initForm();
        }

        function initForm() {
            if ($cookies.getObject(vm.cookiePesquisa)) {
                vm.pesquisa = $cookies.getObject(vm.cookiePesquisa);
            }

            if ($cookies.getObject(vm.cookieFiltro)) {
                vm.filtro = $cookies.getObject(vm.cookieFiltro);
            }
        }

        function pesquisarServidor(filtro) {
            vm.filtro = filtro;
            listarTipoAtoDecisorios();
        }

        function submitPesquisa() {
            if (vm.form.valid()) {
                vm.tipoAtoDecisorios = [];
                vm.filtro.pagination.start = 0;
                listarTipoAtoDecisorios();
                guardarPesquisaCookie();
            }
        }

        function alterarSituacao(item, situacao) {
            $message.confirmacao('Alerta', 'Deseja realmente alterar a situação de tipoAtoDecisorio?', function () {
                item.Ativo = situacao;
                TipoAtoDecisorioService.editar(item).then(function (response) {
                    $message.sucesso(response.data.mensagem);
                    listarTipoAtoDecisorios();
                }, function (response) {
                    $message.erro(response.data.mensagem);
                });
            });
        }

        function excluir(item) {
            $message.confirmacao('Alerta', 'Deseja excluir este tipoAtoDecisorio?', function () {
                TipoAtoDecisorioService.excluir(item.Id).then(function (response) {
                    $message.sucesso(response.data.mensagem);
                    listarTipoAtoDecisorios();
                }, function (response) {
                    $message.erro(response.data.mensagem);
                });
            });
        }

        function guardarPesquisaCookie() {
            $cookies.putObject(vm.cookiePesquisa, vm.pesquisa);
            $cookies.putObject(vm.cookieFiltro, vm.filtro);
        }

        function limpar() {
            vm.pesquisa = {};
            vm.pesquisa.Ativo = 'true';
            submitPesquisa();
        }

        ///////////

        function listarTipoAtoDecisorios() {
            TipoAtoDecisorioService.pesquisar(vm.filtro, vm.pesquisa).then(function (response) {
                vm.tipoAtoDecisorios = response.data.resultado;
                vm.qtdRegistros = response.data.qtdRegistros;
            }, function (response) {
                $message.erro(response.data ? response.data.mensagem : 'Não foi possível listar tipoAtoDecisorios!');
            });
        }
    }
})();

1) Gere o JS de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo. Substitua a entidade principal pela entidade abaixo."""
    return gerar_codigo(prompt, service_code)