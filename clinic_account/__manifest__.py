{
    'name': 'Clinic Billing',
    'version': '1.0',
    'summary': 'Generate customer invoices from clinic consultations',
    'depends': ['clinic', 'account'],
    'application': True,
    'data': [
        'views/clinic_consultation_views.xml',
        'views/clinic_patient_views.xml',
    ],
    'license': 'LGPL-3',
}
