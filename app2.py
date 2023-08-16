#definindo os valores de conversão
conversionWeight = 2.205
conversionHeight = 3.281

#conversão kg-lbs
weight_kg = input(' What is your weight? ')
weight_lbs = int(weight_kg) * conversionWeight

#conversão m-fts
height_m = input((' What is your height? '))
height_fts = float(height_m) * conversionHeight

#mandando a mensagem no formato certo, limitando 2 casas apos a virgula (2f)
print(' Your weight in pounds is: {:.2f}'.format(weight_lbs))
print(' Your height in feet is : {:.2f}'.format(height_fts))
