fhand = open('Logs.txt')
stand = []
#contador de paises
count_bra = 0
count_chi = 0 
count_mex = 0
count_col = 0
count_cuba = 0
count_peru = 0
#contador para assinados
bra_assi = 0
chi_assi = 0
mex_assi = 0
col_assi = 0
cuba_assi = 0
peru_assi = 0




for line in fhand:
    if line == '\n':
        continue
    else :
        stand.append(line)
print(stand)       

for column in stand: 
    if column[0:2] == '55':
        count_bra = count_bra + 1
    elif column[0:2] == '56':
        count_chi = count_chi + 1
    elif column[0:2] == '52':
        count_mex = count_mex + 1
    elif column[0:2] == '53':
        count_cuba = count_cuba + 1
    elif column[0:2] == '51':
        count_peru = count_peru + 1
    elif column[0:2] == '57':
        count_col = count_col + 1

for column in stand:
    if column[0:2] == '55' and column[16] == 's':
        bra_assi = bra_assi + 1
    elif column[0:2] == '56' and column[16] == 's':
        chi_assi = chi_assi + 1
    elif column[0:2] == '52' and column[16] == 's':
        mex_assi = mex_assi + 1
    elif column[0:2] == '53' and column[16] == 's':
        cuba_assi = cuba_assi + 1
    elif column[0:2] == '51' and column[16] == 's':
        peru_assi = peru_assi + 1
    elif column[0:2] == '57' and column[16] == 's':
        col_assi = col_assi + 1



print('Peru', ',', count_peru, ',', peru_assi)
print('Chile', ',', count_chi, ',', chi_assi)
print('Brasil', ',', count_bra, ',', bra_assi)
print('México', ',', count_mex, ',', mex_assi)
print('Côlombia',',', count_col, ',', col_assi)
print('Cuba', ',', count_cuba, ',', cuba_assi)
