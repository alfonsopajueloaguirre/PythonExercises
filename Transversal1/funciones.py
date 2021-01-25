
def imprimir_trabajadores(lista_trabajadores):
    for x in lista_trabajadores:
        print(x)

def trabajador(lista_trabajadores):
    igm = list()
    igg = list()
    igg_igm = list()
    ni_igg_ni_igm = list()
    mujeres_contagiadas = list()
    hombres_contagiados = list()
    mujeres = list()
    hombres = list()

    for i in lista_trabajadores:
        if i.sexo_trabajador == 'M':
            mujeres.append(i)
            if i.IgG_trabajador == 'Sí' or i.IgM_trabajador == 'Sí':
                mujeres_contagiadas.append(i)
        else:
            hombres.append(i)
            if i.IgG_trabajador == 'Sí' or i.IgM_trabajador == 'Sí':
                hombres_contagiados.append(i)

        if i.IgG_trabajador == 'Sí' and i.IgM_trabajador == 'Sí':
            igg_igm.append(i)
        elif i.IgG_trabajador == 'Sí':
            igg.append(i)
        elif i.IgM_trabajador == 'Sí':
            igm.append(i)
        else:
            ni_igg_ni_igm.append(i)

    numero_hombres = round(len(hombres_contagiados) / len(hombres)*100,1)
    numero_mujeres = round(len(mujeres_contagiadas) / len(mujeres)*100,1)

    datos = {
        'IgM' : igm,
        'IgG' : igg,
        'IgG_IgM' : igg_igm,
        'Ni_IgG_Ni_IgG' : ni_igg_ni_igm,
        'mujeres' : numero_mujeres,
        'hombres' : numero_hombres,
    }
    return datos