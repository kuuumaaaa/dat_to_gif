import numpy as np
import functools
import matplotlib.pyplot as plt
import cmath
import random
import os
from PIL import Image
import glob
 
 #---------------入力-----------------
loop_start =10
loop_int =10
num =50
start =0                #全行読み込む場合はここの値ではなくしたのtableのコメントアウトを外す
stop =55
inputdir = "./ref/output_line"
inputfile = "/output_line"
inputext =".dat" 
outputdir ="./output_line_data/ref"
outputfile ="/output_line"
outputext =".png"
#----------------------------------------------
    # ディレクトリの作成
# path = os.getcwd()
# new_dir_path = path + "/output_line_data"

new_dir_path = outputdir+outputfile

os.makedirs(new_dir_path, exist_ok=True)

for i in range (num):
    # plt.figure(1)
    # plt.figure(2)
    loopnum = loop_start + loop_int*i
    formated_loopnum= '{:8d}'.format(loopnum)      #loopnumの書式(fortran(i9)と同じ)
    table = np.loadtxt(inputdir+inputfile+str(formated_loopnum)+inputext)

    # # 出力ファイルの作成
    figname1 = new_dir_path+str(loopnum)+outputext
    # figname2 = new_dir_path+"/Vin/Vin_output"+str(loopnum)+".png"

    # y =table[start:stop,0]  #横軸
    # x = table[start:stop,1] #縦軸
    y =table[:,0]  #横軸(全行読み込む)
    x = table[:,2] #縦軸(全行読み込む)

    # グラフ表示
    plt.figure(1,figsize=(15,15))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 17
    plt.subplot()
    plt.plot(y, x, label='loop='+str(loopnum))
    plt.xlabel('$\it{y}$ [m]', fontsize=20)
    # plt.xlim([0.018,0.052])
    # plt.xlim([0.017,0.053])
    plt.ylabel('$\it{E_y}$ [V/m]', fontsize=20)
    # plt.ylim([-0.004,0.004])
    plt.grid()
    leg = plt.legend(loc=1, fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.savefig(figname1, bbox_inches='tight')

    # plt.figure(2,figsize=(15,15))
    # plt.subplot()
    # plt.plot(y, Vin, label='loop='+str(loopnum))
    # plt.xlabel('$\it{y} [m]', fontsize=20)
    # plt.xlim([0.018,0.052])
    # plt.ylabel('Voltage [V]', fontsize=20)
    # plt.ylim([-1800,1800])
    # plt.grid()
    # leg = plt.legend(loc=1, fontsize=25)
    # leg.get_frame().set_alpha(1)
    # plt.savefig(figname2, bbox_inches='tight')
    # # np.savetxt('sample.dat', [Time,Vin])
    # # np.savez('sample2.dat', Time,Vin)
    plt.close(1)
    # plt.close(2)
    


# files = sorted(glob.glob('./output_lineall_data/cr/*.png'))
files = sorted(glob.glob(outputdir+"/*"+outputext))
images = list(map(lambda file: Image.open(file), files))

images[0].save(outputdir+'/out.gif', save_all=True, append_images=images[1:], duration=400, loop=0)

# files = sorted(glob.glob('./output_lineall_data/Vin/*.png'))
# images = list(map(lambda file: Image.open(file), files))

# images[0].save('./output_lineall_data/Vin/out.gif', save_all=True, append_images=images[1:], duration=400, loop=0)
