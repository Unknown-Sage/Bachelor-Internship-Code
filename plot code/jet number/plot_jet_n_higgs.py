
simdata = [triboson_jet_n,top_jet_n,fake_jet_n,diboson_jet_n]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

combidata = np.concatenate((triboson_jet_n,top_jet_n,fake_jet_n,diboson_jet_n))
combiweight = np.concatenate((triboson_weight,top_weight,fake_weight,diboson_weight))

temp1 = plt.hist(combidata, bins=jet_n_bin,histtype='bar',weights=combiweight,stacked=True,label=['triboson','top','fake','diboson'])
temp2 = plt.hist(higgs_jet_n, bins=jet_n_bin,histtype='step',weights=higgs_weight,stacked=False,label='doubly charged higgs')



fig, (ax1, ax2) = plt.subplots(1,2)


ax1.hist(higgs_jet_n, bins=jet_n_bin,histtype='step',weights=higgs_weight,stacked=True,label='higgs')
ax1.hist(simdata, bins=jet_n_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([0,6])
ax1.set_xlabel('#jets')
ax1.set_ylim([0,150])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Jet Multiplicity Higgs (300GeV) Comparison')

s = temp2[0]
b = temp1[0]

comparisonvalue = s/np.sqrt(b)
comparisonvalue2 = np.sqrt(2*((temp2[0]+temp1[0])*np.log(1+temp2[0]/temp1[0])-temp2[0]))


ax2.plot(jet_n_scale,comparisonvalue,label='"simple" significance')
ax2.plot(jet_n_scale,comparisonvalue2,label='"complex" significance')
ax2.set_xlim([0,6])
ax2.set_xlabel('#jets')
ax2.set_ylim([0,5])
ax2.set_ylabel('Expected Significance')
ax2.legend()
ax2.set_title('Jet Multiplicity Higgs (300GeV) Expected Significance')


plt.show()
