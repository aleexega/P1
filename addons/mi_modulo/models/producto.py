from odoo import models, fields

class Producto(models.Model):
    _name = "tienda.deportes.producto"
    _description = "Producto de la Tienda de Deportes"

    nombre = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
