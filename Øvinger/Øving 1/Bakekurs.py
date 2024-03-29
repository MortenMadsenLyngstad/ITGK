def oppskrift_a():
  # spør hvor mange cookies om skal lages
  antall = int(input("Hvor mange cookies vil du lage?\n"))

  # ingredienser for å lage 1 stk cookie
  sukker_1 = 400/48
  smør_1 = 320/48
  sjokolade_1 = 500/48
  egg_1 = 2/48
  hvetemel_1 = 460/48

  # lager en liste med alle ingrediensene
  ingredienser = [sukker_1, smør_1, sjokolade_1, egg_1, hvetemel_1]

  # hvis antallet cookies er over 1
  if antall > 1:
    # ganger alle ingrediensene med antalllet personen vil lage
    sukker = round(ingredienser[0] * antall, 0)
    smør = round(ingredienser[1] * antall, 0)
    sjokolade = round(ingredienser[2] * antall, 0)
    egg = round(ingredienser[3]* antall, 0)
    hvetemel = round(ingredienser[-1] * antall, 0)

    # printer svaret ved hjelp av f'strings
    print(f'Antall cookies: {antall}\nSukker (g): {sukker}\nSmør (g): {smør}')
    print(f'Sjokolade (g): {sjokolade}\nEgg: {egg}\nHvetemel (g): {hvetemel}')

  # hvis antallet er eksakt 1
  elif antall == 1:
    # avrunder alle ingrediensene for å få finere tall
    sukker_1 = round(400/48, 0)
    smør_1 = round(320/48, 0)
    sjokolade_1 = round(500/48, 0)
    egg_1 = round(2/48, 2)
    hvetemel_1 = round(460/48, 0)

    print(f'Antall cookies: {antall}\nSukker (g): {sukker_1}\nSmør (g): {smør_1}')
    print(f'Sjokolade (g): {sjokolade_1}\nEgg: {egg_1}\nHvetemel (g): {hvetemel_1}')
  
  # hvis ikke antall > 1 eller == 1, så er det enten en string eller et negativt tall
  else:
    # returnerer en feilmelding
    print("FEIL: Skriv inn et positivt tall (integer)")
    return  

# oppskrift_a()


def oppskrift_b():
  # lager variabler for de ulike inputtene
  antall_1 = int(input("Hvor mange cookies vil du lage?\n"))
  antall_2 = int(input("og hvor mange cookies vil du lage nå?\n"))
  antall_3 = int(input("og hvor mange cookies vil du lage til slutt?\n"))

  # variabler for ingredienser
  sukker_0 = 400/48
  sjokolade_0 = 500/48
  
  # if setninger som regner ut antallet og sjekker om det er et positivt tall
  if antall_1 >= 1:
    sukker_1 = round(sukker_0 * antall_1, 0)
    sjokolade_1 = round(sjokolade_0 * antall_1, 0)
  else:
    print("Skriv inn et positivt tall!")
    return


  if antall_2 >= 1:
    sukker_2 = round(sukker_0 * antall_2, 0)
    sjokolade_2 = round(sjokolade_0 * antall_2, 0)
  else:
    print("Skriv inn et positivt tall!")
    return


  if antall_3 >= 1:
    sukker_3 = round(sukker_0 * antall_3, 0)
    sjokolade_3 = round(sjokolade_0 * antall_3, 0)
  else:
    print("Skriv inn et positivt tall!")
    return

  # printer ut svaret
  print("Antall cookies:", "sukker (g)".rjust(15), "sjokolade (g)".rjust(18))

  print(antall_1," ".rjust(21), sukker_1, " ".rjust(13), sjokolade_1)

  print(antall_2," ".rjust(21), sukker_2, " ".rjust(13), sjokolade_2)

  print(antall_3," ".rjust(21), sukker_3, " ".rjust(13), sjokolade_3)


# oppskrift_b()
