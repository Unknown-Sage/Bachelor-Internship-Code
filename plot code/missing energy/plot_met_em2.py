

simdata4 = [triboson_met_em2,top_met_em2,fake_met_em2,diboson_met_em2]
simweight4 = [triboson_weight_em2,top_weight_em2,fake_weight_em2,diboson_weight_em2]


fig, (ax1) = plt.subplots(1,1)
#fig.suptitle('Missing E_t for eeem and emmm states')

ax1.hist(data_met_em2, bins=met_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata4, bins=met_bin,histtype='bar',weights=simweight4,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([0,300])
ax1.set_xlabel('Missing Transverse Energy (GeV)')
ax1.set_ylim([0.4,1000])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Missing Transverse Energy (eemm)')

plt.show()
