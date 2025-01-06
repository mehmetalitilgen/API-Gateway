# **API Gateway (Flask)**

Bu proje, mikroservisler arasında yük dengeleme ve doğrulama için Flask ile yazılmış bir API Gateway'dir.

## **Özellikler**
- Kimlik doğrulama (JWT)
- Yük dengeleme stratejileri (Round Robin, Random, En Az Bağlantı)
- Redis ile rate limiting (istek sınırı)
- Sağlık kontrol endpoint’i

---

## **Çalıştırma Adımları**

### **1. Projenin Klonlanması**
Öncelikle projeyi bilgisayarınıza klonlayın:
```bash
git clone https://github.com/kullanici-adi/proje-adi.git
cd proje-adi
```
### **2. .env Dosyasını Oluşturma**
Proje klasörüne .env dosyasını ekleyin ve aşağıdaki ortam değişkenlerini yapılandırın:
```bash
SECRET_KEY=your-secret-key
REDIS_HOST=localhost  # Docker üzerinden Redis kullanılıyor
REDIS_PORT=6379
REDIS_DB=0
SERVICE_1=http://localhost:5000
SERVICE_2=http://localhost:5001
LOAD_BALANCER_STRATEGY=round_robin  # round_robin, random veya least_connections
```

### **3. Docker Üzerinden Redis Çalıştırma**
Redis sunucusunu çalıştırmak için aşağıdaki komutu çalıştırın:
```bash
docker run --name redis_container -p 6379:6379 -d redis
```

### **4. Gerekli Bağımlılıkların Yüklenmesi**
Gerekli Python bağımlılıklarını yüklemek için:
```bash
pip install -r requirements.txt
```

### **5. Flask Uygulamasının Çalıştırılması**
Uygulamayı başlatmak için:
```bash
python app.py
```

Herhangi bir sorunla karşılaşırsanız bana ulaşabilirsiniz! 😊







