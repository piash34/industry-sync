{
    'name': 'Fine Dining Restaurant',
    'version': '1.0',
    'category': 'Services',
    'description': """
        This Odoo module is designed to streamline and enhance the management of your restaurant operations.
    """,
    'depends': [
        'account_followup',
        'contacts',
        'hr',
        'knowledge',
        'planning',
        'pos_enterprise',
        'pos_loyalty',
        'pos_online_payment_self_order',
        'pos_restaurant_appointment',
        'project',
        'purchase_stock',
        'website_appointment',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/appointment_type.xml',
        'data/ir_attachment_pre.xml',
        'data/pos_payment_method.xml',
        'data/product_category.xml',
        'data/product_product.xml',
        'data/project_task_type.xml',
        'data/project_project.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/website_view.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/pos_payment_method.xml',
        'demo/payment_provider_demo_post.xml',
        'demo/res_partner.xml',
        'demo/hr_employee.xml',
        'demo/pos_config.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_product.xml',
        'demo/kitchen_display.xml',
        'demo/product_packaging.xml',
        'demo/stock_warehouse_orderpoint.xml',
        'demo/planning_role.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/planning_slot.xml',
        'demo/project_task.xml',
        'demo/appointment_type.xml',
        'demo/website_attachment.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
