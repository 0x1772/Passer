Şifre Yöneticisi

Bu, kullanıcıların web siteleri, uygulamalar ve diğer hesaplara ait şifreleri güvenli bir şekilde depolayabileceği bir Python uygulamasıdır. Kullanıcılar bu uygulama aracılığıyla şifrelerini oluşturabilir, kaydedebilir ve gerektiğinde şifrelerini çözebilirler. Şifreler, AES-256 şifreleme algoritması kullanılarak şifrelenir.
Kullanım

Uygulamayı çalıştırmadan önce, uygulamanın bulunduğu dizinde aşağıdaki komutu kullanarak gereksinimleri yüklemelisiniz:

pip install -r requirements.txt

Şifre Oluşturma

Şifre oluşturmak için, aşağıdaki komutu kullanabilirsiniz:

python password_generator.py

Bu komut, rastgele bir şifre oluşturacak ve bu şifreyi konsola yazdıracaktır.
Şifre Kaydetme

Şifreleri kaydetmek için, aşağıdaki komutu kullanabilirsiniz:

python password_manager.py store

Bu komut, sizden web sitesi adını, kullanıcı adını ve şifreyi isteyecektir. Bu bilgileri girdikten sonra, şifre AES-256 algoritması kullanılarak şifrelenecek ve passwords.json dosyasına kaydedilecektir.
Şifreleri Listeleme

Kaydedilmiş tüm şifreleri listelemek için, aşağıdaki komutu kullanabilirsiniz:

python password_manager.py list

Bu komut, passwords.json dosyasındaki tüm şifreleri çözecek ve web sitesi adlarını ve kullanıcı adlarını konsola yazdıracaktır.
Şifre Çözme

Kaydedilmiş bir şifreyi çözmek için, aşağıdaki komutu kullanabilirsiniz:

arduino

python password_manager.py get <website>

Bu komut, passwords.json dosyasındaki belirtilen web sitesi adına ait kaydedilmiş şifreyi çözecektir. Daha sonra, kullanıcı adını ve şifreyi konsola yazdıracaktır.
Şifre Silme

Kaydedilmiş bir şifreyi silmek için, aşağıdaki komutu kullanabilirsiniz:

arduino

python password_manager.py delete <website>

Bu komut, passwords.json dosyasındaki belirtilen web sitesi adına ait kaydedilmiş şifreyi silecektir.
Güvenlik

Bu uygulama, AES-256 şifreleme algoritması kullanarak şifreleri şifreler.
