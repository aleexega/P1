from odoo import models, fields

class Pedido(models.Model):
    _name = 'mi_modulo.pedido'
    _description = 'Pedido de compra de un cliente'
    
    cliente_id = fields.Many2one('mi_modulo.cliente', string="Cliente")
    producto_ids = fields.Many2many('mi_modulo.producto', string="Productos")
    fecha = fields.Date(string="Fecha", default=fields.Date.today())
