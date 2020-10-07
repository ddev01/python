bedrag = 2.87
DOLLAR = 1
KWARTJES = 0.25
DUBBELTJES = 0.1
STUIVERS = 0.05
CENTEN = 0.01

dollarvar = int(bedrag / DOLLAR)
print("Aantal dollars:", dollarvar)
bedrag = bedrag - dollarvar
kwartjesvar = int (bedrag / KWARTJES)
print("Aantal kwartjes:", kwartjesvar)
bedrag = bedrag - (kwartjesvar*KWARTJES)
dubbeltjesvar = int (bedrag / DUBBELTJES)
print("aatnal dubbeltjes:", dubbeltjesvar)
bedrag = bedrag - (dubbeltjesvar*DUBBELTJES)
stuiversvar = int (bedrag / STUIVERS)
print("Aantal stuivers:", stuiversvar)
bedrag = bedrag - (stuiversvar*STUIVERS)
centenvar = int(bedrag / CENTEN)
print("Aantal centen:", centenvar)