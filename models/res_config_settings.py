from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ai_provider = fields.Selection(
        [
            ('openai', 'OpenAI (ChatGPT)'),
            ('gemini', 'Google Gemini'),
            ('groq', 'Groq Cloud (Llama 3)'),
            ('claude', 'Anthropic Claude')
        ],
        string="AI Provider",
        default='gemini',
        config_parameter='ai_product_description.ai_provider'
    )
    
    openai_api_key = fields.Char(
        string="OpenAI API Key",
        config_parameter='ai_product_description.openai_api_key',
    )
    openai_model = fields.Selection(
        [
            ('gpt-4o-mini', 'GPT-4o Mini'),
            ('gpt-4o', 'GPT-4o'),
            ('gpt-3.5-turbo', 'GPT-3.5 Turbo'),
        ],
        string="OpenAI Model",
        default='gpt-4o-mini',
        config_parameter='ai_product_description.openai_model',
    )
    
    gemini_api_key = fields.Char(
        string="Gemini API Key",
        config_parameter='ai_product_description.gemini_api_key',
    )
    gemini_model = fields.Selection(
        [
            ('gemini-flash-latest', 'Gemini Flash (Latest)'),
            ('gemini-3.5-flash', 'Gemini 3.5 Flash'),
            ('gemini-2.5-flash', 'Gemini 2.5 Flash'),
            ('gemini-pro-latest', 'Gemini Pro (Latest)'),
            # Keep legacy models below to prevent ValueError on existing DBs
            ('gemini-1.5-flash', 'Gemini 1.5 Flash (Sunset)'),
            ('gemini-1.5-pro', 'Gemini 1.5 Pro (Sunset)'),
            ('gemini-pro', 'Gemini 1.0 Pro (Sunset)'),
        ],
        string="Gemini Model",
        default='gemini-flash-latest',
        config_parameter='ai_product_description.gemini_model',
    )
    
    groq_api_key = fields.Char(
        string="Groq API Key",
        config_parameter='ai_product_description.groq_api_key',
    )
    groq_model = fields.Selection(
        [
            ('llama-3.3-70b-versatile', 'Llama 3.3 70B Versatile'),
            ('llama3-8b-8192', 'Llama 3 8B 8192'),
        ],
        string="Groq Model",
        default='llama-3.3-70b-versatile',
        config_parameter='ai_product_description.groq_model',
    )
    
    claude_api_key = fields.Char(
        string="Claude API Key",
        config_parameter='ai_product_description.claude_api_key',
    )
    claude_model = fields.Selection(
        [
            ('claude-3-5-sonnet-latest', 'Claude 3.5 Sonnet (Latest)'),
            ('claude-3-5-haiku-latest', 'Claude 3.5 Haiku (Latest)'),
            ('claude-3-opus-latest', 'Claude 3 Opus (Latest)'),
        ],
        string="Claude Model",
        default='claude-3-5-sonnet-latest',
        config_parameter='ai_product_description.claude_model',
    )
    
    max_tokens = fields.Integer(
        string="Max Tokens",
        default=300,
        config_parameter='ai_product_description.max_tokens',
    )
