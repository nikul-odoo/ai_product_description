import requests
import json
import re
from odoo import api, fields, models
from odoo.exceptions import UserError

class AIDescriptionWizard(models.TransientModel):
    _name = 'ai.description.wizard'
    _description = 'Generate AI Description Wizard'

    @api.model
    def _default_ai_provider(self):
        return self.env['ir.config_parameter'].sudo().get_param('ai_product_description.ai_provider', 'gemini')

    product_tmpl_id = fields.Many2one('product.template', string='Product', required=True)
    product_name = fields.Char(related='product_tmpl_id.name', string='Product Name', readonly=True)
    ai_provider = fields.Selection(
        [
            ('openai', 'OpenAI (ChatGPT)'),
            ('gemini', 'Google Gemini'),
            ('groq', 'Groq Cloud (Llama 3)'),
            ('claude', 'Anthropic Claude')
        ],
        string="AI Provider",
        default=_default_ai_provider,
        readonly=True
    )
    keywords = fields.Text(string='Keywords', required=True, placeholder="e.g. 100% cotton, breathable, slim fit")
    tone = fields.Selection(
        [
            ('professional', 'Professional'),
            ('catchy', 'Catchy & Marketing'),
            ('casual', 'Casual'),
            ('technical', 'Technical / Detailed')
        ],
        string='Tone',
        default='catchy',
        required=True
    )
    target_field = fields.Selection(
        [
            ('description_sale', 'Sales Description'),
            ('description', 'Internal Notes')
        ],
        string='Target Field',
        default='description_sale',
        required=True
    )

    def action_generate_and_apply(self):
        self.ensure_one()
        
        Config = self.env['ir.config_parameter'].sudo()
        provider = self.ai_provider
        max_tokens = int(Config.get_param('ai_product_description.max_tokens', default=300))

        prompt = (
            f"Generate a compelling, well-formatted product description in clean HTML format with bullet points for key features. "
            f"Product Name: {self.product_name}, Keywords/Specs: {self.keywords}, Tone: {self.tone}. "
            f"Return only the HTML body without markdown backticks."
        )

        description = ""

        try:
            if provider == 'openai':
                api_key = Config.get_param('ai_product_description.openai_api_key')
                model = Config.get_param('ai_product_description.openai_model', default='gpt-4o-mini')
                if not api_key:
                    raise UserError("OpenAI API key is not configured. Please set it in Settings.")

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                data = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are an expert copywriter."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                }
                response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                description = result['choices'][0]['message']['content'].strip()

            elif provider == 'groq':
                api_key = Config.get_param('ai_product_description.groq_api_key')
                model = Config.get_param('ai_product_description.groq_model', default='llama-3.3-70b-versatile')
                if not api_key:
                    raise UserError("Groq API key is not configured. Please set it in Settings.")

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                data = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are an expert copywriter."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                }
                response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                description = result['choices'][0]['message']['content'].strip()

            elif provider == 'gemini':
                api_key = Config.get_param('ai_product_description.gemini_api_key')
                model = Config.get_param('ai_product_description.gemini_model', default='gemini-flash-latest')
                if not api_key:
                    raise UserError("Gemini API key is not configured. Please set it in Settings.")

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                data = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are an expert copywriter."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                }
                response = requests.post("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions", headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                if 'choices' in result and result['choices']:
                    description = result['choices'][0]['message']['content'].strip()
                else:
                    raise UserError("Unexpected response format from Gemini API.")

            elif provider == 'claude':
                api_key = Config.get_param('ai_product_description.claude_api_key')
                model = Config.get_param('ai_product_description.claude_model', default='claude-3-5-sonnet-latest')
                if not api_key:
                    raise UserError("Claude API key is not configured. Please set it in Settings.")

                headers = {
                    "Content-Type": "application/json",
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01"
                }
                data = {
                    "model": model,
                    "system": "You are an expert copywriter.",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                }
                response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                description = result['content'][0]['text'].strip()

        except requests.exceptions.HTTPError as e:
            error_msg = f"API Error: {e.response.text}" if e.response is not None else str(e)
            raise UserError(f"Failed to generate description.\n{error_msg}")
        except Exception as e:
            if isinstance(e, UserError):
                raise e
            raise UserError(f"An unexpected error occurred: {str(e)}")

        # Strip markdown code fences if present (e.g. ```html ... ```)
        description = re.sub(r'^```(html)?\s*', '', description, flags=re.IGNORECASE)
        description = re.sub(r'\s*```$', '', description)

        if self.target_field == 'description_sale':
            self.product_tmpl_id.description_sale = description
        elif self.target_field == 'description':
            self.product_tmpl_id.description = description

        return {'type': 'ir.actions.act_window_close'}
