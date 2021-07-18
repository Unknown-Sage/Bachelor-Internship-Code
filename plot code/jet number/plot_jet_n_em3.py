
simdata = [triboson_jet_n_em3,top_jet_n_em3,fake_jet_n_em3,diboson_jet_n_em3]
simweight = [triboson_weight_em3,top_weight_em3,fake_weight_em3,diboson_weight_em3]
simdatahigh = [triboson_jet_n_high_em3,top_jet_n_high_em3,fake_jet_n_high_em3,diboson_jet_n_high_em3]
simweighthigh = [triboson_weight_high_em3,top_weight_high_em3,fake_weight_high_em3,diboson_weight_high_em3]
simdatalow = [triboson_jet_n_low_em3,top_jet_n_low_em3,fake_jet_n_low_em3,diboson_jet_n_low_em3]
simweightlow = [triboson_weight_low_em3,top_weight_low_em3,fake_weight_low_em3,diboson_weight_low_em3]


fig, (ax1, ax2, ax3) = plt.subplots(1,3)
fig.suptitle('Jet Multiplicity')
ax1.hist(data_jet_n_em3, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=jet_n_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([0,6])
ax1.set_xlabel('#jets')
ax1.set_ylim([0,30])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Jet Multiplicity')

ax2.hist(data_jet_n_high_em3, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatahigh, bins=jet_n_bin,histtype='bar',weights=simweighthigh,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_xlim([0,6])
ax2.set_xlabel('#jets')
ax2.set_ylim([0,30])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Missing E_t > 50')

ax3.hist(data_jet_n_low_em3, bins=jet_n_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatalow, bins=jet_n_bin,histtype='bar',weights=simweightlow,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_xlim([0,6])
ax3.set_xlabel('#jets')
ax3.set_ylim([0,30])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('Missing E_t < 50')

plt.show()
