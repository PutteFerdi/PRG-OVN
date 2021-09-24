svar1 = input ("Hur många mil står mätaren på idag? ")
svar2 = input ("Vad var mätarställningen för ett år sedan? ")
svar3 = input ("Hur många liter har du förbrukat under året? ")

mil = float(svar1) - float(svar2)
förbrukning = float(svar3) / float(mil)

print(f"Antal körda mil: {mil}")
print(f"Antal liter bensin: {svar3}")
print(f"Förbrukning per mil: {förbrukning}")
