

import discord
from discord.ext import commands
from bot_token import bot_token
from keras_code import detected_valorant_agents
import os
from ajan_sözlük import detected_valorant_agents


# Discord intents ve bot ayarları
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Bot hazır olduğunda bir mesaj yaz
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Basit bir merhaba komutu
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'selam ben bir botum {bot.user}!')

# "he" komutu
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

# Valorant ajanlarını algılama komutu
@bot.command()
async def detect(ctx):
    if ctx.message.attachments:
        await ctx.send(f'Algılama başladı!')

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"

            # Fotoğraf kaydetme
            await attachment.save(file_path)

            # Dosya formatı kontrolü (sadece resimler)
            if not file_name.endswith(('png', 'jpg', 'jpeg', 'gif')):
                await ctx.send(f"Geçersiz dosya formatı! Lütfen bir resim dosyası yükleyin.")

            # Model ile tahmin yapma
            classname, score = detected_valorant_agents(
            file_path,  
            "converted_keras/keras_model.h5", 
            "converted_keras/labels.txt"
            )
            print(classname)
            await ctx.send(f'Tahmin edilen ajan: {classname} (Güven Skoru: {score:.2f})')
            
            

            # Dosya kaydedildi mesajı
            await ctx.send(f'Dosya kaydedildi ve işleme alındı!')

    else:
        await ctx.send(f'Bu komutla birlikte bir fotoğraf da yüklemelisiniz!')
        
    if classname == 'neon':
        await ctx.send("""Düellocu rolündeki bu karakter elektro ok ile düşmanlarını sersemletir,
yüksek devir ile daha hızlı yol alır,
hız şeridi ile hem görüşü engelleyen hem de düşmana hasar veren duvar örer ve ulti yeteneği ile düşmanlarına ölümcül saldırılar yapar.""")
    elif classname == 'yoru':
        await ctx.send("""Yoru’nun uzmanlığı düşmanlarını farklı şekillerde kandırabilmesi.
Bir boyut parçacığını koparıp fırlattığı kör nokta ile düşmanlarını kör ediyor.
Bir boyut geçidi küresi kuşandığı çatkapı ile küreyi konumlandırdığı yere ışınlanıyor.
Düşmanları kandırmak için kullandığı fake at ile istediği yöne ve noktaya doğru ayak sesi çıkmasını sağlıyor.
Ulti yeteneği boyutlararası geçiş ise onu düşmanları tarafından hem görünmez, hem de etkilenmez hale getiriyor.""")
    elif  classname == 'chamber':
        await ctx.send("""Gözcü rolündeki bu karakter kelle avcısı ile ağır bir tabanca kuşanır, 
        buluşma ile belli bir noktaya ışınlanabilir, 
        kartvizit ile düşmanlarını yavaşlatır ve ulti yeteneği ile öldürücü bir keskin nişancı tüfeği kuşanır.""")
    elif  classname == 'cypher':
        await ctx.send("""Düşmanın nerede olduğunu tespit etmek için doğmuş Cypher. 
        Etkili şekilde kullanabilmek için bol antrenman isteyen ajanın siber kafes yeteneği sayesinde görüşü engelleyen ve düşmanı içine hapseden dairesel alanlar oluşturuluyor. Hedef alınan noktaya yerleştirilen gizli kamera sayesinde düşmanları gözlemlemek, hatta işaretleyici iğne atmak mümkün.
        Atıldığı noktadan karşıya hat çeken bubi tuzağı, yakalanan rakibi sarsıp görünür kılıyor. Ulti yeteneği nöron hırsızı ise ölen bir düşmanı kullanarak, adeta sorgulayarak diğer düşmanların konumunu ortaya çıkarıyor.""")

    elif  classname == 'raze':
        await ctx.send("""Oyunun kapalı beta sürecinde en çok tartışma yaratan ajan Raze olmuştu.
Bunun nedeni ise Valorant’ın temel yapısına aykırı özellikleri.
Tamamı hasar vermeye yönelik yeteneklere sahip Raze’in patlayıcı çantası düşmana hasar verirken, kendisini yukarı fırlatıyor.
Kullanım şekli kısıtlanan renk tesirli bomba ile düşmanlar kolayca avlanıyor. Gördüğü düşmana odaklanan ve vurulmadığı takdirde kolayca skor alabilen bombot yüzünden rakipler paniğe kapılabiliyor.
Ultisi ise bir hamlede “ace” aldırabilen nefes kesen (roketatar) ki tüm bu özellikler bir araya geldiğinde oynaması en kolay karakterlerden biri sayılabilir Raze.""")


    elif  classname == 'brimstone':
        await ctx.send("""Oyuna yeni başlayan herkesin ilk tercihi olması gereken bir ajan.
Bunun nedeni yeteneklerinin hem kolay kullanılması, hem de gayet etkili olması.
İlk olarak yakıcı özelliği sayesinde kısa süreliğine belli bir zemini alevle kaplıyor.
Takıma hareket alanı sağlayan dumanlı hava sahası ile ayrı ayrı ya da eş zamanlı olarak üç duman bulutu atıyor.
Yere bıraktığı kuvvet işareti sayesinde silahların atış hızını artırıyor.
Ultisi uydu saldırısı ise belli bir alandaki düşmanlara lazerle yüksek miktarda hasar veriyor.""")


    elif  classname == 'jett':
        await ctx.send("""Oyundaki en hareketli karakter olan Jett’i kontrol edebilmek ve etkili kullanabilmek uzmanlık gerektiriyor.
Ona hareket kabiliyeti veren özelliklerden hafifle ile havaya sıçramak, rüzgar gibi ile hareket edilen yöne ya da ileriye atılmak mümkün.
Bu özellikler rakibin görüşünü engelleyen duman bulutu ile beraber kullanıldığında bir hayli etkili oluyor.
Jett’in ultisi keskin fırtına ise ona fırlatılabilir beş bıçak veriyor. Bıçaklar tek tek ya da topluca atılabiliyor ve bir düşmanı öldürünce yenileniyor.
Nişan alma kabiliyetine fazlasıyla güvenenler için ideal.""")

    elif  classname == 'phonix':
        await ctx.send("""Oynaması en eğlenceli karakterlerden biri Phoenix ancak onu etkili şekilde kullanmak için biraz pratik gerekiyor.
Düellocu rolündeki bu karakterin ördüğü ateşten duvar ile hem görüş engelleniyor, hem de duvara temas eden düşmana hasar veriliyor.
Sola ve sağa fırlatılabilen falso ile düşmanlar kısa süreliğine kör edilirken, atıldığı zeminde belli bir süre kalarak düşmana hasar veren yakar top düşmanı durdurmak için bire bir.
Phoenix’i eğlenceli kılan yakardöner ultisi ise kontrol edilebilir bir klon yaratarak kısa süreliğine adeta iki kişilik oynamayı mümkün kılıyor.""")
        
    
    elif  classname == 'sage ':
        await ctx.send("""Oyundaki en etkili destek ajanlarından biri, belki de birincisi. Öncelikle bariyer küresi yeteneği sayesinde buzdan bir duvar örerek koridorları kapatabiliyor. Zeminde etkili olan yavaşlatan küre ile geçiş yollarını buzla kaplıyor. Hem kendi, hem de takım arkadaşları üzerinde kullanabildiği can küresi ile iyileştirme sağlıyor.
En çarpıcı yeteneği diriliş sayesinde ise ölen bir takım arkadaşının cesedini hedef alarak onu yeniden hayata döndürüyor.""")

    elif  classname == 'sova':
        await ctx.send("""Farklı özelliklere sahip oklarıyla adeta avcı rolünde bir ajan.
Oklardan önce bahsedilmesi gereken baykuş dron cihazı ile haritada ufak bir gezintiye çıkmak ve düşmanları işaretleyen iğneler atmak mümkün.
Sova’nın patlayıcı özelliğe sahip şok oku atıldığı yerin yakınındaki düşmanlara hasar veriyor, keşif oku saplandığı noktayı gören düşmanları ortaya çıkarıyor, ulti yeteneği avcının hiddeti ise duvarların içinden geçen oklarla düşmanlara hasar verip onların konumlarını görünür kılıyor.""")

    elif  classname == 'breach':
        await ctx.send("""Tüm yetenekleriyle düşmanları sersemletmeyi amaçlayan bir ajan.
Breach’in gözkamaştıran özelliği sayesinde duvarların içinden geçen bir patlama oluşturup düşmanları kör etmek mümkün.
Benzer şekilde kullanılan artçı sarsıntı ile etki alanı içindeki düşmanlara hasar veriliyor.
Fay hattı yeteneği, etki alanı ve alan hattı üstündeki tüm oyuncuları sarsarak sersemletiyor.
Breach’in ultisi zelzele ise koni biçimindeki bir alanda düşmanları sarsıyor ve havaya savuruyor.""")

    elif  classname == 'omen':
        await ctx.send("""Karşı takımda bir Omen varsa huzur içinde mücadele etmeniz hiç kolay değil.
Neden mi? Birincisi, duvarlardan geçen paranoya gölge atışı sayesinde düşmanları kör edebilmesi.
İkincisi, düşmanları kör eden karanlık örtü (gölge küresi) fırlatabilmesi.
Üçüncüsü, gizli adım sayesinde belli bir menzile kadar ileri doğru ışınlanabilmesi.
Ve en önemlisi de gölgelerin içinden ultisi sayesinde haritanın istediği yerine ışınlanabilmesi.
Işınlanma sesi duyulduğu an Omen’in nereden çıkacağı tam bir muamma!""")

    elif  classname == 'reyna':
        await ctx.send("""Oyuna 2 Haziran itibariyle gelen bir ajan.
Tam anlamıyla bir “ruh emici” olan Reyna, sömür ile öldürdüğü düşmanların kısa süreliğine geride bıraktıkları ruh kürelerini tüketerek canını yeniliyor ki ultisi aktifken bu otomatik olarak gerçekleşiyor.
Bir diğer yeteneği azlet ile ruh küresi tüketerek kısa süreliğine silahını bırakıyor, saydamlaşıyor ve kurşun geçirmez oluyor ki yine ultisi aktifken tamamen görünmez oluyor.
Görüşü engelleme amaçlı kem göz yeteneği sayesinde kuşandığı küreyi ileri doğru fırlatıp küreye bakan düşmanların uzağı görmesini engelliyor.
Ulti yeteneği imparatoriçe ise belli bir süreliğine ateş etme ve şarjör yenileme hızını artırıyor, düşman öldürdükçe de yeteneğin süresini yeniliyor""")

    elif  classname == 'viper':
        await ctx.send("""Zehirle beslenen, zehirle öldüren bir ajan Viper.
Fırlattığı asit havuzu ile düşmana hasar veren kimyasal bir alan oluşturuyor.
Atıldığı noktada tur boyunca tekrar tekrar kullanılabilen zehir bulutu düşmana hasar veriliyor.
Gaz salgılayan zehir perdesi ile hem görüşü engelliyor, hem de alan kontrolü sağlıyor.
Ulti yeteneği Viper’ın ini ise Viper’ın çevresindeki geniş bir alanı kaplayan kimyasal bulut oluşturuyor ve bu alan düşmana hasar verirken görüşü de kısıtlıyor.""")

    elif  classname == 'killjoy':
        await ctx.send("""Bir dahi olarak nitelendirilen Killjoy’un elinde kendi icadı olan ilginç ekipmanlar mevcut.
Zemine yerleştirdiği alarm botu, menziline giren düşmanların peşine düşerek patlıyor ancak istendiği takdirde geri çağrılıyor.
Yine zemine yerleştirilen taret 180 derecelik bakış açısına giren düşmanlara ateş etmeye başlıyor.
Nanosürü bombası etkinleştirildiği zaman düşmana hasar veren nano robot sürüsünü serbest bırakıyor.
Ulti yeteneği tecrit ise düşmanın hareket kabiliyetini kısıtlıyor.""")

    elif  classname == 'skye':
        ("""Avustralya’dan gelen Skye’ın en büyük yardımcısı, beraberinde getirdiği vahşi hayvanları.
Bir tazmanya kaplanını kontrol ettiği av peşinde ile ileri atılarak düşmana hasar veriyor.
Hedef alınan noktaya doğru yol alan bir şahin gönderdiği kılavuz ışık sayesinde düşmanı kör eden bir patlama gerçekleştiriyor.
Belli bir menzilde etkili olan doğanın şifası ile takım arkadaşlarını iyileştiriyor.
Ulti yeteneği izsürenler ise en yakınındaki üç düşmana onların görüşünü kısıtlayan izsüren göndermesini sağlıyor.""")

    elif  classname == 'astra':("""Astra kozmosun enerjisini kullanarak savaş meydanlarını lehine kullanabiliyor.
Astral Yolcu halindeyken nova darbesi sayesinde etki alanındaki düşmanları sersemletir, yıldız bulutu ile görüşü engelleyen küreler yaratır, çekim alanı ile düşmanları içine çeken bir alan oluşturur. Tüm yetenekleri gibi yine Astral Yolcu halindeyken kullanabildiği ulti yeteneği kozmik ayrım ise istenen iki nokta arasına hem kurşunları engelleyen, hem de sesi bastıran bir duvar çeker.""")

    elif  classname == 'kayo':("""Öncü rolündeki bu karakter flaş bellek ile düşmanlarını kör eder, sıfır noktası ile menzilindeki düşmanları sindirir, parça tesirli ile düşmanlarına hasar verir ve ulti yeteneği ile devasa bir alandaki düşmanlarını kısa süreliğine sindirir.""")
        
# Botu başlatma
bot.run(bot_token)