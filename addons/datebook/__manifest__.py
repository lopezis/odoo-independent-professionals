{
    "name": "Datebook - Booking de Citas",
    "summary": "Reserva de citas similar a Calendly con portal, disponibilidad, recordatorios e integración de CRM.",
    "version": "18.0.1.0.0",
    "author": "lopezis",
    "website": "https://github.com/lopezis",
    "category": "Productivity/Calendar",
    "license": "LGPL-3",
    "depends": ["base", "website", "mail", "calendar", "crm"],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_templates.xml",
        "data/cron_jobs.xml",
        "views/backend_views.xml",
        "views/dashboard_views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "datebook/static/src/css/booking.css",
            "datebook/static/src/js/booking.js",
        ],
    },
    "application": True,
    "installable": True,
}
