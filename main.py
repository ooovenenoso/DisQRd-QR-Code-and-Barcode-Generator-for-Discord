# DisQRd: QR Code Generator
# Author: ooovenenoso

import os
import discord
from discord.ext import commands
import qrcode
import barcode
from barcode.writer import ImageWriter

# Set up Discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.typing = True
intents.message_content = True  # Add this line to enable the message contents intent

# Create Discord bot
bot = commands.Bot(command_prefix="!", intents=intents)

# QR code generation command
@bot.command()
async def qr(ctx, url: str):
    """Generates a QR code for the given URL and sends it in the current channel as a PNG file.
    
    Usage: !qr <url>
    """

    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image to file
    with open("qr.png", "wb") as f:
        img.save(f)

    # Send QR code PNG in current channel
    await ctx.send("Here is your QR code in PNG format:", file=discord.File("qr.png"))

# EAN13 barcode generation command
@bot.command()
async def ean13(ctx, data: str):
    """Generates an EAN13 barcode for the given data and sends it in the current channel as a PNG file.
    
    Usage: !ean13 <data>
    """

    # Create EAN13 barcode object
    ean13 = barcode.get_barcode_class('ean13')(data, writer=ImageWriter())

    # Generate EAN13 barcode image
    ean13.save('ean13')

    # Send EAN13 barcode PNG in current channel
    await ctx.send("Here is your EAN13 barcode in PNG format:", file=discord.File("ean13.png"))

  
  # EAN8 barcode generation command
@bot.command()
async def ean8(ctx, data: str):
    """Generates an EAN8 barcode for the given data and sends it in the current channel as a PNG file.
    
    Usage: !ean8 <data>
    """

    # Create EAN8 barcode object
    ean8 = barcode.get_barcode_class('ean8')(data, writer=ImageWriter())

    # Generate EAN8 barcode image
    ean8.save('ean8')

    # Send EAN8 barcode PNG in current channel
    await ctx.send("Here is your EAN8 barcode in PNG format:", file=discord.File("ean8.png"))


# Code 39 barcode generation command
@bot.command()
async def code39(ctx, data: str):
    """Generates a Code 39 barcode for the given data and sends it in the current channel as a PNG file.
    
    Usage: !code39 <data>
    """

    # Create Code 39 barcode object
    code39 = barcode.get_barcode_class('code39')(data, writer=ImageWriter())

    # Generate Code 39 barcode image
    code39.save('code39')

    # Send Code 39 barcode PNG in current channel
    await ctx.send("Here is your Code 39 barcode in PNG format:", file=discord.File("code39.png"))

# Code 128 barcode generation command
@bot.command()
async def code128(ctx, data: str):
    """Generates a Code 128 barcode for the given data and sends it in the current channel as a PNG file.
    
    Usage: !code128 <data>
    """

    # Create Code 128 barcode object
    code128 = barcode.get_barcode_class('code128')(data, writer=ImageWriter())

    # Generate Code 128 barcode image
    code128.save('code128')

    # Send Code 128 barcode PNG in current channel
    await ctx.send("Here is your Code 128 barcode in PNG format:", file=discord.File("code128.png"))

# Help command
@bot.command()
async def hello(ctx):
    """Shows a list of available commands and their usage.
    
    Usage: !hello
    """

    commands_list = [
        ("!qr <url>", "Generates a QR code for the given URL."),
        ("!ean8 <data>", "Generates a EAN8 barcode for the given data."),
        ("!ean13 <data>", "Generates an EAN13 barcode for the given data."),
        ("!code39 <data>", "Generates a Code 39 barcode for the given data."),
        ("!code128 <data>", "Generates a Code 128 barcode for the given data."),
        ("!hello", "Shows a list of available commands and their usage."),
    ]

    commands_text = "\n".join([f"{c[0]}: {c[1]}" for c in commands_list])
    await ctx.send(f"DisQRd: QR Code Generator\n\nAvailable commands:\n{commands_text}")

# Info command
@bot.command()
async def info(ctx):
    """Shows information about the bot.
    
    Usage: !info
    """

    await ctx.send("DisQRd: QR Code Generator\nAuthor: ooovenenoso\n\nhttps://github.com/ooovenenoso/DisQRd-QR-Code-and-Barcode-Generator-for-Discord")

# Run bot
token = os.environ["TOKEN"]
bot.run(token)
