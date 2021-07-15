#inv_mass_cut

#imtribosonindex = np.where(triboson_inv_mass < 400)
#imtribosonindex = imtribosonindex[0]

#triboson_inv_mass = np.take(triboson_inv_mass,imtribosonindex)
#triboson_met = np.take(triboson_met,imtribosonindex)
#triboson_weight = np.take(triboson_weight,imtribosonindex)
#triboson_dilep_mass = np.take(triboson_dilep_mass,imtribosonindex)
#triboson_electron_n = np.take(triboson_electron_n,imtribosonindex)
#triboson_muon_n = np.take(triboson_muon_n,imtribosonindex)
#triboson_electron_charge = np.take(triboson_electron_charge,imtribosonindex)
#triboson_muon_charge = np.take(triboson_muon_charge,imtribosonindex)
#triboson_jet_n = np.take(triboson_jet_n,imtribosonindex)
#triboson_jet_btag = np.take(triboson_jet_btag,imtribosonindex)
#triboson_muononz = np.take(triboson_muononz,imtribosonindex)
#triboson_electrononz = np.take(triboson_electrononz,imtribosonindex)
#triboson_electron_mt = np.take(triboson_electron_mt,imtribosonindex)
#triboson_muon_mt = np.take(triboson_muon_mt,imtribosonindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(triboson_electrononz):

    array = np.concatenate((triboson_electrononz[n],triboson_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

tribosonindex = index.astype('int64')

triboson_inv_mass = np.take(triboson_inv_mass,tribosonindex)
triboson_met = np.take(triboson_met,tribosonindex)
triboson_weight = np.take(triboson_weight,tribosonindex)
triboson_dilep_mass = np.take(triboson_dilep_mass,tribosonindex)
triboson_electron_n = np.take(triboson_electron_n,tribosonindex)
triboson_muon_n = np.take(triboson_muon_n,tribosonindex)
triboson_electron_charge = np.take(triboson_electron_charge,tribosonindex)
triboson_muon_charge = np.take(triboson_muon_charge,tribosonindex)
triboson_jet_n = np.take(triboson_jet_n,tribosonindex)
triboson_jet_btag = np.take(triboson_jet_btag,tribosonindex)
triboson_electron_mt = np.take(triboson_electron_mt,tribosonindex)
triboson_muon_mt = np.take(triboson_muon_mt,tribosonindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(triboson_jet_btag):

    array = triboson_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

triboson_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(triboson_electron_charge):

    temp1 = triboson_electron_charge[n]
    temp2 = triboson_muon_charge[n]

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

triboson_total_charge = temp


#add high or low missing transverse energy groups

tribosonindexlow = np.where(triboson_met < 50)
tribosonindexlow = tribosonindexlow[0]
tribosonindexhigh = np.where(triboson_met > 50)
tribosonindexhigh = tribosonindexhigh[0]


triboson_inv_mass_high = np.take(triboson_inv_mass,tribosonindexhigh)
triboson_weight_high = np.take(triboson_weight,tribosonindexhigh)
triboson_dilep_mass_high = np.take(triboson_dilep_mass,tribosonindexhigh)
triboson_electron_n_high = np.take(triboson_electron_n,tribosonindexhigh)
triboson_muon_n_high = np.take(triboson_muon_n,tribosonindexhigh)
triboson_total_charge_high = np.take(triboson_total_charge,tribosonindexhigh)
triboson_jet_n_high = np.take(triboson_jet_n,tribosonindexhigh)
triboson_bjet_n_high = np.take(triboson_bjet_n,tribosonindexhigh)

triboson_electron_mt_high = np.take(triboson_electron_mt,tribosonindexhigh)
triboson_muon_mt_high = np.take(triboson_muon_mt,tribosonindexhigh)


triboson_inv_mass_low = np.take(triboson_inv_mass,tribosonindexlow)
triboson_weight_low = np.take(triboson_weight,tribosonindexlow)
triboson_dilep_mass_low = np.take(triboson_dilep_mass,tribosonindexlow)
triboson_electron_n_low = np.take(triboson_electron_n,tribosonindexlow)
triboson_muon_n_low = np.take(triboson_muon_n,tribosonindexlow)
triboson_total_charge_low = np.take(triboson_total_charge,tribosonindexlow)
triboson_jet_n_low = np.take(triboson_jet_n,tribosonindexlow)
triboson_bjet_n_low = np.take(triboson_bjet_n,tribosonindexlow)

triboson_electron_mt_low = np.take(triboson_electron_mt,tribosonindexlow)
triboson_muon_mt_low = np.take(triboson_muon_mt,tribosonindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(triboson_electron_mt):

    array = np.concatenate((triboson_electron_mt[n],triboson_muon_mt[n]))
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

triboson_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
triboson_total_mt_weight = np.concatenate((triboson_weight,triboson_weight,triboson_weight,triboson_weight))

n = 0
temp = np.empty((4,0))
while n < len(triboson_electron_mt_high):

    array = np.concatenate((triboson_electron_mt_high[n],triboson_muon_mt_high[n]))
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

triboson_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
triboson_total_mt_weight_high = np.concatenate((triboson_weight_high,triboson_weight_high,triboson_weight_high,triboson_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(triboson_electron_mt_low):

    array = np.concatenate((triboson_electron_mt_low[n],triboson_muon_mt_low[n]))
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

triboson_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
triboson_total_mt_weight_low = np.concatenate((triboson_weight_low,triboson_weight_low,triboson_weight_low,triboson_weight_low))

#get only emmm or eeem end states

tribosonindexm3 = np.where(triboson_electron_n == 1)
tribosonindexe3 = np.where(triboson_electron_n == 3)
tribosonindexm3 = tribosonindexm3[0]
tribosonindexe3 = tribosonindexe3[0]
tribosonindexem3 = np.concatenate((tribosonindexm3,tribosonindexe3))
tribosonindexem3 = np.sort(tribosonindexem3)

tribosonindexhighm3 = np.where(triboson_electron_n_high == 1)
tribosonindexhighe3 = np.where(triboson_electron_n_high == 3)
tribosonindexhighm3 = tribosonindexhighm3[0]
tribosonindexhighe3 = tribosonindexhighe3[0]
tribosonindexhighem3 = np.concatenate((tribosonindexhighm3,tribosonindexhighe3))
tribosonindexhighem3 = np.sort(tribosonindexhighem3)

tribosonindexlowm3 = np.where(triboson_electron_n_low == 1)
tribosonindexlowe3 = np.where(triboson_electron_n_low == 3)
tribosonindexlowm3 = tribosonindexlowm3[0]
tribosonindexlowe3 = tribosonindexlowe3[0]
tribosonindexlowem3 = np.concatenate((tribosonindexlowm3,tribosonindexlowe3))
tribosonindexlowem3 = np.sort(tribosonindexlowem3)

triboson_inv_mass_em3 = np.take(triboson_inv_mass,tribosonindexem3)
triboson_met_em3 = np.take(triboson_met,tribosonindexem3)
triboson_weight_em3 = np.take(triboson_weight,tribosonindexem3)
triboson_dilep_mass_em3 = np.take(triboson_dilep_mass,tribosonindexem3)
triboson_total_charge_em3 = np.take(triboson_total_charge,tribosonindexem3)
triboson_jet_n_em3 = np.take(triboson_jet_n,tribosonindexem3)
triboson_bjet_n_em3 = np.take(triboson_bjet_n,tribosonindexem3)

triboson_electron_mt_em3 = np.take(triboson_electron_mt,tribosonindexem3)
triboson_muon_mt_em3 = np.take(triboson_muon_mt,tribosonindexem3)

triboson_inv_mass_high_em3 = np.take(triboson_inv_mass_high,tribosonindexhighem3)
triboson_weight_high_em3 = np.take(triboson_weight_high,tribosonindexhighem3)
triboson_dilep_mass_high_em3 = np.take(triboson_dilep_mass_high,tribosonindexhighem3)
triboson_total_charge_high_em3 = np.take(triboson_total_charge_high,tribosonindexhighem3)
triboson_jet_n_high_em3 = np.take(triboson_jet_n_high,tribosonindexhighem3)
triboson_bjet_n_high_em3 = np.take(triboson_bjet_n_high,tribosonindexhighem3)

triboson_electron_mt_high_em3 = np.take(triboson_electron_mt_high,tribosonindexhighem3)
triboson_muon_mt_high_em3 = np.take(triboson_muon_mt_high,tribosonindexhighem3)

triboson_inv_mass_low_em3 = np.take(triboson_inv_mass_low,tribosonindexlowem3)
triboson_weight_low_em3 = np.take(triboson_weight_low,tribosonindexlowem3)
triboson_dilep_mass_low_em3 = np.take(triboson_dilep_mass_low,tribosonindexlowem3)
triboson_total_charge_low_em3 = np.take(triboson_total_charge_low,tribosonindexlowem3)
triboson_jet_n_low_em3 = np.take(triboson_jet_n_low,tribosonindexlowem3)
triboson_bjet_n_low_em3 = np.take(triboson_bjet_n_low,tribosonindexlowem3)

triboson_electron_mt_low_em3 = np.take(triboson_electron_mt_low,tribosonindexlowem3)
triboson_muon_mt_low_em3 = np.take(triboson_muon_mt_low,tribosonindexlowem3)

n = 0
temp = np.empty(0)
while n < len(triboson_electron_mt_em3):

    array1 = triboson_electron_mt_em3[n]
    array2 = triboson_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

triboson_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(triboson_electron_mt_low_em3):

    array1 = triboson_electron_mt_low_em3[n]
    array2 = triboson_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

triboson_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(triboson_electron_mt_high_em3):

    array1 = triboson_electron_mt_high_em3[n]
    array2 = triboson_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

triboson_single_mt_high = temp

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(triboson_dilep_mass_em3):

    array = triboson_dilep_mass_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

triboson_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
triboson_weight_dilep_em3 = np.concatenate((triboson_weight_em3,triboson_weight_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(triboson_dilep_mass_high_em3):

    array = triboson_dilep_mass_high_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

triboson_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
triboson_weight_dilep_high_em3 = np.concatenate((triboson_weight_high_em3,triboson_weight_high_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(triboson_dilep_mass_low_em3):

    array = triboson_dilep_mass_low_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

triboson_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
triboson_weight_dilep_low_em3 = np.concatenate((triboson_weight_low_em3,triboson_weight_low_em3))

#only states with 0 jets

triboson_jet_0_index = np.where(triboson_jet_n == 0)
triboson_jet_0_index = triboson_jet_0_index[0]
triboson_jet_0_index_high = np.where(triboson_jet_n_high == 0)
triboson_jet_0_index_high = triboson_jet_0_index_high[0]
triboson_jet_0_index_low = np.where(triboson_jet_n_low == 0)
triboson_jet_0_index_low = triboson_jet_0_index_low[0]


triboson_inv_mass_0jet = np.take(triboson_inv_mass,triboson_jet_0_index)
triboson_met_0jet = np.take(triboson_met,triboson_jet_0_index)
triboson_weight_0jet = np.take(triboson_weight,triboson_jet_0_index)
triboson_total_charge_0jet = np.take(triboson_total_charge,triboson_jet_0_index)


triboson_inv_mass_high_0jet = np.take(triboson_inv_mass_high,triboson_jet_0_index_high)
triboson_weight_high_0jet = np.take(triboson_weight_high,triboson_jet_0_index_high)
triboson_total_charge_high_0jet = np.take(triboson_total_charge_high,triboson_jet_0_index_high)

triboson_inv_mass_low_0jet = np.take(triboson_inv_mass_low,triboson_jet_0_index_low)
triboson_weight_low_0jet = np.take(triboson_weight_low,triboson_jet_0_index_low)
triboson_total_charge_low_0jet = np.take(triboson_total_charge_low,triboson_jet_0_index_low)

#only states where eeem or emmm and 0 bjets

triboson_bjet_0em3_index = np.where(triboson_bjet_n_em3 == 0)
triboson_bjet_0em3_index = triboson_bjet_0em3_index[0]
triboson_bjet_0em3_index_high = np.where(triboson_bjet_n_high_em3 == 0)
triboson_bjet_0em3_index_high = triboson_bjet_0em3_index_high[0]
triboson_bjet_0em3_index_low = np.where(triboson_bjet_n_low_em3 == 0)
triboson_bjet_0em3_index_low = triboson_bjet_0em3_index_low[0]


triboson_inv_mass_0em3 = np.take(triboson_inv_mass_em3,triboson_bjet_0em3_index)
triboson_met_0em3 = np.take(triboson_met_em3,triboson_bjet_0em3_index)
triboson_weight_0em3 = np.take(triboson_weight_em3,triboson_bjet_0em3_index)
triboson_dilep_mass_0em3 = np.take(triboson_dilep_mass_em3,triboson_bjet_0em3_index)
triboson_total_charge_0em3 = np.take(triboson_total_charge_em3,triboson_bjet_0em3_index)
triboson_jet_n_0em3 = np.take(triboson_jet_n_em3,triboson_bjet_0em3_index)

triboson_inv_mass_high_0em3 = np.take(triboson_inv_mass_high_em3,triboson_bjet_0em3_index_high)
triboson_weight_high_0em3 = np.take(triboson_weight_high_em3,triboson_bjet_0em3_index_high)
triboson_dilep_mass_high_0em3 = np.take(triboson_dilep_mass_high_em3,triboson_bjet_0em3_index_high)
triboson_total_charge_high_0em3 = np.take(triboson_total_charge_high_em3,triboson_bjet_0em3_index_high)
triboson_jet_n_high_0em3 = np.take(triboson_jet_n_high_em3,triboson_bjet_0em3_index_high)

triboson_inv_mass_low_0em3 = np.take(triboson_inv_mass_low_em3,triboson_bjet_0em3_index_low)
triboson_weight_low_0em3 = np.take(triboson_weight_low_em3,triboson_bjet_0em3_index_low)
triboson_dilep_mass_low_0em3 = np.take(triboson_dilep_mass_low_em3,triboson_bjet_0em3_index_low)
triboson_total_charge_low_0em3 = np.take(triboson_total_charge_low_em3,triboson_bjet_0em3_index_low)
triboson_jet_n_low_0em3 = np.take(triboson_jet_n_low_em3,triboson_bjet_0em3_index_low)

triboson_electron_mt_0em3 = np.take(triboson_electron_mt_em3,triboson_bjet_0em3_index)
triboson_muon_mt_0em3 = np.take(triboson_muon_mt_em3,triboson_bjet_0em3_index)

triboson_electron_mt_high_0em3 = np.take(triboson_electron_mt_high_em3,triboson_bjet_0em3_index_high)
triboson_muon_mt_high_0em3 = np.take(triboson_muon_mt_high_em3,triboson_bjet_0em3_index_high)

triboson_electron_mt_low_0em3 = np.take(triboson_electron_mt_low_em3,triboson_bjet_0em3_index_low)
triboson_muon_mt_low_0em3 = np.take(triboson_muon_mt_low_em3,triboson_bjet_0em3_index_low)

triboson_single_mt_0b = np.take(triboson_single_mt,triboson_bjet_0em3_index)
triboson_single_mt_high_0b = np.take(triboson_single_mt_high,triboson_bjet_0em3_index_high)
triboson_single_mt_low_0b = np.take(triboson_single_mt_low,triboson_bjet_0em3_index_low)

#division based on total charge

triboson_charge0_index = np.where(triboson_total_charge == 0)
triboson_charge0_index = triboson_charge0_index[0]
triboson_charge0_index_high = np.where(triboson_total_charge_high == 0)
triboson_charge0_index_high = triboson_charge0_index_high[0]
triboson_charge0_index_low = np.where(triboson_total_charge_low == 0)
triboson_charge0_index_low = triboson_charge0_index_low[0]

triboson_inv_mass_charge0 = np.take(triboson_inv_mass,triboson_charge0_index)
triboson_met_charge0 = np.take(triboson_met,triboson_charge0_index)
triboson_weight_charge0 = np.take(triboson_weight,triboson_charge0_index)
triboson_jet_n_charge0 = np.take(triboson_jet_n,triboson_charge0_index)
triboson_electron_mt_charge0 = np.take(triboson_electron_mt,triboson_charge0_index)
triboson_muon_mt_charge0 = np.take(triboson_muon_mt,triboson_charge0_index)

triboson_inv_mass_charge0_high = np.take(triboson_inv_mass_high,triboson_charge0_index_high)
triboson_weight_charge0_high = np.take(triboson_weight_high,triboson_charge0_index_high)
triboson_jet_n_charge0_high = np.take(triboson_jet_n_high,triboson_charge0_index_high)
triboson_electron_mt_charge0_high = np.take(triboson_electron_mt_high,triboson_charge0_index_high)
triboson_muon_mt_charge0_high = np.take(triboson_muon_mt_high,triboson_charge0_index_high)

triboson_inv_mass_charge0_low = np.take(triboson_inv_mass_low,triboson_charge0_index_low)
triboson_weight_charge0_low = np.take(triboson_weight_low,triboson_charge0_index_low)
triboson_jet_n_charge0_low = np.take(triboson_jet_n_low,triboson_charge0_index_low)
triboson_electron_mt_charge0_low = np.take(triboson_electron_mt_low,triboson_charge0_index_low)
triboson_muon_mt_charge0_low = np.take(triboson_muon_mt_low,triboson_charge0_index_low)


triboson_charge2_index = np.where(triboson_total_charge == 2)
triboson_charge2_index = triboson_charge2_index[0]
triboson_charge2_index_high = np.where(triboson_total_charge_high == 2)
triboson_charge2_index_high = triboson_charge2_index_high[0]
triboson_charge2_index_low = np.where(triboson_total_charge_low == 2)
triboson_charge2_index_low = triboson_charge2_index_low[0]

triboson_inv_mass_charge2 = np.take(triboson_inv_mass,triboson_charge2_index)
triboson_met_charge2 = np.take(triboson_met,triboson_charge2_index)
triboson_weight_charge2 = np.take(triboson_weight,triboson_charge2_index)
triboson_jet_n_charge2 = np.take(triboson_jet_n,triboson_charge2_index)
triboson_electron_mt_charge2 = np.take(triboson_electron_mt,triboson_charge2_index)
triboson_muon_mt_charge2 = np.take(triboson_muon_mt,triboson_charge2_index)

triboson_inv_mass_charge2_high = np.take(triboson_inv_mass_high,triboson_charge2_index_high)
triboson_weight_charge2_high = np.take(triboson_weight_high,triboson_charge2_index_high)
triboson_jet_n_charge2_high = np.take(triboson_jet_n_high,triboson_charge2_index_high)
triboson_electron_mt_charge2_high = np.take(triboson_electron_mt_high,triboson_charge2_index_high)
triboson_muon_mt_charge2_high = np.take(triboson_muon_mt_high,triboson_charge2_index_high)

triboson_inv_mass_charge2_low = np.take(triboson_inv_mass_low,triboson_charge2_index_low)
triboson_weight_charge2_low = np.take(triboson_weight_low,triboson_charge2_index_low)
triboson_jet_n_charge2_low = np.take(triboson_jet_n_low,triboson_charge2_index_low)
triboson_electron_mt_charge2_low = np.take(triboson_electron_mt_low,triboson_charge2_index_low)
triboson_muon_mt_charge2_low = np.take(triboson_muon_mt_low,triboson_charge2_index_low)


triboson_charge2min_index = np.where(triboson_total_charge == -2)
triboson_charge2min_index = triboson_charge2min_index[0]
triboson_charge2min_index_high = np.where(triboson_total_charge_high == -2)
triboson_charge2min_index_high = triboson_charge2min_index_high[0]
triboson_charge2min_index_low = np.where(triboson_total_charge_low == -2)
triboson_charge2min_index_low = triboson_charge2min_index_low[0]

triboson_inv_mass_charge2min = np.take(triboson_inv_mass,triboson_charge2min_index)
triboson_met_charge2min = np.take(triboson_met,triboson_charge2min_index)
triboson_weight_charge2min = np.take(triboson_weight,triboson_charge2min_index)
triboson_jet_n_charge2min = np.take(triboson_jet_n,triboson_charge2min_index)
triboson_electron_mt_charge2min = np.take(triboson_electron_mt,triboson_charge2min_index)
triboson_muon_mt_charge2min = np.take(triboson_muon_mt,triboson_charge2min_index)

triboson_inv_mass_charge2min_high = np.take(triboson_inv_mass_high,triboson_charge2min_index_high)
triboson_weight_charge2min_high = np.take(triboson_weight_high,triboson_charge2min_index_high)
triboson_jet_n_charge2min_high = np.take(triboson_jet_n_high,triboson_charge2min_index_high)
triboson_electron_mt_charge2min_high = np.take(triboson_electron_mt_high,triboson_charge2min_index_high)
triboson_muon_mt_charge2min_high = np.take(triboson_muon_mt_high,triboson_charge2min_index_high)

triboson_inv_mass_charge2min_low = np.take(triboson_inv_mass_low,triboson_charge2min_index_low)
triboson_weight_charge2min_low = np.take(triboson_weight_low,triboson_charge2min_index_low)
triboson_jet_n_charge2min_low = np.take(triboson_jet_n_low,triboson_charge2min_index_low)
triboson_electron_mt_charge2min_low = np.take(triboson_electron_mt_low,triboson_charge2min_index_low)
triboson_muon_mt_charge2min_low = np.take(triboson_muon_mt_low,triboson_charge2min_index_low)

# charge division of em3 states

triboson_charge0_index_em3 = np.where(triboson_total_charge_em3 == 0)
triboson_charge0_index_em3 = triboson_charge0_index_em3[0]
triboson_charge0_index_high_em3 = np.where(triboson_total_charge_high_em3 == 0)
triboson_charge0_index_high_em3 = triboson_charge0_index_high_em3[0]
triboson_charge0_index_low_em3 = np.where(triboson_total_charge_low_em3 == 0)
triboson_charge0_index_low_em3 = triboson_charge0_index_low_em3[0]

triboson_inv_mass_charge0_em3 = np.take(triboson_inv_mass_em3,triboson_charge0_index_em3)
triboson_met_charge0_em3 = np.take(triboson_met_em3,triboson_charge0_index_em3)
triboson_weight_charge0_em3 = np.take(triboson_weight_em3,triboson_charge0_index_em3)
triboson_jet_n_charge0_em3 = np.take(triboson_jet_n_em3,triboson_charge0_index_em3)
triboson_single_mt_charge0_em3 = np.take(triboson_single_mt,triboson_charge0_index_em3)

triboson_inv_mass_charge0_high_em3 = np.take(triboson_inv_mass_high_em3,triboson_charge0_index_high_em3)
triboson_weight_charge0_high_em3 = np.take(triboson_weight_high_em3,triboson_charge0_index_high_em3)
triboson_jet_n_charge0_high_em3 = np.take(triboson_jet_n_high_em3,triboson_charge0_index_high_em3)
triboson_single_mt_charge0_high_em3 = np.take(triboson_single_mt_high,triboson_charge0_index_high_em3)

triboson_inv_mass_charge0_low_em3 = np.take(triboson_inv_mass_low_em3,triboson_charge0_index_low_em3)
triboson_weight_charge0_low_em3 = np.take(triboson_weight_low_em3,triboson_charge0_index_low_em3)
triboson_jet_n_charge0_low_em3 = np.take(triboson_jet_n_low_em3,triboson_charge0_index_low_em3)
triboson_single_mt_charge0_low_em3 = np.take(triboson_single_mt_low,triboson_charge0_index_low_em3)


triboson_charge2_index_em3 = np.where(triboson_total_charge_em3 == 2)
triboson_charge2_index_em3 = triboson_charge2_index_em3[0]
triboson_charge2_index_high_em3 = np.where(triboson_total_charge_high_em3 == 2)
triboson_charge2_index_high_em3 = triboson_charge2_index_high_em3[0]
triboson_charge2_index_low_em3 = np.where(triboson_total_charge_low_em3 == 2)
triboson_charge2_index_low_em3 = triboson_charge2_index_low_em3[0]

triboson_inv_mass_charge2_em3 = np.take(triboson_inv_mass_em3,triboson_charge2_index_em3)
triboson_met_charge2_em3 = np.take(triboson_met_em3,triboson_charge2_index_em3)
triboson_weight_charge2_em3 = np.take(triboson_weight_em3,triboson_charge2_index_em3)
triboson_jet_n_charge2_em3 = np.take(triboson_jet_n_em3,triboson_charge2_index_em3)
triboson_single_mt_charge2_em3 = np.take(triboson_single_mt,triboson_charge2_index_em3)

triboson_inv_mass_charge2_high_em3 = np.take(triboson_inv_mass_high_em3,triboson_charge2_index_high_em3)
triboson_weight_charge2_high_em3 = np.take(triboson_weight_high_em3,triboson_charge2_index_high_em3)
triboson_jet_n_charge2_high_em3 = np.take(triboson_jet_n_high_em3,triboson_charge2_index_high_em3)
triboson_single_mt_charge2_high_em3 = np.take(triboson_single_mt_high,triboson_charge2_index_high_em3)

triboson_inv_mass_charge2_low_em3 = np.take(triboson_inv_mass_low_em3,triboson_charge2_index_low_em3)
triboson_weight_charge2_low_em3 = np.take(triboson_weight_low_em3,triboson_charge2_index_low_em3)
triboson_jet_n_charge2_low_em3 = np.take(triboson_jet_n_low_em3,triboson_charge2_index_low_em3)
triboson_single_mt_charge2_low_em3 = np.take(triboson_single_mt_low,triboson_charge2_index_low_em3)


triboson_charge2min_index_em3 = np.where(triboson_total_charge_em3 == -2)
triboson_charge2min_index_em3 = triboson_charge2min_index_em3[0]
triboson_charge2min_index_high_em3 = np.where(triboson_total_charge_high_em3 == -2)
triboson_charge2min_index_high_em3 = triboson_charge2min_index_high_em3[0]
triboson_charge2min_index_low_em3 = np.where(triboson_total_charge_low_em3 == -2)
triboson_charge2min_index_low_em3 = triboson_charge2min_index_low_em3[0]

triboson_inv_mass_charge2min_em3 = np.take(triboson_inv_mass_em3,triboson_charge2min_index_em3)
triboson_met_charge2min_em3 = np.take(triboson_met_em3,triboson_charge2min_index_em3)
triboson_weight_charge2min_em3 = np.take(triboson_weight_em3,triboson_charge2min_index_em3)
triboson_jet_n_charge2min_em3 = np.take(triboson_jet_n_em3,triboson_charge2min_index_em3)
triboson_single_mt_charge2min_em3 = np.take(triboson_single_mt,triboson_charge2min_index_em3)

triboson_inv_mass_charge2min_high_em3 = np.take(triboson_inv_mass_high_em3,triboson_charge2min_index_high_em3)
triboson_weight_charge2min_high_em3 = np.take(triboson_weight_high_em3,triboson_charge2min_index_high_em3)
triboson_jet_n_charge2min_high_em3 = np.take(triboson_jet_n_high_em3,triboson_charge2min_index_high_em3)
triboson_single_mt_charge2min_high_em3 = np.take(triboson_single_mt_high,triboson_charge2min_index_high_em3)

triboson_inv_mass_charge2min_low_em3 = np.take(triboson_inv_mass_low_em3,triboson_charge2min_index_low_em3)
triboson_weight_charge2min_low_em3 = np.take(triboson_weight_low_em3,triboson_charge2min_index_low_em3)
triboson_jet_n_charge2min_low_em3 = np.take(triboson_jet_n_low_em3,triboson_charge2min_index_low_em3)
triboson_single_mt_charge2min_low_em3 = np.take(triboson_single_mt_low,triboson_charge2min_index_low_em3)


#higgs relevant selection

n=0
index = np.empty(0)
while n < len(triboson_electron_charge):

    temp1 = triboson_electron_charge[n]
    temp2 = triboson_muon_charge[n]

    num = triboson_electron_n[n]

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


triboson_higgs_index = index.astype('int64')

triboson_higgs_inv_mass = np.take(triboson_inv_mass,triboson_higgs_index)
triboson_higgs_met = np.take(triboson_met,triboson_higgs_index)
triboson_higgs_weight = np.take(triboson_weight,triboson_higgs_index)
#triboson_higgs_dilep_mass = np.take(triboson_dilep_mass,triboson_higgs_index)
triboson_higgs_electron_n = np.take(triboson_electron_n,triboson_higgs_index)
triboson_higgs_muon_n = np.take(triboson_muon_n,triboson_higgs_index)
triboson_higgs_electron_charge = np.take(triboson_electron_charge,triboson_higgs_index)
triboson_higgs_muon_charge = np.take(triboson_muon_charge,triboson_higgs_index)
triboson_higgs_jet_n = np.take(triboson_jet_n,triboson_higgs_index)
triboson_higgs_jet_btag = np.take(triboson_jet_btag,triboson_higgs_index)
triboson_higgs_electron_mt = np.take(triboson_electron_mt,triboson_higgs_index)
triboson_higgs_muon_mt = np.take(triboson_muon_mt,triboson_higgs_index)
