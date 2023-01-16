# DisQRd: QR Code and Barcode Generator for Discord

![alt text](https://github.com/ooopoison/DisQRd/blob/main/image.jpg)

## Introduction
DisQRd is a powerful and easy-to-use Discord bot that generates QR codes and barcodes for any given data. The bot can generate QR codes for URLs, as well as EAN13, EAN8, Code 39 and Code 128,  barcodes for various types of data. Simply send the appropriate command in any Discord server or DM, and the bot will generate a code image and send it back to you.

## Installation

1. Install the required dependencies: `pip install -U discord qrcode barcode pillow`
2. Clone this repository: `git clone https://github.com/ooopoison/DisQRd`
3. Create a new bot in the Discord Developer Portal and obtain its token.
4. Set the `TOKEN` environment variable to your bot's token.
5. Run the bot: `python main.py`

## Usage

To use DisQRd, simply send one of the following commands in any Discord server or DM:

**Show all commands:** `!hello`

**QR code for URL:** `!qr <url>`

**EAN8 barcode:** `!ean8 <data>`

**EAN13 barcode:** `!ean13 <data>`

**Code 39 barcode:** `!code39 <data>`

**Code 128 barcode:** `!code128 <data>`

For example:

**!qr https://github.com/ooopoison/DisQRd**

**!ean13 123456789012**

**!code39 ABC123**

## Installation without code

[![Invite to Discord](https://img.shields.io/badge/Invite-to%20Discord-7289DA.svg)](https://discord.com/api/oauth2/authorize?client_id=1052240238388445194&permissions=2147650560&scope=bot)

## License

DisQRd is licensed under the MIT License. See [[LICENSE]](https://opensource.org/licenses/MIT) for more information.
