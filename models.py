# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api


class AlquilerCategoria(models.Model):
    _name = 'alquiler.categoria'
    _description = 'Categorías'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    coches = fields.One2many('alquiler.coche', 'categoria_id', string='Coches')
    num_coches = fields.Integer(string='Número de coches', compute='_compute_num_coches')

    @api.depends('coches')
    def _compute_num_coches(self):
        for categoria in self:
            categoria.num_coches = len(categoria.coches)



class AlquilerCoche(models.Model):
    _name = 'alquiler.coche'
    _description = 'Coche'

    name = fields.Char(string='Nombre', required=True)
    precio_alquiler = fields.Float(string='Precio de Alquiler', required=True)
    ano_fabricacion = fields.Integer(string='Año de Fabricación')
    categoria_id = fields.Many2one('alquiler.categoria', string='Categoría')
    estado = fields.Selection([('nuevo', 'Nuevo'), ('usado', 'Usado')], string='Estado por año', compute='_compute_estado_anio')

    @api.depends('ano_fabricacion')
    def _compute_estado_anio(self):
        for coche in self:
            if coche.ano_fabricacion >= 2020:
                coche.estado = 'nuevo'
            else:
                coche.estado = 'usado'
        

class AlquilerReserva(models.Model):
    _name = 'alquiler.reserva'
    _description = 'Reserva'

    cliente_id = fields.Many2one('alquiler.cliente', string='Cliente', required=True)
    coche_id = fields.Many2one('alquiler.coche', string='Coche', required=True)
    precio_alquiler = fields.Float(string='Precio de Alquiler', required=True)
    dias_reserva = fields.Integer(string='Días de reserva', required=True)
    precio_seguro = fields.Float(string='Precio del seguro')
    importe_impuesto = fields.Float(string='Importe impuesto')
    impuesto = fields.Float(string='Impuesto', compute='_compute_impuesto')
    importe_total = fields.Float(string='Importe total SIN IVA', compute='_compute_importe_total')

    @api.depends('dias_reserva', 'precio_seguro', 'precio_alquiler')
    def _compute_importe_total(self):
        for reserva in self:
            reserva.importe_total = (reserva.precio_alquiler * reserva.dias_reserva) + reserva.precio_seguro

    @api.depends('importe_total', 'importe_impuesto')
    def _compute_impuesto(self):
        for reserva in self:
            reserva.impuesto = reserva.importe_total * reserva.importe_impuesto



class AlquilerCliente(models.Model):
    _name = 'alquiler.cliente'
    _description = 'Cliente'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellidos')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    reservas = fields.One2many('alquiler.reserva', 'cliente_id', string='Reservas')

# class alquilercoches(models.Model):
#     _name = 'alquilercoches.alquilercoches'
#     _description = 'alquilercoches.alquilercoches'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
