
simdata = [triboson_bjet_n,top_bjet_n,fake_bjet_n,diboson_bjet_n]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]
simdatahigh = [triboson_bjet_n_high,top_bjet_n_high,fake_bjet_n_high,diboson_bjet_n_high]
simweighthigh = [triboson_weight_high,top_weight_high,fake_weight_high,diboson_weight_high]
simdatalow = [triboson_bjet_n_low,top_bjet_n_low,fake_bjet_n_low,diboson_bjet_n_low]
simweightlow = [triboson_weight_low,top_weight_low,fake_weight_low,diboson_weight_low]


fig, (ax1, ax2, ax3) = plt.subplots(1,3)
#fig.suptitle('bjet Multiplicity')
ax1.hist(data_bjet_n, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=jet_n_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([0,6])
ax1.set_xlabel('#bjets')
ax1.set_ylim([0.3,1000])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('# of BJets')

ax2.hist(data_bjet_n_high, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatahigh, bins=jet_n_bin,histtype='bar',weights=simweighthigh,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_yscale('log')
ax2.set_xlim([0,6])
ax2.set_xlabel('#bjets')
ax2.set_ylim([0.3,1000])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('# of BJets at MET > 50')

ax3.hist(data_bjet_n_low, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatalow, bins=jet_n_bin,histtype='bar',weights=simweightlow,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_yscale('log')
ax3.set_xlim([0,6])
ax3.set_xlabel('#bjets')
ax3.set_ylim([0.3,1000])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('# of BJets at MET < 50')

plt.show()
