#!/bin/bash/python3
#-*-coding: utf-8-*-
# Title: instalation and configuration for Abraxas < version 0.0.1 >
# to: ThE Ibam3 Community
# WItH LoV3 MUD0
import os
from hashlib import md5
from json import dumps
from subprocess import run,PIPE
from requests import get

def Comporobate_Abraxas():
    if [ True for x in os.listdir(os.getcwd()) if x == 'Abraxas'][0]:
        pass
    else:
        raise NameError('no se encontro Abraxas: Alerta Este programa debe de estar en la misma path que abraxas')
def encrypt_with(task,key):
    for x in task:
        x = task[x].encode('rot13')
    return task

def biuld_config_env(coon,lock=False):
    ''' lock >> argumento que requiere una clave de encriptacion '''
    chez = os.environ.get("$PREFIX",False)
    if chez:
        run(['sed','-i',f'$a export ABRAXAS={coon["work"]}',os.path.join(chez,'usr','bash.bashrc')],stdout=PIPE,stderr=PIPE)
    else: raise NameError("no se pudo localizar la vareable de entorno $PREFIX")
    with open(os.path.join(os.environ.get('ABRAXAS'),'lock.file'),'w') as file:
        task = coon
        if lock:
            encrypt_with(task,lock)
        file.write(dumps(task))

def download_recurses():
    req = get(,strem=True)
    with open(os.path.join(os.environ['ABRAXAS'],'oui.csv'),'w') as temp:
        for x in req:
            temp.write(x.iterContent())
    req.close()
    run(['git','clone',''])
    print('INSTALANDO DEPENDENCIAS ESPECIALES')
    run(['curl','-LO','https://its-pointless.github.io/setup-pointless-repo.sh])
    run(['bash setup-pointless-repo.sh'])
    run(['pkg','install','numpy'])
    run(['pip','install','-r','Abraxas/requirements.txt'])

def FIRST_HIT():
    coon = {'ath':os.getcwd(),'work':'$PREFIX/bin/Abraxas'}
    banner =
    '''
 _________________________________________________________________
                                                                 
| ++    ---------------------------------------------------    ++ |
| bienvenido al menu de instalacion de Abraxas < version: 0.0.1 > |
| ++    ---------------------------------------------------    ++ |
|  + _________________________________________________________ +  |
|                                                                 |
|                                                                 |
|   + ___________________________________________________ +       |

  | la ruta donde actual mente se trabaja es: {coon["path"]} [1]

|    + ___________________________________________________ +      |
|                                                                 |
|                                                                 |
|   + ____________________________________________________ +      |

  | la ruta donde se creara el directorio base es: {coon["work"]} [2]

|   + ____________________________________________________ +      |
  
'''
    data = int(input("desea realizar algun cambio ? : "))
    if data == 1:
        coon['path'] = input('[?]:')
    elif data == 2:
        coon['work'] = input('[?]:')
    else:
        pass
    disp1 = os.path.exists(coon['path'])
    disp2 = os.path.exists(coon['work'])
    if disp1 and disp2 == True:
        if os.path.isdir(coon['path']) and os.path.isdir(coon['work']):
            pass
        else:
            raise NameError('se nececita un directorio no un archivo')
    else:
        raise NameError('los directorios no son utilizables')
    lock,lock2 = coon['path'],coon['work']
    lock = md5(lock.encode('utf-8')).hexdigest()
    lock2 = md5(lock2.encode('utf-8')).hexdigest()
    coon['sect'] = f'{lock};{lock2}'
    biuld_config_env(coon)
    downloa_recurses()
    
if __name__ == '__main__':
    FIRST_HIT()
