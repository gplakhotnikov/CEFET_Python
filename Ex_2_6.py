def disp_dois_especialistas(medico01, medico02):
   return list(set(medico01) & set(medico02))

def disp_tres_especialistas(medico01, medico02, medico03):
   return list(set(medico01) & set(medico02) & set(medico03))
