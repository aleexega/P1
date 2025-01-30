from odoo import models, fields

class Cliente(models.Model):
    _name = 'mi_modulo.cliente'
    _description = 'Cliente del sistema'
    
    nombre = fields.Char(string="Nombre", required=True)
    direccion = fields.Char(string="Dirección")
    correo = fields.Char(string="Correo electrónico")
    telefono = fields.Char(string="Teléfono")
