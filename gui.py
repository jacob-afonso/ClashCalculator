from tkinter import *

# ---Max Level Constants
CANNON = 20
AT = 19
MORTAR = 13
AD = 11
WT = 13
AS = 7
TES = 13
BT = 9
XBOW = 8
IT = 8
EA = 5
GIGA = 5
SCATTER = 3
HUT = 4
BOMB = 10
SPR = 5
RAB = 8
GB = 7
SAM = 4
SKELT = 4
NADO = 3
CAMP = 11
BAR = 14
DBAR = 9
LAB = 12
SPELL = 6
DSPELL = 5
WORK = 5
PET = 4
STORAGE = 15
DESTORAGE = 9
DEDRILL = 8
COLLECTOR = 14
CC = 10



root = Tk() # screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
main = Frame(root) # main frame to work in 
main.pack()


def show():
    Label(main, text=can1.get()).grid(row=8, column=0)
    Label(main, text=can2.get()).grid(row=9, column=0)
    Label(main, text=can3.get()).grid(row=10, column=0)
    Label(main, text=can4.get()).grid(row=11, column=0)
    Label(main, text=can5.get()).grid(row=12, column=0)
    Label(main, text=can6.get()).grid(row=13, column=0)
    Label(main, text=can7.get()).grid(row=14, column=0)

def clear():
    global main, root
    main.destroy()
    main = Frame(root)
    main.pack()

def compile_res():
    clear()
    Label(main, text="you can now close this window and move to step 2").pack()
    file = open("currentlvl.txt", "a+")
    # ---Heros and pets---
    file.write(bk1.get() + ",x1,bk\n")
    file.write(aq1.get() + ",x1,aq\n")
    file.write(gw1.get() + ",x1,gw\n")
    file.write(rc1.get() + ",x1,rc\n")
    file.write(las1.get() + ",x1,Lassi\n")
    file.write(owl1.get() + ",x1,Owl\n")
    file.write(yak1.get() + ",x1,Yak\n")
    file.write(uni1.get() + ",x1,Unicorn\n")

    # ---Lab---
    file.write(barb1.get() + ",x1,barb\n")
    file.write(arch1.get() + ",x1,arch\n")
    file.write(gi1.get() + ",x1,gi\n")
    file.write(gob1.get() + ",x1,gob\n")
    file.write(wb1.get() + ",x1,wb\n")
    file.write(loon1.get() + ",x1,loon\n")
    file.write(wiz1.get() + ",x1,wiz\n")
    file.write(helr1.get() + ",x1,healer\n")
    file.write(drag1.get() + ",x1,drag\n")
    file.write(pek1.get() + ",x1,pekka\n")
    file.write(bd1.get() + ",x1,bd\n")
    file.write(mine1.get() + ",x1,miner\n")
    file.write(ed1.get() + ",x1,ed\n")
    file.write(yeti1.get() + ",x1,yeti\n")
    file.write(min1.get() + ",x1,min\n")
    file.write(hog1.get() + ",x1,hog\n")
    file.write(valk1.get() + ",x1,valk\n")
    file.write(gol1.get() + ",x1,golem\n")
    file.write(witc1.get() + ",x1,witch\n")
    file.write(lava1.get() + ",x1,lava\n")
    file.write(bowl1.get() + ",x1,bowler\n")
    file.write(ig1.get() + ",x1,ig\n")
    file.write(hh1.get() + ",x1,hh\n")
    file.write(zap1.get() + ",x1,lightning\n")
    file.write(heal1.get() + ",x1,heal\n")
    file.write(rage1.get() + ",x1,rage\n")
    file.write(jump1.get() + ",x1,jump\n")
    file.write(frz1.get() + ",x1,freeze\n")
    file.write(cln1.get() + ",x1,clone\n")
    file.write(invs1.get() + ",x1,invis\n")
    file.write(poi1.get() + ",x1,poi\n")
    file.write(eq1.get() + ",x1,eq\n")
    file.write(hste1.get() + ",x1,haste\n")
    file.write(sksp1.get() + ",x1,skelly spell\n")
    file.write(bat1.get() + ",x1,bat\n")
    file.write(ww1.get() + ",x1,ww\n")
    file.write(blmp1.get() + ",x1,blimp\n")
    file.write(ss1.get() + ",x1,slammer\n")
    file.write(sb1.get() + ",x1,sb\n")
    file.write(log1.get() + ",x1,log\n")

    # ---Defenses---
    countarr=[]
    countarr = [0 for i in range(CANNON+1)]
    countarr[int(can1.get())] += 1
    countarr[int(can2.get())] += 1
    countarr[int(can3.get())] += 1
    countarr[int(can4.get())] += 1
    countarr[int(can5.get())] += 1
    countarr[int(can6.get())] += 1
    countarr[int(can7.get())] += 1
    for i in range (CANNON+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",cannon\n")

    countarr = [0 for i in range(AT+1)]
    countarr[int(at1.get())] += 1
    countarr[int(at2.get())] += 1
    countarr[int(at3.get())] += 1
    countarr[int(at4.get())] += 1
    countarr[int(at5.get())] += 1
    countarr[int(at6.get())] += 1
    countarr[int(at7.get())] += 1
    countarr[int(at8.get())] += 1
    for i in range (AT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",at\n")

    countarr = [0 for i in range(MORTAR+1)]
    countarr[int(mor1.get())] += 1
    countarr[int(mor2.get())] += 1
    countarr[int(mor3.get())] += 1
    countarr[int(mor4.get())] += 1
    for i in range (MORTAR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",mortar\n")

    countarr = [0 for i in range(AD+1)]
    countarr[int(ad1.get())] += 1
    countarr[int(ad2.get())] += 1
    countarr[int(ad3.get())] += 1
    countarr[int(ad4.get())] += 1
    for i in range (AD+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",ad\n")

    countarr = [0 for i in range(WT+1)]
    countarr[int(wt1.get())] += 1
    countarr[int(wt2.get())] += 1
    countarr[int(wt3.get())] += 1
    countarr[int(wt4.get())] += 1
    countarr[int(wt5.get())] += 1
    for i in range (WT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",wt\n")
    
    countarr = [0 for i in range(AS+1)]
    countarr[int(as1.get())] += 1
    countarr[int(as2.get())] += 1
    for i in range (AS+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",as\n")

    countarr = [0 for i in range(TES+1)]
    countarr[int(tes1.get())] += 1
    countarr[int(tes2.get())] += 1
    countarr[int(tes3.get())] += 1
    countarr[int(tes4.get())] += 1
    countarr[int(tes5.get())] += 1
    for i in range (WT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",tesla\n")

    countarr = [0 for i in range(XBOW+1)]
    countarr[int(bow1.get())] += 1
    countarr[int(bow2.get())] += 1
    countarr[int(bow3.get())] += 1
    countarr[int(bow4.get())] += 1
    for i in range (XBOW+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",bow\n")
    
    countarr = [0 for i in range(IT+1)]
    countarr[int(it1.get())] += 1
    countarr[int(it2.get())] += 1
    countarr[int(it3.get())] += 1
    for i in range (IT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",it\n")
    
    countarr = [0 for i in range(EA+1)]
    countarr[int(ea1.get())] += 1
    for i in range (EA+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",ea\n")

    countarr = [0 for i in range(GIGA+1)]
    countarr[int(git1.get())] += 1
    for i in range (GIGA+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",th14\n")

    countarr = [0 for i in range(SCATTER+1)]
    countarr[int(sca1.get())] += 1 
    countarr[int(sca2.get())] += 1
    for i in range (SCATTER+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",scatter\n")

    countarr = [0 for i in range(HUT+1)]
    countarr[int(hut1.get())] += 1
    countarr[int(hut2.get())] += 1
    countarr[int(hut3.get())] += 1
    countarr[int(hut4.get())] += 1
    for i in range (HUT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",hut\n")

    countarr = [0 for i in range(BOMB+1)]
    countarr[int(bomb1.get())] += 1
    countarr[int(bomb2.get())] += 1
    countarr[int(bomb3.get())] += 1
    countarr[int(bomb4.get())] += 1
    countarr[int(bomb5.get())] += 1
    countarr[int(bomb6.get())] += 1
    countarr[int(bomb7.get())] += 1
    countarr[int(bomb8.get())] += 1
    for i in range (BOMB+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",bomb\n")

    countarr = [0 for i in range(SPR+1)]
    countarr[int(spr1.get())] += 1
    countarr[int(spr2.get())] += 1
    countarr[int(spr3.get())] += 1
    countarr[int(spr4.get())] += 1
    countarr[int(spr5.get())] += 1
    countarr[int(spr6.get())] += 1
    countarr[int(spr7.get())] += 1
    countarr[int(spr8.get())] += 1
    countarr[int(spr9.get())] += 1
    for i in range (SPR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",spring\n")
    
    countarr = [0 for i in range(RAB+1)]
    countarr[int(rab1.get())] += 1
    countarr[int(rab2.get())] += 1
    countarr[int(rab3.get())] += 1
    countarr[int(rab4.get())] += 1
    countarr[int(rab5.get())] += 1
    countarr[int(rab6.get())] += 1
    countarr[int(rab7.get())] += 1
    for i in range (RAB+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",rab\n")

    countarr = [0 for i in range(GB+1)]
    countarr[int(gb1.get())] += 1
    countarr[int(gb2.get())] += 1
    countarr[int(gb3.get())] += 1
    countarr[int(gb4.get())] += 1
    countarr[int(gb5.get())] += 1
    countarr[int(gb6.get())] += 1
    countarr[int(gb7.get())] += 1
    for i in range (GB+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",gb\n")

    countarr = [0 for i in range(SAM+1)]
    countarr[int(sam1.get())] += 1
    countarr[int(sam2.get())] += 1
    countarr[int(sam3.get())] += 1
    countarr[int(sam4.get())] += 1
    countarr[int(sam5.get())] += 1
    countarr[int(sam6.get())] += 1
    countarr[int(sam7.get())] += 1
    countarr[int(sam8.get())] += 1
    for i in range (SAM+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",sam\n")
    
    countarr = [0 for i in range(SKELT+1)]
    countarr[int(ske1.get())] += 1 
    countarr[int(ske2.get())] += 1
    countarr[int(ske3.get())] += 1
    countarr[int(ske4.get())] += 1
    for i in range (SKELT+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",skelly\n")
    
    countarr = [0 for i in range(NADO+1)]
    countarr[int(nado1.get())] += 1 
    for i in range (NADO+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",nado\n")
    
    countarr = [0 for i in range(CAMP+1)]
    countarr[int(camp1.get())] += 1 
    countarr[int(camp2.get())] += 1
    countarr[int(camp3.get())] += 1
    countarr[int(camp4.get())] += 1
    for i in range (CAMP+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",camp\n")

    countarr = [0 for i in range(BAR+1)]
    countarr[int(bar1.get())] += 1 
    countarr[int(bar2.get())] += 1
    countarr[int(bar3.get())] += 1
    countarr[int(bar4.get())] += 1
    for i in range (BAR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",baracks\n")

    countarr = [0 for i in range(DBAR+1)]
    countarr[int(dbar1.get())] += 1 
    countarr[int(dbar2.get())] += 1
    for i in range (DBAR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",dark baracks\n")
    
    file.write(lab1.get() + ",x1,lab\n")
    file.write(spf1.get() + ",x1,spell fac\n")
    file.write(dspf1.get() + ",x1,de spell fac\n")
    file.write(wrk1.get() + ",x1,workshop\n")
    file.write(pet1.get() + ",x1,pet\n")

    countarr = [0 for i in range(STORAGE+1)]
    countarr[int(glds1.get())] += 1 
    countarr[int(glds2.get())] += 1
    countarr[int(glds3.get())] += 1
    countarr[int(glds4.get())] += 1
    for i in range (STORAGE+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",gold storage\n")
    
    countarr = [0 for i in range(STORAGE+1)]
    countarr[int(elxs1.get())] += 1 
    countarr[int(elxs2.get())] += 1
    countarr[int(elxs3.get())] += 1
    countarr[int(elxs4.get())] += 1
    for i in range (STORAGE+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",elix storage\n")

    countarr = [0 for i in range(COLLECTOR+1)]
    countarr[int(gldm1.get())] += 1 
    countarr[int(gldm2.get())] += 1
    countarr[int(gldm3.get())] += 1
    countarr[int(gldm4.get())] += 1
    countarr[int(gldm5.get())] += 1
    countarr[int(gldm6.get())] += 1
    countarr[int(gldm7.get())] += 1
    for i in range (COLLECTOR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",gold mine\n")

    countarr = [0 for i in range(COLLECTOR+1)]
    countarr[int(elxc1.get())] += 1 
    countarr[int(elxc2.get())] += 1
    countarr[int(elxc3.get())] += 1
    countarr[int(elxc4.get())] += 1
    countarr[int(elxc5.get())] += 1
    countarr[int(elxc6.get())] += 1
    countarr[int(elxc7.get())] += 1
    for i in range (COLLECTOR+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",elix collector\n")
    
    countarr = [0 for i in range(DEDRILL+1)]
    countarr[int(delxc1.get())] += 1 
    countarr[int(delxc2.get())] += 1
    countarr[int(delxc3.get())] += 1
    for i in range (DEDRILL+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",de drill\n")
    
    countarr = [0 for i in range(DESTORAGE+1)]
    countarr[int(delxs1.get())] += 1 
    for i in range (DEDRILL+1):
        if countarr[i] != 0:
            file.write(str(i) + ",x" + str(countarr[i]) + ",de storage\n")
    
    file.write(cc1.get() + ",x1,cc\n")
    file.close()
    
    



    file.close()
    
def th14Hero():
    clear()
    # Troop/Hero/Pet levels
    heroLevels = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22',
            '23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44',
            '45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66',
            '67','68','69','70','71','72','73','74','75','76','77','78','79','80']

    # ---BK---
    Label(main, text="Barbarian King:").grid(row=0, column=0)
    global bk1
    bk1 = StringVar()
    bk1.set('0')
    OptionMenu(main, bk1, *heroLevels).grid(row=0, column=1)

    # ---AQ---
    Label(main, text="Archer Queen:").grid(row=1, column=0)
    global aq1
    aq1 = StringVar()
    aq1.set('0')
    OptionMenu(main, aq1, *heroLevels).grid(row=1, column=1)

    # ---GW---
    Label(main, text="Grand Warden:").grid(row=2, column=0)
    global gw1
    gw1 = StringVar()
    gw1.set('0')
    OptionMenu(main, gw1, *heroLevels[:-25]).grid(row=2, column=1)

    # ---RC---
    Label(main, text="Royal Champion:").grid(row=3, column=0)
    global rc1
    rc1 = StringVar()
    rc1.set('0')
    OptionMenu(main, rc1, *heroLevels[:-50]).grid(row=3, column=1)

    # ---LASSI---
    Label(main, text="Lassi:").grid(row=4, column=0)
    global las1
    las1 = StringVar()
    las1.set('0')
    OptionMenu(main, las1, *heroLevels[:-70]).grid(row=4, column=1)

    # ---OWL---
    Label(main, text="Owl:").grid(row=5, column=0)
    global owl1
    owl1 = StringVar()
    owl1.set('0')
    OptionMenu(main, owl1, *heroLevels[:-70]).grid(row=5, column=1)

    # ---YAK---
    Label(main, text="Yak:").grid(row=6, column=0)
    global yak1
    yak1 = StringVar()
    yak1.set('0')
    OptionMenu(main, yak1, *heroLevels[:-70]).grid(row=6, column=1)

    # ---UNICORN---
    Label(main, text="Unicorn:").grid(row=7, column=0)
    global uni1
    uni1 = StringVar()
    uni1.set('0')
    OptionMenu(main, uni1, *heroLevels[:-70]).grid(row=7, column=1)

    Label(main, text="LAB TROOPS", fg="red").grid(row=8, column=0)
    # ---BARB---
    Label(main, text="Barbarian:").grid(row=9, column=0)
    global barb1
    barb1 = StringVar()
    barb1.set('0')
    OptionMenu(main, barb1, *heroLevels[:-70]).grid(row=9, column=1)

    # ---ARCH---
    Label(main, text="Archer:").grid(row=10, column=0)
    global arch1
    arch1 = StringVar()
    arch1.set('0')
    OptionMenu(main, arch1, *heroLevels[:-70]).grid(row=10, column=1)

    # ---Giant---
    Label(main, text="Giant:").grid(row=11, column=0)
    global gi1
    gi1 = StringVar()
    gi1.set('0')
    OptionMenu(main, gi1, *heroLevels[:-70]).grid(row=11, column=1)

    # ---GOB---
    Label(main, text="Goblin:").grid(row=12, column=0)
    global gob1
    gob1 = StringVar()
    gob1.set('0')
    OptionMenu(main, gob1, *heroLevels[:-72]).grid(row=12, column=1)

    # ---WB---
    Label(main, text="Wall Breaker:").grid(row=13, column=0)
    global wb1
    wb1 = StringVar()
    wb1.set('0')
    OptionMenu(main, wb1, *heroLevels[:-70]).grid(row=13, column=1)
    
    # ---LOON---
    Label(main, text="Baloon:").grid(row=14, column=0)
    global loon1
    loon1 = StringVar()
    loon1.set('0')
    OptionMenu(main, loon1, *heroLevels[:-71]).grid(row=14, column=1)
    
    # ---WIZ---
    Label(main, text="Wizard:").grid(row=15, column=0)
    global wiz1
    wiz1 = StringVar()
    wiz1.set('0')
    OptionMenu(main, wiz1, *heroLevels[:-70]).grid(row=15, column=1)
    
    # ---HEALER---
    Label(main, text="Healer:").grid(row=16, column=0)
    global helr1
    helr1 = StringVar()
    helr1.set('0')
    OptionMenu(main, helr1, *heroLevels[:-73]).grid(row=16, column=1)
    
    # ---DRAG---
    Label(main, text="Dragon:").grid(row=17, column=0)
    global drag1
    drag1 = StringVar()
    drag1.set('0')
    OptionMenu(main, drag1, *heroLevels[:-72]).grid(row=17, column=1)
    
    # ---PEKKA---
    Label(main, text="PEKKA:").grid(row=18, column=0)
    global pek1
    pek1 = StringVar()
    pek1.set('0')
    OptionMenu(main, pek1, *heroLevels[:-71]).grid(row=18, column=1)
    
    # ---BD---
    Label(main, text="Baby Dragon:").grid(row=19, column=0)
    global bd1
    bd1 = StringVar()
    bd1.set('0')
    OptionMenu(main, bd1, *heroLevels[:-72]).grid(row=19, column=1)
    
    # ---MINER---
    Label(main, text="Miner:").grid(row=20, column=0)
    global mine1
    mine1 = StringVar()
    mine1.set('0')
    OptionMenu(main, mine1, *heroLevels[:-73]).grid(row=20, column=1)

    # ---EDRAG---
    Label(main, text="Electro Dragon:").grid(row=21, column=0)
    global ed1
    ed1 = StringVar()
    ed1.set('0')
    OptionMenu(main, ed1, *heroLevels[:-76]).grid(row=21, column=1)

    # ---YETI---
    Label(main, text="Yeti:").grid(row=22, column=0)
    global yeti1
    yeti1 = StringVar()
    yeti1.set('0')
    OptionMenu(main, yeti1, *heroLevels[:-77]).grid(row=22, column=1)

    # ---MIN---
    Label(main, text="Minion:").grid(row=23, column=0)
    global min1
    min1 = StringVar()
    min1.set('0')
    OptionMenu(main, min1, *heroLevels[:-70]).grid(row=23, column=1)

    # ---HOG---
    Label(main, text="Hog Rider:").grid(row=24, column=0)
    global hog1
    hog1 = StringVar()
    hog1.set('0')
    OptionMenu(main, hog1, *heroLevels[:-70]).grid(row=24, column=1)

    # ---VALK---
    Label(main, text="Valkyrie:").grid(row=25, column=0)
    global valk1
    valk1 = StringVar()
    valk1.set('0')
    OptionMenu(main, valk1, *heroLevels[:-71]).grid(row=25, column=1)

    # ---GOLEM---
    Label(main, text="Golem:").grid(row=26, column=0)
    global gol1
    gol1 = StringVar()
    gol1.set('0')
    OptionMenu(main, gol1, *heroLevels[:-70]).grid(row=26, column=1)

    # ---WITCH---
    Label(main, text="Witch:").grid(row=27, column=0)
    global witc1
    witc1 = StringVar()
    witc1.set('0')
    OptionMenu(main, witc1, *heroLevels[:-75]).grid(row=27, column=1)

    # ---LAVA---
    Label(main, text="Lava Hound:").grid(row=28, column=0)
    global lava1
    lava1 = StringVar()
    lava1.set('0')
    OptionMenu(main, lava1, *heroLevels[:-74]).grid(row=28, column=1)

    # ---BOWLER---
    Label(main, text="Bowler:").grid(row=29, column=0)
    global bowl1
    bowl1 = StringVar()
    bowl1.set('0')
    OptionMenu(main, bowl1, *heroLevels[:-75]).grid(row=29, column=1)

    # ---IG---
    Label(main, text="Ice Golem:").grid(row=30, column=0)
    global ig1
    ig1 = StringVar()
    ig1.set('0')
    OptionMenu(main, ig1, *heroLevels[:-74]).grid(row=30, column=1)

    # ---HH---
    Label(main, text="Head Hunter:").grid(row=31, column=0)
    global hh1
    hh1 = StringVar()
    hh1.set('0')
    OptionMenu(main, hh1, *heroLevels[:-77]).grid(row=31, column=1)

    Label(main, text="LAB SPELLS", fg="red").grid(row=0, column=2)
    # ---LIGHTNING---
    Label(main, text="Lightning Spell:").grid(row=1, column=2)
    global zap1
    zap1 = StringVar()
    zap1.set('0')
    OptionMenu(main, zap1, *heroLevels[:-71]).grid(row=1, column=3)

    # ---HEAL---
    Label(main, text="Healing Spell:").grid(row=2, column=2)
    global heal1
    heal1 = StringVar()
    heal1.set('0')
    OptionMenu(main, heal1, *heroLevels[:-72]).grid(row=2, column=3)

    # ---RAGE---
    Label(main, text="Rage Spell:").grid(row=3, column=2)
    global rage1
    rage1 = StringVar()
    rage1.set('0')
    OptionMenu(main, rage1, *heroLevels[:-74]).grid(row=3, column=3)

    # ---JUMP---
    Label(main, text="Jump Spell:").grid(row=4, column=2)
    global jump1
    jump1 = StringVar()
    jump1.set('0')
    OptionMenu(main, jump1, *heroLevels[:-76]).grid(row=4, column=3)

    # ---FREEZE---
    Label(main, text="Freeze Spell:").grid(row=5, column=2)
    global frz1
    frz1 = StringVar()
    frz1.set('0')
    OptionMenu(main, frz1, *heroLevels[:-73]).grid(row=5, column=3)

    # ---CLONE---
    Label(main, text="Clone Spell:").grid(row=6, column=2)
    global cln1
    cln1 = StringVar()
    cln1.set('0')
    OptionMenu(main, cln1, *heroLevels[:-73]).grid(row=6, column=3)

    # ---INVIS---
    Label(main, text="Invisibility Spell:").grid(row=7, column=2)
    global invs1
    invs1 = StringVar()
    invs1.set('0')
    OptionMenu(main, invs1, *heroLevels[:-76]).grid(row=7, column=3)

    # ---POI---
    Label(main, text="Poison Spell:").grid(row=8, column=2)
    global poi1
    poi1 = StringVar()
    poi1.set('0')
    OptionMenu(main, poi1, *heroLevels[:-72]).grid(row=8, column=3)

    # ---EQ---
    Label(main, text="Earthquake Spell:").grid(row=9, column=2)
    global eq1
    eq1 = StringVar()
    eq1.set('0')
    OptionMenu(main, eq1, *heroLevels[:-75]).grid(row=9, column=3)

    # ---HASTE---
    Label(main, text="Haste Spell:").grid(row=10, column=2)
    global hste1
    hste1 = StringVar()
    hste1.set('0')
    OptionMenu(main, hste1, *heroLevels[:-75]).grid(row=10, column=3)

    # ---SKELLY SPELL---
    Label(main, text="Skeleton Spell:").grid(row=11, column=2)
    global sksp1
    sksp1 = StringVar()
    sksp1.set('0')
    OptionMenu(main, sksp1, *heroLevels[:-73]).grid(row=11, column=3)

    # ---BAT---
    Label(main, text="Bat Spell:").grid(row=12, column=2)
    global bat1
    bat1 = StringVar()
    bat1.set('0')
    OptionMenu(main, bat1, *heroLevels[:-75]).grid(row=12, column=3)

    Label(main, text="LAB SIEGES", fg="red").grid(row=13, column=2)
    # ---WW---
    Label(main, text="Wall Wrecker:").grid(row=14, column=2)
    global ww1
    ww1 = StringVar()
    ww1.set('0')
    OptionMenu(main, ww1, *heroLevels[:-76]).grid(row=14, column=3)

    # ---BLIMP---
    Label(main, text="Battle Blimp:").grid(row=15, column=2)
    global blmp1
    blmp1 = StringVar()
    blmp1.set('0')
    OptionMenu(main, blmp1, *heroLevels[:-76]).grid(row=15, column=3)

    # ---Slammer---
    Label(main, text="Stone Slammer:").grid(row=16, column=2)
    global ss1
    ss1 = StringVar()
    ss1.set('0')
    OptionMenu(main, ss1, *heroLevels[:-76]).grid(row=16, column=3)

    # ---SIEGE BARACKS---
    Label(main, text="Siege Baracks:").grid(row=17, column=2)
    global sb1
    sb1 = StringVar()
    sb1.set('0')
    OptionMenu(main, sb1, *heroLevels[:-76]).grid(row=17, column=3)

    # ---LOG LAUNCHER---
    Label(main, text="Log Launcher:").grid(row=18, column=2)
    global log1
    log1 = StringVar()
    log1.set('0')
    OptionMenu(main, log1, *heroLevels[:-76]).grid(row=18, column=3)

    Button(main, text="DONE", command=compile_res).grid(row=21, column=3)


# def th12():
    # default: rc, pet, giga it, th14, 2 scatter, 5 huts, 2 bombs, 1 spring, 1 rab, 1 gb, 2 sam, 1 skelly
    # file = open("currentlvl.txt", "a+")
    # file.write("0,x1,rc\n")
    # file.write("0,x1,pet\n")
    # file.write("0,x1,giga it\n")
    # file.write("0,x1,th14\n")
    # file.write("0,x2,scatter\n")
    # file.write("1,x5,hut\n")
    # file.write("0,x2,bomb\n")
    # file.write("0,x1,spring\n")
    # file.write("0,x1,rab\n")
    # file.write("0,x1,gb\n")
    # file.write("0,x2,sam\n")
    # file.write("0,x1,skelly\n")
    
    #file.close()


# def th13():
    # default: pet, th14, 5 huts, 1 bomb, 1 rab, 1 gb, 1 sam, 1 skelly, giga tesla max
    # file = open("currentlvl.txt", "a+")
    # file.write("5,x1,giga tesla\n")
    # file.write("0,x1,pet\n")
    # file.write("0,x1,th14\n")
    # file.write("1,x5,hut\n")
    # file.write("0,x1,bomb\n")
    # file.write("0,x1,rab\n")
    # file.write("0,x1,gb\n")
    # file.write("0,x1,sam\n")
    # file.write("0,x1,skelly\n")

    #file.close()

def th14():
    levels = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    # default: giga tesla max, giga it max
    file = open("currentlvl.txt", "a+")
    file.write("5,x1,giga tesla\n")
    file.write("5,x1,giga it\n")
    file.close()
    # input for user levels
    # ---Cannons---
    Label(main, text="CANNONS", fg="red").grid(row=0, column=0)
    global can1, can2, can3, can4, can5, can6, can7
    can1 = StringVar()
    can1.set('0')
    Label(main, text="cannon 1 level:").grid(row=1, column=0)
    OptionMenu(main, can1, *levels).grid(row=1, column=1)
    can2 = StringVar()
    can2.set('0')
    Label(main, text="cannon 2 level:").grid(row=2, column=0)
    OptionMenu(main, can2, *levels).grid(row=2, column=1)
    can3 = StringVar()
    can3.set('0')
    Label(main, text="cannon 3 level:").grid(row=3, column=0)
    OptionMenu(main, can3, *levels).grid(row=3, column=1)
    can4 = StringVar()
    can4.set('0')
    Label(main, text="cannon 4 level:").grid(row=4, column=0)
    OptionMenu(main, can4, *levels).grid(row=4, column=1)
    can5 = StringVar()
    can5.set('0')
    Label(main, text="cannon 5 level:").grid(row=5, column=0)
    OptionMenu(main, can5, *levels).grid(row=5, column=1)
    can6 = StringVar()
    can6.set('0')
    Label(main, text="cannon 6 level:").grid(row=6, column=0)
    OptionMenu(main, can6, *levels).grid(row=6, column=1)
    can7 = StringVar()
    can7.set('0')
    Label(main, text="cannon 7 level:").grid(row=7, column=0)
    OptionMenu(main, can7, *levels).grid(row=7, column=1)

    # ---ATs---
    Label(main, text="ARCHER TOWERS", fg="red").grid(row=8, column=0)
    global at1, at2, at3, at4, at5, at6, at7, at8
    at1 = StringVar()
    at1.set('0')
    Label(main, text="archer tower 1 level:").grid(row=9, column=0)
    OptionMenu(main, at1, *levels[:-1]).grid(row=9, column=1)
    at2 = StringVar()
    at2.set('0')
    Label(main, text="archer tower 2 level:").grid(row=10, column=0)
    OptionMenu(main, at2, *levels[:-1]).grid(row=10, column=1)
    at3 = StringVar()
    at3.set('0')
    Label(main, text="archer tower 3 level:").grid(row=11, column=0)
    OptionMenu(main, at3, *levels[:-1]).grid(row=11, column=1)
    at4 = StringVar()
    at4.set('0')
    Label(main, text="archer tower 4 level:").grid(row=11, column=0)
    OptionMenu(main, at4, *levels[:-1]).grid(row=11, column=1)
    at5 = StringVar()
    at5.set('0')
    Label(main, text="archer tower 5 level:").grid(row=12, column=0)
    OptionMenu(main, at5, *levels[:-1]).grid(row=12, column=1)
    at6 = StringVar()
    at6.set('0')
    Label(main, text="archer tower 6 level:").grid(row=13, column=0)
    OptionMenu(main, at6, *levels[:-1]).grid(row=13, column=1)
    at7 = StringVar()
    at7.set('0')
    Label(main, text="archer tower 7 level:").grid(row=14, column=0)
    OptionMenu(main, at7, *levels[:-1]).grid(row=14, column=1)
    at8 = StringVar()
    at8.set('0')
    Label(main, text="archer tower 8 level:").grid(row=15, column=0)
    OptionMenu(main, at8, *levels[:-1]).grid(row=15, column=1)

    # ---Mortars---
    Label(main, text="MORTARS", fg="red").grid(row=16, column=0)
    global mor1, mor2, mor3, mor4
    mor1 = StringVar()
    mor1.set('0')
    Label(main, text="mortar 1 level:").grid(row=17, column=0)
    OptionMenu(main, mor1, *levels[:-7]).grid(row=17, column=1)
    mor2 = StringVar()
    mor2.set('0')
    Label(main, text="mortar 2 level:").grid(row=18, column=0)
    OptionMenu(main, mor2, *levels[:-7]).grid(row=18, column=1)
    mor3 = StringVar()
    mor3.set('0')
    Label(main, text="mortar 3 level:").grid(row=19, column=0)
    OptionMenu(main, mor3, *levels[:-7]).grid(row=19, column=1)
    mor4 = StringVar()
    mor4.set('0')
    Label(main, text="mortar 4 level:").grid(row=20, column=0)
    OptionMenu(main, mor4, *levels[:-7]).grid(row=20, column=1)

    # ---HUTS---
    Label(main, text="BUILDER HUTS", fg="red").grid(row=21, column=0)
    global hut1, hut2, hut3, hut4, hut5
    hut1 = StringVar()
    hut1.set('0')
    Label(main, text="hut 1 level:").grid(row=22, column=0)
    OptionMenu(main, hut1, *levels[:-16]).grid(row=22, column=1)
    hut2 = StringVar()
    hut2.set('0')
    Label(main, text="hut 2 level:").grid(row=23, column=0)
    OptionMenu(main, hut2, *levels[:-16]).grid(row=23, column=1)
    hut3 = StringVar()
    hut3.set('0')
    Label(main, text="hut 3 level:").grid(row=24, column=0)
    OptionMenu(main, hut3, *levels[:-16]).grid(row=24, column=1)
    hut4 = StringVar()
    hut4.set('0')
    Label(main, text="hut 4 level:").grid(row=25, column=0)
    OptionMenu(main, hut4, *levels[:-16]).grid(row=25, column=1)
    hut5 = StringVar()
    hut5.set('0')
    Label(main, text="hut 5 level:").grid(row=26, column=0)
    OptionMenu(main, hut5, *levels[:-16]).grid(row=26, column=1)

    # ---WTS---
    Label(main, text="WIZARD TOWERS", fg="red").grid(row=27, column=0)
    global wt1, wt2, wt3, wt4, wt5
    wt1 = StringVar()
    wt1.set('0')
    Label(main, text="wiz tower 1 level:").grid(row=28, column=0)
    OptionMenu(main, wt1, *levels[:-7]).grid(row=28, column=1)
    wt2 = StringVar()
    wt2.set('0')
    Label(main, text="wiz tower 2 level:").grid(row=29, column=0)
    OptionMenu(main, wt2, *levels[:-7]).grid(row=29, column=1)
    wt3 = StringVar()
    wt3.set('0')
    Label(main, text="wiz tower 3 level:").grid(row=30, column=0)
    OptionMenu(main, wt3, *levels[:-7]).grid(row=30, column=1)
    wt4 = StringVar()
    wt4.set('0')
    Label(main, text="wiz tower 4 level:").grid(row=31, column=0)
    OptionMenu(main, wt4, *levels[:-7]).grid(row=31, column=1)
    wt5 = StringVar()
    wt5.set('0')
    Label(main, text="wiz tower 5 level:").grid(row=32, column=0)
    OptionMenu(main, wt5, *levels[:-7]).grid(row=32, column=1)

    # ---AIR SWEEPS---
    Label(main, text="AIR SWEEPERS", fg="red").grid(row=0, column=2)
    global as1, as2
    as1 = StringVar()
    as1.set('0')
    Label(main, text="air sweeper 1 level:").grid(row=1, column=2)
    OptionMenu(main, as1, *levels[:-13]).grid(row=1, column=3)
    as2 = StringVar()
    as2.set('0')
    Label(main, text="air sweeper 2 level:").grid(row=2, column=2)
    OptionMenu(main, as2, *levels[:-13]).grid(row=2, column=3)

    # ---TESLAS---
    Label(main, text="TESLAS", fg="red").grid(row=3, column=2)
    global tes1, tes2, tes3, tes4, tes5
    tes1 = StringVar()
    tes1.set('0')
    Label(main, text="tesla 1 level:").grid(row=4, column=2)
    OptionMenu(main, tes1, *levels[:-7]).grid(row=4, column=3)
    tes2 = StringVar()
    tes2.set('0')
    Label(main, text="tesla 2 level:").grid(row=5, column=2)
    OptionMenu(main, tes2, *levels[:-7]).grid(row=5, column=3)
    tes3 = StringVar()
    tes3.set('0')
    Label(main, text="tesla 3 level:").grid(row=6, column=2)
    OptionMenu(main, tes3, *levels[:-7]).grid(row=6, column=3)
    tes4 = StringVar()
    tes4.set('0')
    Label(main, text="tesla 4 level:").grid(row=7, column=2)
    OptionMenu(main, tes4, *levels[:-7]).grid(row=7, column=3)
    tes5 = StringVar()
    tes5.set('0')
    Label(main, text="tesla 5 level:").grid(row=8, column=2)
    OptionMenu(main, tes5, *levels[:-7]).grid(row=8, column=3)

    # ---BTS---
    Label(main, text="BOMB TOWERS", fg="red").grid(row=9, column=2)
    global bt1, bt2
    bt1 = StringVar()
    bt1.set('0')
    Label(main, text="bt 1 level:").grid(row=10, column=2)
    OptionMenu(main, bt1, *levels[:-11]).grid(row=10, column=3)
    bt2 = StringVar()
    bt2.set('0')
    Label(main, text="bt 2 level:").grid(row=11, column=2)
    OptionMenu(main, bt2, *levels[:-11]).grid(row=11, column=3)

    # ---XBOWS---
    Label(main, text="XBOWS", fg="red").grid(row=12, column=2)
    global bow1, bow2, bow3, bow4
    bow1 = StringVar()
    bow1.set('0')
    Label(main, text="xbow 1 level:").grid(row=13, column=2)
    OptionMenu(main, bow1, *levels[:-12]).grid(row=13, column=3)
    bow2 = StringVar()
    bow2.set('0')
    Label(main, text="xbow 2 level:").grid(row=14, column=2)
    OptionMenu(main, bow2, *levels[:-12]).grid(row=14, column=3)
    bow3 = StringVar()
    bow3.set('0')
    Label(main, text="xbow 3 level:").grid(row=15, column=2)
    OptionMenu(main, bow3, *levels[:-12]).grid(row=15, column=3)
    bow4 = StringVar()
    bow4.set('0')
    Label(main, text="xbow 4 level:").grid(row=16, column=2)
    OptionMenu(main, bow4, *levels[:-12]).grid(row=16, column=3)

    # ---ITS---
    Label(main, text="INFERNO TOWERS", fg="red").grid(row=17, column=2)
    global it1, it2, it3
    it1 = StringVar()
    it1.set('0')
    Label(main, text="it 1 level:").grid(row=18, column=2)
    OptionMenu(main, it1, *levels[:-12]).grid(row=18, column=3)
    it2 = StringVar()
    it2.set('0')
    Label(main, text="it 2 level:").grid(row=19, column=2)
    OptionMenu(main, it2, *levels[:-12]).grid(row=19, column=3)
    it3 = StringVar()
    it3.set('0')
    Label(main, text="it 3 level:").grid(row=20, column=2)
    OptionMenu(main, it3, *levels[:-12]).grid(row=20, column=3)

    # ---EA---
    Label(main, text="EAGLE ARTILLERY", fg="red").grid(row=21, column=2)
    global ea1
    ea1 = StringVar()
    ea1.set('0')
    Label(main, text="ea level:").grid(row=22, column=2)
    OptionMenu(main, ea1, *levels[:-15]).grid(row=22, column=3)

    # ---SCATTER---
    Label(main, text="SCATTERSHOTS", fg="red").grid(row=23, column=2)
    global sca1, sca2
    sca1 = StringVar()
    sca1.set('0')
    Label(main, text="scatter 1 level:").grid(row=24, column=2)
    OptionMenu(main, sca1, *levels[:-17]).grid(row=24, column=3)
    sca2 = StringVar()
    sca2.set('0')
    Label(main, text="scatter 2 level:").grid(row=25, column=2)
    OptionMenu(main, sca2, *levels[:-17]).grid(row=25, column=3)

    # ---GIGA IT (TH14)---
    Label(main, text="GIGA IT(TH14)", fg="red").grid(row=26, column=2)
    global git1
    git1 = StringVar()
    git1.set('0')
    Label(main, text="giga it level:").grid(row=27, column=2)
    OptionMenu(main, git1, *levels[:-15]).grid(row=27, column=3)

    # ---Air Ds---
    Label(main, text="AIR DEFENSES", fg="red").grid(row=28, column=2)
    global ad1, ad2, ad3, ad4
    ad1 = StringVar()
    ad1.set('0')
    Label(main, text="air d 1 level:").grid(row=29, column=2)
    OptionMenu(main, ad1, *levels[:-9]).grid(row=29, column=3)
    ad2 = StringVar()
    ad2.set('0')
    Label(main, text="air d 2 level:").grid(row=30, column=2)
    OptionMenu(main, ad2, *levels[:-9]).grid(row=30, column=3)
    ad3 = StringVar()
    ad3.set('0')
    Label(main, text="air d 3 level:").grid(row=31, column=2)
    OptionMenu(main, ad3, *levels[:-9]).grid(row=31, column=3)
    ad4 = StringVar()
    ad4.set('0')
    Label(main, text="air d 4 level:").grid(row=32, column=2)
    OptionMenu(main, ad4, *levels[:-9]).grid(row=32, column=3)

    # ---Bombs---
    Label(main, text="BOMBS", fg="red").grid(row=0, column=4)
    global bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7, bomb8
    bomb1 = StringVar()
    bomb1.set('0')
    Label(main, text="bomb 1 level:").grid(row=1, column=4)
    OptionMenu(main, bomb1, *levels[:-10]).grid(row=1, column=5)
    bomb2 = StringVar()
    bomb2.set('0')
    Label(main, text="bomb 2 level:").grid(row=2, column=4)
    OptionMenu(main, bomb2, *levels[:-10]).grid(row=2, column=5)
    bomb3 = StringVar()
    bomb3.set('0')
    Label(main, text="bomb 3 level:").grid(row=3, column=4)
    OptionMenu(main, bomb3, *levels[:-10]).grid(row=3, column=5)
    bomb4 = StringVar()
    bomb4.set('0')
    Label(main, text="bomb 4 level:").grid(row=4, column=4)
    OptionMenu(main, bomb4, *levels[:-10]).grid(row=4, column=5)
    bomb5 = StringVar()
    bomb5.set('0')
    Label(main, text="bomb 5 level:").grid(row=5, column=4)
    OptionMenu(main, bomb5, *levels[:-10]).grid(row=5, column=5)
    bomb6 = StringVar()
    bomb6.set('0')
    Label(main, text="bomb 6 level:").grid(row=6, column=4)
    OptionMenu(main, bomb6, *levels[:-10]).grid(row=6, column=5)
    bomb7 = StringVar()
    bomb7.set('0')
    Label(main, text="bomb 7 level:").grid(row=7, column=4)
    OptionMenu(main, bomb7, *levels[:-10]).grid(row=7, column=5)
    bomb8 = StringVar()
    bomb8.set('0')
    Label(main, text="bomb 8 level:").grid(row=8, column=4)
    OptionMenu(main, bomb8, *levels[:-10]).grid(row=8, column=5)

    # ---Springs---
    Label(main, text="SPRING TRAPS", fg="red").grid(row=9, column=4)
    global spr1, spr2, spr3, spr4, spr5, spr6, spr7, spr8, spr9
    spr1 = StringVar()
    spr1.set('0')
    Label(main, text="spring 1 level:").grid(row=10, column=4)
    OptionMenu(main, spr1, *levels[:-15]).grid(row=10, column=5)
    spr2 = StringVar()
    spr2.set('0')
    Label(main, text="spring 2 level:").grid(row=11, column=4)
    OptionMenu(main, spr2, *levels[:-15]).grid(row=11, column=5)
    spr3 = StringVar()
    spr3.set('0')
    Label(main, text="spring 3 level:").grid(row=12, column=4)
    OptionMenu(main, spr3, *levels[:-15]).grid(row=12, column=5)
    spr4 = StringVar()
    spr4.set('0')
    Label(main, text="spring 4 level:").grid(row=13, column=4)
    OptionMenu(main, spr4, *levels[:-15]).grid(row=13, column=5)
    spr5 = StringVar()
    spr5.set('0')
    Label(main, text="spring 5 level:").grid(row=14, column=4)
    OptionMenu(main, spr5, *levels[:-15]).grid(row=14, column=5)
    spr6 = StringVar()
    spr6.set('0')
    Label(main, text="spring 6 level:").grid(row=15, column=4)
    OptionMenu(main, spr6, *levels[:-15]).grid(row=15, column=5)
    spr7 = StringVar()
    spr7.set('0')
    Label(main, text="spring 7 level:").grid(row=16, column=4)
    OptionMenu(main, spr7, *levels[:-15]).grid(row=16, column=5)
    spr8 = StringVar()
    spr8.set('0')
    Label(main, text="spring 8 level:").grid(row=17, column=4)
    OptionMenu(main, spr8, *levels[:-15]).grid(row=17, column=5)
    spr9 = StringVar()
    spr9.set('0')
    Label(main, text="spring 9 level:").grid(row=18, column=4)
    OptionMenu(main, spr9, *levels[:-15]).grid(row=18, column=5)

    # ---SAM---
    Label(main, text="SEEKING AIR MINES", fg="red").grid(row=19, column=4)
    global sam1, sam2, sam3, sam4, sam5, sam6, sam7, sam8
    sam1 = StringVar()
    sam1.set('0')
    Label(main, text="sam 1 level:").grid(row=20, column=4)
    OptionMenu(main, sam1, *levels[:-16]).grid(row=20, column=5)
    sam2 = StringVar()
    sam2.set('0')
    Label(main, text="sam 2 level:").grid(row=21, column=4)
    OptionMenu(main, sam2, *levels[:-16]).grid(row=21, column=5)
    sam3 = StringVar()
    sam3.set('0')
    Label(main, text="sam 3 level:").grid(row=22, column=4)
    OptionMenu(main, sam3, *levels[:-16]).grid(row=22, column=5)
    sam4 = StringVar()
    sam4.set('0')
    Label(main, text="sam 4 level:").grid(row=23, column=4)
    OptionMenu(main, sam4, *levels[:-16]).grid(row=23, column=5)
    sam5 = StringVar()
    sam5.set('0')
    Label(main, text="sam 5 level:").grid(row=24, column=4)
    OptionMenu(main, sam5, *levels[:-16]).grid(row=24, column=5)
    sam6 = StringVar()
    sam6.set('0')
    Label(main, text="sam 6 level:").grid(row=25, column=4)
    OptionMenu(main, sam6, *levels[:-16]).grid(row=25, column=5)
    sam7 = StringVar()
    sam7.set('0')
    Label(main, text="sam 7 level:").grid(row=26, column=4)
    OptionMenu(main, sam7, *levels[:-16]).grid(row=26, column=5)
    sam8 = StringVar()
    sam8.set('0')
    Label(main, text="sam 8 level:").grid(row=27, column=4)
    OptionMenu(main, sam8, *levels[:-16]).grid(row=27, column=5)

    # ---SKELLY---
    Label(main, text="SKELETON TRAPS", fg="red").grid(row=28, column=4)
    global ske1, ske2, ske3, ske4
    ske1 = StringVar()
    ske1.set('0')
    Label(main, text="skelly 1 level:").grid(row=29, column=4)
    OptionMenu(main, ske1, *levels[:-16]).grid(row=29, column=5)
    ske2 = StringVar()
    ske2.set('0')
    Label(main, text="skelly 2 level:").grid(row=30, column=4)
    OptionMenu(main, ske2, *levels[:-16]).grid(row=30, column=5)
    ske3 = StringVar()
    ske3.set('0')
    Label(main, text="skelly 3 level:").grid(row=31, column=4)
    OptionMenu(main, ske3, *levels[:-16]).grid(row=31, column=5)
    ske4 = StringVar()
    ske4.set('0')
    Label(main, text="skelly 4 level:").grid(row=32, column=4)
    OptionMenu(main, ske4, *levels[:-16]).grid(row=32, column=5)

    # ---RAB---
    Label(main, text="AIR BOMBS", fg="red").grid(row=0, column=6)
    global rab1, rab2, rab3, rab4, rab5, rab6, rab7
    rab1 = StringVar()
    rab1.set('0')
    Label(main, text="rab 1 level:").grid(row=1, column=6)
    OptionMenu(main, rab1, *levels[:-12]).grid(row=1, column=7)
    rab2 = StringVar()
    rab2.set('0')
    Label(main, text="rab 2 level:").grid(row=2, column=6)
    OptionMenu(main, rab2, *levels[:-12]).grid(row=2, column=7)
    rab3 = StringVar()
    rab3.set('0')
    Label(main, text="rab 3 level:").grid(row=3, column=6)
    OptionMenu(main, rab3, *levels[:-12]).grid(row=3, column=7)
    rab4 = StringVar()
    rab4.set('0')
    Label(main, text="rab 4 level:").grid(row=4, column=6)
    OptionMenu(main, rab4, *levels[:-12]).grid(row=4, column=7)
    rab5 = StringVar()
    rab5.set('0')
    Label(main, text="rab 5 level:").grid(row=5, column=6)
    OptionMenu(main, rab5, *levels[:-12]).grid(row=5, column=7)
    rab6 = StringVar()
    rab6.set('0')
    Label(main, text="rab 6 level:").grid(row=6, column=6)
    OptionMenu(main, rab6, *levels[:-12]).grid(row=6, column=7)
    rab7 = StringVar()
    rab7.set('0')
    Label(main, text="rab 7 level:").grid(row=7, column=6)
    OptionMenu(main, rab7, *levels[:-12]).grid(row=7, column=7)

    # ---GB---
    Label(main, text="GIANT BOMBS", fg="red").grid(row=8, column=6)
    global gb1, gb2, gb3, gb4, gb5, gb6, gb7
    gb1 = StringVar()
    gb1.set('0')
    Label(main, text="gb 1 level:").grid(row=9, column=6)
    OptionMenu(main, gb1, *levels[:-13]).grid(row=9, column=7)
    gb2 = StringVar()
    gb2.set('0')
    Label(main, text="gb 2 level:").grid(row=10, column=6)
    OptionMenu(main, gb2, *levels[:-13]).grid(row=10, column=7)
    gb3 = StringVar()
    gb3.set('0')
    Label(main, text="gb 3 level:").grid(row=11, column=6)
    OptionMenu(main, gb3, *levels[:-13]).grid(row=11, column=7)
    gb4 = StringVar()
    gb4.set('0')
    Label(main, text="gb 4 level:").grid(row=12, column=6)
    OptionMenu(main, gb4, *levels[:-13]).grid(row=12, column=7)
    gb5 = StringVar()
    gb5.set('0')
    Label(main, text="gb 5 level:").grid(row=13, column=6)
    OptionMenu(main, gb5, *levels[:-13]).grid(row=13, column=7)
    gb6 = StringVar()
    gb6.set('0')
    Label(main, text="gb 6 level:").grid(row=14, column=6)
    OptionMenu(main, gb6, *levels[:-13]).grid(row=14, column=7)
    gb7 = StringVar()
    gb7.set('0')
    Label(main, text="gb 7 level:").grid(row=15, column=6)
    OptionMenu(main, gb7, *levels[:-13]).grid(row=15, column=7)

    # ---TORNADO---
    Label(main, text="TORNADO TRAP", fg="red").grid(row=16, column=6)
    global nado1
    nado1 = StringVar()
    nado1.set('0')
    Label(main, text="tornado level:").grid(row=17, column=6)
    OptionMenu(main, nado1, *levels[:-17]).grid(row=17, column=7)

    # ---CAMP---
    Label(main, text="ARMY CAMPS", fg="red").grid(row=18, column=6)
    global camp1, camp2, camp3, camp4
    camp1 = StringVar()
    camp1.set('0')
    Label(main, text="camp 1 level:").grid(row=19, column=6)
    OptionMenu(main, camp1, *levels[:-9]).grid(row=19, column=7)
    camp2 = StringVar()
    camp2.set('0')
    Label(main, text="camp 2 level:").grid(row=20, column=6)
    OptionMenu(main, camp2, *levels[:-9]).grid(row=20, column=7)
    camp3 = StringVar()
    camp3.set('0')
    Label(main, text="camp 3 level:").grid(row=21, column=6)
    OptionMenu(main, camp3, *levels[:-9]).grid(row=21, column=7)
    camp4 = StringVar()
    camp4.set('0')
    Label(main, text="camp 4 level:").grid(row=22, column=6)
    OptionMenu(main, camp4, *levels[:-9]).grid(row=22, column=7)

    # ---BARACKS---
    Label(main, text="BARACKS", fg="red").grid(row=23, column=6)
    global bar1, bar2, bar3, bar4
    bar1 = StringVar()
    bar1.set('0')
    Label(main, text="baracks 1 level:").grid(row=24, column=6)
    OptionMenu(main, bar1, *levels[:-6]).grid(row=24, column=7)
    bar2 = StringVar()
    bar2.set('0')
    Label(main, text="baracks 2 level:").grid(row=25, column=6)
    OptionMenu(main, bar2, *levels[:-6]).grid(row=25, column=7)
    bar3 = StringVar()
    bar3.set('0')
    Label(main, text="baracks 3 level:").grid(row=26, column=6)
    OptionMenu(main, bar3, *levels[:-6]).grid(row=26, column=7)
    bar4 = StringVar()
    bar4.set('0')
    Label(main, text="baracks 4 level:").grid(row=27, column=6)
    OptionMenu(main, bar4, *levels[:-6]).grid(row=27, column=7)
     
    # ---DARK BARACKS---
    Label(main, text="DARK BARACKS", fg="red").grid(row=28, column=6)
    global dbar1, dbar2
    dbar1 = StringVar()
    dbar1.set('0')
    Label(main, text="dark baracks 1 level:").grid(row=29, column=6)
    OptionMenu(main, dbar1, *levels[:-11]).grid(row=29, column=7)
    dbar2 = StringVar()
    dbar2.set('0')
    Label(main, text="dark baracks 2 level:").grid(row=30, column=6)
    OptionMenu(main, dbar2, *levels[:-11]).grid(row=30, column=7)

    # ---LAB---
    Label(main, text="LABORATORY", fg="red").grid(row=31, column=6)
    global lab1
    lab1 = StringVar()
    lab1.set('0')
    Label(main, text="lab level:").grid(row=32, column=6)
    OptionMenu(main, lab1, *levels[:-8]).grid(row=32, column=7)

    # ---SPELL FAC---
    Label(main, text="SPELL FACTORY", fg="red").grid(row=0, column=8)
    global spf1
    spf1 = StringVar()
    spf1.set('0')
    Label(main, text="spell fac level:").grid(row=1, column=8)
    OptionMenu(main, spf1, *levels[:-14]).grid(row=1, column=9)

    # ---DE SPELL FAC---
    Label(main, text="DARK SPELL FACTORY", fg="red").grid(row=2, column=8)
    global dspf1
    dspf1 = StringVar()
    dspf1.set('0')
    Label(main, text="de spell fac level:").grid(row=3, column=8)
    OptionMenu(main, dspf1, *levels[:-15]).grid(row=3, column=9)

    # ---WORKSHOP---
    Label(main, text="WORKSHOP", fg="red").grid(row=4, column=8)
    global wrk1
    wrk1 = StringVar()
    wrk1.set('0')
    Label(main, text="workshop level:").grid(row=5, column=8)
    OptionMenu(main, wrk1, *levels[:-15]).grid(row=5, column=9)

    # ---PETHOUSE---
    Label(main, text="PETHOUSE", fg="red").grid(row=6, column=8)
    global pet1
    pet1 = StringVar()
    pet1.set('0')
    Label(main, text="pethouse level:").grid(row=7, column=8)
    OptionMenu(main, pet1, *levels[:-16]).grid(row=7, column=9)

    # ---GOLD MINE---
    Label(main, text="GOLD MINES", fg="red").grid(row=8, column=8)
    global gldm1, gldm2, gldm3, gldm4, gldm5, gldm6, gldm7
    gldm1 = StringVar()
    gldm1.set('0')
    Label(main, text="gold mine 1 level:").grid(row=9, column=8)
    OptionMenu(main, gldm1, *levels[:-6]).grid(row=9, column=9)
    gldm2 = StringVar()
    gldm2.set('0')
    Label(main, text="gold mine 2 level:").grid(row=10, column=8)
    OptionMenu(main, gldm2, *levels[:-6]).grid(row=10, column=9)
    gldm3 = StringVar()
    gldm3.set('0')
    Label(main, text="gold mine 3 level:").grid(row=11, column=8)
    OptionMenu(main, gldm3, *levels[:-6]).grid(row=11, column=9)
    gldm4 = StringVar()
    gldm4.set('0')
    Label(main, text="gold mine 4 level:").grid(row=12, column=8)
    OptionMenu(main, gldm4, *levels[:-6]).grid(row=12, column=9)
    gldm5 = StringVar()
    gldm5.set('0')
    Label(main, text="gold mine 5 level:").grid(row=13, column=8)
    OptionMenu(main, gldm5, *levels[:-6]).grid(row=13, column=9)
    gldm6 = StringVar()
    gldm6.set('0')
    Label(main, text="gold mine 6 level:").grid(row=14, column=8)
    OptionMenu(main, gldm6, *levels[:-6]).grid(row=14, column=9)
    gldm7 = StringVar()
    gldm7.set('0')
    Label(main, text="gold mine 7 level:").grid(row=15, column=8)
    OptionMenu(main, gldm7, *levels[:-6]).grid(row=15, column=9)

    # ---ELIX COLLECTORS---
    Label(main, text="ELIXIR COLLECTORS", fg="red").grid(row=16, column=8)
    global elxc1, elxc2, elxc3, elxc4, elxc5, elxc6, elxc7
    elxc1 = StringVar()
    elxc1.set('0')
    Label(main, text="elix collector 1 level:").grid(row=17, column=8)
    OptionMenu(main, elxc1, *levels[:-6]).grid(row=17, column=9)
    elxc2 = StringVar()
    elxc2.set('0')
    Label(main, text="elix collector 2 level:").grid(row=18, column=8)
    OptionMenu(main, elxc2, *levels[:-6]).grid(row=18, column=9)
    elxc3 = StringVar()
    elxc3.set('0')
    Label(main, text="elix collector 3 level:").grid(row=19, column=8)
    OptionMenu(main, elxc3, *levels[:-6]).grid(row=19, column=9)
    elxc4 = StringVar()
    elxc4.set('0')
    Label(main, text="elix collector 4 level:").grid(row=20, column=8)
    OptionMenu(main, elxc4, *levels[:-6]).grid(row=20, column=9)
    elxc5 = StringVar()
    elxc5.set('0')
    Label(main, text="elix collector 5 level:").grid(row=21, column=8)
    OptionMenu(main, elxc5, *levels[:-6]).grid(row=21, column=9)
    elxc6 = StringVar()
    elxc6.set('0')
    Label(main, text="elix collector 6 level:").grid(row=22, column=8)
    OptionMenu(main, elxc6, *levels[:-6]).grid(row=22, column=9)
    elxc7 = StringVar()
    elxc7.set('0')
    Label(main, text="elix collector 7 level:").grid(row=23, column=8)
    OptionMenu(main, elxc7, *levels[:-6]).grid(row=23, column=9)

    # ---DE COLLECTORS---
    Label(main, text="DARK ELIXIR COLLECTORS", fg="red").grid(row=24, column=8)
    global delxc1, delxc2, delxc3
    delxc1 = StringVar()
    delxc1.set('0')
    Label(main, text="de collector 1 level:").grid(row=25, column=8)
    OptionMenu(main, delxc1, *levels[:-12]).grid(row=25, column=9)
    delxc2 = StringVar()
    delxc2.set('0')
    Label(main, text="de collector 2 level:").grid(row=26, column=8)
    OptionMenu(main, delxc2, *levels[:-12]).grid(row=26, column=9)
    delxc3 = StringVar()
    delxc3.set('0')
    Label(main, text="de collector 3 level:").grid(row=27, column=8)
    OptionMenu(main, delxc3, *levels[:-12]).grid(row=27, column=9)

    # ---GOLD STORAGE---
    Label(main, text="GOLD STORAGES", fg="red").grid(row=28, column=8)
    global glds1, glds2, glds3, glds4
    glds1 = StringVar()
    glds1.set('0')
    Label(main, text="gold storage 1 level:").grid(row=29, column=8)
    OptionMenu(main, glds1, *levels[:-5]).grid(row=29, column=9)
    glds2 = StringVar()
    glds2.set('0')
    Label(main, text="gold storage 2 level:").grid(row=30, column=8)
    OptionMenu(main, glds2, *levels[:-5]).grid(row=30, column=9)
    glds3 = StringVar()
    glds3.set('0')
    Label(main, text="gold storage 3 level:").grid(row=31, column=8)
    OptionMenu(main, glds3, *levels[:-5]).grid(row=31, column=9)
    glds4 = StringVar()
    glds4.set('0')
    Label(main, text="gold storage 4 level:").grid(row=32, column=8)
    OptionMenu(main, glds4, *levels[:-5]).grid(row=32, column=9)

    # ---ELIX STORAGE---
    Label(main, text="ELIXIR STORAGES", fg="red").grid(row=0, column=10)
    global elxs1, elxs2, elxs3, elxs4
    elxs1 = StringVar()
    elxs1.set('0')
    Label(main, text="elix storage 1 level:").grid(row=1, column=10)
    OptionMenu(main, elxs1, *levels[:-5]).grid(row=1, column=11)
    elxs2 = StringVar()
    elxs2.set('0')
    Label(main, text="elix storage 2 level:").grid(row=2, column=10)
    OptionMenu(main, elxs2, *levels[:-5]).grid(row=2, column=11)
    elxs3 = StringVar()
    elxs3.set('0')
    Label(main, text="elix storage 3 level:").grid(row=3, column=10)
    OptionMenu(main, elxs3, *levels[:-5]).grid(row=3, column=11)
    elxs4 = StringVar()
    elxs4.set('0')
    Label(main, text="elix storage 4 level:").grid(row=4, column=10)
    OptionMenu(main, elxs4, *levels[:-5]).grid(row=4, column=11)

    # ---DE STORAGE---
    Label(main, text="DARK ELIXIR STORAGES", fg="red").grid(row=5, column=10)
    global delxs1
    delxs1 = StringVar()
    delxs1.set('0')
    Label(main, text="de storage level:").grid(row=6, column=10)
    OptionMenu(main, delxs1, *levels[:-11]).grid(row=6, column=11)

    # ---CC---
    Label(main, text="CLAN CASTLE", fg="red").grid(row=7, column=10)
    global cc1
    cc1 = StringVar()
    cc1.set('0')
    Label(main, text="cc level:").grid(row=8, column=10)
    OptionMenu(main, cc1, *levels[:-10]).grid(row=8, column=11)


    Button(main, text="DONE", command=th14Hero).grid(row=11, column=11)


def thEntered():
    global thlvl
    clear()
    file = open("currentlvl.txt", "w+")
    file.write(str(thlvl.get()) + ",x1,th\n")
    file.close()
    if thlvl.get() == 14:
        th14()
    # elif thlvl.get() == 13:
    #     th13()
    # else:
    #     th12()
 

# initial screen
thlvl = IntVar()
thLabel = Label(main, text="Choose your TH level").pack()
thlvl14 = Radiobutton(main, text="14", width=10, variable=thlvl, value=14).pack()
#thlvl13 = Radiobutton(main, text="13", width=10, variable=thlvl, value=13).pack()
#thlvl12 = Radiobutton(main, text="12", width=10, variable=thlvl, value=12).pack()
cont = Button(main, text="DONE", command=thEntered).pack()



# Event loop
root.mainloop()

#ctrl+k+c to comment --- ctrl+k+u to uncomment