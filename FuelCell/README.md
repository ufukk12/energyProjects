ELEKTRİKLİ ARAÇLAR İÇİN METANOL BUHAR REFERMASYONU (MSR) TABANLI MENZİL UZATICI SİSTEM TASARIMI VE OPTİMİZASYONU
    
    Bu proje; elektrikli araçlar için batarya ağırlığını artırmadan menzili teorik olarak 1000 km üzerine çıkaran, Metanol Buhar Reformasyonu (MSR) tabanlı bir Menzil Uzatıcı (Range Extender) sisteminin uçtan uca tasarım sürecini kapsamaktadır. Bu sistemde öncelikle enerji yoğunluğunun maksimum olması için Metanol + İzopropanol karışımının kullanılmasını hedeflemiştim fakat daha sonradan fiyat performans açısından ipanın zarar oluşturduğuna kanaat getirip sadece metanol karışımı ile devam ettim. 

    1. SİSTEM MİMARİSİ VE DEPO YAPILANDIRMALARI
        Bu sistemde 2 farklı depo bulunacak bunlardan biri yakıt için diğeri ise buhar refermasyonu sağlaması amacıyla su deposu olacak. Yakıt deposu , su deposu ve yakıt pili birleşince sisteme ekstra bir yük bindirecek ve aracta bir performans düşüklüğü yaratacak. Bu performans düşüklüğünün sistem sayesinde kazanacağımız enerji miktarının önüne geçmemesi için en uygun depo hacmini belirlememiz gerekir. 

                - Yakıt Hücresi olarak Yüksek Sıcaklıklı PEM (HT-PEM) kuıllanılacak ve bunların verimini ortalama olarak %40 belirledim.

                - Öncelikle temsili olarak yakıt depo hacmine 100x diyelim. yakıt olarak metanol kullanacağımızdan dolayı teorik olarak 53,4x L su deposu gerekir ancak uygulanabilirlik acısından 55x L almak daha mantıklıdır. Burada öncelikle 3 tane x değeri için (0.4 , 0.5 , 0.6) sisteme bindirdiğimiz toplam yükü ve bu depodaki yakıtın sağladığı toplam enerjiyi (enerji yoğunluğu * yakıt depo kütlesi) bulmamız gerekir...

                        |    x  değerleri | Sisteme Bindirilen Top Yük | Toplam Enerji Katkısı |
                        |-----------------|----------------------------|-----------------------|
                        |      0.4        |            59.05kg         |       70.24kWh        |
                        |      0.5        |            73.81kg         |       87.8kWh         |
                        |      0.6        |            88.57kg         |       105.36kWh       |

                 
                 - Bu değerleri kullanarak Öncelikle Enerji Katkısını Sisteme bindirilen toplam yüke bölerek temsili bir verim(kWh/kg) elde edip bu x - (kWh/kg) noktalarından oluşan veri tablosu için lagrange interpolasyonu uygulayarak 2. dereceden bir polinom çıkartıp bu polinomun türevinin 0 olduğu noktayı bularak optimum x değerini bulmayı amaçladım. Hesaplamalar ile yaklaşık olarak Lagrange polinomunu P(x) = -0.7x² + 1.28x + 0.24 olarak buldum. Matematiksel olarak polinomu yorumlarsak bu polinomun grafiğinin kolları aşağı doğru bakar yani bu polinomun tepe noktası, bizim için optimum değerdir. Türevini alıp 0 a eşitlersek tepe noktasını    x = 0.914 bulmuş oluruz. Matematiksel olarak bu yöntem sonucunda bu değer optimum değer olsa bile fiziksel olarak ağırlığı çok fazla artırdığından dolayı bu değeri kullanamayız. 
                 
                - Alternatif bir yöntem olarak "Kısıtlı Optimizasyon Yöntemini" kullandım. Bu yöntemle beraber x değerinin yaklaşık olarak x = 0.677 belirledim. Bununla beraber depo kapasitelerini ve elde edeceğimiz teorik elektrik miktarını aşağıda belirttim 

                        |      Depolar     |     Depo Kapasiteleri    |                    
                        |------------------|--------------------------|         Bununla birlikte teorik olarak 118.9kWh elektrik enerjisi üretebiliriz.
                        |   Yakıt Deposu   |         67.7 L           |
                        |   Su Deposu      |        37.24 L           |


    2. METANOL BUHAR REFORMASYONU (MSR) VE HT-PEM ENTEGRASYONU
            -Sistemin verimliliğinin merkezinde, Yüksek Sıcaklıklı PEM (HT-PEM) yakıt pili ve "Autothermal" (kendi kendini besleyen) ısı döngüsü bulunmaktadır. Sistem operasyonu iki ana faza ayrılır:

               A. Soğuk Başlatma Fazı: Sistemin rejim sıcaklığına ulaşması için araçtaki ana bataryadan (55 kWh) kısa süreliğine beslenen bir elektrikli ön ısıtıcı (PTC Heater) kullanılır. Reformer ünitesini 250C dereceye çıkarmak için gereken elektriksel yük yaklaşık 0.4kWh tir. (Toplam batarya kapasitesinin %1'inden az). Sistem hidrojen üretimine başladığında bu elektrik tüketimi sıfırlanır.
               B. Autothermal Rejim ve Bedava Isı Kaynakları: Sistem çalışmaya başladıktan sonra tamamen kendi atık ısısıyla reaksiyonu sürdürür

                   2.1 : Buharlaştırma: HT-PEM yakıt pilinden çıkan 160C - 200C seviyesindeki atık ısı ve batarya soğutma suyundan alınan düşük dereceli ısı, tanktan gelen sıvı metanol-su karışımını buhar fazına geçirmek için kullanılır.

                   2.2 : Reformasyon: Yakıt pilinde tüketilemeyen %15-20 oranındaki artık hidrojen, bir katalitik yakıcıda yakılarak reformerın endotermik reaksiyonu  için gereken 250C derecelik ana termal gücü sağlar.

                   2.3 : CO Toleransı: HT-PEM'in 30.000ppm kadar Karbonmonoksit (CO) toleransı sunması sayesinde, ağır ve maliyetli gaz saflaştırma ünitelerine olan ihtiyaç ortadan kalkmış ve termal kütle minimize edilmiştir.
 
 

    3. ENERJİ YÖNETİM SİSTEMİ 
            - Sistemin reformasyon ve hidrojen üretim işlemlerinin karmaşıklığını , batarya sağlığının korunması amacıyla batarya dolum an ve sürelerinin belirlenmesi amacıyla sisteme entegre edilecek kapsamlı bir yönetim sistemi tasarlanacaktır. Bu sistem gerektiğinde sistem sağlığının korunması amacıyla kullanıcıya bakıma gidilmesi bildirimini verecek ve önlemler alacak , gerektiğinde batarya sağığının korunması amacıyla şarj değeri %20 altına inmeye basladığında şarj işlemini başlatacak ve bileşen ömürlerini ciddi ölçüde artıracaktır. Bu enerji yönetim sistemi python tabanlı olacaktır

               
                 3.1 : Batarya Sağlığı : Batarya sağlığından korunması ve menzil uzatıcı sistemin gerektiğinde kullanılmadı amacıyla şarj işlemi duruma göre kullanıcının da isteği doğrultusunda %20 seviyelerinde başlayacak , %85 Seviyelerinde bitecek. 55kWh batarya ile çalışan bir aracı düşünürsek ve bataryanın kullanılabilir kapasitesini 50kWh olarak kabul edersek %20 seviyelerinde 10kWh elektrik enerjisi kaldığını , %85 seviyelerine çıkabilmesi için 42.5kWh elektrik enerjisi barındırması gerektiğini ve dolayısıyla yakıt piliyle 32.5kWh elektrik enerjisi üretilmesi gerektiğini çıkarabiliriz. EMS sisteminin görevi ise şarj seviyesi %25 seviyelerine geldiğinde ;
                   
                         - Eğer en yakın şarj istasyonu , 45km ve daha fazla uzaklıkta ise (hızına göre 30km değerine kadar inebilir...) (batarya şarjını %10 - %2) seviyelerine getirecek kadar fazla) yakıt pili sağlığı kısmında anlatacağım kontrolleri devreye sokup uygunsa kullancıya " Yakıt Pili Devreye Giriyor... " şeklinde bilgi vererek yakıt pilini devreye alacak.                   

                         - Eğer mesafe 45km den daha az ise kullanıcıya " Şarj seviyeniz %20 seviyesinin altına inmek üzere , batarya sağlığı içib dilerseniz en yakın şarj istasyonuna gidebilir ya da yakıt pilini devreye sokabilirsiniz... " uyarısı verecek.

                 

                3.2 : Yakıt ve Su Kontrolü : Yakıt pili devreye gireceği zaman öncelikle yakıt ve su kontrolü yapılır , bataryanın elektrik enerjisi ihtiyacı yukarıdaki hesaplamaaya göre 32.5kWh olarak kabul edersek depoda 18.51L yakıt bulunması gerekir (depoyu tam dolu kabul edersek V@32.5kWh = (67.7 × 32.5)/118.9) ) bu 18,51L yakıta karşılık 10,19L su gerekir ( V@su = (37.24 × 18.51)/67.7 ) bu veriler ışığında 1L yakıt için 0.551L su gerektiğini çıkarabiliriz. 

                        - En uç ihtimal olarak kullanıcı şarj seviyesi sadece %20 seviyelerine geldiğinde yakıt pilini kullanacağını varsayarsak 32,5kWh lik enerji için 18,51L yakıt cekmesi gerekir. 67,7 / 18,51 = 3,66 dan dolayı tam dolu bir yakıt ve su deposu ile 3 kere şarj işlemi gerçekleştirilebilecektir. Depodan 18,51L yakıt çekildiğini anlayabilmek için depolara koyulacak sensörler ile tespit edilecek. Onun dısında herhangi bir %x seviyesinde (85 > x > 20) kullanıcı şarj işlemi gerçekleştirmek isterse ayrıca x seviyesinden 85 seviyesine olacak şekilde gerekli metanol ve su miktarını hesaplayıp (depoada yeterli miktarda metanol || su yok ise depodaki aL metanol için 0,551aL su oranına göre) max yakıtı cekip işlemlere devam edecek. 
