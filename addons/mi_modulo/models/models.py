from odoo import models, fields

class MiModulo(models.Model):
    _name = 'mi.modulo'  # Nombre técnico del modelo
    _description = 'Mi primer modelo'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
