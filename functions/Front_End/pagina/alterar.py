from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_alterar_js(service_code):
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef.controller')
        .controller('AlterarTipoAtoDecisorioController', AlterarTipoAtoDecisorioController);

    AlterarTipoAtoDecisorioController.$inject = ['$message', '$stateParams', '$state', 'TipoAtoDecisorioService'];

    function AlterarTipoAtoDecisorioController($message, $stateParams, $state, TipoAtoDecisorioService) {

        var vm = this;
        vm.id = $stateParams.id;
        vm.salvar = salvar;
        init();

        function init() {
            buscar();
        }

        function salvar() {
            if (vm.form.valid()) {
                TipoAtoDecisorioService.editar(vm.registro).then(function (response) {
                    $message.sucesso(response.data.mensagem);
                    $state.go('tipo-ato-decisorio.pesquisa');
                }, function (response) {
                    $message.erro(response.data.mensagem);
                });
            } else {
                $message.erro('Existem erros no formulário!');
            }
        }

        function buscar() {
            TipoAtoDecisorioService.buscar(vm.id).then(function (response) {
                vm.registro = response.data.resultado;
            }, function (response) {
                $message.erro(response.data.resultado);
            });
        }
    }
})();

1) Gere o JS de acordo com o exemplo acima. Considere a entidade e suas propriedades para a construção do arquivo."""
    return gerar_codigo(prompt, service_code)
