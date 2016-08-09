# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################

from unittest import TestCase

from correiosapi.rastreamento.consulta_rastreamento import RequestRastreamento
from correiosapi.rastreamento.consulta_rastreamento import ResponseRastreamento
from correiosapi.webservices.webservice_rastreamento import WebserviceRastreamento
from correiosapi.sigep_exceptions import ErroValidacaoXML
from correiosapi.sigep_exceptions import ErroConexaoComServidor


class TestWebserviceRastreamento(TestCase):

    def test_request(self):
        server = WebserviceRastreamento()
        req = RequestRastreamento('ECT', 'SRO',
                                  RequestRastreamento.TIPO_LISTA_DE_OBJETOS,
                                  RequestRastreamento.ULTIMO_RESULTADO,
                                  ['PJ472895891BR', 'PJ382325976B'])

        try:
            self.assertIsInstance(server.request(req), ResponseRastreamento)
        except ErroValidacaoXML as exc:
            print exc.message
        except ErroConexaoComServidor as exc:
            print exc.message
