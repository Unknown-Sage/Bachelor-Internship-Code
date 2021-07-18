
simdata = [triboson_electron_n,top_electron_n,fake_electron_n,diboson_electron_n]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

combidata = np.concatenate((triboson_electron_n,top_electron_n,fake_electron_n,diboson_electron_n))
combiweight = np.concatenate((triboson_weight,top_weight,fake_weight,diboson_weight))

temp1 = plt.hist(combidata, bins=electron_n_bin,histtype='bar',weights=combiweight,stacked=True,label=['triboson','top','fake','diboson'])
temp2 = plt.hist(higgs2_electron_n, bins=electron_n_bin,histtype='step',weights=higgs2_weight,stacked=False,label='doubly charged higgs2')



fig, (ax1, ax2) = plt.subplots(1,2)


ax1.hist(higgs2_electron_n, bins=electron_n_bin,histtype='step',weights=higgs2_weight,stacked=True,label='higgs2')
ax1.hist(simdata, bins=electron_n_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([0,6])
ax1.set_xlabel('#electrons')
ax1.set_ylim([0,150])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Electron Multiplicity Higgs (500GeV) Comparison')

s = temp2[0]
b = temp1[0]

comparisonvalue = s/np.sqrt(b)
comparisonvalue2 = np.sqrt(2*((temp2[0]+temp1[0])*np.log(1+temp2[0]/temp1[0])-temp2[0]))


ax2.plot(electron_n_scale,comparisonvalue,label='"simple" significance')
ax2.plot(electron_n_scale,comparisonvalue2,label='"complex" significance')
ax2.set_xlim([0,6])
ax2.set_xlabel('#electrons')
ax2.set_ylim([-0.5,1])
ax2.set_ylabel('Expected Significance')
ax2.legend()
ax2.set_title('Electron Multiplicity Higgs (500GeV) Expected Significance')


plt.show()
