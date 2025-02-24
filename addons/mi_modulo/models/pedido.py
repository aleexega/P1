from odoo import models, fields

class Pedido(models.Model):
    _name = "tienda.deportes.pedido"
    _description = "Pedido de la Tienda de Deportes"

    cliente_id = fields.Many2one("tienda.deportes.cliente", string="Cliente", required=True)
    producto_ids = fields.Many2many("tienda.deportes.producto", string="Productos")
    cantidad = fields.Integer(string="Cantidad", default=1)
    fecha_pedido = fields.Date(string="Fecha del Pedido", required=True)
