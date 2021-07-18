
simdata = [triboson_met_charge0_em3,top_met_charge0_em3,fake_met_charge0_em3,diboson_met_charge0_em3]
simweight = [triboson_weight_charge0_em3,top_weight_charge0_em3,fake_weight_charge0_em3,diboson_weight_charge0_em3]
simdata2 = [triboson_met_charge2_em3,top_met_charge2_em3,fake_met_charge2_em3,diboson_met_charge2_em3]
simweight2 = [triboson_weight_charge2_em3,top_weight_charge2_em3,fake_weight_charge2_em3,diboson_weight_charge2_em3]
simdata3 = [triboson_met_charge2min_em3,top_met_charge2min_em3,fake_met_charge2min_em3,diboson_met_charge2min_em3]
simweight3 = [triboson_weight_charge2min_em3,top_weight_charge2min_em3,fake_weight_charge2min_em3,diboson_weight_charge2min_em3]
simdata4 = [triboson_met_em3,top_met_em3,fake_met_em3,diboson_met_em3]
simweight4 = [triboson_weight_em3,top_weight_em3,fake_weight_em3,diboson_weight_em3]


fig, (ax1) = plt.subplots(1,1)
#fig.suptitle('Missing E_t for eeem and emmm states')

ax1.hist(data_met_em3, bins=met_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata4, bins=met_bin,histtype='bar',weights=simweight4,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([0,300])
ax1.set_xlabel('Missing Transverse Energy (GeV)')
ax1.set_ylim([0,10])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Missing Transverse Energy (emmm+eeem)')

plt.show()
