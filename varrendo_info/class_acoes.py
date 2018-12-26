# -*- coding: utf-8 -*-

class Acoes(object):
    def __init__(self):
        self._txt_empresa = ''
        self._txt_codigo = ''
        self._txt_ultimo_fechamento = ''
        self._txt_maxima52s = ''
        self._txt_minima52s = ''
        self._txt_qtd_negocios21d = ''
        self._txt_volume_medio = ''
        self._txt_data = ''

    def __str__(self):
        return str(
            self._txt_empresa + self._txt_codigo + self._txt_ultimo_fechamento + '' + self._txt_maxima52s + '' + self._txt_minima52s + '' + self._txt_qtd_negocios21d + '' + self._txt_volume_medio + '' + self._txt_data)

    @property
    def empresa(self):
        return self._txt_empresa

    @empresa.setter
    def empresa(self, value):
        self._txt_empresa = value

    @property
    def codigo(self):
        return self._txt_codigo

    @codigo.setter
    def codigo(self, value):
        self._txt_codigo = value

    @property
    def ultimo_fechamento(self):
        return self._txt_ultimo_fechamento

    @ultimo_fechamento.setter
    def ultimo_fechamento(self, value):
        self._txt_ultimo_fechamento = value

    @property
    def maxima52s(self):
        return self._txt_maxima52s

    @maxima52s.setter
    def maxima52s(self, value):
        self._txt_maxima52s = value

    @property
    def minima52s(self):
        return self._txt_minima52s

    @minima52s.setter
    def minima52s(self, value):
        self._txt_minima52s = value

    @property
    def qtd_negocios21d(self):
        return self._txt_qtd_negocios21d

    @qtd_negocios21d.setter
    def qtd_negocios21d(self, value):
        self._txt_qtd_negocios21d = value

    @property
    def volume_medio(self):
        return self._txt_volume_medio

    @volume_medio.setter
    def volume_medio(self, value):
        self._txt_volume_medio = value

    @property
    def data(self):
        return self._txt_data

    @data.setter
    def data(self, value):
        self._txt_data = value