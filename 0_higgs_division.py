#inv_mass_cut

#imhiggsindex = np.where(higgs_inv_mass < 400)
#imhiggsindex = imhiggsindex[0]

#higgs_inv_mass = np.take(higgs_inv_mass,imhiggsindex)
#higgs_met = np.take(higgs_met,imhiggsindex)
#higgs_weight = np.take(higgs_weight,imhiggsindex)
#higgs_dilep_mass = np.take(higgs_dilep_mass,imhiggsindex)
#higgs_electron_n = np.take(higgs_electron_n,imhiggsindex)
#higgs_muon_n = np.take(higgs_muon_n,imhiggsindex)
#higgs_electron_charge = np.take(higgs_electron_charge,imhiggsindex)
#higgs_muon_charge = np.take(higgs_muon_charge,imhiggsindex)
#higgs_jet_n = np.take(higgs_jet_n,imhiggsindex)
#higgs_jet_btag = np.take(higgs_jet_btag,imhiggsindex)
#higgs_muononz = np.take(higgs_muononz,imhiggsindex)
#higgs_electrononz = np.take(higgs_electrononz,imhiggsindex)
#higgs_electron_mt = np.take(higgs_electron_mt,imhiggsindex)
#higgs_muon_mt = np.take(higgs_muon_mt,imhiggsindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(higgs_electrononz):

    array = np.concatenate((higgs_electrononz[n],higgs_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

higgsindex = index.astype('int64')

higgs_inv_mass = np.take(higgs_inv_mass,higgsindex)
higgs_met = np.take(higgs_met,higgsindex)
higgs_weight = np.take(higgs_weight,higgsindex)
#higgs_dilep_mass = np.take(higgs_dilep_mass,higgsindex)
higgs_electron_n = np.take(higgs_electron_n,higgsindex)
higgs_muon_n = np.take(higgs_muon_n,higgsindex)
higgs_electron_charge = np.take(higgs_electron_charge,higgsindex)
higgs_muon_charge = np.take(higgs_muon_charge,higgsindex)
higgs_jet_n = np.take(higgs_jet_n,higgsindex)
higgs_jet_btag = np.take(higgs_jet_btag,higgsindex)
higgs_electron_mt = np.take(higgs_electron_mt,higgsindex)
higgs_muon_mt = np.take(higgs_muon_mt,higgsindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(higgs_jet_btag):

    array = higgs_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

higgs_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(higgs_electron_charge):

    temp1 = higgs_electron_charge[n]
    temp2 = higgs_muon_charge[n]

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

higgs_total_charge = temp


#add high or low missing transverse energy groups

higgsindexlow = np.where(higgs_met < 50)
higgsindexlow = higgsindexlow[0]
higgsindexhigh = np.where(higgs_met > 50)
higgsindexhigh = higgsindexhigh[0]


higgs_inv_mass_high = np.take(higgs_inv_mass,higgsindexhigh)
higgs_weight_high = np.take(higgs_weight,higgsindexhigh)
#higgs_dilep_mass_high = np.take(higgs_dilep_mass,higgsindexhigh)
higgs_electron_n_high = np.take(higgs_electron_n,higgsindexhigh)
higgs_muon_n_high = np.take(higgs_muon_n,higgsindexhigh)
higgs_total_charge_high = np.take(higgs_total_charge,higgsindexhigh)
higgs_jet_n_high = np.take(higgs_jet_n,higgsindexhigh)
higgs_bjet_n_high = np.take(higgs_bjet_n,higgsindexhigh)

higgs_electron_mt_high = np.take(higgs_electron_mt,higgsindexhigh)
higgs_muon_mt_high = np.take(higgs_muon_mt,higgsindexhigh)


higgs_inv_mass_low = np.take(higgs_inv_mass,higgsindexlow)
higgs_weight_low = np.take(higgs_weight,higgsindexlow)
#higgs_dilep_mass_low = np.take(higgs_dilep_mass,higgsindexlow)
higgs_electron_n_low = np.take(higgs_electron_n,higgsindexlow)
higgs_muon_n_low = np.take(higgs_muon_n,higgsindexlow)
higgs_total_charge_low = np.take(higgs_total_charge,higgsindexlow)
higgs_jet_n_low = np.take(higgs_jet_n,higgsindexlow)
higgs_bjet_n_low = np.take(higgs_bjet_n,higgsindexlow)

higgs_electron_mt_low = np.take(higgs_electron_mt,higgsindexlow)
higgs_muon_mt_low = np.take(higgs_muon_mt,higgsindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(higgs_electron_mt):

    array = np.concatenate((higgs_electron_mt[n],higgs_muon_mt[n]))
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

higgs_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
higgs_total_mt_weight = np.concatenate((higgs_weight,higgs_weight,higgs_weight,higgs_weight))

n = 0
temp = np.empty((4,0))
while n < len(higgs_electron_mt_high):

    array = np.concatenate((higgs_electron_mt_high[n],higgs_muon_mt_high[n]))
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

higgs_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
higgs_total_mt_weight_high = np.concatenate((higgs_weight_high,higgs_weight_high,higgs_weight_high,higgs_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(higgs_electron_mt_low):

    array = np.concatenate((higgs_electron_mt_low[n],higgs_muon_mt_low[n]))
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

higgs_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
higgs_total_mt_weight_low = np.concatenate((higgs_weight_low,higgs_weight_low,higgs_weight_low,higgs_weight_low))

#get only emmm or eeem end states

higgsindexm3 = np.where(higgs_electron_n == 1)
higgsindexe3 = np.where(higgs_electron_n == 3)
higgsindexm3 = higgsindexm3[0]
higgsindexe3 = higgsindexe3[0]
higgsindexem3 = np.concatenate((higgsindexm3,higgsindexe3))
higgsindexem3 = np.sort(higgsindexem3)

higgsindexhighm3 = np.where(higgs_electron_n_high == 1)
higgsindexhighe3 = np.where(higgs_electron_n_high == 3)
higgsindexhighm3 = higgsindexhighm3[0]
higgsindexhighe3 = higgsindexhighe3[0]
higgsindexhighem3 = np.concatenate((higgsindexhighm3,higgsindexhighe3))
higgsindexhighem3 = np.sort(higgsindexhighem3)

higgsindexlowm3 = np.where(higgs_electron_n_low == 1)
higgsindexlowe3 = np.where(higgs_electron_n_low == 3)
higgsindexlowm3 = higgsindexlowm3[0]
higgsindexlowe3 = higgsindexlowe3[0]
higgsindexlowem3 = np.concatenate((higgsindexlowm3,higgsindexlowe3))
higgsindexlowem3 = np.sort(higgsindexlowem3)

higgs_inv_mass_em3 = np.take(higgs_inv_mass,higgsindexem3)
higgs_met_em3 = np.take(higgs_met,higgsindexem3)
higgs_weight_em3 = np.take(higgs_weight,higgsindexem3)
#higgs_dilep_mass_em3 = np.take(higgs_dilep_mass,higgsindexem3)
higgs_total_charge_em3 = np.take(higgs_total_charge,higgsindexem3)
higgs_jet_n_em3 = np.take(higgs_jet_n,higgsindexem3)
higgs_bjet_n_em3 = np.take(higgs_bjet_n,higgsindexem3)

higgs_electron_mt_em3 = np.take(higgs_electron_mt,higgsindexem3)
higgs_muon_mt_em3 = np.take(higgs_muon_mt,higgsindexem3)

higgs_inv_mass_high_em3 = np.take(higgs_inv_mass_high,higgsindexhighem3)
higgs_weight_high_em3 = np.take(higgs_weight_high,higgsindexhighem3)
#higgs_dilep_mass_high_em3 = np.take(higgs_dilep_mass_high,higgsindexhighem3)
higgs_total_charge_high_em3 = np.take(higgs_total_charge_high,higgsindexhighem3)
higgs_jet_n_high_em3 = np.take(higgs_jet_n_high,higgsindexhighem3)
higgs_bjet_n_high_em3 = np.take(higgs_bjet_n_high,higgsindexhighem3)

higgs_electron_mt_high_em3 = np.take(higgs_electron_mt_high,higgsindexhighem3)
higgs_muon_mt_high_em3 = np.take(higgs_muon_mt_high,higgsindexhighem3)

higgs_inv_mass_low_em3 = np.take(higgs_inv_mass_low,higgsindexlowem3)
higgs_weight_low_em3 = np.take(higgs_weight_low,higgsindexlowem3)
#higgs_dilep_mass_low_em3 = np.take(higgs_dilep_mass_low,higgsindexlowem3)
higgs_total_charge_low_em3 = np.take(higgs_total_charge_low,higgsindexlowem3)
higgs_jet_n_low_em3 = np.take(higgs_jet_n_low,higgsindexlowem3)
higgs_bjet_n_low_em3 = np.take(higgs_bjet_n_low,higgsindexlowem3)

higgs_electron_mt_low_em3 = np.take(higgs_electron_mt_low,higgsindexlowem3)
higgs_muon_mt_low_em3 = np.take(higgs_muon_mt_low,higgsindexlowem3)

n = 0
temp = np.empty(0)
while n < len(higgs_electron_mt_em3):

    array1 = higgs_electron_mt_em3[n]
    array2 = higgs_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

higgs_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(higgs_electron_mt_low_em3):

    array1 = higgs_electron_mt_low_em3[n]
    array2 = higgs_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

higgs_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(higgs_electron_mt_high_em3):

    array1 = higgs_electron_mt_high_em3[n]
    array2 = higgs_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

higgs_single_mt_high = temp

#n = 0
#temp1 = np.empty(0)
#temp2 = np.empty(0)
#while n < len(higgs_dilep_mass_em3):

#    array = higgs_dilep_mass_em3[n]
#    temp1 = np.concatenate((temp1,[array[0]]))
#    temp2 = np.concatenate((temp2,[array[1]]))

#    n = n+1

#higgs_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
#higgs_weight_dilep_em3 = np.concatenate((higgs_weight_em3,higgs_weight_em3))

#n = 0
#temp1 = np.empty(0)
#temp2 = np.empty(0)
#while n < len(higgs_dilep_mass_high_em3):

#    array = higgs_dilep_mass_high_em3[n]
#    temp1 = np.concatenate((temp1,[array[0]]))
#    temp2 = np.concatenate((temp2,[array[1]]))

#    n = n+1

#higgs_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
#higgs_weight_dilep_high_em3 = np.concatenate((higgs_weight_high_em3,higgs_weight_high_em3))

#n = 0
#temp1 = np.empty(0)
#temp2 = np.empty(0)
#while n < len(higgs_dilep_mass_low_em3):

#    array = higgs_dilep_mass_low_em3[n]
#    temp1 = np.concatenate((temp1,[array[0]]))
#    temp2 = np.concatenate((temp2,[array[1]]))

#    n = n+1

#higgs_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
#higgs_weight_dilep_low_em3 = np.concatenate((higgs_weight_low_em3,higgs_weight_low_em3))

#only states with 0 jets

higgs_jet_0_index = np.where(higgs_jet_n == 0)
higgs_jet_0_index = higgs_jet_0_index[0]
higgs_jet_0_index_high = np.where(higgs_jet_n_high == 0)
higgs_jet_0_index_high = higgs_jet_0_index_high[0]
higgs_jet_0_index_low = np.where(higgs_jet_n_low == 0)
higgs_jet_0_index_low = higgs_jet_0_index_low[0]


higgs_inv_mass_0jet = np.take(higgs_inv_mass,higgs_jet_0_index)
higgs_met_0jet = np.take(higgs_met,higgs_jet_0_index)
higgs_weight_0jet = np.take(higgs_weight,higgs_jet_0_index)
higgs_total_charge_0jet = np.take(higgs_total_charge,higgs_jet_0_index)


higgs_inv_mass_high_0jet = np.take(higgs_inv_mass_high,higgs_jet_0_index_high)
higgs_weight_high_0jet = np.take(higgs_weight_high,higgs_jet_0_index_high)
higgs_total_charge_high_0jet = np.take(higgs_total_charge_high,higgs_jet_0_index_high)

higgs_inv_mass_low_0jet = np.take(higgs_inv_mass_low,higgs_jet_0_index_low)
higgs_weight_low_0jet = np.take(higgs_weight_low,higgs_jet_0_index_low)
higgs_total_charge_low_0jet = np.take(higgs_total_charge_low,higgs_jet_0_index_low)


#only states where eeem or emmm and 0 bjets

higgs_bjet_0em3_index = np.where(higgs_bjet_n_em3 == 0)
higgs_bjet_0em3_index = higgs_bjet_0em3_index[0]
higgs_bjet_0em3_index_high = np.where(higgs_bjet_n_high_em3 == 0)
higgs_bjet_0em3_index_high = higgs_bjet_0em3_index_high[0]
higgs_bjet_0em3_index_low = np.where(higgs_bjet_n_low_em3 == 0)
higgs_bjet_0em3_index_low = higgs_bjet_0em3_index_low[0]


higgs_inv_mass_0em3 = np.take(higgs_inv_mass_em3,higgs_bjet_0em3_index)
higgs_met_0em3 = np.take(higgs_met_em3,higgs_bjet_0em3_index)
higgs_weight_0em3 = np.take(higgs_weight_em3,higgs_bjet_0em3_index)
#higgs_dilep_mass_0em3 = np.take(higgs_dilep_mass_em3,higgs_bjet_0em3_index)
higgs_total_charge_0em3 = np.take(higgs_total_charge_em3,higgs_bjet_0em3_index)
higgs_jet_n_0em3 = np.take(higgs_jet_n_em3,higgs_bjet_0em3_index)

higgs_inv_mass_high_0em3 = np.take(higgs_inv_mass_high_em3,higgs_bjet_0em3_index_high)
higgs_weight_high_0em3 = np.take(higgs_weight_high_em3,higgs_bjet_0em3_index_high)
#higgs_dilep_mass_high_0em3 = np.take(higgs_dilep_mass_high_em3,higgs_bjet_0em3_index_high)
higgs_total_charge_high_0em3 = np.take(higgs_total_charge_high_em3,higgs_bjet_0em3_index_high)
higgs_jet_n_high_0em3 = np.take(higgs_jet_n_high_em3,higgs_bjet_0em3_index_high)

higgs_inv_mass_low_0em3 = np.take(higgs_inv_mass_low_em3,higgs_bjet_0em3_index_low)
higgs_weight_low_0em3 = np.take(higgs_weight_low_em3,higgs_bjet_0em3_index_low)
#higgs_dilep_mass_low_0em3 = np.take(higgs_dilep_mass_low_em3,higgs_bjet_0em3_index_low)
higgs_total_charge_low_0em3 = np.take(higgs_total_charge_low_em3,higgs_bjet_0em3_index_low)
higgs_jet_n_low_0em3 = np.take(higgs_jet_n_low_em3,higgs_bjet_0em3_index_low)

higgs_electron_mt_0em3 = np.take(higgs_electron_mt_em3,higgs_bjet_0em3_index)
higgs_muon_mt_0em3 = np.take(higgs_muon_mt_em3,higgs_bjet_0em3_index)

higgs_electron_mt_high_0em3 = np.take(higgs_electron_mt_high_em3,higgs_bjet_0em3_index_high)
higgs_muon_mt_high_0em3 = np.take(higgs_muon_mt_high_em3,higgs_bjet_0em3_index_high)

higgs_electron_mt_low_0em3 = np.take(higgs_electron_mt_low_em3,higgs_bjet_0em3_index_low)
higgs_muon_mt_low_0em3 = np.take(higgs_muon_mt_low_em3,higgs_bjet_0em3_index_low)

higgs_single_mt_0b = np.take(higgs_single_mt,higgs_bjet_0em3_index)
higgs_single_mt_high_0b = np.take(higgs_single_mt_high,higgs_bjet_0em3_index_high)
higgs_single_mt_low_0b = np.take(higgs_single_mt_low,higgs_bjet_0em3_index_low)

#division based on total charge

higgs_charge0_index = np.where(higgs_total_charge == 0)
higgs_charge0_index = higgs_charge0_index[0]
higgs_charge0_index_high = np.where(higgs_total_charge_high == 0)
higgs_charge0_index_high = higgs_charge0_index_high[0]
higgs_charge0_index_low = np.where(higgs_total_charge_low == 0)
higgs_charge0_index_low = higgs_charge0_index_low[0]

higgs_inv_mass_charge0 = np.take(higgs_inv_mass,higgs_charge0_index)
higgs_met_charge0 = np.take(higgs_met,higgs_charge0_index)
higgs_weight_charge0 = np.take(higgs_weight,higgs_charge0_index)
higgs_jet_n_charge0 = np.take(higgs_jet_n,higgs_charge0_index)
higgs_electron_mt_charge0 = np.take(higgs_electron_mt,higgs_charge0_index)
higgs_muon_mt_charge0 = np.take(higgs_muon_mt,higgs_charge0_index)

higgs_inv_mass_charge0_high = np.take(higgs_inv_mass_high,higgs_charge0_index_high)
higgs_weight_charge0_high = np.take(higgs_weight_high,higgs_charge0_index_high)
higgs_jet_n_charge0_high = np.take(higgs_jet_n_high,higgs_charge0_index_high)
higgs_electron_mt_charge0_high = np.take(higgs_electron_mt_high,higgs_charge0_index_high)
higgs_muon_mt_charge0_high = np.take(higgs_muon_mt_high,higgs_charge0_index_high)

higgs_inv_mass_charge0_low = np.take(higgs_inv_mass_low,higgs_charge0_index_low)
higgs_weight_charge0_low = np.take(higgs_weight_low,higgs_charge0_index_low)
higgs_jet_n_charge0_low = np.take(higgs_jet_n_low,higgs_charge0_index_low)
higgs_electron_mt_charge0_low = np.take(higgs_electron_mt_low,higgs_charge0_index_low)
higgs_muon_mt_charge0_low = np.take(higgs_muon_mt_low,higgs_charge0_index_low)


higgs_charge2_index = np.where(higgs_total_charge == 2)
higgs_charge2_index = higgs_charge2_index[0]
higgs_charge2_index_high = np.where(higgs_total_charge_high == 2)
higgs_charge2_index_high = higgs_charge2_index_high[0]
higgs_charge2_index_low = np.where(higgs_total_charge_low == 2)
higgs_charge2_index_low = higgs_charge2_index_low[0]

higgs_inv_mass_charge2 = np.take(higgs_inv_mass,higgs_charge2_index)
higgs_met_charge2 = np.take(higgs_met,higgs_charge2_index)
higgs_weight_charge2 = np.take(higgs_weight,higgs_charge2_index)
higgs_jet_n_charge2 = np.take(higgs_jet_n,higgs_charge2_index)
higgs_electron_mt_charge2 = np.take(higgs_electron_mt,higgs_charge2_index)
higgs_muon_mt_charge2 = np.take(higgs_muon_mt,higgs_charge2_index)

higgs_inv_mass_charge2_high = np.take(higgs_inv_mass_high,higgs_charge2_index_high)
higgs_weight_charge2_high = np.take(higgs_weight_high,higgs_charge2_index_high)
higgs_jet_n_charge2_high = np.take(higgs_jet_n_high,higgs_charge2_index_high)
higgs_electron_mt_charge2_high = np.take(higgs_electron_mt_high,higgs_charge2_index_high)
higgs_muon_mt_charge2_high = np.take(higgs_muon_mt_high,higgs_charge2_index_high)

higgs_inv_mass_charge2_low = np.take(higgs_inv_mass_low,higgs_charge2_index_low)
higgs_weight_charge2_low = np.take(higgs_weight_low,higgs_charge2_index_low)
higgs_jet_n_charge2_low = np.take(higgs_jet_n_low,higgs_charge2_index_low)
higgs_electron_mt_charge2_low = np.take(higgs_electron_mt_low,higgs_charge2_index_low)
higgs_muon_mt_charge2_low = np.take(higgs_muon_mt_low,higgs_charge2_index_low)


higgs_charge2min_index = np.where(higgs_total_charge == -2)
higgs_charge2min_index = higgs_charge2min_index[0]
higgs_charge2min_index_high = np.where(higgs_total_charge_high == -2)
higgs_charge2min_index_high = higgs_charge2min_index_high[0]
higgs_charge2min_index_low = np.where(higgs_total_charge_low == -2)
higgs_charge2min_index_low = higgs_charge2min_index_low[0]

higgs_inv_mass_charge2min = np.take(higgs_inv_mass,higgs_charge2min_index)
higgs_met_charge2min = np.take(higgs_met,higgs_charge2min_index)
higgs_weight_charge2min = np.take(higgs_weight,higgs_charge2min_index)
higgs_jet_n_charge2min = np.take(higgs_jet_n,higgs_charge2min_index)
higgs_electron_mt_charge2min = np.take(higgs_electron_mt,higgs_charge2min_index)
higgs_muon_mt_charge2min = np.take(higgs_muon_mt,higgs_charge2min_index)

higgs_inv_mass_charge2min_high = np.take(higgs_inv_mass_high,higgs_charge2min_index_high)
higgs_weight_charge2min_high = np.take(higgs_weight_high,higgs_charge2min_index_high)
higgs_jet_n_charge2min_high = np.take(higgs_jet_n_high,higgs_charge2min_index_high)
higgs_electron_mt_charge2min_high = np.take(higgs_electron_mt_high,higgs_charge2min_index_high)
higgs_muon_mt_charge2min_high = np.take(higgs_muon_mt_high,higgs_charge2min_index_high)

higgs_inv_mass_charge2min_low = np.take(higgs_inv_mass_low,higgs_charge2min_index_low)
higgs_weight_charge2min_low = np.take(higgs_weight_low,higgs_charge2min_index_low)
higgs_jet_n_charge2min_low = np.take(higgs_jet_n_low,higgs_charge2min_index_low)
higgs_electron_mt_charge2min_low = np.take(higgs_electron_mt_low,higgs_charge2min_index_low)
higgs_muon_mt_charge2min_low = np.take(higgs_muon_mt_low,higgs_charge2min_index_low)

# charge division of em3 states

higgs_charge0_index_em3 = np.where(higgs_total_charge_em3 == 0)
higgs_charge0_index_em3 = higgs_charge0_index_em3[0]
higgs_charge0_index_high_em3 = np.where(higgs_total_charge_high_em3 == 0)
higgs_charge0_index_high_em3 = higgs_charge0_index_high_em3[0]
higgs_charge0_index_low_em3 = np.where(higgs_total_charge_low_em3 == 0)
higgs_charge0_index_low_em3 = higgs_charge0_index_low_em3[0]

higgs_inv_mass_charge0_em3 = np.take(higgs_inv_mass_em3,higgs_charge0_index_em3)
higgs_met_charge0_em3 = np.take(higgs_met_em3,higgs_charge0_index_em3)
higgs_weight_charge0_em3 = np.take(higgs_weight_em3,higgs_charge0_index_em3)
higgs_jet_n_charge0_em3 = np.take(higgs_jet_n_em3,higgs_charge0_index_em3)
higgs_single_mt_charge0_em3 = np.take(higgs_single_mt,higgs_charge0_index_em3)

higgs_inv_mass_charge0_high_em3 = np.take(higgs_inv_mass_high_em3,higgs_charge0_index_high_em3)
higgs_weight_charge0_high_em3 = np.take(higgs_weight_high_em3,higgs_charge0_index_high_em3)
higgs_jet_n_charge0_high_em3 = np.take(higgs_jet_n_high_em3,higgs_charge0_index_high_em3)
higgs_single_mt_charge0_high_em3 = np.take(higgs_single_mt_high,higgs_charge0_index_high_em3)

higgs_inv_mass_charge0_low_em3 = np.take(higgs_inv_mass_low_em3,higgs_charge0_index_low_em3)
higgs_weight_charge0_low_em3 = np.take(higgs_weight_low_em3,higgs_charge0_index_low_em3)
higgs_jet_n_charge0_low_em3 = np.take(higgs_jet_n_low_em3,higgs_charge0_index_low_em3)
higgs_single_mt_charge0_low_em3 = np.take(higgs_single_mt_low,higgs_charge0_index_low_em3)


higgs_charge2_index_em3 = np.where(higgs_total_charge_em3 == 2)
higgs_charge2_index_em3 = higgs_charge2_index_em3[0]
higgs_charge2_index_high_em3 = np.where(higgs_total_charge_high_em3 == 2)
higgs_charge2_index_high_em3 = higgs_charge2_index_high_em3[0]
higgs_charge2_index_low_em3 = np.where(higgs_total_charge_low_em3 == 2)
higgs_charge2_index_low_em3 = higgs_charge2_index_low_em3[0]

higgs_inv_mass_charge2_em3 = np.take(higgs_inv_mass_em3,higgs_charge2_index_em3)
higgs_met_charge2_em3 = np.take(higgs_met_em3,higgs_charge2_index_em3)
higgs_weight_charge2_em3 = np.take(higgs_weight_em3,higgs_charge2_index_em3)
higgs_jet_n_charge2_em3 = np.take(higgs_jet_n_em3,higgs_charge2_index_em3)
higgs_single_mt_charge2_em3 = np.take(higgs_single_mt,higgs_charge2_index_em3)

higgs_inv_mass_charge2_high_em3 = np.take(higgs_inv_mass_high_em3,higgs_charge2_index_high_em3)
higgs_weight_charge2_high_em3 = np.take(higgs_weight_high_em3,higgs_charge2_index_high_em3)
higgs_jet_n_charge2_high_em3 = np.take(higgs_jet_n_high_em3,higgs_charge2_index_high_em3)
higgs_single_mt_charge2_high_em3 = np.take(higgs_single_mt_high,higgs_charge2_index_high_em3)

higgs_inv_mass_charge2_low_em3 = np.take(higgs_inv_mass_low_em3,higgs_charge2_index_low_em3)
higgs_weight_charge2_low_em3 = np.take(higgs_weight_low_em3,higgs_charge2_index_low_em3)
higgs_jet_n_charge2_low_em3 = np.take(higgs_jet_n_low_em3,higgs_charge2_index_low_em3)
higgs_single_mt_charge2_low_em3 = np.take(higgs_single_mt_low,higgs_charge2_index_low_em3)


higgs_charge2min_index_em3 = np.where(higgs_total_charge_em3 == -2)
higgs_charge2min_index_em3 = higgs_charge2min_index_em3[0]
higgs_charge2min_index_high_em3 = np.where(higgs_total_charge_high_em3 == -2)
higgs_charge2min_index_high_em3 = higgs_charge2min_index_high_em3[0]
higgs_charge2min_index_low_em3 = np.where(higgs_total_charge_low_em3 == -2)
higgs_charge2min_index_low_em3 = higgs_charge2min_index_low_em3[0]

higgs_inv_mass_charge2min_em3 = np.take(higgs_inv_mass_em3,higgs_charge2min_index_em3)
higgs_met_charge2min_em3 = np.take(higgs_met_em3,higgs_charge2min_index_em3)
higgs_weight_charge2min_em3 = np.take(higgs_weight_em3,higgs_charge2min_index_em3)
higgs_jet_n_charge2min_em3 = np.take(higgs_jet_n_em3,higgs_charge2min_index_em3)
higgs_single_mt_charge2min_em3 = np.take(higgs_single_mt,higgs_charge2min_index_em3)

higgs_inv_mass_charge2min_high_em3 = np.take(higgs_inv_mass_high_em3,higgs_charge2min_index_high_em3)
higgs_weight_charge2min_high_em3 = np.take(higgs_weight_high_em3,higgs_charge2min_index_high_em3)
higgs_jet_n_charge2min_high_em3 = np.take(higgs_jet_n_high_em3,higgs_charge2min_index_high_em3)
higgs_single_mt_charge2min_high_em3 = np.take(higgs_single_mt_high,higgs_charge2min_index_high_em3)

higgs_inv_mass_charge2min_low_em3 = np.take(higgs_inv_mass_low_em3,higgs_charge2min_index_low_em3)
higgs_weight_charge2min_low_em3 = np.take(higgs_weight_low_em3,higgs_charge2min_index_low_em3)
higgs_jet_n_charge2min_low_em3 = np.take(higgs_jet_n_low_em3,higgs_charge2min_index_low_em3)
higgs_single_mt_charge2min_low_em3 = np.take(higgs_single_mt_low,higgs_charge2min_index_low_em3)


#higgs relevant selection

n=0
index = np.empty(0)
while n < len(higgs_electron_charge):

    temp1 = higgs_electron_charge[n]
    temp2 = higgs_muon_charge[n]

    num = higgs_electron_n[n]

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


double_higgs_index = index.astype('int64')

double_higgs_inv_mass = np.take(higgs_inv_mass,double_higgs_index)
double_higgs_met = np.take(higgs_met,double_higgs_index)
double_higgs_weight = np.take(higgs_weight,double_higgs_index)
#double_higgs_dilep_mass = np.take(higgs_dilep_mass,double_higgs_index)
double_higgs_electron_n = np.take(higgs_electron_n,double_higgs_index)
double_higgs_muon_n = np.take(higgs_muon_n,double_higgs_index)
double_higgs_electron_charge = np.take(higgs_electron_charge,double_higgs_index)
double_higgs_muon_charge = np.take(higgs_muon_charge,double_higgs_index)
double_higgs_jet_n = np.take(higgs_jet_n,double_higgs_index)
double_higgs_jet_btag = np.take(higgs_jet_btag,double_higgs_index)
double_higgs_electron_mt = np.take(higgs_electron_mt,double_higgs_index)
double_higgs_muon_mt = np.take(higgs_muon_mt,double_higgs_index)
