{
    'name': 'Clinic Inventory',
    'version': '1.0',
    'summary': 'Track clinic medicine dispensing with Odoo Inventory',
    'depends': ['clinic', 'stock'],
    'application': True,
    'data': [
        'views/clinic_medicine_views.xml',
    ],
    'demo': [
        'demo/clinic_stock_demo.xml',
    ],
    'license': 'LGPL-3',
}
