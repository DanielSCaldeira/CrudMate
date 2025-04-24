from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_incluir_js(service_code):    
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef.controller')
        .controller('IncluirTipoAtoDecisorioController', IncluirTipoAtoDecisorioController);

    IncluirTipoAtoDecisorioController.$inject = ['$message', '$state', 'TipoAtoDecisorioService'];

    function IncluirTipoAtoDecisorioController($message, $state, TipoAtoDecisorioService) {

        var vm = this;
        vm.form = null;
        vm.salvar = salvar;

        init();

        function init() {
        }

        function salvar() {
            if (vm.form.valid()) {
                TipoAtoDecisorioService.inserir(vm.registro).then(function (response) {
                    $message.sucesso(response.data.mensagem);
                    $state.go('tipo-ato-decisorio.consultar');
                }, function (response) {
                    $message.erro(response.data.mensagem ? response.data.mensagem : 'Erro ao salvar Tipo Ato Decisorio !');
                });
            } else {
                $message.erro('Existem erros no formulário!');
            }
        }

        //////////
    }
})();

1) Gere o JS de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo."""
    return gerar_codigo(prompt, service_code)


def gerar_incluir_html(service_code):    
    prompt = """    
<ngf-page-header title="{{vm.id ? 'Editar' : 'Adicionar'}} Tipo Ato Decisorio  {{vm.id ? '#' + vm.id : ''}}" voltar="tipo-ato-decisorio.consultar">
    <button class="btn btn-primary" ng-if="vm.id" ui-sref="tipo-ato-decisorio.visualizar({id: vm.id})">
        <i class="fa fa-eye"></i> Visualizar Tipo Ato Decisorio
    </button>
</ngf-page-header>

<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">
            <i class="fa fa-calendar"></i>
            Formulário
        </h3>
    </div>

    <div class="panel-body">
        <form name="vm.form" ngf-validate="" ng-submit="vm.salvar()" novalidate>
            <div class="row">
                <div class="col-sm-6 form-group">
                    <label class="control-label" for="Nome">Descrição</label>
                    <textarea minlength="5"
                              maxlength="500"
                              class="form-control"
                              id="Nome"
                              name=" Nome do Ato Decisório"
                              ng-model="vm.registro.Nome"
                              placeholder="Informe Nome do Ato Decisório">
                    </textarea>
                </div>

                <div class="col-xs-12 col-sm-4 col-md-4">
                    <label class="control-label" for="possui-multa">
                        Ativo
                        <small class="block">Ato decisório ativo?</small>
                    </label>
                    <div>
                        <div class="radio3 radio-inline radio-danger radio-check">
                            <input type="radio" name="Multa sim" id="possui-multa-nao"
                                   value="false"
                                   ng-model="vm.registro.Ativo"
                                   ng-checked="vm.registro.Ativo == false" required />
                            <label for="possui-multa-nao" class="control-label">Não </label>
                        </div>
                        <div class="radio3 radio-inline radio-success radio-check">
                            <input type="radio" name="Multa sim" id="possui-multa-sim"
                                   value="true"
                                   ng-model="vm.registro.Ativo"
                                   ng-checked="vm.registro.Ativo == true" required />
                            <label for="possui-multa-sim" class="control-label">Sim</label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <button class="btn btn-primary" type="submit">
                        <i class="fa fa-check"></i> Salvar
                    </button>
                    <button class="btn btn-default"
                            ui-sref="tipo-ato-decisorio.visualizar({id: vm.Id})"
                            type="button">
                        <i class="fa fa-times"></i> Cancelar
                    </button>
                </div>
            </div>
        </form>
    </div>
</div>

1) Gere o HTML de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo. Substitua a entidade principal pela entidade abaixo."""
    return gerar_codigo(prompt, service_code)