
simdata = [triboson_met,top_met,fake_met,diboson_met]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]
simdata2 = [triboson_met_em3,top_met_em3,fake_met_em3,diboson_met_em3]
simweight2 = [triboson_weight_em3,top_weight_em3,fake_weight_em3,diboson_weight_em3]
simdata3 = [triboson_met_0jet,top_met_0jet,fake_met_0jet,diboson_met_0jet]
simweight3 = [triboson_weight_0jet,top_weight_0jet,fake_weight_0jet,diboson_weight_0jet]


fig, (ax1, ax2, ax3) = plt.subplots(1,3)
#fig.suptitle('Missing E_t')
ax1.hist(data_met, bins=met_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=met_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([0,300])
ax1.set_xlabel('Missing Transverse Energy (GeV)')
ax1.set_ylim([0.4,2500])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Missing Transverse Energy')

ax2.hist(data_met_em3, bins=met_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdata2, bins=met_bin,histtype='bar',weights=simweight2,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_xlim([0,300])
ax2.set_xlabel('Missing Transverse Energy (GeV)')
ax2.set_ylim([0,10])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Missing Transverse Energy (emmm+eeem)')

ax3.hist(data_met_0jet, bins=met_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdata3, bins=met_bin,histtype='bar',weights=simweight3,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_yscale('log')
ax3.set_xlim([0,300])
ax3.set_xlabel('Missing Transverse Energy (GeV)')
ax3.set_ylim([0.4,500])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('Missing Transverse Energy with 0 jets')

plt.show()
