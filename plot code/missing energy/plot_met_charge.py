
simdata2 = [triboson_met_charge2,top_met_charge2,fake_met_charge2,diboson_met_charge2]
simweight2 = [triboson_weight_charge2,top_weight_charge2,fake_weight_charge2,diboson_weight_charge2]
simdata3 = [triboson_met_charge2min,top_met_charge2min,fake_met_charge2min,diboson_met_charge2min]
simweight3 = [triboson_weight_charge2min,top_weight_charge2min,fake_weight_charge2min,diboson_weight_charge2min]



fig, (ax1, ax2) = plt.subplots(1,2)

ax1.hist(data_met_charge2, bins=met_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata2, bins=met_bin,histtype='bar',weights=simweight2,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([0,300])
ax1.set_xlabel('Missing Transverse Energy (GeV)')
ax1.set_ylim([0,3])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('MET for total charge = 2')

ax2.hist(data_met_charge2min, bins=met_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdata3, bins=met_bin,histtype='bar',weights=simweight3,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_xlim([0,300])
ax2.set_xlabel('Missing Transverse Energy (GeV)')
ax2.set_ylim([0,3])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('MET for total charge = -2')

plt.show()
