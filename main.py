# DisQRd: QR Code Generator
# Author: ooopoison

import os
import discord
from discord.ext import commands
import qrcode

# Set up Discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.typing = True
intents.message_content = True  # Add this line to enable the message contents intent

# Create Discord bot
bot = commands.Bot(command_prefix="/", intents=intents)

# QR code generation command
@bot.command()
async def qr(ctx, url: str):
    """Generates a QR code for the given URL and sends it in the current channel.
    
    Usage: /qr <url>
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

    # Send QR code image in current channel
    await ctx.send("Aquí está tu código QR:", file=discord.File("qr.png"))

# Run bot
token = os.environ["TOKEN"]
bot.run(token)
