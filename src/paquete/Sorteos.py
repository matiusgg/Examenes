
#* RANDOM
import random
#* OS
import os
#* DATETIME
import datetime


class Sorteos():

    """
    CLASE NOMBRECLASE, NOS PERMITIRÁ APLICAR LOS METODOS A LO QUE NECESITEMOS MEDIANTE EL OBJETO
    """

    def __init__(self, collection, email, email_id):

        """
        CONTRUCTOR DE LA CLASE NOMBRECLASE
        """

        self.inicio = 0

        #* Collection mongoDB
        self.collection = collection

        #* Usuario, solo si la vamos a usar un login en la aplicación
        self.email = email

        #* email_id, lo usarmeos para las querys de mongoDB
        self.email_id = email_id



    def listaSorteos(self, actualizarFechaSorteo):

        #* Fecha actual
        x = datetime.datetime.now()
        print(x)

        #* Datos de la fecha actual
        anyoActual = x.strftime("%Y")
        mesActual = x.strftime("%m")
        diaActual = x.strftime("%d")
        horaActual = x.strftime("%X")

        if actualizarFechaSorteo == '1':

            #* Diccionario que reune todos los eventos por mes, para agregarlo a mongoDB
            infoSorteos = {
                'sorteo1':{
                    'plazo': [f'{anyoActual}-{mesActual}-1', f'{anyoActual}-{mesActual}-7'],
                    'premio': 'coche'
                },
                'sorteo2':{
                    'plazo': [f'{anyoActual}-{mesActual}-8', f'{anyoActual}-{mesActual}-15'],
                    'premio': 'moto'
                },
                'sorteo3':{
                    'plazo': [f'{anyoActual}-{mesActual}-16', f'{anyoActual}-{mesActual}-23'],
                    'premio': 'barco'
                },
                #* Lo deje hasta el día 28, porque así no afectará el mes febrero a los sorteos por el tema de que los dias de febrero que son menos.
                'sorteo4':{
                    'plazo': [f'{anyoActual}-{mesActual}-24', f'{anyoActual}-{mesActual}-28'],
                    'premio': 'mansión'
                }
            }

            # #* diccionario que nos servirá para hacer la busqueda de mongoDB en la variable "buscarSorteos"
            buscarDicc = {
                'sorteos.sorteo1.plazo': [f'{anyoActual}-{mesActual}-1', f'{anyoActual}-{mesActual}-7']
            }

            # #* Esta variable con la query de FINd de mongoDB, nos ayudará a que no se repitan registros de los mismos eventos que ya han sido agregados
            buscarSorteos = self.collection.find(buscarDicc)

            if list(buscarSorteos) != []:

                #* variable con query de mongoDB para obtener los sorteos
                verSorteos = self.collection.find(buscarDicc)

                #* lista que contendrá los sorteos
                listaConSorteos = []

                for i in list(verSorteos):

                    listaConSorteos.append(i)

                #* dias de los plazos de  los sorteos
                diaInicial1 = int(listaConSorteos[0]['sorteos']['sorteo1']['plazo'][0].split('-')[2])
                diaFinal1 = int(listaConSorteos[0]['sorteos']['sorteo1']['plazo'][1].split('-')[2])

                diaInicial2 = int(listaConSorteos[0]['sorteos']['sorteo2']['plazo'][0].split('-')[2])
                diaFinal2 = int(listaConSorteos[0]['sorteos']['sorteo2']['plazo'][1].split('-')[2])

                diaInicial3 = int(listaConSorteos[0]['sorteos']['sorteo3']['plazo'][0].split('-')[2])
                diaFinal3 = int(listaConSorteos[0]['sorteos']['sorteo3']['plazo'][1].split('-')[2])

                diaInicial4 = int(listaConSorteos[0]['sorteos']['sorteo4']['plazo'][0].split('-')[2])
                diaFinal4 = int(listaConSorteos[0]['sorteos']['sorteo4']['plazo'][1].split('-')[2])

                sorteo1 = [False, '']
                sorteo2 = [False, '']
                sorteo3 = [False, '']
                sorteo4 = [False, '']
                condicionarParticipar = False

                if (int(diaActual) < diaFinal1 and int(diaActual) > diaInicial1):

                    sorteo1[0] = True

                    sorteo1[1] = f'Ya existen/fueron agregados sorteos de este mes {mesActual}, puedes participar en este sorteo1'

                    condicionarParticipar = True
                else:

                    sorteo1[0] = False

                    sorteo1[1] = f'El dia de hoy es: {diaActual} por lo que ya no está disponible el sorteo1'


                    condicionarParticipar = False

                #????????????????????????????????????????????????????????????????????????

                if (int(diaActual) < diaFinal2 and int(diaActual) > diaInicial2):

                    sorteo2[0] = True 

                    sorteo2[1] = f'Ya existen/fueron agregados sorteos de este mes {mesActual}, puedes participar en este sorteo2'

                    condicionarParticipar = True


                else:

                    sorteo2[0] = False

                    sorteo2[1] = f'El dia de hoy es: {diaActual} por lo que ya no está disponible el sorteo2'

                    condicionarParticipar = False


                #????????????????????????????????????????????????????????????????????????

                if (int(diaActual) < diaFinal3 and int(diaActual) > diaInicial3):

                    sorteo3[0] = True

                    sorteo3[1] = f'Ya existen/fueron agregados sorteos de este mes {mesActual}, puedes participar en este sorteo3'

                    condicionarParticipar = True

                else:

                    sorteo3[0] = False

                    sorteo3[1] = f'El dia de hoy es: {diaActual} por lo que ya no está disponible el sorteo3'

                    condicionarParticipar = False

                #????????????????????????????????????????????????????????????????????????

                if (int(diaActual) < diaFinal4 and int(diaActual) > diaInicial4):

                    sorteo4[0] = True

                    sorteo4[1] = f'Ya existen/fueron agregados sorteos de este mes {mesActual}, puedes participar en este sorteo4'

                    condicionarParticipar = True

                else:

                    sorteo4[0] = False

                    sorteo4[1] = f'El dia de hoy: {diaActual} por lo que ya no está disponible el sorteo4'

                    condicionarParticipar = False

                return {'sorteo1': sorteo1, 'sorteo2': sorteo2, 'sorteo3': sorteo3, 'sorteo4': sorteo4}, listaConSorteos, condicionarParticipar

            else:

                #* agregamos los sorteos del mes
                agregarSorteos = self.collection.insert_one({'sorteos': infoSorteos})

                #* lista para agregar el id_sorteo
                lista_Sorteo_id = []

                buscarSorteos2 = self.collection.find(buscarDicc)

                for i in list(buscarSorteos2):

                    lista_Sorteo_id.append(str(i['_id']))

                
                agregarSorteo_id = self.collection.update_one(buscarDicc, {'$set': {'sorteo_id': lista_Sorteo_id[0]}})

                #* Este return solo funcionará cuando estemos en un nuevo mes, y el metodo agregue los sorteos actualizados del mes actual
                #* en el que estemos, ya que si ya fue agregado, hará el return anterior, es decir este: return f'Ya existen sorteos de este mes {mesActual}'
                return {'msg': f'Se han agregado los sorteos del mes: {mesActual}'}, [], None

    def sorteo(self, participar, semana):

        agregarParticipante = self.collection.update_one({'email_id': self.email_id}, {'$set': {'sorteo_id': participar}})

        agregarSemana = self.collection.update_one({'email_id': self.email_id}, {'$set': {'sorteoSemana': semana}})

        listaInfoUsuario = []

        infoUsuario = self.collection.find({'email_id': self.email_id})

        for i in list(infoUsuario):

            listaInfoUsuario.append(i)

        # if listaInfoUsuario != []:

            #* SORTEO DE LA SEMANA

            #******************************+

        listaTodosUsuarios = []

        all_users = self.collection.find({})

        for i in list(all_users):

            listaTodosUsuarios.append(i)

        print(listaTodosUsuarios)

        return 'GRACIAS POR PARTICIPAR, ESPERA EL RESULTADO A FINAL DE LA SEMANA', listaTodosUsuarios

            # for sort in listaTodosUsuarios:

            #     if 




            #*******************************


        # return 'GRACIAS POR PARTICIPAR, ESPERA EL RESULTADO A FINAL DE LA SEMANA', listaTodosUsuarios

