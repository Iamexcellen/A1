import qrcode

url = "https://genesisthebeginning.streamlit.app/"

img = qrcode.make(url)
img.save("lifestyle_app_qr.png")

print("二维码已生成：lifestyle_app_qr.png")
