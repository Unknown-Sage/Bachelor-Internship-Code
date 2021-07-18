
simdata = [triboson_inv_mass,top_inv_mass,fake_inv_mass,diboson_inv_mass]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

combidata = np.concatenate((triboson_inv_mass,top_inv_mass,fake_inv_mass,diboson_inv_mass))
combiweight = np.concatenate((triboson_weight,top_weight,fake_weight,diboson_weight))

minimumvaluescale = [-1000,500,2000]
minimumvaluescale2 = [250,750]

temp1 = plt.hist(combidata, bins=minimumvaluescale,histtype='bar',weights=combiweight,stacked=True,label=['triboson','top','fake','diboson'])
temp2 = plt.hist(higgs_inv_mass, bins=minimumvaluescale,histtype='step',weights=higgs_weight,stacked=False,label='doubly charged higgs')


fig, (ax1, ax2) = plt.subplots(1,2)
#fig.suptitle('Invariant Mass')

ax1.hist(higgs_inv_mass, bins=minimumvaluescale,histtype='step',weights=higgs_weight,stacked=False,label='doubly charged higgs')
ax1.hist(simdata, bins=minimumvaluescale,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([100,1800])
ax1.set_xlabel('invariant mass (GeV)')
ax1.set_ylim([0.4,2500])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Invariant Mass Higgs (300GeV) Comparison')

s = temp2[0]
b = temp1[0]

comparisonvalue = s/np.sqrt(b)
comparisonvalue2 = np.sqrt(2*((temp2[0]+temp1[0])*np.log(1+temp2[0]/temp1[0])-temp2[0]))

ax2.plot(minimumvaluescale2,comparisonvalue,label='"simple" significance',linestyle="",marker="x")
ax2.plot(minimumvaluescale2,comparisonvalue2,label='"complex" significance',linestyle="",marker="+")
ax2.set_xlim([100,900])
ax2.set_xlabel('invariant mass (GeV)')
ax2.set_ylim([-1,10])
ax2.set_ylabel('Expected Significance')
ax2.legend()
ax2.set_title('Invariant Mass Higgs (300GeV) Expected Significance')

plt.show()
