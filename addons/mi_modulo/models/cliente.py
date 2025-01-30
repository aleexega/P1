from odoo import models, fields

class Cliente(models.Model):
    _name = 'mi.modulo.cliente'
    _description = 'Clientes'

    name = fields.Char(string="Nombre", required=True)
    correo = fields.Char(string="Correo", required=True)

