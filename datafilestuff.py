import numpy as np
import matplotlib.pyplot as plt
import uproot
import yaml

data1 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodD_0.root')
data2 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodE_0.root')
data3 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodF_0.root')
data4 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodG_0.root')
data5 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodH_0.root')
data6 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data15_13TeV_periodJ_0.root')
data7 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodA_0.root')
data8 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodB_0.root')
data9 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodC_0.root')
data10 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodD_0.root')
data11 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodE_0.root')
data12 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodF_0.root')
data13 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodG_0.root')
data14 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodI_0.root')
data15 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodK_0.root')
data16 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data16_13TeV_periodL_0.root')
data17 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodB_0.root')
data18 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodC_0.root')
data19 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodD_0.root')
data20 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodE_0.root')
data21 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodF_0.root')
data22 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodH_0.root')
data23 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodI_0.root')
data24 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data17_13TeV_periodK_0.root')
data25 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodB_0.root')
data26 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodC_0.root')
data27 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodD_0.root')
data28 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodF_0.root')
data29 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodI_0.root')
data30 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodK_0.root')
data31 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodL_0.root')
data32 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodM_0.root')
data33 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodO_0.root')
data34 = uproot.open(r'C:\Users\Lars\Documents\0bachelorstage\data\ntuple-data18_13TeV_periodQ_0.root')

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='inv_mass', library='np')
data_inv_mass = temp['inv_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met', library='np')
data_met = temp['track_met']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='dilep_mass', library='np')
data_dilep_mass = temp['dilep_mass']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_n', library='np')
data_electron_n = temp['electron_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_n', library='np')
data_muon_n = temp['muon_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_n', library='np')
data_jet_n = temp['jet_n']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='jet_has_btag', library='np')
data_jet_btag = temp['jet_has_btag']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='isOnZ', library='np')
data_onZ = temp['isOnZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_charge', library='np')
data_muon_charge = temp['muon_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_charge', library='np')
data_electron_charge = temp['electron_charge']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_onZ', library='np')
muononz = temp['muon_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_onZ', library='np')
electrononz = temp['electron_onZ']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_pt', library='np')
data_electron_pt = temp['electron_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_eta', library='np')
data_electron_eta = temp['electron_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_phi', library='np')
data_electron_phi = temp['electron_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='electron_mt', library='np')
data_electron_mt = temp['electron_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_pt', library='np')
data_muon_pt = temp['muon_pt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_eta', library='np')
data_muon_eta = temp['muon_eta']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_phi', library='np')
data_muon_phi = temp['muon_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='muon_mt', library='np')
data_muon_mt = temp['muon_mt']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='track_met_phi', library='np')
data_met_phi = temp['track_met_phi']

temp = uproot.concatenate(r'C:\Users\Lars\Documents\0bachelorstage\data\actualdata\*.root:Nominal/BaseSelection_tree_Final', filter_name='weight', library='np')
data_weight = temp['weight']


inv_mass_bin = [100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900,925,950,975,1000]
met_bin = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
electron_n_bin = [0,1,2,3,4,5]
charge_bin = [-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5]
dilep_mass_bin = [80,82,84,86,88,90,92,94,96,98,100,102]
jet_n_bin = [0,1,2,3,4,5,6]

inv_mass_scale = [100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900,925,950,975]
met_scale = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290]
electron_n_scale = [0,1,2,3,4]
jet_n_scale = [0,1,2,3,4,5]


indexonz = np.where(data_onZ == True)
indexonz = indexonz[0]

data_electrononz = np.take(electrononz,indexonz)
data_muononz = np.take(muononz,indexonz)

data_met = data_met/1000
data_inv_mass = np.take(data_inv_mass,indexonz)
data_met = np.take(data_met,indexonz)

data_dilep_mass = np.take(data_dilep_mass,indexonz)
data_weight = np.take(data_weight,indexonz)
data_electron_n = np.take(data_electron_n,indexonz)
data_muon_n = np.take(data_muon_n,indexonz)
data_electron_charge = np.take(data_electron_charge,indexonz)
data_muon_charge = np.take(data_muon_charge,indexonz)
data_jet_n = np.take(data_jet_n,indexonz)
data_jet_btag = np.take(data_jet_btag,indexonz)

data_electron_pt = np.take(data_electron_pt,indexonz)
data_electron_eta = np.take(data_electron_eta,indexonz)
data_electron_phi = np.take(data_electron_phi,indexonz)
data_electron_mt = np.take(data_electron_mt,indexonz)
data_muon_pt = np.take(data_muon_pt,indexonz)
data_muon_eta = np.take(data_muon_eta,indexonz)
data_muon_phi = np.take(data_muon_phi,indexonz)
data_muon_mt = np.take(data_muon_mt,indexonz)
data_met_phi = np.take(data_met_phi,indexonz)

#plt.hist(mettotrdx, bins=met_bin,histtype='step',stacked=False,label='data')
