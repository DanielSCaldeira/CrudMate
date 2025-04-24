from functions.Back_End.gerar_codigo import gerar_codigo

def gerar_router_js(service_code):
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef')
        .config(function ($stateProvider, $urlRouterProvider) {
            $stateProvider
                .state('tipo-ato-decisorio', {
                    url: '/tipo-ato-decisorio',
                    ncyBreadcrumb: {
                        label: 'Tipo Ato Decisorio '
                    },
                    redirectTo: 'tipo-ato-decisorio.consultar'
                })

                .state('tipo-ato-decisorio.consultar', {
                    url: '/consultar',
                    templateUrl: 'pages/tipo-ato-decisorio/consultar/consultar.view.html',
                    controller: 'ConsultarTipoAtoDecisorioController',
                    controllerAs: 'vm',
                    ncyBreadcrumb: {
                        label: 'Consultar'
                    }
                })

                .state('tipo-ato-decisorio.incluir', {
                    url: '/incluir',
                    templateUrl: 'pages/tipo-ato-decisorio/incluir/incluir.view.html',
                    controller: 'IncluirTipoAtoDecisorioController',
                    controllerAs: 'vm',
                    ncyBreadcrumb: {
                        label: 'Cadastro'
                    }
                })

                .state('tipo-ato-decisorio.alterar', {
                    url: '/alterar/:id',
                    templateUrl: 'pages/tipo-ato-decisorio/incluir/incluir.view.html',
                    controller: 'AlterarTipoAtoDecisorioController',
                    controllerAs: 'vm',
                    ncyBreadcrumb: {
                        label: 'Editar'
                    }
                })

                .state('tipo-ato-decisorio.visualizar', {
                    url: '/visualizar/:id',
                    templateUrl: 'pages/tipo-ato-decisorio/visualizar/visualizar.view.html',
                    controller: 'VisualizarTipoAtoDecisorioController',
                    controllerAs: 'vm',
                    ncyBreadcrumb: {
                        label: 'Visualizar'
                    }
                })
        });
})();

1) Gere a Router js de acordo com o exemplo acima.
Considere a entidade e suas propriedades para a construção do arquivo.
Substitua a entidade principal pela entidade abaixo.
Crie 4 urls visualizar, alterar, incluir e consultar."""""
    return gerar_codigo(prompt, service_code)