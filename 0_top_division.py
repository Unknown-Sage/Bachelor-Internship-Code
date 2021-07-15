#inv_mass_cut

#imtopindex = np.where(top_inv_mass < 400)
#imtopindex = imtopindex[0]

#top_inv_mass = np.take(top_inv_mass,imtopindex)
#top_met = np.take(top_met,imtopindex)
#top_weight = np.take(top_weight,imtopindex)
#top_dilep_mass = np.take(top_dilep_mass,imtopindex)
#top_electron_n = np.take(top_electron_n,imtopindex)
#top_muon_n = np.take(top_muon_n,imtopindex)
#top_electron_charge = np.take(top_electron_charge,imtopindex)
#top_muon_charge = np.take(top_muon_charge,imtopindex)
#top_jet_n = np.take(top_jet_n,imtopindex)
#top_jet_btag = np.take(top_jet_btag,imtopindex)
#top_muononz = np.take(top_muononz,imtopindex)
#top_electrononz = np.take(top_electrononz,imtopindex)
#top_electron_mt = np.take(top_electron_mt,imtopindex)
#top_muon_mt = np.take(top_muon_mt,imtopindex)

#not 4 leptons with onZ = true

n = 0
index = np.empty(0)
while n < len(top_electrononz):

    array = np.concatenate((top_electrononz[n],top_muononz[n]))

    test = np.where(array == True)

    if len(test[0]) != 4: #and len(test[0]) > 2:
        index = np.concatenate((index,[int(n)]))

    n = n+1

topindex = index.astype('int64')

top_inv_mass = np.take(top_inv_mass,topindex)
top_met = np.take(top_met,topindex)
top_weight = np.take(top_weight,topindex)
top_dilep_mass = np.take(top_dilep_mass,topindex)
top_electron_n = np.take(top_electron_n,topindex)
top_muon_n = np.take(top_muon_n,topindex)
top_electron_charge = np.take(top_electron_charge,topindex)
top_muon_charge = np.take(top_muon_charge,topindex)
top_jet_n = np.take(top_jet_n,topindex)
top_jet_btag = np.take(top_jet_btag,topindex)
top_electron_mt = np.take(top_electron_mt,topindex)
top_muon_mt = np.take(top_muon_mt,topindex)


#number of bjets

n = 0
temp = np.empty(0)
while n < len(top_jet_btag):

    array = top_jet_btag[n]

    test = np.where(array == True)
    test = test[0]
    array = [len(test)]

    temp = np.concatenate((temp,array))
    
    n = n+1

top_bjet_n = temp.astype('int64')

#calculate total charge

n=0
temp = np.empty(0)
while n < len(top_electron_charge):

    temp1 = top_electron_charge[n]
    temp2 = top_muon_charge[n]

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

top_total_charge = temp


#add high or low missing transverse energy groups

topindexlow = np.where(top_met < 50)
topindexlow = topindexlow[0]
topindexhigh = np.where(top_met > 50)
topindexhigh = topindexhigh[0]


top_inv_mass_high = np.take(top_inv_mass,topindexhigh)
top_weight_high = np.take(top_weight,topindexhigh)
top_dilep_mass_high = np.take(top_dilep_mass,topindexhigh)
top_electron_n_high = np.take(top_electron_n,topindexhigh)
top_muon_n_high = np.take(top_muon_n,topindexhigh)
top_total_charge_high = np.take(top_total_charge,topindexhigh)
top_jet_n_high = np.take(top_jet_n,topindexhigh)
top_bjet_n_high = np.take(top_bjet_n,topindexhigh)

top_electron_mt_high = np.take(top_electron_mt,topindexhigh)
top_muon_mt_high = np.take(top_muon_mt,topindexhigh)


top_inv_mass_low = np.take(top_inv_mass,topindexlow)
top_weight_low = np.take(top_weight,topindexlow)
top_dilep_mass_low = np.take(top_dilep_mass,topindexlow)
top_electron_n_low = np.take(top_electron_n,topindexlow)
top_muon_n_low = np.take(top_muon_n,topindexlow)
top_total_charge_low = np.take(top_total_charge,topindexlow)
top_jet_n_low = np.take(top_jet_n,topindexlow)
top_bjet_n_low = np.take(top_bjet_n,topindexlow)

top_electron_mt_low = np.take(top_electron_mt,topindexlow)
top_muon_mt_low = np.take(top_muon_mt,topindexlow)

#merging transverse mass arrays

n = 0
temp = np.empty((4,0))
while n < len(top_electron_mt):

    array = np.concatenate((top_electron_mt[n],top_muon_mt[n]))
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

top_total_mt = np.concatenate((temp1,temp2,temp3,temp4))
top_total_mt_weight = np.concatenate((top_weight,top_weight,top_weight,top_weight))

n = 0
temp = np.empty((4,0))
while n < len(top_electron_mt_high):

    array = np.concatenate((top_electron_mt_high[n],top_muon_mt_high[n]))
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

top_total_mt_high = np.concatenate((temp1,temp2,temp3,temp4))
top_total_mt_weight_high = np.concatenate((top_weight_high,top_weight_high,top_weight_high,top_weight_high))

n = 0
temp = np.empty((4,0))
while n < len(top_electron_mt_low):

    array = np.concatenate((top_electron_mt_low[n],top_muon_mt_low[n]))
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

top_total_mt_low = np.concatenate((temp1,temp2,temp3,temp4))
top_total_mt_weight_low = np.concatenate((top_weight_low,top_weight_low,top_weight_low,top_weight_low))

#get only emmm or eeem end states

topindexm3 = np.where(top_electron_n == 1)
topindexe3 = np.where(top_electron_n == 3)
topindexm3 = topindexm3[0]
topindexe3 = topindexe3[0]
topindexem3 = np.concatenate((topindexm3,topindexe3))
topindexem3 = np.sort(topindexem3)

topindexhighm3 = np.where(top_electron_n_high == 1)
topindexhighe3 = np.where(top_electron_n_high == 3)
topindexhighm3 = topindexhighm3[0]
topindexhighe3 = topindexhighe3[0]
topindexhighem3 = np.concatenate((topindexhighm3,topindexhighe3))
topindexhighem3 = np.sort(topindexhighem3)

topindexlowm3 = np.where(top_electron_n_low == 1)
topindexlowe3 = np.where(top_electron_n_low == 3)
topindexlowm3 = topindexlowm3[0]
topindexlowe3 = topindexlowe3[0]
topindexlowem3 = np.concatenate((topindexlowm3,topindexlowe3))
topindexlowem3 = np.sort(topindexlowem3)

top_inv_mass_em3 = np.take(top_inv_mass,topindexem3)
top_met_em3 = np.take(top_met,topindexem3)
top_weight_em3 = np.take(top_weight,topindexem3)
top_dilep_mass_em3 = np.take(top_dilep_mass,topindexem3)
top_total_charge_em3 = np.take(top_total_charge,topindexem3)
top_jet_n_em3 = np.take(top_jet_n,topindexem3)
top_bjet_n_em3 = np.take(top_bjet_n,topindexem3)

top_electron_mt_em3 = np.take(top_electron_mt,topindexem3)
top_muon_mt_em3 = np.take(top_muon_mt,topindexem3)

top_inv_mass_high_em3 = np.take(top_inv_mass_high,topindexhighem3)
top_weight_high_em3 = np.take(top_weight_high,topindexhighem3)
top_dilep_mass_high_em3 = np.take(top_dilep_mass_high,topindexhighem3)
top_total_charge_high_em3 = np.take(top_total_charge_high,topindexhighem3)
top_jet_n_high_em3 = np.take(top_jet_n_high,topindexhighem3)
top_bjet_n_high_em3 = np.take(top_bjet_n_high,topindexhighem3)

top_electron_mt_high_em3 = np.take(top_electron_mt_high,topindexhighem3)
top_muon_mt_high_em3 = np.take(top_muon_mt_high,topindexhighem3)

top_inv_mass_low_em3 = np.take(top_inv_mass_low,topindexlowem3)
top_weight_low_em3 = np.take(top_weight_low,topindexlowem3)
top_dilep_mass_low_em3 = np.take(top_dilep_mass_low,topindexlowem3)
top_total_charge_low_em3 = np.take(top_total_charge_low,topindexlowem3)
top_jet_n_low_em3 = np.take(top_jet_n_low,topindexlowem3)
top_bjet_n_low_em3 = np.take(top_bjet_n_low,topindexlowem3)

top_electron_mt_low_em3 = np.take(top_electron_mt_low,topindexlowem3)
top_muon_mt_low_em3 = np.take(top_muon_mt_low,topindexlowem3)

n = 0
temp = np.empty(0)
while n < len(top_electron_mt_em3):

    array1 = top_electron_mt_em3[n]
    array2 = top_muon_mt_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

top_single_mt = temp

n = 0
temp = np.empty(0)
while n < len(top_electron_mt_low_em3):

    array1 = top_electron_mt_low_em3[n]
    array2 = top_muon_mt_low_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

top_single_mt_low = temp

n = 0
temp = np.empty(0)
while n < len(top_electron_mt_high_em3):

    array1 = top_electron_mt_high_em3[n]
    array2 = top_muon_mt_high_em3[n]

    if len(array1) == 1:
        temp = np.concatenate((temp,array1))
    if len(array2) == 1:
        temp = np.concatenate((temp,array2))
    
    n = n+1

top_single_mt_high = temp

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(top_dilep_mass_em3):

    array = top_dilep_mass_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

top_dilep_mass_new_em3 = np.concatenate((temp1,temp2))
top_weight_dilep_em3 = np.concatenate((top_weight_em3,top_weight_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(top_dilep_mass_high_em3):

    array = top_dilep_mass_high_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

top_dilep_mass_new_high_em3 = np.concatenate((temp1,temp2))
top_weight_dilep_high_em3 = np.concatenate((top_weight_high_em3,top_weight_high_em3))

n = 0
temp1 = np.empty(0)
temp2 = np.empty(0)
while n < len(top_dilep_mass_low_em3):

    array = top_dilep_mass_low_em3[n]
    temp1 = np.concatenate((temp1,[array[0]]))
    temp2 = np.concatenate((temp2,[array[1]]))

    n = n+1

top_dilep_mass_new_low_em3 = np.concatenate((temp1,temp2))
top_weight_dilep_low_em3 = np.concatenate((top_weight_low_em3,top_weight_low_em3))

#only states with 0 jets

top_jet_0_index = np.where(top_jet_n == 0)
top_jet_0_index = top_jet_0_index[0]
top_jet_0_index_high = np.where(top_jet_n_high == 0)
top_jet_0_index_high = top_jet_0_index_high[0]
top_jet_0_index_low = np.where(top_jet_n_low == 0)
top_jet_0_index_low = top_jet_0_index_low[0]


top_inv_mass_0jet = np.take(top_inv_mass,top_jet_0_index)
top_met_0jet = np.take(top_met,top_jet_0_index)
top_weight_0jet = np.take(top_weight,top_jet_0_index)
top_total_charge_0jet = np.take(top_total_charge,top_jet_0_index)


top_inv_mass_high_0jet = np.take(top_inv_mass_high,top_jet_0_index_high)
top_weight_high_0jet = np.take(top_weight_high,top_jet_0_index_high)
top_total_charge_high_0jet = np.take(top_total_charge_high,top_jet_0_index_high)

top_inv_mass_low_0jet = np.take(top_inv_mass_low,top_jet_0_index_low)
top_weight_low_0jet = np.take(top_weight_low,top_jet_0_index_low)
top_total_charge_low_0jet = np.take(top_total_charge_low,top_jet_0_index_low)

#only states where eeem or emmm and 0 bjets

top_bjet_0em3_index = np.where(top_bjet_n_em3 == 0)
top_bjet_0em3_index = top_bjet_0em3_index[0]
top_bjet_0em3_index_high = np.where(top_bjet_n_high_em3 == 0)
top_bjet_0em3_index_high = top_bjet_0em3_index_high[0]
top_bjet_0em3_index_low = np.where(top_bjet_n_low_em3 == 0)
top_bjet_0em3_index_low = top_bjet_0em3_index_low[0]


top_inv_mass_0em3 = np.take(top_inv_mass_em3,top_bjet_0em3_index)
top_met_0em3 = np.take(top_met_em3,top_bjet_0em3_index)
top_weight_0em3 = np.take(top_weight_em3,top_bjet_0em3_index)
top_dilep_mass_0em3 = np.take(top_dilep_mass_em3,top_bjet_0em3_index)
top_total_charge_0em3 = np.take(top_total_charge_em3,top_bjet_0em3_index)
top_jet_n_0em3 = np.take(top_jet_n_em3,top_bjet_0em3_index)

top_inv_mass_high_0em3 = np.take(top_inv_mass_high_em3,top_bjet_0em3_index_high)
top_weight_high_0em3 = np.take(top_weight_high_em3,top_bjet_0em3_index_high)
top_dilep_mass_high_0em3 = np.take(top_dilep_mass_high_em3,top_bjet_0em3_index_high)
top_total_charge_high_0em3 = np.take(top_total_charge_high_em3,top_bjet_0em3_index_high)
top_jet_n_high_0em3 = np.take(top_jet_n_high_em3,top_bjet_0em3_index_high)

top_inv_mass_low_0em3 = np.take(top_inv_mass_low_em3,top_bjet_0em3_index_low)
top_weight_low_0em3 = np.take(top_weight_low_em3,top_bjet_0em3_index_low)
top_dilep_mass_low_0em3 = np.take(top_dilep_mass_low_em3,top_bjet_0em3_index_low)
top_total_charge_low_0em3 = np.take(top_total_charge_low_em3,top_bjet_0em3_index_low)
top_jet_n_low_0em3 = np.take(top_jet_n_low_em3,top_bjet_0em3_index_low)

top_electron_mt_0em3 = np.take(top_electron_mt_em3,top_bjet_0em3_index)
top_muon_mt_0em3 = np.take(top_muon_mt_em3,top_bjet_0em3_index)

top_electron_mt_high_0em3 = np.take(top_electron_mt_high_em3,top_bjet_0em3_index_high)
top_muon_mt_high_0em3 = np.take(top_muon_mt_high_em3,top_bjet_0em3_index_high)

top_electron_mt_low_0em3 = np.take(top_electron_mt_low_em3,top_bjet_0em3_index_low)
top_muon_mt_low_0em3 = np.take(top_muon_mt_low_em3,top_bjet_0em3_index_low)

top_single_mt_0b = np.take(top_single_mt,top_bjet_0em3_index)
top_single_mt_high_0b = np.take(top_single_mt_high,top_bjet_0em3_index_high)
top_single_mt_low_0b = np.take(top_single_mt_low,top_bjet_0em3_index_low)

#division based on total charge

top_charge0_index = np.where(top_total_charge == 0)
top_charge0_index = top_charge0_index[0]
top_charge0_index_high = np.where(top_total_charge_high == 0)
top_charge0_index_high = top_charge0_index_high[0]
top_charge0_index_low = np.where(top_total_charge_low == 0)
top_charge0_index_low = top_charge0_index_low[0]

top_inv_mass_charge0 = np.take(top_inv_mass,top_charge0_index)
top_met_charge0 = np.take(top_met,top_charge0_index)
top_weight_charge0 = np.take(top_weight,top_charge0_index)
top_jet_n_charge0 = np.take(top_jet_n,top_charge0_index)
top_electron_mt_charge0 = np.take(top_electron_mt,top_charge0_index)
top_muon_mt_charge0 = np.take(top_muon_mt,top_charge0_index)

top_inv_mass_charge0_high = np.take(top_inv_mass_high,top_charge0_index_high)
top_weight_charge0_high = np.take(top_weight_high,top_charge0_index_high)
top_jet_n_charge0_high = np.take(top_jet_n_high,top_charge0_index_high)
top_electron_mt_charge0_high = np.take(top_electron_mt_high,top_charge0_index_high)
top_muon_mt_charge0_high = np.take(top_muon_mt_high,top_charge0_index_high)

top_inv_mass_charge0_low = np.take(top_inv_mass_low,top_charge0_index_low)
top_weight_charge0_low = np.take(top_weight_low,top_charge0_index_low)
top_jet_n_charge0_low = np.take(top_jet_n_low,top_charge0_index_low)
top_electron_mt_charge0_low = np.take(top_electron_mt_low,top_charge0_index_low)
top_muon_mt_charge0_low = np.take(top_muon_mt_low,top_charge0_index_low)


top_charge2_index = np.where(top_total_charge == 2)
top_charge2_index = top_charge2_index[0]
top_charge2_index_high = np.where(top_total_charge_high == 2)
top_charge2_index_high = top_charge2_index_high[0]
top_charge2_index_low = np.where(top_total_charge_low == 2)
top_charge2_index_low = top_charge2_index_low[0]

top_inv_mass_charge2 = np.take(top_inv_mass,top_charge2_index)
top_met_charge2 = np.take(top_met,top_charge2_index)
top_weight_charge2 = np.take(top_weight,top_charge2_index)
top_jet_n_charge2 = np.take(top_jet_n,top_charge2_index)
top_electron_mt_charge2 = np.take(top_electron_mt,top_charge2_index)
top_muon_mt_charge2 = np.take(top_muon_mt,top_charge2_index)

top_inv_mass_charge2_high = np.take(top_inv_mass_high,top_charge2_index_high)
top_weight_charge2_high = np.take(top_weight_high,top_charge2_index_high)
top_jet_n_charge2_high = np.take(top_jet_n_high,top_charge2_index_high)
top_electron_mt_charge2_high = np.take(top_electron_mt_high,top_charge2_index_high)
top_muon_mt_charge2_high = np.take(top_muon_mt_high,top_charge2_index_high)

top_inv_mass_charge2_low = np.take(top_inv_mass_low,top_charge2_index_low)
top_weight_charge2_low = np.take(top_weight_low,top_charge2_index_low)
top_jet_n_charge2_low = np.take(top_jet_n_low,top_charge2_index_low)
top_electron_mt_charge2_low = np.take(top_electron_mt_low,top_charge2_index_low)
top_muon_mt_charge2_low = np.take(top_muon_mt_low,top_charge2_index_low)


top_charge2min_index = np.where(top_total_charge == -2)
top_charge2min_index = top_charge2min_index[0]
top_charge2min_index_high = np.where(top_total_charge_high == -2)
top_charge2min_index_high = top_charge2min_index_high[0]
top_charge2min_index_low = np.where(top_total_charge_low == -2)
top_charge2min_index_low = top_charge2min_index_low[0]

top_inv_mass_charge2min = np.take(top_inv_mass,top_charge2min_index)
top_met_charge2min = np.take(top_met,top_charge2min_index)
top_weight_charge2min = np.take(top_weight,top_charge2min_index)
top_jet_n_charge2min = np.take(top_jet_n,top_charge2min_index)
top_electron_mt_charge2min = np.take(top_electron_mt,top_charge2min_index)
top_muon_mt_charge2min = np.take(top_muon_mt,top_charge2min_index)

top_inv_mass_charge2min_high = np.take(top_inv_mass_high,top_charge2min_index_high)
top_weight_charge2min_high = np.take(top_weight_high,top_charge2min_index_high)
top_jet_n_charge2min_high = np.take(top_jet_n_high,top_charge2min_index_high)
top_electron_mt_charge2min_high = np.take(top_electron_mt_high,top_charge2min_index_high)
top_muon_mt_charge2min_high = np.take(top_muon_mt_high,top_charge2min_index_high)

top_inv_mass_charge2min_low = np.take(top_inv_mass_low,top_charge2min_index_low)
top_weight_charge2min_low = np.take(top_weight_low,top_charge2min_index_low)
top_jet_n_charge2min_low = np.take(top_jet_n_low,top_charge2min_index_low)
top_electron_mt_charge2min_low = np.take(top_electron_mt_low,top_charge2min_index_low)
top_muon_mt_charge2min_low = np.take(top_muon_mt_low,top_charge2min_index_low)

# charge division of em3 states

top_charge0_index_em3 = np.where(top_total_charge_em3 == 0)
top_charge0_index_em3 = top_charge0_index_em3[0]
top_charge0_index_high_em3 = np.where(top_total_charge_high_em3 == 0)
top_charge0_index_high_em3 = top_charge0_index_high_em3[0]
top_charge0_index_low_em3 = np.where(top_total_charge_low_em3 == 0)
top_charge0_index_low_em3 = top_charge0_index_low_em3[0]

top_inv_mass_charge0_em3 = np.take(top_inv_mass_em3,top_charge0_index_em3)
top_met_charge0_em3 = np.take(top_met_em3,top_charge0_index_em3)
top_weight_charge0_em3 = np.take(top_weight_em3,top_charge0_index_em3)
top_jet_n_charge0_em3 = np.take(top_jet_n_em3,top_charge0_index_em3)
top_single_mt_charge0_em3 = np.take(top_single_mt,top_charge0_index_em3)

top_inv_mass_charge0_high_em3 = np.take(top_inv_mass_high_em3,top_charge0_index_high_em3)
top_weight_charge0_high_em3 = np.take(top_weight_high_em3,top_charge0_index_high_em3)
top_jet_n_charge0_high_em3 = np.take(top_jet_n_high_em3,top_charge0_index_high_em3)
top_single_mt_charge0_high_em3 = np.take(top_single_mt_high,top_charge0_index_high_em3)

top_inv_mass_charge0_low_em3 = np.take(top_inv_mass_low_em3,top_charge0_index_low_em3)
top_weight_charge0_low_em3 = np.take(top_weight_low_em3,top_charge0_index_low_em3)
top_jet_n_charge0_low_em3 = np.take(top_jet_n_low_em3,top_charge0_index_low_em3)
top_single_mt_charge0_low_em3 = np.take(top_single_mt_low,top_charge0_index_low_em3)


top_charge2_index_em3 = np.where(top_total_charge_em3 == 2)
top_charge2_index_em3 = top_charge2_index_em3[0]
top_charge2_index_high_em3 = np.where(top_total_charge_high_em3 == 2)
top_charge2_index_high_em3 = top_charge2_index_high_em3[0]
top_charge2_index_low_em3 = np.where(top_total_charge_low_em3 == 2)
top_charge2_index_low_em3 = top_charge2_index_low_em3[0]

top_inv_mass_charge2_em3 = np.take(top_inv_mass_em3,top_charge2_index_em3)
top_met_charge2_em3 = np.take(top_met_em3,top_charge2_index_em3)
top_weight_charge2_em3 = np.take(top_weight_em3,top_charge2_index_em3)
top_jet_n_charge2_em3 = np.take(top_jet_n_em3,top_charge2_index_em3)
top_single_mt_charge2_em3 = np.take(top_single_mt,top_charge2_index_em3)

top_inv_mass_charge2_high_em3 = np.take(top_inv_mass_high_em3,top_charge2_index_high_em3)
top_weight_charge2_high_em3 = np.take(top_weight_high_em3,top_charge2_index_high_em3)
top_jet_n_charge2_high_em3 = np.take(top_jet_n_high_em3,top_charge2_index_high_em3)
top_single_mt_charge2_high_em3 = np.take(top_single_mt_high,top_charge2_index_high_em3)

top_inv_mass_charge2_low_em3 = np.take(top_inv_mass_low_em3,top_charge2_index_low_em3)
top_weight_charge2_low_em3 = np.take(top_weight_low_em3,top_charge2_index_low_em3)
top_jet_n_charge2_low_em3 = np.take(top_jet_n_low_em3,top_charge2_index_low_em3)
top_single_mt_charge2_low_em3 = np.take(top_single_mt_low,top_charge2_index_low_em3)


top_charge2min_index_em3 = np.where(top_total_charge_em3 == -2)
top_charge2min_index_em3 = top_charge2min_index_em3[0]
top_charge2min_index_high_em3 = np.where(top_total_charge_high_em3 == -2)
top_charge2min_index_high_em3 = top_charge2min_index_high_em3[0]
top_charge2min_index_low_em3 = np.where(top_total_charge_low_em3 == -2)
top_charge2min_index_low_em3 = top_charge2min_index_low_em3[0]

top_inv_mass_charge2min_em3 = np.take(top_inv_mass_em3,top_charge2min_index_em3)
top_met_charge2min_em3 = np.take(top_met_em3,top_charge2min_index_em3)
top_weight_charge2min_em3 = np.take(top_weight_em3,top_charge2min_index_em3)
top_jet_n_charge2min_em3 = np.take(top_jet_n_em3,top_charge2min_index_em3)
top_single_mt_charge2min_em3 = np.take(top_single_mt,top_charge2min_index_em3)

top_inv_mass_charge2min_high_em3 = np.take(top_inv_mass_high_em3,top_charge2min_index_high_em3)
top_weight_charge2min_high_em3 = np.take(top_weight_high_em3,top_charge2min_index_high_em3)
top_jet_n_charge2min_high_em3 = np.take(top_jet_n_high_em3,top_charge2min_index_high_em3)
top_single_mt_charge2min_high_em3 = np.take(top_single_mt_high,top_charge2min_index_high_em3)

top_inv_mass_charge2min_low_em3 = np.take(top_inv_mass_low_em3,top_charge2min_index_low_em3)
top_weight_charge2min_low_em3 = np.take(top_weight_low_em3,top_charge2min_index_low_em3)
top_jet_n_charge2min_low_em3 = np.take(top_jet_n_low_em3,top_charge2min_index_low_em3)
top_single_mt_charge2min_low_em3 = np.take(top_single_mt_low,top_charge2min_index_low_em3)


#higgs relevant selection

n=0
index = np.empty(0)
while n < len(top_electron_charge):

    temp1 = top_electron_charge[n]
    temp2 = top_muon_charge[n]

    num = top_electron_n[n]

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


top_higgs_index = index.astype('int64')

top_higgs_inv_mass = np.take(top_inv_mass,top_higgs_index)
top_higgs_met = np.take(top_met,top_higgs_index)
top_higgs_weight = np.take(top_weight,top_higgs_index)
#top_higgs_dilep_mass = np.take(top_dilep_mass,top_higgs_index)
top_higgs_electron_n = np.take(top_electron_n,top_higgs_index)
top_higgs_muon_n = np.take(top_muon_n,top_higgs_index)
top_higgs_electron_charge = np.take(top_electron_charge,top_higgs_index)
top_higgs_muon_charge = np.take(top_muon_charge,top_higgs_index)
top_higgs_jet_n = np.take(top_jet_n,top_higgs_index)
top_higgs_jet_btag = np.take(top_jet_btag,top_higgs_index)
top_higgs_electron_mt = np.take(top_electron_mt,top_higgs_index)
top_higgs_muon_mt = np.take(top_muon_mt,top_higgs_index)
