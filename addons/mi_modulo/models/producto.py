from odoo import models, fields

class Producto(models.Model):
    _name = 'mi_modulo.producto'
    _description = 'Producto del sistema'
    
    nombre = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio")
    cantidad = fields.Integer(string="Cantidad disponible")
    categoria = fields.Char(string="Categoría")
