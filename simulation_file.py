import numpy as np
import matplotlib.pyplot as plt
import uproot
import yaml


intluma = 36*1000000
intlumd = 43.5*1000000
intlume = 59*1000000

#Triboson simulations

simtriboson1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364243_0.MC16a.root')
simtriboson1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364243_0.MC16d.root')
simtriboson1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364243_0.MC16e.root')

simtribosona1 = simtriboson1a['Nominal/BaseSelection_tree_Final']
simtribosona1cutflow = simtriboson1a['Nominal/cutflow_DxAOD']
temp = simtribosona1cutflow.values()
simtribosona1numsimvalue = temp[1]

simtribosona1weight = simtribosona1['weight'].array(library='np')

simtribosond1 = simtriboson1d['Nominal/BaseSelection_tree_Final']
simtribosond1cutflow = simtriboson1d['Nominal/cutflow_DxAOD']
temp = simtribosond1cutflow.values()
simtribosond1numsimvalue = temp[1]

simtribosond1weight = simtribosond1['weight'].array(library='np')

simtribosone1 = simtriboson1e['Nominal/BaseSelection_tree_Final']
simtribosone1cutflow = simtriboson1e['Nominal/cutflow_DxAOD']
temp = simtribosone1cutflow.values()
simtribosone1numsimvalue = temp[1]

simtribosone1weight = simtribosone1['weight'].array(library='np')

weightfactortri1a = intluma*1.797/1000000/simtribosona1numsimvalue

weightfactortri1d = intlumd*1.797/1000000/simtribosond1numsimvalue
weightfactortri1e = intlume*1.797/1000000/simtribosone1numsimvalue

tribosonweight1a = simtribosona1weight*weightfactortri1a

tribosonweight1d = simtribosond1weight*weightfactortri1d
tribosonweight1e = simtribosone1weight*weightfactortri1e

tribosonweight1 = np.concatenate((tribosonweight1a,tribosonweight1d,tribosonweight1e))

simtriboson2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364245_0.MC16a.root')
simtriboson2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364245_0.MC16d.root')
simtriboson2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364245_0.MC16e.root')

simtribosona2 = simtriboson2a['Nominal/BaseSelection_tree_Final']
simtribosona2cutflow = simtriboson2a['Nominal/cutflow_DxAOD']
temp = simtribosona2cutflow.values()
simtribosona2numsimvalue = temp[1]

simtribosona2weight = simtribosona2['weight'].array(library='np')

simtribosond2 = simtriboson2d['Nominal/BaseSelection_tree_Final']
simtribosond2cutflow = simtriboson2d['Nominal/cutflow_DxAOD']
temp = simtribosond2cutflow.values()
simtribosond2numsimvalue = temp[1]

simtribosond2weight = simtribosond2['weight'].array(library='np')

simtribosone2 = simtriboson2e['Nominal/BaseSelection_tree_Final']
simtribosone2cutflow = simtriboson2e['Nominal/cutflow_DxAOD']
temp = simtribosone2cutflow.values()
simtribosone2numsimvalue = temp[1]

simtribosone2weight = simtribosone2['weight'].array(library='np')

weightfactortri2a = intluma*1.8805/10000000/simtribosona2numsimvalue

weightfactortri2d = intlumd*1.8805/10000000/simtribosond2numsimvalue
weightfactortri2e = intlume*1.8805/10000000/simtribosone2numsimvalue

tribosonweight2a = simtribosona2weight*weightfactortri2a

tribosonweight2d = simtribosond2weight*weightfactortri2d
tribosonweight2e = simtribosone2weight*weightfactortri2e

tribosonweight2 = np.concatenate((tribosonweight2a,tribosonweight2d,tribosonweight2e))

simtriboson3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364247_0.MC16a.root')
simtriboson3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364247_0.MC16d.root')
simtriboson3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364247_0.MC16e.root')

simtribosona3 = simtriboson3a['Nominal/BaseSelection_tree_Final']
simtribosona3cutflow = simtriboson3a['Nominal/cutflow_DxAOD']
temp = simtribosona3cutflow.values()
simtribosona3numsimvalue = temp[1]

simtribosona3weight = simtribosona3['weight'].array(library='np')

simtribosond3 = simtriboson3d['Nominal/BaseSelection_tree_Final']
simtribosond3cutflow = simtriboson3d['Nominal/cutflow_DxAOD']
temp = simtribosond3cutflow.values()
simtribosond3numsimvalue = temp[1]

simtribosond3weight = simtribosond3['weight'].array(library='np')

simtribosone3 = simtriboson3e['Nominal/BaseSelection_tree_Final']
simtribosone3cutflow = simtriboson3e['Nominal/cutflow_DxAOD']
temp = simtribosone3cutflow.values()
simtribosone3numsimvalue = temp[1]

simtribosone3weight = simtribosone3['weight'].array(library='np')

weightfactortri3a = intluma*1.452/100000000/simtribosona3numsimvalue

weightfactortri3d = intlumd*1.452/100000000/simtribosond3numsimvalue
weightfactortri3e = intlume*1.452/100000000/simtribosone3numsimvalue

tribosonweight3a = simtribosona3weight*weightfactortri3a

tribosonweight3d = simtribosond3weight*weightfactortri3d
tribosonweight3e = simtribosone3weight*weightfactortri3e

tribosonweight3 = np.concatenate((tribosonweight3a,tribosonweight3d,tribosonweight3e))

simtriboson4a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364248_0.MC16a.root')
simtriboson4d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364248_0.MC16d.root')
simtriboson4e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364248_0.MC16e.root')

simtribosona4 = simtriboson4a['Nominal/BaseSelection_tree_Final']
simtribosona4cutflow = simtriboson4a['Nominal/cutflow_DxAOD']
temp = simtribosona4cutflow.values()
simtribosona4numsimvalue = temp[1]

simtribosona4weight = simtribosona4['weight'].array(library='np')

simtribosond4 = simtriboson4d['Nominal/BaseSelection_tree_Final']
simtribosond4cutflow = simtriboson4d['Nominal/cutflow_DxAOD']
temp = simtribosond4cutflow.values()
simtribosond4numsimvalue = temp[1]

simtribosond4weight = simtribosond4['weight'].array(library='np')

simtribosone4 = simtriboson4e['Nominal/BaseSelection_tree_Final']
simtribosone4cutflow = simtriboson4e['Nominal/cutflow_DxAOD']
temp = simtribosone4cutflow.values()
simtribosone4numsimvalue = temp[1]

simtribosone4weight = simtribosone4['weight'].array(library='np')

weightfactortri4a = intluma*0.22453*3.8532/10000000/simtribosona4numsimvalue

weightfactortri4d = intlumd*0.22453*3.8532/10000000/simtribosond4numsimvalue
weightfactortri4e = intlume*0.22453*3.8532/10000000/simtribosone4numsimvalue

tribosonweight4a = simtribosona4weight*weightfactortri4a

tribosonweight4d = simtribosond4weight*weightfactortri4d
tribosonweight4e = simtribosone4weight*weightfactortri4e

tribosonweight4 = np.concatenate((tribosonweight4a,tribosonweight4d,tribosonweight4e))


triboson_weight = np.concatenate((tribosonweight1,tribosonweight2,tribosonweight3,tribosonweight4))

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='inv_mass', library='np')
triboson_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met', library='np')
triboson_met = temp['track_met']
triboson_met = triboson_met/1000

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='dilep_mass', library='np')
triboson_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_n', library='np')
triboson_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_n', library='np')
triboson_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_charge', library='np')
triboson_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_charge', library='np')
triboson_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_n', library='np')
triboson_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_has_btag', library='np')
triboson_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='isOnZ', library='np')
triboson_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_onZ', library='np')
triboson_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_onZ', library='np')
triboson_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_pt', library='np')
triboson_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_eta', library='np')
triboson_electron_eta = temp['electron_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_phi', library='np')
triboson_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_mt', library='np')
triboson_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_pt', library='np')
triboson_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_eta', library='np')
triboson_muon_eta = temp['muon_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_phi', library='np')
triboson_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_mt', library='np')
triboson_muon_mt = temp['muon_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\triboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met_phi', library='np')
triboson_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

tri_index_onz = np.where(triboson_onz == True)
tri_index_onz = tri_index_onz[0]

triboson_inv_mass = np.take(triboson_inv_mass,tri_index_onz)
triboson_met = np.take(triboson_met,tri_index_onz)
triboson_muononz = np.take(triboson_muononz,tri_index_onz)
triboson_electrononz = np.take(triboson_electrononz,tri_index_onz)
triboson_weight = np.take(triboson_weight,tri_index_onz)
triboson_dilep_mass = np.take(triboson_dilep_mass,tri_index_onz)
triboson_electron_n = np.take(triboson_electron_n,tri_index_onz)
triboson_muon_n = np.take(triboson_muon_n,tri_index_onz)
triboson_electron_charge = np.take(triboson_electron_charge,tri_index_onz)
triboson_muon_charge = np.take(triboson_muon_charge,tri_index_onz)
triboson_jet_n = np.take(triboson_jet_n,tri_index_onz)
triboson_jet_btag = np.take(triboson_jet_btag,tri_index_onz)

triboson_electron_pt = np.take(triboson_electron_pt,tri_index_onz)
triboson_electron_eta = np.take(triboson_electron_eta,tri_index_onz)
triboson_electron_phi = np.take(triboson_electron_phi,tri_index_onz)
triboson_electron_mt = np.take(triboson_electron_mt,tri_index_onz)
triboson_muon_pt = np.take(triboson_muon_pt,tri_index_onz)
triboson_muon_eta = np.take(triboson_muon_eta,tri_index_onz)
triboson_muon_phi = np.take(triboson_muon_phi,tri_index_onz)
triboson_muon_mt = np.take(triboson_muon_mt,tri_index_onz)
triboson_met_phi = np.take(triboson_met_phi,tri_index_onz)

#Diboson simulations

simdiboson1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364250_0.MC16a.root')
simdiboson1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364250_0.MC16d.root')
simdiboson1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364250_0.MC16e.root')

simdibosona1 = simdiboson1a['Nominal/BaseSelection_tree_Final']
simdibosona1cutflow = simdiboson1a['Nominal/cutflow_DxAOD']
temp = simdibosona1cutflow.values()
simdibosona1numsimvalue = temp[1]

simdibosona1weight = simdibosona1['weight'].array(library='np')

simdibosond1 = simdiboson1d['Nominal/BaseSelection_tree_Final']
simdibosond1cutflow = simdiboson1d['Nominal/cutflow_DxAOD']
temp = simdibosond1cutflow.values()
simdibosond1numsimvalue = temp[1]

simdibosond1weight = simdibosond1['weight'].array(library='np')

simdibosone1 = simdiboson1e['Nominal/BaseSelection_tree_Final']
simdibosone1cutflow = simdiboson1e['Nominal/cutflow_DxAOD']
temp = simdibosone1cutflow.values()
simdibosone1numsimvalue = temp[1]

simdibosone1weight = simdibosone1['weight'].array(library='np')

weightfactordi1a = intluma*0.0012517/simdibosona1numsimvalue

weightfactordi1d = intlumd*0.0012517/simdibosond1numsimvalue
weightfactordi1e = intlume*0.0012517/simdibosone1numsimvalue

dibosonweight1a = simdibosona1weight*weightfactordi1a

dibosonweight1d = simdibosond1weight*weightfactordi1d
dibosonweight1e = simdibosone1weight*weightfactordi1e

dibosonweight1 = np.concatenate((dibosonweight1a,dibosonweight1d,dibosonweight1e))

simdiboson2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364283_0.MC16a.root')
simdiboson2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364283_0.MC16d.root')
simdiboson2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364283_0.MC16e.root')

simdibosona2 = simdiboson2a['Nominal/BaseSelection_tree_Final']
simdibosona2cutflow = simdiboson2a['Nominal/cutflow_DxAOD']
temp = simdibosona2cutflow.values()
simdibosona2numsimvalue = temp[1]

simdibosona2weight = simdibosona2['weight'].array(library='np')

simdibosond2 = simdiboson2d['Nominal/BaseSelection_tree_Final']
simdibosond2cutflow = simdiboson2d['Nominal/cutflow_DxAOD']
temp = simdibosond2cutflow.values()
simdibosond2numsimvalue = temp[1]

simdibosond2weight = simdibosond2['weight'].array(library='np')

simdibosone2 = simdiboson2e['Nominal/BaseSelection_tree_Final']
simdibosone2cutflow = simdiboson2e['Nominal/cutflow_DxAOD']
temp = simdibosone2cutflow.values()
simdibosone2numsimvalue = temp[1]

simdibosone2weight = simdibosone2['weight'].array(library='np')

weightfactordi2a = intluma*1.058/100000/simdibosona2numsimvalue

weightfactordi2d = intlumd*1.058/100000/simdibosond2numsimvalue
weightfactordi2e = intlume*1.058/100000/simdibosone2numsimvalue

dibosonweight2a = simdibosona2weight*weightfactordi2a

dibosonweight2d = simdibosond2weight*weightfactordi2d
dibosonweight2e = simdibosone2weight*weightfactordi2e

dibosonweight2 = np.concatenate((dibosonweight2a,dibosonweight2d,dibosonweight2e))

simdiboson3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364288_0.MC16a.root')
simdiboson3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364288_0.MC16d.root')
simdiboson3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-364288_0.MC16e.root')

simdibosona3 = simdiboson3a['Nominal/BaseSelection_tree_Final']
simdibosona3cutflow = simdiboson3a['Nominal/cutflow_DxAOD']
temp = simdibosona3cutflow.values()
simdibosona3numsimvalue = temp[1]

simdibosona3weight = simdibosona3['weight'].array(library='np')

simdibosond3 = simdiboson3d['Nominal/BaseSelection_tree_Final']
simdibosond3cutflow = simdiboson3d['Nominal/cutflow_DxAOD']
temp = simdibosond3cutflow.values()
simdibosond3numsimvalue = temp[1]

simdibosond3weight = simdibosond3['weight'].array(library='np')

simdibosone3 = simdiboson3e['Nominal/BaseSelection_tree_Final']
simdibosone3cutflow = simdiboson3e['Nominal/cutflow_DxAOD']
temp = simdibosone3cutflow.values()
simdibosone3numsimvalue = temp[1]

simdibosone3weight = simdibosone3['weight'].array(library='np')

weightfactordi3a = intluma*0.0014496/simdibosona3numsimvalue

weightfactordi3d = intlumd*0.0014496/simdibosond3numsimvalue
weightfactordi3e = intlume*0.0014496/simdibosone3numsimvalue

dibosonweight3a = simdibosona3weight*weightfactordi3a

dibosonweight3d = simdibosond3weight*weightfactordi3d
dibosonweight3e = simdibosone3weight*weightfactordi3e

dibosonweight3 = np.concatenate((dibosonweight3a,dibosonweight3d,dibosonweight3e))

simdiboson4a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345705_0.MC16a.root')
simdiboson4d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345705_0.MC16d.root')
simdiboson4e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345705_0.MC16e.root')

simdibosona4 = simdiboson4a['Nominal/BaseSelection_tree_Final']
simdibosona4cutflow = simdiboson4a['Nominal/cutflow_DxAOD']
temp = simdibosona4cutflow.values()
simdibosona4numsimvalue = temp[1]

simdibosona4weight = simdibosona4['weight'].array(library='np')

simdibosond4 = simdiboson4d['Nominal/BaseSelection_tree_Final']
simdibosond4cutflow = simdiboson4d['Nominal/cutflow_DxAOD']
temp = simdibosond4cutflow.values()
simdibosond4numsimvalue = temp[1]

simdibosond4weight = simdibosond4['weight'].array(library='np')

simdibosone4 = simdiboson4e['Nominal/BaseSelection_tree_Final']
simdibosone4cutflow = simdiboson4e['Nominal/cutflow_DxAOD']
temp = simdibosone4cutflow.values()
simdibosone4numsimvalue = temp[1]

simdibosone4weight = simdibosone4['weight'].array(library='np')

weightfactordi4a = intluma*9.9577/1000000/simdibosona4numsimvalue

weightfactordi4d = intlumd*9.9577/1000000/simdibosond4numsimvalue
weightfactordi4e = intlume*9.9577/1000000/simdibosone4numsimvalue

dibosonweight4a = simdibosona4weight*weightfactordi4a

dibosonweight4d = simdibosond4weight*weightfactordi4d
dibosonweight4e = simdibosone4weight*weightfactordi4e

dibosonweight4 = np.concatenate((dibosonweight4a,dibosonweight4d,dibosonweight4e))

simdiboson5a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345706_0.MC16a.root')
simdiboson5d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345706_0.MC16d.root')
simdiboson5e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-345706_0.MC16e.root')

simdibosona5 = simdiboson5a['Nominal/BaseSelection_tree_Final']
simdibosona5cutflow = simdiboson5a['Nominal/cutflow_DxAOD']
temp = simdibosona5cutflow.values()
simdibosona5numsimvalue = temp[1]

simdibosona5weight = simdibosona5['weight'].array(library='np')

simdibosond5 = simdiboson5d['Nominal/BaseSelection_tree_Final']
simdibosond5cutflow = simdiboson5d['Nominal/cutflow_DxAOD']
temp = simdibosond5cutflow.values()
simdibosond5numsimvalue = temp[1]

simdibosond5weight = simdibosond5['weight'].array(library='np')

simdibosone5 = simdiboson5e['Nominal/BaseSelection_tree_Final']
simdibosone5cutflow = simdiboson5e['Nominal/cutflow_DxAOD']
temp = simdibosone5cutflow.values()
simdibosone5numsimvalue = temp[1]

simdibosone5weight = simdibosone5['weight'].array(library='np')

weightfactordi5a = intluma*1.0076/100000/simdibosona5numsimvalue

weightfactordi5d = intlumd*1.0076/100000/simdibosond5numsimvalue
weightfactordi5e = intlume*1.0076/100000/simdibosone5numsimvalue

dibosonweight5a = simdibosona5weight*weightfactordi5a

dibosonweight5d = simdibosond5weight*weightfactordi5d
dibosonweight5e = simdibosone5weight*weightfactordi5e

dibosonweight5 = np.concatenate((dibosonweight5a,dibosonweight5d,dibosonweight5e))



diboson_weight = np.concatenate((dibosonweight1,dibosonweight2,dibosonweight3,dibosonweight4,dibosonweight5))


temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='inv_mass', library='np')
diboson_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met', library='np')
diboson_met = temp['track_met']
diboson_met = diboson_met/1000

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='dilep_mass', library='np')
diboson_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_n', library='np')
diboson_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_n', library='np')
diboson_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_charge', library='np')
diboson_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_charge', library='np')
diboson_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_n', library='np')
diboson_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_has_btag', library='np')
diboson_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='isOnZ', library='np')
diboson_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_onZ', library='np')
diboson_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_onZ', library='np')
diboson_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_pt', library='np')
diboson_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_eta', library='np')
diboson_electron_eta = temp['electron_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_phi', library='np')
diboson_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_mt', library='np')
diboson_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_pt', library='np')
diboson_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_eta', library='np')
diboson_muon_eta = temp['muon_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_phi', library='np')
diboson_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_mt', library='np')
diboson_muon_mt = temp['muon_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\diboson\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met_phi', library='np')
diboson_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

di_index_onz = np.where(diboson_onz == True)
di_index_onz = di_index_onz[0]

diboson_inv_mass = np.take(diboson_inv_mass,di_index_onz)
diboson_met = np.take(diboson_met,di_index_onz)
diboson_muononz = np.take(diboson_muononz,di_index_onz)
diboson_electrononz = np.take(diboson_electrononz,di_index_onz)
diboson_weight = np.take(diboson_weight,di_index_onz)
diboson_dilep_mass = np.take(diboson_dilep_mass,di_index_onz)
diboson_electron_n = np.take(diboson_electron_n,di_index_onz)
diboson_muon_n = np.take(diboson_muon_n,di_index_onz)
diboson_electron_charge = np.take(diboson_electron_charge,di_index_onz)
diboson_muon_charge = np.take(diboson_muon_charge,di_index_onz)
diboson_jet_n = np.take(diboson_jet_n,di_index_onz)
diboson_jet_btag = np.take(diboson_jet_btag,di_index_onz)

diboson_electron_pt = np.take(diboson_electron_pt,di_index_onz)
diboson_electron_eta = np.take(diboson_electron_eta,di_index_onz)
diboson_electron_phi = np.take(diboson_electron_phi,di_index_onz)
diboson_electron_mt = np.take(diboson_electron_mt,di_index_onz)
diboson_muon_pt = np.take(diboson_muon_pt,di_index_onz)
diboson_muon_eta = np.take(diboson_muon_eta,di_index_onz)
diboson_muon_phi = np.take(diboson_muon_phi,di_index_onz)
diboson_muon_mt = np.take(diboson_muon_mt,di_index_onz)
diboson_met_phi = np.take(diboson_met_phi,di_index_onz)



#Unclear

simwzgamma1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-366160_0.MC16a.root')
simwzgamma1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-366160_0.MC16d.root')
simwzgamma1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-366160_0.MC16e.root')

simtwz1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16a.root')
simtwz1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16d.root')
simtwz1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16e.root')

#alternate Triboson do not use

simtribosonoff1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407311_0.MC16a.root')
simtribosonoff1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407311_0.MC16d.root')
simtribosonoff1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407311_0.MC16e.root')

simtribosonoff2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407312_0.MC16a.root')
simtribosonoff2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407312_0.MC16d.root')
simtribosonoff2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407312_0.MC16e.root')

simtribosonoff3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407313_0.MC16a.root')
simtribosonoff3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407313_0.MC16d.root')
simtribosonoff3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-407313_0.MC16e.root')


#Top simulations

simtop1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410218_0.MC16a.root')
simtop1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410218_0.MC16d.root')
simtop1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410218_0.MC16e.root')

simtopa1 = simtop1a['Nominal/BaseSelection_tree_Final']
simtopa1cutflow = simtop1a['Nominal/cutflow_DxAOD']
temp = simtopa1cutflow.values()
simtopa1numsimvalue = temp[1]

simtopa1weight = simtopa1['weight'].array(library='np')

simtopd1 = simtop1d['Nominal/BaseSelection_tree_Final']
simtopd1cutflow = simtop1d['Nominal/cutflow_DxAOD']
temp = simtopd1cutflow.values()
simtopd1numsimvalue = temp[1]

simtopd1weight = simtopd1['weight'].array(library='np')

simtope1 = simtop1e['Nominal/BaseSelection_tree_Final']
simtope1cutflow = simtop1e['Nominal/cutflow_DxAOD']
temp = simtope1cutflow.values()
simtope1numsimvalue = temp[1]

simtope1weight = simtope1['weight'].array(library='np')

weightfactortop1a = intluma*1.12*3.6864/100000/simtopa1numsimvalue
weightfactortop1d = intlumd*1.12*3.6864/100000/simtopd1numsimvalue
weightfactortop1e = intlume*1.12*3.6864/100000/simtope1numsimvalue

topweight1a = simtopa1weight*weightfactortop1a
topweight1d = simtopd1weight*weightfactortop1d
topweight1e = simtope1weight*weightfactortop1e

topweight1 = np.concatenate((topweight1a,topweight1d,topweight1e))


simtop2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410219_0.MC16a.root')
simtop2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410219_0.MC16d.root')
simtop2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410219_0.MC16e.root')

simtopa2 = simtop2a['Nominal/BaseSelection_tree_Final']
simtopa2cutflow = simtop2a['Nominal/cutflow_DxAOD']
temp = simtopa2cutflow.values()
simtopa2numsimvalue = temp[1]

simtopa2weight = simtopa2['weight'].array(library='np')

simtopd2 = simtop2d['Nominal/BaseSelection_tree_Final']
simtopd2cutflow = simtop2d['Nominal/cutflow_DxAOD']
temp = simtopd2cutflow.values()
simtopd2numsimvalue = temp[1]

simtopd2weight = simtopd2['weight'].array(library='np')

simtope2 = simtop2e['Nominal/BaseSelection_tree_Final']
simtope2cutflow = simtop2e['Nominal/cutflow_DxAOD']
temp = simtope2cutflow.values()
simtope2numsimvalue = temp[1]

simtope2weight = simtope2['weight'].array(library='np')

weightfactortop2a = intluma*1.12*3.6865/100000/simtopa2numsimvalue
weightfactortop2d = intlumd*1.12*3.6865/100000/simtopd2numsimvalue
weightfactortop2e = intlume*1.12*3.6865/100000/simtope2numsimvalue

topweight2a = simtopa2weight*weightfactortop2a
topweight2d = simtopd2weight*weightfactortop2d
topweight2e = simtope2weight*weightfactortop2e

topweight2 = np.concatenate((topweight2a,topweight2d,topweight2e))


simtop3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410220_0.MC16a.root')
simtop3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410220_0.MC16d.root')
simtop3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410220_0.MC16e.root')

simtopa3 = simtop3a['Nominal/BaseSelection_tree_Final']
simtopa3cutflow = simtop3a['Nominal/cutflow_DxAOD']
temp = simtopa3cutflow.values()
simtopa3numsimvalue = temp[1]

simtopa3weight = simtopa3['weight'].array(library='np')

simtopd3 = simtop3d['Nominal/BaseSelection_tree_Final']
simtopd3cutflow = simtop3d['Nominal/cutflow_DxAOD']
temp = simtopd3cutflow.values()
simtopd3numsimvalue = temp[1]

simtopd3weight = simtopd3['weight'].array(library='np')

simtope3 = simtop3e['Nominal/BaseSelection_tree_Final']
simtope3cutflow = simtop3e['Nominal/cutflow_DxAOD']
temp = simtope3cutflow.values()
simtope3numsimvalue = temp[1]

simtope3weight = simtope3['weight'].array(library='np')

weightfactortop3a = intluma*1.12*3.6555/100000/simtopa3numsimvalue
weightfactortop3d = intlumd*1.12*3.6555/100000/simtopd3numsimvalue
weightfactortop3e = intlume*1.12*3.6555/100000/simtope3numsimvalue

topweight3a = simtopa3weight*weightfactortop3a
topweight3d = simtopd3weight*weightfactortop3d
topweight3e = simtope3weight*weightfactortop3e

topweight3 = np.concatenate((topweight3a,topweight3d,topweight3e))


simtopr1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346344_0.MC16a.root')
simtopr1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346344_0.MC16d.root')
simtopr1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346344_0.MC16e.root')

simtopra1 = simtopr1a['Nominal/BaseSelection_tree_Final']
simtopra1cutflow = simtopr1a['Nominal/cutflow_DxAOD']
temp = simtopra1cutflow.values()
simtopra1numsimvalue = temp[1]

simtopra1weight = simtopra1['weight'].array(library='np')

simtoprd1 = simtopr1d['Nominal/BaseSelection_tree_Final']
simtoprd1cutflow = simtopr1d['Nominal/cutflow_DxAOD']
temp = simtoprd1cutflow.values()
simtoprd1numsimvalue = temp[1]

simtoprd1weight = simtoprd1['weight'].array(library='np')

simtopre1 = simtopr1e['Nominal/BaseSelection_tree_Final']
simtopre1cutflow = simtopr1e['Nominal/cutflow_DxAOD']
temp = simtopre1cutflow.values()
simtopre1numsimvalue = temp[1]

simtopre1weight = simtopre1['weight'].array(library='np')

weightfactortopr1a = intluma*0.43844*0.00052458/simtopra1numsimvalue
weightfactortopr1d = intlumd*0.43844*0.00052458/simtoprd1numsimvalue
weightfactortopr1e = intlume*0.43844*0.00052458/simtopre1numsimvalue

toprweight1a = simtopra1weight*weightfactortopr1a
toprweight1d = simtoprd1weight*weightfactortopr1d
toprweight1e = simtopre1weight*weightfactortopr1e

toprweight1 = np.concatenate((toprweight1a,toprweight1d,toprweight1e))


simtopr2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346345_0.MC16a.root')
simtopr2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346345_0.MC16d.root')
simtopr2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-346345_0.MC16e.root')

simtopra2 = simtopr2a['Nominal/BaseSelection_tree_Final']
simtopra2cutflow = simtopr2a['Nominal/cutflow_DxAOD']
temp = simtopra2cutflow.values()
simtopra2numsimvalue = temp[1]

simtopra2weight = simtopra2['weight'].array(library='np')

simtoprd2 = simtopr2d['Nominal/BaseSelection_tree_Final']
simtoprd2cutflow = simtopr2d['Nominal/cutflow_DxAOD']
temp = simtoprd2cutflow.values()
simtoprd2numsimvalue = temp[1]

simtoprd2weight = simtoprd2['weight'].array(library='np')

simtopre2 = simtopr2e['Nominal/BaseSelection_tree_Final']
simtopre2cutflow = simtopr2e['Nominal/cutflow_DxAOD']
temp = simtopre2cutflow.values()
simtopre2numsimvalue = temp[1]

simtopre2weight = simtopre2['weight'].array(library='np')

weightfactortopr2a = intluma*5.4667/100000/simtopra2numsimvalue
weightfactortopr2d = intlumd*5.4667/100000/simtoprd2numsimvalue
weightfactortopr2e = intlume*5.4667/100000/simtopre2numsimvalue

toprweight2a = simtopra2weight*weightfactortopr2a
toprweight2d = simtoprd2weight*weightfactortopr2d
toprweight2e = simtopre2weight*weightfactortopr2e

toprweight2 = np.concatenate((toprweight2a,toprweight2d,toprweight2e))


simtopr3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410080_0.MC16a.root')
simtopr3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410080_0.MC16d.root')
simtopr3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410080_0.MC16e.root')

simtopra3 = simtopr3a['Nominal/BaseSelection_tree_Final']
simtopra3cutflow = simtopr3a['Nominal/cutflow_DxAOD']
temp = simtopra3cutflow.values()
simtopra3numsimvalue = temp[1]

simtopra3weight = simtopra3['weight'].array(library='np')

simtoprd3 = simtopr3d['Nominal/BaseSelection_tree_Final']
simtoprd3cutflow = simtopr3d['Nominal/cutflow_DxAOD']
temp = simtoprd3cutflow.values()
simtoprd3numsimvalue = temp[1]

simtoprd3weight = simtoprd3['weight'].array(library='np')

simtopre3 = simtopr3e['Nominal/BaseSelection_tree_Final']
simtopre3cutflow = simtopr3e['Nominal/cutflow_DxAOD']
temp = simtopre3cutflow.values()
simtopre3numsimvalue = temp[1]

simtopre3weight = simtopre3['weight'].array(library='np')

weightfactortopr3a = intluma*1.00413615479*9.1626/1000000/simtopra3numsimvalue
weightfactortopr3d = intlumd*1.00413615479*9.1626/1000000/simtoprd3numsimvalue
weightfactortopr3e = intlume*1.00413615479*9.1626/1000000/simtopre3numsimvalue

toprweight3a = simtopra3weight*weightfactortopr3a
toprweight3d = simtoprd3weight*weightfactortopr3d
toprweight3e = simtopre3weight*weightfactortopr3e

toprweight3 = np.concatenate((toprweight3a,toprweight3d,toprweight3e))


simtopr4a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410081_0.MC16a.root')
simtopr4d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410081_0.MC16d.root')
simtopr4e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-410081_0.MC16e.root')

simtopra4 = simtopr4a['Nominal/BaseSelection_tree_Final']
simtopra4cutflow = simtopr4a['Nominal/cutflow_DxAOD']
temp = simtopra4cutflow.values()
simtopra4numsimvalue = temp[1]

simtopra4weight = simtopra4['weight'].array(library='np')

simtoprd4 = simtopr4d['Nominal/BaseSelection_tree_Final']
simtoprd4cutflow = simtopr4d['Nominal/cutflow_DxAOD']
temp = simtoprd4cutflow.values()
simtoprd4numsimvalue = temp[1]

simtoprd4weight = simtoprd4['weight'].array(library='np')

simtopre4 = simtopr4e['Nominal/BaseSelection_tree_Final']
simtopre4cutflow = simtopr4e['Nominal/cutflow_DxAOD']
temp = simtopre4cutflow.values()
simtopre4numsimvalue = temp[1]

simtopre4weight = simtopre4['weight'].array(library='np')

weightfactortopr4a = intluma*1.22342593851*8.0952/1000000/simtopra4numsimvalue
weightfactortopr4d = intlumd*1.22342593851*8.0952/1000000/simtoprd4numsimvalue
weightfactortopr4e = intlume*1.22342593851*8.0952/1000000/simtopre4numsimvalue

toprweight4a = simtopra4weight*weightfactortopr4a
toprweight4d = simtoprd4weight*weightfactortopr4d
toprweight4e = simtopre4weight*weightfactortopr4e

toprweight4 = np.concatenate((toprweight4a,toprweight4d,toprweight4e))


simtopr5a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16a.root')
simtopr5d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16d.root')
simtopr5e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-412118_0.MC16e.root')

simtopra5 = simtopr5a['Nominal/BaseSelection_tree_Final']
simtopra5cutflow = simtopr5a['Nominal/cutflow_DxAOD']
temp = simtopra5cutflow.values()
simtopra5numsimvalue = temp[1]

simtopra5weight = simtopra5['weight'].array(library='np')

simtoprd5 = simtopr5d['Nominal/BaseSelection_tree_Final']
simtoprd5cutflow = simtopr5d['Nominal/cutflow_DxAOD']
temp = simtoprd5cutflow.values()
simtoprd5numsimvalue = temp[1]

simtoprd5weight = simtoprd5['weight'].array(library='np')

simtopre5 = simtopr5e['Nominal/BaseSelection_tree_Final']
simtopre5cutflow = simtopr5e['Nominal/cutflow_DxAOD']
temp = simtopre5cutflow.values()
simtopre5numsimvalue = temp[1]

simtopre5weight = simtopre5['weight'].array(library='np')

weightfactortopr5a = intluma*1.6095/100000/simtopra5numsimvalue
weightfactortopr5d = intlumd*1.6095/100000/1000000/simtoprd5numsimvalue
weightfactortopr5e = intlume*1.6095/100000/1000000/simtopre5numsimvalue

toprweight5a = simtopra5weight*weightfactortopr5a
toprweight5d = simtoprd5weight*weightfactortopr5d
toprweight5e = simtopre5weight*weightfactortopr5e

toprweight5 = np.concatenate((toprweight5a,toprweight5d,toprweight5e))


top_weight = np.concatenate((topweight1,topweight2,topweight3,toprweight1,toprweight2,toprweight3,toprweight4,toprweight5))

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='inv_mass', library='np')
top_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met', library='np')
top_met = temp['track_met']
top_met = top_met/1000

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='dilep_mass', library='np')
top_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_n', library='np')
top_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_n', library='np')
top_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_charge', library='np')
top_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_charge', library='np')
top_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_n', library='np')
top_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_has_btag', library='np')
top_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='isOnZ', library='np')
top_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_onZ', library='np')
top_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_onZ', library='np')
top_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_pt', library='np')
top_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_eta', library='np')
top_electron_eta = temp['electron_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_phi', library='np')
top_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_mt', library='np')
top_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_pt', library='np')
top_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_eta', library='np')
top_muon_eta = temp['muon_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_phi', library='np')
top_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_mt', library='np')
top_muon_mt = temp['muon_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\top\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met_phi', library='np')
top_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

top_index_onz = np.where(top_onz == True)
top_index_onz = top_index_onz[0]

top_inv_mass = np.take(top_inv_mass,top_index_onz)
top_met = np.take(top_met,top_index_onz)
top_muononz = np.take(top_muononz,top_index_onz)
top_electrononz = np.take(top_electrononz,top_index_onz)
top_weight = np.take(top_weight,top_index_onz)
top_dilep_mass = np.take(top_dilep_mass,top_index_onz)
top_electron_n = np.take(top_electron_n,top_index_onz)
top_muon_n = np.take(top_muon_n,top_index_onz)
top_electron_charge = np.take(top_electron_charge,top_index_onz)
top_muon_charge = np.take(top_muon_charge,top_index_onz)
top_jet_n = np.take(top_jet_n,top_index_onz)
top_jet_btag = np.take(top_jet_btag,top_index_onz)

top_electron_pt = np.take(top_electron_pt,top_index_onz)
top_electron_eta = np.take(top_electron_eta,top_index_onz)
top_electron_phi = np.take(top_electron_phi,top_index_onz)
top_electron_mt = np.take(top_electron_mt,top_index_onz)
top_muon_pt = np.take(top_muon_pt,top_index_onz)
top_muon_eta = np.take(top_muon_eta,top_index_onz)
top_muon_phi = np.take(top_muon_phi,top_index_onz)
top_muon_mt = np.take(top_muon_mt,top_index_onz)
top_met_phi = np.take(top_met_phi,top_index_onz)


#Higgs Sims

simhiggs1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\ntuple-306540_0.MC16a.root')
simhiggs1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\ntuple-306540_0.MC16d.root')
simhiggs1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\ntuple-306540_0.MC16e.root')

simhiggsa1 = simhiggs1a['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggsa1cutflow = simhiggs1a['Nominal/cutflow_DxAOD']
temp = simhiggsa1cutflow.values()
simhiggsa1numsimvalue = temp[1]

simhiggsa1weight = simhiggsa1['weight'].array(library='np')

simhiggsd1 = simhiggs1d['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggsd1cutflow = simhiggs1d['Nominal/cutflow_DxAOD']
temp = simhiggsd1cutflow.values()
simhiggsd1numsimvalue = temp[1]

simhiggsd1weight = simhiggsd1['weight'].array(library='np')

simhiggse1 = simhiggs1e['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggse1cutflow = simhiggs1e['Nominal/cutflow_DxAOD']
temp = simhiggse1cutflow.values()
simhiggse1numsimvalue = temp[1]

simhiggse1weight = simhiggse1['weight'].array(library='np')

weightfactorhiggs1a = intluma*2.325/100000/simhiggsa1numsimvalue

weightfactorhiggs1d = intlumd*2.325/100000/simhiggsd1numsimvalue
weightfactorhiggs1e = intlume*2.325/100000/simhiggse1numsimvalue

higgsweight1a = simhiggsa1weight*weightfactorhiggs1a

higgsweight1d = simhiggsd1weight*weightfactorhiggs1d
higgsweight1e = simhiggse1weight*weightfactorhiggs1e

higgsweight1 = np.concatenate((higgsweight1a,higgsweight1d,higgsweight1e))


higgs_weight = higgsweight1


temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='inv_mass', library='np')
higgs_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met', library='np')
higgs_met = temp['track_met']
higgs_met = higgs_met/1000

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='dilep_mass', library='np')
#higgs_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_n', library='np')
higgs_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_n', library='np')
higgs_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_charge', library='np')
higgs_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_charge', library='np')
higgs_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_n', library='np')
higgs_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_has_btag', library='np')
higgs_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='isOnZ', library='np')
higgs_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_onZ', library='np')
higgs_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_onZ', library='np')
higgs_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_pt', library='np')
higgs_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_eta', library='np')
higgs_electron_eta = temp['electron_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_phi', library='np')
#higgs_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_mt', library='np')
higgs_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_pt', library='np')
higgs_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_eta', library='np')
higgs_muon_eta = temp['muon_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_phi', library='np')
#higgs_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_mt', library='np')
higgs_muon_mt = temp['muon_mt']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\1\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met_phi', library='np')
#higgs_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

higgs_index_onz = np.where(higgs_onz == True)
higgs_index_onz = higgs_index_onz[0]

higgs_inv_mass = np.take(higgs_inv_mass,higgs_index_onz)
higgs_met = np.take(higgs_met,higgs_index_onz)
higgs_muononz = np.take(higgs_muononz,higgs_index_onz)
higgs_electrononz = np.take(higgs_electrononz,higgs_index_onz)
higgs_weight = np.take(higgs_weight,higgs_index_onz)
#higgs_dilep_mass = np.take(higgs_dilep_mass,higgs_index_onz)
higgs_electron_n = np.take(higgs_electron_n,higgs_index_onz)
higgs_muon_n = np.take(higgs_muon_n,higgs_index_onz)
higgs_electron_charge = np.take(higgs_electron_charge,higgs_index_onz)
higgs_muon_charge = np.take(higgs_muon_charge,higgs_index_onz)
higgs_jet_n = np.take(higgs_jet_n,higgs_index_onz)
higgs_jet_btag = np.take(higgs_jet_btag,higgs_index_onz)

higgs_electron_pt = np.take(higgs_electron_pt,higgs_index_onz)
higgs_electron_eta = np.take(higgs_electron_eta,higgs_index_onz)
#higgs_electron_phi = np.take(higgs_electron_phi,higgs_index_onz)
higgs_electron_mt = np.take(higgs_electron_mt,higgs_index_onz)
higgs_muon_pt = np.take(higgs_muon_pt,higgs_index_onz)
higgs_muon_eta = np.take(higgs_muon_eta,higgs_index_onz)
#higgs_muon_phi = np.take(higgs_muon_phi,higgs_index_onz)
higgs_muon_mt = np.take(higgs_muon_mt,higgs_index_onz)
#higgs_met_phi = np.take(higgs_met_phi,higgs_index_onz)

#Checking that the total lepton number is 4

temp = higgs_electron_n + higgs_muon_n
higgs_n_index = np.where(temp == 4)
higgs_n_index = higgs_n_index[0]

higgs_inv_mass = np.take(higgs_inv_mass,higgs_n_index)
higgs_met = np.take(higgs_met,higgs_n_index)
higgs_weight = np.take(higgs_weight,higgs_n_index)
#higgs_dilep_mass = np.take(higgs_dilep_mass,higgs_n_index)
higgs_electron_n = np.take(higgs_electron_n,higgs_n_index)
higgs_muon_n = np.take(higgs_muon_n,higgs_n_index)
higgs_electron_charge = np.take(higgs_electron_charge,higgs_n_index)
higgs_muon_charge = np.take(higgs_muon_charge,higgs_n_index)
higgs_jet_n = np.take(higgs_jet_n,higgs_n_index)
higgs_jet_btag = np.take(higgs_jet_btag,higgs_n_index)
higgs_muononz = np.take(higgs_muononz,higgs_n_index)
higgs_electrononz = np.take(higgs_electrononz,higgs_n_index)

higgs_electron_pt = np.take(higgs_electron_pt,higgs_n_index)
higgs_electron_eta = np.take(higgs_electron_eta,higgs_n_index)
#higgs_electron_phi = np.take(higgs_electron_phi,higgs_n_index)
higgs_electron_mt = np.take(higgs_electron_mt,higgs_n_index)
higgs_muon_pt = np.take(higgs_muon_pt,higgs_n_index)
higgs_muon_eta = np.take(higgs_muon_eta,higgs_n_index)
#higgs_muon_phi = np.take(higgs_muon_phi,higgs_n_index)
higgs_muon_mt = np.take(higgs_muon_mt,higgs_n_index)
#higgs_met_phi = np.take(higgs_met_phi,higgs_n_index)


#second higgs

simhiggs2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\ntuple-306544_0.MC16a.root')
simhiggs2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\ntuple-306544_0.MC16d.root')
simhiggs2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\ntuple-306544_0.MC16e.root')

simhiggsa2 = simhiggs2a['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggsa2cutflow = simhiggs2a['Nominal/cutflow_DxAOD']
temp = simhiggsa2cutflow.values()
simhiggsa2numsimvalue = temp[1]

simhiggsa2weight = simhiggsa2['weight'].array(library='np')

simhiggsd2 = simhiggs2d['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggsd2cutflow = simhiggs2d['Nominal/cutflow_DxAOD']
temp = simhiggsd2cutflow.values()
simhiggsd2numsimvalue = temp[1]

simhiggsd2weight = simhiggsd2['weight'].array(library='np')

simhiggse2 = simhiggs2e['Nominal/BaseSelection_ml_tree_syst_Final']
simhiggse2cutflow = simhiggs2e['Nominal/cutflow_DxAOD']
temp = simhiggse2cutflow.values()
simhiggse2numsimvalue = temp[1]

simhiggse2weight = simhiggse2['weight'].array(library='np')

weightfactorhiggs2a = intluma*2.4924/1000000/simhiggsa2numsimvalue

weightfactorhiggs2d = intlumd*2.4924/1000000/simhiggsd2numsimvalue
weightfactorhiggs2e = intlume*2.4924/1000000/simhiggse2numsimvalue

higgsweight2a = simhiggsa2weight*weightfactorhiggs2a

higgsweight2d = simhiggsd2weight*weightfactorhiggs2d
higgsweight2e = simhiggse2weight*weightfactorhiggs2e

higgsweight2 = np.concatenate((higgsweight2a,higgsweight2d,higgsweight2e))

higgs2_weight = higgsweight2


temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='inv_mass', library='np')
higgs2_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met', library='np')
higgs2_met = temp['track_met']
higgs2_met = higgs2_met/1000

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='dilep_mass', library='np')
#higgs_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_n', library='np')
higgs2_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_n', library='np')
higgs2_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_charge', library='np')
higgs2_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_charge', library='np')
higgs2_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_n', library='np')
higgs2_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_has_btag', library='np')
higgs2_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='isOnZ', library='np')
higgs2_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_onZ', library='np')
higgs2_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_onZ', library='np')
higgs2_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_pt', library='np')
higgs2_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_eta', library='np')
higgs2_electron_eta = temp['electron_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_phi', library='np')
#higgs2_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_mt', library='np')
higgs2_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_pt', library='np')
higgs2_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_eta', library='np')
higgs2_muon_eta = temp['muon_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_phi', library='np')
#higgs2_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_mt', library='np')
higgs2_muon_mt = temp['muon_mt']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\higgs\2\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met_phi', library='np')
#higgs2_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

higgs2_index_onz = np.where(higgs2_onz == True)
higgs2_index_onz = higgs2_index_onz[0]

higgs2_inv_mass = np.take(higgs2_inv_mass,higgs2_index_onz)
higgs2_met = np.take(higgs2_met,higgs2_index_onz)
higgs2_muononz = np.take(higgs2_muononz,higgs2_index_onz)
higgs2_electrononz = np.take(higgs2_electrononz,higgs2_index_onz)
higgs2_weight = np.take(higgs2_weight,higgs2_index_onz)
#higgs2_dilep_mass = np.take(higgs2_dilep_mass,higgs2_index_onz)
higgs2_electron_n = np.take(higgs2_electron_n,higgs2_index_onz)
higgs2_muon_n = np.take(higgs2_muon_n,higgs2_index_onz)
higgs2_electron_charge = np.take(higgs2_electron_charge,higgs2_index_onz)
higgs2_muon_charge = np.take(higgs2_muon_charge,higgs2_index_onz)
higgs2_jet_n = np.take(higgs2_jet_n,higgs2_index_onz)
higgs2_jet_btag = np.take(higgs2_jet_btag,higgs2_index_onz)

higgs2_electron_pt = np.take(higgs2_electron_pt,higgs2_index_onz)
higgs2_electron_eta = np.take(higgs2_electron_eta,higgs2_index_onz)
#higgs2_electron_phi = np.take(higgs2_electron_phi,higgs2_index_onz)
higgs2_electron_mt = np.take(higgs2_electron_mt,higgs2_index_onz)
higgs2_muon_pt = np.take(higgs2_muon_pt,higgs2_index_onz)
higgs2_muon_eta = np.take(higgs2_muon_eta,higgs2_index_onz)
#higgs2_muon_phi = np.take(higgs2_muon_phi,higgs2_index_onz)
higgs2_muon_mt = np.take(higgs2_muon_mt,higgs2_index_onz)
#higgs2_met_phi = np.take(higgs2_met_phi,higgs2_index_onz)

#Checking that the total lepton number is 4

temp = higgs2_electron_n + higgs2_muon_n
higgs2_n_index = np.where(temp == 4)
higgs2_n_index = higgs2_n_index[0]

higgs2_inv_mass = np.take(higgs2_inv_mass,higgs2_n_index)
higgs2_met = np.take(higgs2_met,higgs2_n_index)
higgs2_weight = np.take(higgs2_weight,higgs2_n_index)
#higgs2_dilep_mass = np.take(higgs2_dilep_mass,higgs2_n_index)
higgs2_electron_n = np.take(higgs2_electron_n,higgs2_n_index)
higgs2_muon_n = np.take(higgs2_muon_n,higgs2_n_index)
higgs2_electron_charge = np.take(higgs2_electron_charge,higgs2_n_index)
higgs2_muon_charge = np.take(higgs2_muon_charge,higgs2_n_index)
higgs2_jet_n = np.take(higgs2_jet_n,higgs2_n_index)
higgs2_jet_btag = np.take(higgs2_jet_btag,higgs2_n_index)
higgs2_muononz = np.take(higgs2_muononz,higgs2_n_index)
higgs2_electrononz = np.take(higgs2_electrononz,higgs2_n_index)

higgs2_electron_pt = np.take(higgs2_electron_pt,higgs2_n_index)
higgs2_electron_eta = np.take(higgs2_electron_eta,higgs2_n_index)
#higgs2_electron_phi = np.take(higgs2_electron_phi,higgs2_n_index)
higgs2_electron_mt = np.take(higgs2_electron_mt,higgs2_n_index)
higgs2_muon_pt = np.take(higgs2_muon_pt,higgs2_n_index)
higgs2_muon_eta = np.take(higgs2_muon_eta,higgs2_n_index)
#higgs2_muon_phi = np.take(higgs2_muon_phi,higgs2_n_index)
higgs2_muon_mt = np.take(higgs2_muon_mt,higgs2_n_index)
#higgs2_met_phi = np.take(higgs2_met_phi,higgs2_n_index)


#Fake simulations

simfake1a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001568_0.MC16a.root')
simfake2a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001569_0.MC16a.root')
simfake3a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001570_0.MC16a.root')
simfake4a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001571_0.MC16a.root')
simfake5a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001572_0.MC16a.root')
simfake6a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001574_0.MC16a.root')
simfake7a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001665_0.MC16a.root')
simfake8a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001666_0.MC16a.root')
simfake9a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001667_0.MC16a.root')
simfake10a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001668_0.MC16a.root')
simfake11a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001669_0.MC16a.root')
simfake12a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001670_0.MC16a.root')
simfake13a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001671_0.MC16a.root')
simfake14a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001673_0.MC16a.root')
simfake15a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001675_0.MC16a.root')
simfake16a = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001676_0.MC16a.root')

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='inv_mass', library='np')
fake_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met', library='np')
fake_met = temp['track_met']
fake_met = fake_met/1000

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='dilep_mass', library='np')
fake_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_n', library='np')
fake_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_n', library='np')
fake_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_charge', library='np')
fake_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_charge', library='np')
fake_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_n', library='np')
fake_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='jet_has_btag', library='np')
fake_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='isOnZ', library='np')
fake_onz = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_onZ', library='np')
fake_muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_onZ', library='np')
fake_electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='weight', library='np')
fake_weight = temp['weight']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_pt', library='np')
fake_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_eta', library='np')
fake_electron_eta = temp['electron_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_phi', library='np')
#fake_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='electron_mt', library='np')
fake_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_pt', library='np')
fake_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_eta', library='np')
fake_muon_eta = temp['muon_eta']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_phi', library='np')
#fake_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='muon_mt', library='np')
fake_muon_mt = temp['muon_mt']

#temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\mc\fake\all\*.root:Nominal/BaseSelection_ml_tree_syst_Final', filter_name='track_met_phi', library='np')
#fake_met_phi = temp['track_met_phi']

#removing all the isOnZ == False entries

fake_index_onz = np.where(fake_onz == True)
fake_index_onz = fake_index_onz[0]

fake_inv_mass = np.take(fake_inv_mass,fake_index_onz)
fake_met = np.take(fake_met,fake_index_onz)
fake_muononz = np.take(fake_muononz,fake_index_onz)
fake_electrononz = np.take(fake_electrononz,fake_index_onz)
fake_weight = np.take(fake_weight,fake_index_onz)
fake_dilep_mass = np.take(fake_dilep_mass,fake_index_onz)
fake_electron_n = np.take(fake_electron_n,fake_index_onz)
fake_muon_n = np.take(fake_muon_n,fake_index_onz)
fake_electron_charge = np.take(fake_electron_charge,fake_index_onz)
fake_muon_charge = np.take(fake_muon_charge,fake_index_onz)
fake_jet_n = np.take(fake_jet_n,fake_index_onz)
fake_jet_btag = np.take(fake_jet_btag,fake_index_onz)

fake_electron_pt = np.take(fake_electron_pt,fake_index_onz)
fake_electron_eta = np.take(fake_electron_eta,fake_index_onz)
#fake_electron_phi = np.take(fake_electron_phi,fake_index_onz)
fake_electron_mt = np.take(fake_electron_mt,fake_index_onz)
fake_muon_pt = np.take(fake_muon_pt,fake_index_onz)
fake_muon_eta = np.take(fake_muon_eta,fake_index_onz)
#fake_muon_phi = np.take(fake_muon_phi,fake_index_onz)
fake_muon_mt = np.take(fake_muon_mt,fake_index_onz)
#fake_met_phi = np.take(fake_met_phi,fake_index_onz)

#Checking that the total lepton number is 4

temp = fake_electron_n + fake_muon_n
fake_n_index = np.where(temp == 4)
fake_n_index = fake_n_index[0]

fake_inv_mass = np.take(fake_inv_mass,fake_n_index)
fake_met = np.take(fake_met,fake_n_index)
fake_weight = np.take(fake_weight,fake_n_index)
fake_dilep_mass = np.take(fake_dilep_mass,fake_n_index)
fake_electron_n = np.take(fake_electron_n,fake_n_index)
fake_muon_n = np.take(fake_muon_n,fake_n_index)
fake_electron_charge = np.take(fake_electron_charge,fake_n_index)
fake_muon_charge = np.take(fake_muon_charge,fake_n_index)
fake_jet_n = np.take(fake_jet_n,fake_n_index)
fake_jet_btag = np.take(fake_jet_btag,fake_n_index)
fake_muononz = np.take(fake_muononz,fake_n_index)
fake_electrononz = np.take(fake_electrononz,fake_n_index)

fake_electron_pt = np.take(fake_electron_pt,fake_n_index)
fake_electron_eta = np.take(fake_electron_eta,fake_n_index)
#fake_electron_phi = np.take(fake_electron_phi,fake_n_index)
fake_electron_mt = np.take(fake_electron_mt,fake_n_index)
fake_muon_pt = np.take(fake_muon_pt,fake_n_index)
fake_muon_eta = np.take(fake_muon_eta,fake_n_index)
#fake_muon_phi = np.take(fake_muon_phi,fake_n_index)
fake_muon_mt = np.take(fake_muon_mt,fake_n_index)
#fake_met_phi = np.take(fake_met_phi,fake_n_index)



simfake1d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001766_0.MC16d.root')
simfake2d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001767_0.MC16d.root')
simfake3d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001768_0.MC16d.root')
simfake4d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001769_0.MC16d.root')
simfake5d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001770_0.MC16d.root')
simfake6d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001772_0.MC16d.root')
simfake7d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001773_0.MC16d.root')
simfake8d = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001775_0.MC16d.root')

simfake1e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001866_0.MC16e.root')
simfake2e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001867_0.MC16e.root')
simfake3e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001868_0.MC16e.root')
simfake4e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001870_0.MC16e.root')
simfake5e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001873_0.MC16e.root')
simfake6e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001875_0.MC16e.root')
simfake7e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001876_0.MC16e.root')
simfake8e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001877_0.MC16e.root')
simfake9e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001879_0.MC16e.root')
simfake10e = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-9001881_0.MC16e.root')
