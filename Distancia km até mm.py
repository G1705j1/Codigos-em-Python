medida = float(input('Digite uma distancia em métros: '))
cm = medida*100
mm = medida*1000
dm = medida*10
dam = medida*100
km = medida*10
print('A medida entre: {} metros, corresponde a: \n -> {} metros  \n -> {:.0f} centimetros \n -> {:.0f} milimetros \n -> {:.0f} decimetro \n -> {:.0f} decametro \n -> {:.0f} kilometo   '.format(medida, medida, cm, mm, dm, dam, km))