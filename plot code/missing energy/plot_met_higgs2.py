
simdata = [triboson_met,top_met,fake_met,diboson_met]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

combidata = np.concatenate((triboson_met,top_met,fake_met,diboson_met))
combiweight = np.concatenate((triboson_weight,top_weight,fake_weight,diboson_weight))

temp1 = plt.hist(combidata, bins=met_bin_higgs,histtype='bar',weights=combiweight,stacked=True,label=['triboson','top','fake','diboson'])
temp2 = plt.hist(higgs2_met, bins=met_bin_higgs,histtype='step',weights=higgs2_weight,stacked=False,label='doubly charged higgs2')

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.hist(higgs2_met, bins=met_bin_higgs,histtype='step',weights=higgs2_weight,stacked=False,label='doubly charged higgs2')
ax1.hist(simdata, bins=met_bin_higgs,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([0,300])
ax1.set_xlabel('Missing Transverse Energy (GeV)')
ax1.set_ylim([0.4,2500])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Missing Transverse Energy Higgs (500GeV) Comparison')

s = temp2[0]
b = temp1[0]

comparisonvalue = s/np.sqrt(b)
comparisonvalue2 = np.sqrt(2*((temp2[0]+temp1[0])*np.log(1+temp2[0]/temp1[0])-temp2[0]))

ax2.plot(met_scale,comparisonvalue,label='"simple" significance')
ax2.plot(met_scale,comparisonvalue2,label='"complex" significance')
ax2.set_xlim([0,300])
ax2.set_xlabel('Missing Transverse Energy (GeV)')
ax2.set_ylim([-0.1,0.2])
ax2.set_ylabel('Expected Significance')
ax2.legend()
ax2.set_title('Missing Transverse Energy Higgs (500GeV) Expected Significance')

plt.show()
