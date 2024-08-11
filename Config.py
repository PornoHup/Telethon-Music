import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24548143"))
    API_HASH = os.environ.get("API_HASH", "6cba049c135a0393615878ea1e3c9443")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7356145623:AAEfeB8yGbQMd_CIeAuMGUQalj6gob7MSXI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgF2ky8AjSzO6Wbk5lzM3wXSPdcFm7p0pcupRNkmOdmweQGt15jlGgWAWkNvys3ddjLU-IpPilm-LOpc1qJx07N4wFmgvyt46BSpguHnxRhoyzBNWZeJx47v1c1rAJzCIMNAUgpdfA308oC-xA3Z6SQxvx7HMmeMjOiHf-pxrvPQpr9paB0hDlPHpUookO6xO_8b4quOOT-EUnGRIs70-998l0xIRzoQsqNoFcNv2VGq6jy98l8xsUA7ThEJPnaeMTrxI-5I_4fBQ9FBrA0IbdUpCYPubwf_jqCk17nFLf2edZh1KLQ6w0mXaDXXvrHbvZQd5cKl0vWbhI_QDGwS8ILGs7YyoAAAAAGLGQbjAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", "HRKU-9f135b26-5fa2-443d-aa24-3563d5e6c00a")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NezrinNmusicRobot")
    SUPPORT = os.environ.get("SUPPORT", "nezrinsupp") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "nezrinlogo") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7423909421")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
