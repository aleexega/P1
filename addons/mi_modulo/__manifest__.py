# -*- coding: utf-8 -*-
{
    'name': "Elite Sports",

    'summary': "Gestión de clientes, productos y pedidos en una tienda de deportes",

    'description': """
Módulo para gestionar clientes, productos y pedidos en una tienda de artículos deportivos.
    """,

    'author': "Alex",
    'website': "https://www.elitesports.com",

    'category': 'Ropa',
    'version': '1.0',

    # Módulos necesarios para que este funcione correctamente
    'depends': ['base'],

    # Archivos siempre cargados
    'data': [
        'security/ir.model.access.csv',
        'views/cliente.xml',
        'views/producto.xml',
        'views/pedido.xml',
        'views/menu.xml',
    ],

    # Solo se carga en modo demostración
    'demo': [],
}
