from pydantic_settings import BaseSettings, SettingsConfigDict

# creating data validation settings for the app 
class Settings(BaseSettings):
     model_config = SettingsConfigDict(env_file=".env", extra="ignore")
     DATABASE_URL : str
     SECRET_KEY : str
     ACCESS_TOKEN_MINS_BEFORE_EXPIRY : int = 300

     SMTP_HOST : str = ""
     SMTP_PORT : str = 842
     SMTP_USER : str = ""
     SMTP_PASSWORD : str = ""
     SMTP_EMAIL_FROM : str = ""

     GEMINI_API_KEY : str
     GEMINI_MODEL : str = "gemini-1.5-flash"

     APP_NAME : str = "In House Language AI"
     FRONTEND_URL : str = "http://localhost:3000"

app_settings = Settings()