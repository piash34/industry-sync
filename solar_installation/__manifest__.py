{
    'name': 'Solar Energy Systems',
    'version': '1.0',
    'category': 'Construction',
    'description': """
This configuration is designed for companies specializing in solar equipment and installation services.
They cater to both residential and commercial customers,
ensuring the efficient installation of solar panels and associated equipment.
""",
    'depends': [
        'account_followup',
        'helpdesk_account',
        'helpdesk_fsm',
        'helpdesk_repair',
        'industry_fsm_sale_report',
        'industry_fsm_stock',
        'mrp_account',
        'product_expiry',
        'project_sms',
        'sale_crm',
        'sale_purchase',
        'stock_landed_costs',
        'web_studio',
        'website_crm',
        'website_helpdesk_knowledge',
        'website_livechat',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/helpdesk_config.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_model_access.xml',
        'data/ir_rule.xml',
        'data/project_task_type.xml',
        'data/product_category.xml',
        'data/worksheet_template.xml',
        'data/project_project.xml',
        'data/product_template.xml',
        'data/product_product.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/mrp_bom.xml',
        'data/mrp_bom_line.xml',
        'data/chatbot_script_answer.xml',
        'data/chatbot_script_step.xml',
        'data/crm_stage.xml',
        'data/crm_team.xml',
        'data/website_view.xml',
        'data/website_page.xml',
        'data/website_menu.xml',
        'data/ir_model_data.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_tag.xml',
        'demo/crm_lead.xml',
        'demo/account_analytic_plan.xml',
        'demo/account_analytic_account.xml',
        'demo/project_project.xml',
        'demo/product_supplierinfo.xml',
        'demo/stock_lot.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/project_task.xml',
        'demo/project_task_post.xml',
        'demo/im_livechat_channel.xml',
        'demo/im_livechat_channel_rule.xml',
        'demo/website_ir_attachment.xml',
        'demo/website.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/helpdesk_ticket.xml',
        'demo/repair_order.xml',
        'demo/repair_order_confirm.xml',
        'demo/stock_picking_return.xml',
        'demo/ir_attachment_post.xml',
        'demo/x_project_task_worksheet.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'solar_installation/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
    'images': ['images/main.png'],
}
