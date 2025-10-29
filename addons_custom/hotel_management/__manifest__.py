{
    'name': 'Hotel Management',
    'version': '18.0.1.0.0',
    'category': 'Services/Hotel',
    'summary': 'Manage hotel operations, rooms, bookings and guests',
    'description': """
        Hotel Management System
        =======================
        * Manage hotel rooms and room types
        * Handle guest bookings and reservations
        * Track room availability
        * Manage guest information
        * Generate booking reports
    """,
    'author': 'Me',
    'website': 'https://www.company.com',
    'depends': ['base', 'mail', 'portal'],
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'views/hotel_dashboard_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_guest_views.xml',
        'views/hotel_menus.xml',
        'views/mainmenu.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
