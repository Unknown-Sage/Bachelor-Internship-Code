
simdata = [triboson_total_charge,top_total_charge,fake_total_charge,diboson_total_charge]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

simdataem3 = [triboson_total_charge_em3,top_total_charge_em3,fake_total_charge_em3,diboson_total_charge_em3]
simweightem3 = [triboson_weight_em3,top_weight_em3,fake_weight_em3,diboson_weight_em3]


fig, (ax1, ax2) = plt.subplots(1,2)
#fig.suptitle('Total charge distribution')
ax1.hist(data_total_charge,bins=charge_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata,bins=charge_bin, histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([-3,3])
ax1.set_xlabel('elementary charge')
ax1.set_ylim([0.4,1000])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Total Charge Distribution')

ax2.hist(data_total_charge_em3,bins=charge_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdataem3,bins=charge_bin, histtype='bar',weights=simweightem3,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_yscale('log')
ax2.set_xlim([-3,3])
ax2.set_xlabel('elementary charge')
ax2.set_ylim([0.4,1000])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Total Charge Distribution (emmm+eeem)')

plt.show()
