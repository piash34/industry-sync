{
    'name': 'Photography',
    'version': '1.0',
    'category': 'Services',
    'description': """
        The Odoo app for photography professionals provides a preconfigured database with all the
        necessary features to manage their business. The app includes pre-configured products and
        projects, a website template, and beautiful quotes to help photographers showcase their work
        and attract new clients. With this app, photographers can easily manage their projects, track
        their time, and create invoices. The website template allows photographers to showcase their
        portfolio and services, and the pre-configured products make it easy to sell prints and other
        photography-related items.
    """,
    'depends': [
        'crm',
        'sale_management',
        'knowledge',
        'project_enterprise',
        'website_appointment',
        'sale_project',
        'theme_nano',
    ],
    'data': [
        'data/res_groups_data.xml',
        'data/mail_templates.xml',
        'data/appointment_data.xml',
        'data/project_data.xml',
        'data/product_data.xml',
        'data/sale_order_template_data.xml',
        'data/crm_tags_data.xml',
        "data/ir_attachment.xml",
        "data/knowledge_cover.xml",
        "data/knowledge_article.xml",
        "data/knowledge_article_favorite.xml",
        "data/mail_message.xml",
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/sale_order.xml',
        "demo/sale_order_confirm.xml",
        'demo/project_task.xml',
        'demo/appointment.xml',
        'demo/website_ir_attachment.xml',
        "demo/website.xml",
        'demo/website_view.xml',
        "demo/website_contactus.xml",
        "demo/website_theme_apply.xml",
        'demo/website_page.xml',
        'demo/website_menu.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
