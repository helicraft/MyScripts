#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AM Tester
# Purpose: test am.exe
#
# Author:      Wangbo
#
#-------------------------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt
import time



def main():
    cwd = os.getcwd()
    wd1 = os.path.join(cwd,'TestResults')
    wd2 = os.path.join(cwd,'ExperimentResults')
    #files = os.listdir(wd)
    draw02(wd1,wd2)
    draw03(wd1,wd2)
    draw04(wd1,wd2)
    draw05b(wd1,wd2)
    draw05a(wd1,wd2)
    draw06a(wd1,wd2)
    draw07(wd1,wd2)
    #draw08(wd1,wd2)
    draw09(wd1,wd2)
    draw10(wd1,wd2)

def draw01(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'1OK_AM_Input_Fig7-16_porous+plate-TL.txt'))
    pdata = np.loadtxt(os.path.join(wd2,'1OK_AM_Input_Fig7-16_porous+plate-TL.txt'))
    
def draw02(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.19.txt'))
    pdata = np.loadtxt(os.path.join(wd1,'2OK_AM_Input_Fig7-17_porous+plate-TL.txt.results3.txt'))
    fig = plt.figure(figsize=(8,7))
    plt.plot(edata[:,0],edata[:,1],'ko',label = "Measurements")
    plt.plot(pdata[:,0]/1000,pdata[:,2],'r-',label = "Prediction")
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Transmission Loss ($dB$)",fontsize=16)
    plt.xlim(-0.5,10.5)
    plt.yticks(range(0,55,5))
    plt.xticks(range(0,11,1))
    plt.ylim(0,50)
    #plt.title("porous+plate-TL",fontsize=20)
    plt.legend(loc=1)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.19.txt.png'))
    plt.close()
    
def draw03(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.9.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'10ok_AM_Input_Tab7-3_2porous-abs.txt.results3.txt'))
    pdata2 = np.loadtxt(os.path.join(wd1,'12ok_AM_Input_Fig7.8_Tab7-3_noFacing.txt.results3.txt'))
    fig = plt.figure(figsize=(8,6))
    plt.plot(edata[:,0],edata[:,1],'r.',label = "Measurements no facing")
    plt.plot(pdata2[:,0]/1000,pdata2[:,1],'r-',label = "Prediction no facing")
    plt.plot(edata[:,2],edata[:,3],'b.',label = "Measurements with facing")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction with facing")
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("$A_0$",fontsize=16)
    plt.xlim(0,3.5)
    plt.xticks(range(0,4,1))
    plt.yticks([0,.2,.4,.6,.8])
    #plt.title("Tab7-3_2porous-abs\nFig7.8_Tab7-3_noFacing",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.9.txt.png'))
    plt.close()

def draw04(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.7.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'11ok_AM_Input_Tab7-3_noFacing.txt.results2.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,4],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
    plt.xlim(0.,3)
    plt.ylim(-10,3.5)
    plt.xticks([0,1,2,3])
    plt.yticks(range(-10,4,1))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.7.txt.png'))
    plt.close()

def draw05b(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.12.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'9O_AM_Input_Tab7-4_4porous-Z.txt.results3.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements, with screen")
    #plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction, with screen")
    #plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,4],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Absorption Coefficient",fontsize=16)
    plt.xlim(0.4,2.1)
    plt.ylim(0,1)
    plt.xticks([0.5,1,1.5,2])
    plt.yticks([0,0.2,0.4,0.6,0.8,1])
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.12.txt.png'))
    plt.close()


def draw05a(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.11.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'9O_AM_Input_Tab7-4_4porous-Z.txt.results2.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,4],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
    plt.xlim(0.4,2.1)
    plt.ylim(-8,8)
    plt.xticks([0.5,1,1.5,2])
    plt.yticks(range(-8,9,1))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=3)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.11.txt.png'))
    plt.close()

def draw06a(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.17.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'15_AM_Input_Fig11-17vsTab11-7_3porous-Z.txt.results2.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0],pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0],pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,1400],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($Hz$)",fontsize=16)
    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
    plt.xlim(200,1400)
    plt.ylim(-35,35)
    plt.xticks(range(200,1600,200))
    plt.yticks(range(-30,40,10))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=3)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.17.txt.png'))
    plt.close()
    
def draw07(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.18.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'1OK_AM_Input_Fig7-16_porous+plate-TL.txt.results3.txt'))
    plt.plot(edata[:,0],edata[:,1],'b--',label = "(a)")
    plt.plot(edata[:,2],edata[:,3],'r--',label = "(b)")
    plt.plot(edata[:,4],edata[:,5],'g--',label = "(c)")
    #plt.plot(pdata1[:,0],pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'b-',label = "Prediction")
    plt.plot([0,1400],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($Hz$)",fontsize=16)
    plt.ylabel("Transmission Loss ($dB$)",fontsize=16)
    plt.xlim(.1,4)
    plt.ylim(0,65)
    plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4])
    plt.yticks(range(0,70,10))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.18.txt.png'))
    plt.close()

#def draw08(wd1,wd2):
#    edata = np.loadtxt(os.path.join(wd2,'11.7.txt'))
#    pdata1 = np.loadtxt(os.path.join(wd1,'15_AM_Input_Fig11-17vsTab11-7_3porous-Z.txt.results2.txt'))
#    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
#    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
#    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction Real")
#    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
#    plt.plot([0,4],[0,0],'k-',lw=1)
#    plt.xlabel("Frequency ($kHz$)",fontsize=16)
#    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
#    plt.xlim(0.,3)
#    plt.ylim(-10,3.5)
#    plt.xticks([0,1,2,3])
#    plt.yticks(range(-10,4,1))
#    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
#    plt.legend(loc=4)
#    plt.tight_layout()
#    #plt.grid()
#    #plt.show()
#    plt.savefig(os.path.join(wd2,'11.7-15.txt.png'))
#    plt.close()

def draw09(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.15.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'17_AM_Input_Fig11-15vsTab11-6_1porous-Z-30deg.txt.results2.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,4],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
    plt.xlim(0.79,2.5)
    plt.ylim(-10,6)
    plt.xticks([.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4])
    plt.yticks(range(-10,8,2))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.15.txt.png'))
    plt.close()

def draw10(wd1,wd2):
    edata = np.loadtxt(os.path.join(wd2,'11.8.txt'))
    pdata1 = np.loadtxt(os.path.join(wd1,'16_AM_Input_Fig11-8vsTab11-3_2porous-Z.txt.results2.txt'))
    plt.plot(edata[:,0],edata[:,1],'b.',label = "Measurements Real")
    plt.plot(edata[:,2],edata[:,3],'r.',label = "Measurements Image")
    plt.plot(pdata1[:,0]/1000,pdata1[:,1],'b-',label = "Prediction Real")
    plt.plot(pdata1[:,0]/1000,pdata1[:,2],'r-',label = "Prediction Image")
    plt.plot([0,4],[0,0],'k-',lw=1)
    plt.xlabel("Frequency ($kHz$)",fontsize=16)
    plt.ylabel("Z ($\\rho_{0} c_{0}$ unit)",fontsize=16)
    plt.xlim(0.37,3)
    plt.ylim(-3,3.5)
    plt.xticks(range(1,4,1))
    plt.yticks(range(-3,4,1))
    #plt.title("Tab7-3_noFacing.txt.results2",fontsize=20)
    plt.legend(loc=4)
    plt.tight_layout()
    #plt.grid()
    #plt.show()
    plt.savefig(os.path.join(wd2,'11.8.txt.png'))
    plt.close()


def savefigure(wd,fn):
    data = np.loadtxt(os.path.join(wd,fn))
    n1 = fn.lower().index('.txt')
    n2 = fn.lower().index('input_')
    case_name = fn[:n1]
    fig = plt.figure(figsize=(8,5))           #调整图片大小
    fz1 = 20
    cn = case_name[n2+6:n1]
    if len(cn)>40:
        fz1 = 18
    fz2 = 16
    
    ax1 = fig.add_subplot(211)
    plt.setp( ax1.get_xticklabels(), visible=False)
    plt.plot(data[:,0], data[:,1], 'b-',label='Col 2')
    plt.xscale('log')
    #fig.suptitle(case_name,fontsize=24)
    plt.title(cn+'\n ',fontsize=fz1)
    plt.grid()
    plt.legend(loc=4)
    ax2 = fig.add_subplot(212, sharex=ax1)
    plt.ylabel('$dB$',fontsize=fz2)
    plt.xlabel('$Hz$',fontsize=fz2)
    plt.xlim(90,12000)
    plt.plot(data[:,0], data[:,2], 'r-',label='Col 3')
    plt.grid()
    plt.legend(loc=2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(wd,fn+'.png'))
    plt.close()

def savecomparefigure(wd,wd2,fn):
    data = np.loadtxt(os.path.join(wd,fn))
    data2 = np.loadtxt(os.path.join(wd2,fn))
    n1 = fn.lower().index('.txt')
    n2 = fn.lower().index('input_')
    case_name = fn[:n1]
    fig = plt.figure(figsize=(8,5))                #调整图片大小
    fz1 = 20
    cn = case_name[n2+6:n1]
    if len(cn)>40:
        fz1 = 18
    fz2 = 16
    
    ax1 = fig.add_subplot(211)
    plt.setp( ax1.get_xticklabels(), visible=False)
    plt.plot(data[:,0], data[:,1], 'b-',label='Col 2')
    plt.plot(data2[:,0], data2[:,1], 'k.',label=' Standard Col 2')
    plt.xscale('log')
    #fig.suptitle(case_name,fontsize=24)
    plt.title(cn+'\n ',fontsize=fz1)
    plt.grid()
    plt.legend(loc=4)
    ax2 = fig.add_subplot(212, sharex=ax1)
    plt.ylabel('$dB$',fontsize=fz2)
    plt.xlabel('$Hz$',fontsize=fz2)
    plt.xlim(90,12000)
    plt.plot(data[:,0], data[:,2], 'r-',label='Col 3')
    plt.plot(data2[:,0], data2[:,2], 'k.',label=' Standard Col 3')
    plt.grid()
    plt.legend(loc=2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(wd2,fn+'.png'))
    plt.close()


if __name__ == "__main__":
    main()
