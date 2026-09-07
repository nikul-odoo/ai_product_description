# All-in-One AI Product Description Generator

An Odoo 17 & 18 compatible module that leverages top-tier Artificial Intelligence models to automatically generate engaging, clean, and HTML-formatted product descriptions. 

With built-in support for **OpenAI (ChatGPT)**, **Google Gemini**, **Groq (Llama 3)**, and **Anthropic Claude**, you can easily craft the perfect product pitch with the tone of your choice.

## Key Features
* **Multi-Provider Support:** Easily switch between OpenAI, Google Gemini, Groq, and Anthropic Claude APIs.
* **Tone Selection:** Choose from predefined tones including Professional, Catchy & Marketing, Casual, or Technical / Detailed.
* **Smart Formatting:** The AI is instructed to return clean HTML with bullet points, ensuring the output drops perfectly into your Odoo product views without messy markdown artifacts.
* **Seamless Integration:** A convenient "Generate AI Description" button is added directly to the Product Template form view.

## Installation
1. Download or clone this module into your Odoo `addons` directory.
2. Restart your Odoo server.
3. Turn on "Developer Mode" in Odoo and click **Update Apps List**.
4. Search for `AI Product Description` and click **Install**.

## Configuration
Before using the module, you must configure your preferred AI provider's API key:
1. Navigate to **Settings > General Settings**.
2. Scroll down to the **AI Product Description** section.
3. Select your **AI Provider** from the dropdown menu.
4. Enter your provider's API Key (e.g., `sk-...`).
5. Select your preferred Model and configure the Max Tokens if desired.
6. Click **Save** in the top left corner.

## Usage
1. Open any Product from your **Sales** or **Inventory** apps (e.g., `Sales > Products > Products`).
2. At the top of the Product form view, click the **Generate AI Description** button.
3. A wizard will appear. Enter a few comma-separated keywords or features describing your product.
4. Select the Tone and the Target Field (Sales Description or Internal Notes).
5. Click **Generate & Apply**. The AI will generate the content and automatically apply it to the product!

## Author & Support
**Author:** Nikulkumar Alagiya  
**Support:** nikulkumar.alagiya@gmail.com

If you encounter any issues or have feature requests, feel free to reach out via email!
