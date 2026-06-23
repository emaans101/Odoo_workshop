{
    'name': 'Clinic Management',
    'version': '1.0',
    'summary': 'Patients, doctors, appointments, consultations and medicine stock',
    'depends': ['base', 'mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/clinic_patient_views.xml',
        'views/clinic_doctor_views.xml',
        'views/clinic_specialization_views.xml',
        'views/clinic_medicine_views.xml',
        'views/clinic_appointment_views.xml',
        'views/clinic_consultation_views.xml',
        'views/clinic_menus.xml',
    ],

    'license': 'LGPL-3',
}
