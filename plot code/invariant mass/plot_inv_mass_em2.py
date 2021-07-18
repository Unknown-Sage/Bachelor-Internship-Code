
simdata = [triboson_inv_mass_em2,top_inv_mass_em2,fake_inv_mass_em2,diboson_inv_mass_em2]
simweight = [triboson_weight_em2,top_weight_em2,fake_weight_em2,diboson_weight_em2]
simdatahigh = [triboson_inv_mass_high_em2,top_inv_mass_high_em2,fake_inv_mass_high_em2,diboson_inv_mass_high_em2]
simweighthigh = [triboson_weight_high_em2,top_weight_high_em2,fake_weight_high_em2,diboson_weight_high_em2]
simdatalow = [triboson_inv_mass_low_em2,top_inv_mass_low_em2,fake_inv_mass_low_em2,diboson_inv_mass_low_em2]
simweightlow = [triboson_weight_low_em2,top_weight_low_em2,fake_weight_low_em2,diboson_weight_low_em2]


fig, (ax1, ax2, ax3) = plt.subplots(1,3)
#fig.suptitle('Invariant Mass for emmm+eeem')
ax1.hist(data_inv_mass_em2, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=inv_mass_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([100,800])
ax1.set_xlabel('invariant mass (GeV)')
ax1.set_ylim([0.4,1000])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Invariant Mass (eemm)')

ax2.hist(data_inv_mass_high_em2, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatahigh, bins=inv_mass_bin,histtype='bar',weights=simweighthigh,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_yscale('log')
ax2.set_xlim([100,800])
ax2.set_xlabel('invariant mass (GeV)')
ax2.set_ylim([0.4,1000])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Invariant Mass (eemm) with MET > 50')

ax3.hist(data_inv_mass_low_em2, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatalow, bins=inv_mass_bin,histtype='bar',weights=simweightlow,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_yscale('log')
ax3.set_xlim([100,800])
ax3.set_xlabel('invariant mass (GeV)')
ax3.set_ylim([0.4,1000])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('Invariant Mass (eemm) with MET < 50')

plt.show()
