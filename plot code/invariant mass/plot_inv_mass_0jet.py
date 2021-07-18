
simdata = [triboson_inv_mass_0jet,top_inv_mass_0jet,fake_inv_mass_0jet,diboson_inv_mass_0jet]
simweight = [triboson_weight_0jet,top_weight_0jet,fake_weight_0jet,diboson_weight_0jet]
simdatahigh = [triboson_inv_mass_high_0jet,top_inv_mass_high_0jet,fake_inv_mass_high_0jet,diboson_inv_mass_high_0jet]
simweighthigh = [triboson_weight_high_0jet,top_weight_high_0jet,fake_weight_high_0jet,diboson_weight_high_0jet]
simdatalow = [triboson_inv_mass_low_0jet,top_inv_mass_low_0jet,fake_inv_mass_low_0jet,diboson_inv_mass_low_0jet]
simweightlow = [triboson_weight_low_0jet,top_weight_low_0jet,fake_weight_low_0jet,diboson_weight_low_0jet]


fig, (ax1, ax2, ax3 ) = plt.subplots(1,3)
#fig.suptitle('Invariant Mass')
ax1.hist(data_inv_mass_0jet, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=inv_mass_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([100,800])
ax1.set_xlabel('invariant mass (GeV)')
ax1.set_ylim([0.4,2500])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Invariant Mass for 0 jets')

ax2.hist(data_inv_mass_low_0jet, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatalow, bins=inv_mass_bin,histtype='bar',weights=simweightlow,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_yscale('log')
ax2.set_xlim([100,800])
ax2.set_xlabel('invariant mass (GeV)')
ax2.set_ylim([0.4,2500])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Invariant Mass for 0 jets with Missing E_t < 50')

ax3.hist(data_inv_mass_high_0jet, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatahigh, bins=inv_mass_bin,histtype='bar',weights=simweighthigh,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_yscale('log')
ax3.set_xlim([100,800])
ax3.set_xlabel('invariant mass (GeV)')
ax3.set_ylim([0.4,2500])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('Invariant Mass for 0 jets with Missing E_t > 50')

plt.show()
