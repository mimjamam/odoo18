{
    'name': 'Hospital Management',
    'version': '18.0.1.0',
    'category': 'Services/Hospital',
    'summary': 'Manage hospital operations, patients, appointments, and doctors',
    'sequence': -200,
    'description': """
        Hospital Management System
        ==========================
        * Manage hospital patients and appointments
        * Track patient information
        * Generate appointment reports
    """,
    'author': 'Om Hospital',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        "security/ir.model.access.csv",
        "views/patient_views.xml",  # includes patients and actions
        "views/menu.xml",  # menus depend on actions above
        "views/female_patient_view.xml",  # depend on parent menu
        "views/male_patient.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/hospital.svg']
}
