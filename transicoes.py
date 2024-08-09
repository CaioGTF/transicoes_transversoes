from Bio import AlignIO
'''
Transição
Uma transição ocorre quando uma purina é substituída por uma purina , ou uma pirimidina por uma pirimidina.

Transversão
Uma mudança de uma purina para uma pirimidina , ou vice-versa, é uma transversão.

Purinas
Os nucleotídeos adenina (A) e guanina (G) são conhecidos como purinas.

Pirimidinas
Os nucleotídeos citosina (C) e timina (T) são conhecidos como pirimidinas.

'''
# Carregar o alinhamento do arquivo
align = AlignIO.read("atp6_felinae_at.aln", "clustal")

# Inicializar contadores
AG_count = 0
GA_count = 0
CT_count = 0
TC_count = 0
AT_count = 0
TA_count = 0
AC_count = 0
CA_count = 0
GC_count = 0
CG_count = 0
AA_count = 0

# Iterar sobre cada coluna no alinhamento
for i in range(align.get_alignment_length()):
    coluna = str(align[:,i])
    caracteres_unicos = set(coluna)
    
    # Contar ocorrências de 'A' e 'G' e ignorar outras bases
    A = coluna.count('A')
    G = coluna.count('G')
    C = coluna.count('C')
    # Considerar colunas que contém apenas 'A' e 'G'
    #if  {'A', 'G', 'C'} == caracteres_unicos:
    if 'A' in caracteres_unicos and 'G' in caracteres_unicos:
        if G == C:
            pass
        elif A > G:
            AG_count += 1
        elif G > A:
            GA_count += 1

    if  'C' in caracteres_unicos and 'T' in caracteres_unicos:
        C = coluna.count('C')
        T = coluna.count('T')
        G = coluna.count('G')
        # Imprimir informações da coluna
        # Incrementar os contadores respectivos com base nas ocorrências de 'A' e 'G'
        if C == G:
            pass
        elif T == G:
            pass
        elif T == A:
            pass
        elif C == A:
            pass
        elif T > C:
            TC_count += 1
        elif C > T:
            CT_count += 1
    if 'A' in caracteres_unicos and 'T' in caracteres_unicos:
        A = coluna.count('A')
        G = coluna.count('G')
        C = coluna.count('C')
        T = coluna.count('T')    
        #print(coluna) 
        # Incrementar os contadores respectivos com base nas ocorrências de 'A' e 'G'
        if C > T:
            pass
        elif G > T:
            pass
        elif C > A:
            pass
        elif A > T:
            AT_count += 1
            print(f'{i} {AT_count}')
        elif T > A:
            TA_count += 1
            
    if  'G' in caracteres_unicos and 'C' in caracteres_unicos:
        A = coluna.count('A')
        G = coluna.count('G')
        C = coluna.count('C')
        T = coluna.count('T')
        
        # Incrementar os contadores respectivos com base nas ocorrências de 'A' e 'G'
        if G == T:
            pass
        elif T > C:
            pass
        elif A > C:
            pass
        elif C > G:
            CG_count += 1
        elif G > C:
            GC_count += 1
    if 'A' in caracteres_unicos and 'C' in caracteres_unicos:
        if T > A:
            pass
        elif G > C:
            pass
        elif A > C:
            AC_count += 1
        elif C > A:
            CA_count += 1
    if 'A'in caracteres_unicos and 'G' in caracteres_unicos:
        A = coluna.count('A')
        G = coluna.count('G')
        C = coluna.count('C')
        T = coluna.count('T')
        if 'T' in caracteres_unicos and T < A and T < G:
            AA_count += 1
            print(coluna)
            
            
        

print(f'CT_count: {CT_count}')
print(f'TC_count: {TC_count}')
print(f'AG_count: {AG_count}')
print(f'GA_count: {GA_count}')
trans = AG_count + GA_count + CT_count + TC_count
print(f'transições:', trans)
print(f'AT_count: {AT_count}')
print(f'TA_count: {TA_count}')
print(f'GC_count: {GC_count}')
print(f'CG_count: {CG_count}')
print(f'AC_count: {AC_count}')
print(f'CA_count: {CA_count}')
print(f'AA_count: {AA_count}')
transv = AT_count + TA_count + GC_count + CG_count + AC_count + CA_count + AA_count
print(f'transversões:', transv)