# ----------------------------------------
# Cantilever Retaining Wall
# ----------------------------------------


# Gerekli kütüphaneler import ediliyor.
import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opsplt

# Çağırılan opensees komutları ile oluşturulan her şeyi temizle.
ops.wipe()

# Model oluşturacağımız uzayı tanımlıyoruz.
ops.model('basic','-ndm',2,'-ndf',2) # 2 yönde yer değiştirme, düzlem dışı yer değiştirmeler ve dönmeler kısıtlı.

# Düğüm noktaları koordinatları (m)
ops.node(1, 0.0,  0.0)
ops.node(2, 0.0,  0.5)
ops.node(3, 0.5, 0.0)
ops.node(4, 0.5, 0.5)
ops.node(5, 1.0, 0.0)
ops.node(6, 1.0, 0.5)
ops.node(7, 2.0, 0.0)
ops.node(8, 2.0, 0.5)
ops.node(9, 0.56, 1.5)
ops.node(10, 1.0, 1.5)
ops.node(11, 0.63, 2.5)
ops.node(12, 1.0, 2.5)
ops.node(13, 0.69, 3.5)
ops.node(14, 1.0, 3.5)
ops.node(15, 0.75, 4.5)
ops.node(16, 1.0, 4.5)


# Mesnet bilgileri
# Sistemde 6 adet kayıcı mesnet(ikisi 1 düğümünde) bulunmakta.
ops.fix(1, 1, 1)
ops.fix(2, 1, 0)
ops.fix(3, 0, 1)
ops.fix(5, 0, 1)
ops.fix(7, 0, 1)

# Malzeme tanımlama
ops.nDMaterial('ElasticIsotropic', 1, 32000000.0, 0.2)

# Eleman tanımlama
# Elemanlarımız üçgen eleman, düzlem-şekil değiştirme sistemi
ops.element('Tri31', 1, 1, 4, 2, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 2, 3, 4, 1, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 3, 3, 6, 4, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 4, 5, 6, 3, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 5, 5, 8, 6, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 6, 7, 8, 5, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 7, 4, 10, 9, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 8, 6, 10, 4, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 9, 9, 12, 11, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 10, 10, 12, 9, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 11, 11, 14, 13, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 12, 12, 14, 11, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 13, 13, 16, 15, 1.0, 'PlaneStrain', 1)
ops.element('Tri31', 14, 14, 16, 13, 1.0, 'PlaneStrain', 1)

# Zaman serisi tanımlama
ops.timeSeries("Linear", 1)

# Yük sınıfı tanımlama
# Tek tip yükümüz var.
ops.pattern("Plain", 1, 1)

# Yükler tanımlanır. (kN)
ops.load(7, -24.0, 0.0)
ops.load(8, -24.0, -60.0)
ops.load(6, -41.0, -60.0)
ops.load(10,-73.0, 0.0)
ops.load(12,-56.0, 0.0)
ops.load(14,-38.0, 0.0)
ops.load(16,-14.0, 0.0)

ops.system('BandSPD')
ops.numberer('RCM')
ops.constraints('Plain')
ops.integrator('LoadControl', 1.0)

# Çözüm algoritması
ops.algorithm('Linear')
 
# Analiz türü
ops.analysis('Static')
ops.analyze(1) # Analizin kaç kez yapılacağını belirtir.

# ---------------------------------
# Çıktı
# ---------------------------------

# Yer değiştirmeler
for i in range(1,17):
    print(i,"numaralı düğüm x=",ops.nodeDisp(i,1),"m  -  y=",ops.nodeDisp(i,2),"m")
    
# Modeli çizdir
opsplt.plot_model("nodes","elements")
