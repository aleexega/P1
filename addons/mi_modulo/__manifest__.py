{
    'name': 'Gestión de Clientes y Productos',
    'version': '1.0',  
    'author': 'Titan Block',  
    'website': 'https://www.titanblock.com',
    'depends': ['base', 'sale'], 
    'data': [
        'views/cliente_views.xml', 
        'views/producto_views.xml', 
        'views/pedido_views.xml',  
        'security/ir.model.access.csv', 
        'views/pedido_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False, 
    'license': 'LGPL-3',
}
