from functions.back_end.gerar_codigo import gerar_codigo

def gerar_service_js(service_code):
    prompt = """    
(function () {
    'use strict';

    angular.module('funcef.service')
        .service('TipoAtoDecisorioService', TipoAtoDecisorioService);

    TipoAtoDecisorioService.$inject = ['$http', 'BASEPATH'];

    function TipoAtoDecisorioService($http, BASEPATH) {
        var service = {
            listar: listar,
            pesquisar: pesquisar,
            inserir: inserir,
            editar: editar,
            buscar: buscar,
            excluir: excluir
        };

        return service;

        ////////////

        function listar(filtro, pesquisa) {
            return $http.post(BASEPATH + 'TipoAtoDecisorio');
        }

        function pesquisar(filtro, pesquisa) {
            var param = angular.copy(pesquisa);
            if (pesquisa) {
                //param.Ativo = (param && param.Ativo) ? parseInt(param.Ativo) === 1 : null;
            }

            return $http.post(BASEPATH + 'TipoAtoDecisorio/Consultar', {
                filtro: filtro,
                pesquisa: param
            });
        }

        function inserir(registro) {
            return $http.post(BASEPATH + 'TipoAtoDecisorio/Incluir', {
                registro: registro
            });
        }

        function buscar(id) {
            return $http.post(BASEPATH + 'TipoAtoDecisorio/Buscar', {
                Id: id
            });
        }

        function editar(registro) {
            return $http.post(BASEPATH + 'TipoAtoDecisorio/Alterar', {
                registro: registro
            });
        }

        function excluir(id) {
            return $http.post(BASEPATH + 'TipoAtoDecisorio/Excluir', {
                Id: id
            });
        }
    };
})();

1) Gere a service js de acordo com o exemplo acima, utilizando a classe Controller C# fornecida no exemplo abaixo."""""
    return gerar_codigo(prompt, service_code)