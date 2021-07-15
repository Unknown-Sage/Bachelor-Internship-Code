#inv_mass_cut

#imdataindex = np.where(data_inv_mass < 400)
#imdataindex = imdataindex[0]

#data_inv_mass = np.take(data_inv_mass,imdataindex)
#data_met = np.take(data_met,imdataindex)
#data_weight = np.take(data_weight,imdataindex)
#data_dilep_mass = np.take(data_dilep_mass,imdataindex)
#data_electron_n = np.take(data_electron_n,imdataindex)
#data_muon_n = np.take(data_muon_n,imdataindex)
#data_electron_charge = np.take(data_electron_charge,imdataindex)
#data_muon_charge = np.take(data_muon_charge,imdataindex)
#data_jet_n = np.take(data_jet_n,imdataindex)
#data_jet_btag = np.take(data_jet_btag,imdataindex)
#data_muononz = np.take(data_muononz,imdataindex)
#data_electrononz = np.take(data_electrononz,imdataindex)
#data_electron_mt = np.take(data_electron_mt,imdataindex)
#data_muon_mt = np.take(data_muon_mt,imdataindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(data_electrononz):

    array = np.concatenate((data_electrononz[n],data_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

dataindex = index.astype('int64')

data_inv_mass = np.take(data_inv_mass,dataindex)
data_met = np.take(data_met,dataindex)
data_weight = np.take(data_weight,dataindex)
data_dilep_mass = np.take(data_dilep_mass,dataindex)
data_electron_n = np.take(data_electron_n,dataindex)
data_muon_n = np.take(data_muon_n,dataindex)
data_electron_charge = np.take(data_electron_charge,dataindex)
data_muon_charge = np.take(data_muon_charge,dataindex)
data_jet_n = np.take(data_jet_n,dataindex)
data_jet_btag = np.take(data_jet_btag,dataindex)
data_electron_mt = np.take(data_electron_mt,dataindex)
data_muon_mt = np.take(data_muon_mt,dataindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(data_jet_btag):

    array = data_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

data_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(data_electron_charge):

    temp1 = data_electron_charge[n]
    temp2 = data_muon_charge[n]

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

data_total_charge = temp


#add high or low missing transverse energy groups

dataindexlow = np.where(data_met < 50)
dataindexlow = dataindexlow[0]
dataindexhigh = np.where(data_met > 50)
dataindexhigh = dataindexhigh[0]


data_inv_mass_high = np.take(data_inv_mass,dataindexhigh)
data_weight_high = np.take(data_weight,dataindexhigh)
data_dilep_mass_high = np.take(data_dilep_mass,dataindexhigh)
data_electron_n_high = np.take(data_electron_n,dataindexhigh)
data_muon_n_high = np.take(data_muon_n,dataindexhigh)
data_total_charge_high = np.take(data_total_charge,dataindexhigh)
data_jet_n_high = np.take(data_jet_n,dataindexhigh)
data_bjet_n_high = np.take(data_bjet_n,dataindexhigh)

data_electron_mt_high = np.take(data_electron_mt,dataindexhigh)
data_muon_mt_high = np.take(data_muon_mt,dataindexhigh)


data_inv_mass_low = np.take(data_inv_mass,dataindexlow)
data_weight_low = np.take(data_weight,dataindexlow)
data_dilep_mass_low = np.take(data_dilep_mass,dataindexlow)
data_electron_n_low = np.take(data_electron_n,dataindexlow)
data_muon_n_low = np.take(data_muon_n,dataindexlow)
data_total_charge_low = np.take(data_total_charge,dataindexlow)
data_jet_n_low = np.take(data_jet_n,dataindexlow)
data_bjet_n_low = np.take(data_bjet_n,dataindexlow)

data_electron_mt_low = np.take(data_electron_mt,dataindexlow)
data_muon_mt_low = np.take(data_muon_mt,dataindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(data_electron_mt):

    array = np.concatenate((data_electron_mt[n],data_muon_mt[n]))
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

data_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
data_total_mt_weight = np.concatenate((data_weight,data_weight,data_weight,data_weight))

n = 0
temp = np.empty((4,0))
while n < len(data_electron_mt_high):

    array = np.concatenate((data_electron_mt_high[n],data_muon_mt_high[n]))
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

data_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
data_total_mt_weight_high = np.concatenate((data_weight_high,data_weight_high,data_weight_high,data_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(data_electron_mt_low):

    array = np.concatenate((data_electron_mt_low[n],data_muon_mt_low[n]))
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

data_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
data_total_mt_weight_low = np.concatenate((data_weight_low,data_weight_low,data_weight_low,data_weight_low))

#get only emmm or eeem end states

dataindexm3 = np.where(data_electron_n == 1)
dataindexe3 = np.where(data_electron_n == 3)
dataindexm3 = dataindexm3[0]
dataindexe3 = dataindexe3[0]
dataindexem3 = np.concatenate((dataindexm3,dataindexe3))
dataindexem3 = np.sort(dataindexem3)

dataindexhighm3 = np.where(data_electron_n_high == 1)
dataindexhighe3 = np.where(data_electron_n_high == 3)
dataindexhighm3 = dataindexhighm3[0]
dataindexhighe3 = dataindexhighe3[0]
dataindexhighem3 = np.concatenate((dataindexhighm3,dataindexhighe3))
dataindexhighem3 = np.sort(dataindexhighem3)

dataindexlowm3 = np.where(data_electron_n_low == 1)
dataindexlowe3 = np.where(data_electron_n_low == 3)
dataindexlowm3 = dataindexlowm3[0]
dataindexlowe3 = dataindexlowe3[0]
dataindexlowem3 = np.concatenate((dataindexlowm3,dataindexlowe3))
dataindexlowem3 = np.sort(dataindexlowem3)

data_inv_mass_em3 = np.take(data_inv_mass,dataindexem3)
data_met_em3 = np.take(data_met,dataindexem3)
data_weight_em3 = np.take(data_weight,dataindexem3)
data_dilep_mass_em3 = np.take(data_dilep_mass,dataindexem3)
data_total_charge_em3 = np.take(data_total_charge,dataindexem3)
data_jet_n_em3 = np.take(data_jet_n,dataindexem3)
data_bjet_n_em3 = np.take(data_bjet_n,dataindexem3)

data_electron_mt_em3 = np.take(data_electron_mt,dataindexem3)
data_muon_mt_em3 = np.take(data_muon_mt,dataindexem3)

data_inv_mass_high_em3 = np.take(data_inv_mass_high,dataindexhighem3)
data_weight_high_em3 = np.take(data_weight_high,dataindexhighem3)
data_dilep_mass_high_em3 = np.take(data_dilep_mass_high,dataindexhighem3)
data_total_charge_high_em3 = np.take(data_total_charge_high,dataindexhighem3)
data_jet_n_high_em3 = np.take(data_jet_n_high,dataindexhighem3)
data_bjet_n_high_em3 = np.take(data_bjet_n_high,dataindexhighem3)

data_electron_mt_high_em3 = np.take(data_electron_mt_high,dataindexhighem3)
data_muon_mt_high_em3 = np.take(data_muon_mt_high,dataindexhighem3)

data_inv_mass_low_em3 = np.take(data_inv_mass_low,dataindexlowem3)
data_weight_low_em3 = np.take(data_weight_low,dataindexlowem3)
data_dilep_mass_low_em3 = np.take(data_dilep_mass_low,dataindexlowem3)
data_total_charge_low_em3 = np.take(data_total_charge_low,dataindexlowem3)
data_jet_n_low_em3 = np.take(data_jet_n_low,dataindexlowem3)
data_bjet_n_low_em3 = np.take(data_bjet_n_low,dataindexlowem3)

data_electron_mt_low_em3 = np.take(data_electron_mt_low,dataindexlowem3)
data_muon_mt_low_em3 = np.take(data_muon_mt_low,dataindexlowem3)

n = 0
temp = np.empty(0)
while n < len(data_electron_mt_em3):

    array1 = data_electron_mt_em3[n]
    array2 = data_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

data_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(data_electron_mt_low_em3):

    array1 = data_electron_mt_low_em3[n]
    array2 = data_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

data_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(data_electron_mt_high_em3):

    array1 = data_electron_mt_high_em3[n]
    array2 = data_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

data_single_mt_high = temp

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(data_dilep_mass_em3):

    array = data_dilep_mass_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

data_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
data_weight_dilep_em3 = np.concatenate((data_weight_em3,data_weight_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(data_dilep_mass_high_em3):

    array = data_dilep_mass_high_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

data_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
data_weight_dilep_high_em3 = np.concatenate((data_weight_high_em3,data_weight_high_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(data_dilep_mass_low_em3):

    array = data_dilep_mass_low_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

data_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
data_weight_dilep_low_em3 = np.concatenate((data_weight_low_em3,data_weight_low_em3))

#only states with 0 jets

data_jet_0_index = np.where(data_jet_n == 0)
data_jet_0_index = data_jet_0_index[0]
data_jet_0_index_high = np.where(data_jet_n_high == 0)
data_jet_0_index_high = data_jet_0_index_high[0]
data_jet_0_index_low = np.where(data_jet_n_low == 0)
data_jet_0_index_low = data_jet_0_index_low[0]


data_inv_mass_0jet = np.take(data_inv_mass,data_jet_0_index)
data_met_0jet = np.take(data_met,data_jet_0_index)
data_weight_0jet = np.take(data_weight,data_jet_0_index)
data_total_charge_0jet = np.take(data_total_charge,data_jet_0_index)


data_inv_mass_high_0jet = np.take(data_inv_mass_high,data_jet_0_index_high)
data_weight_high_0jet = np.take(data_weight_high,data_jet_0_index_high)
data_total_charge_high_0jet = np.take(data_total_charge_high,data_jet_0_index_high)

data_inv_mass_low_0jet = np.take(data_inv_mass_low,data_jet_0_index_low)
data_weight_low_0jet = np.take(data_weight_low,data_jet_0_index_low)
data_total_charge_low_0jet = np.take(data_total_charge_low,data_jet_0_index_low)


#only states where eeem or emmm and 0 jets

data_bjet_0em3_index = np.where(data_bjet_n_em3 == 0)
data_bjet_0em3_index = data_bjet_0em3_index[0]
data_bjet_0em3_index_high = np.where(data_bjet_n_high_em3 == 0)
data_bjet_0em3_index_high = data_bjet_0em3_index_high[0]
data_bjet_0em3_index_low = np.where(data_bjet_n_low_em3 == 0)
data_bjet_0em3_index_low = data_bjet_0em3_index_low[0]


data_inv_mass_0em3 = np.take(data_inv_mass_em3,data_bjet_0em3_index)
data_met_0em3 = np.take(data_met_em3,data_bjet_0em3_index)
data_weight_0em3 = np.take(data_weight_em3,data_bjet_0em3_index)
data_dilep_mass_0em3 = np.take(data_dilep_mass_em3,data_bjet_0em3_index)
data_total_charge_0em3 = np.take(data_total_charge_em3,data_bjet_0em3_index)
data_jet_n_0em3 = np.take(data_jet_n_em3,data_bjet_0em3_index)

data_inv_mass_high_0em3 = np.take(data_inv_mass_high_em3,data_bjet_0em3_index_high)
data_weight_high_0em3 = np.take(data_weight_high_em3,data_bjet_0em3_index_high)
data_dilep_mass_high_0em3 = np.take(data_dilep_mass_high_em3,data_bjet_0em3_index_high)
data_total_charge_high_0em3 = np.take(data_total_charge_high_em3,data_bjet_0em3_index_high)
data_jet_n_high_0em3 = np.take(data_jet_n_high_em3,data_bjet_0em3_index_high)

data_inv_mass_low_0em3 = np.take(data_inv_mass_low_em3,data_bjet_0em3_index_low)
data_weight_low_0em3 = np.take(data_weight_low_em3,data_bjet_0em3_index_low)
data_dilep_mass_low_0em3 = np.take(data_dilep_mass_low_em3,data_bjet_0em3_index_low)
data_total_charge_low_0em3 = np.take(data_total_charge_low_em3,data_bjet_0em3_index_low)
data_jet_n_low_0em3 = np.take(data_jet_n_low_em3,data_bjet_0em3_index_low)

data_electron_mt_0em3 = np.take(data_electron_mt_em3,data_bjet_0em3_index)
data_muon_mt_0em3 = np.take(data_muon_mt_em3,data_bjet_0em3_index)

data_electron_mt_high_0em3 = np.take(data_electron_mt_high_em3,data_bjet_0em3_index_high)
data_muon_mt_high_0em3 = np.take(data_muon_mt_high_em3,data_bjet_0em3_index_high)

data_electron_mt_low_0em3 = np.take(data_electron_mt_low_em3,data_bjet_0em3_index_low)
data_muon_mt_low_0em3 = np.take(data_muon_mt_low_em3,data_bjet_0em3_index_low)

data_single_mt_0b = np.take(data_single_mt,data_bjet_0em3_index)
data_single_mt_high_0b = np.take(data_single_mt_high,data_bjet_0em3_index_high)
data_single_mt_low_0b = np.take(data_single_mt_low,data_bjet_0em3_index_low)

#division based on total charge

data_charge0_index = np.where(data_total_charge == 0)
data_charge0_index = data_charge0_index[0]
data_charge0_index_high = np.where(data_total_charge_high == 0)
data_charge0_index_high = data_charge0_index_high[0]
data_charge0_index_low = np.where(data_total_charge_low == 0)
data_charge0_index_low = data_charge0_index_low[0]

data_inv_mass_charge0 = np.take(data_inv_mass,data_charge0_index)
data_met_charge0 = np.take(data_met,data_charge0_index)
data_weight_charge0 = np.take(data_weight,data_charge0_index)
data_jet_n_charge0 = np.take(data_jet_n,data_charge0_index)
data_electron_mt_charge0 = np.take(data_electron_mt,data_charge0_index)
data_muon_mt_charge0 = np.take(data_muon_mt,data_charge0_index)

data_inv_mass_charge0_high = np.take(data_inv_mass_high,data_charge0_index_high)
data_weight_charge0_high = np.take(data_weight_high,data_charge0_index_high)
data_jet_n_charge0_high = np.take(data_jet_n_high,data_charge0_index_high)
data_electron_mt_charge0_high = np.take(data_electron_mt_high,data_charge0_index_high)
data_muon_mt_charge0_high = np.take(data_muon_mt_high,data_charge0_index_high)

data_inv_mass_charge0_low = np.take(data_inv_mass_low,data_charge0_index_low)
data_weight_charge0_low = np.take(data_weight_low,data_charge0_index_low)
data_jet_n_charge0_low = np.take(data_jet_n_low,data_charge0_index_low)
data_electron_mt_charge0_low = np.take(data_electron_mt_low,data_charge0_index_low)
data_muon_mt_charge0_low = np.take(data_muon_mt_low,data_charge0_index_low)


data_charge2_index = np.where(data_total_charge == 2)
data_charge2_index = data_charge2_index[0]
data_charge2_index_high = np.where(data_total_charge_high == 2)
data_charge2_index_high = data_charge2_index_high[0]
data_charge2_index_low = np.where(data_total_charge_low == 2)
data_charge2_index_low = data_charge2_index_low[0]

data_inv_mass_charge2 = np.take(data_inv_mass,data_charge2_index)
data_met_charge2 = np.take(data_met,data_charge2_index)
data_weight_charge2 = np.take(data_weight,data_charge2_index)
data_jet_n_charge2 = np.take(data_jet_n,data_charge2_index)
data_electron_mt_charge2 = np.take(data_electron_mt,data_charge2_index)
data_muon_mt_charge2 = np.take(data_muon_mt,data_charge2_index)

data_inv_mass_charge2_high = np.take(data_inv_mass_high,data_charge2_index_high)
data_weight_charge2_high = np.take(data_weight_high,data_charge2_index_high)
data_jet_n_charge2_high = np.take(data_jet_n_high,data_charge2_index_high)
data_electron_mt_charge2_high = np.take(data_electron_mt_high,data_charge2_index_high)
data_muon_mt_charge2_high = np.take(data_muon_mt_high,data_charge2_index_high)

data_inv_mass_charge2_low = np.take(data_inv_mass_low,data_charge2_index_low)
data_weight_charge2_low = np.take(data_weight_low,data_charge2_index_low)
data_jet_n_charge2_low = np.take(data_jet_n_low,data_charge2_index_low)
data_electron_mt_charge2_low = np.take(data_electron_mt_low,data_charge2_index_low)
data_muon_mt_charge2_low = np.take(data_muon_mt_low,data_charge2_index_low)


data_charge2min_index = np.where(data_total_charge == -2)
data_charge2min_index = data_charge2min_index[0]
data_charge2min_index_high = np.where(data_total_charge_high == -2)
data_charge2min_index_high = data_charge2min_index_high[0]
data_charge2min_index_low = np.where(data_total_charge_low == -2)
data_charge2min_index_low = data_charge2min_index_low[0]

data_inv_mass_charge2min = np.take(data_inv_mass,data_charge2min_index)
data_met_charge2min = np.take(data_met,data_charge2min_index)
data_weight_charge2min = np.take(data_weight,data_charge2min_index)
data_jet_n_charge2min = np.take(data_jet_n,data_charge2min_index)
data_electron_mt_charge2min = np.take(data_electron_mt,data_charge2min_index)
data_muon_mt_charge2min = np.take(data_muon_mt,data_charge2min_index)

data_inv_mass_charge2min_high = np.take(data_inv_mass_high,data_charge2min_index_high)
data_weight_charge2min_high = np.take(data_weight_high,data_charge2min_index_high)
data_jet_n_charge2min_high = np.take(data_jet_n_high,data_charge2min_index_high)
data_electron_mt_charge2min_high = np.take(data_electron_mt_high,data_charge2min_index_high)
data_muon_mt_charge2min_high = np.take(data_muon_mt_high,data_charge2min_index_high)

data_inv_mass_charge2min_low = np.take(data_inv_mass_low,data_charge2min_index_low)
data_weight_charge2min_low = np.take(data_weight_low,data_charge2min_index_low)
data_jet_n_charge2min_low = np.take(data_jet_n_low,data_charge2min_index_low)
data_electron_mt_charge2min_low = np.take(data_electron_mt_low,data_charge2min_index_low)
data_muon_mt_charge2min_low = np.take(data_muon_mt_low,data_charge2min_index_low)

# charge division of em3 states

data_charge0_index_em3 = np.where(data_total_charge_em3 == 0)
data_charge0_index_em3 = data_charge0_index_em3[0]
data_charge0_index_high_em3 = np.where(data_total_charge_high_em3 == 0)
data_charge0_index_high_em3 = data_charge0_index_high_em3[0]
data_charge0_index_low_em3 = np.where(data_total_charge_low_em3 == 0)
data_charge0_index_low_em3 = data_charge0_index_low_em3[0]

data_inv_mass_charge0_em3 = np.take(data_inv_mass_em3,data_charge0_index_em3)
data_met_charge0_em3 = np.take(data_met_em3,data_charge0_index_em3)
data_weight_charge0_em3 = np.take(data_weight_em3,data_charge0_index_em3)
data_jet_n_charge0_em3 = np.take(data_jet_n_em3,data_charge0_index_em3)
data_single_mt_charge0_em3 = np.take(data_single_mt,data_charge0_index_em3)

data_inv_mass_charge0_high_em3 = np.take(data_inv_mass_high_em3,data_charge0_index_high_em3)
data_weight_charge0_high_em3 = np.take(data_weight_high_em3,data_charge0_index_high_em3)
data_jet_n_charge0_high_em3 = np.take(data_jet_n_high_em3,data_charge0_index_high_em3)
data_single_mt_charge0_high_em3 = np.take(data_single_mt_high,data_charge0_index_high_em3)

data_inv_mass_charge0_low_em3 = np.take(data_inv_mass_low_em3,data_charge0_index_low_em3)
data_weight_charge0_low_em3 = np.take(data_weight_low_em3,data_charge0_index_low_em3)
data_jet_n_charge0_low_em3 = np.take(data_jet_n_low_em3,data_charge0_index_low_em3)
data_single_mt_charge0_low_em3 = np.take(data_single_mt_low,data_charge0_index_low_em3)


data_charge2_index_em3 = np.where(data_total_charge_em3 == 2)
data_charge2_index_em3 = data_charge2_index_em3[0]
data_charge2_index_high_em3 = np.where(data_total_charge_high_em3 == 2)
data_charge2_index_high_em3 = data_charge2_index_high_em3[0]
data_charge2_index_low_em3 = np.where(data_total_charge_low_em3 == 2)
data_charge2_index_low_em3 = data_charge2_index_low_em3[0]

data_inv_mass_charge2_em3 = np.take(data_inv_mass_em3,data_charge2_index_em3)
data_met_charge2_em3 = np.take(data_met_em3,data_charge2_index_em3)
data_weight_charge2_em3 = np.take(data_weight_em3,data_charge2_index_em3)
data_jet_n_charge2_em3 = np.take(data_jet_n_em3,data_charge2_index_em3)
data_single_mt_charge2_em3 = np.take(data_single_mt,data_charge2_index_em3)

data_inv_mass_charge2_high_em3 = np.take(data_inv_mass_high_em3,data_charge2_index_high_em3)
data_weight_charge2_high_em3 = np.take(data_weight_high_em3,data_charge2_index_high_em3)
data_jet_n_charge2_high_em3 = np.take(data_jet_n_high_em3,data_charge2_index_high_em3)
data_single_mt_charge2_high_em3 = np.take(data_single_mt_high,data_charge2_index_high_em3)

data_inv_mass_charge2_low_em3 = np.take(data_inv_mass_low_em3,data_charge2_index_low_em3)
data_weight_charge2_low_em3 = np.take(data_weight_low_em3,data_charge2_index_low_em3)
data_jet_n_charge2_low_em3 = np.take(data_jet_n_low_em3,data_charge2_index_low_em3)
data_single_mt_charge2_low_em3 = np.take(data_single_mt_low,data_charge2_index_low_em3)


data_charge2min_index_em3 = np.where(data_total_charge_em3 == -2)
data_charge2min_index_em3 = data_charge2min_index_em3[0]
data_charge2min_index_high_em3 = np.where(data_total_charge_high_em3 == -2)
data_charge2min_index_high_em3 = data_charge2min_index_high_em3[0]
data_charge2min_index_low_em3 = np.where(data_total_charge_low_em3 == -2)
data_charge2min_index_low_em3 = data_charge2min_index_low_em3[0]

data_inv_mass_charge2min_em3 = np.take(data_inv_mass_em3,data_charge2min_index_em3)
data_met_charge2min_em3 = np.take(data_met_em3,data_charge2min_index_em3)
data_weight_charge2min_em3 = np.take(data_weight_em3,data_charge2min_index_em3)
data_jet_n_charge2min_em3 = np.take(data_jet_n_em3,data_charge2min_index_em3)
data_single_mt_charge2min_em3 = np.take(data_single_mt,data_charge2min_index_em3)

data_inv_mass_charge2min_high_em3 = np.take(data_inv_mass_high_em3,data_charge2min_index_high_em3)
data_weight_charge2min_high_em3 = np.take(data_weight_high_em3,data_charge2min_index_high_em3)
data_jet_n_charge2min_high_em3 = np.take(data_jet_n_high_em3,data_charge2min_index_high_em3)
data_single_mt_charge2min_high_em3 = np.take(data_single_mt_high,data_charge2min_index_high_em3)

data_inv_mass_charge2min_low_em3 = np.take(data_inv_mass_low_em3,data_charge2min_index_low_em3)
data_weight_charge2min_low_em3 = np.take(data_weight_low_em3,data_charge2min_index_low_em3)
data_jet_n_charge2min_low_em3 = np.take(data_jet_n_low_em3,data_charge2min_index_low_em3)
data_single_mt_charge2min_low_em3 = np.take(data_single_mt_low,data_charge2min_index_low_em3)

#higgs relevant selection

n=0
index = np.empty(0)
while n < len(data_electron_charge):

    temp1 = data_electron_charge[n]
    temp2 = data_muon_charge[n]

    num = data_electron_n[n]

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


data_higgs_index = index.astype('int64')

data_higgs_inv_mass = np.take(data_inv_mass,data_higgs_index)
data_higgs_met = np.take(data_met,data_higgs_index)
data_higgs_weight = np.take(data_weight,data_higgs_index)
#data_higgs_dilep_mass = np.take(data_dilep_mass,data_higgs_index)
data_higgs_electron_n = np.take(data_electron_n,data_higgs_index)
data_higgs_muon_n = np.take(data_muon_n,data_higgs_index)
data_higgs_electron_charge = np.take(data_electron_charge,data_higgs_index)
data_higgs_muon_charge = np.take(data_muon_charge,data_higgs_index)
data_higgs_jet_n = np.take(data_jet_n,data_higgs_index)
data_higgs_jet_btag = np.take(data_jet_btag,data_higgs_index)
data_higgs_electron_mt = np.take(data_electron_mt,data_higgs_index)
data_higgs_muon_mt = np.take(data_muon_mt,data_higgs_index)
