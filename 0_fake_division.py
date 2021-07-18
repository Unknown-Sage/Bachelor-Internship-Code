#inv_mass_cut

#imfakeindex = np.where(fake_inv_mass < 400)
#imfakeindex = imfakeindex[0]

#fake_inv_mass = np.take(fake_inv_mass,imfakeindex)
#fake_met = np.take(fake_met,imfakeindex)
#fake_weight = np.take(fake_weight,imfakeindex)
#fake_dilep_mass = np.take(fake_dilep_mass,imfakeindex)
#fake_electron_n = np.take(fake_electron_n,imfakeindex)
#fake_muon_n = np.take(fake_muon_n,imfakeindex)
#fake_electron_charge = np.take(fake_electron_charge,imfakeindex)
#fake_muon_charge = np.take(fake_muon_charge,imfakeindex)
#fake_jet_n = np.take(fake_jet_n,imfakeindex)
#fake_jet_btag = np.take(fake_jet_btag,imfakeindex)
#fake_muononz = np.take(fake_muononz,imfakeindex)
#fake_electrononz = np.take(fake_electrononz,imfakeindex)
#fake_electron_mt = np.take(fake_electron_mt,imfakeindex)
#fake_muon_mt = np.take(fake_muon_mt,imfakeindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(fake_electrononz):

    array = np.concatenate((fake_electrononz[n],fake_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

fakeindex = index.astype('int64')

fake_inv_mass = np.take(fake_inv_mass,fakeindex)
fake_met = np.take(fake_met,fakeindex)
fake_weight = np.take(fake_weight,fakeindex)
fake_dilep_mass = np.take(fake_dilep_mass,fakeindex)
fake_electron_n = np.take(fake_electron_n,fakeindex)
fake_muon_n = np.take(fake_muon_n,fakeindex)
fake_electron_charge = np.take(fake_electron_charge,fakeindex)
fake_muon_charge = np.take(fake_muon_charge,fakeindex)
fake_jet_n = np.take(fake_jet_n,fakeindex)
fake_jet_btag = np.take(fake_jet_btag,fakeindex)
fake_electron_mt = np.take(fake_electron_mt,fakeindex)
fake_muon_mt = np.take(fake_muon_mt,fakeindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(fake_jet_btag):

    array = fake_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

fake_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(fake_electron_charge):

    temp1 = fake_electron_charge[n]
    temp2 = fake_muon_charge[n]

    if len(temp1) == 0:
        value = temp2[0] + temp2[1] + temp2[2] + temp2[3]
    if len(temp1) == 1:
        value = temp1[0] + temp2[0] + temp2[1] + temp2[2]
    if len(temp1) == 2:
        value = temp1[1] + temp1[0] + temp2[0] + temp2[1]
    if len(temp1) == 3:
        value = temp1[2] + temp1[1] + temp1[0] + temp2[0]
    if len(temp1) == 4:
        value = temp1[3] + temp1[2] + temp1[1] + temp1[0]

    temp = np.concatenate((temp,[value]))

    n = n+1

fake_total_charge = temp


#add high or low missing transverse energy groups

fakeindexlow = np.where(fake_met < 50)
fakeindexlow = fakeindexlow[0]
fakeindexhigh = np.where(fake_met > 50)
fakeindexhigh = fakeindexhigh[0]


fake_inv_mass_high = np.take(fake_inv_mass,fakeindexhigh)
fake_weight_high = np.take(fake_weight,fakeindexhigh)
fake_dilep_mass_high = np.take(fake_dilep_mass,fakeindexhigh)
fake_electron_n_high = np.take(fake_electron_n,fakeindexhigh)
fake_muon_n_high = np.take(fake_muon_n,fakeindexhigh)
fake_total_charge_high = np.take(fake_total_charge,fakeindexhigh)
fake_jet_n_high = np.take(fake_jet_n,fakeindexhigh)
fake_bjet_n_high = np.take(fake_bjet_n,fakeindexhigh)

fake_electron_mt_high = np.take(fake_electron_mt,fakeindexhigh)
fake_muon_mt_high = np.take(fake_muon_mt,fakeindexhigh)


fake_inv_mass_low = np.take(fake_inv_mass,fakeindexlow)
fake_weight_low = np.take(fake_weight,fakeindexlow)
fake_dilep_mass_low = np.take(fake_dilep_mass,fakeindexlow)
fake_electron_n_low = np.take(fake_electron_n,fakeindexlow)
fake_muon_n_low = np.take(fake_muon_n,fakeindexlow)
fake_total_charge_low = np.take(fake_total_charge,fakeindexlow)
fake_jet_n_low = np.take(fake_jet_n,fakeindexlow)
fake_bjet_n_low = np.take(fake_bjet_n,fakeindexlow)

fake_electron_mt_low = np.take(fake_electron_mt,fakeindexlow)
fake_muon_mt_low = np.take(fake_muon_mt,fakeindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(fake_electron_mt):

    array = np.concatenate((fake_electron_mt[n],fake_muon_mt[n]))
    array = [array]

    if n == 1:
        temp = np.concatenate((oldarray,array),axis=0)
    if n > 1:
        temp = np.concatenate((temp,array),axis=0)
    

    oldarray = array

    n = n+1

temp = np.transpose(temp)
temp1 = temp[0]
temp2 = temp[1]
temp3 = temp[2]
temp4 = temp[3]

fake_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
fake_total_mt_weight = np.concatenate((fake_weight,fake_weight,fake_weight,fake_weight))

n = 0
temp = np.empty((4,0))
while n < len(fake_electron_mt_high):

    array = np.concatenate((fake_electron_mt_high[n],fake_muon_mt_high[n]))
    array = [array]

    if n == 1:
        temp = np.concatenate((oldarray,array),axis=0)
    if n > 1:
        temp = np.concatenate((temp,array),axis=0)
    

    oldarray = array

    n = n+1

temp = np.transpose(temp)
temp1 = temp[0]
temp2 = temp[1]
temp3 = temp[2]
temp4 = temp[3]

fake_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
fake_total_mt_weight_high = np.concatenate((fake_weight_high,fake_weight_high,fake_weight_high,fake_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(fake_electron_mt_low):

    array = np.concatenate((fake_electron_mt_low[n],fake_muon_mt_low[n]))
    array = [array]

    if n == 1:
        temp = np.concatenate((oldarray,array),axis=0)
    if n > 1:
        temp = np.concatenate((temp,array),axis=0)
    

    oldarray = array

    n = n+1

temp = np.transpose(temp)
temp1 = temp[0]
temp2 = temp[1]
temp3 = temp[2]
temp4 = temp[3]

fake_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
fake_total_mt_weight_low = np.concatenate((fake_weight_low,fake_weight_low,fake_weight_low,fake_weight_low))

#get only emmm or eeem end states

fakeindexm3 = np.where(fake_electron_n == 1)
fakeindexe3 = np.where(fake_electron_n == 3)
fakeindexm3 = fakeindexm3[0]
fakeindexe3 = fakeindexe3[0]
fakeindexem3 = np.concatenate((fakeindexm3,fakeindexe3))
fakeindexem3 = np.sort(fakeindexem3)

fakeindexhighm3 = np.where(fake_electron_n_high == 1)
fakeindexhighe3 = np.where(fake_electron_n_high == 3)
fakeindexhighm3 = fakeindexhighm3[0]
fakeindexhighe3 = fakeindexhighe3[0]
fakeindexhighem3 = np.concatenate((fakeindexhighm3,fakeindexhighe3))
fakeindexhighem3 = np.sort(fakeindexhighem3)

fakeindexlowm3 = np.where(fake_electron_n_low == 1)
fakeindexlowe3 = np.where(fake_electron_n_low == 3)
fakeindexlowm3 = fakeindexlowm3[0]
fakeindexlowe3 = fakeindexlowe3[0]
fakeindexlowem3 = np.concatenate((fakeindexlowm3,fakeindexlowe3))
fakeindexlowem3 = np.sort(fakeindexlowem3)

fake_inv_mass_em3 = np.take(fake_inv_mass,fakeindexem3)
fake_met_em3 = np.take(fake_met,fakeindexem3)
fake_weight_em3 = np.take(fake_weight,fakeindexem3)
fake_dilep_mass_em3 = np.take(fake_dilep_mass,fakeindexem3)
fake_total_charge_em3 = np.take(fake_total_charge,fakeindexem3)
fake_jet_n_em3 = np.take(fake_jet_n,fakeindexem3)
fake_bjet_n_em3 = np.take(fake_bjet_n,fakeindexem3)

fake_electron_mt_em3 = np.take(fake_electron_mt,fakeindexem3)
fake_muon_mt_em3 = np.take(fake_muon_mt,fakeindexem3)

fake_inv_mass_high_em3 = np.take(fake_inv_mass_high,fakeindexhighem3)
fake_weight_high_em3 = np.take(fake_weight_high,fakeindexhighem3)
fake_dilep_mass_high_em3 = np.take(fake_dilep_mass_high,fakeindexhighem3)
fake_total_charge_high_em3 = np.take(fake_total_charge_high,fakeindexhighem3)
fake_jet_n_high_em3 = np.take(fake_jet_n_high,fakeindexhighem3)
fake_bjet_n_high_em3 = np.take(fake_bjet_n_high,fakeindexhighem3)

fake_electron_mt_high_em3 = np.take(fake_electron_mt_high,fakeindexhighem3)
fake_muon_mt_high_em3 = np.take(fake_muon_mt_high,fakeindexhighem3)

fake_inv_mass_low_em3 = np.take(fake_inv_mass_low,fakeindexlowem3)
fake_weight_low_em3 = np.take(fake_weight_low,fakeindexlowem3)
fake_dilep_mass_low_em3 = np.take(fake_dilep_mass_low,fakeindexlowem3)
fake_total_charge_low_em3 = np.take(fake_total_charge_low,fakeindexlowem3)
fake_jet_n_low_em3 = np.take(fake_jet_n_low,fakeindexlowem3)
fake_bjet_n_low_em3 = np.take(fake_bjet_n_low,fakeindexlowem3)

fake_electron_mt_low_em3 = np.take(fake_electron_mt_low,fakeindexlowem3)
fake_muon_mt_low_em3 = np.take(fake_muon_mt_low,fakeindexlowem3)

n = 0
temp = np.empty(0)
while n < len(fake_electron_mt_em3):

    array1 = fake_electron_mt_em3[n]
    array2 = fake_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

fake_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(fake_electron_mt_low_em3):

    array1 = fake_electron_mt_low_em3[n]
    array2 = fake_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

fake_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(fake_electron_mt_high_em3):

    array1 = fake_electron_mt_high_em3[n]
    array2 = fake_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

fake_single_mt_high = temp

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(fake_dilep_mass_em3):

    array = fake_dilep_mass_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

fake_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
fake_weight_dilep_em3 = np.concatenate((fake_weight_em3,fake_weight_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(fake_dilep_mass_high_em3):

    array = fake_dilep_mass_high_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

fake_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
fake_weight_dilep_high_em3 = np.concatenate((fake_weight_high_em3,fake_weight_high_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(fake_dilep_mass_low_em3):

    array = fake_dilep_mass_low_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

fake_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
fake_weight_dilep_low_em3 = np.concatenate((fake_weight_low_em3,fake_weight_low_em3))


#get only eemm end states

fakeindexem2 = np.where(fake_electron_n == 2)
fakeindexem2 = fakeindexem2[0]

fakeindexhighem2 = np.where(fake_electron_n_high == 2)
fakeindexhighem2 = fakeindexhighem2[0]

fakeindexlowem2 = np.where(fake_electron_n_low == 2)
fakeindexlowem2 = fakeindexlowem2[0]


fake_inv_mass_em2 = np.take(fake_inv_mass,fakeindexem2)
fake_met_em2 = np.take(fake_met,fakeindexem2)
fake_weight_em2 = np.take(fake_weight,fakeindexem2)
#fake_dilep_mass_em2 = np.take(fake_dilep_mass,fakeindexem2)
fake_total_charge_em2 = np.take(fake_total_charge,fakeindexem2)
fake_jet_n_em2 = np.take(fake_jet_n,fakeindexem2)
fake_bjet_n_em2 = np.take(fake_bjet_n,fakeindexem2)

fake_electron_mt_em2 = np.take(fake_electron_mt,fakeindexem2)
fake_muon_mt_em2 = np.take(fake_muon_mt,fakeindexem2)

fake_inv_mass_high_em2 = np.take(fake_inv_mass_high,fakeindexhighem2)
fake_weight_high_em2 = np.take(fake_weight_high,fakeindexhighem2)
#fake_dilep_mass_high_em2 = np.take(fake_dilep_mass_high,fakeindexhighem2)
fake_total_charge_high_em2 = np.take(fake_total_charge_high,fakeindexhighem2)
fake_jet_n_high_em2 = np.take(fake_jet_n_high,fakeindexhighem2)
fake_bjet_n_high_em2 = np.take(fake_bjet_n_high,fakeindexhighem2)

fake_electron_mt_high_em2 = np.take(fake_electron_mt_high,fakeindexhighem2)
fake_muon_mt_high_em2 = np.take(fake_muon_mt_high,fakeindexhighem2)

fake_inv_mass_low_em2 = np.take(fake_inv_mass_low,fakeindexlowem2)
fake_weight_low_em2 = np.take(fake_weight_low,fakeindexlowem2)
#fake_dilep_mass_low_em2 = np.take(fake_dilep_mass_low,fakeindexlowem2)
fake_total_charge_low_em2 = np.take(fake_total_charge_low,fakeindexlowem2)
fake_jet_n_low_em2 = np.take(fake_jet_n_low,fakeindexlowem2)
fake_bjet_n_low_em2 = np.take(fake_bjet_n_low,fakeindexlowem2)


#only states with 0 jets

fake_jet_0_index = np.where(fake_jet_n == 0)
fake_jet_0_index = fake_jet_0_index[0]
fake_jet_0_index_high = np.where(fake_jet_n_high == 0)
fake_jet_0_index_high = fake_jet_0_index_high[0]
fake_jet_0_index_low = np.where(fake_jet_n_low == 0)
fake_jet_0_index_low = fake_jet_0_index_low[0]


fake_inv_mass_0jet = np.take(fake_inv_mass,fake_jet_0_index)
fake_met_0jet = np.take(fake_met,fake_jet_0_index)
fake_weight_0jet = np.take(fake_weight,fake_jet_0_index)
fake_total_charge_0jet = np.take(fake_total_charge,fake_jet_0_index)


fake_inv_mass_high_0jet = np.take(fake_inv_mass_high,fake_jet_0_index_high)
fake_weight_high_0jet = np.take(fake_weight_high,fake_jet_0_index_high)
fake_total_charge_high_0jet = np.take(fake_total_charge_high,fake_jet_0_index_high)

fake_inv_mass_low_0jet = np.take(fake_inv_mass_low,fake_jet_0_index_low)
fake_weight_low_0jet = np.take(fake_weight_low,fake_jet_0_index_low)
fake_total_charge_low_0jet = np.take(fake_total_charge_low,fake_jet_0_index_low)

#only states where eeem or emmm and 0 bjets

fake_bjet_0em3_index = np.where(fake_bjet_n_em3 == 0)
fake_bjet_0em3_index = fake_bjet_0em3_index[0]
fake_bjet_0em3_index_high = np.where(fake_bjet_n_high_em3 == 0)
fake_bjet_0em3_index_high = fake_bjet_0em3_index_high[0]
fake_bjet_0em3_index_low = np.where(fake_bjet_n_low_em3 == 0)
fake_bjet_0em3_index_low = fake_bjet_0em3_index_low[0]


fake_inv_mass_0em3 = np.take(fake_inv_mass_em3,fake_bjet_0em3_index)
fake_met_0em3 = np.take(fake_met_em3,fake_bjet_0em3_index)
fake_weight_0em3 = np.take(fake_weight_em3,fake_bjet_0em3_index)
fake_dilep_mass_0em3 = np.take(fake_dilep_mass_em3,fake_bjet_0em3_index)
fake_total_charge_0em3 = np.take(fake_total_charge_em3,fake_bjet_0em3_index)
fake_jet_n_0em3 = np.take(fake_jet_n_em3,fake_bjet_0em3_index)

fake_inv_mass_high_0em3 = np.take(fake_inv_mass_high_em3,fake_bjet_0em3_index_high)
fake_weight_high_0em3 = np.take(fake_weight_high_em3,fake_bjet_0em3_index_high)
fake_dilep_mass_high_0em3 = np.take(fake_dilep_mass_high_em3,fake_bjet_0em3_index_high)
fake_total_charge_high_0em3 = np.take(fake_total_charge_high_em3,fake_bjet_0em3_index_high)
fake_jet_n_high_0em3 = np.take(fake_jet_n_high_em3,fake_bjet_0em3_index_high)

fake_inv_mass_low_0em3 = np.take(fake_inv_mass_low_em3,fake_bjet_0em3_index_low)
fake_weight_low_0em3 = np.take(fake_weight_low_em3,fake_bjet_0em3_index_low)
fake_dilep_mass_low_0em3 = np.take(fake_dilep_mass_low_em3,fake_bjet_0em3_index_low)
fake_total_charge_low_0em3 = np.take(fake_total_charge_low_em3,fake_bjet_0em3_index_low)
fake_jet_n_low_0em3 = np.take(fake_jet_n_low_em3,fake_bjet_0em3_index_low)

fake_electron_mt_0em3 = np.take(fake_electron_mt_em3,fake_bjet_0em3_index)
fake_muon_mt_0em3 = np.take(fake_muon_mt_em3,fake_bjet_0em3_index)

fake_electron_mt_high_0em3 = np.take(fake_electron_mt_high_em3,fake_bjet_0em3_index_high)
fake_muon_mt_high_0em3 = np.take(fake_muon_mt_high_em3,fake_bjet_0em3_index_high)

fake_electron_mt_low_0em3 = np.take(fake_electron_mt_low_em3,fake_bjet_0em3_index_low)
fake_muon_mt_low_0em3 = np.take(fake_muon_mt_low_em3,fake_bjet_0em3_index_low)

fake_single_mt_0b = np.take(fake_single_mt,fake_bjet_0em3_index)
fake_single_mt_high_0b = np.take(fake_single_mt_high,fake_bjet_0em3_index_high)
fake_single_mt_low_0b = np.take(fake_single_mt_low,fake_bjet_0em3_index_low)

#division based on total charge

fake_charge0_index = np.where(fake_total_charge == 0)
fake_charge0_index = fake_charge0_index[0]
fake_charge0_index_high = np.where(fake_total_charge_high == 0)
fake_charge0_index_high = fake_charge0_index_high[0]
fake_charge0_index_low = np.where(fake_total_charge_low == 0)
fake_charge0_index_low = fake_charge0_index_low[0]

fake_inv_mass_charge0 = np.take(fake_inv_mass,fake_charge0_index)
fake_met_charge0 = np.take(fake_met,fake_charge0_index)
fake_weight_charge0 = np.take(fake_weight,fake_charge0_index)
fake_jet_n_charge0 = np.take(fake_jet_n,fake_charge0_index)
fake_electron_mt_charge0 = np.take(fake_electron_mt,fake_charge0_index)
fake_muon_mt_charge0 = np.take(fake_muon_mt,fake_charge0_index)

fake_inv_mass_charge0_high = np.take(fake_inv_mass_high,fake_charge0_index_high)
fake_weight_charge0_high = np.take(fake_weight_high,fake_charge0_index_high)
fake_jet_n_charge0_high = np.take(fake_jet_n_high,fake_charge0_index_high)
fake_electron_mt_charge0_high = np.take(fake_electron_mt_high,fake_charge0_index_high)
fake_muon_mt_charge0_high = np.take(fake_muon_mt_high,fake_charge0_index_high)

fake_inv_mass_charge0_low = np.take(fake_inv_mass_low,fake_charge0_index_low)
fake_weight_charge0_low = np.take(fake_weight_low,fake_charge0_index_low)
fake_jet_n_charge0_low = np.take(fake_jet_n_low,fake_charge0_index_low)
fake_electron_mt_charge0_low = np.take(fake_electron_mt_low,fake_charge0_index_low)
fake_muon_mt_charge0_low = np.take(fake_muon_mt_low,fake_charge0_index_low)


fake_charge2_index = np.where(fake_total_charge == 2)
fake_charge2_index = fake_charge2_index[0]
fake_charge2_index_high = np.where(fake_total_charge_high == 2)
fake_charge2_index_high = fake_charge2_index_high[0]
fake_charge2_index_low = np.where(fake_total_charge_low == 2)
fake_charge2_index_low = fake_charge2_index_low[0]

fake_inv_mass_charge2 = np.take(fake_inv_mass,fake_charge2_index)
fake_met_charge2 = np.take(fake_met,fake_charge2_index)
fake_weight_charge2 = np.take(fake_weight,fake_charge2_index)
fake_jet_n_charge2 = np.take(fake_jet_n,fake_charge2_index)
fake_electron_mt_charge2 = np.take(fake_electron_mt,fake_charge2_index)
fake_muon_mt_charge2 = np.take(fake_muon_mt,fake_charge2_index)

fake_inv_mass_charge2_high = np.take(fake_inv_mass_high,fake_charge2_index_high)
fake_weight_charge2_high = np.take(fake_weight_high,fake_charge2_index_high)
fake_jet_n_charge2_high = np.take(fake_jet_n_high,fake_charge2_index_high)
fake_electron_mt_charge2_high = np.take(fake_electron_mt_high,fake_charge2_index_high)
fake_muon_mt_charge2_high = np.take(fake_muon_mt_high,fake_charge2_index_high)

fake_inv_mass_charge2_low = np.take(fake_inv_mass_low,fake_charge2_index_low)
fake_weight_charge2_low = np.take(fake_weight_low,fake_charge2_index_low)
fake_jet_n_charge2_low = np.take(fake_jet_n_low,fake_charge2_index_low)
fake_electron_mt_charge2_low = np.take(fake_electron_mt_low,fake_charge2_index_low)
fake_muon_mt_charge2_low = np.take(fake_muon_mt_low,fake_charge2_index_low)


fake_charge2min_index = np.where(fake_total_charge == -2)
fake_charge2min_index = fake_charge2min_index[0]
fake_charge2min_index_high = np.where(fake_total_charge_high == -2)
fake_charge2min_index_high = fake_charge2min_index_high[0]
fake_charge2min_index_low = np.where(fake_total_charge_low == -2)
fake_charge2min_index_low = fake_charge2min_index_low[0]

fake_inv_mass_charge2min = np.take(fake_inv_mass,fake_charge2min_index)
fake_met_charge2min = np.take(fake_met,fake_charge2min_index)
fake_weight_charge2min = np.take(fake_weight,fake_charge2min_index)
fake_jet_n_charge2min = np.take(fake_jet_n,fake_charge2min_index)
fake_electron_mt_charge2min = np.take(fake_electron_mt,fake_charge2min_index)
fake_muon_mt_charge2min = np.take(fake_muon_mt,fake_charge2min_index)

fake_inv_mass_charge2min_high = np.take(fake_inv_mass_high,fake_charge2min_index_high)
fake_weight_charge2min_high = np.take(fake_weight_high,fake_charge2min_index_high)
fake_jet_n_charge2min_high = np.take(fake_jet_n_high,fake_charge2min_index_high)
fake_electron_mt_charge2min_high = np.take(fake_electron_mt_high,fake_charge2min_index_high)
fake_muon_mt_charge2min_high = np.take(fake_muon_mt_high,fake_charge2min_index_high)

fake_inv_mass_charge2min_low = np.take(fake_inv_mass_low,fake_charge2min_index_low)
fake_weight_charge2min_low = np.take(fake_weight_low,fake_charge2min_index_low)
fake_jet_n_charge2min_low = np.take(fake_jet_n_low,fake_charge2min_index_low)
fake_electron_mt_charge2min_low = np.take(fake_electron_mt_low,fake_charge2min_index_low)
fake_muon_mt_charge2min_low = np.take(fake_muon_mt_low,fake_charge2min_index_low)

# charge division of em3 states

fake_charge0_index_em3 = np.where(fake_total_charge_em3 == 0)
fake_charge0_index_em3 = fake_charge0_index_em3[0]
fake_charge0_index_high_em3 = np.where(fake_total_charge_high_em3 == 0)
fake_charge0_index_high_em3 = fake_charge0_index_high_em3[0]
fake_charge0_index_low_em3 = np.where(fake_total_charge_low_em3 == 0)
fake_charge0_index_low_em3 = fake_charge0_index_low_em3[0]

fake_inv_mass_charge0_em3 = np.take(fake_inv_mass_em3,fake_charge0_index_em3)
fake_met_charge0_em3 = np.take(fake_met_em3,fake_charge0_index_em3)
fake_weight_charge0_em3 = np.take(fake_weight_em3,fake_charge0_index_em3)
fake_jet_n_charge0_em3 = np.take(fake_jet_n_em3,fake_charge0_index_em3)
fake_single_mt_charge0_em3 = np.take(fake_single_mt,fake_charge0_index_em3)

fake_inv_mass_charge0_high_em3 = np.take(fake_inv_mass_high_em3,fake_charge0_index_high_em3)
fake_weight_charge0_high_em3 = np.take(fake_weight_high_em3,fake_charge0_index_high_em3)
fake_jet_n_charge0_high_em3 = np.take(fake_jet_n_high_em3,fake_charge0_index_high_em3)
fake_single_mt_charge0_high_em3 = np.take(fake_single_mt_high,fake_charge0_index_high_em3)

fake_inv_mass_charge0_low_em3 = np.take(fake_inv_mass_low_em3,fake_charge0_index_low_em3)
fake_weight_charge0_low_em3 = np.take(fake_weight_low_em3,fake_charge0_index_low_em3)
fake_jet_n_charge0_low_em3 = np.take(fake_jet_n_low_em3,fake_charge0_index_low_em3)
fake_single_mt_charge0_low_em3 = np.take(fake_single_mt_low,fake_charge0_index_low_em3)


fake_charge2_index_em3 = np.where(fake_total_charge_em3 == 2)
fake_charge2_index_em3 = fake_charge2_index_em3[0]
fake_charge2_index_high_em3 = np.where(fake_total_charge_high_em3 == 2)
fake_charge2_index_high_em3 = fake_charge2_index_high_em3[0]
fake_charge2_index_low_em3 = np.where(fake_total_charge_low_em3 == 2)
fake_charge2_index_low_em3 = fake_charge2_index_low_em3[0]

fake_inv_mass_charge2_em3 = np.take(fake_inv_mass_em3,fake_charge2_index_em3)
fake_met_charge2_em3 = np.take(fake_met_em3,fake_charge2_index_em3)
fake_weight_charge2_em3 = np.take(fake_weight_em3,fake_charge2_index_em3)
fake_jet_n_charge2_em3 = np.take(fake_jet_n_em3,fake_charge2_index_em3)
fake_single_mt_charge2_em3 = np.take(fake_single_mt,fake_charge2_index_em3)

fake_inv_mass_charge2_high_em3 = np.take(fake_inv_mass_high_em3,fake_charge2_index_high_em3)
fake_weight_charge2_high_em3 = np.take(fake_weight_high_em3,fake_charge2_index_high_em3)
fake_jet_n_charge2_high_em3 = np.take(fake_jet_n_high_em3,fake_charge2_index_high_em3)
fake_single_mt_charge2_high_em3 = np.take(fake_single_mt_high,fake_charge2_index_high_em3)

fake_inv_mass_charge2_low_em3 = np.take(fake_inv_mass_low_em3,fake_charge2_index_low_em3)
fake_weight_charge2_low_em3 = np.take(fake_weight_low_em3,fake_charge2_index_low_em3)
fake_jet_n_charge2_low_em3 = np.take(fake_jet_n_low_em3,fake_charge2_index_low_em3)
fake_single_mt_charge2_low_em3 = np.take(fake_single_mt_low,fake_charge2_index_low_em3)


fake_charge2min_index_em3 = np.where(fake_total_charge_em3 == -2)
fake_charge2min_index_em3 = fake_charge2min_index_em3[0]
fake_charge2min_index_high_em3 = np.where(fake_total_charge_high_em3 == -2)
fake_charge2min_index_high_em3 = fake_charge2min_index_high_em3[0]
fake_charge2min_index_low_em3 = np.where(fake_total_charge_low_em3 == -2)
fake_charge2min_index_low_em3 = fake_charge2min_index_low_em3[0]

fake_inv_mass_charge2min_em3 = np.take(fake_inv_mass_em3,fake_charge2min_index_em3)
fake_met_charge2min_em3 = np.take(fake_met_em3,fake_charge2min_index_em3)
fake_weight_charge2min_em3 = np.take(fake_weight_em3,fake_charge2min_index_em3)
fake_jet_n_charge2min_em3 = np.take(fake_jet_n_em3,fake_charge2min_index_em3)
fake_single_mt_charge2min_em3 = np.take(fake_single_mt,fake_charge2min_index_em3)

fake_inv_mass_charge2min_high_em3 = np.take(fake_inv_mass_high_em3,fake_charge2min_index_high_em3)
fake_weight_charge2min_high_em3 = np.take(fake_weight_high_em3,fake_charge2min_index_high_em3)
fake_jet_n_charge2min_high_em3 = np.take(fake_jet_n_high_em3,fake_charge2min_index_high_em3)
fake_single_mt_charge2min_high_em3 = np.take(fake_single_mt_high,fake_charge2min_index_high_em3)

fake_inv_mass_charge2min_low_em3 = np.take(fake_inv_mass_low_em3,fake_charge2min_index_low_em3)
fake_weight_charge2min_low_em3 = np.take(fake_weight_low_em3,fake_charge2min_index_low_em3)
fake_jet_n_charge2min_low_em3 = np.take(fake_jet_n_low_em3,fake_charge2min_index_low_em3)
fake_single_mt_charge2min_low_em3 = np.take(fake_single_mt_low,fake_charge2min_index_low_em3)


#higgs relevant selection

n=0
index = np.empty(0)
while n < len(fake_electron_charge):

    temp1 = fake_electron_charge[n]
    temp2 = fake_muon_charge[n]

    num = fake_electron_n[n]

    if num == 0:
        index = np.concatenate((index,[int(n)]))
    if num == 2:
        test1 = temp1[0] + temp1[1]
        test2 = temp2[0] + temp2[1]
        if test1 == 2:
            index = np.concatenate((index,[int(n)]))
        elif test1 == -2:
            index = np.concatenate((index,[int(n)]))
        elif test2 == 2:
            index = np.concatenate((index,[int(n)]))
        elif test2 == -2:
            index = np.concatenate((index,[int(n)]))
            
    if num == 4:
        index = np.concatenate((index,[int(n)]))


    n = n+1


fake_higgs_index = index.astype('int64')

fake_higgs_inv_mass = np.take(fake_inv_mass,fake_higgs_index)
fake_higgs_met = np.take(fake_met,fake_higgs_index)
fake_higgs_weight = np.take(fake_weight,fake_higgs_index)
#fake_higgs_dilep_mass = np.take(fake_dilep_mass,fake_higgs_index)
fake_higgs_electron_n = np.take(fake_electron_n,fake_higgs_index)
fake_higgs_muon_n = np.take(fake_muon_n,fake_higgs_index)
fake_higgs_electron_charge = np.take(fake_electron_charge,fake_higgs_index)
fake_higgs_muon_charge = np.take(fake_muon_charge,fake_higgs_index)
fake_higgs_jet_n = np.take(fake_jet_n,fake_higgs_index)
fake_higgs_jet_btag = np.take(fake_jet_btag,fake_higgs_index)
fake_higgs_electron_mt = np.take(fake_electron_mt,fake_higgs_index)
fake_higgs_muon_mt = np.take(fake_muon_mt,fake_higgs_index)
