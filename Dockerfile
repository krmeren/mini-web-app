# Base image olarak Python 3.14 slim kullanıyoruz
FROM python:3.14-slim

# Çalışma dizinini belirle
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "app.py"]