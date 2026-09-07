{
    'name': 'AI Product Description',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Generate product descriptions using OpenAI, Gemini, Groq, and Claude',
    'description': """
        This module allows generating AI product descriptions using OpenAI, Google Gemini, Groq, and Anthropic Claude APIs.
        Easily generate HTML-formatted text for product sales descriptions or internal notes directly from the product template.
    """,
    'author': 'Nikulkumar Alagiya',
    'maintainer': 'Nikulkumar Alagiya',
    'depends': ['base', 'base_setup', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/product_template_views.xml',
        'wizard/ai_description_wizard_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'price': 0.00,
    'currency': 'USD',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
