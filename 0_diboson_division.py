#inv_mass_cut

#imdibosonindex = np.where(diboson_inv_mass < 400)
#imdibosonindex = imdibosonindex[0]

#diboson_inv_mass = np.take(diboson_inv_mass,imdibosonindex)
#diboson_met = np.take(diboson_met,imdibosonindex)
#diboson_weight = np.take(diboson_weight,imdibosonindex)
#diboson_dilep_mass = np.take(diboson_dilep_mass,imdibosonindex)
#diboson_electron_n = np.take(diboson_electron_n,imdibosonindex)
#diboson_muon_n = np.take(diboson_muon_n,imdibosonindex)
#diboson_electron_charge = np.take(diboson_electron_charge,imdibosonindex)
#diboson_muon_charge = np.take(diboson_muon_charge,imdibosonindex)
#diboson_jet_n = np.take(diboson_jet_n,imdibosonindex)
#diboson_jet_btag = np.take(diboson_jet_btag,imdibosonindex)
#diboson_muononz = np.take(diboson_muononz,imdibosonindex)
#diboson_electrononz = np.take(diboson_electrononz,imdibosonindex)
#diboson_electron_mt = np.take(diboson_electron_mt,imdibosonindex)
#diboson_muon_mt = np.take(diboson_muon_mt,imdibosonindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(diboson_electrononz):

    array = np.concatenate((diboson_electrononz[n],diboson_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

dibosonindex = index.astype('int64')

diboson_inv_mass = np.take(diboson_inv_mass,dibosonindex)
diboson_met = np.take(diboson_met,dibosonindex)
diboson_weight = np.take(diboson_weight,dibosonindex)
diboson_dilep_mass = np.take(diboson_dilep_mass,dibosonindex)
diboson_electron_n = np.take(diboson_electron_n,dibosonindex)
diboson_muon_n = np.take(diboson_muon_n,dibosonindex)
diboson_electron_charge = np.take(diboson_electron_charge,dibosonindex)
diboson_muon_charge = np.take(diboson_muon_charge,dibosonindex)
diboson_jet_n = np.take(diboson_jet_n,dibosonindex)
diboson_jet_btag = np.take(diboson_jet_btag,dibosonindex)
diboson_electron_mt = np.take(diboson_electron_mt,dibosonindex)
diboson_muon_mt = np.take(diboson_muon_mt,dibosonindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(diboson_jet_btag):

    array = diboson_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

diboson_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(diboson_electron_charge):

    temp1 = diboson_electron_charge[n]
    temp2 = diboson_muon_charge[n]

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

diboson_total_charge = temp


#add high or low missing transverse energy groups

dibosonindexlow = np.where(diboson_met < 50)
dibosonindexlow = dibosonindexlow[0]
dibosonindexhigh = np.where(diboson_met > 50)
dibosonindexhigh = dibosonindexhigh[0]


diboson_inv_mass_high = np.take(diboson_inv_mass,dibosonindexhigh)
diboson_weight_high = np.take(diboson_weight,dibosonindexhigh)
diboson_dilep_mass_high = np.take(diboson_dilep_mass,dibosonindexhigh)
diboson_electron_n_high = np.take(diboson_electron_n,dibosonindexhigh)
diboson_muon_n_high = np.take(diboson_muon_n,dibosonindexhigh)
diboson_total_charge_high = np.take(diboson_total_charge,dibosonindexhigh)
diboson_jet_n_high = np.take(diboson_jet_n,dibosonindexhigh)
diboson_bjet_n_high = np.take(diboson_bjet_n,dibosonindexhigh)

diboson_electron_mt_high = np.take(diboson_electron_mt,dibosonindexhigh)
diboson_muon_mt_high = np.take(diboson_muon_mt,dibosonindexhigh)


diboson_inv_mass_low = np.take(diboson_inv_mass,dibosonindexlow)
diboson_weight_low = np.take(diboson_weight,dibosonindexlow)
diboson_dilep_mass_low = np.take(diboson_dilep_mass,dibosonindexlow)
diboson_electron_n_low = np.take(diboson_electron_n,dibosonindexlow)
diboson_muon_n_low = np.take(diboson_muon_n,dibosonindexlow)
diboson_total_charge_low = np.take(diboson_total_charge,dibosonindexlow)
diboson_jet_n_low = np.take(diboson_jet_n,dibosonindexlow)
diboson_bjet_n_low = np.take(diboson_bjet_n,dibosonindexlow)

diboson_electron_mt_low = np.take(diboson_electron_mt,dibosonindexlow)
diboson_muon_mt_low = np.take(diboson_muon_mt,dibosonindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(diboson_electron_mt):

    array = np.concatenate((diboson_electron_mt[n],diboson_muon_mt[n]))
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

diboson_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
diboson_total_mt_weight = np.concatenate((diboson_weight,diboson_weight,diboson_weight,diboson_weight))

n = 0
temp = np.empty((4,0))
while n < len(diboson_electron_mt_high):

    array = np.concatenate((diboson_electron_mt_high[n],diboson_muon_mt_high[n]))
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

diboson_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
diboson_total_mt_weight_high = np.concatenate((diboson_weight_high,diboson_weight_high,diboson_weight_high,diboson_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(diboson_electron_mt_low):

    array = np.concatenate((diboson_electron_mt_low[n],diboson_muon_mt_low[n]))
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

diboson_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
diboson_total_mt_weight_low = np.concatenate((diboson_weight_low,diboson_weight_low,diboson_weight_low,diboson_weight_low))

#get only emmm or eeem end states

dibosonindexm3 = np.where(diboson_electron_n == 1)
dibosonindexe3 = np.where(diboson_electron_n == 3)
dibosonindexm3 = dibosonindexm3[0]
dibosonindexe3 = dibosonindexe3[0]
dibosonindexem3 = np.concatenate((dibosonindexm3,dibosonindexe3))
dibosonindexem3 = np.sort(dibosonindexem3)

dibosonindexhighm3 = np.where(diboson_electron_n_high == 1)
dibosonindexhighe3 = np.where(diboson_electron_n_high == 3)
dibosonindexhighm3 = dibosonindexhighm3[0]
dibosonindexhighe3 = dibosonindexhighe3[0]
dibosonindexhighem3 = np.concatenate((dibosonindexhighm3,dibosonindexhighe3))
dibosonindexhighem3 = np.sort(dibosonindexhighem3)

dibosonindexlowm3 = np.where(diboson_electron_n_low == 1)
dibosonindexlowe3 = np.where(diboson_electron_n_low == 3)
dibosonindexlowm3 = dibosonindexlowm3[0]
dibosonindexlowe3 = dibosonindexlowe3[0]
dibosonindexlowem3 = np.concatenate((dibosonindexlowm3,dibosonindexlowe3))
dibosonindexlowem3 = np.sort(dibosonindexlowem3)

diboson_inv_mass_em3 = np.take(diboson_inv_mass,dibosonindexem3)
diboson_met_em3 = np.take(diboson_met,dibosonindexem3)
diboson_weight_em3 = np.take(diboson_weight,dibosonindexem3)
diboson_dilep_mass_em3 = np.take(diboson_dilep_mass,dibosonindexem3)
diboson_total_charge_em3 = np.take(diboson_total_charge,dibosonindexem3)
diboson_jet_n_em3 = np.take(diboson_jet_n,dibosonindexem3)
diboson_bjet_n_em3 = np.take(diboson_bjet_n,dibosonindexem3)

diboson_electron_mt_em3 = np.take(diboson_electron_mt,dibosonindexem3)
diboson_muon_mt_em3 = np.take(diboson_muon_mt,dibosonindexem3)

diboson_inv_mass_high_em3 = np.take(diboson_inv_mass_high,dibosonindexhighem3)
diboson_weight_high_em3 = np.take(diboson_weight_high,dibosonindexhighem3)
diboson_dilep_mass_high_em3 = np.take(diboson_dilep_mass_high,dibosonindexhighem3)
diboson_total_charge_high_em3 = np.take(diboson_total_charge_high,dibosonindexhighem3)
diboson_jet_n_high_em3 = np.take(diboson_jet_n_high,dibosonindexhighem3)
diboson_bjet_n_high_em3 = np.take(diboson_bjet_n_high,dibosonindexhighem3)

diboson_electron_mt_high_em3 = np.take(diboson_electron_mt_high,dibosonindexhighem3)
diboson_muon_mt_high_em3 = np.take(diboson_muon_mt_high,dibosonindexhighem3)

diboson_inv_mass_low_em3 = np.take(diboson_inv_mass_low,dibosonindexlowem3)
diboson_weight_low_em3 = np.take(diboson_weight_low,dibosonindexlowem3)
diboson_dilep_mass_low_em3 = np.take(diboson_dilep_mass_low,dibosonindexlowem3)
diboson_total_charge_low_em3 = np.take(diboson_total_charge_low,dibosonindexlowem3)
diboson_jet_n_low_em3 = np.take(diboson_jet_n_low,dibosonindexlowem3)
diboson_bjet_n_low_em3 = np.take(diboson_bjet_n_low,dibosonindexlowem3)

diboson_electron_mt_low_em3 = np.take(diboson_electron_mt_low,dibosonindexlowem3)
diboson_muon_mt_low_em3 = np.take(diboson_muon_mt_low,dibosonindexlowem3)

n = 0
temp = np.empty(0)
while n < len(diboson_electron_mt_em3):

    array1 = diboson_electron_mt_em3[n]
    array2 = diboson_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

diboson_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(diboson_electron_mt_low_em3):

    array1 = diboson_electron_mt_low_em3[n]
    array2 = diboson_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

diboson_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(diboson_electron_mt_high_em3):

    array1 = diboson_electron_mt_high_em3[n]
    array2 = diboson_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

diboson_single_mt_high = temp

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(diboson_dilep_mass_em3):

    array = diboson_dilep_mass_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

diboson_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
diboson_weight_dilep_em3 = np.concatenate((diboson_weight_em3,diboson_weight_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(diboson_dilep_mass_high_em3):

    array = diboson_dilep_mass_high_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

diboson_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
diboson_weight_dilep_high_em3 = np.concatenate((diboson_weight_high_em3,diboson_weight_high_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(diboson_dilep_mass_low_em3):

    array = diboson_dilep_mass_low_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

diboson_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
diboson_weight_dilep_low_em3 = np.concatenate((diboson_weight_low_em3,diboson_weight_low_em3))

#only states with 0 jets

diboson_jet_0_index = np.where(diboson_jet_n == 0)
diboson_jet_0_index = diboson_jet_0_index[0]
diboson_jet_0_index_high = np.where(diboson_jet_n_high == 0)
diboson_jet_0_index_high = diboson_jet_0_index_high[0]
diboson_jet_0_index_low = np.where(diboson_jet_n_low == 0)
diboson_jet_0_index_low = diboson_jet_0_index_low[0]


diboson_inv_mass_0jet = np.take(diboson_inv_mass,diboson_jet_0_index)
diboson_met_0jet = np.take(diboson_met,diboson_jet_0_index)
diboson_weight_0jet = np.take(diboson_weight,diboson_jet_0_index)
diboson_total_charge_0jet = np.take(diboson_total_charge,diboson_jet_0_index)


diboson_inv_mass_high_0jet = np.take(diboson_inv_mass_high,diboson_jet_0_index_high)
diboson_weight_high_0jet = np.take(diboson_weight_high,diboson_jet_0_index_high)
diboson_total_charge_high_0jet = np.take(diboson_total_charge_high,diboson_jet_0_index_high)

diboson_inv_mass_low_0jet = np.take(diboson_inv_mass_low,diboson_jet_0_index_low)
diboson_weight_low_0jet = np.take(diboson_weight_low,diboson_jet_0_index_low)
diboson_total_charge_low_0jet = np.take(diboson_total_charge_low,diboson_jet_0_index_low)

#only states where eeem or emmm and 0 bjets

diboson_bjet_0em3_index = np.where(diboson_bjet_n_em3 == 0)
diboson_bjet_0em3_index = diboson_bjet_0em3_index[0]
diboson_bjet_0em3_index_high = np.where(diboson_bjet_n_high_em3 == 0)
diboson_bjet_0em3_index_high = diboson_bjet_0em3_index_high[0]
diboson_bjet_0em3_index_low = np.where(diboson_bjet_n_low_em3 == 0)
diboson_bjet_0em3_index_low = diboson_bjet_0em3_index_low[0]


diboson_inv_mass_0em3 = np.take(diboson_inv_mass_em3,diboson_bjet_0em3_index)
diboson_met_0em3 = np.take(diboson_met_em3,diboson_bjet_0em3_index)
diboson_weight_0em3 = np.take(diboson_weight_em3,diboson_bjet_0em3_index)
diboson_dilep_mass_0em3 = np.take(diboson_dilep_mass_em3,diboson_bjet_0em3_index)
diboson_total_charge_0em3 = np.take(diboson_total_charge_em3,diboson_bjet_0em3_index)
diboson_jet_n_0em3 = np.take(diboson_jet_n_em3,diboson_bjet_0em3_index)

diboson_inv_mass_high_0em3 = np.take(diboson_inv_mass_high_em3,diboson_bjet_0em3_index_high)
diboson_weight_high_0em3 = np.take(diboson_weight_high_em3,diboson_bjet_0em3_index_high)
diboson_dilep_mass_high_0em3 = np.take(diboson_dilep_mass_high_em3,diboson_bjet_0em3_index_high)
diboson_total_charge_high_0em3 = np.take(diboson_total_charge_high_em3,diboson_bjet_0em3_index_high)
diboson_jet_n_high_0em3 = np.take(diboson_jet_n_high_em3,diboson_bjet_0em3_index_high)

diboson_inv_mass_low_0em3 = np.take(diboson_inv_mass_low_em3,diboson_bjet_0em3_index_low)
diboson_weight_low_0em3 = np.take(diboson_weight_low_em3,diboson_bjet_0em3_index_low)
diboson_dilep_mass_low_0em3 = np.take(diboson_dilep_mass_low_em3,diboson_bjet_0em3_index_low)
diboson_total_charge_low_0em3 = np.take(diboson_total_charge_low_em3,diboson_bjet_0em3_index_low)
diboson_jet_n_low_0em3 = np.take(diboson_jet_n_low_em3,diboson_bjet_0em3_index_low)

diboson_electron_mt_0em3 = np.take(diboson_electron_mt_em3,diboson_bjet_0em3_index)
diboson_muon_mt_0em3 = np.take(diboson_muon_mt_em3,diboson_bjet_0em3_index)

diboson_electron_mt_high_0em3 = np.take(diboson_electron_mt_high_em3,diboson_bjet_0em3_index_high)
diboson_muon_mt_high_0em3 = np.take(diboson_muon_mt_high_em3,diboson_bjet_0em3_index_high)

diboson_electron_mt_low_0em3 = np.take(diboson_electron_mt_low_em3,diboson_bjet_0em3_index_low)
diboson_muon_mt_low_0em3 = np.take(diboson_muon_mt_low_em3,diboson_bjet_0em3_index_low)

diboson_single_mt_0b = np.take(diboson_single_mt,diboson_bjet_0em3_index)
diboson_single_mt_high_0b = np.take(diboson_single_mt_high,diboson_bjet_0em3_index_high)
diboson_single_mt_low_0b = np.take(diboson_single_mt_low,diboson_bjet_0em3_index_low)

#division based on total charge

diboson_charge0_index = np.where(diboson_total_charge == 0)
diboson_charge0_index = diboson_charge0_index[0]
diboson_charge0_index_high = np.where(diboson_total_charge_high == 0)
diboson_charge0_index_high = diboson_charge0_index_high[0]
diboson_charge0_index_low = np.where(diboson_total_charge_low == 0)
diboson_charge0_index_low = diboson_charge0_index_low[0]

diboson_inv_mass_charge0 = np.take(diboson_inv_mass,diboson_charge0_index)
diboson_met_charge0 = np.take(diboson_met,diboson_charge0_index)
diboson_weight_charge0 = np.take(diboson_weight,diboson_charge0_index)
diboson_jet_n_charge0 = np.take(diboson_jet_n,diboson_charge0_index)
diboson_electron_mt_charge0 = np.take(diboson_electron_mt,diboson_charge0_index)
diboson_muon_mt_charge0 = np.take(diboson_muon_mt,diboson_charge0_index)

diboson_inv_mass_charge0_high = np.take(diboson_inv_mass_high,diboson_charge0_index_high)
diboson_weight_charge0_high = np.take(diboson_weight_high,diboson_charge0_index_high)
diboson_jet_n_charge0_high = np.take(diboson_jet_n_high,diboson_charge0_index_high)
diboson_electron_mt_charge0_high = np.take(diboson_electron_mt_high,diboson_charge0_index_high)
diboson_muon_mt_charge0_high = np.take(diboson_muon_mt_high,diboson_charge0_index_high)

diboson_inv_mass_charge0_low = np.take(diboson_inv_mass_low,diboson_charge0_index_low)
diboson_weight_charge0_low = np.take(diboson_weight_low,diboson_charge0_index_low)
diboson_jet_n_charge0_low = np.take(diboson_jet_n_low,diboson_charge0_index_low)
diboson_electron_mt_charge0_low = np.take(diboson_electron_mt_low,diboson_charge0_index_low)
diboson_muon_mt_charge0_low = np.take(diboson_muon_mt_low,diboson_charge0_index_low)


diboson_charge2_index = np.where(diboson_total_charge == 2)
diboson_charge2_index = diboson_charge2_index[0]
diboson_charge2_index_high = np.where(diboson_total_charge_high == 2)
diboson_charge2_index_high = diboson_charge2_index_high[0]
diboson_charge2_index_low = np.where(diboson_total_charge_low == 2)
diboson_charge2_index_low = diboson_charge2_index_low[0]

diboson_inv_mass_charge2 = np.take(diboson_inv_mass,diboson_charge2_index)
diboson_met_charge2 = np.take(diboson_met,diboson_charge2_index)
diboson_weight_charge2 = np.take(diboson_weight,diboson_charge2_index)
diboson_jet_n_charge2 = np.take(diboson_jet_n,diboson_charge2_index)
diboson_electron_mt_charge2 = np.take(diboson_electron_mt,diboson_charge2_index)
diboson_muon_mt_charge2 = np.take(diboson_muon_mt,diboson_charge2_index)

diboson_inv_mass_charge2_high = np.take(diboson_inv_mass_high,diboson_charge2_index_high)
diboson_weight_charge2_high = np.take(diboson_weight_high,diboson_charge2_index_high)
diboson_jet_n_charge2_high = np.take(diboson_jet_n_high,diboson_charge2_index_high)
diboson_electron_mt_charge2_high = np.take(diboson_electron_mt_high,diboson_charge2_index_high)
diboson_muon_mt_charge2_high = np.take(diboson_muon_mt_high,diboson_charge2_index_high)

diboson_inv_mass_charge2_low = np.take(diboson_inv_mass_low,diboson_charge2_index_low)
diboson_weight_charge2_low = np.take(diboson_weight_low,diboson_charge2_index_low)
diboson_jet_n_charge2_low = np.take(diboson_jet_n_low,diboson_charge2_index_low)
diboson_electron_mt_charge2_low = np.take(diboson_electron_mt_low,diboson_charge2_index_low)
diboson_muon_mt_charge2_low = np.take(diboson_muon_mt_low,diboson_charge2_index_low)


diboson_charge2min_index = np.where(diboson_total_charge == -2)
diboson_charge2min_index = diboson_charge2min_index[0]
diboson_charge2min_index_high = np.where(diboson_total_charge_high == -2)
diboson_charge2min_index_high = diboson_charge2min_index_high[0]
diboson_charge2min_index_low = np.where(diboson_total_charge_low == -2)
diboson_charge2min_index_low = diboson_charge2min_index_low[0]

diboson_inv_mass_charge2min = np.take(diboson_inv_mass,diboson_charge2min_index)
diboson_met_charge2min = np.take(diboson_met,diboson_charge2min_index)
diboson_weight_charge2min = np.take(diboson_weight,diboson_charge2min_index)
diboson_jet_n_charge2min = np.take(diboson_jet_n,diboson_charge2min_index)
diboson_electron_mt_charge2min = np.take(diboson_electron_mt,diboson_charge2min_index)
diboson_muon_mt_charge2min = np.take(diboson_muon_mt,diboson_charge2min_index)

diboson_inv_mass_charge2min_high = np.take(diboson_inv_mass_high,diboson_charge2min_index_high)
diboson_weight_charge2min_high = np.take(diboson_weight_high,diboson_charge2min_index_high)
diboson_jet_n_charge2min_high = np.take(diboson_jet_n_high,diboson_charge2min_index_high)
diboson_electron_mt_charge2min_high = np.take(diboson_electron_mt_high,diboson_charge2min_index_high)
diboson_muon_mt_charge2min_high = np.take(diboson_muon_mt_high,diboson_charge2min_index_high)

diboson_inv_mass_charge2min_low = np.take(diboson_inv_mass_low,diboson_charge2min_index_low)
diboson_weight_charge2min_low = np.take(diboson_weight_low,diboson_charge2min_index_low)
diboson_jet_n_charge2min_low = np.take(diboson_jet_n_low,diboson_charge2min_index_low)
diboson_electron_mt_charge2min_low = np.take(diboson_electron_mt_low,diboson_charge2min_index_low)
diboson_muon_mt_charge2min_low = np.take(diboson_muon_mt_low,diboson_charge2min_index_low)

# charge division of em3 states

diboson_charge0_index_em3 = np.where(diboson_total_charge_em3 == 0)
diboson_charge0_index_em3 = diboson_charge0_index_em3[0]
diboson_charge0_index_high_em3 = np.where(diboson_total_charge_high_em3 == 0)
diboson_charge0_index_high_em3 = diboson_charge0_index_high_em3[0]
diboson_charge0_index_low_em3 = np.where(diboson_total_charge_low_em3 == 0)
diboson_charge0_index_low_em3 = diboson_charge0_index_low_em3[0]

diboson_inv_mass_charge0_em3 = np.take(diboson_inv_mass_em3,diboson_charge0_index_em3)
diboson_met_charge0_em3 = np.take(diboson_met_em3,diboson_charge0_index_em3)
diboson_weight_charge0_em3 = np.take(diboson_weight_em3,diboson_charge0_index_em3)
diboson_jet_n_charge0_em3 = np.take(diboson_jet_n_em3,diboson_charge0_index_em3)
diboson_single_mt_charge0_em3 = np.take(diboson_single_mt,diboson_charge0_index_em3)

diboson_inv_mass_charge0_high_em3 = np.take(diboson_inv_mass_high_em3,diboson_charge0_index_high_em3)
diboson_weight_charge0_high_em3 = np.take(diboson_weight_high_em3,diboson_charge0_index_high_em3)
diboson_jet_n_charge0_high_em3 = np.take(diboson_jet_n_high_em3,diboson_charge0_index_high_em3)
diboson_single_mt_charge0_high_em3 = np.take(diboson_single_mt_high,diboson_charge0_index_high_em3)

diboson_inv_mass_charge0_low_em3 = np.take(diboson_inv_mass_low_em3,diboson_charge0_index_low_em3)
diboson_weight_charge0_low_em3 = np.take(diboson_weight_low_em3,diboson_charge0_index_low_em3)
diboson_jet_n_charge0_low_em3 = np.take(diboson_jet_n_low_em3,diboson_charge0_index_low_em3)
diboson_single_mt_charge0_low_em3 = np.take(diboson_single_mt_low,diboson_charge0_index_low_em3)


diboson_charge2_index_em3 = np.where(diboson_total_charge_em3 == 2)
diboson_charge2_index_em3 = diboson_charge2_index_em3[0]
diboson_charge2_index_high_em3 = np.where(diboson_total_charge_high_em3 == 2)
diboson_charge2_index_high_em3 = diboson_charge2_index_high_em3[0]
diboson_charge2_index_low_em3 = np.where(diboson_total_charge_low_em3 == 2)
diboson_charge2_index_low_em3 = diboson_charge2_index_low_em3[0]

diboson_inv_mass_charge2_em3 = np.take(diboson_inv_mass_em3,diboson_charge2_index_em3)
diboson_met_charge2_em3 = np.take(diboson_met_em3,diboson_charge2_index_em3)
diboson_weight_charge2_em3 = np.take(diboson_weight_em3,diboson_charge2_index_em3)
diboson_jet_n_charge2_em3 = np.take(diboson_jet_n_em3,diboson_charge2_index_em3)
diboson_single_mt_charge2_em3 = np.take(diboson_single_mt,diboson_charge2_index_em3)

diboson_inv_mass_charge2_high_em3 = np.take(diboson_inv_mass_high_em3,diboson_charge2_index_high_em3)
diboson_weight_charge2_high_em3 = np.take(diboson_weight_high_em3,diboson_charge2_index_high_em3)
diboson_jet_n_charge2_high_em3 = np.take(diboson_jet_n_high_em3,diboson_charge2_index_high_em3)
diboson_single_mt_charge2_high_em3 = np.take(diboson_single_mt_high,diboson_charge2_index_high_em3)

diboson_inv_mass_charge2_low_em3 = np.take(diboson_inv_mass_low_em3,diboson_charge2_index_low_em3)
diboson_weight_charge2_low_em3 = np.take(diboson_weight_low_em3,diboson_charge2_index_low_em3)
diboson_jet_n_charge2_low_em3 = np.take(diboson_jet_n_low_em3,diboson_charge2_index_low_em3)
diboson_single_mt_charge2_low_em3 = np.take(diboson_single_mt_low,diboson_charge2_index_low_em3)


diboson_charge2min_index_em3 = np.where(diboson_total_charge_em3 == -2)
diboson_charge2min_index_em3 = diboson_charge2min_index_em3[0]
diboson_charge2min_index_high_em3 = np.where(diboson_total_charge_high_em3 == -2)
diboson_charge2min_index_high_em3 = diboson_charge2min_index_high_em3[0]
diboson_charge2min_index_low_em3 = np.where(diboson_total_charge_low_em3 == -2)
diboson_charge2min_index_low_em3 = diboson_charge2min_index_low_em3[0]

diboson_inv_mass_charge2min_em3 = np.take(diboson_inv_mass_em3,diboson_charge2min_index_em3)
diboson_met_charge2min_em3 = np.take(diboson_met_em3,diboson_charge2min_index_em3)
diboson_weight_charge2min_em3 = np.take(diboson_weight_em3,diboson_charge2min_index_em3)
diboson_jet_n_charge2min_em3 = np.take(diboson_jet_n_em3,diboson_charge2min_index_em3)
diboson_single_mt_charge2min_em3 = np.take(diboson_single_mt,diboson_charge2min_index_em3)

diboson_inv_mass_charge2min_high_em3 = np.take(diboson_inv_mass_high_em3,diboson_charge2min_index_high_em3)
diboson_weight_charge2min_high_em3 = np.take(diboson_weight_high_em3,diboson_charge2min_index_high_em3)
diboson_jet_n_charge2min_high_em3 = np.take(diboson_jet_n_high_em3,diboson_charge2min_index_high_em3)
diboson_single_mt_charge2min_high_em3 = np.take(diboson_single_mt_high,diboson_charge2min_index_high_em3)

diboson_inv_mass_charge2min_low_em3 = np.take(diboson_inv_mass_low_em3,diboson_charge2min_index_low_em3)
diboson_weight_charge2min_low_em3 = np.take(diboson_weight_low_em3,diboson_charge2min_index_low_em3)
diboson_jet_n_charge2min_low_em3 = np.take(diboson_jet_n_low_em3,diboson_charge2min_index_low_em3)
diboson_single_mt_charge2min_low_em3 = np.take(diboson_single_mt_low,diboson_charge2min_index_low_em3)


#higgs relevant selection

n=0
index = np.empty(0)
while n < len(diboson_electron_charge):

    temp1 = diboson_electron_charge[n]
    temp2 = diboson_muon_charge[n]

    num = diboson_electron_n[n]

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


diboson_higgs_index = index.astype('int64')

diboson_higgs_inv_mass = np.take(diboson_inv_mass,diboson_higgs_index)
diboson_higgs_met = np.take(diboson_met,diboson_higgs_index)
diboson_higgs_weight = np.take(diboson_weight,diboson_higgs_index)
#diboson_higgs_dilep_mass = np.take(diboson_dilep_mass,diboson_higgs_index)
diboson_higgs_electron_n = np.take(diboson_electron_n,diboson_higgs_index)
diboson_higgs_muon_n = np.take(diboson_muon_n,diboson_higgs_index)
diboson_higgs_electron_charge = np.take(diboson_electron_charge,diboson_higgs_index)
diboson_higgs_muon_charge = np.take(diboson_muon_charge,diboson_higgs_index)
diboson_higgs_jet_n = np.take(diboson_jet_n,diboson_higgs_index)
diboson_higgs_jet_btag = np.take(diboson_jet_btag,diboson_higgs_index)
diboson_higgs_electron_mt = np.take(diboson_electron_mt,diboson_higgs_index)
diboson_higgs_muon_mt = np.take(diboson_muon_mt,diboson_higgs_index)
