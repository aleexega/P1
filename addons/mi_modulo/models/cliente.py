from odoo import models, fields

class Cliente(models.Model):
    _name = "tienda.deportes.cliente"
    _description = "Cliente de la Tienda de Deportes"

    name = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
